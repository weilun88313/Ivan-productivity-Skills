"""
Design System for PPT Generation
Centralized constants for consistent typography and layout across all slides.
"""

from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

# ============================================================================
# TYPOGRAPHY
# ============================================================================

# Font Family (fallback chain)
FONT_FAMILY = "Segoe UI"  # Primary: Segoe UI, fallback to system default

# Title Styling
TITLE_FONT_SIZE = Pt(54)
TITLE_FONT_BOLD = True
TITLE_COLOR = RGBColor(255, 255, 255)  # Pure white

# Content Styling
CONTENT_FONT_SIZE = Pt(28)
CONTENT_LINE_SPACING = 1.5
CONTENT_COLOR = RGBColor(230, 230, 230)  # 90% white for softer look

# Cover Slide Styling
COVER_TITLE_SIZE = Pt(72)
COVER_SUBTITLE_SIZE = Pt(36)
COVER_SUBTITLE_COLOR = RGBColor(180, 180, 180)  # Muted for hierarchy

# Closing Slide Styling
CLOSING_TITLE_SIZE = Pt(60)
CLOSING_CONTENT_SIZE = Pt(32)

# ============================================================================
# LAYOUT (16:9 Slide Dimensions)
# ============================================================================

# Slide Dimensions
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Title Position (Standard Content Slides)
TITLE_TOP_MARGIN = Inches(0.6)
TITLE_LEFT_MARGIN = Inches(0.8)
TITLE_WIDTH = Inches(12)
TITLE_HEIGHT = Inches(1.2)

# Content Position (Standard Content Slides)
CONTENT_TOP_MARGIN = Inches(2.2)
CONTENT_LEFT_MARGIN = Inches(0.8)
CONTENT_WIDTH = Inches(6.5)  # Left 50% for text, right 50% for visuals
CONTENT_HEIGHT = Inches(4.8)

# Cover Slide Layout (Centered)
COVER_TITLE_TOP = Inches(2.5)
COVER_TITLE_LEFT = Inches(1.5)
COVER_TITLE_WIDTH = Inches(10.333)
COVER_TITLE_HEIGHT = Inches(1.5)

COVER_SUBTITLE_TOP = Inches(4.2)
COVER_SUBTITLE_LEFT = Inches(1.5)
COVER_SUBTITLE_WIDTH = Inches(10.333)
COVER_SUBTITLE_HEIGHT = Inches(1.0)

# Closing Slide Layout (Centered)
CLOSING_TITLE_TOP = Inches(2.8)
CLOSING_TITLE_LEFT = Inches(1.5)
CLOSING_TITLE_WIDTH = Inches(10.333)
CLOSING_TITLE_HEIGHT = Inches(1.2)

CLOSING_CONTENT_TOP = Inches(4.3)
CLOSING_CONTENT_LEFT = Inches(1.5)
CLOSING_CONTENT_WIDTH = Inches(10.333)
CLOSING_CONTENT_HEIGHT = Inches(1.5)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def apply_title_style(text_frame, is_cover=False, is_closing=False):
    """Apply consistent title styling to a text frame."""
    text_frame.word_wrap = True
    text_frame.vertical_anchor = MSO_ANCHOR.TOP
    
    for paragraph in text_frame.paragraphs:
        paragraph.alignment = PP_ALIGN.LEFT if not (is_cover or is_closing) else PP_ALIGN.CENTER
        paragraph.font.name = FONT_FAMILY
        paragraph.font.bold = TITLE_FONT_BOLD
        paragraph.font.color.rgb = TITLE_COLOR
        
        if is_cover:
            paragraph.font.size = COVER_TITLE_SIZE
        elif is_closing:
            paragraph.font.size = CLOSING_TITLE_SIZE
        else:
            paragraph.font.size = TITLE_FONT_SIZE


def apply_content_style(text_frame, is_cover=False, is_closing=False):
    """Apply consistent content styling to a text frame."""
    text_frame.word_wrap = True
    text_frame.vertical_anchor = MSO_ANCHOR.TOP
    
    for paragraph in text_frame.paragraphs:
        paragraph.alignment = PP_ALIGN.LEFT if not (is_cover or is_closing) else PP_ALIGN.CENTER
        paragraph.font.name = FONT_FAMILY
        paragraph.font.bold = False
        paragraph.line_spacing = CONTENT_LINE_SPACING
        
        if is_cover:
            paragraph.font.size = COVER_SUBTITLE_SIZE
            paragraph.font.color.rgb = COVER_SUBTITLE_COLOR
        elif is_closing:
            paragraph.font.size = CLOSING_CONTENT_SIZE
            paragraph.font.color.rgb = CONTENT_COLOR
        else:
            paragraph.font.size = CONTENT_FONT_SIZE
            paragraph.font.color.rgb = CONTENT_COLOR


def format_bullet_points(content_list):
    """Format content list as bullet points with consistent spacing."""
    if not content_list:
        return ""
    
    # Join with newlines, add bullet points
    return "\n".join(f"• {item}" for item in content_list)
