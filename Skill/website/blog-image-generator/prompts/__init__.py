"""
Platform-specific prompt templates for blog-image-generator.

This module exports all prompt template classes for easy import:

    from Skill.blog_image_generator.prompts import (
        BlogPrompts,
        LinkedInPrompts,
        TwitterPrompts,
        JikePrompts,
        PPTPrompts
    )
"""

from .base import BasePrompts
from .blog import BlogPrompts
from .linkedin import LinkedInPrompts
from .twitter import TwitterPrompts
from .jike import JikePrompts
from .pptx import PPTPrompts

__all__ = [
    "BasePrompts",
    "BlogPrompts",
    "LinkedInPrompts",
    "TwitterPrompts",
    "JikePrompts",
    "PPTPrompts",
]
