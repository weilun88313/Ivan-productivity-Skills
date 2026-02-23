---
name: jike-post-writer
description: "将零散想法或主题转化为即刻（Jike）帖子，可选配图生成。适用场景：(1) 将碎片化想法、笔记整理成即刻帖子，(2) 围绕某个话题展开写成完整帖子，(3) 为帖子生成配图（使用 Gemini API，1:1 比例），(4) 保持一致的个人风格（口语化、轻松随意、像朋友聊天，涵盖 AI/科技/产品/创业/生活话题，50-500字灵活长度）。Use this skill when the user wants to write a 即刻 post, Jike post, or mentions 即刻/jike in the context of content creation."
---

# 即刻帖子写作

将碎片想法转化为即刻风格的中文帖子，配合可选配图。

## 路径配置

所有路径相对于 Skill 根目录（`Skill/jike-post-writer/`）。

| 变量 | 路径 |
|------|------|
| `SKILL_ROOT` | 本 SKILL.md 所在目录 |
| `WORKSPACE` | `../../workspace`（相对于 SKILL_ROOT） |
| `BLOG_IMAGE_GENERATOR` | `../blog-image-generator`（兄弟 Skill） |

## 关键要求

- 所有帖子用**中文**写作
- 风格**口语化、随意**，像朋友聊天
- 长度 **50-500字**，根据内容灵活调整
- 配图**可选**，用户要求时才生成（1:1 正方形）
- 输出目录：`WORKSPACE`
- Markdown 输出：只包含帖子正文，不加标签或元数据

## 工作流程

### 第一步：理解输入

**场景 A：碎片想法**
- 用户提供零散的想法、笔记、bullet points
- 整理、归纳、找到核心观点，组织成帖子

**场景 B：给定话题**
- 用户给一个主题/方向
- 如需要，问 1-2 个关键问题明确角度
- 找到个人视角和具体切入点

### 第二步：写帖子

1. 参考 `references/post_templates.md` 选择合适的结构
2. 参考 `references/brand_persona.md` 保持风格一致
3. 写作要点：
   - 开头要抓人（具体场景、反常识观点、直接提问）
   - 中间言之有物（个人经历、具体案例、有洞察）
   - 结尾自然收束（不强求互动引导，自然就好）
   - 保持口语感，像在跟朋友说话
   - emoji 自然使用（0-3个），不刻意

### 第三步：配图（可选）

仅在用户明确要求配图时执行。

```bash
python Skill/blog-image-generator/scripts/generate.py \
  --platform jike \
  --type post \
  --prompt "图片描述" \
  --output WORKSPACE/jike_post.png \
  --aspect-ratio 1:1
```

- 默认 1:1 正方形比例
- 风格：清新、有质感、不要太商务

### 第四步：输出

- 保存为 `.md` 文件到 `WORKSPACE`
- 只包含帖子正文，直接可复制到即刻

## 资源

- **`references/brand_persona.md`**：写作风格和人设指南
- **`references/post_templates.md`**：帖子结构模板和示例
- **`blog-image-generator`**：统一图片生成引擎（兄弟 Skill，支持 `--platform jike`）
