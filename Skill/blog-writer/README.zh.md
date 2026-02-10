[English](README.md) | [中文](README.zh.md)

---

# professional blog 博客文章撰写器

> 以 professional blog 风格撰写高排名、SEO 友好的博客文章

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 概述

**professional blog 博客文章撰写器** 技能可帮助您按照 professional blog 博客行之有效的内容公式，创建专业、可操作且经过 SEO 优化的博客文章。它将专业的内容结构与 AI 生成的视觉资产相结合，以生成可供发布的文章。

### 主要功能

- ✍️ **professional blog 风格内容** - 专业、可操作、富有同情心的语调
- 📊 **SEO 优化** - 为搜索引擎可见性而结构化
- 🎨 **AI 生成插图** - 高质量 16:9 图像，采用 Linear 暗色模式风格
- 📝 **结构化格式** - 钩子 → 为什么 → 如何 → CTA 框架
- 💡 **专业提示** - 贯穿始终的内幕建议
- 🎯 **可供发布** - 兼容 Webflow Blog Publisher

## 快速入门

### 前提条件

```bash
# 安装依赖项
pip install requests

# 设置 Gemini API 密钥
export GEMINI_API_KEY='your_api_key_here'

# 或者添加到 ~/.claude/lensmor_secrets.json
{
  "NANO_API_KEY": "your_api_key_here"
}
```

### 基本用法

**步骤 0：品牌合规性检查（如果与产品相关）**

如果您的博客文章将提及 Lensmor 或产品功能，请首先阅读品牌指南：

```bash
# 阅读最新产品信息：
- /Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/SKILL.md
- /Users/ivan/Documents/Ivan_Skills/Skill/brand-guidelines/resources/product-details.md

# 验证：
- 产品功能是最新的
- 价值主张是准确的
- 术语是正确的
- 竞争定位是最新的
```

**步骤 1：请求一篇博客文章**

```
"Write a blog post about email marketing best practices"
```

**步骤 2：生成图像**

```bash
# 封面图片
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Abstract email marketing data visualization, flowing connections, Linear dark mode aesthetic" \
  --output_dir workspace/blog/images \
  --filename cover

# 内联图片（重复 3-5 次）
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Email inbox interface wireframe, clean UI mockup, dark mode" \
  --output_dir workspace/blog/images \
  --filename inline_1
```

**步骤 3：审阅和发布**

输出包括一个格式正确的 Markdown 文件，可使用 [webflow-blog-publisher](../webflow-blog-publisher) 进行发布。

## 内容结构

### professional blog 公式

```
┌─────────────────────────────────────┐
│ 1. 钩子 (引言)                      │
│    - 问题                           │
│    - 煽动 (可选)                    │
│    - 承诺                           │
│    - “是什么” (定义)                │
├─────────────────────────────────────┤
│ 2. “为什么” (重要性)                │
│    - 要点形式的益处                 │
│    - 数据和统计信息                 │
├─────────────────────────────────────┤
│ 3. “如何做” (核心内容)              │
│    - 分步指南 或                    │
│    - 列表形式                       │
│    - 贯穿始终的专业提示             │
├─────────────────────────────────────┤
│ 4. 结论和 CTA                       │
│    - 关键要点                       │
│    - 鼓励性结尾                     │
│    - 明确的行动号召                 │
└─────────────────────────────────────┘
```

### 输出格式

每篇博客文章都包含此元数据块：

```markdown
# [带有关键词的吸引人标题]

**Slug**: /blog/[category]/[keyword-slug]
**Meta Description**: [150-160 字符的 SEO 摘要]
**Cover Image**:
![Description](images/cover.png)

---

[文章内容从此处开始]
```

## 语调和风格

### 专业而易懂
- 像一位知识渊博的同事一样撰写
- 使用“您”和“我们”等人称代词
- 避免不加解释的行话

### 富有同情心
- 承认读者的痛点
- *“我们知道 X 可能令人望而生畏……”*
- 在提供解决方案之前表现出理解

### 行动导向
- 每个部分都提供价值
- 没有冗余或填充内容
- 具体、可操作的步骤

### 自信
- 权威但谦逊
- 尽可能有数据支持
- 乐于助人，而非说教

## 格式标准

### 段落
- 每个段落**最多 3-4 行**
- 短句以提高可读性
- 每个段落一个想法

### 标题
- 主部分使用 **H2**
- 子部分使用 **H3**
- 清晰、描述性的标题
- 适当时使用动作动词

