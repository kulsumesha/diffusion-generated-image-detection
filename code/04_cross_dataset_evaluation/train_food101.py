import argparse
import json
import os
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from PIL import Image
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from torch.utils.data import DataLoader, Dataset
from torchvision import models as tv_models
from torchvision import transforms

import timm


# ============================================================
# Paths
# ============================================================

FOOD_BASE = Path("/content/drive_b/MyDrive/Food101_Edge_Experiment")
DATA_DIR = FOOD_BASE / "food-101"
RESULTS_DIR = FOOD_BASE / "results"


# ============================================================
# Configuration
# ============================================================

NUM_CLASSES = 101
IMAGE_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 30
LEARNING_RATE = 1e-4
NUM_WORKERS = 2

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]


# ============================================================
# Model definitions
# ============================================================

TIMM_MODEL_NAMES = {
    "mobilenetv4": "mobilenetv4_conv_small.e2400_r224_in1k",
    "efficientnetv2s": "tf_efficientnetv2_s.in1k",
    "ghostnet": "ghostnet_100.in1k",
    "mobilenetv3small": "mobilenetv3_small_100",
    "resnet50": "resnet50.a1_in1k",
    "densenet121": "densenet121.ra_in1k",
}


def create_model(model_name):
    if model_name == "shufflenetv2":
        model = tv_models.shufflenet_v2_x1_0(weights="DEFAULT")

        in_features = model.fc.in_features
        model.fc = nn.Linear(in_features, NUM_CLASSES)

        return model

    timm_name = TIMM_MODEL_NAMES[model_name]

    model = timm.create_model(
        timm_name,
        pretrained=True,
        num_classes=NUM_CLASSES,
    )

    return model


# ============================================================
# Food-101 Dataset
# ============================================================

class Food101Dataset(Dataset):
    def __init__(self, root_dir, split, transform=None):
        self.root_dir = Path(root_dir)
        self.transform = transform

        meta_dir = self.root_dir / "meta"
        images_dir = self.root_dir / "images"

        class_file = meta_dir / "classes.txt"
        split_file = meta_dir / f"{split}.txt"

        self.classes = [
            line.strip()
            for line in class_file.read_text().splitlines()
            if line.strip()
        ]

        self.class_to_idx = {
            class_name: idx
            for idx, class_name in enumerate(self.classes)
        }

        self.samples = []

        for line in split_file.read_text().splitlines():
            line = line.strip()

            if not line:
                continue

            class_name, image_id = line.rsplit("/", 1)

            image_path = images_dir / class_name / f"{image_id}.jpg"

            label = self.class_to_idx[class_name]

            self.samples.append((image_path, label))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        image_path, label = self.samples[index]

        image = Image.open(image_path).convert("RGB")

        if self.transform is not None:
            image = self.transform(image)

        return image, label


# ============================================================
# Data transforms
# ============================================================

def get_transforms():
    train_transform = transforms.Compose([
        transforms.RandomResizedCrop(IMAGE_SIZE),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])

    test_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(IMAGE_SIZE),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])

    return train_transform, test_transform


# ============================================================
# Training
# ============================================================

def train_one_epoch(model, loader, criterion, optimizer, device):
    model.train()

    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()

        outputs = model(images)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)

        predictions = outputs.argmax(dim=1)

        correct += (predictions == labels).sum().item()
        total += labels.size(0)

    epoch_loss = running_loss / total
    epoch_accuracy = correct / total

    return epoch_loss, epoch_accuracy


# ============================================================
# Evaluation
# ============================================================

