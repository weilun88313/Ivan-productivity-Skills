"""
Gemini API client for image generation.
Provides GeminiImageGenerator for generating images via the Gemini API.
"""

import os
import sys
import base64
import requests

# Initialize environment from .env (with legacy JSON fallback)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "..", "scripts"))
import env_setup; env_setup.init_env()


class GeminiImageGenerator:
    """Gemini API client for generating slide images."""

    def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            print("Error: GEMINI_API_KEY environment variable not set.")
            sys.exit(1)
        self.model_name = model_name
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"

    def generate_image(self, prompt, aspect_ratio="16:9", image_size="4K"):
        """Generate an image from a text prompt via Gemini API.

        Returns base64-encoded image data, or None on failure.
        """
        url = f"{self.base_url}/{self.model_name}:generateContent?key={self.api_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseModalities": ["IMAGE"],
                "imageConfig": {
                    "aspectRatio": aspect_ratio,
                    "imageSize": image_size
                }
            }
        }
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=120)
            if response.status_code != 200:
                print(f"API error (HTTP {response.status_code}): {response.text[:200]}")
                return None
            result = response.json()
            if "candidates" in result:
                for candidate in result.get("candidates", []):
                    for part in candidate.get("content", {}).get("parts", []):
                        inline_data = part.get("inline_data") or part.get("inlineData")
                        if inline_data:
                            return inline_data.get("data")
            print("API returned no image data in response.")
            return None
        except requests.exceptions.Timeout:
            print("API request timed out.")
            return None
        except Exception as e:
            print(f"API request failed: {e}")
            return None

    @staticmethod
    def save_image(b64_data, filepath):
        """Save base64-encoded image data to a file."""
        try:
            img_data = base64.b64decode(b64_data)
            with open(filepath, "wb") as f:
                f.write(img_data)
            return True
        except Exception as e:
            print(f"Error saving image to {filepath}: {e}")
            return False


if __name__ == "__main__":
    gen = GeminiImageGenerator()
    print("GeminiImageGenerator loaded successfully")
