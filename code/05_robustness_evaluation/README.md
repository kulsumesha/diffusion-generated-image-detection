# Robustness Experiment: ShuffleNetV2 for Diffusion-Generated Image Detection

This experiment evaluates the robustness of a lightweight ShuffleNetV2-based image classifier for detecting diffusion-generated images under common image degradations. It further investigates whether robustness-oriented training remains effective after post-training INT8 quantization, with emphasis on edge-device deployment.

The experiment is conducted as a separate extension of the original ShuffleNetV2 evaluation. All experiment-specific checkpoints, results, and plots are stored separately from the original model results.

---

## 1. Objectives

The robustness experiment has four main objectives:

1. Establish the original ShuffleNetV2 model's performance on clean and corrupted test images.
2. Train a robustness-enhanced ShuffleNetV2 model using corrupted training images.
3. Evaluate whether robustness training improves performance under image degradations while maintaining acceptable clean-image performance.
4. Apply static post-training INT8 quantization to the robust model and determine whether robustness is preserved after quantization.

The evaluated corruptions are:

* JPEG compression
* Gaussian blur
* Gaussian noise
* Low-resolution degradation

The final experiment therefore compares:

* Original FP32 ShuffleNetV2
* Robustly trained FP32 ShuffleNetV2
* Robustly trained INT8 ShuffleNetV2

---

## 2. Dataset

The experiment uses the previously prepared AI-vs-real image classification dataset.

### Dataset composition

| Property            |     Value |
| ------------------- | --------: |
| Total images        |     5,000 |
| AI-generated images |     2,500 |
| Real/natural images |     2,500 |
| Training images     |     3,500 |
| Validation images   |       750 |
| Test images         |       750 |
| Image size          | 224 × 224 |
| Number of classes   |         2 |

The two classes are:

* `ai`
* `nature`

The dataset uses a balanced class distribution, with 1,750 training, 375 validation, and 375 test images per class.

### Dataset location

```text
diffusion_project/
└── dataset_final/
    ├── train/
    ├── val/
    ├── test/
    └── manifest.csv
```

The existing dataset was used without modification during the robustness experiment.

---

## 3. Model

The model evaluated in this experiment is **ShuffleNetV2 x1.0**, selected because of its lightweight architecture and suitability for resource-constrained and edge-device environments.

The original model was initialized from ImageNet-pretrained weights and adapted for binary classification.

### Model configuration

* Architecture: ShuffleNetV2 x1.0
* Input resolution: 224 × 224
* Output classes: 2
* Optimizer: Adam
* Original training learning rate: `1e-4`
* Loss function: Cross-Entropy Loss
* Batch size: 32
* Original training duration: 100 epochs
* Early stopping: Disabled

The original trained checkpoint is located at:

```text
results/shufflenetv2/checkpoint.pth
```

This original checkpoint and its associated results were treated as read-only during the robustness experiment.

---

## 4. Experiment Isolation

All robustness-related files were stored in a separate experiment directory so that the original ShuffleNetV2 results were not overwritten or modified.

```text
diffusion_project/
├── results/
│   └── shufflenetv2/
│       └── ... original experiment files ...
│
└── robustness_experiment/
    ├── checkpoints/
    ├── results/
    ├── plots/
    └── code/
```

The original directory:

```text
results/shufflenetv2/
```

was not modified.

---

## 5. Evaluation Preprocessing

The clean evaluation used the same preprocessing configuration as the original ShuffleNetV2 evaluation:

```python
transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
```

This ensured that the robustness experiment's clean baseline was directly comparable with the original ShuffleNetV2 result.

---

## 6. Baseline Robustness Evaluation

Before robustness training, the original ShuffleNetV2 checkpoint was evaluated on the clean test set and on four corrupted versions of the test images.

### Corruption configurations

#### JPEG compression

```text
JPEG quality = 30
```

#### Gaussian blur

```text
Gaussian blur radius = 2.0
```

#### Gaussian noise

```text
Noise standard deviation = 0.08
```

Noise was applied to normalized image intensity values before conversion back to an image representation.

#### Low resolution

Images were first downsampled to:

```text
56 × 56
```

and then resized back to:

```text
224 × 224
```

using bilinear interpolation.

### Baseline results

