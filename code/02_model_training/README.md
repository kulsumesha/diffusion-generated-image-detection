# Model Training

This stage trains and evaluates multiple CNN-based deep learning architectures for binary classification of **diffusion-generated images (AI)** versus **natural images (nature)**.

The final training pipeline evaluates seven architectures with the same dataset, preprocessing, training configuration, and evaluation metrics to provide a consistent comparison of classification performance and computational characteristics.

---

## Directory Structure

```text
02_model_training/
├── train_pipeline_colab_plots.py
├── model-training-0.ipynb
├── model-training-1.ipynb
├── model-training-2.ipynb
└── model-training-3.ipynb
```

### Files

* **`train_pipeline_colab_plots.py`**
  Main training and evaluation pipeline. It loads a selected pretrained architecture, trains it on the prepared dataset, evaluates it on the test set, measures computational characteristics, and saves the results.

* **`model-training-0.ipynb`**
  Training notebook for:

  * MobileNetV4
  * EfficientNetV2-S

* **`model-training-1.ipynb`**
  Training notebook for:

  * ShuffleNetV2
  * GhostNet

* **`model-training-2.ipynb`**
  Training notebook for:

  * MobileNetV3-Small
  * DenseNet121

* **`model-training-3.ipynb`**
  Training notebook for:

  * ResNet50

The notebooks contain the execution workflow and recorded outputs from the final training runs, while `train_pipeline_colab_plots.py` contains the reusable training and evaluation implementation.

---

## Objective

The purpose of this stage is to train and compare different CNN architectures for detecting whether an input image is:

* **AI** — diffusion-generated image
* **Nature** — natural/real image

The comparison considers both classification performance and model efficiency, including:

* Test accuracy
* Precision
* Recall
* F1-score
* Number of parameters
* Model size
* Average inference latency

These measurements provide a basis for selecting suitable architectures for later quantization, robustness evaluation, and edge-device deployment analysis.

---

## Dataset

The training stage uses the processed dataset generated during the **Dataset Preprocessing** stage.

Expected dataset structure:

```text
dataset_final/
├── train/
│   ├── ai/
│   └── nature/
├── val/
│   ├── ai/
│   └── nature/
└── test/
    ├── ai/
    └── nature/
```

The dataset contains:

* **5,000 total images**
* **2,500 AI-generated images**
* **2,500 natural images**
* Image size: **224 × 224 RGB**
* Train/validation/test split: **70% / 15% / 15%**
* Classes: `ai`, `nature`

---

## Models

Seven CNN architectures are evaluated:

| Model             | Parameters | Model Size |
| ----------------- | ---------: | ---------: |
| MobileNetV4       |  2,495,586 |    9.85 MB |
| EfficientNetV2-S  | 20,180,050 |   78.16 MB |
| ShuffleNetV2      |  1,255,654 |    4.97 MB |
| GhostNet          |  3,904,070 |   15.21 MB |
| MobileNetV3-Small |  1,519,906 |    6.02 MB |
| ResNet50          | 23,512,130 |   90.03 MB |
| DenseNet121       |  6,955,906 |   27.31 MB |

The models are loaded using the `timm` library with pretrained ImageNet weights and adapted for binary classification.

---

## Training Configuration

The final model training experiments use the following configuration:

| Configuration      | Value               |
| ------------------ | ------------------- |
| Image size         | 224 × 224           |
| Batch size         | 32                  |
| Epochs             | 100                 |
| Optimizer          | Adam                |
| Learning rate      | 1 × 10⁻⁴            |
| Loss function      | Cross-Entropy Loss  |
| Pretrained weights | ImageNet            |
| Early stopping     | Disabled            |
| Device             | CUDA when available |

Early stopping was disabled for the final 100-epoch experiments so that all models were trained for the requested number of epochs.

The best validation-loss model state is retained during training and restored after training.

---

## Data Augmentation

Training images are subjected to the following transformations:

1. Resize to **224 × 224**
2. Random horizontal flip
3. Random rotation up to **15°**
4. Random affine transformation:

   * Translation up to 10%
   * Scale range: 0.85–1.15
5. Conversion to tensor
6. ImageNet normalization

Validation and test images use resizing, tensor conversion, and ImageNet normalization without the training augmentations.

---

## Training Workflow

The overall process is:

```text
Prepared Dataset
       ↓
Load Training / Validation / Test Sets
       ↓
Load Pretrained CNN
       ↓
Replace Classification Layer
       ↓
Train for 100 Epochs
       ↓
Track Training & Validation Performance
       ↓
Restore Best Validation Model
       ↓
Evaluate on Test Set
       ↓
Calculate Metrics
       ↓
Measure Parameters / Model Size / Latency
       ↓
Save Results and Plots
```

---

## Evaluation Metrics

Each trained model is evaluated on the held-out test set.

### Classification Metrics

