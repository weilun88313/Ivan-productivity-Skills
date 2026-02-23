#!/usr/bin/env python3
"""
Generate images using unified blog-image-generator.

Usage:
    python scripts/generate.py --platform blog --type cover --prompt "..." --output image.py

Examples:
    # Blog cover image
    python scripts/generate.py --platform blog --type cover --prompt "Email Marketing" --output cover.png

    # LinkedIn post image
    python scripts/generate.py --platform linkedin --type post --prompt "New product launch" --output linkedin.png

    # Twitter image with custom aspect ratio
    python scripts/generate.py --platform twitter --type post --prompt "Viral tweet" --output tweet.png --aspect-ratio 1:1
"""

import argparse
import sys
import os

# Add parent directory to path for imports
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from scripts.image_generator import ImageGenerator
from prompts import BlogPrompts, LinkedInPrompts, TwitterPrompts, JikePrompts, PPTPrompts


def get_prompt(platform, image_type, prompt_text, labels=None, emotion=None, photo_url=None):
    """
    Get platform-specific prompt template.

    Args:
        platform: Platform name (blog, linkedin, twitter, jike, pptx)
        image_type: Image type (cover, inline, post, slide, photo_infographic, photo_info)
        prompt_text: User-provided prompt text
        labels: Optional list of labels for photo_infographic style
        emotion: Optional emotion for photo_infographic style
        photo_url: Optional photo URL for photo_infographic or photo_info styles

    Returns:
        Complete prompt string
    """
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
        if image_type == "slide":
            # For PPT, prompt_text is expected to be a JSON string or simple title
            return PPTPrompts.cover(prompt_text)  # Default to cover
        else:
            return PPTPrompts.cover(prompt_text)

    else:
        # Fallback to blog style
        return BlogPrompts.cover(prompt_text)


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using unified blog-image-generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Blog cover image
  %(prog)s --platform blog --type cover --prompt "Email Marketing" --output cover.png

  # LinkedIn post image
  %(prog)s --platform linkedin --type post --prompt "New product" --output linkedin.png

  # Twitter square image
  %(prog)s --platform twitter --type post --prompt "Viral tweet" --output tweet.png --aspect-ratio 1:1
        """
    )

    parser.add_argument(
        "--platform",
        required=True,
        choices=["blog", "linkedin", "twitter", "jike", "pptx"],
        help="Platform to generate image for"
    )
    parser.add_argument(
        "--type",
        choices=["cover", "inline", "post", "slide", "data_cluster", "data_flow",
                 "segmentation", "temporal", "announcement", "viral", "quote", "discussion",
                 "photo_infographic", "photo_info"],
        default="cover",
        help="Image type (default: cover)"
    )
    parser.add_argument(
        "--labels",
        help="Comma-separated labels for photo_infographic style (e.g., 'AI WINS,300%')"
    )
    parser.add_argument(
        "--emotion",
        default="thinking",
        choices=["thinking", "shocked", "surprised", "excited", "worried", "confused", "headache", "amazed"],
        help="Facial expression for photo_infographic (default: thinking)"
    )
    parser.add_argument(
        "--photo-url",
        help="URL or path to user's photo (for photo_infographic or photo_info styles)"
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Text description or title for the image"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output file path (e.g., image.png)"
    )
    parser.add_argument(
        "--aspect-ratio",
        default="16:9",
        choices=["16:9", "1:1", "4:3", "9:16", "3:2"],
        help="Image aspect ratio (default: 16:9)"
    )
    parser.add_argument(
        "--quality",
        default="2K",
        choices=["2K", "4K", "HD"],
        help="Image quality (default: 2K)"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Request timeout in seconds (default: 180)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show full prompt being used"
    )

    args = parser.parse_args()

    # Get platform-specific prompt
    full_prompt = get_prompt(
        args.platform,
        args.type,
        args.prompt,
        labels=getattr(args, 'labels', None),
        emotion=getattr(args, 'emotion', None),
        photo_url=getattr(args, 'photo_url', None)
    )

    if args.verbose:
        print("=" * 60)
        print("FULL PROMPT:")
        print("=" * 60)
        print(full_prompt)
        print("=" * 60)
        print()

    # Initialize generator
    gen = ImageGenerator()

    # Generate image
    print(f"Generating {args.platform} {args.type} image...")
    print(f"Prompt: {args.prompt[:80]}{'...' if len(args.prompt) > 80 else ''}")
    print(f"Aspect ratio: {args.aspect_ratio}")
    print(f"Quality: {args.quality}")

    # Check if using local photo
    photo_url = getattr(args, 'photo_url', None)
    if photo_url and photo_url.startswith('/') and args.type == "photo_infographic":
        # Use image-to-image generation
        print(f"Using photo as CHARACTER REFERENCE: {photo_url}")
        print()

        # For photo_infographic with local photo
        labels = getattr(args, 'labels', 'INSIGHT')
        labels_list = labels.split(',') if labels else ['INSIGHT']
        emotion = getattr(args, 'emotion', 'thinking')

        emotion_prompts = {
            "thinking": "DEEP IN THOUGHT - finger on chin/temple, eyes looking upward, contemplative expression, natural pose",
            "shocked": "GENUINELY SHOCKED - wide eyes, jaw dropped, hands raised in surprise, authentic reaction",
            "surprised": "PLEASANTLY SURPRISED - eyebrows raised, leaning forward slightly with curiosity, genuine expression",
            "excited": "GENUINELY EXCITED - warm enthusiastic smile, eyes bright, natural hand gestures, authentic energy",
            "worried": "THOUGHTFULLY CONCERNED - genuine worried expression, hand near face, concerned but composed",
            "confused": "GENUINELY PUZZLED - squinting slightly, head tilted naturally, questioning expression",
            "headache": "TIRED FROM THINKING - hand rubbing temples naturally, slight frown, eyes closed or looking down",
            "amazed": "GENUINELY AMAZED - eyes wide with wonder, mouth slightly open, hands framing face naturally"
        }

        emotion_instruction = emotion_prompts.get(emotion, emotion_prompts["thinking"])

        edit_prompt = f"""LinkedIn Post Photo Infographic: Use this photo ONLY as CHARACTER REFERENCE. Apple-style aesthetic.

