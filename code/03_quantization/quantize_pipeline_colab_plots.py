"""
quantize_pipeline_colab_plots.py

Applies INT8 post-training STATIC quantization to a trained model's checkpoint,
re-evaluates it on the same test set used in train_pipeline.py, and saves
FP32-vs-INT8 comparison plots into each model's results folder.

No plots are displayed during quantization. Plotting is saved to disk only,
so the quantization run does not spend time rendering/displaying figures.

Supported models:
    mobilenetv4
    efficientnetv2s
    shufflenetv2
    resnet50
    densenet121
    mobilenetv3small
    ghostnet

Usage in Colab:

    !python quantize_pipeline_colab_plots.py \
        --model shufflenetv2 \
        --data_dir "/content/drive/MyDrive/diffusion_project/dataset_final" \
        --results_dir "/content/drive/MyDrive/diffusion_project/results" \
        --batch_size 32 \
        --calibration_batches 10

For all seven models, run the commands individually or in a loop. Each model
writes into results/<model>/ and therefore does not overwrite another model.

Saved files per model:
    results.json              -> existing FP32 training results
    results_int8.json         -> INT8 results + FP32 comparison
    int8_confusion_matrix.png -> INT8 confusion matrix
    fp32_vs_int8_metrics.png  -> FP32 vs INT8 metric comparison
    model_size_comparison.png -> FP32 vs INT8 storage comparison
    latency_comparison.png    -> FP32 vs INT8 latency comparison
"""

import argparse
import copy
import json
import time
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import matplotlib.pyplot as plt

try:
    import timm
except ImportError:
    raise SystemExit("Missing dependency. Run: pip install timm")


MODEL_MAP = {
    "mobilenetv4": "mobilenetv4_conv_small.e2400_r224_in1k",
    "efficientnetv2s": "tf_efficientnetv2_s.in1k",
    "shufflenetv2": "shufflenetv2_x1_0",
    "resnet50": "resnet50.a1_in1k",
    "densenet121": "densenet121.tv_in1k",
    "mobilenetv3small": "mobilenetv3_small_100.lamb_in1k",
    "ghostnet": "ghostnet_100.in1k",
}

IMG_SIZE = 224


def build_model(model_key: str, num_classes: int = 2):
    timm_name = MODEL_MAP[model_key]
    try:
        from timm.layers import set_layer_config
        with set_layer_config(exportable=True):
            model = timm.create_model(
                timm_name,
                pretrained=False,
                num_classes=num_classes
            )
    except Exception as e:
        if model_key == "shufflenetv2":
            from torchvision.models import shufflenet_v2_x1_0
            model = shufflenet_v2_x1_0(weights=None)
            model.fc = nn.Linear(model.fc.in_features, num_classes)
        else:
            raise e
    return model


def get_loaders(data_dir: str, batch_size: int):
    eval_tf = transforms.Compose([
        transforms.Resize((IMG_SIZE, IMG_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        ),
    ])

    data_dir = Path(data_dir)

    train_ds = datasets.ImageFolder(
        data_dir / "train",
        transform=eval_tf
    )
    test_ds = datasets.ImageFolder(
        data_dir / "test",
        transform=eval_tf
    )

    train_loader = DataLoader(
        train_ds,
        batch_size=batch_size,
        shuffle=False,
        num_workers=2
    )
    test_loader = DataLoader(
        test_ds,
        batch_size=batch_size,
        shuffle=False,
        num_workers=2
    )

    return train_loader, test_loader, test_ds.classes


def evaluate(model, loader, device):
    model.eval()
    all_preds, all_labels = [], []
    latencies = []

    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device)

            if device.type == "cuda":
                torch.cuda.synchronize()

            start = time.time()
            outputs = model(images)

            if device.type == "cuda":
                torch.cuda.synchronize()

            elapsed = (time.time() - start) / images.size(0)
            latencies.append(elapsed * 1000)

            preds = outputs.argmax(dim=1).cpu().numpy()
            all_preds.extend(preds)
            all_labels.extend(labels.numpy())

    acc = accuracy_score(all_labels, all_preds)

    precision, recall, f1, _ = precision_recall_fscore_support(
        all_labels,
        all_preds,
        average="binary",
        zero_division=0
    )

    avg_latency_ms = sum(latencies) / len(latencies)

    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "avg_inference_latency_ms": avg_latency_ms,
        "predictions": all_preds,
        "labels": all_labels,
    }


