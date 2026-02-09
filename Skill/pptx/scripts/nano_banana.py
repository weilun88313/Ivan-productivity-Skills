"""
Simple command-line tool for generating images with Gemini API.
For testing or single image generation.
"""

import os
import argparse
from gemini_api import GeminiImageGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Generate an image using Gemini API"
    )
    parser.add_argument("--prompt", required=True, help="Text prompt for image generation")
    parser.add_argument("--output_dir", required=True, help="Directory to save the image")
    parser.add_argument("--filename", default="image.png", help="Output filename (default: image.png)")
    parser.add_argument("--model", default="models/gemini-3-pro-image-preview", help="Model name")

    args = parser.parse_args()

    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Initialize generator
    generator = GeminiImageGenerator(model_name=args.model)

    print(f"Generating image with {args.model}...")
    print(f"Prompt: {args.prompt}")

    # Generate image
    b64_data = generator.generate_image(args.prompt)

    if b64_data:
        filepath = os.path.join(args.output_dir, args.filename)
        if generator.save_image(b64_data, filepath):
            print(f"✓ Image saved to {filepath}")
        else:
            print("✗ Failed to save image")
            exit(1)
    else:
        print("✗ Failed to generate image")
        exit(1)


if __name__ == "__main__":
    main()
