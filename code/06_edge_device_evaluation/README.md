# 06 — Edge Device Evaluation

## Overview

This stage evaluates the deployment behavior of selected diffusion-generated image detection models under a simulated resource-constrained edge environment.

The evaluation focuses on two architectures:

* **ShuffleNetV2** — lightweight architecture designed for efficient deployment
* **ResNet50** — comparatively heavyweight convolutional architecture used as a reference model

Both models were evaluated on the same GenImage test set using:

* CPU-only inference
* Single CPU thread
* Batch size of 1
* 224 × 224 RGB input
* Single-image inference
* FP32 and INT8 model variants where applicable

The purpose of this experiment is to evaluate the trade-off between model size, classification performance, latency, throughput, and memory usage for edge-oriented deployment.

---

## Experimental Setup

### Dataset

The experiment uses the test split of the preprocessed GenImage dataset created during the dataset preprocessing stage.

| Property         | Value                  |
| ---------------- | ---------------------- |
| Dataset          | GenImage               |
| Test images      | 750                    |
| Classes          | `ai`, `nature`         |
| Class mapping    | `ai = 0`, `nature = 1` |
| Input resolution | 224 × 224              |
| Input format     | RGB                    |
| Batch size       | 1                      |

The same test dataset and evaluation preprocessing were used for the models to ensure a consistent comparison.

### Simulated Edge Environment

The edge-device environment was simulated by restricting inference to CPU execution with a single CPU thread.

| Configuration       | Value                     |
| ------------------- | ------------------------- |
| Device              | CPU                       |
| CPU threads         | 1                         |
| Batch size          | 1                         |
| Input size          | 224 × 224                 |
| Inference mode      | Single-image              |
| Quantization        | Static post-training INT8 |
| Quantization engine | FBGEMM                    |

The experiment was executed in a Google Colab environment using a Tesla T4 runtime, but the edge inference itself was performed on the CPU rather than the GPU.

---

## Models Evaluated

### ShuffleNetV2

ShuffleNetV2 was selected as the lightweight architecture because of its low parameter count and small storage footprint.

The original FP32 model was loaded from the existing training checkpoint. A separate INT8 model was generated specifically for the edge experiment using static post-training quantization.

The original checkpoint and original experiment results were kept read-only.

### ResNet50

ResNet50 was selected as a heavyweight reference architecture for comparison with ShuffleNetV2.

The original FP32 checkpoint was loaded without modifying the existing model files. A separate INT8 edge artifact was generated using static post-training quantization.

---

## INT8 Quantization

Static post-training INT8 quantization was performed using PyTorch FX graph-mode quantization.

The procedure consisted of:

1. Loading the original FP32 checkpoint.
2. Constructing the corresponding model architecture.
3. Selecting the `fbgemm` quantization engine.
4. Preparing the model for FX static quantization.
5. Calibrating the model using 10 batches from the training dataset.
6. Converting the prepared model to INT8.
7. Saving the resulting INT8 state dictionary as a new edge artifact.
8. Running batch-size-1 CPU inference on the complete test set.

The original FP32 checkpoints and original INT8 result files were not overwritten.

---

## Edge Inference Procedure

For each model:

1. The model was loaded on CPU.
2. CPU execution was restricted to one thread.
3. Ten warm-up inference runs were performed where applicable.
4. The complete 750-image test set was evaluated using batch size 1.
5. Per-image inference latency was recorded.
6. Classification metrics were calculated.
7. Average, median, and 95th-percentile latency were calculated.
8. Throughput was calculated from the average latency.
9. Model artifact size and process memory usage were recorded.
10. Results were saved exclusively inside the `edge_simulation` directory.

---

# Results

## ShuffleNetV2 INT8

| Metric          |              Result |
| --------------- | ------------------: |
| Accuracy        |          **98.53%** |
| Precision       |          **97.89%** |
| Recall          |          **99.20%** |
| F1-score        |          **0.9854** |
| INT8 model size |         **1.45 MB** |
| Average latency | **143.85 ms/image** |
| Median latency  | **126.99 ms/image** |
| P95 latency     | **203.70 ms/image** |
| Throughput      | **6.95 images/sec** |
| Process memory  |      **1715.71 MB** |

The ShuffleNetV2 INT8 model preserved the same test accuracy and F1-score observed for the original FP32 ShuffleNetV2 model.

### Confusion Matrix

The ShuffleNetV2 INT8 edge evaluation produced:

```text
                Predicted
              AI    Nature
Actual AI    367      8
Actual Nature  3    372
```

This corresponds to 739 correct predictions out of 750 test images.

---

## ResNet50 FP32

The FP32 ResNet50 model was also evaluated under the same simulated edge configuration.

| Metric          |              Result |
| --------------- | ------------------: |
| Accuracy        |          **99.60%** |
| Precision       |          **99.47%** |
| Recall          |          **99.73%** |
| F1-score        |          **0.9960** |
| Model size      |        **90.00 MB** |
| Average latency | **143.56 ms/image** |
| Median latency  | **128.37 ms/image** |
| P95 latency     | **187.72 ms/image** |
| Throughput      | **6.97 images/sec** |

---

## ResNet50 INT8

| Metric          |               Result |
| --------------- | -------------------: |
| Accuracy        |           **86.27%** |
| Precision       |           **78.45%** |
| Recall          |          **100.00%** |
| F1-score        |           **0.8792** |
| INT8 model size |         **22.99 MB** |
| Average latency |   **86.26 ms/image** |
| Median latency  |   **76.41 ms/image** |
| P95 latency     |  **114.76 ms/image** |
| Throughput      | **11.59 images/sec** |
| Process memory  |       **2688.34 MB** |

