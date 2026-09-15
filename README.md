# Comparative Evaluation of Lightweight Deep Learning Architectures for Diffusion-Generated Image Detection on Edge Devices

## Overview

This project investigates lightweight deep learning architectures for detecting diffusion-generated images, with a particular focus on **classification performance, model efficiency, quantization behavior, robustness, and edge-oriented deployment**.

The study compares multiple convolutional neural network architectures on a binary classification task:

* **AI-generated images**
* **Real/natural images**

The project evaluates seven architectures:

* MobileNetV4
* EfficientNetV2-S
* ShuffleNetV2
* GhostNet
* MobileNetV3-Small
* ResNet50
* DenseNet121

The evaluation is performed progressively across model training, post-training INT8 quantization, robustness testing, and simulated edge-device inference.

The primary goal is to determine whether lightweight architectures can provide a favorable balance between **classification accuracy, model size, computational efficiency, quantization resilience, and deployment suitability** for diffusion-generated image detection.

---

# Project Status

| Stage                    | Status            |
| ------------------------ | ----------------- |
| Dataset Preprocessing    | Completed         |
| Model Training           | Completed         |
| INT8 Quantization        | Completed         |
| Cross-Dataset Evaluation | Not yet completed |
| Robustness Evaluation    | Completed         |
| Edge-Device Evaluation   | Completed         |

The cross-dataset evaluation stage is currently under development and is intentionally not included in the completed results of this README.

---

# Repository Structure

```text
diffusion-generated-image-detection/
│
├── README.md
│
├── code/
│   ├── 01_dataset_preprocessing/
│   ├── 02_model_training/
│   ├── 03_quantization/
│   ├── 04_cross_dataset_evaluation/
│   ├── 05_robustness_evaluation/
│   └── 06_edge_device_evaluation/
│
└── notebooks/
    ├── 01_dataset_preprocessing/
    ├── 02_model_training/
    ├── 03_quantization/
    ├── 04_cross_dataset_evaluation/
    ├── 05_robustness_evaluation/
    └── 06_edge_device_evaluation/
```

The `code/` directory contains reproducible Python implementations, while the `notebooks/` directory contains corresponding notebook-based workflows.

Large checkpoints, generated datasets, and experiment artifacts are maintained separately from the source repository.

---

# 1. Dataset Preprocessing

## Dataset

The primary dataset used in this study is a subset of the **GenImage** dataset.

The source data used for the project was:

```text
tiny_genimage_data/imagenet_ai_0424_sdv5
```

The experiment uses a controlled subset consisting of:

* **2,500 AI-generated images**
* **2,500 real/natural images**
* **5,000 images total**

The AI-generated images originate from diffusion-generated content, while the real class consists of natural/real images.

---

## Dataset Organization

The final processed dataset is organized as:

```text
dataset_final/
├── train/
│   ├── ai/
│   └── nature/
│
├── val/
│   ├── ai/
│   └── nature/
│
└── test/
    ├── ai/
    └── nature/
```

The dataset is divided using a stratified:

* **70% training**
* **15% validation**
* **15% testing**

split.

### Split Distribution

| Split      |        AI |    Nature |     Total |
| ---------- | --------: | --------: | --------: |
| Train      |     1,750 |     1,750 |     3,500 |
| Validation |       375 |       375 |       750 |
| Test       |       375 |       375 |       750 |
| **Total**  | **2,500** | **2,500** | **5,000** |

All images are converted to:

```text
224 × 224
RGB
```

A `manifest.csv` file is also generated containing:

```text
class
split
original_path
final_path
```

The final test set contains 750 images with the following class mapping:

```text
ai     = 0
nature = 1
```

---

# 2. Model Training

Seven CNN architectures were trained and evaluated on the processed dataset.

## Models

| Model             | Parameters | FP32 Model Size |
| ----------------- | ---------: | --------------: |
| MobileNetV4       |  2,495,586 |         9.85 MB |
| EfficientNetV2-S  | 20,180,050 |        78.16 MB |
| ShuffleNetV2      |  1,255,654 |         4.97 MB |
| GhostNet          |  3,904,070 |        15.21 MB |
| MobileNetV3-Small |  1,519,906 |         6.02 MB |
| ResNet50          | 23,512,130 |        90.03 MB |
| DenseNet121       |  6,955,906 |        27.31 MB |

