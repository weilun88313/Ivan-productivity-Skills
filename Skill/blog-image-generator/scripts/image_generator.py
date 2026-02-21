"""
Unified image generation client with fallback support.
Supports multiple image generation APIs: Gemini, Fal.ai Nano Banana Pro.

This module consolidates image generation functionality from:
- blog-writer/scripts/image_generator.py
- linkedin-post-writer/scripts/gemini_api.py
- twitter-post-writer/scripts/gemini_api.py
- jike-post-writer/scripts/gemini_api.py
- pptx/scripts/gemini_api.py
"""

import os
import sys
import json
import requests
import base64
import time

# Initialize environment from .env (with legacy JSON fallback)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "..", "scripts"))
import env_setup; env_setup.init_env()


class ImageGenerator:
    """Unified image generation client with automatic fallback."""

    def __init__(self, secrets_path=None):
        """
        Initialize with API keys from environment variables.

        Args:
            secrets_path: Deprecated, ignored. Keys are loaded from .env.
        """
        self.providers = self._get_available_providers()
        self.model_name = "models/gemini-3-pro-image-preview"

        if not self.providers:
            print("Error: No image generation API keys found.")
            print("Please add to .env in the repository root:")
            print("  GEMINI_API_KEY=your_key")
            print("  FAL_KEY=your_key")
            print("\nSee .env.example for the expected format.")
            sys.exit(1)

        print(f"Available providers: {', '.join(self.providers)}")

    def _get_available_providers(self):
        """Check which image generation providers are available."""
        providers = []

        # Check Gemini
        if os.environ.get("GEMINI_API_KEY"):
            providers.append("gemini")

        # Check Fal.ai
        if os.environ.get("FAL_KEY"):
            providers.append("fal")

        return providers

    def generate(self, prompt, aspect_ratio="16:9", timeout=180, style=None):
        """
        Generate an image with automatic fallback.

        Tries providers in order: Gemini → Fal.ai

        Args:
            prompt: Text prompt for image generation
            aspect_ratio: Image aspect ratio (default: "16:9")
            timeout: Request timeout in seconds (default: 180)
            style: Optional style hint (for logging purposes)

        Returns:
            Base64-encoded image data, or None if all providers failed
        """
        style_str = f" ({style})" if style else ""
        print(f"Generating image{style_str}...")

        for provider in self.providers:
            print(f"  Trying {provider}...")

            try:
                if provider == "gemini":
                    result = self._generate_gemini(prompt, aspect_ratio, timeout)
                elif provider == "fal":
                    result = self._generate_fal(prompt, aspect_ratio, timeout)
                else:
                    continue

                if result:
                    print(f"  ✓ Success with {provider}")
                    return result
                else:
                    print(f"  ✗ {provider} failed, trying next provider...")

            except Exception as e:
                print(f"  ✗ {provider} error: {e}")
                continue

        print("  ✗ All providers failed")
        return None

    def _generate_gemini(self, prompt, aspect_ratio, timeout):
        """
        Generate image using Gemini API.

        Args:
            prompt: Text prompt for image generation
            aspect_ratio: Image aspect ratio
            timeout: Request timeout in seconds

        Returns:
            Base64-encoded image data, or None if failed
        """
        api_key = os.environ.get("GEMINI_API_KEY")
        model = "models/gemini-3-pro-image-preview"
        url = f"https://generativelanguage.googleapis.com/v1beta/{model}:generateContent?key={api_key}"

        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseModalities": ["IMAGE"],
                "imageConfig": {"aspectRatio": aspect_ratio}
            }
        }

        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                response = requests.post(
                    url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=timeout
                )

                # Handle rate limiting
                if response.status_code == 429:
                    wait_time = 2 ** attempt
                    print(f"    Rate limited, waiting {wait_time}s... ({attempt}/{max_retries})")
                    time.sleep(wait_time)
                    continue

                # Handle server errors with retry
                if response.status_code >= 500 and attempt < max_retries:
                    wait_time = 2 ** attempt
                    print(f"    Server error {response.status_code}, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue

                # Handle region restrictions
                if response.status_code == 400:
                    error_data = response.json()
                    if "not supported" in str(error_data).lower():
                        print("    Region not supported by Gemini")
                        return None

                if response.status_code != 200:
                    print(f"    Gemini API error {response.status_code}: {response.text[:200]}")
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

            except requests.exceptions.Timeout:
                print(f"    Request timed out ({timeout}s), attempt {attempt}/{max_retries}")
                if attempt < max_retries:
                    time.sleep(2 ** attempt)
            except requests.exceptions.RequestException as e:
                print(f"    Network error: {e}, attempt {attempt}/{max_retries}")
                if attempt < max_retries:
                    time.sleep(2 ** attempt)

        return None

    def _generate_fal(self, prompt, aspect_ratio, timeout):
        """
        Generate image using Fal.ai Nano Banana Pro API.

        Args:
            prompt: Text prompt for image generation
            aspect_ratio: Image aspect ratio
            timeout: Request timeout in seconds

        Returns:
            Base64-encoded image data, or None if failed
        """
        api_key = os.environ.get("FAL_KEY")
        url = "https://queue.fal.run/fal-ai/nano-banana-pro"

        # Map aspect ratio to Fal's format
        # Fal supports: auto, 21:9, 16:9, 3:2, 4:3, 5:4, 1:1, 4:5, 3:4, 2:3, 9:16
        aspect_ratio_map = {
            "16:9": "16:9",
            "1:1": "1:1",
            "9:16": "9:16",
            "4:3": "4:3",
            "3:2": "3:2",
            "21:9": "21:9"
        }
        fal_aspect_ratio = aspect_ratio_map.get(aspect_ratio, "16:9")

        payload = {
            "prompt": prompt,
            "num_images": 1,
            "aspect_ratio": fal_aspect_ratio,
            "output_format": "png",
            "sync_mode": True
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Key {api_key}"
        }

        # Submit request
        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=30
            )
        except requests.exceptions.RequestException as e:
            print(f"    Request failed: {e}")
            return None

        if response.status_code != 200:
            print(f"    Fal.ai API error {response.status_code}: {response.text[:200]}")
            return None

        result = response.json()

        # Check if request is in queue
        if result.get("status") in ["IN_QUEUE", "IN_PROGRESS"]:
            # Poll for result using status endpoint
            request_id = result.get("request_id")
            status_url = result.get("status_url") or f"{url}/requests/{request_id}/status"

            print(f"    Request queued (ID: {request_id}), waiting...")

            # Poll for result with timeout
            start_time = time.time()
            poll_interval = 2

            while time.time() - start_time < timeout:
                time.sleep(poll_interval)

                try:
                    status_response = requests.get(status_url, headers=headers, timeout=30)
                    if status_response.status_code != 200:
                        time.sleep(poll_interval)
                        continue

                    status_data = status_response.json()

                    if status_data.get("status") == "COMPLETED":
                        # Get the result
                        response_url = result.get("response_url") or f"{url}/requests/{request_id}"
                        result_response = requests.get(response_url, headers=headers, timeout=30)

                        if result_response.status_code == 200:
                            result_data = result_response.json()
                            if "images" in result_data and len(result_data["images"]) > 0:
                                image_data = result_data["images"][0]
                                if "url" in image_data:
                                    return self._download_image_as_base64(image_data["url"])

                    elif status_data.get("status") in ["FAILED", "CANCELLED"]:
                        error = status_data.get("error", "Unknown error")
                        print(f"    Request {status_data['status']}: {error}")
                        return None

                    # Exponentially increase poll interval
                    poll_interval = min(poll_interval * 1.5, 10)

                except requests.exceptions.RequestException:
                    time.sleep(poll_interval)
                    continue

            print(f"    Request timed out after {timeout}s")
            return None

        elif result.get("status") == "COMPLETED" and "images" in result:
            # Synchronous response with images
            image_data = result["images"][0]
            if "url" in image_data:
                return self._download_image_as_base64(image_data["url"])

        return None

    def _download_image_as_base64(self, image_url):
        """Download image from URL and convert to base64."""
        try:
            # Check if it's a data URI (base64)
            if image_url.startswith("data:image"):
                base64_data = image_url.split(",", 1)[1]
                return base64_data
            else:
                # Download and convert to base64
                img_response = requests.get(image_url, timeout=30)
                if img_response.status_code == 200:
                    return base64.b64encode(img_response.content).decode('utf-8')
        except Exception as e:
            print(f"    Failed to download image: {e}")
        return None

    def _load_image_as_base64(self, image_path):
        """Load local image file and convert to base64."""
        try:
            with open(image_path, "rb") as f:
                return base64.b64encode(f.read()).decode('utf-8')
        except Exception as e:
            print(f"    Failed to load image: {e}")
        return None

    def generate_with_image(self, prompt, image_path, aspect_ratio="16:9", timeout=180, style=None):
        """
        Generate image using an input image as reference (image-to-image or editing).

        Uses Fal.ai nano-banana-pro/edit model for image editing with character consistency.

        Args:
            prompt: Text prompt for image generation/editing
            image_path: Path to local image file to use as reference
            aspect_ratio: Image aspect ratio (default: "16:9")
            timeout: Request timeout in seconds (default: 180)
            style: Optional style hint

        Returns:
            Base64-encoded image data, or None if failed
        """
        api_key = os.environ.get("FAL_KEY")

        # Load input image
        image_b64 = self._load_image_as_base64(image_path)
        if not image_b64:
            print("    Failed to load input image")
            return None

        # Use nano-banana-pro/edit for image editing
        url = "https://queue.fal.run/fal-ai/nano-banana-pro/edit"

        # Map aspect ratio
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
            "image_urls": [f"data:image/jpeg;base64,{image_b64}"],
            "aspect_ratio": fal_aspect_ratio,
            "num_images": 1,
            "output_format": "png",
            "resolution": "2K",
            "sync_mode": True
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Key {api_key}"
        }

        style_str = f" ({style})" if style else ""
        print(f"Generating image with reference{style_str}...")

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
        except requests.exceptions.RequestException as e:
            print(f"    Request failed: {e}")
            return None

        if response.status_code != 200:
            print(f"    API error {response.status_code}: {response.text[:200]}")
            return None

        result = response.json()

        # Handle queued request
        if result.get("status") in ["IN_QUEUE", "IN_PROGRESS"]:
            request_id = result.get("request_id")
            status_url = result.get("status_url") or f"{url}/requests/{request_id}/status"

            print(f"    Request queued (ID: {request_id}), waiting...")

            start_time = time.time()
            poll_interval = 2

            while time.time() - start_time < timeout:
                time.sleep(poll_interval)

                try:
                    status_response = requests.get(status_url, headers=headers, timeout=30)
                    if status_response.status_code != 200:
                        time.sleep(poll_interval)
                        continue

                    status_data = status_response.json()

                    if status_data.get("status") == "COMPLETED":
                        response_url = result.get("response_url") or f"{url}/requests/{request_id}"
                        result_response = requests.get(response_url, headers=headers, timeout=30)

                        if result_response.status_code == 200:
                            result_data = result_response.json()
                            if "images" in result_data and len(result_data["images"]) > 0:
                                image_data = result_data["images"][0]
                                if "url" in image_data:
                                    print("    ✓ Success with nano-banana-pro/edit")
                                    return self._download_image_as_base64(image_data["url"])

                    elif status_data.get("status") in ["FAILED", "CANCELLED"]:
                        error = status_data.get("error", "Unknown error")
                        print(f"    Request {status_data['status']}: {error}")
                        return None

                    poll_interval = min(poll_interval * 1.5, 10)

                except requests.exceptions.RequestException:
                    time.sleep(poll_interval)
                    continue

            print(f"    Request timed out after {timeout}s")
            return None

        elif result.get("status") == "COMPLETED" and "images" in result:
            image_data = result["images"][0]
            if "url" in image_data:
                print("    ✓ Success with nano-banana-pro/edit")
                return self._download_image_as_base64(image_data["url"])

        return None

    @staticmethod
    def save(b64_data, filepath):
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

    @staticmethod
    def save_image(b64_data, filepath):
        """Alias for save() for backward compatibility."""
        return ImageGenerator.save(b64_data, filepath)


