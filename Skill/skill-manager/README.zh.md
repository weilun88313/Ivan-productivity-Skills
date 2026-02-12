[English](README.md) | [中文](README.zh.md)

---

# Skill 生命周期管理器

用于管理基于 GitHub 的 skills 的综合工具，包括更新检测、库存管理和引导式升级流程。

## 核心功能

- **审计与扫描** - 自动扫描本地 skills 目录中的 GitHub-based skills
- **更新检测** - 对比本地 commit hash 与远程仓库
- **状态报告** - 生成详细报告，识别过期的 skills
- **引导式更新** - 结构化的 skill 升级流程
- **库存管理** - 列出和删除 skills，支持版本追踪

## 快速开始

### 检查更新

```
/skill-manager check
```

或使用自然语言：
```
"扫描我的 skills 看看有没有更新"
```

### 列出所有 Skills

```
/skill-manager list
```

### 删除 Skill

```
/skill-manager delete <skill_name>
```

## 使用示例

### 1. 检查过期的 Skills

```
/skill-manager check
```

输出示例：
```
发现 3 个过期的 skills：
- yt-dlp (落后 50 个 commits)
- ffmpeg-tool (落后 2 个 commits)
- image-processor (最新)
```

### 2. 更新 Skill

检查后，触发更新：
```
"更新 yt-dlp"
```

更新流程：
1. 从远程仓库获取新的 README
2. 分析差异（新功能、废弃参数、使用变化）
3. 重写 `SKILL.md` 以反映新功能
4. 更新 frontmatter 中的 `github_hash`
5. 如果 CLI 参数有变化，更新包装器脚本

## 核心脚本

- `scripts/scan_and_check.py` - 扫描目录并比对版本
- `scripts/update_helper.py` - 更新前备份文件
- `scripts/list_skills.py` - 列出已安装的 skills 及元数据
- `scripts/delete_skill.py` - 删除 skill 文件夹

## 元数据要求

要求 skills 包含以下元数据（由 `github-to-skills` 创建）：

```yaml
---
github_url: <源仓库>
github_hash: <commit hash>
---
```

## 工作流：更新 Skill

1. **检测变化** - `scan_and_check.py` 对比本地与远程 hash
2. **获取新内容** - Agent 获取更新的 README
3. **差异分析** - 识别破坏性变更和新功能
4. **重构** - 更新 `SKILL.md` 和包装器脚本
5. **更新 Hash** - 记录新的 `github_hash` 用于未来追踪
6. **验证** - 运行验证检查

## 集成

- 适用于 **github-to-skills** 创建的 skills
- 升级后的更新由 **skill-evolution-manager** 保留
