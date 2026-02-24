"""
Images to PowerPoint Converter
Converts a directory of images into a PowerPoint presentation.
Each image becomes a full-bleed slide (16:9 format).
"""

import os
import sys
import argparse
from pptx import Presentation
from pptx.util import Inches


def images_to_pptx(image_dir, output_file):
    """
    Creates a PowerPoint presentation from images in a directory.

    Args:
        image_dir: Directory containing images
        output_file: Output .pptx file path

    Returns:
        Number of slides created, or None if error
    """
    if not os.path.isdir(image_dir):
        print(f"Error: Directory not found: {image_dir}")
        return None

    # Create presentation with 16:9 aspect ratio
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Find all images in directory
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}
    images = [
        f for f in os.listdir(image_dir)
        if os.path.splitext(f)[1].lower() in valid_extensions
    ]

    if not images:
        print(f"Error: No images found in {image_dir}")
        return None

    # Sort images for consistent ordering
    images.sort()

    # Use blank slide layout
    blank_slide_layout = prs.slide_layouts[6]

    # Add each image as a full-bleed slide
    for img_name in images:
        img_path = os.path.join(image_dir, img_name)

        try:
            slide = prs.slides.add_slide(blank_slide_layout)

            # Add image to cover entire slide
            slide.shapes.add_picture(
                img_path,
                0, 0,
                prs.slide_width,
                prs.slide_height
            )

            print(f"✓ Added: {img_name}")

        except Exception as e:
            print(f"✗ Failed to add {img_name}: {e}")

    # Ensure output directory exists
    output_parent = os.path.dirname(output_file)
    if output_parent:
        os.makedirs(output_parent, exist_ok=True)

    # Save presentation
    try:
        prs.save(output_file)
        print(f"\n{'=' * 60}")
        print(f"✓ Presentation saved: {output_file}")
        print(f"  Total slides: {len(prs.slides)}")
        print(f"{'=' * 60}")
        return len(prs.slides)

    except Exception as e:
        print(f"Error saving presentation: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Convert a folder of images to a PowerPoint presentation"
    )
    parser.add_argument("image_dir", help="Directory containing images")
    parser.add_argument("output_file", help="Output .pptx file path")

    args = parser.parse_args()

    # Validate output filename
    if not args.output_file.endswith('.pptx'):
        print("Warning: Output file should have .pptx extension")
        args.output_file += '.pptx'

    # Convert images to PowerPoint
    result = images_to_pptx(args.image_dir, args.output_file)

    if result is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
