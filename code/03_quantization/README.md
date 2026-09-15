# Quantization

This stage applies **post-training static INT8 quantization** to the trained FP32 models and evaluates the resulting quantized models on the same test dataset used during model training.

The objective is to investigate the trade-off between model compression and classification performance, with particular attention to storage reduction and the suitability of the models for resource-constrained and edge-device deployment.

---

## Directory Structure

```text
03_quantization/
├── quantize_pipeline_colab_plots.py
├── quantization.ipynb
└── README.md
```

### Files

* **`quantize_pipeline_colab_plots.py`**
  Main quantization and evaluation pipeline. It loads a trained FP32 checkpoint, applies static INT8 post-training quantization, evaluates the quantized model, compares it with the original FP32 model, and saves the resulting metrics and plots.

* **`quantization.ipynb`**
  Jupyter/Google Colab notebook containing the execution of the quantization pipeline for all seven trained models.

* **`README.md`**
  Documentation for the quantization stage.

---

## Objective

The purpose of this stage is to evaluate the effect of **INT8 post-training static quantization** on the seven trained CNN architectures.

The quantization process aims to:

* Reduce model storage requirements
* Convert supported model operations to INT8
* Measure the effect of quantization on classification performance
* Compare FP32 and INT8 model sizes
* Compare FP32 and INT8 inference latency
* Identify architectures that maintain good accuracy after quantization

The resulting INT8 models are evaluated using the same binary classification task:

* **AI** — diffusion-generated images
* **Nature** — natural/real images

---

## Input

The quantization pipeline uses the trained model checkpoints produced during the **Model Training** stage.

For each model, the following files are expected inside its results directory:

```text
results/
└── <model>/
    ├── checkpoint.pth
    └── results.json
```

The pipeline loads:

* `checkpoint.pth` — trained FP32 model weights
* `results.json` — original FP32 evaluation results

The prepared dataset from the Dataset Preprocessing stage is also required.

---

## Supported Models

The pipeline supports all seven models used during model training:

```text
mobilenetv4
efficientnetv2s
shufflenetv2
resnet50
densenet121
mobilenetv3small
ghostnet
```

---

## Quantization Method

The pipeline applies **INT8 static post-training quantization**.

The quantization workflow is:

```text
Trained FP32 Checkpoint
          ↓
Load Model
          ↓
Prepare Fixed 224×224 Input
          ↓
Load Calibration Data
          ↓
FX Graph-Mode Quantization
          ↓
Calibration
          ↓
INT8 Conversion
          ↓
INT8 Test Evaluation
          ↓
FP32 vs INT8 Comparison
          ↓
Save Metrics and Plots
```

The pipeline attempts **FX graph-mode quantization** first.

If FX graph-mode quantization fails for a particular architecture, the pipeline falls back to **eager-mode quantization**.

The quantization targets supported **Conv2d and Linear layers**, while Squeeze-and-Excitation layers are excluded from INT8 quantization when applicable and remain in FP32.

---

## Calibration

Static quantization requires calibration data to determine appropriate quantization parameters.

The training dataset is used as the calibration dataset.

The default configuration uses:

* Batch size: **32**
* Calibration batches: **10**

Calibration is performed before converting the prepared model to INT8.

---

## Quantization Environment

Static INT8 quantization is performed on the **CPU**.

The pipeline automatically checks the available PyTorch quantization engines and selects:

1. `fbgemm` when available
2. `qnnpack` when `fbgemm` is unavailable
3. Otherwise, the first supported engine

The quantized model is then evaluated on the CPU.

---

## Evaluation

The INT8 model is evaluated using:

* Test accuracy
* Test precision
* Test recall
* Test F1-score
* Average inference latency
* Model size

The pipeline also compares the INT8 results against the original FP32 results.

---

## Final Results

The final quantization experiments were performed on all seven models.

| Model             | FP32 Accuracy | INT8 Accuracy | FP32 Size | INT8 Size | Storage Reduction | INT8 Latency |
| ----------------- | ------------: | ------------: | --------: | --------: | ----------------: | -----------: |
| MobileNetV4       |        0.9747 |        0.6400 |   9.85 MB |   2.91 MB |            70.47% |     12.98 ms |
| EfficientNetV2-S  |        0.9960 |        0.9693 |  78.16 MB |  22.67 MB |            70.99% |    162.13 ms |
| ShuffleNetV2      |        0.9853 |        0.9853 |   4.97 MB |   1.45 MB |            70.80% |    151.04 ms |
| GhostNet          |        0.9720 |        0.7493 |  15.21 MB |   4.25 MB |            72.06% |    154.27 ms |
| MobileNetV3-Small |        0.9613 |        0.4987 |   6.02 MB |   1.86 MB |            69.01% |     10.24 ms |
| ResNet50          |        0.9960 |        0.8627 |  90.03 MB |  22.99 MB |            74.47% |     73.07 ms |
| DenseNet121       |        0.9960 |        0.9160 |  27.31 MB |   7.80 MB |            71.46% |    118.01 ms |

---

## INT8 Performance

### MobileNetV4

* Accuracy: **0.6400**
* Precision: **0.5848**
* Recall: **0.9653**
* F1-score: **0.7284**
* Model size: **2.91 MB**
* Storage reduction: **70.47%**
* Average CPU latency: **12.98 ms/image**

Quantization substantially reduced classification performance while providing a large reduction in model size.

### EfficientNetV2-S

