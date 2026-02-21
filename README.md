[![EN](https://img.shields.io/badge/English-blue?style=for-the-badge)](./README.md)
[![中文](https://img.shields.io/badge/简体中文-red?style=for-the-badge)](./README.zh-CN.md)

# Ivan's Productivity Skills Collection

Production-ready AI skills for content creation, social media, sales automation, and workflow automation.

## 📚 Available Skills (15 total)

### 🌐 Official Website Blog

**[keyword-research](./Skill/keyword-research/)** - Discover high-value keywords with Ahrefs API integration for SEO strategies

**[blog-writer](./Skill/blog-writer/)** - Generate SEO-optimized blog posts with AI-generated Linear-style illustrations

**[blog-image-generator](./Skill/blog-image-generator/)** - Unified AI image generation for all platforms (blog, LinkedIn, Twitter, Jike, PPTX)

**[webflow-blog-publisher](./Skill/webflow-blog-publisher/)** - Publish markdown posts to Webflow CMS with automatic image upload

**[content-pipeline](./Skill/content-pipeline/)** - End-to-end automation: research → write → images → publish

### 📱 Social Media

**[linkedin-post-writer](./Skill/linkedin-post-writer/)** - Create professional LinkedIn posts with brand-consistent formatting

**[twitter-post-writer](./Skill/twitter-post-writer/)** - Generate engaging Twitter/X posts with viral optimization

**[jike-post-writer](./Skill/jike-post-writer/)** - Create content for Jike (即刻) social platform

### 💼 Sales Automation

**[50k-lead-generation-system](./Skill/50k-lead-generation-system/)** - Automated B2B lead generation and outreach system

### 🛠️ Development Tools

**[pptx](./Skill/pptx/)** - Create presentation slides with AI-generated visuals following Linear design

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
cp .env.example .env
# Edit .env and add your keys
```

### Example: Official Website Blog Workflow

```bash
# 1. Research keywords
cd Skill/keyword-research
# "Research keywords for AI content marketing"

# 2. Write blog post
cd ../blog-writer
# "Write a blog post about AI content marketing best practices"

# 3. Generate images (using unified blog-image-generator)
cd ../blog-image-generator
python scripts/generate.py --platform blog --type cover --prompt "AI Content Marketing" --output ../../workspace/blog/images/cover.png

# 4. Publish to Webflow
cd ../webflow-blog-publisher
python scripts/publish_to_webflow.py --file ../../workspace/blog/article.md --publish
```

**Or use the full pipeline:**
```bash
cd Skill/content-pipeline
# "Run the content pipeline for AI content marketing"
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
- [Content Pipeline Guide](./Skill/content-pipeline/README.md)

---

## 🔐 Configuration

Copy `.env.example` to `.env` and fill in your keys:

```bash
cp .env.example .env
```

```dotenv
# .env
GEMINI_API_KEY=your_gemini_api_key
FAL_KEY=your_fal_api_key
WEBFLOW_API_TOKEN=your_webflow_token
WEBFLOW_BLOG_COLLECTION_ID=your_collection_id
WEBFLOW_SITE_ID=your_site_id
```

Or export as environment variables:
```bash
export GEMINI_API_KEY="your_key"
export FAL_KEY="your_key"
```

---

## 🛠️ Tech Stack

- **Python 3.8+** - Core language
- **Gemini API / Fal.ai** - AI image generation (with automatic fallback)
- **Ahrefs API v3** - SEO keyword research
- **Webflow API v2** - CMS publishing
- **Apollo.io** - Lead data source
- **n8n** - Workflow automation
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

**Built with ❤️ for efficient content creation, social media, and sales automation**