### 列表
- 3 个以上相关项目使用项目符号列表
- 顺序步骤使用编号列表
- **加粗关键概念**以便快速浏览

### 专业提示
每篇文章最少 3 个：

```markdown
**Pro Tip**: Use personalization tokens to increase open rates by up to 26%.
```

### 表格
使用 Markdown 表格进行比较：

```markdown
| Feature | Basic | Premium |
|---------|-------|---------|
| Sends   | 1000  | 50000   |
| Price   | $9    | $49     |
```

## 图像生成

### ⚠️ 关键：使用完整的 5 段提示模板

**所有图像生成都必须使用 visual-style-guide.md 中完整的结构化模板。**

请勿使用简化提示。5 段模板确保：
- ✅ 一致的 Linear 暗色模式美学
- ✅ 准确的 #6B75FF 颜色使用
- ✅ 消除 UI 元素和仪表板
- ✅ 适当的抽象与字面平衡
- ✅ 高质量、可发布的成果

**模板结构**（所有图像必需）：
1. **Style**：定义视觉方法
2. **Color Palette**：指定确切颜色（#6B75FF, #1a1a1a）
3. **Concept**：详细的抽象描述
4. **Keywords Allowed**：最小文本规范
5. **Environment**：背景和深度细节
6. **Negative Constraints**：明确的禁止事项

### 视觉风格指南

所有图像都遵循 **Linear 暗色模式美学**：

- **风格**：极简、技术、现代、抽象
- **颜色**：深木炭色背景（#1a1a1a），紫蓝色强调色（#6B75FF）
- **元素**：抽象形状、数据可视化、几何形式（无 UI 模型）
- **质量**：16:9 宽高比，高分辨率（2K+）
- **文本**：仅限少量关键词（无段落或详细文本）

**参见**：[references/visual-style-guide.md](references/visual-style-guide.md) 获取完整的 5 段模板和示例

### 图像要求

#### 封面图片（必需）
- **目的**：文章的标题图片
- **风格**：纯抽象 — 无文本、无 UI、无字面描绘
- **提示模板**：使用 visual-style-guide.md 中完整的 5 段模板
  ```
  Style: Abstract high-tech cover art, inspired by "Linear" app design...

  Color Palette: Primary glowing light is hex code #6B75FF...

  Theme Concept: [Translate article topic into abstract visual metaphor]...

  Environment: Deep black void. Very subtle isometric grid...

  Negative Constraints: NO TEXT, NO LETTERS, NO UI ELEMENTS...
  ```
- **示例**：参见 visual-style-guide.md 中“封面图片示例”部分，了解 Event Intelligence 博客

#### 内联图片（最少 3 张）
- **目的**：通过抽象概念插图在视觉上支持内容部分
- **类型**（所有都必须是抽象的）：
  - 数据簇可视化（浮动信息卡片）
  - 数据流可视化（粒子流）
  - 分割可视化（几何簇）
  - 时间可视化（演变进程）

- **提示模板**：使用 visual-style-guide.md 中完整的 5 段模板
  ```
  Style: [Visualization type] inspired by Linear design system...

  Color Palette: Deep charcoal background (#1a1a1a), #6B75FF accents...

  Concept: [Detailed abstract description with geometric elements]...

  Keywords Allowed: [Minimal labels only]...

  Environment: Deep [void type] with [depth cues]...

  Negative Constraints: NO UI chrome, NO dashboards, NO [specific]...
  ```

**❌ 请勿使用**：
- 简化的 1 段提示
- 仪表板或界面术语
- UI 模型或界面元素
- 传统图表（饼图、条形图、折线图）

**✅ 始终使用**：
- 完整的 5 段结构化模板
- 抽象几何描述
- 精确的 #6B75FF 颜色规范
- 明确的负面约束

### 生成脚本

```bash
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "Your detailed prompt here" \
  --output_dir "path/to/output" \
  --filename "image_name"
```

**选项**：
- `--prompt` (必需)：详细的图像描述
- `--output_dir` (可选)：输出目录（默认：当前目录）
- `--filename` (可选)：文件名前缀（默认：blog_image）

**输出**：`{filename}_{timestamp}.png`

## 内容类型

### 操作指南

**结构**：
```markdown
## Step 1: [Action Verb Title]

Brief explanation of the step.

**Pro Tip**: Insider advice for this step.

![Relevant diagram](images/step1.png)
```