| Condition      | Accuracy | Precision |  Recall |     F1 |
| -------------- | -------: | --------: | ------: | -----: |
| Clean          |   98.53% |    97.89% |  99.20% | 98.54% |
| JPEG Q30       |   51.33% |    50.68% | 100.00% | 67.26% |
| Gaussian blur  |   60.53% |    55.90% |  99.73% | 71.65% |
| Gaussian noise |   52.53% |    95.24% |   5.33% | 10.10% |
| Low resolution |   54.13% |    52.16% | 100.00% | 68.56% |

The original model achieved very high performance on clean images but experienced substantial degradation under all tested corruptions.

The Gaussian-noise condition was particularly severe, reducing F1 from 98.54% on clean images to 10.10%.

---

## 7. Robustness Training

A second ShuffleNetV2 model was created by starting from the original trained ShuffleNetV2 checkpoint.

The model was then fine-tuned using corrupted training images.

### Training configuration

| Parameter           | Configuration              |
| ------------------- | -------------------------- |
| Starting checkpoint | Original ShuffleNetV2 FP32 |
| Training images     | 3,500                      |
| Validation images   | 750                        |
| Batch size          | 32                         |
| Epochs              | 15                         |
| Optimizer           | Adam                       |
| Learning rate       | `1e-5`                     |
| Loss                | Cross-Entropy Loss         |
| Input size          | 224 × 224                  |
| Early stopping      | Not used                   |

### Training augmentation

Training images first underwent:

* Random resized crop to 224 × 224
* Random horizontal flip

With an 80% probability, one corruption was additionally selected at random from:

* JPEG compression, quality 30
* Gaussian blur, radius 2.0
* Gaussian noise, standard deviation 0.08
* Low-resolution degradation, 56 × 56 → 224 × 224

The resulting images were then converted to tensors and normalized using ImageNet normalization.

The validation set was evaluated using the clean evaluation transform.

### Validation performance

The best clean validation accuracy was:

```text
92.80%
```

The best model was saved as:

```text
robustness_experiment/checkpoints/shufflenetv2_robust_fp32.pth
```

---

## 8. Robust FP32 Evaluation

The robustness-trained FP32 model was evaluated on the same clean and corrupted test conditions used for the original baseline.

### Results

| Condition      | Accuracy | Precision | Recall |     F1 |
| -------------- | -------: | --------: | -----: | -----: |
| Clean          |   92.80% |    97.91% | 87.47% | 92.39% |
| JPEG Q30       |   85.47% |    80.50% | 93.60% | 86.56% |
| Gaussian blur  |   91.60% |    92.39% | 90.67% | 91.52% |
| Gaussian noise |   87.33% |    85.00% | 90.67% | 87.74% |
| Low resolution |   87.73% |    84.10% | 93.07% | 88.35% |

### Baseline vs. robust FP32

| Condition      | Baseline Accuracy | Robust Accuracy |    Change |
| -------------- | ----------------: | --------------: | --------: |
| Clean          |            98.53% |          92.80% |  −5.73 pp |
| JPEG Q30       |            51.33% |          85.47% | +34.13 pp |
| Gaussian blur  |            60.53% |          91.60% | +31.07 pp |
| Gaussian noise |            52.53% |          87.33% | +34.80 pp |
| Low resolution |            54.13% |          87.73% | +33.60 pp |

Robustness training substantially improved performance under every tested corruption.

The largest improvement in accuracy occurred under Gaussian noise, increasing from 52.53% to 87.33%.

F1 score under Gaussian noise increased from 10.10% to 87.74%.

The trade-off was a reduction in clean accuracy from 98.53% to 92.80%.

---

## 9. INT8 Quantization

The robustness-trained ShuffleNetV2 model was subsequently quantized using static post-training INT8 quantization.

The quantization process used:

* FX graph-mode static quantization
* `fbgemm` quantization backend
* CPU inference
* 10 training batches for calibration

The quantized model was saved separately as:

```text
robustness_experiment/checkpoints/shufflenetv2_robust_int8.pth
```

The original FP32 robust checkpoint was not modified.

### INT8 clean evaluation

| Metric    | Robust FP32 | Robust INT8 |   Change |
| --------- | ----------: | ----------: | -------: |
| Accuracy  |      92.80% |      92.00% | −0.80 pp |
| Precision |      97.91% |      97.58% | −0.33 pp |
| Recall    |      87.47% |      86.13% | −1.34 pp |
| F1        |      92.39% |      91.50% | −0.89 pp |

