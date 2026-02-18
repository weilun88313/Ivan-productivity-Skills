"""
Linear Dark Mode style configuration.

Used for blog images - the core aesthetic that other styles derive from.
"""

from .common import COLOR_ACCENT, COLOR_BG_DARK, COLOR_BG_BLACK

STYLE_LINEAR_BLOG = {
    "name": "Linear Dark Mode Blog",
    "description": "Abstract high-tech visualization inspired by Linear app design",

    # Colors
    "background": COLOR_BG_BLACK,
    "background_secondary": COLOR_BG_DARK,
    "accent": COLOR_ACCENT,
    "accent_name": "neon violet-blue indigo",

    # Style characteristics
    "mode": "dark",
    "quality": "minimalist",
    "finish": "matte",
    "lighting": "soft ambient light with subtle ray-traced reflections",

    # Visual elements
    "elements": [
        "abstract geometric shapes",
        "data streams",
        "interconnected nodes",
        "floating frosted glass shapes",
        "abstract light trails"
    ],

    # Environment
    "environment": {
        "type": "deep black void",
        "grid": "very subtle, barely visible isometric grid (5% opacity)",
        "depth": "shallow depth of field with soft bokeh effects"
    },

    # Technical specs
    "aspect_ratio": "16:9",
    "resolution": "2K",
    "min_resolution": "1920x1080",
    "preferred_resolution": "2560x1440",

    # Constraints
    "negative_constraints": [
        "NO TEXT",
        "NO LETTERS",
        "NO WORDS",
        "NO UI ELEMENTS",
        "NO DASHBOARDS",
        "NO CHARTS",
        "Purely abstract visual shapes and light compositions"
    ],

    # Use cases
    "use_cases": ["blog_cover", "blog_inline"]
}

# Cover image specific settings
STYLE_LINEAR_COVER = {
    **STYLE_LINEAR_BLOG,
    "negative_constraints": STYLE_LINEAR_BLOG["negative_constraints"] + [
        "NO keywords",
        "NO labels at all"
    ],
    "abstract_level": "pure"
}

# Inline image specific settings
STYLE_LINEAR_INLINE = {
    **STYLE_LINEAR_BLOG,
    "negative_constraints": [
        "NO product UI chrome",
        "NO navigation bars",
        "NO sidebars",
        "NO browser frames",
        "NO dashboard widgets",
        "NO fake app interfaces"
    ],
    "keywords_allowed": True,
    "keyword_limit": "Simple labels only, 2-5 words max",
    "abstract_level": "conceptual"
}
