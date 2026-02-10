# Ivan's Productivity Skills Collection

[![EN](https://img.shields.io/badge/English-blue?style=for-the-badge)](./README.md)
[![中文](https://img.shields.io/badge/简体中文-red?style=for-the-badge)](./README.zh-CN.md)

Production-ready AI skills for content creation, event intelligence, and workflow automation.

## 📚 Available Skills

### 🎨 Content Creation

**[blog-writer](./Skill/blog-writer/)** - Generate SEO-optimized blog posts with AI-generated Linear-style illustrations

**[pptx](./Skill/pptx/)** - Create presentation slides with AI-generated visuals following Linear design

**[linkedin-post-writer](./Skill/linkedin-post-writer/)** - Create professional LinkedIn posts with brand-consistent formatting

### 📤 Publishing

**[webflow-blog-publisher](./Skill/webflow-blog-publisher/)** - Publish markdown posts to Webflow CMS with automatic image upload

### 🔍 Research & Intelligence

**[exhibitor-page-navigator](./Skill/exhibitor-page-navigator/)** - Extract product and company information from exhibitor websites

### 🛠️ Development Tools

**[skill-creator](./Skill/skill-creator/)** - Scaffold new skills with bilingual documentation templates

**[brand-guidelines](./Skill/brand-guidelines/)** - Centralized brand information and product details reference

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8+
pip install -r requirements.txt

# Configure API keys
cp ~/.claude/lensmor_secrets.json.example ~/.claude/lensmor_secrets.json
# Edit and add your keys: GEMINI_API_KEY, WEBFLOW_API_TOKEN, etc.
```

### Example: Blog Post Workflow

```bash
# Generate blog with images
cd Skill/blog-writer
python scripts/generate_blog.py --topic "Your Topic"

# Publish to Webflow
cd ../webflow-blog-publisher
python scripts/publish_to_webflow.py --file ../../workspace/your-blog.md --publish
```

---

## 📖 Documentation

Each skill includes:
- **README.md** / **README.zh.md** - User guide (bilingual)
- **SKILL.md** - AI agent instructions
- **examples/** - Sample usage
- **scripts/** - Executable tools

**Key Resources:**
- [Skill Development Guidelines](./SKILL_DEVELOPMENT_GUIDELINES.md)
- [Blog Workflow Guide](./Skill/blog-writer/WORKFLOW.md)

---

## 🔐 Configuration

Store API keys in `~/.claude/lensmor_secrets.json`:

```json
{
  "NANO_API_KEY": "your_gemini_api_key",
  "WEBFLOW_API_TOKEN": "your_webflow_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "your_collection_id",
  "WEBFLOW_SITE_ID": "your_site_id"
}
```

Or use environment variables:

```bash
export GEMINI_API_KEY="your_key"
export WEBFLOW_API_TOKEN="your_token"
```

---

## 🛠️ Tech Stack

- **Python 3.8+** - Core language
- **Gemini API** - AI image generation
- **Webflow API v2** - CMS publishing
- **Markdown** - Content format

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Follow existing code style and bilingual documentation standards
4. Test thoroughly
5. Submit Pull Request

---

## 📄 License

This project is private. All rights reserved.

---

**Built with ❤️ for efficient content creation and workflow automation**
