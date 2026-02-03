
import os
import argparse
import requests
import base64
import time
import json
import sys

# Default API Key (User provided)
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyC7mreVvH_q7djnEO4MWlP94QaMEKmmz2Y")

# Model
MODEL_NAME = "models/gemini-3-pro-image-preview"

# Brand Guidelines Injection
# This suffix is automatically appended to every prompt
BRAND_PROMPT_SUFFIX = (
    ". Style: Technical data visualization and conceptual schematic, inspired by Linear design. "
    "Clean, dark mode, matte finish. High-tech blueprint aesthetic but minimalist. "
    "Color Palette: Deep charcoal background. Data structures are slightly lighter matte grey. "
    "Primary accent color is #6B75FF (violet-blue) for key highlights, connections, and active data points. "
    "CRITICAL CONSTRAINT: NO PRODUCT UI CHROME. Do not render navigation bars, sidebars, browser frames, buttons, or dashboard widgets. "
    "VISUAL STRUCTURE: Visualize the content as floating data clusters, interconnected nodes, stacks of conceptual information cards, or abstract flow diagrams suspended in a dark void. "
    "TEXT STRATEGY: KEYWORDS: Only keep the title and tag text, no more detailed descriptive text is needed. "
    "MICRO-DETAILS: Add small, clean icons, tiny status dots (e.g., purple dot for active), and thin connecting lines to create a sense of rich information structure. "
    "Environment: Floating in a deep dark void. Extremely subtle, barely visible technical grid lines in the background. "
    "Resolution: 4K resolution (3840x2160), ultra high detail, sharp and crisp rendering. "
    "Negative Constraints: NO navigation bars, NO dashboards, NO browser frames, NO menus, NO fake app interfaces. NO blurry text. No detailed descriptive text. Keep it clean and structured."
)

def generate_image(prompt, output_dir, filename_prefix="image"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Enhance prompt
    enhanced_prompt = prompt + BRAND_PROMPT_SUFFIX
    print(f"[DEBUG] Full prompt: {enhanced_prompt}")
    print(f"Generating: {enhanced_prompt[:80]}...")

    headers = {"Content-Type": "application/json"}
    url = f"https://generativelanguage.googleapis.com/v1beta/{MODEL_NAME}:generateContent?key={API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": enhanced_prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "16:9"}
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            return

        result = response.json()
        
        if "candidates" in result:
            for i, cand in enumerate(result.get('candidates', [])):
                for part in cand.get('content', {}).get('parts', []):
                    inline_data = part.get('inline_data') or part.get('inlineData')
                    if inline_data:
                        save_image(inline_data.get('data'), output_dir, filename_prefix)
                        return
                    
        print(f"No image data found for {filename_prefix}")
        # print(result) # Silent failure preferred to reduce noise, enable if debugging needed

    except Exception as e:
        print(f"Exception: {e}")

def save_image(b64_data, output_dir, filename_prefix):
    try:
        img_data = base64.b64decode(b64_data)
        # Use simple numeric ordering if possible, or prefix
        filepath = os.path.join(output_dir, f"{filename_prefix}.png")
        with open(filepath, "wb") as f:
            f.write(img_data)
        print(f"Saved: {filepath}")
    except Exception as e:
        print(f"Error saving image: {e}")

def main():
    parser = argparse.ArgumentParser(description="Generate PPT images from a Plan JSON")
    parser.add_argument("plan_file", help="Path to the parameters/plan JSON file")
    parser.add_argument("output_dir", help="Directory to save images")
    
    args = parser.parse_args()
    
    with open(args.plan_file, 'r', encoding='utf-8') as f:
        plan = json.load(f)
        
    print(f"Loaded plan with {len(plan)} slides.")
    
    for slide in plan:
        # New format: {"slide_number": 1, "title": "...", "content": [...], "image_concept": "..."}
        # Legacy format: {"id": "slide_1", "prompt": "..."}
        
        slide_number = slide.get("slide_number")
        title = slide.get("title", "")
        content = slide.get("content", [])
        image_concept = slide.get("image_concept")
        
        # Fallback to legacy format if new format not found
        if not image_concept:
            image_concept = slide.get("prompt", "")
            slide_id = slide.get("id", f"slide_{slide_number}")
            full_prompt = image_concept  # Legacy format already has full prompt
        else:
            slide_id = f"slide_{slide_number:02d}"
            
            # Construct full prompt with text overlay instructions
            text_overlay = f"Professional presentation slide with title '{title}' in large bold text at top"
            
            if content:
                # Add content points
                content_text = ", ".join(content[:3])  # Limit to first 3 points for clarity
                text_overlay += f", key points displayed: {content_text}"
            
            # Combine: [Text Instructions] + [Visual Background] + [Brand Style]
            full_prompt = f"{text_overlay}, visual background: {image_concept}"
        
        if full_prompt:
            generate_image(full_prompt, args.output_dir, slide_id)
            time.sleep(1) # Rate limit courtesy
        else:
            print(f"Warning: No image_concept or prompt found for slide {slide_number or slide.get('id')}")

if __name__ == "__main__":
    main()
