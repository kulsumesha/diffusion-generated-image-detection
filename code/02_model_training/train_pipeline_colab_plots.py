"""
train_pipeline.py

ONE reusable pipeline for training + evaluating any of the 5 architectures
on the fixed dataset_final split. Everyone on the team runs this SAME script,
just changing --model, so results are directly comparable.

Usage (run inside Colab, after mounting Drive):
    python train_pipeline.py \
        --model mobilenetv4 \
        --data_dir "/content/drive/MyDrive/diffusion_project/dataset_final" \
        --output_dir "/content/drive/MyDrive/diffusion_project/results" \
        --epochs 10 \
        --batch_size 32

Supported --model values:
    mobilenetv4
    efficientnetv2s
    shufflenetv2
    resnet50
    densenet121

What it does:
  1. Loads train/val/test from data_dir (expects data_dir/train/ai,
     data_dir/train/nature, etc. — exactly what prepare_dataset.py produces)
  2. Builds the chosen model (pretrained via timm, fine-tuned to 2 classes)
  3. Trains for --epochs, tracking train/val loss and accuracy each epoch
  4. Evaluates on the held-out test set: accuracy, precision, recall, F1,
     confusion matrix
  5. Measures parameter count, FLOPs, model size (MB), and inference
     latency (ms/image, averaged over the test set)
  6. Saves: a checkpoint (.pth), a results JSON with every metric above,
     and a confusion matrix image — all into output_dir/<model_name>/
"""

import argparse
import json
import time
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from sklearn.metrics import precision_recall_fscore_support, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

try:
    import timm
except ImportError:
    raise SystemExit("Missing dependency. Run: pip install timm")

try:
    from thop import profile as thop_profile
except ImportError:
    thop_profile = None  # FLOPs counting becomes optional if thop isn't installed


MODEL_MAP = {
    "mobilenetv4": "mobilenetv4_conv_small.e2400_r224_in1k",
    "efficientnetv2s": "tf_efficientnetv2_s.in1k",
    "shufflenetv2": "shufflenetv2_x1_0",  # via torchvision fallback if not in timm
    "resnet50": "resnet50.a1_in1k",
    "densenet121": "densenet121.tv_in1k",
    "mobilenetv3small": "mobilenetv3_small_100.lamb_in1k",
    "ghostnet": "ghostnet_100.in1k",
}

IMG_SIZE = 224


def build_model(model_key: str, num_classes: int = 2):
    timm_name = MODEL_MAP[model_key]
    try:
        model = timm.create_model(timm_name, pretrained=True, num_classes=num_classes)
    except Exception as e:
        # fallback for shufflenetv2 or any model not pulling from timm cleanly
        if model_key == "shufflenetv2":
            from torchvision.models import shufflenet_v2_x1_0
            model = shufflenet_v2_x1_0(weights="DEFAULT")
            model.fc = nn.Linear(model.fc.in_features, num_classes)
        else:
            raise e
    return model


