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
    skill_path = os.path.expanduser("~/Documents/Ivan_Skills/Skill/blog-image-generator/scripts")
    if skill_path not in sys.path:
        sys.path.insert(0, skill_path)

    from image_generator import ImageGenerator as BaseImageGenerator

    class GeminiImageGenerator(BaseImageGenerator):
        """Twitter-specific wrapper around the unified ImageGenerator."""

        def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
            """Initialize with backward-compatible API."""
            super().__init__()
            self.model_name = model_name
            self.api_key = self.secrets.get("NANO_API_KEY") or os.environ.get("GEMINI_API_KEY")

        # Alias for backward compatibility
        def generate_image(self, prompt, aspect_ratio="16:9", image_size="4K"):
            """Generate image - backward compatible method."""
            return self.generate(prompt, aspect_ratio, timeout=90, style="twitter")

except ImportError:
    # Fallback to local implementation if shared skill is not available
    import os
    import sys
    import json
    import requests
    import base64

    class GeminiImageGenerator:
        """Fallback local implementation when shared skill is unavailable."""

        def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
            if not api_key:
                api_key = self._load_api_key_from_secrets()
            if not api_key:
                api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("NANO_API_KEY")
            if not api_key:
                print("Error: API key not found.")
                sys.exit(1)
            self.api_key = api_key
            self.model_name = model_name
            self.base_url = "https://generativelanguage.googleapis.com/v1beta"

        def _load_api_key_from_secrets(self):
            secrets_path = os.path.expanduser("~/.claude/lensmor_secrets.json")
            if os.path.exists(secrets_path):
                try:
                    with open(secrets_path, "r") as f:
                        secrets = json.load(f)
                        return secrets.get("NANO_API_KEY")
                except Exception:
                    pass
            return None

        def generate_image(self, prompt, aspect_ratio="16:9", image_size="4K"):
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
                    return None
                result = response.json()
                if "candidates" in result:
                    for candidate in result.get("candidates", []):
                        for part in candidate.get("content", {}).get("parts", []):
                            inline_data = part.get("inline_data") or part.get("inlineData")
                            if inline_data:
                                return inline_data.get("data")
                return None
            except Exception:
                return None

        @staticmethod
        def save_image(b64_data, filepath):
            try:
                img_data = base64.b64decode(b64_data)
                with open(filepath, "wb") as f:
                    f.write(img_data)
                return True
            except Exception:
                return False


if __name__ == "__main__":
    # Test
    gen = GeminiImageGenerator()
    print("GeminiImageGenerator loaded successfully")
