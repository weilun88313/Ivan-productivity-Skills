"""
Gemini API client for image generation.
Shared module for hubspot-blog-writer skill.
"""

import os
import sys
import requests
import base64

# Initialize environment from .env (with legacy JSON fallback)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "..", "scripts"))
import env_setup; env_setup.init_env()


class GeminiImageGenerator:
    """Client for Gemini image generation API."""

    def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
        # Try multiple sources for API key
        self.api_key = api_key or self._load_api_key()

        if not self.api_key:
            print("Error: GEMINI_API_KEY not found.")
            print("Add GEMINI_API_KEY to .env in the repository root.")
            print("See .env.example for the expected format.")
            sys.exit(1)

        self.model_name = model_name
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"

    def _load_api_key(self):
        """Load API key from environment (populated by env_setup)."""
        return os.environ.get("GEMINI_API_KEY")

    def generate_image(self, prompt, aspect_ratio="16:9", max_retries=3, timeout=180):
        """
        Generate an image from a text prompt.

        Args:
            prompt: Text prompt for image generation
            aspect_ratio: Image aspect ratio (default: "16:9")
            max_retries: Maximum number of retry attempts (default: 3)
            timeout: Request timeout in seconds (default: 180)

        Returns:
            Base64-encoded image data, or None if generation failed
        """
        url = f"{self.base_url}/{self.model_name}:generateContent?key={self.api_key}"

        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseModalities": ["IMAGE"],
                "imageConfig": {"aspectRatio": aspect_ratio}
            }
        }

        headers = {"Content-Type": "application/json"}

        for attempt in range(1, max_retries + 1):
            try:
                response = requests.post(url, json=payload, headers=headers, timeout=timeout)

                # Handle rate limiting and server errors
                if response.status_code == 429:
                    wait_time = 2 ** attempt
                    print(f"Rate limited, waiting {wait_time}s... ({attempt}/{max_retries})")
                    import time
                    time.sleep(wait_time)
                    continue

                if response.status_code >= 500 and attempt < max_retries:
                    wait_time = 2 ** attempt
                    print(f"Server error {response.status_code}, retrying in {wait_time}s...")
                    import time
                    time.sleep(wait_time)
                    continue

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
                print(f"Request timed out ({timeout}s), attempt {attempt}/{max_retries}")
                if attempt < max_retries:
                    import time
                    time.sleep(2 ** attempt)
            except requests.exceptions.RequestException as e:
                print(f"Network error: {e}, attempt {attempt}/{max_retries}")
                if attempt < max_retries:
                    import time
                    time.sleep(2 ** attempt)

        print("All retries exhausted.")
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