---

## Training Configuration

The models were trained using ImageNet-pretrained weights with the following configuration:

```text
Input size:       224 × 224
Batch size:       32
Epochs:           100
Optimizer:        Adam
Learning rate:    1e-4
Loss:             CrossEntropyLoss
Early stopping:   Disabled
```

The models were evaluated on the held-out test set after training.

---

## FP32 Results

| Model             | Accuracy | Precision | Recall |     F1 |
| ----------------- | -------: | --------: | -----: | -----: |
| MobileNetV4       |   97.47% |    98.11% | 96.80% | 0.9745 |
| EfficientNetV2-S  |   99.60% |    99.47% | 99.73% | 0.9960 |
| ShuffleNetV2      |   98.53% |    97.89% | 99.20% | 0.9854 |
| GhostNet          |   97.20% |    98.63% | 95.73% | 0.9716 |
| MobileNetV3-Small |   96.13% |    98.06% | 94.13% | 0.9605 |
| ResNet50          |   99.60% |    99.47% | 99.73% | 0.9960 |
| DenseNet121       |   99.60% |   100.00% | 99.20% | 0.9960 |

---

## FP32 Efficiency

The original training/evaluation benchmark also measured model size and inference latency.

| Model             |     Size | Latency |
| ----------------- | -------: | ------: |
| MobileNetV4       |  9.85 MB | 0.70 ms |
| EfficientNetV2-S  | 78.16 MB | 3.75 ms |
| ShuffleNetV2      |  4.97 MB | 0.50 ms |
| GhostNet          | 15.21 MB | 0.89 ms |
| MobileNetV3-Small |  6.02 MB | 0.35 ms |
| ResNet50          | 90.03 MB | 3.54 ms |
| DenseNet121       | 27.31 MB | 2.90 ms |

These latency measurements belong to the original FP32 benchmarking stage and should not be directly interpreted as equivalent to the later simulated edge-device measurements, which were performed under a separate controlled CPU configuration.

---

# 3. INT8 Quantization

Post-training static INT8 quantization was performed to investigate whether the models could be compressed for resource-constrained deployment.

## Quantization Configuration

```text
Quantization:       Static post-training INT8
Calibration:        10 batches
Calibration batch:  32
Input size:         224 × 224
Backend:            FBGEMM when available
```

FX graph-mode quantization was used where supported, with appropriate model preparation and conversion.

The original FP32 checkpoints and original experiment results were kept unchanged.

---

## INT8 Results

| Model             |   Accuracy |         F1 |   INT8 Size | Size Reduction |
| ----------------- | ---------: | ---------: | ----------: | -------------: |
| MobileNetV4       |     64.00% |     0.7284 |     2.91 MB |         70.47% |
| EfficientNetV2-S  |     96.93% |     0.9692 |    22.67 MB |         70.99% |
| ShuffleNetV2      | **98.53%** | **0.9854** | **1.45 MB** |     **70.80%** |
| GhostNet          |     74.93% |     0.6908 |     4.25 MB |         72.06% |
| MobileNetV3-Small |     49.87% |     0.0000 |     1.86 MB |         69.01% |
| ResNet50          |     86.27% |     0.8792 |    22.99 MB |         74.47% |
| DenseNet121       |     91.60% |     0.9091 |     7.80 MB |         71.46% |

---

## Quantization Findings

Static INT8 quantization reduced model storage substantially across all evaluated architectures, with reductions of approximately **69–74%**.

However, the effect of quantization on classification performance was strongly architecture-dependent.

ShuffleNetV2 showed particularly strong quantization resilience:

```text
FP32 accuracy: 98.53%
INT8 accuracy: 98.53%

FP32 F1: 0.9854
INT8 F1: 0.9854
```

Thus, ShuffleNetV2 retained its original test performance while reducing its model size from approximately **4.97 MB to 1.45 MB**.

