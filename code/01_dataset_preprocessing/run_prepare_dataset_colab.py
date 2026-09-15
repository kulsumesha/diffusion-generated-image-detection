from google.colab import drive
import subprocess
import sys
from pathlib import Path

# Mount Google Drive
drive.mount("/content/drive")

# Install Pillow
subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    "Pillow"
])

print("Google Drive mounted and Pillow installed.")