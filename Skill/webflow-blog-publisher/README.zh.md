[English](README.md) | [中文](README.zh.md)

---


# Webflow 博客发布器

> 自动发布博客文章到 Webflow CMS

## 概述

**Webflow 博客发布器** 技能帮助你将 Markdown 格式的博客文章自动发布到 Webflow CMS。它处理图片上传、内容转换和 CMS 项创建。

### 核心功能

- 📝 **Markdown 转 HTML** - 自动转换 Markdown 为 Webflow 富文本
- 🖼️ **图片上传** - 上传并链接文章图片到 Webflow 资源
- 📊 **CMS 集成** - 直接创建博客文章条目
- 🎯 **元数据支持** - 处理标题、slug、描述等
- 🚀 **草稿/发布** - 控制文章发布状态

## 快速开始

### 前置要求

```bash
# 安装依赖
pip install requests markdown

# 配置密钥在 ~/.claude/lensmor_secrets.json:
{
  "WEBFLOW_API_TOKEN": "your_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "collection_id",
  "WEBFLOW_SITE_ID": "site_id"
}
```

### 基本使用

```bash
python scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

## 文章格式

### Markdown 元数据块

```markdown
# 文章标题

**Slug**: /blog/strategy/article-slug
**Meta Description**: 150-160 字符的 SEO 描述
**Cover Image**:
![封面图描述](images/cover.png)

---

[文章内容开始...]
```

## 命令选项

- `--file` (必需): Markdown 文件路径
- `--category`: 博客类别（strategy、playbooks、teardowns）
- `--publish`: 直接发布（不带此参数则创建草稿）
- `--writer`: 作者姓名
- `--api-key`: 覆盖配置文件中的 API 密钥

## 工作流集成

### 与 blog-writer 技能配合

```bash
# 1. 写博客文章（使用 AI）
# 输出: workspace/blog/article.md

# 2. 生成图片
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "..." \
  --output_dir workspace/blog/images

# 3. 发布到 Webflow
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

## 类别

可用类别（在 Webflow 中自定义）：
- `strategy` - 战略指南和框架
- `playbooks` - 分步战术指南
- `teardowns` - 案例研究和分析

## 故障排除

### 图片上传失败

**问题**: 图片未上传

**解决方案**:
- 验证 WEBFLOW_SITE_ID 已设置
- 检查 API 令牌权限
- 确保图片文件存在
- 尝试先手动上传一张图片

### 发布为草稿而非正式发布

**默认**: 脚本创建草稿

**正式发布**: 添加 `--publish` 标志
```bash
python publish_to_webflow.py --file article.md --publish
```

## 最佳实践

### 内容策略

1. **长度**: 1500-3000 字以利于 SEO
2. **结构**: 清晰的 H2/H3 层次结构
3. **语气**: 专业但易于理解
4. **CTA**: 包含 1-2 个明确的行动号召

### 图片

1. **数量**: 1 张封面图 + 3-5 张内联图片
2. **格式**: PNG，16:9 宽高比
3. **替代文本**: 为了无障碍访问的描述性文本

### SEO

1. **Slug**: 关键词丰富、可读的 URL
2. **元描述**: 150-160 字符，引人注目
3. **标题**: 描述性、搜索友好的标题

## 架构

```
webflow-blog-publisher/
├── README.md              # 本文件
├── SKILL.md              # AI 工作流指令
└── scripts/
    └── publish_to_webflow.py  # 发布脚本
```

## 资源

- [SKILL.md](SKILL.md) - AI 具体指导
- [博客工作流指南](../BLOG_WORKFLOW.md) - 端到端流程
- [Webflow API 文档](https://developers.webflow.com/) - API 参考

## 支持

如有问题或疑问：
1. 检查此 README
2. 查看博客工作流指南了解集成
3. 测试独立的图片上传

---

**愉快发布！** 🚀✨