In contrast, several architectures experienced substantial accuracy degradation after quantization, demonstrating that model compression does not necessarily preserve classification performance equally across architectures.

---

# 4. Cross-Dataset Evaluation

**Status: Not yet completed**

Cross-dataset evaluation is currently under development.

This stage will evaluate the trained models on a dataset or distribution different from the primary training/test dataset in order to investigate generalization beyond the original data distribution.

No cross-dataset results are included in the current project conclusions.

This section will be updated after the experiment has been completed.

---

# 5. Robustness Evaluation

The robustness experiment investigates how well ShuffleNetV2 performs when images are subjected to common image-quality degradations.

The experiment evaluates both the original model and a robustness-trained version.

---

## Corruptions

The following corruptions were evaluated:

* JPEG compression
* Gaussian blur
* Gaussian noise
* Low-resolution input

The baseline evaluation also included clean, unmodified images.

---

## Baseline ShuffleNetV2

The original FP32 ShuffleNetV2 achieved:

| Condition       | Accuracy |     F1 |
| --------------- | -------: | -----: |
| Clean           |   98.53% | 0.9854 |
| JPEG quality 30 |   51.33% | 0.6726 |
| Gaussian blur   |   60.53% | 0.7165 |
| Gaussian noise  |   52.53% | 0.1010 |
| Low resolution  |   54.13% | 0.6856 |

The results show that although the original model performs strongly on clean images, its performance can deteriorate substantially under image degradation.

---

## Robustness Training

A robustness-trained ShuffleNetV2 model was initialized from the original ShuffleNetV2 checkpoint.

Training used:

```text
Training images:     3,500
Validation images:   750
Batch size:          32
Epochs:              15
Learning rate:       1e-5
Optimizer:           Adam
```

Training used standard augmentation together with randomly selected image corruptions.

Approximately 80% of training samples were exposed to one randomly selected corruption.

The best validation checkpoint achieved a clean validation accuracy of approximately **92.80%**.

---

## Robust FP32 Results

| Condition       | Accuracy |     F1 |
| --------------- | -------: | -----: |
| Clean           |   92.80% | 0.9239 |
| JPEG quality 30 |   85.47% | 0.8656 |
| Gaussian blur   |   91.60% | 0.9152 |
| Gaussian noise  |   87.33% | 0.8774 |
| Low resolution  |   87.73% | 0.8835 |

Robustness training substantially improved performance under the tested corruptions, although the clean-image performance was lower than that of the original ShuffleNetV2 model.

---

## Robust INT8 Results

The robustness-trained model was subsequently quantized to INT8.

The resulting INT8 artifact size was:

```text
1.45 MB
```

with approximately:

```text
70.73% storage reduction
```

Results:

| Condition       | Accuracy |     F1 |
| --------------- | -------: | -----: |
| Clean           |   92.00% | 0.9150 |
| JPEG quality 30 |   86.80% | 0.8748 |
| Gaussian blur   |   89.07% | 0.8861 |
| Gaussian noise  |   86.27% | 0.8587 |
| Low resolution  |   87.20% | 0.8763 |

The robustness experiment demonstrates that targeted corruption-based training can substantially improve performance under degraded image conditions.

---

# 6. Edge-Device Evaluation

The edge-device experiment evaluates deployment behavior under a simulated resource-constrained environment.

The evaluation focuses on:

* ShuffleNetV2 INT8
* ResNet50 FP32
* ResNet50 INT8

The experiment uses:

```text
Device:        CPU
CPU threads:   1
Batch size:    1
Input:         224 × 224
Test images:   750
```

The edge experiment was performed as a **CPU simulation**, rather than on a physical edge device.

---

## Edge INT8 Quantization

Both ShuffleNetV2 and ResNet50 were converted into separate INT8 edge artifacts using static post-training quantization.

The original model checkpoints and original result files were treated as read-only.

New edge artifacts were stored separately under:

```text
results/edge_simulation/
```

---

## ShuffleNetV2 INT8 Edge Results

