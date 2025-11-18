#!/usr/bin/env python3
"""
Main interactive CLI runner.
Usage: python main.py [--dry-run]
"""
import os
import sys
import json
import time
import logging
import argparse
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

import utils
from gemini_client import GeminiClient
from seedream_client import SeedreamClient

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("main")

load_dotenv()  # loads .env

ROOT = Path.cwd()
CONFIG_PATH = ROOT / "config_example.json"
if not CONFIG_PATH.exists():
    logger.error("config_example.json not found. Please create it from config_example.json")
    sys.exit(1)

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

IO = CONFIG.get("io", {})
FACES_DIR = IO.get("faces_dir", "FACE")
SCENES_DIR = IO.get("scenes_dir", "SCENE")
OUTPUT_DIR = IO.get("output_dir", "OUTPUT")
PROMPT_FILE = IO.get("gemini_prompt_file", "gemini_user_prompt.txt")
RESULT_FORMAT = IO.get("result_format", "png")

BEHAVIOR = CONFIG.get("behavior", {})
PAUSE = BEHAVIOR.get("pause_between_requests_s", 0.8)
MAX_RETRIES = BEHAVIOR.get("max_retries", 3)

def read_user_prompt(prompt_path):
    p = Path(prompt_path)
    if not p.exists():
        logger.error("Prompt file not found: %s", prompt_path)
        return ""
    return p.read_text(encoding="utf-8")

def pick_two_faces(faces_list):
    if len(faces_list) < 2:
        raise RuntimeError(f"Need at least 2 face images in {FACES_DIR}")
    return faces_list[0], faces_list[1]

def run(dry_run=False):
    print("=== Face+Scene → Gemini → Seedream pipeline ===")
    faces = utils.list_images(FACES_DIR)
    scenes = utils.list_images(SCENES_DIR)
    print(f"Found face images: {len(faces)} in {FACES_DIR}")
    for f in faces:
        print("  ", f)
    print(f"Found scene images: {len(scenes)} in {SCENES_DIR}")

    if len(faces) < 2:
        logger.error("Please put at least 2 face images into the FACE/ directory before running.")
        return
    if len(scenes) == 0:
        logger.error("No scene images found in SCENE/ directory.")
        return

    user_prompt = read_user_prompt(PROMPT_FILE)
    if not user_prompt:
        logger.error("User prompt is empty. Please edit %s", PROMPT_FILE)
        return
    print(f"\nLoaded user prompt (first 240 chars):\n{user_prompt[:240]}\n")

    input("Press Enter to start processing all scenes (or Ctrl+C to cancel)...")

    face1, face2 = pick_two_faces(faces)
    print(f"Using face1: {face1}")
    print(f"Using face2: {face2}")

    gemini_cfg = CONFIG.get("gemini", {})
    seedream_cfg = CONFIG.get("seedream", {})
    gemini_client = GeminiClient(gemini_cfg)
    seedream_client = SeedreamClient(seedream_cfg)

    utils.ensure_dir(OUTPUT_DIR)

    for idx, scene_path in enumerate(tqdm(scenes, desc="Scenes", unit="scene")):
        scene_name = Path(scene_path).stem
        index_label = f"{idx+1:04d}_{utils.safe_filename(scene_name)}"
        try:
            # Gemini
            gemini_prompt = None
            for attempt in range(1, MAX_RETRIES+1):
                try:
                    if dry_run:
                        gemini_prompt = f"[DRY-RUN] mock prompt for {scene_name}"
                    else:
                        gemini_prompt = gemini_client.call([face1, face2, scene_path], user_prompt)
                    logger.info("Gemini returned prompt (len=%d).", len(gemini_prompt) if gemini_prompt else 0)
                    break
                except Exception as e:
                    logger.warning("Gemini call failed on attempt %d: %s", attempt, e)
                    time.sleep(1 + attempt)
            if not gemini_prompt:
                logger.error("Skipping scene %s due to Gemini failure.", scene_path)
                continue

            # Seedream
            resp = None
            for attempt in range(1, MAX_RETRIES+1):
                try:
                    if dry_run:
                        # build mocked response structure
                        resp = {"data": {"outputs": [ {"mock_note": "dry-run", "b64_json": None} ]}}
                    else:
                        resp = seedream_client.call([face1, face2, scene_path], gemini_prompt, size=seedream_cfg.get("default_size"))
                    break
                except Exception as e:
                    logger.warning("Seedream call failed on attempt %d: %s", attempt, e)
                    time.sleep(1 + attempt)
            if not resp:
                logger.error("Skipping scene %s due to Seedream failure.", scene_path)
                continue

            # Save result (if dry-run: create small text file)
            try:
                if dry_run:
                    out_txt = Path(OUTPUT_DIR) / f"{index_label}.txt"
                    out_txt.write_text(f"DRY-RUN result for {scene_name}\nGemini prompt:\n{gemini_prompt}", encoding="utf-8")
                    logger.info("Saved dry-run file: %s", out_txt)
                else:
                    out_img, out_caption = seedream_client.download_output_image(resp, OUTPUT_DIR, index_label)
                    logger.info("Saved: %s", out_img)
            except Exception as e:
                logger.error("Error saving result for %s: %s", scene_path, e)

            time.sleep(PAUSE)
        except KeyboardInterrupt:
            logger.info("Interrupted by user. Exiting.")
            break
        except Exception as e:
            logger.exception("Unhandled error processing %s: %s", scene_path, e)
            continue

    logger.info("Processing complete. Check the OUTPUT folder for results.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Face+Scene -> Gemini -> Seedream pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Do not call external APIs; create dry-run outputs")
    args = parser.parse_args()
    run(dry_run=args.dry_run)