@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()

    running_loss = 0.0
    all_predictions = []
    all_labels = []

    for images, labels in loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)

        outputs = model(images)
        loss = criterion(outputs, labels)

        running_loss += loss.item() * images.size(0)

        predictions = outputs.argmax(dim=1)

        all_predictions.extend(predictions.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

    total = len(all_labels)

    loss = running_loss / total

    accuracy = accuracy_score(all_labels, all_predictions)

    precision = precision_score(
        all_labels,
        all_predictions,
        average="macro",
        zero_division=0,
    )

    recall = recall_score(
        all_labels,
        all_predictions,
        average="macro",
        zero_division=0,
    )

    f1 = f1_score(
        all_labels,
        all_predictions,
        average="macro",
        zero_division=0,
    )

    return {
        "loss": loss,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


# ============================================================
# CPU latency
# ============================================================

@torch.no_grad()
def measure_cpu_latency(model, sample):
    torch.set_num_threads(1)

    model = model.to("cpu")
    model.eval()

    sample = sample.to("cpu")

    for _ in range(10):
        _ = model(sample)

    latencies = []

    for _ in range(100):
        start = time.perf_counter()

        _ = model(sample)

        end = time.perf_counter()

        latencies.append((end - start) * 1000)

    latencies = np.array(latencies)

    return {
        "mean_ms": float(np.mean(latencies)),
        "median_ms": float(np.median(latencies)),
        "p95_ms": float(np.percentile(latencies, 95)),
        "throughput_images_per_second": float(
            1000.0 / np.mean(latencies)
        ),
    }


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--model",
        required=True,
        choices=[
            "mobilenetv4",
            "efficientnetv2s",
            "shufflenetv2",
            "ghostnet",
            "mobilenetv3small",
            "resnet50",
            "densenet121",
        ],
    )

    args = parser.parse_args()

    model_name = args.model

    result_dir = RESULTS_DIR / model_name
    result_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_path = result_dir / "checkpoint.pth"
    history_path = result_dir / "training_history.json"
    results_path = result_dir / "results.json"

    print("=" * 70)
    print(f"Food-101 training: {model_name}")
    print("=" * 70)

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print(f"Device: {device}")

    train_transform, test_transform = get_transforms()

    train_dataset = Food101Dataset(
        DATA_DIR,
        "train",
        transform=train_transform,
    )

    test_dataset = Food101Dataset(
        DATA_DIR,
        "test",
        transform=test_transform,
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=torch.cuda.is_available(),
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=torch.cuda.is_available(),
    )

    print(f"Classes: {len(train_dataset.classes)}")
    print(f"Training images: {len(train_dataset)}")
    print(f"Test images: {len(test_dataset)}")

    model = create_model(model_name)

    model = model.to(device)

    total_params = sum(
        parameter.numel()
        for parameter in model.parameters()
    )

    trainable_params = sum(
        parameter.numel()
        for parameter in model.parameters()
        if parameter.requires_grad
    )

    print(f"Total parameters: {total_params:,}")
    print(f"Trainable parameters: {trainable_params:,}")

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=LEARNING_RATE,
    )

    history = []

    best_test_accuracy = 0.0

    for epoch in range(1, EPOCHS + 1):
        start_time = time.time()

        train_loss, train_accuracy = train_one_epoch(
            model,
            train_loader,
            criterion,
            optimizer,
            device,
        )

        test_metrics = evaluate(
            model,
            test_loader,
            criterion,
            device,
        )

        epoch_time = time.time() - start_time

        epoch_result = {
            "epoch": epoch,
            "train_loss": train_loss,
            "train_accuracy": train_accuracy,
            "test_loss": test_metrics["loss"],
            "test_accuracy": test_metrics["accuracy"],
            "test_precision": test_metrics["precision"],
            "test_recall": test_metrics["recall"],
            "test_f1": test_metrics["f1"],
            "epoch_time_seconds": epoch_time,
        }

        history.append(epoch_result)

        print(
            f"Epoch {epoch:02d}/{EPOCHS} | "
            f"Train Acc: {train_accuracy:.4f} | "
            f"Test Acc: {test_metrics['accuracy']:.4f} | "
            f"F1: {test_metrics['f1']:.4f} | "
            f"Time: {epoch_time:.1f}s"
        )

        if test_metrics["accuracy"] > best_test_accuracy:
            best_test_accuracy = test_metrics["accuracy"]

    # --------------------------------------------------------
    # Final evaluation
    # --------------------------------------------------------

    final_metrics = evaluate(
        model,
        test_loader,
        criterion,
        device,
    )

    # --------------------------------------------------------
    # Save checkpoint
    # --------------------------------------------------------

    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "model_name": model_name,
            "num_classes": NUM_CLASSES,
            "image_size": IMAGE_SIZE,
            "epochs": EPOCHS,
            "batch_size": BATCH_SIZE,
            "learning_rate": LEARNING_RATE,
        },
        checkpoint_path,
    )

    # --------------------------------------------------------
    # Save training history
    # --------------------------------------------------------

    with open(history_path, "w") as f:
        json.dump(history, f, indent=2)

    # --------------------------------------------------------
    # Model size
    # --------------------------------------------------------

    model_size_mb = checkpoint_path.stat().st_size / (
        1024 * 1024
    )

    # --------------------------------------------------------
    # CPU latency
    # --------------------------------------------------------

    sample_image, _ = test_dataset[0]

    latency = measure_cpu_latency(
        model,
        sample_image.unsqueeze(0),
    )

    # --------------------------------------------------------
    # Final results
    # --------------------------------------------------------

    results = {
        "dataset": "Food-101",
        "model": model_name,
        "num_classes": NUM_CLASSES,
        "train_images": len(train_dataset),
        "test_images": len(test_dataset),
        "epochs": EPOCHS,
        "batch_size": BATCH_SIZE,
        "learning_rate": LEARNING_RATE,
        "image_size": IMAGE_SIZE,
        "total_parameters": total_params,
        "trainable_parameters": trainable_params,
        "checkpoint_size_mb": model_size_mb,
        "best_test_accuracy": best_test_accuracy,
        "final_test_metrics": final_metrics,
        "cpu_latency": latency,
    }

    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)

    print()
    print("=" * 70)
    print("Training complete")
    print("=" * 70)
    print(f"Model: {model_name}")
    print(f"Final accuracy: {final_metrics['accuracy']:.4f}")
    print(f"Final precision: {final_metrics['precision']:.4f}")
    print(f"Final recall: {final_metrics['recall']:.4f}")
    print(f"Final F1: {final_metrics['f1']:.4f}")
    print(f"Parameters: {total_params:,}")
    print(f"Checkpoint size: {model_size_mb:.2f} MB")
    print(f"CPU latency: {latency['mean_ms']:.2f} ms/image")
    print(
        f"CPU throughput: "
        f"{latency['throughput_images_per_second']:.2f} images/s"
    )
    print(f"Results: {results_path}")


if __name__ == "__main__":
    main()