# Backward compatibility: keep GeminiImageGenerator as alias
class GeminiImageGenerator(ImageGenerator):
    """Backward compatibility alias for existing code."""

    def __init__(self, api_key=None, model_name="models/gemini-3-pro-image-preview"):
        """
        Initialize with backward-compatible API.

        Args:
            api_key: Optional API key (deprecated, uses secrets file)
            model_name: Model name (for compatibility)
        """
        super().__init__()
        self.model_name = model_name
        self.api_key = os.environ.get("GEMINI_API_KEY")

    def generate_image(self, prompt, aspect_ratio="16:9", max_retries=3, timeout=180):
        """
        Generate an image - backward compatible method.

        Args:
            prompt: Text prompt for image generation
            aspect_ratio: Image aspect ratio
            max_retries: Maximum retry attempts (handled internally)
            timeout: Request timeout

        Returns:
            Base64-encoded image data, or None if failed
        """
        return self.generate(prompt, aspect_ratio, timeout)


if __name__ == "__main__":
    # Test the generator
    generator = ImageGenerator()

    test_prompt = """Style: Abstract high-tech visualization inspired by Linear design. Dark mode, minimalist.

Color Palette: Deep charcoal background, glowing violet-blue (#6B75FF) accents.

Concept: Floating geometric data nodes connected by thin glowing lines in dark void.

Environment: Deep black background with subtle technical grid.

Negative Constraints: NO UI elements, NO text, NO dashboards."""

    print("\nTesting image generation...")
    result = generator.generate(test_prompt, style="test")

    if result:
        output = "test_image.png"
        if generator.save(result, output):
            print(f"\n✓ Test image saved to {output}")
        else:
            print("\n✗ Failed to save test image")
    else:
        print("\n✗ Test failed")
