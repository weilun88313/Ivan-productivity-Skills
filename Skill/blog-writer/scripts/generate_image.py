"""
Blog image generation script.
Generates high-quality illustrations for HubSpot-style blog posts.
"""

import os
import time
import argparse
from gemini_api import GeminiImageGenerator


def generate_blog_image(prompt, output_dir, filename_prefix="blog_image"):
    """
    Generate a single blog image.

    Args:
        prompt: Image generation prompt
        output_dir: Directory to save the image
        filename_prefix: Prefix for the output filename

    Returns:
        Path to the generated image, or None if failed
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Initialize generator
    generator = GeminiImageGenerator()

    print(f"Generating image with {generator.model_name}...")
    print(f"Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")

    # Generate image
    b64_data = generator.generate_image(prompt, aspect_ratio="16:9", timeout=180)

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
        description="Generate high-quality blog post illustrations"
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Detailed image generation prompt"
    )
    parser.add_argument(
        "--output_dir",
        default=".",
        help="Directory to save the image (default: current directory)"
    )
    parser.add_argument(
        "--filename",
        default="blog_image",
        help="Filename prefix (default: blog_image)"
    )

    args = parser.parse_args()

    # Generate image
    result = generate_blog_image(args.prompt, args.output_dir, args.filename)

    if result:
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
