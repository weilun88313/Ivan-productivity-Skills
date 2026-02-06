import os
import argparse
import requests
import base64
import time
import json

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    try:
        with open(os.path.expanduser("~/.claude/lensmor_secrets.json"), "r") as f:
            secrets = json.load(f)
            API_KEY = secrets.get("NANO_API_KEY")
    except Exception:
        pass

MODEL_NAME = "gemini-3-pro-image-preview"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"
MAX_RETRIES = 3
TIMEOUT = 60


def generate_image(prompt, output_dir):
    if not API_KEY:
        print("Error: GEMINI_API_KEY not set and not found in ~/.claude/lensmor_secrets.json")
        return None

    os.makedirs(output_dir, exist_ok=True)

    print(f"Generating image with {MODEL_NAME}...")
    print(f"Prompt: {prompt}")

    headers = {"Content-Type": "application/json"}
    url = f"{API_URL}?key={API_KEY}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "16:9"},
        },
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)

            if response.status_code >= 500 and attempt < MAX_RETRIES:
                wait = 2**attempt
                print(f"Server error {response.status_code}, retrying in {wait}s... ({attempt}/{MAX_RETRIES})")
                time.sleep(wait)
                continue

            if response.status_code != 200:
                print(f"Error {response.status_code}: {response.text}")
                return None

            result = response.json()

            if "candidates" in result:
                for i, cand in enumerate(result.get("candidates", [])):
                    for part in cand.get("content", {}).get("parts", []):
                        inline_data = part.get("inline_data") or part.get("inlineData")
                        if inline_data:
                            return save_image(inline_data.get("data"), output_dir, i)

            print("No image data found in response.")
            print(result)
            return None

        except requests.exceptions.Timeout:
            print(f"Request timed out ({TIMEOUT}s), attempt {attempt}/{MAX_RETRIES}")
            if attempt < MAX_RETRIES:
                time.sleep(2**attempt)
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}, attempt {attempt}/{MAX_RETRIES}")
            if attempt < MAX_RETRIES:
                time.sleep(2**attempt)

    print("All retries exhausted.")
    return None


def save_image(b64_data, output_dir, index):
    try:
        img_data = base64.b64decode(b64_data)
        timestamp = int(time.time())
        filename = f"blog_image_{timestamp}_{index}.png"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "wb") as f:
            f.write(img_data)
        print(f"Saved image to {filepath}")
        return filepath
    except Exception as e:
        print(f"Error saving image: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True, help="Image generation prompt")
    parser.add_argument("--output_dir", default=".", help="Directory to save the image")
    args = parser.parse_args()

    generate_image(args.prompt, args.output_dir)
