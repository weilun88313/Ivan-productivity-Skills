"""
Visual style definitions for blog-image-generator.

This module exports all style configurations:

    from Skill.blog_image_generator.styles import (
        get_style,
        STYLE_LINEAR_BLOG,
        STYLE_LINKEDIN,
        STYLE_TWITTER,
        STYLE_JIKE,
        STYLE_PPTX
    )
"""

from .common import (
    COLOR_ACCENT,
    COLOR_BG_DARK,
    COLOR_BG_BLACK,
    ASPECT_RATIOS
)
from .linear import STYLE_LINEAR_BLOG
from .linkedin import STYLE_LINKEDIN
from .twitter import STYLE_TWITTER
from .jike import STYLE_JIKE
from .pptx import STYLE_PPTX

__all__ = [
    "COLOR_ACCENT",
    "COLOR_BG_DARK",
    "COLOR_BG_BLACK",
    "ASPECT_RATIOS",
    "STYLE_LINEAR_BLOG",
    "STYLE_LINKEDIN",
    "STYLE_TWITTER",
    "STYLE_JIKE",
    "STYLE_PPTX",
    "get_style",
]


def get_style(platform):
    """
    Get style configuration for a platform.

    Args:
        platform: Platform name (blog, linkedin, twitter, jike, pptx)

    Returns:
        Style configuration dictionary
    """
    styles = {
        "blog": STYLE_LINEAR_BLOG,
        "linkedin": STYLE_LINKEDIN,
        "twitter": STYLE_TWITTER,
        "jike": STYLE_JIKE,
        "pptx": STYLE_PPTX,
    }
    return styles.get(platform.lower(), STYLE_LINEAR_BLOG)