def get_dataloaders(data_dir: str, batch_size: int):
    train_tf = transforms.Compose([
        transforms.Resize((IMG_SIZE, IMG_SIZE)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(degrees=15),
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1), scale=(0.85, 1.15)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    eval_tf = transforms.Compose([
        transforms.Resize((IMG_SIZE, IMG_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    data_dir = Path(data_dir)
    train_ds = datasets.ImageFolder(data_dir / "train", transform=train_tf)
    val_ds = datasets.ImageFolder(data_dir / "val", transform=eval_tf)
    test_ds = datasets.ImageFolder(data_dir / "test", transform=eval_tf)

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, num_workers=2)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False, num_workers=2)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False, num_workers=2)

    return train_loader, val_loader, test_loader, train_ds.classes


def run_epoch(model, loader, criterion, optimizer, device, train: bool):
    model.train() if train else model.eval()
    total_loss, correct, total = 0.0, 0, 0

    torch.set_grad_enabled(train)
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        if train:
            optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        if train:
            loss.backward()
            optimizer.step()

        total_loss += loss.item() * images.size(0)
        preds = outputs.argmax(dim=1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)

    return total_loss / total, correct / total


def evaluate_test_set(model, loader, device):
    model.eval()
    all_preds, all_labels = [], []
    latencies = []

    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device)
            start = time.time()
            outputs = model(images)
            torch.cuda.synchronize() if device.type == "cuda" else None
            elapsed = (time.time() - start) / images.size(0)  # per-image latency
            latencies.append(elapsed * 1000)  # ms

            preds = outputs.argmax(dim=1).cpu().numpy()
            all_preds.extend(preds)
            all_labels.extend(labels.numpy())

    acc = accuracy_score(all_labels, all_preds)
    precision, recall, f1, _ = precision_recall_fscore_support(all_labels, all_preds, average="binary")
    cm = confusion_matrix(all_labels, all_preds)
    avg_latency_ms = sum(latencies) / len(latencies)

    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion_matrix": cm.tolist(),
        "avg_inference_latency_ms": avg_latency_ms,
    }


def get_model_stats(model, device):
    param_count = sum(p.numel() for p in model.parameters())
    dummy_input = torch.randn(1, 3, IMG_SIZE, IMG_SIZE).to(device)

    flops = None
    if thop_profile is not None:
        try:
            flops, _ = thop_profile(model, inputs=(dummy_input,), verbose=False)
        except Exception:
            flops = None

    return {"parameters": param_count, "flops": flops}


def get_model_size_mb(checkpoint_path: Path) -> float:
    return checkpoint_path.stat().st_size / (1024 * 1024)


def save_training_curves(history: dict, output_path: Path):
    """
    Plots train vs val loss and accuracy side by side. A widening gap between
    the two (train improving while val plateaus/worsens) is the visual sign
    of overfitting the advisor asked to check for.
    """
    epochs = range(1, len(history["train_loss"]) + 1)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    axes[0].plot(epochs, history["train_loss"], label="Train Loss", marker="o", markersize=3)
    axes[0].plot(epochs, history["val_loss"], label="Val Loss", marker="o", markersize=3)
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Loss")
    axes[0].set_title("Train vs Validation Loss")
    axes[0].legend()
    axes[0].grid(alpha=0.3)

    axes[1].plot(epochs, history["train_acc"], label="Train Accuracy", marker="o", markersize=3)
    axes[1].plot(epochs, history["val_acc"], label="Val Accuracy", marker="o", markersize=3)
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Accuracy")
    axes[1].set_title("Train vs Validation Accuracy")
    axes[1].legend()
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    plt.close()


def save_confusion_matrix(cm, class_names, output_path: Path):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(cm, cmap="Blues")
    ax.set_xticks(range(len(class_names)))
    ax.set_yticks(range(len(class_names)))
    ax.set_xticklabels(class_names)
    ax.set_yticklabels(class_names)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    for i in range(len(class_names)):
        for j in range(len(class_names)):
            ax.text(j, i, cm[i][j], ha="center", va="center")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    plt.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=list(MODEL_MAP.keys()))
    ap.add_argument("--data_dir", required=True)
    ap.add_argument("--output_dir", required=True)
    ap.add_argument("--epochs", type=int, default=50)
    ap.add_argument("--batch_size", type=int, default=32)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--early_stop_patience", type=int, default=3, help="Stop if val_loss doesn't improve for this many epochs")
    ap.add_argument("--disable_early_stopping", action="store_true",
                     help="Train for the full --epochs regardless of val_loss, to observe true overfitting behavior")
    ap.add_argument("--early_stop_min_delta", type=float, default=0.01)
    args = ap.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    train_loader, val_loader, test_loader, class_names = get_dataloaders(args.data_dir, args.batch_size)
    print(f"Classes: {class_names}")

    model = build_model(args.model).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    history = {"train_loss": [], "train_acc": [], "val_loss": [], "val_acc": []}
    best_val_loss = float("inf")
    best_model_state = None
    epochs_without_improvement = 0
    stopped_early_at = None

    for epoch in range(1, args.epochs + 1):
        train_loss, train_acc = run_epoch(model, train_loader, criterion, optimizer, device, train=True)
        val_loss, val_acc = run_epoch(model, val_loader, criterion, optimizer, device, train=False)

        history["train_loss"].append(train_loss)
        history["train_acc"].append(train_acc)
        history["val_loss"].append(val_loss)
        history["val_acc"].append(val_acc)

        print(f"Epoch {epoch}/{args.epochs} | train_loss={train_loss:.4f} train_acc={train_acc:.4f} "
              f"| val_loss={val_loss:.4f} val_acc={val_acc:.4f}")

        if val_loss < best_val_loss - args.early_stop_min_delta:
            best_val_loss = val_loss
            best_model_state = {k: v.clone() for k, v in model.state_dict().items()}
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1
            if not args.disable_early_stopping and epochs_without_improvement >= args.early_stop_patience:
                stopped_early_at = epoch
                print(f"Early stopping triggered at epoch {epoch} (no val_loss improvement for "
                      f"{args.early_stop_patience} epochs). Restoring best weights from val_loss={best_val_loss:.4f}.")
                break

    if best_model_state is not None:
        model.load_state_dict(best_model_state)

    print("\nEvaluating on test set...")
    test_results = evaluate_test_set(model, test_loader, device)
    model_stats = get_model_stats(model, device)

    output_dir = Path(args.output_dir) / args.model
    output_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_path = output_dir / "checkpoint.pth"
    torch.save(model.state_dict(), checkpoint_path)
    model_size_mb = get_model_size_mb(checkpoint_path)

    save_confusion_matrix(test_results["confusion_matrix"], class_names, output_dir / "confusion_matrix.png")
    save_training_curves(history, output_dir / "training_curves.png")

    results = {
        "model": args.model,
        "epochs_requested": args.epochs,
        "stopped_early_at_epoch": stopped_early_at,
        "batch_size": args.batch_size,
        "learning_rate": args.lr,
        "history": history,
        "test_accuracy": test_results["accuracy"],
        "test_precision": test_results["precision"],
        "test_recall": test_results["recall"],
        "test_f1": test_results["f1"],
        "avg_inference_latency_ms": test_results["avg_inference_latency_ms"],
        "parameters": model_stats["parameters"],
        "flops": model_stats["flops"],
        "model_size_mb": model_size_mb,
        "confusion_matrix": test_results["confusion_matrix"],
    }

    results_path = output_dir / "results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nDone. Results saved to: {results_path}")
    print(f"Checkpoint saved to: {checkpoint_path}")
    print(f"\nSummary — {args.model}:")
    print(f"  Test Accuracy:  {results['test_accuracy']:.4f}")
    print(f"  Test Precision: {results['test_precision']:.4f}")
    print(f"  Test Recall:    {results['test_recall']:.4f}")
    print(f"  Test F1:        {results['test_f1']:.4f}")
    print(f"  Parameters:     {results['parameters']:,}")
    print(f"  Model size:     {results['model_size_mb']:.2f} MB")
    print(f"  Avg latency:    {results['avg_inference_latency_ms']:.2f} ms/image")


if __name__ == "__main__":
    main()