**示例主题**：
- “如何构建电子邮件营销策略”
- “如何优化您的着陆页”
- “如何进行关键词研究”

### 列表文章

**结构**：
```markdown
## 1. [Item Name/Concept]

Description of the item and why it matters.

**Why this works**: Explanation of effectiveness.

![Illustration](images/item1.png)
```

**示例主题**：
- “10 个电子邮件营销最佳实践”
- “2026 年 7 大内容营销趋势”
- “每个营销人员都需要 15 个 SEO 工具”

### 思想领导力

**结构**：
- 争议性或反传统钩子
- 数据支持的论点
- 行业洞察
- 未来预测
- 可操作的要点

**示例主题**：
- “为什么传统营销已死（以及下一步是什么）”
- “内容营销的未来”
- “大多数营销人员对 SEO 的误解”

## SEO 最佳实践

### 标题优化
- **长度**：50-60 个字符
- **格式**：[数字] + [形容词] + [关键词] + [承诺]
- **示例**：“10 Proven Email Marketing Strategies to 3x Your ROI”

### 元描述
- **长度**：150-160 个字符
- **包含**：主要关键词、益处、行动号召
- **示例**：“Learn 10 proven email marketing strategies that top brands use to triple their ROI. Actionable tips inside.”

### Slug 结构
- **格式**：`/blog/[category]/[keyword-slug]`
- **类别**：strategy, playbooks, 或 teardowns
- **Slug**：小写、连字符、富含关键词
- **示例**：`/blog/strategy/email-marketing-best-practices`

### 关键词整合
- **主要关键词**：在标题、H2、第一段、元描述中
- **次要关键词**：在 H3 标题、内容中
- **自然使用**：首先为人类撰写，其次为搜索引擎
- **密度**：1-2% 是理想的，避免关键词堆砌

### 内部链接
- 链接到相关文章（发布时）
- 使用描述性锚文本
- 每篇文章 2-3 个内部链接

## 示例提示

### 针对 AI 助手

**基本请求**：
```
Write a blog post about [topic]
```

**详细请求**：
```
Write a comprehensive how-to guide about email marketing automation for small businesses.
Include 8-10 steps, focus on practical implementation, and target beginners.
Tone: friendly but professional. Include data points where relevant.
```

**列表文章请求**：
```
Write a listicle: "15 Content Marketing Tools Every Startup Needs".
Low density (2-3 points per tool), include pricing tiers, and why each tool matters.
```

### 针对图像生成

**⚠️ 重要**：始终使用完整的 5 段模板。以下示例为可读性而缩写 — 参见 visual-style-guide.md 获取完整模板。

**封面图片示例** (Event Intelligence)：
```bash
--prompt "Style: Abstract high-tech cover art, inspired by \"Linear\" app design. Dark mode UI, minimalist, clean, futuristic.

Color Palette: Primary glowing light is hex code #6B75FF (neon violet-blue indigo). Soft, diffused glow on deep charcoal background.

Theme Concept: Scattered event data signals—exhibitor profiles, attendee behavior patterns, competitive intelligence fragments—flowing as glowing particle streams from all directions, converging into a central crystalline intelligence hub. The hub emanates organized insight pathways radiating outward to strategic decision nodes. Translate this into glowing geometric data streams, interconnected nodes pulsing with #6B75FF light, floating frosted glass prismatic shapes representing crystallized insights, and abstract light trails showing data transformation. Composition representing raw chaos organizing into actionable intelligence.

Environment: Deep black void. Very subtle, barely visible isometric grid fading into darkness. Shallow depth of field with soft bokeh effects on distant data streams.

Negative Constraints: NO TEXT, NO LETTERS, NO WORDS, NO CHARACTERS, NO UI ELEMENTS, NO DASHBOARDS, NO CHARTS. Purely abstract visual shapes and light compositions."
```

**内联图片示例** (Data Flow)：
```bash
--prompt "Style: Abstract real-time data flow visualization inspired by Linear aesthetic. Dark mode, dynamic, flowing composition.

Color Palette: Deep charcoal background, flowing data streams in matte grey with #6B75FF highlights for high-priority signals.

Concept: Living data streams flowing from left to right across the frame—representing real-time event intelligence. Multiple parallel streams of varying thickness, each stream composed of small geometric particles (circles, diamonds, hexagons) moving at different velocities. Key insight nodes pulse with #6B75FF glow as data passes through them. Thin connecting lines branch off from main streams to floating analysis nodes. Create sense of continuous information flow and pattern recognition happening in real-time.

Keywords Allowed: Minimal labels—\"Foot Traffic\", \"Engagement\", \"Leads\". Tiny, clean text integrated into the flow.

Environment: Deep black background with subtle motion blur on particles suggesting speed. No grid—pure void emphasizing movement.

Negative Constraints: NO UI elements, NO charts with axes, NO dashboard frames, NO static graphs. Pure flowing abstract visualization."
```

