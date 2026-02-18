"""
Blog image generation client.

This module now imports from the unified blog-image-generator skill.
Kept here for backward compatibility with existing blog-writer code.

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

    class ImageGenerator(BaseImageGenerator):
        """Blog-specific wrapper around the unified ImageGenerator."""

        def __init__(self):
            super().__init__()

        # Alias for backward compatibility
        def generate_image(self, prompt, aspect_ratio="16:9", timeout=180):
            """Generate image - backward compatible method name."""
            return self.generate(prompt, aspect_ratio, timeout, style="blog")

    # Backward compatibility alias
    GeminiImageGenerator = ImageGenerator

except ImportError:
    # Fallback to local implementation if shared skill is not available
    import os
    import sys
    import json
    import requests
    import base64
    import time

    class ImageGenerator:
        """Fallback local implementation when shared skill is unavailable."""

        def __init__(self):
            self.secrets = self._load_secrets()
            self.providers = self._get_available_providers()
            self.model_name = "models/gemini-3-pro-image-preview"

            if not self.providers:
                print("Error: No image generation API keys found.")
                print("Please add to ~/.claude/lensmor_secrets.json:")
                print("  - NANO_API_KEY (Gemini)")
                print("  - FAL_KEY (Fal.ai Nano Banana Pro)")
                sys.exit(1)

            print(f"Available providers: {', '.join(self.providers)}")

        def _load_secrets(self):
            try:
                secrets_path = os.path.expanduser("~/.claude/lensmor_secrets.json")
                with open(secrets_path, "r") as f:
                    return json.load(f)
            except Exception:
                return {}

        def _get_available_providers(self):
            providers = []
            if self.secrets.get("NANO_API_KEY") or os.environ.get("GEMINI_API_KEY"):
                providers.append("gemini")
            if self.secrets.get("FAL_KEY") or os.environ.get("FAL_KEY"):
                providers.append("fal")
            return providers

        def generate(self, prompt, aspect_ratio="16:9", timeout=180, style=None):
            for provider in self.providers:
                print(f"Trying {provider}...")
                try:
                    if provider == "gemini":
                        result = self._generate_gemini(prompt, aspect_ratio, timeout)
                    elif provider == "fal":
                        result = self._generate_fal(prompt, aspect_ratio, timeout)
                    else:
                        continue
                    if result:
                        print(f"✓ Success with {provider}")
                        return result
                except Exception as e:
                    print(f"✗ {provider} error: {e}")
                    continue
            return None

        def _generate_gemini(self, prompt, aspect_ratio, timeout):
            api_key = self.secrets.get("NANO_API_KEY") or os.environ.get("GEMINI_API_KEY")
            model = "models/gemini-3-pro-image-preview"
            url = f"https://generativelanguage.googleapis.com/v1beta/{model}:generateContent?key={api_key}"
            payload = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "responseModalities": ["IMAGE"],
                    "imageConfig": {"aspectRatio": aspect_ratio}
                }
            }
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=timeout)
            if response.status_code == 400:
                if "not supported" in str(response.json()).lower():
                    print("  Region not supported by Gemini")
                    return None
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

        def _generate_fal(self, prompt, aspect_ratio, timeout):
            api_key = self.secrets.get("FAL_KEY") or os.environ.get("FAL_KEY")
            url = "https://queue.fal.run/fal-ai/nano-banana-pro"
            aspect_ratio_map = {"16:9": "16:9", "1:1": "1:1", "9:16": "9:16", "4:3": "4:3", "3:2": "3:2"}
            fal_aspect_ratio = aspect_ratio_map.get(aspect_ratio, "16:9")
            payload = {
                "prompt": prompt,
                "num_images": 1,
                "aspect_ratio": fal_aspect_ratio,
                "output_format": "png",
                "sync_mode": True
            }
            headers = {"Content-Type": "application/json", "Authorization": f"Key {api_key}"}
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            if response.status_code != 200:
                return None
            result = response.json()
            if result.get("status") == "COMPLETED" and "images" in result:
                image_data = result["images"][0]
                if "url" in image_data:
                    if image_data["url"].startswith("data:image"):
                        return image_data["url"].split(",", 1)[1]
                    else:
                        img_response = requests.get(image_data["url"], timeout=30)
                        if img_response.status_code == 200:
                            return base64.b64encode(img_response.content).decode('utf-8')
            return None

        @staticmethod
        def save(b64_data, filepath):
            try:
                img_data = base64.b64decode(b64_data)
                with open(filepath, "wb") as f:
                    f.write(img_data)
                return True
            except Exception:
                return False

        def generate_image(self, prompt, aspect_ratio="16:9", timeout=180):
            return self.generate(prompt, aspect_ratio, timeout)

        @staticmethod
        def save_image(b64_data, filepath):
            return ImageGenerator.save(b64_data, filepath)

    class GeminiImageGenerator(ImageGenerator):
        """Backward compatibility alias."""
        pass


if __name__ == "__main__":
    # Test the generator
    generator = ImageGenerator()
    test_prompt = """Style: Abstract high-tech visualization inspired by Linear design. Dark mode, minimalist.

Color Palette: Deep charcoal background, glowing violet-blue (#6B75FF) accents.

Concept: Floating geometric data nodes connected by thin glowing lines in dark void.

Environment: Deep black background with subtle technical grid.

Negative Constraints: NO UI elements, NO text, NO dashboards."""
    print("\nTesting image generation...")
    result = generator.generate_image(test_prompt, aspect_ratio="16:9")
    if result:
        output = "test_image.png"
        if generator.save_image(result, output):
            print(f"\n✓ Test image saved to {output}")
        else:
            print("\n✗ Failed to save test image")
    else:
        print("\n✗ Test failed")
