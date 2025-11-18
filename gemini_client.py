"""
Gemini Client using the official google-generativeai library.
Supports:
 - mock mode
 - real mode using Gemini 2.0 Flash
"""

import os
import logging
from pathlib import Path
from utils import read_binary_as_b64

import google.generativeai as genai

logger = logging.getLogger(__name__)


class GeminiClient:
    def __init__(self, cfg):
        """
        cfg:
          {
            "mode": "mock" | "real",
            "api_key_env": "GEMINI_API_KEY",
            "model": "gemini-2.0-flash",
            "mock_response_template": "...",
          }
        """
        self.mode = cfg.get("mode", "mock")
        self.model_name = cfg.get("model", "gemini-2.0-flash")
        self.api_key_env = cfg.get("api_key_env", "GEMINI_API_KEY")
        self.mock_template = cfg.get(
            "mock_response_template",
            "Use first two images for face; scene for environment; produce single-line prompt."
        )

        self.api_key = os.getenv(self.api_key_env)
        if self.mode == "real":
            if not self.api_key:
                raise RuntimeError("Gemini key missing in environment.")
            genai.configure(api_key=self.api_key)

            self.model = genai.GenerativeModel(self.model_name)

    def call(self, image_paths, user_prompt):
        """
        Send 3 images (face1, face2, scene) + user prompt to Gemini.
        Returns: prompt string for Seedream.
        """

        if len(image_paths) != 3:
            raise ValueError("GeminiClient requires exactly 3 images")

        if self.mode == "mock":
            scene_name = Path(image_paths[2]).stem
            return f"{self.mock_template} Scene:{scene_name}. UserPrompt:{user_prompt}"

        # REAL GEMINI CALL
        try:
            images_b64 = [read_binary_as_b64(p) for p in image_paths]

            response = self.model.generate_content(
                [
                    {"mime_type": "image/jpeg", "data": images_b64[0]},
                    {"mime_type": "image/jpeg", "data": images_b64[1]},
                    {"mime_type": "image/jpeg", "data": images_b64[2]},
                    user_prompt
                ]
            )

            return response.text.strip()

        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            raise
