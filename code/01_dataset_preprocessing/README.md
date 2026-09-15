# Dataset Preprocessing

The dataset preprocessing stage was performed in Google Colab using the tiny-genimage dataset.

## Steps

1. The official GenImage dataset was initially considered, but its approximately 90 GB size, distributed across 30 split archive files, made it impractical to use directly.
2. A smaller `tiny-genimage` dataset was therefore used instead.
3. The dataset archive was extracted inside Google Colab.
4. The extracted folder structure was checked to confirm that it matched the structure expected by the preparation script.
5. Google Drive was mounted in Colab so that the processed dataset could be stored permanently.
6. The `prepare_dataset.py` script was uploaded and executed on the `imagenet_ai_0424_sdv5` subset.
7. The subset contained 2,500 AI-generated images and 2,500 real images.
8. The preparation script converted the images to RGB and resized them to 224 × 224 pixels.
9. The images were divided into 70% training, 15% validation, and 15% testing sets for each class.
10. The resulting dataset was saved to Google Drive as `dataset_final`.
11. A `manifest.csv` file was generated to record the class, split, original path, and final path of each processed image.

## Final Dataset

- Total images: 5,000
- AI-generated images: 2,500
- Real images: 2,500
- Training: 3,500 images
- Validation: 750 images
- Testing: 750 images
- Image resolution: 224 × 224
- Classes: `ai`, `nature`