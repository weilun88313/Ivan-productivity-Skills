"""
Base prompt templates for image generation.

This module provides the foundation for all platform-specific prompts.
"""

from abc import ABC, abstractmethod


class BasePrompts(ABC):
    """Base class for all platform-specific prompt templates."""

    # Shared visual constants
    COLOR_ACCENT = "#6B75FF"  # Violet-blue
    COLOR_BG_DARK = "#1a1a1a"  # Deep charcoal
    COLOR_BG_BLACK = "#0a0a0a"  # Nearly black

    # Common negative constraints
    NEGATIVE_CONSTRAINTS_COMMON = [
        "NO UI chrome",
        "NO navigation bars",
        "NO sidebars",
        "NO buttons",
        "NO browser frames"
    ]

    @classmethod
    @abstractmethod
    def cover(cls, title, **kwargs):
        """Generate a cover image prompt."""
        pass

    @classmethod
    @abstractmethod
    def inline(cls, content, **kwargs):
        """Generate an inline image prompt."""
        pass


class PromptBuilder:
    """Helper class for building structured prompts."""

    @staticmethod
    def build(style="", colors="", concept="", keywords="", environment="", negative=""):
        """
        Build a complete 5-paragraph prompt template.

        Args:
            style: Style description (paragraph 1)
            colors: Color palette (paragraph 2)
            concept: Concept description (paragraph 3)
            keywords: Allowed keywords (paragraph 4)
            environment: Environment description (paragraph 5)
            negative: Negative constraints (paragraph 6)

        Returns:
            Complete prompt string
        """
        paragraphs = []
        if style:
            paragraphs.append(f"Style: {style}")
        if colors:
            paragraphs.append(f"Color Palette: {colors}")
        if concept:
            paragraphs.append(f"Concept: {concept}")
        if keywords:
            paragraphs.append(f"Keywords Allowed: {keywords}")
        if environment:
            paragraphs.append(f"Environment: {environment}")
        if negative:
            paragraphs.append(f"Negative Constraints: {negative}")

        return "\n\n".join(paragraphs)

    @staticmethod
    def escape_for_xml(text):
        """Escape special characters for XML/API requests."""
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
