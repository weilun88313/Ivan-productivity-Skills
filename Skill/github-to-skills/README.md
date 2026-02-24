[English](README.md) | [中文](README.zh.md)

---

# GitHub to Skills Factory

Automated tool for converting GitHub repositories into specialized AI skills with standardized structure and metadata.

## Key Features

- **Automatic Analysis** - Fetches repository metadata, README, and latest commit hash
- **Standardized Scaffolding** - Creates consistent skill directory structure
- **Enhanced Metadata** - Generates `SKILL.md` with extended frontmatter for lifecycle management
- **Wrapper Generation** - Creates interface scripts (`wrapper.py`) to interact with tools
- **Version Tracking** - Captures commit hash for future update detection

## Quick Start

### Trigger the Skill

```
/github-to-skills <github_url>
```

Or use natural language:
```
"Package this repo into a skill: https://github.com/user/repo"
```

### Example

```
/github-to-skills https://github.com/yt-dlp/yt-dlp
```

This will:
1. Fetch repository information
2. Analyze the README to understand usage patterns
3. Create a new skill directory with `SKILL.md` and wrapper scripts
4. Inject metadata including `github_url`, `github_hash`, and `version`

## Generated Skill Structure

```
new-skill/
├── SKILL.md          # Skill definition with extended metadata
└── scripts/
    └── wrapper.py    # Interface script
```

## Metadata Schema

Every generated skill includes this frontmatter in `SKILL.md`:

```yaml
---
name: <kebab-case-repo-name>
description: <concise-description>
github_url: <original-repo-url>
github_hash: <latest-commit-hash>
version: <tag-or-0.1.0>
created_at: <ISO-8601-date>
entry_point: scripts/wrapper.py
dependencies: ["list", "of", "dependencies"]
---
```

## Core Scripts

- `scripts/fetch_github_info.py` - Fetches repository details from GitHub
- `scripts/create_github_skill.py` - Orchestrates skill scaffolding

## Best Practices

- **Isolation** - Generated skills manage their own dependencies
- **Progressive Disclosure** - Only include necessary wrapper code, reference original repo for details
- **Idempotency** - `github_hash` enables future update detection via `skill-manager`

## Integration

Works seamlessly with:
- **skill-manager** - Uses metadata for update tracking
- **skill-evolution-manager** - Enables experience-based optimization
