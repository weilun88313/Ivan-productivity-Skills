[English](README.md) | [中文](README.zh.md)

---

# Skill Evolution Manager

Experience-driven skill optimization system that learns from conversations and continuously improves skill definitions based on user feedback.

## Key Features

- **Session Review** - Analyzes skill performance at conversation end
- **Experience Extraction** - Converts unstructured feedback into structured JSON
- **Smart Stitching** - Automatically persists learnings to `SKILL.md`
- **Cross-Version Alignment** - Preserves experiences through skill updates
- **Multi-Skill Coordination** - Supports evolution across multiple skills

## Quick Start

### Trigger Evolution

```
/evolve
```

Or use natural language:
```
"Review what we just did"
"That tool didn't work well, record this"
"Save this experience to the skill"
```

## Usage Examples

### 1. Record User Preferences

After using a skill:
```
"I prefer downloads to be muted by default"
```

Agent will:
1. Scan conversation context
2. Identify the relevant skill
3. Generate experience JSON
4. Persist to `evolution.json`

### 2. Document Fixes

When encountering issues:
```
"The ffmpeg path needs escaping on Windows"
```

Agent captures this as a fix and adds to skill knowledge.

### 3. Optimize Prompts

After successful interactions:
```
"Always show estimated time before execution"
```

Custom prompts are saved for future use.

## Evolution Workflow

### 1. Review & Extract
- Scan context for satisfaction/dissatisfaction points
- Identify which skill needs evolution
- Generate structured JSON:

```json
{
  "preferences": ["User wants downloads muted by default"],
  "fixes": ["Windows ffmpeg path requires escaping"],
  "custom_prompts": "Always print estimated duration before execution"
}
```

### 2. Persist Experience
```bash
python scripts/merge_evolution.py <skill_path> <json_string>
```

Merges new experiences into `evolution.json`.

### 3. Stitch to Documentation
```bash
python scripts/smart_stitch.py <skill_path>
```

Converts `evolution.json` to Markdown and appends to `SKILL.md`.

### 4. Cross-Version Alignment

After `skill-manager` updates a skill:
```bash
python scripts/align_all.py
```

Re-stitches preserved experiences to updated documentation.

## Core Scripts

- `scripts/merge_evolution.py` - Incrementally merges experiences to JSON
- `scripts/smart_stitch.py` - Generates Markdown from JSON and appends to `SKILL.md`
- `scripts/align_all.py` - Batch alignment after skill updates

## Experience Schema

```json
{
  "preferences": ["list", "of", "user", "preferences"],
  "fixes": ["documented", "bug", "fixes"],
  "custom_prompts": "optimized prompt templates"
}
```

## Best Practices

- **Don't Edit SKILL.md Directly** - Use `evolution.json` pipeline to preserve changes through updates
- **Multi-Skill Sessions** - Run evolution workflow for each skill used in conversation
- **Regular Alignment** - Run `align_all.py` after batch updates

## Integration

- Preserves experiences through **skill-manager** updates
- Complements skills created by **github-to-skills**
- Builds institutional knowledge over time
