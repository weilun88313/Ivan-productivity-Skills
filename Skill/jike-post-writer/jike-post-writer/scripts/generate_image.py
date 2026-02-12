#!/usr/bin/env python3
"""
Generate images using Gemini API for Jike posts.
"""

import os
import sys
import time
import argparse
from pathlib import Path
from gemini_api import GeminiImageGenerator


def enhance_prompt_for_jike(post_content: str, style_hints: str = None) -> str:
    """Enhance image prompt for Jike post style."""
    base_prompt = f"Create a visually appealing image for a social media post about: {post_content[:200]}"

    style_guide = """
    Style requirements:
    - Clean, fresh, modern aesthetic
    - Warm and approachable feel (not corporate)
    - High resolution, 2K quality
    - 1:1 square format
    - Minimal or no text overlay
    - Bright, warm color palette
    - Suitable for casual social media
    - Illustration or photography style, avoid stock photo feel
    """

    if style_hints:
        style_guide += f"\nAdditional style: {style_hints}"

    return f"{base_prompt}\n\n{style_guide}"


def generate_jike_image(prompt, output_dir, filename_prefix="jike_post", aspect_ratio="1:1"):
    """Generate a Jike post image."""
    os.makedirs(output_dir, exist_ok=True)

    generator = GeminiImageGenerator()

    print(f"Generating image with {generator.model_name}...")
    print(f"Aspect ratio: {aspect_ratio}")
    print(f"Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")

    b64_data = generator.generate_image(prompt, aspect_ratio=aspect_ratio, timeout=180)

    if not b64_data:
        print("Failed to generate image")
        return None

    timestamp = int(time.time())
    filename = f"{filename_prefix}_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    if generator.save_image(b64_data, filepath):
        print(f"Image saved to {filepath}")
        return filepath
    else:
        print("Failed to save image")
        return None


def main():
    parser = argparse.ArgumentParser(description="Generate images for Jike posts using Gemini API")
    parser.add_argument("--prompt", required=True, help="Image description")
    parser.add_argument("--output_dir", default="/Users/ivan/Documents/Ivan_Skills/workspace",
                        help="Output directory")
    parser.add_argument("--filename", default="jike_post", help="Filename prefix")
    parser.add_argument("--aspect-ratio", default="1:1", help="Aspect ratio (default: 1:1)")
    parser.add_argument("--enhance", action="store_true", help="Enhance prompt for Jike style")
    parser.add_argument("--style", help="Additional style hints")

    args = parser.parse_args()

    prompt = args.prompt
    if args.enhance:
        prompt = enhance_prompt_for_jike(args.prompt, args.style)
        print(f"Enhanced prompt:\n{prompt}\n")
        print("-" * 60)

    result = generate_jike_image(prompt, args.output_dir, args.filename, aspect_ratio=args.aspect_ratio)

    if result:
        print(f"\nImage generation complete!")
        exit(0)
    else:
        print(f"\nImage generation failed")
        exit(1)


if __name__ == "__main__":
    main()