* Accuracy: **0.9693**
* Precision: **0.9731**
* Recall: **0.9653**
* F1-score: **0.9692**
* Model size: **22.67 MB**
* Storage reduction: **70.99%**
* Average CPU latency: **162.13 ms/image**

EfficientNetV2-S retained relatively strong classification performance after quantization while reducing its model size by approximately 71%.

### ShuffleNetV2

* Accuracy: **0.9853**
* Precision: **0.9789**
* Recall: **0.9920**
* F1-score: **0.9854**
* Model size: **1.45 MB**
* Storage reduction: **70.80%**
* Average CPU latency: **151.04 ms/image**

ShuffleNetV2 retained its FP32 classification performance after INT8 quantization. Its accuracy remained **0.9853**, while its model size decreased from **4.97 MB to 1.45 MB**.

This makes ShuffleNetV2 an important candidate for subsequent resource-constrained and edge-device evaluation.

### GhostNet

* Accuracy: **0.7493**
* Precision: **0.9013**
* Recall: **0.5600**
* F1-score: **0.6908**
* Model size: **4.25 MB**
* Storage reduction: **72.06%**
* Average CPU latency: **154.27 ms/image**

GhostNet achieved a substantial reduction in model size, but classification performance decreased considerably after quantization.

### MobileNetV3-Small

* Accuracy: **0.4987**
* Precision: **0.0000**
* Recall: **0.0000**
* F1-score: **0.0000**
* Model size: **1.86 MB**
* Storage reduction: **69.01%**
* Average CPU latency: **10.24 ms/image**

MobileNetV3-Small achieved a large reduction in model size, but its classification performance degraded substantially after INT8 quantization.

### ResNet50

* Accuracy: **0.8627**
* Precision: **0.7845**
* Recall: **1.0000**
* F1-score: **0.8792**
* Model size: **22.99 MB**
* Storage reduction: **74.47%**
* Average CPU latency: **73.07 ms/image**

ResNet50 achieved the largest storage reduction among the evaluated models, but experienced a noticeable reduction in classification performance.

### DenseNet121

* Accuracy: **0.9160**
* Precision: **0.9906**
* Recall: **0.8400**
* F1-score: **0.9091**
* Model size: **7.80 MB**
* Storage reduction: **71.46%**
* Average CPU latency: **118.01 ms/image**

DenseNet121 retained relatively high precision after quantization but experienced a reduction in recall and overall accuracy.

---

## Key Findings

The quantization experiments demonstrate that INT8 quantization provides a substantial reduction in model storage across all seven architectures.

The storage reduction ranged from approximately **69% to 74%**.

However, the effect on classification performance was architecture-dependent.

**ShuffleNetV2 produced the strongest overall quantization result**, maintaining the same test accuracy and F1-score as its FP32 model while reducing its storage requirement by **70.80%**.

In contrast, several architectures experienced substantial accuracy degradation after quantization. This demonstrates that successful post-training quantization depends on the architecture and cannot be evaluated solely from model-size reduction.

---

## Output Files

For each model, the quantization pipeline saves the results inside the corresponding model directory:

```text
results/
└── <model>/
    ├── checkpoint.pth
    ├── results.json
    ├── results_int8.json
    ├── int8_confusion_matrix.png
    ├── fp32_vs_int8_metrics.png
    ├── model_size_comparison.png
    └── latency_comparison.png
```

### `results_int8.json`

This file stores the INT8 evaluation results together with the corresponding FP32 baseline information.

It contains:

```text
model
quantization
calibration_batches
test_accuracy
test_precision
test_recall
test_f1
avg_inference_latency_ms
model_size_mb
fp32_model_size_mb
fp32_test_accuracy
fp32_test_precision
fp32_test_recall
fp32_test_f1
fp32_avg_inference_latency_ms
size_reduction_pct
accuracy_change
saved_plots
```

### Generated Plots

The pipeline generates four visualizations:

* **`int8_confusion_matrix.png`** — Confusion matrix for the INT8 model.
* **`fp32_vs_int8_metrics.png`** — Comparison of FP32 and INT8 accuracy, precision, recall, and F1-score.
* **`model_size_comparison.png`** — Comparison of FP32 and INT8 model storage.
* **`latency_comparison.png`** — Comparison of FP32 and INT8 inference latency.

---

## Usage

The quantization pipeline is executed separately for each model.

Example:

```bash
python quantize_pipeline_colab_plots.py \
    --model efficientnetv2s \
    --data_dir "/content/drive/MyDrive/diffusion_project/dataset_final" \
    --results_dir "/content/drive/MyDrive/diffusion_project/results" \
    --batch_size 32 \
    --calibration_batches 10
```

The same command structure is used for all seven models by changing the `--model` argument.

Example model identifiers:

```text
mobilenetv4
efficientnetv2s
shufflenetv2
ghostnet
mobilenetv3small
resnet50
densenet121
```

---

## Requirements

The pipeline requires Python packages including:

```text
torch
torchvision
timm
scikit-learn
matplotlib
```

The quantization process uses PyTorch's quantization functionality and requires a CPU environment with a supported quantization backend.

---

## Relation to the Overall Project

The quantization stage follows the FP32 model training stage and provides compressed INT8 versions of the trained models.

```text
01 Dataset Preprocessing
          ↓
02 Model Training
          ↓
03 Quantization
          ↓
04 Cross-Dataset Evaluation
          ↓
05 Robustness Evaluation
          ↓
06 Edge-Device Evaluation
```

The FP32 and INT8 results generated here provide the basis for determining which models are appropriate for subsequent evaluation under cross-dataset, robustness, and edge-device conditions.
