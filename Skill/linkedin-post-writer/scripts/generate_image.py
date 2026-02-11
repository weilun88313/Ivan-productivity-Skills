#!/usr/bin/env python3
"""
Generate images using Gemini API for LinkedIn posts.

This script generates images based on text prompts using Google's Gemini 3 Pro Image API.
"""

import os
import sys
import time
import argparse
from pathlib import Path
from gemini_api import GeminiImageGenerator


def enhance_prompt_for_linkedin(post_content: str, style_hints: str = None) -> str:
    """
    Enhance the image prompt based on LinkedIn post content and style.

    Args:
        post_content: The LinkedIn post text
        style_hints: Additional style guidance (optional)

    Returns:
        str: Enhanced prompt for image generation
    """
    base_prompt = f"Create a professional, engaging image for a LinkedIn post about: {post_content[:200]}"

    # Add LinkedIn-specific style guidance
    style_guide = """
    Style requirements for LinkedIn:
    - Professional yet approachable aesthetic
    - Clean, modern, minimalist design
    - Suitable for business social media
    - High resolution, 2K quality, professional photography quality
    - Ultra-detailed, sharp, crisp imagery
    - Use relevant icons or visual metaphors
    - Vibrant but professional color palette (blues, teals, oranges)
    - 16:9 widescreen format optimized for LinkedIn
    - Avoid text overlay or keep minimal
    - Premium quality suitable for professional presentations
    """

    if style_hints:
        style_guide += f"\nAdditional style hints: {style_hints}"

    return f"{base_prompt}\n\n{style_guide}"


def generate_linkedin_image(prompt, output_dir, filename_prefix="linkedin_post", aspect_ratio="16:9"):
    """
    Generate a LinkedIn post image.

    Args:
        prompt: Image generation prompt
        output_dir: Directory to save the image
        filename_prefix: Prefix for the output filename
        aspect_ratio: Image aspect ratio (default: "16:9" for LinkedIn posts)

    Returns:
        Path to the generated image, or None if failed
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Initialize generator
    generator = GeminiImageGenerator()

    print(f"Generating LinkedIn image with {generator.model_name}...")
    print(f"Aspect ratio: {aspect_ratio}")
    print(f"Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")

    # Generate image with specified aspect ratio
    b64_data = generator.generate_image(prompt, aspect_ratio=aspect_ratio, timeout=180)

    if not b64_data:
        print("✗ Image generation failed")
        return None

    # Save image with timestamp
    timestamp = int(time.time())
    filename = f"{filename_prefix}_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    if generator.save_image(b64_data, filepath):
        print(f"✓ Image saved to {filepath}")
        return filepath
    else:
        print("✗ Failed to save image")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate images for LinkedIn posts using Gemini API"
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Text description of the image to generate"
    )
    parser.add_argument(
        "--output_dir",
        default="/Users/ivan/Documents/Ivan_Skills/workspace",
        help="Directory to save the image (default: /Users/ivan/Documents/Ivan_Skills/workspace)"
    )
    parser.add_argument(
        "--filename",
        default="linkedin_post",
        help="Filename prefix (default: linkedin_post)"
    )
    parser.add_argument(
        "--aspect-ratio",
        default="16:9",
        help="Image aspect ratio (default: 16:9, also supports 1:1, 4:3, etc.)"
    )
    parser.add_argument(
        "--enhance",
        help="Enhance prompt for LinkedIn style",
        action="store_true"
    )
    parser.add_argument(
        "--style",
        help="Additional style hints for image generation"
    )

    args = parser.parse_args()

    # Prepare prompt
    prompt = args.prompt
    if args.enhance:
        prompt = enhance_prompt_for_linkedin(args.prompt, args.style)
        print(f"Enhanced prompt:\n{prompt}\n")
        print("-" * 60)

    # Generate image
    result = generate_linkedin_image(
        prompt,
        args.output_dir,
        args.filename,
        aspect_ratio=args.aspect_ratio
    )

    if result:
        print(f"\n✓ Image generation complete!")
        exit(0)
    else:
        print(f"\n✗ Image generation failed")
        exit(1)


if __name__ == "__main__":
    main()
