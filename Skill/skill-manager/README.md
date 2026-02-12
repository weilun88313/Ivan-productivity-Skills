[English](README.md) | [中文](README.zh.md)

---

# Skill Lifecycle Manager

Comprehensive tool for managing GitHub-based skills, including update detection, inventory management, and guided upgrade workflows.

## Key Features

- **Audit & Scan** - Automatically scans local skills directory for GitHub-based skills
- **Update Detection** - Compares local commit hashes with remote repositories
- **Status Reports** - Generates detailed reports identifying outdated skills
- **Guided Updates** - Structured workflow for upgrading skill wrappers
- **Inventory Management** - List and delete skills with version tracking

## Quick Start

### Check for Updates

```
/skill-manager check
```

Or use natural language:
```
"Scan my skills for updates"
```

### List All Skills

```
/skill-manager list
```

### Delete a Skill

```
/skill-manager delete <skill_name>
```

## Usage Examples

### 1. Check for Outdated Skills

```
/skill-manager check
```

Output example:
```
Found 3 outdated skills:
- yt-dlp (behind 50 commits)
- ffmpeg-tool (behind 2 commits)
- image-processor (current)
```

### 2. Update a Skill

After checking, trigger an update:
```
"Update yt-dlp"
```

The update workflow:
1. Fetches new README from remote repository
2. Analyzes differences (new features, deprecated flags, usage changes)
3. Rewrites `SKILL.md` to reflect new capabilities
4. Updates `github_hash` in frontmatter
5. Updates wrapper scripts if CLI arguments changed

## Core Scripts

- `scripts/scan_and_check.py` - Scans directories and compares versions
- `scripts/update_helper.py` - Backs up files before updates
- `scripts/list_skills.py` - Lists installed skills with metadata
- `scripts/delete_skill.py` - Removes skill folders

## Metadata Requirements

Requires skills to have the following metadata (created by `github-to-skills`):

```yaml
---
github_url: <source-repository>
github_hash: <commit-hash>
---
```

## Workflow: Updating a Skill

1. **Detect Changes** - `scan_and_check.py` compares local vs remote hash
2. **Fetch New Context** - Agent retrieves updated README
3. **Diff Analysis** - Identifies breaking changes and new features
4. **Refactor** - Updates `SKILL.md` and wrapper scripts
5. **Update Hash** - Records new `github_hash` for future tracking
6. **Verify** - Runs validation checks

## Integration

- Works with skills created by **github-to-skills**
- Updates preserved by **skill-evolution-manager** after upgrades