def get_model_size_mb(model, tmp_path: Path) -> float:
    torch.save(model.state_dict(), tmp_path)
    size_mb = tmp_path.stat().st_size / (1024 * 1024)
    tmp_path.unlink()
    return size_mb


class QuantWrapper(nn.Module):
    """
    Eager-mode fallback wrapper used when FX tracing fails.
    """

    def __init__(self, model):
        super().__init__()
        self.quant = torch.quantization.QuantStub()
        self.model = model
        self.dequant = torch.quantization.DeQuantStub()

    def forward(self, x):
        x = self.quant(x)
        x = self.model(x)
        x = self.dequant(x)
        return x


def _quantize_fx_mode(
    model,
    calibration_loader,
    calibration_batches: int,
    device,
    example_input,
    engine
):
    from torch.quantization.quantize_fx import prepare_fx, convert_fx
    from torch.ao.quantization import get_default_qconfig_mapping

    qconfig_mapping = get_default_qconfig_mapping(engine)

    try:
        from timm.layers.squeeze_excite import SqueezeExcite
        qconfig_mapping = qconfig_mapping.set_object_type(
            SqueezeExcite,
            None
        )
        print(
            "Excluding SqueezeExcite layers from INT8 quantization "
            "(kept in FP32)."
        )
    except ImportError:
        pass

    prepared_model = prepare_fx(
        model,
        qconfig_mapping,
        example_input
    )

    with torch.no_grad():
        for i, (images, _) in enumerate(calibration_loader):
            if i >= calibration_batches:
                break
            images = images.to(device)
            prepared_model(images)

    return convert_fx(prepared_model)


def _quantize_eager_mode(
    model,
    calibration_loader,
    calibration_batches: int,
    device,
    engine
):
    wrapped_model = QuantWrapper(model)
    wrapped_model.to(device)
    wrapped_model.qconfig = torch.quantization.get_default_qconfig(engine)

    prepared_model = torch.quantization.prepare(
        wrapped_model,
        inplace=False
    )

    with torch.no_grad():
        for i, (images, _) in enumerate(calibration_loader):
            if i >= calibration_batches:
                break
            images = images.to(device)
            prepared_model(images)

    return torch.quantization.convert(
        prepared_model,
        inplace=False
    )


def static_quantize(
    model,
    calibration_loader,
    calibration_batches: int,
    device,
    example_input
):
    model.eval()
    model.to(device)

    supported = torch.backends.quantized.supported_engines
    print(f"Supported quantized engines on this system: {supported}")

    engine = (
        "fbgemm"
        if "fbgemm" in supported
        else ("qnnpack" if "qnnpack" in supported else supported[0])
    )

    print(f"Using quantized engine: {engine}")
    torch.backends.quantized.engine = engine

    print("Calibrating (attempting FX graph mode quantization)...")

    try:
        return _quantize_fx_mode(
            model,
            calibration_loader,
            calibration_batches,
            device,
            example_input,
            engine
        )

    except Exception as e:
        print(
            f"\nFX graph mode failed "
            f"({type(e).__name__}: {e})."
        )
        print(
            "Falling back to eager-mode quantization "
            "for this architecture...\n"
        )
        print("Calibrating (eager mode)...")

        return _quantize_eager_mode(
            model,
            calibration_loader,
            calibration_batches,
            device,
            engine
        )


