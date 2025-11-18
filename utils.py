import os
import base64
from pathlib import Path
import imghdr
import logging

logger = logging.getLogger(__name__)

VALID_IMG_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".gif"}

def list_images(dirpath):
    """
    Return sorted list of image file paths in dirpath (relative or absolute).
    Accepts common image extensions. Ignores hidden files.
    """
    p = Path(dirpath)
    if not p.exists() or not p.is_dir():
        return []
    files = []
    for f in sorted(p.iterdir()):
        if not f.is_file():
            continue
        # skip hidden files
        if f.name.startswith("."):
            continue
        suffix = f.suffix.lower()
        # quick extension check first
        if suffix in VALID_IMG_EXT:
            files.append(str(f))
            continue
        # fallback: try imghdr to detect
        try:
            if imghdr.what(str(f)):
                files.append(str(f))
        except Exception:
            continue
    return files

def read_binary_as_b64(path):
    with open(path, "rb") as f:
        raw = f.read()
    return base64.b64encode(raw).decode("utf-8")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def safe_filename(s):
    # produce filesystem-safe filename
    return "".join(c if c.isalnum() or c in " ._-" else "_" for c in s)[:200]