CHARACTER REFERENCE:
- Keep person's FACE and IDENTITY exactly the same
- You MUST CHANGE: expression to {emotion_instruction}
- You CAN CHANGE: pose, camera angle, shot distance
- Make pose natural, confident, intentional

BACKGROUND - APPLE-STYLE SETTING:
- Clean, minimalist environment: modern office or bright neutral space
- Lots of negative space - uncluttered, calm
- Soft diffused natural light - like Apple product photography
- Background gently blurred
- Think "Behind the Mac" campaign aesthetic

GRAPHICS - APPLE MINIMALISM:
- Text: clean sans-serif (SF Pro style), generous letter-spacing
- Labels: {', '.join(labels_list[:3])}
- One primary label prominent, others smaller if multiple
- Position with generous whitespace - don't crowd
- Ultra-precise alignment

Color (Apple rules):
- Primary: white text OR #1D1D1F (near-black) text
- ONE accent color max: #0071E3 (blue) OR #FF6B35 (orange) OR #00D68F (green)
- Background overlays: white 90% opacity (soft blur) OR black 75%
- Ultra-thin 0.5px lines in #E5E5E5
- Small precise geometric accents only

LAYOUT:
- Generous negative space everywhere
- Elements breathe - no crowding
- Clean horizontal or vertical guide lines
- Balanced composition

INTEGRATION:
- Graphics belong in photo, not added
- Soft multi-layer shadows (large spread, subtle)
- Feather edges naturally
- Unified color grade

STYLE: Premium, minimalist, intentional. Apple product launch feel.
TOPIC: {args.prompt}

QUALITY: Refined, sophisticated, confident"""

        image_data = gen.generate_with_image(
            edit_prompt,
            photo_url,
            aspect_ratio=args.aspect_ratio,
            timeout=args.timeout,
            style=args.platform
        )
    else:
        print()
        image_data = gen.generate(
            full_prompt,
            aspect_ratio=args.aspect_ratio,
            timeout=args.timeout,
            style=args.platform
        )

    if not image_data:
        print("\n❌ Failed to generate image.")
        return 1

    # Save image
    print(f"\nSaving to: {args.output}")
    if gen.save(image_data, args.output):
        print(f"✅ Image successfully generated: {args.output}")
        return 0
    else:
        print(f"❌ Failed to save image.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
