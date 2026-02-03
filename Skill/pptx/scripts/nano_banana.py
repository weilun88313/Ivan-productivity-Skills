
import os
import argparse
import requests
import base64
import time

API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyC7mreVvH_q7djnEO4MWlP94QaMEKmmz2Y")

# User strictly requested Nano Banana Pro (Gemini 3 Pro)
MODEL_NAME = "models/gemini-3-pro-image-preview" 

def generate_image(prompt, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Generating image with {MODEL_NAME}...")

    headers = {"Content-Type": "application/json"}
    
    # Determine endpoint and payload based on model family
    if "gemini" in MODEL_NAME:
        url = f"https://generativelanguage.googleapis.com/v1beta/{MODEL_NAME}:generateContent?key={API_KEY}"
        payload = {
          "contents": [{"parts": [{"text": prompt}]}],
          "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "16:9"}
          }
        }
    else:
        # Assume Imagen style (predict)
        url = f"https://generativelanguage.googleapis.com/v1beta/{MODEL_NAME}:predict?key={API_KEY}"
        payload = {
            "instances": [{"prompt": prompt}],
            "parameters": {"sampleCount": 1, "aspectRatio": "16:9"}
        }

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            # Fallback logic could go here
            return

        result = response.json()
        
        # Handle Gemini structure
        if "candidates" in result:
            for i, cand in enumerate(result.get('candidates', [])):
                for part in cand.get('content', {}).get('parts', []):
                    # Handle both snake_case and camelCase keys
                    inline_data = part.get('inline_data') or part.get('inlineData')
                    if inline_data:
                        save_image(inline_data.get('data'), output_dir, i)
                        return # Save first and exit
        
        # Handle Imagen structure
        elif "predictions" in result:
            for i, pred in enumerate(result.get('predictions', [])):
                b64 = pred.get('bytesBase64Encoded', pred)
                save_image(b64, output_dir, i)
                return

        print("No image data found in response.")
        print(result)

    except Exception as e:
        print(f"Exception: {e}")

def save_image(b64_data, output_dir, index):
    try:
        img_data = base64.b64decode(b64_data)
        timestamp = int(time.time())
        filename = f"image_{timestamp}_{index}.png"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "wb") as f:
            f.write(img_data)
        print(f"Saved image to {filepath}")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--output_dir", required=True)
    args = parser.parse_args()
    generate_image(args.prompt, args.output_dir)
