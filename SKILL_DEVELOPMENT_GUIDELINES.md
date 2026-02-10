# Skill 开发规范 / Skill Development Guidelines

[English](#english) | [中文](#中文)

---

## English

### Documentation Requirements

**CRITICAL**: Every skill MUST have bilingual documentation.

#### Required Files for Every Skill

1. **README.md (English)**
   - **MUST be concise and focused** - aim for 40-50% reduction from verbose versions
   - Overview and key features
   - Quick start and essential usage examples (1-2 examples max)
   - Configuration (only if needed)
   - **NO version history, NO detailed changelogs, NO redundant examples**

2. **README.zh.md (Chinese - Simplified)**
   - Complete translation of README.md
   - All technical terms in English (code, commands, file paths)
   - Natural Chinese for descriptions and explanations
   - **Maintain same concise structure as English version**

3. **Language Switcher (Both Files)**
   - Add this at the TOP of both README.md and README.zh.md:
   ```markdown
   [English](README.md) | [中文](README.zh.md)

   ---

   ```

4. **SKILL.md**
   - AI instructions and workflow
   - English only (AI instructions)
   - Include brand-guidelines reference if product-related

#### Skill Structure Template

```
my-new-skill/
├── README.md              # English documentation (required) ✅
├── README.zh.md           # Chinese documentation (required) ✅
├── SKILL.md               # AI instructions (required) ✅
├── scripts/               # Executable scripts (if needed)
│   └── *.py
├── references/            # Reference materials (if needed)
│   └── *.md
└── examples/              # Usage examples (if needed)
    └── *.md
```

### When Creating a New Skill

- [ ] Create README.md with language switcher
- [ ] Create README.zh.md with language switcher
- [ ] Create SKILL.md with AI instructions
- [ ] If product-related, reference brand-guidelines in SKILL.md
- [ ] Test all code examples in documentation
- [ ] Add skill to main repository

### When Updating a Skill

- [ ] Update README.md if functionality changes
- [ ] Update README.zh.md to match README.md changes
- [ ] Update SKILL.md if AI workflow changes
- [ ] Update version number and changelog
- [ ] Test updated functionality

### When Syncing to Public Repository

- [ ] Ensure all Skills have both README.md and README.zh.md
- [ ] Verify language switchers are present
- [ ] Remove any sensitive information (API keys, credentials)
- [ ] Update public repository with all documentation changes
- [ ] Sync both English and Chinese documentation

### Quality Checklist

Before committing any skill:

- [ ] Both README.md and README.zh.md exist
- [ ] Language switchers at the top of both files
- [ ] All code examples tested and working
- [ ] No sensitive information (API keys, credentials)
- [ ] Translations are accurate and natural
- [ ] File structure follows template
- [ ] SKILL.md references brand-guidelines if needed

---

## 中文

### 文档要求

**重要**：每个技能必须有双语文档。

#### 每个 Skill 必需的文件

1. **README.md（英文）**
   - **必须简洁明了** - 目标是比冗长版本减少 40-50%
   - 概述和关键特性
   - 快速开始和必要的使用示例（最多 1-2 个示例）
   - 配置说明（仅在需要时）
   - **不包含版本历史、详细更新日志、冗余示例**

2. **README.zh.md（简体中文）**
   - README.md 的完整翻译
   - 所有技术术语使用英文（代码、命令、文件路径）
   - 描述和解释使用自然的中文
   - **保持与英文版本相同的简洁结构**

3. **语言切换器（两个文件）**
   - 在 README.md 和 README.zh.md 顶部添加：
   ```markdown
   [English](README.md) | [中文](README.zh.md)

   ---

   ```

4. **SKILL.md**
   - AI 指令和工作流
   - 仅英文（AI 指令）
   - 如果与产品相关，包含 brand-guidelines 引用

#### Skill 结构模板

```
my-new-skill/
├── README.md              # 英文文档（必需）✅
├── README.zh.md           # 中文文档（必需）✅
├── SKILL.md               # AI 指令（必需）✅
├── scripts/               # 可执行脚本（如需要）
│   └── *.py
├── references/            # 参考资料（如需要）
│   └── *.md
└── examples/              # 使用示例（如需要）
    └── *.md
```

### 创建新 Skill 时

- [ ] 创建带语言切换器的 README.md
- [ ] 创建带语言切换器的 README.zh.md
- [ ] 创建带 AI 指令的 SKILL.md
- [ ] 如果与产品相关，在 SKILL.md 中引用 brand-guidelines
- [ ] 测试文档中的所有代码示例
- [ ] 将技能添加到主仓库

### 更新 Skill 时

- [ ] 如果功能改变，更新 README.md
- [ ] 更新 README.zh.md 以匹配 README.md 的改动
- [ ] 如果 AI 工作流改变，更新 SKILL.md
- [ ] 更新版本号和变更日志
- [ ] 测试更新的功能

### 同步到公共仓库时

- [ ] 确保所有 Skills 都有 README.md 和 README.zh.md
- [ ] 验证语言切换器存在
- [ ] 移除任何敏感信息（API 密钥、凭据）
- [ ] 用所有文档更改更新公共仓库
- [ ] 同步英文和中文文档

### 质量检查清单

提交任何技能之前：

- [ ] README.md 和 README.zh.md 都存在
- [ ] 两个文件顶部都有语言切换器
- [ ] 所有代码示例已测试且能运行
- [ ] 没有敏感信息（API 密钥、凭据）
- [ ] 翻译准确自然
- [ ] 文件结构遵循模板
- [ ] SKILL.md 如需要已引用 brand-guidelines

---

## Automation Scripts

### Translate README to Chinese

**Using Gemini Flash (Cost-Effective)**

Translate a single README:
```bash
python3 scripts/translate_readme.py Skill/my-skill/README.md
```

Batch translate all READMEs:
```bash
./scripts/translate_all_readmes.sh
```

Features:
- ✅ Uses Gemini 2.0 Flash (low cost)
- ✅ Preserves all code blocks and technical terms
- ✅ Maintains markdown formatting
- ✅ Auto-adds language switcher
- ✅ Smart detection of existing translations

### Check Bilingual Documentation

```bash
# Check all skills have bilingual READMEs
./scripts/check-bilingual-docs.sh
```

### Create New Skill

```bash
# Use skill-creator with bilingual template
./scripts/create-skill.sh my-new-skill --bilingual
```

### Sync to Public Repository

```bash
# Sync with documentation checks
./scripts/sync-to-public.sh --check-docs
```

---

## 自动化脚本 / Automation Scripts

### 翻译 README 为中文

**使用 Gemini Flash（成本友好）**

翻译单个 README：
```bash
python3 scripts/translate_readme.py Skill/my-skill/README.md
```

批量翻译所有 README：
```bash
./scripts/translate_all_readmes.sh
```

特性：
- ✅ 使用 Gemini 2.0 Flash（低成本）
- ✅ 保留所有代码块和技术术语
- ✅ 维护 markdown 格式
- ✅ 自动添加语言切换器
- ✅ 智能检测现有翻译

---

## Version History

### v1.0.0 (2026-02-10)
- ✅ Established bilingual documentation requirement
- ✅ Added language switcher standard
- ✅ Created quality checklist
- ✅ Defined skill structure template

---

**Remember**: Good documentation is as important as good code!
**记住**：好的文档和好的代码一样重要！

## Sync Rules

### Files That Should NOT Be Synced to Public Repository

**CRITICAL - Never sync these to public repository:**

1. **workspace/** - All generated content and temporary files
   - Already in .gitignore
   - Contains user-specific generated content
   - Can be very large (images, PDFs, PPT files)

2. **brand-guidelines/** - Private brand information
   - Contains proprietary product details
   - Competitive positioning
   - Internal messaging

3. **.opensource/** - Sync tooling (only for private repo)
   - Sync scripts
   - Brand configuration
   - Cleanup tools

4. **Sensitive data**:
   - API keys and secrets
   - Real author names/emails (anonymize)
   - Company-specific URLs
   - Internal documentation

### Verification Before Sync

```bash
# Check what will be synced
cd Ivan_Skills_Public
git status

# Ensure workspace is not tracked
git ls-files | grep workspace
# Should return nothing

# Check for brand information
grep -r "Lensmor" . --exclude-dir=.git
# Should return nothing or minimal references
```
