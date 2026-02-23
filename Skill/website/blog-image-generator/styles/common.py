"""
Common style definitions and color constants.

Shared across all platform styles.
"""

# Core Linear Design System Colors
COLOR_ACCENT = "#6B75FF"  # Violet-blue indigo
COLOR_BG_DARK = "#1a1a1a"  # Deep charcoal
COLOR_BG_BLACK = "#0a0a0a"  # Nearly black
COLOR_TEXT_WHITE = "#FFFFFF"  # Pure white for titles
COLOR_TEXT_DIM = "#E6E6E6"  # 90% white for content

# Aspect Ratio Constants
ASPECT_RATIOS = {
    "16:9": "16:9",  # Widescreen (default for blog, LinkedIn, Twitter)
    "1:1": "1:1",    # Square (default for Jike)
    "4:3": "4:3",    # Standard
    "9:16": "9:16",  # Portrait/mobile
    "3:2": "3:2",    # Photo standard
    "21:9": "21:9",  # Ultrawide
}

# Resolution Standards
RESOLUTION_2K = "2560x1440"
RESOLUTION_4K = "3840x2160"
RESOLUTION_HD = "1920x1080"

# Common negative constraints
NEGATIVE_CONSTRAINTS = [
    "NO UI chrome",
    "NO navigation bars",
    "NO sidebars",
    "NO buttons",
    "NO browser frames",
    "NO dashboard widgets"
]


def get_aspect_ratio(platform, default="16:9"):
    """
    Get default aspect ratio for a platform.

    Args:
        platform: Platform name
        default: Default aspect ratio if platform not found

    Returns:
        Aspect ratio string
    """
    platform_ratios = {
        "blog": "16:9",
        "linkedin": "16:9",
        "twitter": "16:9",  # Also supports 1:1, 4:3
        "jike": "1:1",
        "pptx": "16:9",
    }
    return platform_ratios.get(platform.lower(), default)


def get_resolution(platform, quality="2K"):
    """
    Get resolution for a platform and quality level.

    Args:
        platform: Platform name
        quality: Quality level (2K, 4K, HD)

    Returns:
        Resolution string
    """
    resolutions = {
        "2K": RESOLUTION_2K,
        "4K": RESOLUTION_4K,
        "HD": RESOLUTION_HD,
    }
    return resolutions.get(quality.upper(), RESOLUTION_2K)