def replace_dynamic_padding_convs(model, dummy_input, device):
    """
    Replaces timm Conv2dSame layers with fixed-padding equivalents for the
    fixed 224x224 input used by this project.
    """

    from timm.layers.conv2d_same import Conv2dSame
    from timm.layers.padding import get_same_padding

    captured_shapes = {}
    hooks = []

    def make_hook(name):
        def hook(module, inp):
            captured_shapes[name] = inp[0].shape[-2:]
        return hook

    targets = [
        (name, m)
        for name, m in model.named_modules()
        if isinstance(m, Conv2dSame)
    ]

    if not targets:
        return model

    for name, module in targets:
        hooks.append(
            module.register_forward_pre_hook(make_hook(name))
        )

    model.eval()

    with torch.no_grad():
        model(dummy_input.to(device))

    for h in hooks:
        h.remove()

    replaced_count = 0

    for name, module in targets:
        if name not in captured_shapes:
            continue

        ih, iw = (
            int(s)
            for s in captured_shapes[name]
        )

        kh, kw = module.kernel_size
        sh, sw = module.stride
        dh, dw = module.dilation

        pad_h = get_same_padding(
            ih, kh, sh, dh
        )
        pad_w = get_same_padding(
            iw, kw, sw, dw
        )

        pad_top = pad_h // 2
        pad_bottom = pad_h - pad_top
        pad_left = pad_w // 2
        pad_right = pad_w - pad_left

        new_conv = nn.Conv2d(
            module.in_channels,
            module.out_channels,
            module.kernel_size,
            stride=module.stride,
            padding=0,
            dilation=module.dilation,
            groups=module.groups,
            bias=(module.bias is not None),
        )

        new_conv.weight = module.weight

        if module.bias is not None:
            new_conv.bias = module.bias

        replacement = nn.Sequential(
            nn.ZeroPad2d(
                (
                    pad_left,
                    pad_right,
                    pad_top,
                    pad_bottom
                )
            ),
            new_conv,
        )

        parent_name, _, attr_name = name.rpartition(".")
        parent = (
            model.get_submodule(parent_name)
            if parent_name
            else model
        )

        setattr(parent, attr_name, replacement)
        replaced_count += 1

    print(
        f"Replaced {replaced_count} dynamic-padding "
        f"Conv2dSame layer(s) with static equivalents."
    )

    return model


def save_int8_confusion_matrix(
    model,
    loader,
    device,
    class_names,
    output_path
):
    """
    Evaluates the INT8 model and saves its confusion matrix.
    """

    from sklearn.metrics import confusion_matrix

    result = evaluate(model, loader, device)

    cm = confusion_matrix(
        result["labels"],
        result["predictions"]
    )

    fig, ax = plt.subplots(figsize=(4.5, 4.5))

    ax.imshow(cm, cmap="Blues")

    ax.set_xticks(range(len(class_names)))
    ax.set_yticks(range(len(class_names)))

    ax.set_xticklabels(class_names)
    ax.set_yticklabels(class_names)

    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("INT8 Confusion Matrix")

    for i in range(len(class_names)):
        for j in range(len(class_names)):
            ax.text(
                j,
                i,
                cm[i][j],
                ha="center",
                va="center"
            )

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()

    return result


def save_fp32_vs_int8_metrics_plot(
    fp32_data,
    int8_results,
    output_path
):
    metrics = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1",
    ]

    fp32_values = [
        fp32_data.get("test_accuracy"),
        fp32_data.get("test_precision"),
        fp32_data.get("test_recall"),
        fp32_data.get("test_f1"),
    ]

    int8_values = [
        int8_results.get("test_accuracy"),
        int8_results.get("test_precision"),
        int8_results.get("test_recall"),
        int8_results.get("test_f1"),
    ]

    x = range(len(metrics))
    width = 0.36

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        [i - width / 2 for i in x],
        fp32_values,
        width,
        label="FP32"
    )

    ax.bar(
        [i + width / 2 for i in x],
        int8_values,
        width,
        label="INT8"
    )

    ax.set_xticks(list(x))
    ax.set_xticklabels(metrics)
    ax.set_ylabel("Score")
    ax.set_ylim(0, 1.05)
    ax.set_title("FP32 vs INT8 Performance")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    for i, value in enumerate(fp32_values):
        if value is not None:
            ax.text(
                i - width / 2,
                value + 0.015,
                f"{value:.3f}",
                ha="center",
                fontsize=8
            )

    for i, value in enumerate(int8_values):
        if value is not None:
            ax.text(
                i + width / 2,
                value + 0.015,
                f"{value:.3f}",
                ha="center",
                fontsize=8
            )

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()


def save_model_size_plot(
    fp32_size_mb,
    int8_size_mb,
    size_reduction_pct,
    output_path
):
    labels = ["FP32", "INT8"]
    values = [fp32_size_mb, int8_size_mb]

    fig, ax = plt.subplots(figsize=(6, 5))

    bars = ax.bar(labels, values)

    ax.set_ylabel("Model Size (MB)")
    ax.set_title("FP32 vs INT8 Model Size")

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:.2f} MB",
            ha="center",
            va="bottom"
        )

    if size_reduction_pct is not None:
        ax.text(
            0.5,
            0.92,
            f"Storage reduction: {size_reduction_pct:.2f}%",
            transform=ax.transAxes,
            ha="center"
        )

    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()


