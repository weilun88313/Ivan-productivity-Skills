"""
Blog image generation client.

Thin wrapper that imports from the unified blog-image-generator skill.
The actual implementation lives in: Skill/blog-image-generator/scripts/image_generator.py
"""

import sys
import os

# Resolve path to the shared blog-image-generator skill relative to this file.
# Layout: Skill/blog-writer/scripts/image_generator.py
#       → Skill/blog-image-generator/scripts/image_generator.py
_this_dir = os.path.dirname(os.path.abspath(__file__))
_skill_root = os.path.dirname(os.path.dirname(_this_dir))  # → Skill/
_shared_scripts = os.path.join(_skill_root, "blog-image-generator", "scripts")

if _shared_scripts not in sys.path:
    sys.path.insert(0, _shared_scripts)

from image_generator import ImageGenerator  # noqa: E402

# Backward compatibility aliases
GeminiImageGenerator = ImageGenerator
