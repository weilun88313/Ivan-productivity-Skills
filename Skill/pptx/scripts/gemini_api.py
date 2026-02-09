"""
Gemini API client for image generation.
Shared module to avoid code duplication.
"""

import os
import sys
import requests
import base64


class GeminiImageGenerator:
    """Client for Gemini image generation API."""

    def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            print("Error: GEMINI_API_KEY environment variable not set.")
            print("Please set it with: export GEMINI_API_KEY='your_api_key'")
            sys.exit(1)

        self.model_name = model_name
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"

    def generate_image(self, prompt, aspect_ratio="16:9", image_size="4K"):
        """
        Generate an image from a text prompt.

        Args:
            prompt: Text prompt for image generation
            aspect_ratio: Image aspect ratio (default: "16:9")
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
            response = requests.post(url, json=payload, headers=headers, timeout=60)

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
            print("Error: API request timed out after 60 seconds.")
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
