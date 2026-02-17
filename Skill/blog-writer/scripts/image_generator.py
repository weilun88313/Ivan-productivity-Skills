"""
Unified image generation client with fallback support.
Supports multiple image generation APIs: Gemini, Fal.ai Nano Banana Pro.
"""

import os
import sys
import json
import requests
import base64
import time


class ImageGenerator:
    """Unified image generation client with automatic fallback."""

    def __init__(self):
        """Initialize with API keys from secrets file."""
        self.secrets = self._load_secrets()
        self.providers = self._get_available_providers()

        if not self.providers:
            print("Error: No image generation API keys found.")
            print("Please add to ~/.claude/lensmor_secrets.json:")
            print("  - NANO_API_KEY (Gemini)")
            print("  - FAL_KEY (Fal.ai Nano Banana Pro)")
            sys.exit(1)

        print(f"Available providers: {', '.join(self.providers)}")

    def _load_secrets(self):
        """Load API keys from secrets file."""
        try:
            secrets_path = os.path.expanduser("~/.claude/lensmor_secrets.json")
            with open(secrets_path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading secrets: {e}")
            return {}

    def _get_available_providers(self):
        """Check which image generation providers are available."""
        providers = []

        # Check Gemini
        if self.secrets.get("NANO_API_KEY") or os.environ.get("GEMINI_API_KEY"):
            providers.append("gemini")

        # Check Fal.ai
        if self.secrets.get("FAL_KEY") or os.environ.get("FAL_KEY"):
            providers.append("fal")

        return providers

    def generate_image(self, prompt, aspect_ratio="16:9", timeout=180):
        """
        Generate an image with automatic fallback.

        Tries providers in order: Gemini → Fal.ai

        Args:
            prompt: Text prompt for image generation
            aspect_ratio: Image aspect ratio (default: "16:9")
            timeout: Request timeout in seconds (default: 180)

        Returns:
            Base64-encoded image data, or None if all providers failed
        """
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
                else:
                    print(f"✗ {provider} failed, trying next provider...")

            except Exception as e:
                print(f"✗ {provider} error: {e}")
                continue

        print("✗ All providers failed")
        return None

    def _generate_gemini(self, prompt, aspect_ratio, timeout):
        """Generate image using Gemini API."""
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

        response = requests.post(
            url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=timeout
        )

        if response.status_code == 400:
            error_data = response.json()
            if "not supported" in str(error_data).lower():
                print("  Region not supported by Gemini")
                return None

        if response.status_code != 200:
            print(f"  Gemini API error {response.status_code}: {response.text[:200]}")
            return None

        result = response.json()

        # Extract image data
        if "candidates" in result:
            for candidate in result.get("candidates", []):
                for part in candidate.get("content", {}).get("parts", []):
                    inline_data = part.get("inline_data") or part.get("inlineData")
                    if inline_data:
                        return inline_data.get("data")

        return None

    def _generate_fal(self, prompt, aspect_ratio, timeout):
        """Generate image using Fal.ai Nano Banana Pro API."""
        api_key = self.secrets.get("FAL_KEY") or os.environ.get("FAL_KEY")
        url = "https://queue.fal.run/fal-ai/nano-banana-pro"

        # Map aspect ratio to Fal's format
        # Fal supports: auto, 21:9, 16:9, 3:2, 4:3, 5:4, 1:1, 4:5, 3:4, 2:3, 9:16
        aspect_ratio_map = {
            "16:9": "16:9",
            "1:1": "1:1",
            "9:16": "9:16",
            "4:3": "4:3",
            "3:2": "3:2"
        }
        fal_aspect_ratio = aspect_ratio_map.get(aspect_ratio, "16:9")

        payload = {
            "prompt": prompt,
            "num_images": 1,
            "aspect_ratio": fal_aspect_ratio,
            "output_format": "png",
            "sync_mode": True  # Request synchronous mode
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Key {api_key}"
        }

        # Submit request
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30
        )

        if response.status_code != 200:
            print(f"  Fal.ai API error {response.status_code}: {response.text[:200]}")
            return None

        result = response.json()

        # Check if request is in queue
        if result.get("status") == "IN_QUEUE" or result.get("status") == "IN_PROGRESS":
            # Poll for result using status endpoint
            request_id = result.get("request_id")
            status_url = result.get("status_url") or f"{url}/requests/{request_id}/status"

            print(f"  Request queued (ID: {request_id}), waiting for completion...")

            # Poll for result with timeout
            start_time = time.time()
            poll_interval = 2  # Start with 2 seconds

            while time.time() - start_time < timeout:
                time.sleep(poll_interval)

                status_response = requests.get(status_url, headers=headers, timeout=30)
                if status_response.status_code != 200:
                    print(f"  Status check error: {status_response.status_code}")
                    time.sleep(poll_interval)
                    continue

                status_data = status_response.json()

                if status_data.get("status") == "COMPLETED":
                    # Get the result
                    response_url = result.get("response_url") or f"{url}/requests/{request_id}"
                    result_response = requests.get(response_url, headers=headers, timeout=30)

                    if result_response.status_code == 200:
                        result_data = result_response.json()
                        # Extract image data
                        if "images" in result_data and len(result_data["images"]) > 0:
                            image_data = result_data["images"][0]

                            if "url" in image_data:
                                image_url = image_data["url"]
                                # Check if it's a data URI (base64)
                                if image_url.startswith("data:image"):
                                    # Extract base64 data from data URI
                                    # Format: data:image/png;base64,<base64_data>
                                    base64_data = image_url.split(",", 1)[1]
                                    return base64_data
                                else:
                                    # Download and convert to base64
                                    try:
                                        img_response = requests.get(image_url, timeout=30)
                                        if img_response.status_code == 200:
                                            return base64.b64encode(img_response.content).decode('utf-8')
                                    except Exception as e:
                                        print(f"  Failed to download image: {e}")
                                        return None

                elif status_data.get("status") in ["FAILED", "CANCELLED"]:
                    error = status_data.get("error", "Unknown error")
                    print(f"  Request {status_data['status']}: {error}")
                    return None
                else:
                    # Still processing, continue polling
                    # Exponentially increase poll interval
                    poll_interval = min(poll_interval * 1.5, 10)
                    continue

            print(f"  Request timed out after {timeout}s")
            return None

        elif result.get("status") == "COMPLETED" and "images" in result:
            # Synchronous response with images
            image_data = result["images"][0]
            if "url" in image_data:
                image_url = image_data["url"]
                # Check if it's a data URI (base64)
                if image_url.startswith("data:image"):
                    # Extract base64 data from data URI
                    base64_data = image_url.split(",", 1)[1]
                    return base64_data
                else:
                    # Download and convert to base64
                    try:
                        img_response = requests.get(image_url, timeout=30)
                        if img_response.status_code == 200:
                            return base64.b64encode(img_response.content).decode('utf-8')
                    except Exception as e:
                        print(f"  Failed to download image: {e}")
                        return None

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


# Backward compatibility: keep GeminiImageGenerator as alias
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
