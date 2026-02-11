#!/usr/bin/env python3
"""
Generate Twitter-optimized images using Gemini 3 Pro Image API.

Usage:
    python3 generate_twitter_image.py "your prompt" [--aspect-ratio 16:9] [--output twitter_image.png]

Examples:
    # Landscape (recommended for Twitter)
    python3 generate_twitter_image.py "Modern tech infographic showing AI adoption statistics"

    # Square format
    python3 generate_twitter_image.py "Product screenshot mockup" --aspect-ratio 1:1

    # Standard format
    python3 generate_twitter_image.py "Data visualization chart" --aspect-ratio 4:3
"""

import sys
import os
import argparse

# Add current directory to path to import gemini_api
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gemini_api import GeminiImageGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Generate Twitter-optimized images using Gemini 3 Pro Image API"
    )
    parser.add_argument(
        "prompt",
        type=str,
        help="Image generation prompt"
    )
    parser.add_argument(
        "--aspect-ratio",
        type=str,
        default="16:9",
        choices=["16:9", "1:1", "4:3"],
        help="Image aspect ratio (default: 16:9 for Twitter)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="twitter_image.png",
        help="Output file path (default: twitter_image.png)"
    )
    parser.add_argument(
        "--quality",
        type=str,
        default="4K",
        choices=["4K", "HD"],
        help="Image quality (default: 4K)"
    )

    args = parser.parse_args()

    # Enhance prompt for Twitter context
    enhanced_prompt = f"""
Create a visually striking image optimized for Twitter/X social media.

Context: {args.prompt}

Requirements:
- High visual impact and professional quality
- Clear, readable text if any text is included
- Suitable for social media sharing
- Modern, clean design aesthetic
- Optimized for {args.aspect_ratio} aspect ratio

Generate the image with these specifications in mind.
""".strip()

    # Initialize generator
    print("Initializing Gemini 3 Pro Image generator...")
    generator = GeminiImageGenerator()

    # Generate image
    print(f"\nPrompt: {args.prompt}")
    print(f"Aspect ratio: {args.aspect_ratio}")
    print(f"Quality: {args.quality}")
    print("\nGenerating image (this may take 30-90 seconds)...\n")

    image_data = generator.generate_image(
        prompt=enhanced_prompt,
        aspect_ratio=args.aspect_ratio,
        image_size=args.quality
    )

    if not image_data:
        print("\n❌ Failed to generate image.")
        sys.exit(1)

    # Save image
    print(f"Saving image to: {args.output}")
    if generator.save_image(image_data, args.output):
        print(f"\n✅ Image successfully generated: {args.output}")
        print(f"\nYou can now attach this image to your tweet!")
    else:
        print("\n❌ Failed to save image.")
        sys.exit(1)


if __name__ == "__main__":
    main()