* **Accuracy** — Overall proportion of correctly classified images.
* **Precision** — Proportion of predicted AI images that are actually AI.
* **Recall** — Proportion of actual AI images correctly detected.
* **F1-score** — Harmonic mean of precision and recall.

### Efficiency Metrics

* **Parameters** — Total number of trainable model parameters.
* **Model Size** — Size of the saved model checkpoint.
* **Average Inference Latency** — Average time required to process one image during inference.

The pipeline also generates a **confusion matrix** and training curves for further analysis.

---

## Final Results

The final 100-epoch training results are:

| Model             | Accuracy | Precision | Recall |     F1 | Parameters |     Size | Latency |
| ----------------- | -------: | --------: | -----: | -----: | ---------: | -------: | ------: |
| MobileNetV4       |   0.9747 |    0.9811 | 0.9680 | 0.9745 |  2,495,586 |  9.85 MB | 0.70 ms |
| EfficientNetV2-S  |   0.9960 |    0.9947 | 0.9973 | 0.9960 | 20,180,050 | 78.16 MB | 3.75 ms |
| ShuffleNetV2      |   0.9853 |    0.9789 | 0.9920 | 0.9854 |  1,255,654 |  4.97 MB | 0.50 ms |
| GhostNet          |   0.9720 |    0.9863 | 0.9573 | 0.9716 |  3,904,070 | 15.21 MB | 0.89 ms |
| MobileNetV3-Small |   0.9613 |    0.9806 | 0.9413 | 0.9605 |  1,519,906 |  6.02 MB | 0.35 ms |
| ResNet50          |   0.9960 |    0.9947 | 0.9973 | 0.9960 | 23,512,130 | 90.03 MB | 3.54 ms |
| DenseNet121       |   0.9960 |    1.0000 | 0.9920 | 0.9960 |  6,955,906 | 27.31 MB | 2.90 ms |

---

## Results Summary

The experiments show that **EfficientNetV2-S, ResNet50, and DenseNet121** achieved the highest test accuracy of **0.9960**.

Among the lightweight architectures, **ShuffleNetV2** achieved strong classification performance while maintaining a small computational footprint:

* Accuracy: **0.9853**
* F1-score: **0.9854**
* Parameters: **1.26 million**
* Model size: **4.97 MB**
* Average latency: **0.50 ms/image**

**MobileNetV3-Small** achieved the lowest measured inference latency at **0.35 ms/image**, while also having only **1.52 million parameters** and a **6.02 MB** model size.

The larger architectures generally achieved higher classification performance but required substantially more parameters and storage.

These results are used as the baseline for the subsequent stages of the project, including model quantization, cross-dataset evaluation, robustness evaluation, and edge-device evaluation.

---

## Output Structure

For each model, the pipeline saves its outputs under the corresponding model directory:

```text
results/
├── mobilenetv4/
│   ├── checkpoint.pth
│   ├── results.json
│   └── plots/
│
├── efficientnetv2s/
│   ├── checkpoint.pth
│   ├── results.json
│   └── plots/
│
├── shufflenetv2/
│   ├── checkpoint.pth
│   ├── results.json
│   └── plots/
│
├── ghostnet/
│   ├── checkpoint.pth
│   ├── results.json
│   └── plots/
│
├── mobilenetv3small/
│   ├── checkpoint.pth
│   ├── results.json
│   └── plots/
│
├── resnet50/
│   ├── checkpoint.pth
│   ├── results.json
│   └── plots/
│
└── densenet121/
    ├── checkpoint.pth
    ├── results.json
    └── plots/
```

The exact plot files depend on the outputs generated by the training pipeline.

---

## Results JSON

For each model, `results.json` stores the main training and evaluation information, including:

```text
model
epochs_requested
stopped_early_at_epoch
batch_size
learning_rate
history
test_accuracy
test_precision
test_recall
test_f1
avg_inference_latency_ms
parameters
flops
model_size_mb
confusion_matrix
```

This allows the numerical results to be reused in later analysis without rerunning the training process.

---

## Requirements

The training pipeline requires Python packages including:

```text
torch
torchvision
timm
numpy
scikit-learn
matplotlib
Pillow
thop
```

The experiments are designed to run in a CUDA-enabled environment such as Google Colab when GPU acceleration is available.

---

## Usage

Set the dataset and output directories, then run the training pipeline for the required model.

Example:

```bash
python train_pipeline_colab_plots.py \
    --model shufflenetv2 \
    --data_dir /path/to/dataset_final \
    --output_dir /path/to/results \
    --epochs 100 \
    --batch_size 32 \
    --disable_early_stopping
```

The `--model` argument selects the architecture to train.

Available model identifiers are:

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

## Relation to the Overall Project

This stage establishes the **FP32 baseline models** used for comparison throughout the remainder of the project.

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

The trained checkpoints and recorded baseline metrics from this stage provide the starting point for evaluating the effects of quantization, generalization, robustness, and deployment efficiency.
