from pathlib import Path

PREDICTIONS_DIR = Path("predictions")
VIDEOS_DIR = Path("videos")

def ensure_dirs():
    PREDICTIONS_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)