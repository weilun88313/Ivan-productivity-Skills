[English](README.md) | [中文](README.zh.md)

---

# Skill 进化管理器

基于经验驱动的 skill 优化系统，从对话中学习并根据用户反馈持续改进 skill 定义。

## 核心功能

- **会话复盘** - 在对话结束时分析 skill 表现
- **经验提取** - 将非结构化反馈转换为结构化 JSON
- **智能缝合** - 自动将学习成果持久化到 `SKILL.md`
- **跨版本对齐** - 在 skill 更新过程中保留经验
- **多 Skill 协同** - 支持多个 skills 的演化

## 快速开始

### 触发进化

```
/evolve
```

或使用自然语言：
```
"复盘一下刚才的对话"
"那个工具不太好用，记录一下"
"把这个经验保存到 skill 里"
```

## 使用示例

### 1. 记录用户偏好

使用 skill 后：
```
"我希望下载默认静音"
```

Agent 将：
1. 扫描对话上下文
2. 识别相关 skill
3. 生成经验 JSON
4. 持久化到 `evolution.json`

### 2. 记录问题修复

遇到问题时：
```
"Windows 下 ffmpeg 路径需要转义"
```

Agent 将此作为修复记录并添加到 skill 知识库。

### 3. 优化提示词

成功交互后：
```
"执行前总是显示预估时间"
```

自定义提示词被保存以供未来使用。

## 进化工作流

### 1. 复盘与提取
- 扫描上下文中的满意/不满意点
- 识别需要进化的 skill
- 生成结构化 JSON：

```json
{
  "preferences": ["用户希望下载默认静音"],
  "fixes": ["Windows 下 ffmpeg 路径需转义"],
  "custom_prompts": "执行前总是打印预估耗时"
}
```

### 2. 持久化经验
```bash
python scripts/merge_evolution.py <skill_path> <json_string>
```

将新经验合并到 `evolution.json`。

### 3. 缝合到文档
```bash
python scripts/smart_stitch.py <skill_path>
```

将 `evolution.json` 转换为 Markdown 并追加到 `SKILL.md`。

### 4. 跨版本对齐

在 `skill-manager` 更新 skill 后：
```bash
python scripts/align_all.py
```

将保留的经验重新缝合到更新后的文档。

## 核心脚本

- `scripts/merge_evolution.py` - 增量合并经验到 JSON
- `scripts/smart_stitch.py` - 从 JSON 生成 Markdown 并追加到 `SKILL.md`
- `scripts/align_all.py` - skill 更新后批量对齐

## 经验架构

```json
{
  "preferences": ["用户", "偏好", "列表"],
  "fixes": ["记录的", "bug", "修复"],
  "custom_prompts": "优化的提示词模板"
}
```

## 最佳实践

- **不要直接编辑 SKILL.md** - 使用 `evolution.json` 管道以在更新时保留变更
- **多 Skill 会话** - 为对话中使用的每个 skill 运行进化流程
- **定期对齐** - 批量更新后运行 `align_all.py`

## 集成

- 在 **skill-manager** 更新过程中保留经验
- 补充 **github-to-skills** 创建的 skills
- 随时间构建机构知识