| Metric          |          Result |
| --------------- | --------------: |
| Accuracy        |      **98.53%** |
| Precision       |      **97.89%** |
| Recall          |      **99.20%** |
| F1              |      **0.9854** |
| Model size      |     **1.45 MB** |
| Average latency | 143.85 ms/image |
| Median latency  | 126.99 ms/image |
| P95 latency     | 203.70 ms/image |
| Throughput      | 6.95 images/sec |
| Process memory  |      1715.71 MB |

The edge evaluation confirmed that ShuffleNetV2 INT8 retained the same classification performance as its original FP32 test evaluation.

---

## ResNet50 FP32 Edge Results

| Metric          |          Result |
| --------------- | --------------: |
| Accuracy        |      **99.60%** |
| Precision       |      **99.47%** |
| Recall          |      **99.73%** |
| F1              |      **0.9960** |
| Model size      |        90.00 MB |
| Average latency | 143.56 ms/image |
| Median latency  | 128.37 ms/image |
| P95 latency     | 187.72 ms/image |
| Throughput      | 6.97 images/sec |

---

## ResNet50 INT8 Edge Results

| Metric          |               Result |
| --------------- | -------------------: |
| Accuracy        |               86.27% |
| Precision       |               78.45% |
| Recall          |              100.00% |
| F1              |               0.8792 |
| Model size      |             22.99 MB |
| Average latency |   **86.26 ms/image** |
| Median latency  |   **76.41 ms/image** |
| P95 latency     |  **114.76 ms/image** |
| Throughput      | **11.59 images/sec** |
| Process memory  |           2688.34 MB |

---

## Final INT8 Edge Comparison

| Metric          | ShuffleNetV2 INT8 |   ResNet50 INT8 |
| --------------- | ----------------: | --------------: |
| Accuracy        |        **98.53%** |          86.27% |
| Precision       |        **97.89%** |          78.45% |
| Recall          |            99.20% |     **100.00%** |
| F1              |        **0.9854** |          0.8792 |
| Model size      |       **1.45 MB** |        22.99 MB |
| Average latency |         143.85 ms |    **86.26 ms** |
| Median latency  |         126.99 ms |    **76.41 ms** |
| P95 latency     |         203.70 ms |   **114.76 ms** |
| Throughput      |        6.95 img/s | **11.59 img/s** |
| Process memory  |    **1715.71 MB** |      2688.34 MB |

Compared with ResNet50 INT8, ShuffleNetV2 INT8 achieved:

* **93.69% smaller model size**
* **12.27 percentage points higher accuracy**
* **0.1062 higher F1-score**
* Lower measured process memory

However, ResNet50 INT8 achieved lower latency and higher throughput in this specific CPU simulation.

Therefore, the edge experiment does **not** support the general claim that the smaller model is automatically faster. Instead, it demonstrates a trade-off between model compactness, classification performance, and measured CPU inference performance.

---

# Overall Findings

The completed experiments provide several important observations.

## 1. Lightweight architectures can achieve competitive detection performance

ShuffleNetV2 achieved:

```text
98.53% accuracy
0.9854 F1
```

while using only approximately:

```text
4.97 MB FP32
1.45 MB INT8
```

This makes it particularly attractive for deployment scenarios where storage and memory are constrained.

---

## 2. Quantization behavior is architecture-dependent

INT8 quantization reduced model size substantially across the evaluated architectures, but classification performance did not degrade uniformly.

ShuffleNetV2 demonstrated excellent quantization resilience, while other architectures experienced significant performance losses.

Therefore, selecting a model for edge deployment should consider not only its original FP32 performance but also its behavior after quantization.

---

## 3. Robustness training improves degraded-image performance

The original ShuffleNetV2 model experienced substantial performance degradation under JPEG compression, blur, Gaussian noise, and low-resolution conditions.

Robustness-oriented training substantially improved performance under these corruptions.

This demonstrates the importance of considering real-world image degradation when developing AI-generated image detectors.

---

## 4. Model size and latency are separate deployment considerations

The edge simulation showed that the smaller ShuffleNetV2 INT8 model was not the fastest model under the tested CPU configuration.

ResNet50 INT8 achieved:

```text
86.26 ms/image
11.59 images/sec
```