### Model size

| Model       |    Size |
| ----------- | ------: |
| Robust FP32 | 4.96 MB |
| Robust INT8 | 1.45 MB |

The INT8 model achieved approximately:

```text
70.73% storage reduction
```

relative to the robust FP32 model.

The small clean-performance reduction demonstrates that the robust model retained most of its predictive performance after quantization.

---

## 10. Robust INT8 Corruption Evaluation

The quantized robustness-trained ShuffleNetV2 model was evaluated under the same corruption configurations used for the FP32 experiments.

### Results

| Condition      | Accuracy | Precision | Recall |     F1 |
| -------------- | -------: | --------: | -----: | -----: |
| Clean          |   92.00% |    97.58% | 86.13% | 91.50% |
| JPEG Q30       |   86.80% |    83.17% | 92.27% | 87.48% |
| Gaussian blur  |   89.07% |    92.46% | 85.07% | 88.61% |
| Gaussian noise |   86.27% |    88.42% | 83.47% | 85.87% |
| Low resolution |   87.20% |    84.79% | 90.67% | 87.63% |

The INT8 model maintained strong performance across all tested corruptions.

---

## 11. Overall Comparison

The complete robustness experiment can be summarized as follows:

| Condition      | Original FP32 Accuracy | Robust FP32 Accuracy | Robust INT8 Accuracy |
| -------------- | ---------------------: | -------------------: | -------------------: |
| Clean          |                 98.53% |               92.80% |               92.00% |
| JPEG Q30       |                 51.33% |               85.47% |               86.80% |
| Gaussian blur  |                 60.53% |               91.60% |               89.07% |
| Gaussian noise |                 52.53% |               87.33% |               86.27% |
| Low resolution |                 54.13% |               87.73% |               87.20% |

The results demonstrate three main observations:

1. The original ShuffleNetV2 model performs very well on clean images but is highly sensitive to image degradation.
2. Robustness-oriented training substantially improves performance across all tested corruption types, with an expected reduction in clean-set accuracy.
3. INT8 quantization preserves most of the robust model's performance while reducing model storage by approximately 70.73%.

The robust INT8 model therefore provides a favorable balance between clean-image accuracy, corruption robustness, and model compactness for resource-constrained deployment.

---

## 12. Files

The robustness experiment contains the following outputs:

```text
robustness_experiment/
├── checkpoints/
│   ├── shufflenetv2_robust_fp32.pth
│   └── shufflenetv2_robust_int8.pth
│
├── results/
│   ├── baseline_robustness.json
│   ├── baseline_corruptions.json
│   ├── baseline_vs_robust_fp32.json
│   ├── robust_fp32.json
│   ├── robust_int8_clean.json
│   └── robust_int8_corruptions.json
│
├── plots/
│   └── baseline_vs_robust_fp32.png
│
└── code/
    └── [robustness experiment Jupyter notebook]
```

The Jupyter notebook contains the implementation used to perform the robustness evaluation, robustness training, INT8 quantization, and corruption testing.

---

## 13. Reproducibility

The experiment uses fixed model architecture, dataset splits, image resolution, normalization, corruption parameters, training hyperparameters, and quantization configuration as documented above.

For the corruption evaluation, the same corruption definitions and parameter values were used for the baseline FP32, robust FP32, and robust INT8 evaluations.

The experiment-specific files are isolated under `robustness_experiment/`, while the original ShuffleNetV2 results remain preserved under `results/shufflenetv2/`.

---

## 14. Conclusion

The robustness experiment shows that a lightweight ShuffleNetV2 model can be substantially improved against common image degradations through corruption-aware training.

Although robustness training reduces clean accuracy from 98.53% to 92.80%, it increases corrupted-image accuracy by approximately 31–35 percentage points across the four tested corruption types.

After static INT8 quantization, the model retains 92.00% clean accuracy and achieves between 86.27% and 89.07% accuracy across the tested corruptions, while reducing model storage by approximately 70.73%.

These findings support the use of robustness-aware training followed by INT8 quantization as a practical approach for deploying lightweight image classification models in resource-constrained edge environments.
