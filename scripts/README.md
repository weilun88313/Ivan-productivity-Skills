# Your Name Skills - Automation Scripts

Utility scripts for managing Your Name Skills repository.

## Translation Scripts

### translate_readme.py

Translate README.md to README.zh.md using Gemini Flash.

**Usage:**
```bash
python3 translate_readme.py <path/to/README.md> [options]

Options:
  -o, --output PATH    Output path (default: README.zh.md in same directory)
  --api-key KEY        Gemini API key (or set GEMINI_API_KEY env var)
```

**Example:**
```bash
# Translate a single README
python3 translate_readme.py ../Skill/website/blog-writer/README.md

# Specify custom output
python3 translate_readme.py ../Skill/website/blog-writer/README.md -o /tmp/README.zh.md
```

**Features:**
- Uses Gemini 2.0 Flash (cost-effective)
- Preserves code blocks, file paths, commands
- Maintains markdown formatting
- Auto-adds language switcher

**API Key Setup:**
```bash
# Option 1: Add to .env in the repository root
GEMINI_API_KEY=your_key

# Option 2: Environment variable
export GEMINI_API_KEY='your_key'
```

### translate_all_readmes.sh

Batch translate all README.md files in the Skills directory.

**Usage:**
```bash
./translate_all_readmes.sh
```

**Behavior:**
- Scans all subdirectories in `Skill/`
- Translates each README.md to README.zh.md
- Prompts before overwriting existing translations
- Shows progress with counters

**Example Output:**
```
🌐 Batch Translation: README.md → README.zh.md
Using: Gemini Flash (Cost-effective)

[1/7] 📁 blog-writer
🔄 Translating with Gemini Flash...
💾 Writing to ../Skill/website/blog-writer/README.zh.md...
✅ Translation complete!
  ✅ Translated successfully

[2/7] 📁 mycompany-brand-guideline
...
```

## Cost Comparison

| Model | Cost per 1M tokens | Typical README Cost |
|-------|-------------------|---------------------|
| Claude Sonnet | ~$3.00 | ~$0.15 |
| Gemini Flash | ~$0.075 | ~$0.004 |
| **Savings** | **40x cheaper** | **~97% savings** |

*For a typical 5000-token README, Gemini Flash costs ~$0.004 vs Claude's ~$0.15*

## Requirements

```bash
pip install requests
```

## Troubleshooting

### API Key Not Found

**Error:** `❌ Error: Gemini API key required.`

**Solution:**
1. Check .env file exists in repo root with `GEMINI_API_KEY=...`
2. Check environment variable: `echo $GEMINI_API_KEY`
3. Set the key using one of the methods above

### Translation Failed

**Error:** `❌ Translation failed`

**Common causes:**
- API rate limit exceeded (wait a few minutes)
- Invalid API key
- Network connectivity issues
- README file too large (>8000 tokens)

**Solution:**
- Check API key is valid
- Wait and retry
- For large files, split into sections

### Code Blocks Not Preserved

**Issue:** Code blocks are translated or broken

**This shouldn't happen**, but if it does:
1. Check the prompt in `translate_readme.py`
2. Verify the markdown formatting in the source
3. Report the issue with the specific README

## Development

### Testing Translation Quality

Test on a sample README before batch processing:

```bash
# Test translation
python3 translate_readme.py ../Skill/skill-creator/README.md -o /tmp/test.zh.md

# Compare output
diff /tmp/test.zh.md ../Skill/skill-creator/README.zh.md
```

### Improving Translation Prompt

Edit the prompt in `translate_readme.py`:
- Line ~50: Main translation instructions
- Adjust temperature (currently 0.3) for consistency
- Modify maxOutputTokens for longer documents

## License

Proprietary - For internal use

---

**Questions?** Check the main [SKILL_DEVELOPMENT_GUIDELINES.md](../SKILL_DEVELOPMENT_GUIDELINES.md)