---

# INT8 Edge Comparison

The final comparison between the two INT8 models is:

| Metric          | ShuffleNetV2 INT8 |   ResNet50 INT8 |
| --------------- | ----------------: | --------------: |
| Accuracy        |        **98.53%** |          86.27% |
| Precision       |        **97.89%** |          78.45% |
| Recall          |            99.20% |     **100.00%** |
| F1-score        |        **0.9854** |          0.8792 |
| Model size      |       **1.45 MB** |        22.99 MB |
| Average latency |         143.85 ms |    **86.26 ms** |
| Median latency  |         126.99 ms |    **76.41 ms** |
| P95 latency     |         203.70 ms |   **114.76 ms** |
| Throughput      |        6.95 img/s | **11.59 img/s** |
| Process memory  |    **1715.71 MB** |      2688.34 MB |

### Size and Performance Trade-off

Relative to the ResNet50 INT8 model, ShuffleNetV2 INT8 achieved:

* **93.69% lower model size**
* **+12.27 percentage points higher accuracy**
* **+0.1062 higher F1-score**
* **1715.71 MB vs 2688.34 MB process memory**

However, ResNet50 INT8 achieved lower measured CPU latency and higher throughput in this particular simulated environment:

* ShuffleNetV2: **143.85 ms/image**
* ResNet50: **86.26 ms/image**

Therefore, ShuffleNetV2 was approximately **66.76% slower in average latency** and had approximately **40.03% lower throughput** than ResNet50 under this specific edge simulation.

These latency results should be interpreted as measurements of this particular simulated CPU environment and configuration rather than as a universal hardware-speed ranking between the architectures.

---

# Key Findings

### 1. ShuffleNetV2 provides a substantially smaller edge artifact

The INT8 ShuffleNetV2 artifact is only **1.45 MB**, compared with **22.99 MB** for INT8 ResNet50.

This represents a **93.69% reduction in model storage** relative to the ResNet50 INT8 artifact.

### 2. ShuffleNetV2 retains excellent classification performance after INT8 quantization

ShuffleNetV2 achieved **98.53% accuracy and 0.9854 F1-score** during the edge evaluation.

These values match its original FP32 test performance, indicating that static INT8 quantization caused negligible classification degradation for this architecture on the evaluated dataset.

### 3. ResNet50 experiences substantial INT8 accuracy degradation

Although FP32 ResNet50 achieved **99.60% accuracy**, its INT8 edge version achieved **86.27% accuracy**.

The F1-score decreased from approximately **0.9960 to 0.8792**.

This demonstrates that quantization sensitivity can vary considerably between architectures.

### 4. Smaller does not automatically mean faster under every CPU configuration

Despite its much smaller size, ShuffleNetV2 did not achieve lower measured latency in this simulated environment.

ResNet50 INT8 recorded:

* 86.26 ms/image average latency
* 11.59 images/sec throughput

while ShuffleNetV2 INT8 recorded:

* 143.85 ms/image average latency
* 6.95 images/sec throughput

This highlights that model size, computational efficiency, implementation, and CPU backend behavior can affect real inference latency independently.

### 5. ShuffleNetV2 offers the stronger overall size–accuracy trade-off

For this diffusion-generated image detection task, ShuffleNetV2 INT8 provides a particularly favorable deployment trade-off:

* Very small model footprint
* High classification accuracy
* High F1-score
* Low process memory compared with ResNet50
* Successful preservation of FP32 classification performance after quantization

The main disadvantage observed in this experiment is its higher measured CPU inference latency and lower throughput compared with the INT8 ResNet50 implementation.

---

# Output Files

All new edge-simulation artifacts and results are stored separately from the original model results.

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

The original model directories remain separate:

```text
results/
├── shufflenetv2/
└── resnet50/
```

No original checkpoints or original result files were overwritten during the edge-device experiments.

---

# Reproducibility

The edge simulation uses the same preprocessed dataset generated during the dataset preprocessing stage.

Important configuration values:

```text
Input resolution: 224 × 224
Batch size: 1
CPU threads: 1
Test images: 750
Calibration batches: 10
Quantization engine: FBGEMM
Quantization: Static post-training INT8
```

The experiment should be interpreted as a **simulated edge-device evaluation**, rather than a measurement on a physical edge board. Actual deployment latency and memory behavior may differ depending on the target hardware, CPU architecture, inference runtime, quantization backend, and operating system.

---

# Conclusion

The edge-device simulation demonstrates that **ShuffleNetV2 INT8 provides a substantially more compact and quantization-resilient solution for diffusion-generated image detection than ResNet50 INT8**.

ShuffleNetV2 reduced the INT8 model footprint by **93.69%** while achieving **98.53% accuracy and a 0.9854 F1-score**. In contrast, ResNet50 INT8 retained a larger model footprint and experienced a substantial reduction in classification performance after quantization.

However, the simulated CPU measurements showed that ResNet50 INT8 achieved lower inference latency and higher throughput in this specific environment. Therefore, the results indicate that **edge suitability cannot be determined from model size alone**.

Overall, ShuffleNetV2 provides the stronger **accuracy–model-size–memory trade-off** for this application, while ResNet50 demonstrates an advantage in the measured CPU latency and throughput under the tested configuration.
