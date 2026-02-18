#!/usr/bin/env python3
"""
Batch image generation using unified blog-image-generator.

Usage:
    python scripts/batch.py --platform blog --prompts prompts.json --output_dir images/

Prompts JSON format:
    {
        "images": [
            {
                "type": "cover",
                "prompt": "Email Marketing Best Practices",
                "output": "cover.png"
            },
            {
                "type": "inline",
                "prompt": "Data flow visualization",
                "output": "inline_01.png"
            }
        ]
    }

Or simplified array format:
    {
        "images": [
            "Email Marketing Best Practices",
            "Data flow visualization",
            "User segmentation analysis"
        ]
    }
"""

import argparse
import json
import os
import sys
import time

# Add parent directory to path for imports
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from scripts.image_generator import ImageGenerator
from prompts import BlogPrompts, LinkedInPrompts, TwitterPrompts, JikePrompts, PPTPrompts


def get_prompt(platform, image_type, prompt_text, labels=None, emotion=None, photo_url=None):
    """Get platform-specific prompt template."""
    if platform == "blog":
        if image_type == "cover":
            return BlogPrompts.cover(prompt_text)
        elif image_type == "inline":
            return BlogPrompts.inline(prompt_text)
        elif image_type == "data_cluster":
            return BlogPrompts.data_cluster(prompt_text)
        elif image_type == "data_flow":
            return BlogPrompts.data_flow(prompt_text)
        elif image_type == "segmentation":
            return BlogPrompts.segmentation(prompt_text)
        elif image_type == "temporal":
            return BlogPrompts.temporal(prompt_text)
        else:
            return BlogPrompts.inline(prompt_text)

    elif platform == "linkedin":
        if image_type == "cover":
            return LinkedInPrompts.cover(prompt_text)
        elif image_type == "announcement":
            return LinkedInPrompts.announcement(prompt_text)
        elif image_type == "photo_infographic":
            labels_list = labels.split(',') if labels else None
            return LinkedInPrompts.photo_infographic(prompt_text, emotion or "thinking", labels_list, photo_url)
        elif image_type == "photo_info":
            return LinkedInPrompts.photo_info(prompt_text, photo_url)
        else:
            return LinkedInPrompts.post(prompt_text)

    elif platform == "twitter":
        if image_type == "cover":
            return TwitterPrompts.cover(prompt_text)
        elif image_type == "viral":
            return TwitterPrompts.viral(prompt_text)
        elif image_type == "quote":
            return TwitterPrompts.quote(prompt_text)
        else:
            return TwitterPrompts.tweet(prompt_text)

    elif platform == "jike":
        if image_type == "cover":
            return JikePrompts.cover(prompt_text)
        elif image_type == "discussion":
            return JikePrompts.discussion(prompt_text)
        else:
            return JikePrompts.post(prompt_text)

    elif platform == "pptx":
        return PPTPrompts.cover(prompt_text)

    else:
        return BlogPrompts.cover(prompt_text)


def load_prompts(prompts_file):
    """
    Load prompts from JSON file.

    Args:
        prompts_file: Path to JSON file

    Returns:
        List of image specifications
    """
    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Handle simplified array format
    if isinstance(data, list):
        return [{"prompt": p, "type": "cover", "output": f"image_{i:03d}.png"}
                for i, p in enumerate(data)]

    # Handle full format
    if "images" in data:
        return data["images"]

    # Handle single object format
    if "prompt" in data:
        return [data]

    raise ValueError("Invalid prompts JSON format")


def main():
    parser = argparse.ArgumentParser(
        description="Batch generate images using unified blog-image-generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Prompts JSON format (full):
    {
        "images": [
            {
                "type": "cover",
                "prompt": "Email Marketing",
                "output": "cover.png",
                "aspect_ratio": "16:9"
            }
        ]
    }

Prompts JSON format (simple):
    {
        "images": [
            "Email Marketing",
            "Data Flow",
            "User Segmentation"
        ]
    }
        """
    )

    parser.add_argument(
        "--platform",
        required=True,
        choices=["blog", "linkedin", "twitter", "jike", "pptx"],
        help="Platform to generate images for"
    )
    parser.add_argument(
        "--prompts",
        required=True,
        help="JSON file with prompts (see format in help)"
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory to save generated images"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between API calls in seconds (default: 1.0)"
    )
    parser.add_argument(
        "--default-aspect-ratio",
        default="16:9",
        choices=["16:9", "1:1", "4:3", "9:16", "3:2"],
        help="Default aspect ratio (default: 16:9)"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Request timeout in seconds per image (default: 180)"
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue generating even if some images fail"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show full prompts being used"
    )

    args = parser.parse_args()

    # Validate prompts file
    if not os.path.isfile(args.prompts):
        print(f"Error: Prompts file not found: {args.prompts}")
        return 1

    # Load prompts
    try:
        images = load_prompts(args.prompts)
    except Exception as e:
        print(f"Error loading prompts: {e}")
        return 1

    if not images:
        print("Error: No images found in prompts file")
        return 1

    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    # Initialize generator
    gen = ImageGenerator()

    print(f"Loaded {len(images)} image(s) to generate.")
    print(f"Output directory: {args.output_dir}")
    print(f"Platform: {args.platform}")
    print("=" * 60)

    # Generate images
    success_count = 0
    failed_count = 0

    for i, image_spec in enumerate(images):
        prompt_text = image_spec.get("prompt", "")
        image_type = image_spec.get("type", "cover")
        output_name = image_spec.get("output", f"image_{i:03d}.png")
        aspect_ratio = image_spec.get("aspect_ratio", args.default_aspect_ratio)
        labels = image_spec.get("labels", None)
        emotion = image_spec.get("emotion", "shocked")
        photo_url = image_spec.get("photo_url", None)

        if not prompt_text:
            print(f"\n[{i+1}/{len(images)}] Skipping: No prompt provided")
            failed_count += 1
            continue

        # Get full prompt
        full_prompt = get_prompt(args.platform, image_type, prompt_text, labels, emotion, photo_url)

        if args.verbose:
            print("\n" + "=" * 60)
            print("FULL PROMPT:")
            print("=" * 60)
            print(full_prompt)
            print("=" * 60)

        # Generate
        print(f"\n[{i+1}/{len(images)}] Generating: {output_name}")
        print(f"  Type: {image_type}")
        print(f"  Prompt: {prompt_text[:60]}{'...' if len(prompt_text) > 60 else ''}")
        print(f"  Aspect ratio: {aspect_ratio}")

        image_data = gen.generate(
            full_prompt,
            aspect_ratio=aspect_ratio,
            timeout=args.timeout,
            style=args.platform
        )

        if image_data:
            output_path = os.path.join(args.output_dir, output_name)
            if gen.save(image_data, output_path):
                print(f"  ✓ Saved: {output_path}")
                success_count += 1
            else:
                print(f"  ✗ Failed to save")
                failed_count += 1
                if not args.continue_on_error:
                    break
        else:
            print(f"  ✗ Failed to generate")
            failed_count += 1
            if not args.continue_on_error:
                break

        # Rate limiting
        if i < len(images) - 1:
            time.sleep(args.delay)

    # Summary
    print("\n" + "=" * 60)
    print(f"Batch generation complete:")
    print(f"  ✓ Success: {success_count}/{len(images)}")
    print(f"  ✗ Failed: {failed_count}/{len(images)}")

    if failed_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
