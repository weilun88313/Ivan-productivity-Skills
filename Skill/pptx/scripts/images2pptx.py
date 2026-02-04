
import os
import argparse
from pptx import Presentation
from pptx.util import Inches

def images_to_pptx(image_dir, output_file):
    """
    Creates a PowerPoint presentation from images in a directory.
    Each image becomes a new slide (full bleed).
    Text is already embedded in the AI-generated images.
    """
    prs = Presentation()
    # 16:9 aspect ratio default
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Get all images
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}
    images = [
        f for f in os.listdir(image_dir) 
        if os.path.splitext(f)[1].lower() in valid_extensions
    ]
    images.sort() # Ensure consistent order

    if not images:
        print(f"No images found in {image_dir}")
        return

    blank_slide_layout = prs.slide_layouts[6]

    for img_name in images:
        img_path = os.path.join(image_dir, img_name)
        slide = prs.slides.add_slide(blank_slide_layout)
        
        # Add image to cover the whole slide (full bleed)
        pic = slide.shapes.add_picture(
            img_path, 
            0, 0, 
            prs.slide_width, 
            prs.slide_height
        )
        print(f"Added slide from {img_name}")

    prs.save(output_file)
    print(f"\n✓ Presentation saved to {output_file}")
    print(f"  Total slides: {len(prs.slides)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a folder of images to a PowerPoint presentation."
    )
    parser.add_argument("image_dir", help="Directory containing images")
    parser.add_argument("output_file", help="Output .pptx file path")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.image_dir):
        print(f"Error: Directory {args.image_dir} does not exist.")
        exit(1)
        
    images_to_pptx(args.image_dir, args.output_file)
