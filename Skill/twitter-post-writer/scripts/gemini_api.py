"""
Gemini API client for image generation.
Shared module to avoid code duplication.
"""

import os
import sys
import json
import requests
import base64


class GeminiImageGenerator:
    """Client for Gemini image generation API."""

    def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
        # Try to load from secrets file first
        if not api_key:
            api_key = self._load_api_key_from_secrets()

        # Fall back to environment variable
        if not api_key:
            api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("NANO_API_KEY")

        if not api_key:
            print("Error: API key not found.")
            print("Please ensure NANO_API_KEY is set in ~/.claude/lensmor_secrets.json")
            print("Or set GEMINI_API_KEY/NANO_API_KEY environment variable.")
            sys.exit(1)

        self.api_key = api_key
        self.model_name = model_name
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"

    def _load_api_key_from_secrets(self):
        """Load API key from secrets file."""
        secrets_path = os.path.expanduser("~/.claude/lensmor_secrets.json")
        if os.path.exists(secrets_path):
            try:
                with open(secrets_path, "r") as f:
                    secrets = json.load(f)
                    return secrets.get("NANO_API_KEY")
            except Exception as e:
                print(f"Warning: Could not load secrets file: {e}")
        return None

    def generate_image(self, prompt, aspect_ratio="16:9", image_size="4K"):
        """
        Generate an image from a text prompt.

        Args:
            prompt: Text prompt for image generation
            aspect_ratio: Image aspect ratio (default: "16:9")
                Options: "16:9" (landscape), "1:1" (square), "4:3" (standard)
            image_size: Image size/quality (default: "4K")

        Returns:
            Base64-encoded image data, or None if generation failed
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
            print(f"Generating image with aspect ratio {aspect_ratio}...")
            response = requests.post(url, json=payload, headers=headers, timeout=90)

            if response.status_code != 200:
                print(f"API Error {response.status_code}: {response.text}")
                return None

            result = response.json()

            # Extract image data from response
            if "candidates" in result:
                for candidate in result.get("candidates", []):
                    for part in candidate.get("content", {}).get("parts", []):
                        inline_data = part.get("inline_data") or part.get("inlineData")
                        if inline_data:
                            return inline_data.get("data")

            print("No image data found in API response.")
            return None

        except requests.exceptions.Timeout:
            print("Error: API request timed out after 90 seconds.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    @staticmethod
    def save_image(b64_data, filepath):
        """
        Save base64-encoded image data to a file.

        Args:
            b64_data: Base64-encoded image data
            filepath: Output file path

        Returns:
            True if successful, False otherwise
        """
        try:
            img_data = base64.b64decode(b64_data)
            with open(filepath, "wb") as f:
                f.write(img_data)
            return True
        except Exception as e:
            print(f"Error saving image to {filepath}: {e}")
            return False
