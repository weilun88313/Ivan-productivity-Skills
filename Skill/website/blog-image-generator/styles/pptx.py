"""
PowerPoint style configuration.

Linear presentation style for PPT slides with Chinese language support.
"""

from .common import COLOR_ACCENT, COLOR_BG_DARK, COLOR_BG_BLACK

STYLE_PPTX = {
    "name": "Linear Presentation (PPT)",
    "description": "Linear technical aesthetic for presentation slides, Chinese language",

    # Colors
    "background": COLOR_BG_BLACK,  # Deep black gradient
    "background_secondary": COLOR_BG_DARK,  # Deep charcoal
    "accent": COLOR_ACCENT,  # Violet-blue for highlights
    "accent_name": "紫蓝色 (violet-blue)",

    # Text colors
    "title_color": "#FFFFFF",  # Pure white
    "content_color": "#E6E6E6",  # 90% white

    # Style characteristics
    "mode": "dark",
    "quality": "expert presentation designer",
    "finish": "matte surface, no gloss, technical feel",
    "lighting": "soft ambient light, subtle ray-traced reflections",

    # Visual elements
    "elements": [
        "floating geometric shapes",
        "cubes",
        "spheres",
        "hexagons",
        "abstract data structures",
        "connecting lines with glow effect",
        "3D bar charts",
        "ring charts",
        "network node diagrams"
    ],

    # Environment
    "environment": {
        "type": "deep space background",
        "grid": "extremely subtle technical grid lines (5% opacity)",
        "depth": "soft shadows creating floating hover effect",
        "whitespace": "generous whitespace, avoid crowding"
    },

    # Typography rules
    "typography": {
        "title": "bold modern sans-serif, pure white, eye-catching",
        "content": "regular weight, 90% white, clear and readable",
        "line_spacing": "1.5x for content",
        "alignment": "left-aligned (cover and closing centered)",
        "separation": "use blank lines or visual elements, no bullet points"
    },

    # Technical specs
    "aspect_ratio": "16:9",
    "resolution": "4K",  # High quality for presentations
    "render_quality": "ultra-high detail, sharp and clear",

    # Language
    "language": "Chinese",
    "font_style": "modern sans-serif, supports Chinese characters",

    # Slide types
    "slide_types": {
        "cover": "centered or upper-left composition, large bold title",
        "content": "free creative layout, text and visuals naturally integrated",
        "data": "data-driven creative layout, numbers and visual narrative integrated",
        "closing": "centered symmetrical composition, fade-out effect"
    },

    # Constraints
    "negative_constraints": [
        "NO bullet points in content",
        "NO isolated text blocks",
        "NO cramped layouts"
    ],

    # Design principles
    "design_principles": [
        "Text is part of visual design, not isolated blocks",
        "Visual elements can surround or embed text",
        "Text can have gradients, glow, shadow effects to blend with background",
        "Background and foreground should be coordinated",
        "Use blank lines or visual elements to separate points naturally"
    ],

    # Use cases
    "use_cases": ["pptx_cover", "pptx_content", "pptx_data", "pptx_closing"]
}
