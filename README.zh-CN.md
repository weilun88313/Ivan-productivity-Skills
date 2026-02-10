[English](README.md) | [中文](README.zh-CN.md)

---

# Ivan的生产力技能合集

[![EN](https://img.shields.io/badge/English-blue?style=for-the-badge)](./README.md)
[![中文](https://img.shields.io/badge/简体中文-red?style=for-the-badge)](./README.zh-CN.md)

用于内容创作、活动情报和工作流自动化的生产就绪AI技能。

## 📚 可用技能

### 🎨 内容创作

**[blog-writer](./Skill/blog-writer/)** - 生成SEO优化博客文章，并配有AI生成的Linear风格插图

**[pptx](./Skill/pptx/)** - 创建遵循Linear设计风格的AI生成视觉内容的演示文稿幻灯片

**[linkedin-post-writer](./Skill/linkedin-post-writer/)** - 创建具有品牌一致格式的专业LinkedIn帖子

### 📤 发布

**[webflow-blog-publisher](./Skill/webflow-blog-publisher/)** - 将Markdown文章发布到Webflow CMS，并自动上传图片

### 🔍 研究与情报

**[exhibitor-page-navigator](./Skill/exhibitor-page-navigator/)** - 从参展商网站提取产品和公司信息

### 🛠️ 开发工具

**[skill-creator](./Skill/skill-creator/)** - 使用双语文档模板搭建新技能

**[brand-guidelines](./Skill/brand-guidelines/)** - 集中化的品牌信息和产品详情参考

---

## 🚀 快速开始

### 先决条件

```bash
# Python 3.8+
pip install -r requirements.txt

# 配置API密钥
cp ~/.claude/lensmor_secrets.json.example ~/.claude/lensmor_secrets.json
# 编辑并添加您的密钥：GEMINI_API_KEY, WEBFLOW_API_TOKEN, etc.
```

### 示例：博客文章工作流

```bash
# 生成带图片的博客
cd Skill/blog-writer
python scripts/generate_blog.py --topic "Your Topic"

# 发布到Webflow
cd ../webflow-blog-publisher
python scripts/publish_to_webflow.py --file ../../workspace/your-blog.md --publish
```

---

## 📖 文档

每个技能都包含：
- **README.md** / **README.zh.md** - 用户指南（双语）
- **SKILL.md** - AI代理指令
- **examples/** - 示例用法
- **scripts/** - 可执行工具

**关键资源：**
- [技能开发指南](./SKILL_DEVELOPMENT_GUIDELINES.md)
- [博客工作流指南](./Skill/blog-writer/WORKFLOW.md)

---

## 🔐 配置

将API密钥存储在 `~/.claude/lensmor_secrets.json` 中：

```json
{
  "NANO_API_KEY": "your_gemini_api_key",
  "WEBFLOW_API_TOKEN": "your_webflow_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "your_collection_id",
  "WEBFLOW_SITE_ID": "your_site_id"
}
```

或使用环境变量：

```bash
export GEMINI_API_KEY="your_key"
export WEBFLOW_API_TOKEN="your_token"
```

---

## 🛠️ 技术栈

- **Python 3.8+** - 核心语言
- **Gemini API** - AI图像生成
- **Webflow API v2** - CMS发布
- **Markdown** - 内容格式

---

## 🤝 贡献

1.  Fork此仓库
2.  创建功能分支
3.  遵循现有代码风格和双语文档标准
4.  彻底测试
5.  提交Pull Request

---

## 📄 许可证

本项目为私有项目。保留所有权利。

---

**用 ❤️ 构建，旨在实现高效内容创作和工作流自动化**