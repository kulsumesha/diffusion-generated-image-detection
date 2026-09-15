"""
prepare_dataset.py

Takes a raw GenImage generator folder (e.g. "Stable Diffusion V1.4") which
looks like:

    Stable Diffusion V1.4/
        train/
            ai/
            nature/
        val/
            ai/
            nature/

...and produces a fixed, subsampled train/val/test split that everyone
on the team uses identically.

Usage:
    python prepare_dataset.py \
        --source "/path/to/Stable Diffusion V1.4" \
        --output "/path/to/dataset_final" \
        --per_class 5000 \
        --seed 42

This will:
  1. Pool the "ai" images from both train/ and val/ into one list (repeat for "nature")
  2. Randomly subsample --per_class images per class (default 5000 real + 5000 fake)
  3. Split into 70% train / 15% val / 15% test (stratified by class)
  4. Copy the chosen files into output/train/ai, output/train/nature,
     output/val/ai, output/val/nature, output/test/ai, output/test/nature
  5. Write a manifest.csv logging every file's final split + original path,
     so the exact split is fully reproducible and auditable
"""

import argparse
import csv
import random
from pathlib import Path

from PIL import Image

IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def collect_images(source: Path, cls: str) -> list[Path]:
    """Pool images of one class ('ai' or 'nature') from train/ and val/ subfolders."""
    found = []
    for subset in ("train", "val"):
        folder = source / subset / cls
        if folder.exists():
            found.extend([p for p in folder.rglob("*") if p.suffix.lower() in IMG_EXTS])
    return found


def split_list(items: list, train_frac: float, val_frac: float):
    n = len(items)
    n_train = int(n * train_frac)
    n_val = int(n * val_frac)
    train = items[:n_train]
    val = items[n_train:n_train + n_val]
    test = items[n_train + n_val:]
    return train, val, test


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="Path to raw generator folder (e.g. 'Stable Diffusion V1.4')")
    ap.add_argument("--output", required=True, help="Path to write the final split dataset")
    ap.add_argument("--per_class", type=int, default=5000, help="Images to sample per class (ai / nature)")
    ap.add_argument("--train_frac", type=float, default=0.70)
    ap.add_argument("--val_frac", type=float, default=0.15)
    # remaining fraction goes to test
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--resolution", type=int, default=224, help="Fixed square resolution to resize every image to")
    args = ap.parse_args()

    random.seed(args.seed)
    source = Path(args.source)
    output = Path(args.output)

    if not source.exists():
        raise SystemExit(f"Source folder not found: {source}")

    manifest_rows = []

    for cls in ("ai", "nature"):
        print(f"Collecting '{cls}' images from {source} ...")
        all_images = collect_images(source, cls)
        print(f"  Found {len(all_images)} total '{cls}' images")

        if len(all_images) == 0:
            raise SystemExit(f"No images found for class '{cls}' — check your source folder structure.")

        random.shuffle(all_images)
        sampled = all_images[: min(args.per_class, len(all_images))]
        print(f"  Sampled {len(sampled)} '{cls}' images (requested {args.per_class})")

        train, val, test = split_list(sampled, args.train_frac, args.val_frac)

        for split_name, files in (("train", train), ("val", val), ("test", test)):
            dest_dir = output / split_name / cls
            dest_dir.mkdir(parents=True, exist_ok=True)
            for src_path in files:
                dest_path = dest_dir / src_path.name
                # avoid filename collisions across generators/subfolders
                if dest_path.exists():
                    dest_path = dest_dir / f"{src_path.parent.name}_{src_path.name}"
                try:
                    with Image.open(src_path) as img:
                        img = img.convert("RGB")  # fixes any grayscale/CMYK/PNG-alpha inconsistencies
                        img = img.resize((args.resolution, args.resolution), Image.BICUBIC)
                        img.save(dest_path, quality=95)
                except Exception as e:
                    print(f"    Skipping unreadable image {src_path}: {e}")
                    continue
                manifest_rows.append({
                    "class": cls,
                    "split": split_name,
                    "original_path": str(src_path),
                    "final_path": str(dest_path),
                })
            print(f"    {split_name}: {len(files)} images -> {dest_dir}")

    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / "manifest.csv"
    with open(manifest_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["class", "split", "original_path", "final_path"])
        writer.writeheader()
        writer.writerows(manifest_rows)

    print(f"\nDone. Final dataset written to: {output}")
    print(f"Manifest (full reproducibility log) written to: {manifest_path}")
    print("\nFinal structure:")
    print(f"  {output}/train/ai, {output}/train/nature")
    print(f"  {output}/val/ai,   {output}/val/nature")
    print(f"  {output}/test/ai,  {output}/test/nature")


if __name__ == "__main__":
    main()
