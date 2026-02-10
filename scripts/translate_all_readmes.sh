#!/bin/bash
# Batch translate all README.md files to README.zh.md using Gemini Flash

SKILLS_DIR="/Users/ivan/Documents/Ivan_Skills/Skill"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TRANSLATE_SCRIPT="$SCRIPT_DIR/translate_readme.py"

echo "🌐 Batch Translation: README.md → README.zh.md"
echo "Using: Gemini Flash (Cost-effective)"
echo ""

# Count total skills
total_skills=$(find "$SKILLS_DIR" -maxdepth 1 -type d | tail -n +2 | wc -l)
current=0

for skill_dir in "$SKILLS_DIR"/*/ ; do
    skill_name=$(basename "$skill_dir")
    readme="$skill_dir/README.md"
    readme_zh="$skill_dir/README.zh.md"
    
    current=$((current + 1))
    
    echo "[$current/$total_skills] 📁 $skill_name"
    
    # Check if README.md exists
    if [ ! -f "$readme" ]; then
        echo "  ⏭️  No README.md, skipping"
        continue
    fi
    
    # Check if README.zh.md already exists
    if [ -f "$readme_zh" ]; then
        echo "  ⚠️  README.zh.md already exists"
        read -p "  Overwrite? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "  ⏭️  Skipped"
            continue
        fi
    fi
    
    # Translate
    python3 "$TRANSLATE_SCRIPT" "$readme"
    
    if [ $? -eq 0 ]; then
        echo "  ✅ Translated successfully"
    else
        echo "  ❌ Translation failed"
    fi
    echo ""
done

echo "🎉 Batch translation complete!"
