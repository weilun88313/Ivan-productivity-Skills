[English](README.md) | [中文](README.zh.md)

---


# 博客写作工具

> 创建高排名、SEO 友好的专业风格博客文章

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 概述

**博客写作工具** 技能帮助你创建专业、可操作和 SEO 优化的博客文章。它结合了专家内容结构和 AI 生成的视觉资源，生成可直接发布的文章。

### 核心功能

- ✍️ **专业风格内容** - 专业、可操作、富有同理心的语气
- 📊 **SEO 优化** - 为搜索引擎可见性而结构化
- 🎨 **AI 生成插图** - 高质量 16:9 图片，Linear 深色模式风格
- 📝 **结构化格式** - 钩子 → 为什么 → 如何 → CTA 框架
- 💡 **专业提示** - 贯穿全文的内部建议标注
- 🎯 **准备发布** - 兼容 Webflow 博客发布器

## 快速开始

### 前置要求

```bash
# 安装依赖
pip install requests

# 设置 Gemini API key
export GEMINI_API_KEY='your_api_key_here'

# 或添加到 ~/.claude/lensmor_secrets.json
{
  "NANO_API_KEY": "your_api_key_here"
}
```

### 基本使用

**步骤 0：品牌合规性检查（如果与产品相关）**

如果你的博客文章将提及 Lensmor 或产品功能，首先阅读品牌指南：

```bash
# 阅读最新产品信息：
- /Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/SKILL.md
- /Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/resources/product-details.md

# 验证：
- 产品功能是最新的
- 价值主张准确
- 术语正确
- 竞争定位是最新的
```

**步骤 1：请求博客文章**

```
"写一篇关于电子邮件营销最佳实践的博客文章"
```

**步骤 2：生成图片**

```bash
# 封面图片
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "抽象电子邮件营销数据可视化，流动连接，Linear 深色模式美学" \
  --output_dir workspace/blog/images \
  --filename cover

# 内联图片（重复 3-5 次）
python Skill/blog-writer/scripts/generate_image.py \
  --prompt "收件箱界面线框，清洁 UI 模型，深色模式" \
  --output_dir workspace/blog/images \
  --filename inline_1
```

**步骤 3：审查和发布**

输出包括一个格式正确的 markdown 文件，可用 [webflow-blog-publisher](../webflow-blog-publisher) 发布。

## 内容结构

### 公式

```
┌─────────────────────────────────────┐
│ 1. 钩子（引言）                      │
│    - 问题                           │
│    - 激化（可选）                    │
│    - 承诺                           │
│    - "什么是"（定义）                │
├─────────────────────────────────────┤
│ 2. "为什么"（重要性）                │
│    - 以要点形式列出好处              │
│    - 数据和统计                      │
├─────────────────────────────────────┤
│ 3. "如何做"（核心内容）              │
│    - 分步指南 或                     │
│    - 列表格式                        │
│    - 贯穿全文的专业提示              │
├─────────────────────────────────────┤
│ 4. 结论 & CTA                       │
│    - 关键要点                        │
│    - 鼓舞人心的结语                  │
│    - 明确的行动号召                  │
└─────────────────────────────────────┘
```

### 输出格式

每篇博客文章包含此元数据块：

```markdown
# [引人入胜的带关键词标题]

**Slug**: /blog/[category]/[keyword-slug]
**Meta Description**: [150-160 字符 SEO 摘要]
**Cover Image**:
![描述](images/cover.png)

---

[文章内容从这里开始]
```

## 语气和声音

### 专业但易于理解
- 像一位知识渊博的同事一样写作
- 使用"你"和"我们"代词
- 避免不加解释的行话

### 富有同理心
- 承认读者的痛点
- *"我们知道 X 可能令人望而生畏..."*
- 在解决方案之前表现理解

### 以行动为导向
- 每个部分都提供价值
- 没有废话或填充内容
- 具体、可操作的步骤

### 自信
- 权威但谦逊
- 在可能的情况下有数据支持
- 乐于助人，不说教

## 格式标准

### 段落
- **最多 3-4 行**每段
- 可读性短句
- 每段一个想法

### 标题
- **H2** 用于主要部分
- **H3** 用于子部分
- 清晰、描述性的标题
- 适当时使用动作动词

### 列表
- 3+ 相关项目使用要点
- 顺序步骤使用编号列表
- **加粗关键概念**以便扫描

### 专业提示
每篇文章至少 3 个：

```markdown
**专业提示**：使用个性化标记可将打开率提高高达 26%。
```

## 图片生成

### ⚠️ 关键：使用完整的 5 段提示模板

**所有图片生成必须使用 visual-style-guide.md 中的完整结构化模板。**