**更多示例**：参见 [references/visual-style-guide.md](references/visual-style-guide.md) 获取：
- 数据簇可视化
- 分割示意图
- 时间演变图
- 完整提示库

## 工作流集成

此技能与 [webflow-blog-publisher](../webflow-blog-publisher) 无缝协作：

```bash
# 1. 撰写博客文章（使用 AI）
# 输出：workspace/blog/article.md

# 2. 生成图像
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "..." \
  --output_dir workspace/blog/images

# 3. 发布到 Webflow
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

参见 [BLOG_WORKFLOW.md](../BLOG_WORKFLOW.md) 获取完整的端到端指南。

## 故障排除

### 图像生成失败

**错误**：`GEMINI_API_KEY not found`

**解决方案**：
```bash
# 选项 1：环境变量
export GEMINI_API_KEY='your_key'

# 选项 2：密钥文件
echo '{"NANO_API_KEY": "your_key"}' > ~/.claude/lensmor_secrets.json
```

**错误**：`Request timed out`

**解决方案**：
- 简化您的提示（减少细节）
- 检查互联网连接
- 几分钟后重试（API 可能繁忙）

**错误**：`No image data found in response`

**解决方案**：
- 您的提示可能违反内容政策
- 避免品牌名称、受版权保护的内容
- 使用通用描述

### 内容质量问题

**问题**：内容过于通用

**解决方案**：
- 提供更具体的主题细节
- 包含目标受众信息
- 提及具体的痛点
- 请求数据点或统计信息

**问题**：语调过于正式/非正式

**解决方案**：
- 明确请求调整语调
- 参考风格：“Write in professional blog Blog style”
- 提供语调示例

**问题**：内容过长/过短

**解决方案**：
- 指定字数：“Write a 2000-word guide”
- 指定部分：“Include 8 main sections”
- 请求密度：“High density” 或 “Low density”

## 最佳实践

### 内容策略
1. **品牌合规优先**：如果撰写关于 Lensmor/产品的内容，请阅读 brand-guidelines/SKILL.md 获取最新产品信息
2. **研究优先**：深入了解您的主题
3. **了解您的受众**：为特定的读者画像撰写
4. **数据驱动**：包含统计数据和研究
5. **可操作**：每个部分都应提供价值
6. **SEO 意识**：但首先为人类撰写

### 图像策略
1. **风格一致**：在整个过程中使用相同的视觉语言
2. **相关视觉效果**：图像应支持内容，而非分散注意力
3. **高质量**：绝不妥协图像分辨率
4. **描述性 Alt 文本**：为了可访问性和 SEO
5. **战略性放置**：分隔长文本部分

### 发布策略
1. **先起草**：在上线发布前务必审阅
2. **同行评审**：从同事那里获取反馈
3. **SEO 检查**：验证关键词使用和元数据
4. **移动预览**：在移动设备上测试
5. **性能跟踪**：发布后监控分析数据

## 架构

```
hubspot-blog-writer/
├── README.md                  # 此文件
├── SKILL.md                   # AI 工作流指令
├── scripts/
│   ├── gemini_api.py         # 共享 API 客户端
│   └── generate_image.py     # 图像生成工具
└── references/
    └── visual-style-guide.md # 详细视觉指南
```

## 版本历史

### v2.1.0 (2026-02-09)
- ✅ **重大变更**：强制所有图像使用完整的 5 段提示模板
- ✅ 更新 visual-style-guide.md，包含详细模板和示例
- ✅ 添加 4 种内联图像类别模板（数据簇、流、分割、时间）
- ✅ 增强 README，包含模板使用指南和质量要求
- ✅ 消除简化提示，以确保一致的质量

### v2.0.0 (2026-02-08)
- ✅ 重构图像生成以使用共享 API 模块
- ✅ 改进错误处理和用户反馈
- ✅ 添加全面的 README 文档
- ✅ 更清晰的代码架构（106 → 85 行）

### v1.0.0 (2026-02-07)
-