compared with:

```text
143.85 ms/image
6.95 images/sec
```

for ShuffleNetV2 INT8.

Consequently, deployment decisions should consider the complete resource-performance profile rather than model size alone.

---

## 5. ShuffleNetV2 provides a strong overall edge trade-off

Among the evaluated models, ShuffleNetV2 demonstrates a particularly favorable balance of:

* High classification accuracy
* High F1-score
* Small model footprint
* Strong INT8 quantization resilience
* Lower memory requirements than the larger reference model

Its higher measured latency in the simulated CPU environment remains an important trade-off.

---

# Reproducibility

The project uses a consistent preprocessing and evaluation pipeline across the completed experiments.

### Dataset

```text
5,000 total images
2,500 AI-generated
2,500 real/natural
70/15/15 train/validation/test split
224 × 224 RGB
```

### Training

```text
Batch size: 32
Epochs: 100
Optimizer: Adam
Learning rate: 1e-4
Loss: CrossEntropyLoss
```

### Quantization

```text
Static post-training INT8
Calibration batches: 10
Backend: FBGEMM where available
```

### Edge simulation

```text
CPU
1 CPU thread
Batch size: 1
224 × 224 input
750 test images
```

---

# Output Organization

Generated experiment artifacts are maintained separately from the source code.

The edge-device artifacts follow this structure:

```text
results/
└── edge_simulation/
    ├── artifacts/
    │   ├── shufflenetv2_int8_edge.pth
    │   └── resnet50_int8_edge.pth
    │
    └── results/
        ├── shufflenetv2_edge_inference_results.json
        ├── resnet50_edge_inference_results.json
        ├── resnet50_int8_edge_inference_results.json
        └── final_int8_edge_comparison.json
```

Original model results remain in their respective model directories and were not overwritten by the edge experiments.

---

# Limitations

The current study has several limitations.

1. The primary dataset is a controlled subset rather than the complete GenImage dataset.
2. The current completed evaluation is based primarily on the same dataset distribution used for training and testing.
3. Cross-dataset generalization has not yet been completed.
4. The edge experiment is a simulated CPU evaluation rather than a physical edge-device deployment.
5. CPU latency can depend strongly on hardware, runtime, backend, thread configuration, and implementation.
6. Quantization sensitivity differs substantially between architectures.
7. Robustness training improves corrupted-image performance but can reduce clean-image performance.

The cross-dataset experiment will address an important part of the generalization limitation once completed.

---

# Future Work

The next major stage is **cross-dataset evaluation**.

Planned future work includes:

* Evaluating trained models on an independent image-generation dataset
* Measuring cross-dataset accuracy and F1-score
* Comparing generalization across architectures
* Investigating whether lightweight models maintain their advantage outside the original dataset distribution
* Completing the final comparative analysis across all evaluation stages
* Further investigation of deployment on physical edge hardware

---

# Project Conclusion

The completed experiments indicate that lightweight CNN architectures can provide strong performance for diffusion-generated image detection while substantially reducing model storage requirements.

Among the evaluated architectures, **ShuffleNetV2 stands out as a particularly effective lightweight candidate**. Its FP32 model achieved **98.53% accuracy**, while its INT8 version retained the same accuracy and F1-score with an approximately **70.80% reduction in model size**.

The simulated edge evaluation further reduced the ShuffleNetV2 INT8 artifact to approximately **1.45 MB**, while maintaining **98.53% accuracy**.

The robustness experiment showed that corruption-aware training can significantly improve performance under degraded image conditions.

At the same time, the edge experiment demonstrated that a smaller model is not necessarily faster under every CPU configuration. ResNet50 INT8 achieved lower measured latency and higher throughput in the simulated environment, but at the cost of a substantially larger model footprint, greater memory usage, and significantly lower classification performance after quantization.

Overall, the results support the use of **ShuffleNetV2 as a strong candidate for compact AI-generated image detection**, particularly when model size, memory requirements, and quantization resilience are important deployment considerations.

The remaining cross-dataset evaluation will determine how well these conclusions generalize beyond the original dataset distribution.
