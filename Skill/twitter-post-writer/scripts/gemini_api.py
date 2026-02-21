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
        """Twitter-specific wrapper around the unified ImageGenerator."""

        def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
            """Initialize with backward-compatible API."""
            super().__init__()
            self.model_name = model_name
            self.api_key = os.environ.get("GEMINI_API_KEY")

        # Alias for backward compatibility
        def generate_image(self, prompt, aspect_ratio="16:9", image_size="4K"):
            """Generate image - backward compatible method."""
            return self.generate(prompt, aspect_ratio, timeout=90, style="twitter")

except ImportError:
    # Fallback to local implementation if shared skill is not available
    import os
    import sys
    import requests
    import base64

    # Initialize environment from .env (with legacy JSON fallback)
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "..", "scripts"))
    import env_setup; env_setup.init_env()

    class GeminiImageGenerator:
        """Fallback local implementation when shared skill is unavailable."""

        def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
            self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
            if not self.api_key:
                print("Error: GEMINI_API_KEY not found.")
                print("Add GEMINI_API_KEY to .env in the repository root. See .env.example.")
                sys.exit(1)
            self.model_name = model_name
            self.base_url = "https://generativelanguage.googleapis.com/v1beta"

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
