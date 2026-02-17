[![EN](https://img.shields.io/badge/English-blue?style=for-the-badge)](./README.md)
[![中文](https://img.shields.io/badge/简体中文-red?style=for-the-badge)](./README.zh-CN.md)

# Ivan's Productivity Skills Collection

Production-ready AI skills for content creation, social media, and workflow automation.

## 📚 Available Skills (14 total)

### 🎨 Content Creation

**[blog-writer](./Skill/blog-writer/)** - Generate SEO-optimized blog posts with AI-generated Linear-style illustrations

**[pptx](./Skill/pptx/)** - Create presentation slides with AI-generated visuals following Linear design

**[linkedin-post-writer](./Skill/linkedin-post-writer/)** - Create professional LinkedIn posts with brand-consistent formatting

**[twitter-post-writer](./Skill/twitter-post-writer/)** - Generate engaging Twitter/X posts with viral optimization

**[jike-post-writer](./Skill/jike-post-writer/)** - Create content for Jike (即刻) social platform

### 📤 Publishing & Automation

**[webflow-blog-publisher](./Skill/webflow-blog-publisher/)** - Publish markdown posts to Webflow CMS with automatic image upload

**[content-pipeline](./Skill/content-pipeline/)** - End-to-end workflow: research → write → images → publish

### 🔍 Research & Intelligence

**[keyword-research](./Skill/keyword-research/)** - Discover high-value keywords with Ahrefs API integration for SEO strategies

**[50k-lead-generation-system](./Skill/50k-lead-generation-system/)** - Automated lead generation and outreach system

### 🛠️ Development Tools

**[skill-creator](./Skill/skill-creator/)** - Scaffold new skills with bilingual documentation templates

**[skill-manager](./Skill/skill-manager/)** - Manage and organize skills repository

**[skill-evolution-manager](./Skill/skill-evolution-manager/)** - Track and evolve skill capabilities over time

**[github-to-skills](./Skill/github-to-skills/)** - Convert GitHub repos to Claude Code skills

**[brand-guidelines](./Skill/brand-guidelines/)** - Centralized brand information and product details reference

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8+
pip install -r requirements.txt

# Configure API keys
cp ~/.claude/lensmor_secrets.json.example ~/.claude/lensmor_secrets.json
# Edit and add your keys
```

### Example: Content Creation Workflow

```bash
# 1. Research keywords
cd Skill/keyword-research
# "Research keywords for AI content marketing"

# 2. Write blog post
cd ../blog-writer
# "Write a blog post about AI content marketing best practices"

# 3. Generate images
python scripts/generate_image.py --prompt "..." --output_dir workspace/blog/images

# 4. Publish to Webflow
cd ../webflow-blog-publisher
python scripts/publish_to_webflow.py --file ../../workspace/blog/article.md --publish
```

---

## 📖 Documentation

Each skill includes:
- **README.md** / **README.zh.md** - User guide (bilingual)
- **SKILL.md** - AI agent instructions
- **examples/** - Sample usage (optional)
- **scripts/** - Executable tools

**Key Resources:**
- [Skill Development Guidelines](./SKILL_DEVELOPMENT_GUIDELINES.md)
- [Content Workflow Guide](./Skill/content-pipeline/README.md)

---

## 🔐 Configuration

Store API keys in `~/.claude/lensmor_secrets.json`:

```json
{
  "NANO_API_KEY": "your_gemini_api_key",
  "FAL_KEY": "your_fal_api_key",
  "Ahrefs_API_TOKEN": "your_ahrefs_token",
  "WEBFLOW_API_TOKEN": "your_webflow_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "your_collection_id",
  "WEBFLOW_SITE_ID": "your_site_id"
}
```

Or use environment variables:
```bash
export GEMINI_API_KEY="your_key"
export FAL_KEY="your_key"
export Ahrefs_API_TOKEN="your_token"
```

---

## 🛠️ Tech Stack

- **Python 3.8+** - Core language
- **Gemini API / Fal.ai** - AI image generation (with automatic fallback)
- **Ahrefs API v3** - SEO keyword research
- **Webflow API v2** - CMS publishing
- **Markdown** - Content format

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Follow [Skill Development Guidelines](./SKILL_DEVELOPMENT_GUIDELINES.md)
4. Test thoroughly
5. Submit Pull Request

---

## 📄 License

This project is private. All rights reserved.

---

**Built with ❤️ for efficient content creation and workflow automation**
