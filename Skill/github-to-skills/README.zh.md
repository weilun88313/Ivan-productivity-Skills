[English](README.md) | [中文](README.zh.md)

---

# GitHub 转 Skill 工厂

自动将 GitHub 仓库转换为标准化 AI Skill 的工具，包含完整的结构和元数据。

## 核心功能

- **自动分析** - 抓取仓库元数据、README 和最新 commit hash
- **标准化脚手架** - 创建一致的 Skill 目录结构
- **增强元数据** - 生成带扩展 frontmatter 的 `SKILL.md`，用于生命周期管理
- **包装器生成** - 创建接口脚本（`wrapper.py`）与工具交互
- **版本追踪** - 捕获 commit hash，便于后续更新检测

## 快速开始

### 触发 Skill

```
/github-to-skills <github_url>
```

或使用自然语言：
```
"把这个仓库打包成 skill: https://github.com/user/repo"
```

### 示例

```
/github-to-skills https://github.com/yt-dlp/yt-dlp
```

执行流程：
1. 获取仓库信息
2. 分析 README 理解使用模式
3. 创建新的 skill 目录，包含 `SKILL.md` 和包装器脚本
4. 注入元数据，包括 `github_url`、`github_hash` 和 `version`

## 生成的 Skill 结构

```
new-skill/
├── SKILL.md          # Skill 定义及扩展元数据
└── scripts/
    └── wrapper.py    # 接口脚本
```

## 元数据架构

每个生成的 skill 在 `SKILL.md` 中包含以下 frontmatter：

```yaml
---
name: <kebab-case-repo-name>
description: <简洁描述>
github_url: <原始仓库URL>
github_hash: <最新commit hash>
version: <标签或0.1.0>
created_at: <ISO-8601日期>
entry_point: scripts/wrapper.py
dependencies: ["依赖", "列表"]
---
```

## 核心脚本

- `scripts/fetch_github_info.py` - 从 GitHub 获取仓库详情
- `scripts/create_github_skill.py` - 编排 skill 脚手架创建

## 最佳实践

- **隔离性** - 生成的 skills 管理自己的依赖
- **渐进式披露** - 只包含必要的包装器代码，详细内容引用原始仓库
- **幂等性** - `github_hash` 使 `skill-manager` 能够检测更新

## 集成

无缝协作：
- **skill-manager** - 使用元数据进行更新追踪
- **skill-evolution-manager** - 支持基于经验的优化
