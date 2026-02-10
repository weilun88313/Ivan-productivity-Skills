# Ivan's Productivity Skills Collection

[![EN](https://img.shields.io/badge/English-blue?style=for-the-badge)](./README.md)
[![中文](https://img.shields.io/badge/简体中文-red?style=for-the-badge)](./README.zh-CN.md)

A collection of production-ready AI skills for content creation, event intelligence, and workflow automation.

## 📚 Available Skills

### 🎨 Content Creation

#### [blog-writer](./Skill/blog-writer/)
Generate high-quality, SEO-optimized blog posts with AI-generated illustrations following Linear design aesthetic.

**Features:**
- 5-paragraph prompt template for consistent image quality
- Linear dark mode aesthetic (#6B75FF, #1a1a1a)
- Automatic image generation with Gemini API
- 4 inline image categories (data cluster, flow, segmentation, temporal)
- Complete content structure (Hook → Why → How → CTA)

**Use case:** Create professional blog content with abstract visualizations

---

#### [pptx](./Skill/pptx/)
Generate presentation slides with AI-generated images following Linear design principles.

**Features:**
- Structured prompt templates for consistent visuals
- Shared Gemini API module
- Support for multiple slide layouts
- Design system documentation

**Use case:** Create presentation decks with professional visuals

---

### 📤 Content Publishing

#### [webflow-blog-publisher](./Skill/webflow-blog-publisher/)
Publish markdown blog posts directly to Webflow CMS with automatic image upload and field mapping.

**Features:**
- Automatic cover image and inline image upload to Webflow Assets
- Full-width image styling with `!important` overrides
- Dynamic field detection and mapping
- Support for meta descriptions, categories, and writer profiles
- Markdown to HTML conversion with proper alt text

**Use case:** Automated blog publishing workflow from markdown to live Webflow site

---

### 🔍 Research & Intelligence

#### [exhibitor-page-navigator](./Skill/exhibitor-page-navigator/)
Intelligently navigate exhibitor websites to extract product and company information.

**Features:**
- 4-phase workflow with confidence scoring
- Fallback strategies for protected content
- 6 JSON example scenarios
- High/medium/low confidence levels

**Use case:** Automated exhibitor research for trade shows and events

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8+
python --version

# Install dependencies
pip install -r requirements.txt

# Set up API keys
cp ~/.claude/lensmor_secrets.json.example ~/.claude/lensmor_secrets.json
# Edit and add your API keys
```

### Example: Generate a Blog Post

```bash
# 1. Generate blog content
cd Skill/blog-writer
python scripts/generate_blog.py --topic "Email Marketing Best Practices"

# 2. Generate images (using 5-paragraph template)
python scripts/generate_image.py \
  --prompt "$(cat references/visual-style-guide.md | grep -A 50 'Cover Image Example')" \
  --output_dir ../../workspace/images

# 3. Publish to Webflow
cd ../webflow-blog-publisher
python scripts/publish_to_webflow.py \
  --file ../../workspace/your-blog.md \
  --category strategy
```

---

## 📖 Documentation

Each skill includes comprehensive documentation:

- **README.md** - User guide with quick start, use cases, and troubleshooting
- **SKILL.md** - AI agent instructions (for Claude Code and similar tools)
- **examples/** - Sample inputs and outputs
- **references/** - Style guides and templates

### Key Documentation Files

- [Blog Workflow Guide](./Skill/blog-writer/WORKFLOW.md) - End-to-end blog creation and publishing
- [Visual Style Guide](./Skill/blog-writer/references/visual-style-guide.md) - Mandatory 5-paragraph prompt templates

---

## 🎨 Visual Style System

All generated images follow a **strict 5-paragraph prompt template**:

1. **Style** - Visual approach (e.g., "Abstract high-tech cover art")
2. **Color Palette** - Exact hex codes (#6B75FF, #1a1a1a)
3. **Concept** - Detailed abstract description
4. **Keywords Allowed** - Minimal text specification
5. **Environment** - Background and depth details
6. **Negative Constraints** - Explicit prohibitions (NO UI, NO dashboards)

**Why?** Ensures consistent Linear dark mode aesthetic and prevents UI elements.

---

## 🛠️ Tech Stack

- **Python 3.8+** - Core language
- **Gemini API** - AI image generation (gemini-3-pro-image-preview)
- **Webflow API v2** - CMS publishing
- **Markdown** - Content format
- **GitHub Actions** - CI/CD (optional)

---

## 📊 Project Structure

```
.
├── README.md                           # This file (English)
├── README.zh-CN.md                     # Chinese version
├── .gitignore                          # Ignore rules
├── Skill/
│   │
│   ├── blog-writer/
│   │   ├── README.md                   # User guide (503 lines)
│   │   ├── SKILL.md                    # AI instructions
│   │   ├── WORKFLOW.md                 # End-to-end blog workflow
│   │   ├── references/
│   │   │   └── visual-style-guide.md   # 5-paragraph templates (303 lines)
│   │   ├── scripts/
│   │   │   ├── gemini_api.py           # Shared API module
│   │   │   └── generate_image.py       # Image generation
│   │   └── examples/
│   │       └── sample-blog-post.md     # Full example (2,400 words)
│   │
│   ├── webflow-blog-publisher/
│   │   ├── README.md                   # User guide (573 lines)
│   │   ├── scripts/
│   │   │   └── publish_to_webflow.py   # Publishing script (449 lines)
│   │   └── assets/
│   │       └── writers/
│   │           └── writers.json        # Writer profiles
│   │
│   ├── exhibitor-page-navigator/
│   │   ├── README.md                   # User guide (329 lines)
│   │   ├── SKILL.md                    # Enhanced from 38 lines (293 lines)
│   │   └── examples/                   # 6 JSON scenarios
│   │
│   └── pptx/
│       ├── README.md                   # User guide (464 lines)
│       ├── SKILL.md
│       └── scripts/
│           ├── gemini_api.py           # Shared module
│           ├── ppt_img_gen.py
│           └── images2pptx.py
│
└── workspace/                          # Generated content (gitignored)
    ├── images/
    └── *.md
```

---

## 🔐 Configuration

All API keys should be stored in `~/.claude/lensmor_secrets.json`:

```json
{
  "NANO_API_KEY": "your_gemini_api_key",
  "WEBFLOW_API_TOKEN": "your_webflow_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "your_collection_id",
  "WEBFLOW_SITE_ID": "your_site_id"
}
```

Alternatively, set environment variables:

```bash
export GEMINI_API_KEY="your_key"
export WEBFLOW_API_TOKEN="your_token"
export WEBFLOW_BLOG_COLLECTION_ID="your_collection_id"
export WEBFLOW_SITE_ID="your_site_id"
```

---

## 📈 Recent Updates

### v2.1.0 (2026-02-09)

**Image Generation Quality Control**
- ✅ Mandated complete 5-paragraph prompt template for all images
- ✅ Updated visual-style-guide.md (61 → 303 lines)
- ✅ Added 4 inline image category templates
- ✅ Enhanced all skill README files

**Webflow Publisher Improvements**
- ✅ Fixed cover image upload (proper markdown format detection)
- ✅ Added full-width image styling with `!important` overrides
- ✅ Improved alt text for accessibility

**Code Quality**
- ✅ Created shared `gemini_api.py` module (DRY principle)
- ✅ Removed hardcoded API keys
- ✅ Added comprehensive .gitignore

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Follow existing code style and documentation standards
4. Test your changes thoroughly
5. Commit with descriptive messages
6. Push to your branch
7. Open a Pull Request

---

## 📄 License

This project is private. All rights reserved.

---

## 🔗 Related Resources

- [Claude Code Documentation](https://docs.anthropic.com)
- [Webflow API v2 Docs](https://developers.webflow.com)
- [Gemini API Documentation](https://ai.google.dev)
- [Linear Design System](https://linear.app)

---

## 📞 Support

For issues or questions:
1. Check individual skill README files
2. Review examples/ directories
3. Consult visual-style-guide.md for image generation
4. Open a GitHub issue

---

**Built with ❤️ for efficient content creation and workflow automation**