def save_latency_plot(
    fp32_latency,
    int8_latency,
    output_path
):
    labels = ["FP32", "INT8"]
    values = [fp32_latency, int8_latency]

    fig, ax = plt.subplots(figsize=(6, 5))

    bars = ax.bar(labels, values)

    ax.set_ylabel("Average Inference Latency (ms/image)")
    ax.set_title("FP32 vs INT8 Inference Latency")

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:.2f} ms",
            ha="center",
            va="bottom"
        )

    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument(
        "--model",
        required=True,
        choices=list(MODEL_MAP.keys())
    )

    ap.add_argument(
        "--data_dir",
        required=True
    )

    ap.add_argument(
        "--results_dir",
        required=True
    )

    ap.add_argument(
        "--batch_size",
        type=int,
        default=32
    )

    ap.add_argument(
        "--calibration_batches",
        type=int,
        default=10
    )

    args = ap.parse_args()

    # Static INT8 quantization is performed on CPU.
    device = torch.device("cpu")

    print(
        f"Using device: {device} "
        f"(INT8 static quantization runs on CPU)"
    )

    model_dir = Path(args.results_dir) / args.model

    checkpoint_path = model_dir / "checkpoint.pth"
    fp32_results_path = model_dir / "results.json"

    if not checkpoint_path.exists():
        raise SystemExit(
            f"No FP32 checkpoint found at {checkpoint_path}. "
            f"Run train_pipeline.py for --model "
            f"{args.model} first."
        )

    if not fp32_results_path.exists():
        raise SystemExit(
            f"No FP32 results.json found at "
            f"{fp32_results_path}."
        )

    print(
        f"Loading FP32 checkpoint: {checkpoint_path}"
    )

    model = build_model(args.model)

    raw_state_dict = torch.load(
        checkpoint_path,
        map_location=device
    )

    clean_state_dict = {
        k: v
        for k, v in raw_state_dict.items()
        if not k.endswith("total_ops")
        and not k.endswith("total_params")
    }

    model.load_state_dict(clean_state_dict)

    dummy_input = torch.randn(
        1,
        3,
        IMG_SIZE,
        IMG_SIZE
    ).to(device)

    model = replace_dynamic_padding_convs(
        model,
        dummy_input,
        device
    )

    train_loader, test_loader, class_names = get_loaders(
        args.data_dir,
        args.batch_size
    )

    print(f"Classes: {class_names}")

    print(
        "\nApplying INT8 static quantization "
        "(Conv2d + Linear layers)..."
    )

    example_input = torch.randn(
        1,
        3,
        IMG_SIZE,
        IMG_SIZE
    ).to(device)

    quantized_model = static_quantize(
        copy.deepcopy(model),
        train_loader,
        args.calibration_batches,
        device,
        example_input
    )

    print("\nEvaluating INT8 model on test set...")

    int8_results_raw = evaluate(
        quantized_model,
        test_loader,
        device
    )

    tmp_checkpoint = (
        model_dir / "checkpoint_int8_tmp.pth"
    )

    int8_size_mb = get_model_size_mb(
        quantized_model,
        tmp_checkpoint
    )

    with open(fp32_results_path) as f:
        fp32_data = json.load(f)

    fp32_size_mb = fp32_data.get("model_size_mb")
    fp32_accuracy = fp32_data.get("test_accuracy")
    fp32_precision = fp32_data.get("test_precision")
    fp32_recall = fp32_data.get("test_recall")
    fp32_f1 = fp32_data.get("test_f1")
    fp32_latency = fp32_data.get(
        "avg_inference_latency_ms"
    )

    size_reduction_pct = (
        round(
            (1 - int8_size_mb / fp32_size_mb) * 100,
            2
        )
        if fp32_size_mb
        else None
    )

    accuracy_change = (
        round(
            int8_results_raw["accuracy"] - fp32_accuracy,
            4
        )
        if fp32_accuracy is not None
        else None
    )

    # Save INT8 confusion matrix.
    int8_confusion_path = (
        model_dir / "int8_confusion_matrix.png"
    )

    save_int8_confusion_matrix(
        quantized_model,
        test_loader,
        device,
        class_names,
        int8_confusion_path
    )

    # Save FP32-vs-INT8 performance plot.
    save_fp32_vs_int8_metrics_plot(
        fp32_data,
        {
            "test_accuracy": int8_results_raw["accuracy"],
            "test_precision": int8_results_raw["precision"],
            "test_recall": int8_results_raw["recall"],
            "test_f1": int8_results_raw["f1"],
        },
        model_dir / "fp32_vs_int8_metrics.png"
    )

    # Save FP32-vs-INT8 model storage plot.
    save_model_size_plot(
        fp32_size_mb,
        int8_size_mb,
        size_reduction_pct,
        model_dir / "model_size_comparison.png"
    )

    # Save FP32-vs-INT8 latency plot.
    save_latency_plot(
        fp32_latency,
        int8_results_raw["avg_inference_latency_ms"],
        model_dir / "latency_comparison.png"
    )

    results = {
        "model": args.model,
        "quantization": (
            "INT8 static (post-training, "
            "Conv2d + Linear)"
        ),
        "calibration_batches": args.calibration_batches,

        "test_accuracy": int8_results_raw["accuracy"],
        "test_precision": int8_results_raw["precision"],
        "test_recall": int8_results_raw["recall"],
        "test_f1": int8_results_raw["f1"],

        "avg_inference_latency_ms": (
            int8_results_raw[
                "avg_inference_latency_ms"
            ]
        ),

        "model_size_mb": int8_size_mb,

        "fp32_model_size_mb": fp32_size_mb,
        "fp32_test_accuracy": fp32_accuracy,
        "fp32_test_precision": fp32_precision,
        "fp32_test_recall": fp32_recall,
        "fp32_test_f1": fp32_f1,
        "fp32_avg_inference_latency_ms": fp32_latency,

        "size_reduction_pct": size_reduction_pct,
        "accuracy_change": accuracy_change,

        "saved_plots": {
            "int8_confusion_matrix": str(
                int8_confusion_path
            ),
            "fp32_vs_int8_metrics": str(
                model_dir / "fp32_vs_int8_metrics.png"
            ),
            "model_size_comparison": str(
                model_dir / "model_size_comparison.png"
            ),
            "latency_comparison": str(
                model_dir / "latency_comparison.png"
            ),
        },
    }

    int8_results_path = (
        model_dir / "results_int8.json"
    )

    with open(int8_results_path, "w") as f:
        json.dump(results, f, indent=2)

    print(
        f"\nDone. INT8 results saved to: "
        f"{int8_results_path}"
    )

    print(
        f"Plots saved in: {model_dir}"
    )

    print(
        f"\nSummary — {args.model} (INT8):"
    )

    print(
        f"  Test Accuracy:  "
        f"{results['test_accuracy']:.4f} "
        f"(FP32 was: {fp32_accuracy})"
    )

    print(
        f"  Test Precision: "
        f"{results['test_precision']:.4f} "
        f"(FP32 was: {fp32_precision})"
    )

    print(
        f"  Test Recall:    "
        f"{results['test_recall']:.4f} "
        f"(FP32 was: {fp32_recall})"
    )

    print(
        f"  Test F1:        "
        f"{results['test_f1']:.4f} "
        f"(FP32 was: {fp32_f1})"
    )

    print(
        f"  Model size:     "
        f"{results['model_size_mb']:.2f} MB "
        f"(FP32 was: {fp32_size_mb} MB, "
        f"{results['size_reduction_pct']}% smaller)"
    )

    print(
        f"  Avg latency:    "
        f"{results['avg_inference_latency_ms']:.2f} "
        f"ms/image (CPU)"
    )

    print("\nSaved plot files:")
    print(
        f"  - {model_dir / 'int8_confusion_matrix.png'}"
    )
    print(
        f"  - {model_dir / 'fp32_vs_int8_metrics.png'}"
    )
    print(
        f"  - {model_dir / 'model_size_comparison.png'}"
    )
    print(
        f"  - {model_dir / 'latency_comparison.png'}"
    )


if __name__ == "__main__":
    main()