不要使用简化的提示。5 段模板确保：
- ✅ 一致的 Linear 深色模式美学
- ✅ 准确的 #6B75FF 颜色使用
- ✅ 消除 UI 元素和仪表板
- ✅ 适当的抽象与字面平衡
- ✅ 高质量、可发布的结果

**模板结构**（所有图片必需）：
1. **风格**：定义视觉方法
2. **调色板**：指定确切颜色（#6B75FF、#1a1a1a）
3. **概念**：详细的抽象描述
4. **允许的关键词**：最少文本规范
5. **环境**：背景和深度细节
6. **否定约束**：明确禁止

### 视觉风格指南

所有图片遵循 **Linear 深色模式美学**：

- **风格**：极简、技术、现代、抽象
- **颜色**：深炭灰背景（#1a1a1a），紫蓝色强调（#6B75FF）
- **元素**：抽象形状、数据可视化、几何形式（无 UI 模型）
- **质量**：16:9 宽高比，高分辨率（2K+）
- **文本**：仅最少关键词（无段落或详细文本）

**参见**：[references/visual-style-guide.md](references/visual-style-guide.md) 了解完整的 5 段模板和示例

## 内容类型

### 操作指南

**结构**:
```markdown
## 步骤 1：[动作动词标题]

步骤的简要解释。

**专业提示**：此步骤的内部建议。

![相关图表](images/step1.png)
```

### 列表文章

**结构**:
```markdown
## 1. [项目名称/概念]

项目的描述及其重要性。

**为什么有效**：有效性解释。

![插图](images/item1.png)
```

## SEO 最佳实践

### 标题优化
- **长度**：50-60 字符
- **格式**：[数字] + [形容词] + [关键词] + [承诺]
- **示例**："10 个经过验证的电子邮件营销策略，让你的 ROI 提高 3 倍"

### 元描述
- **长度**：150-160 字符
- **包含**：主要关键词、好处、行动号召
- **示例**："学习顶级品牌用来将 ROI 提高三倍的 10 个经过验证的电子邮件营销策略。内附可操作的技巧。"

### Slug 结构
- **格式**：`/blog/[category]/[keyword-slug]`
- **类别**：strategy、playbooks 或 teardowns
- **Slug**：小写、连字符、富含关键词
- **示例**：`/blog/strategy/email-marketing-best-practices`

## 工作流集成

此技能与 [webflow-blog-publisher](../webflow-blog-publisher) 无缝协作：

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

参见 [BLOG_WORKFLOW.md](../BLOG_WORKFLOW.md) 了解完整的端到端指南。

## 故障排除

### 图片生成失败

**错误**: `GEMINI_API_KEY not found`

**解决方案**:
```bash
# 选项 1：环境变量
export GEMINI_API_KEY='your_key'

# 选项 2：密钥文件
echo '{"NANO_API_KEY": "your_key"}' > ~/.claude/lensmor_secrets.json
```

**错误**: `Request timed out`

**解决方案**:
- 简化你的提示（更少细节）
- 检查互联网连接
- 几分钟后再试（API 可能很忙）

## 最佳实践

### 内容策略
1. **品牌合规优先**：如果写关于 Lensmor/产品的内容，先阅读 brand-guidelines/SKILL.md 了解最新产品信息
2. **先研究**：深入了解你的主题
3. **了解你的受众**：为特定读者画像写作
4. **数据驱动**：包含统计和研究
5. **可操作**：每个部分都应提供价值
6. **SEO 意识**：但首先为人类写作

## 架构

```
blog-writer/
├── README.md                  # 本文件
├── SKILL.md                   # AI 工作流指令
├── scripts/
│   ├── gemini_api.py         # 共享 API 客户端
│   └── generate_image.py     # 图片生成工具
└── references/
    └── visual-style-guide.md # 详细视觉指南
```

## 版本历史

### v2.1.0 (2026-02-10)
- ✅ 添加了品牌规范引用机制
- ✅ 为产品相关内容添加了品牌合规性检查
- ✅ 更新了工作流以包含品牌验证步骤

### v2.0.0 (2026-02-08)
- ✅ 重构图片生成以使用共享 API 模块
- ✅ 改进错误处理和用户反馈
- ✅ 添加了全面的 README 文档

## 资源

- [SKILL.md](SKILL.md) - 详细的 AI 指令和内容指南
- [视觉风格指南](references/visual-style-guide.md) - 图片生成指南
- [Webflow 博客发布器](../webflow-blog-publisher) - 发布集成
- [博客工作流指南](../BLOG_WORKFLOW.md) - 端到端流程
- [品牌规范](../brand-guidelines) - Lensmor 品牌信息

## 支持

如有问题或疑问：
1. 查看此 README
2. 查看 SKILL.md 了解 AI 特定指导
3. 查阅博客工作流指南了解集成
4. 独立测试图片生成

---

**愉快写作！** 📝✨
