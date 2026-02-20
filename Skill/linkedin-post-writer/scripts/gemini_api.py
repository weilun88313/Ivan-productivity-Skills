"""
Gemini API client for image generation.

This module now imports from the unified blog-image-generator skill.
Kept here for backward compatibility with existing code.

The actual implementation is in: Skill/blog-image-generator/scripts/image_generator.py
"""

# Import from the unified blog-image-generator skill
try:
    # Try to import from the shared skill
    import sys
    import os
    skill_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "blog-image-generator", "scripts")
    if skill_path not in sys.path:
        sys.path.insert(0, skill_path)

    from image_generator import ImageGenerator as BaseImageGenerator

    class GeminiImageGenerator(BaseImageGenerator):
        """LinkedIn-specific wrapper around the unified ImageGenerator."""

        def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
            """Initialize with backward-compatible API."""
            super().__init__()
            self.model_name = model_name
            self.api_key = self.secrets.get("NANO_API_KEY") or os.environ.get("GEMINI_API_KEY")

        # Alias for backward compatibility
        def generate_image(self, prompt, aspect_ratio="16:9", max_retries=3, timeout=180):
            """Generate image - backward compatible method."""
            return self.generate(prompt, aspect_ratio, timeout, style="linkedin")

except ImportError:
    # Fallback to local implementation if shared skill is not available
    import os
    import sys
    import json
    import requests
    import base64
    import time

    class GeminiImageGenerator:
        """Fallback local implementation when shared skill is unavailable."""

        def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
            self.api_key = api_key or self._load_api_key()
            if not self.api_key:
                print("Error: GEMINI_API_KEY not found.")
                sys.exit(1)
            self.model_name = model_name
            self.base_url = "https://generativelanguage.googleapis.com/v1beta"

        def _load_api_key(self):
            # Priority: secrets file first, then environment variable (consistent with primary class)
            try:
                secrets_path = os.path.expanduser("~/.claude/lensmor_secrets.json")
                with open(secrets_path, "r") as f:
                    secrets = json.load(f)
                    key = secrets.get("NANO_API_KEY")
                    if key:
                        return key
            except Exception:
                pass
            return os.environ.get("GEMINI_API_KEY")

        def generate_image(self, prompt, aspect_ratio="16:9", max_retries=3, timeout=180):
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
                    if response.status_code == 429:
                        wait_time = 2 ** attempt
                        print(f"Rate limited, waiting {wait_time}s... ({attempt}/{max_retries})")
                        time.sleep(wait_time)
                        continue
                    if response.status_code >= 500 and attempt < max_retries:
                        wait_time = 2 ** attempt
                        print(f"Server error {response.status_code}, retrying in {wait_time}s...")
                        time.sleep(wait_time)
                        continue
                    if response.status_code != 200:
                        print(f"API Error {response.status_code}: {response.text}")
                        return None
                    result = response.json()
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
                        time.sleep(2 ** attempt)
                except requests.exceptions.RequestException as e:
                    print(f"Network error: {e}, attempt {attempt}/{max_retries}")
                    if attempt < max_retries:
                        time.sleep(2 ** attempt)

            print("All retries exhausted.")
            return None

        @staticmethod
        def save_image(b64_data, filepath):
            try:
                img_data = base64.b64decode(b64_data)
                with open(filepath, "wb") as f:
                    f.write(img_data)
                return True
            except Exception as e:
                print(f"Error saving image to {filepath}: {e}")
                return False


if __name__ == "__main__":
    # Test
    gen = GeminiImageGenerator()
    print("GeminiImageGenerator loaded successfully")
