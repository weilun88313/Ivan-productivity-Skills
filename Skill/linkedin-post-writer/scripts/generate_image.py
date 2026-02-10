#!/usr/bin/env python3
"""
Generate images using Gemini API for LinkedIn posts.

This script generates images based on text prompts using Google's Gemini 3 Pro Image API.
"""

import os
import sys
import json
import argparse
import requests
from pathlib import Path


def generate_image(prompt: str, api_key: str, output_path: str = None, model: str = "gemini-3-pro") -> dict:
    """
    Generate an image using Gemini API.

    Args:
        prompt: Text description of the image to generate
        api_key: Gemini API key
        output_path: Path to save the generated image (optional)
        model: Gemini model to use (default: gemini-3-pro)

    Returns:
        dict: Response containing image data and metadata
    """

    # Gemini API endpoint (Note: As of Jan 2025, Gemini primarily focuses on text/vision understanding
    # For image generation, you might want to use Imagen API or similar services)
    # This is a placeholder structure - adjust based on actual API availability
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

    headers = {
        "Content-Type": "application/json",
    }

    # Construct the request body
    data = {
        "contents": [{
            "parts": [{
                "text": f"Generate an image: {prompt}"
            }]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 2048,
        }
    }

    # Add API key to URL
    url_with_key = f"{url}?key={api_key}"

    try:
        response = requests.post(url_with_key, headers=headers, json=data, timeout=60)
        response.raise_for_status()

        result = response.json()

        # Extract image data from response (structure depends on actual API)
        # This is a placeholder - adjust based on actual response format
        if output_path:
            # Save image to file
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)

            # If response contains base64 image data
            if 'image' in result:
                import base64
                image_data = base64.b64decode(result['image'])
                with open(output_path, 'wb') as f:
                    f.write(image_data)
                print(f"✓ Image saved to: {output_path}")

        return result

    except requests.exceptions.RequestException as e:
        print(f"✗ Error calling Gemini API: {e}", file=sys.stderr)
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


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

    # Add style guidance
    style_guide = """
    Style requirements:
    - Professional yet approachable aesthetic
    - Clean, modern design
    - Suitable for business social media
    - High quality, visually appealing
    - Include relevant icons or visual metaphors
    - Use vibrant but professional colors
    """

    if style_hints:
        style_guide += f"\nAdditional style hints: {style_hints}"

    return f"{base_prompt}\n\n{style_guide}"


def main():
    parser = argparse.ArgumentParser(
        description="Generate images for LinkedIn posts using Gemini API"
    )
    parser.add_argument(
        "prompt",
        help="Text description of the image to generate"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path for the generated image",
        default="generated_image.png"
    )
    parser.add_argument(
        "-k", "--api-key",
        help="Gemini API key (or set GEMINI_API_KEY environment variable)",
        default=os.getenv("GEMINI_API_KEY")
    )
    parser.add_argument(
        "-m", "--model",
        help="Gemini model to use",
        default="gemini-3-pro"
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

    # Validate API key
    if not args.api_key:
        print("✗ Error: Gemini API key required. Set GEMINI_API_KEY environment variable or use --api-key", file=sys.stderr)
        sys.exit(1)

    # Prepare prompt
    prompt = args.prompt
    if args.enhance:
        prompt = enhance_prompt_for_linkedin(args.prompt, args.style)
        print(f"Enhanced prompt: {prompt}\n")

    # Generate image
    print(f"Generating image with Gemini {args.model}...")
    result = generate_image(
        prompt=prompt,
        api_key=args.api_key,
        output_path=args.output,
        model=args.model
    )

    print(f"\n✓ Image generation complete!")
    print(f"Result: {json.dumps(result, indent=2)}")


if __name__ == "__main__":
    main()
