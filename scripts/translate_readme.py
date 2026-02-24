#!/usr/bin/env python3
"""
Translate README.md to README.zh.md using Gemini Flash
Cost-effective translation for documentation
"""

import os
import sys
import json
import argparse
import requests

import env_setup; env_setup.init_env()


def load_api_key():
    """Load Gemini API key from environment (populated by env_setup)."""
    return os.environ.get("GEMINI_API_KEY")


def translate_with_gemini(text, api_key):
    """
    Translate English text to Simplified Chinese using Gemini Flash.
    
    Args:
        text: English text to translate
        api_key: Gemini API key
        
    Returns:
        Translated Chinese text
    """
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    
    prompt = f"""Translate the following README documentation from English to Simplified Chinese (简体中文).

CRITICAL RULES:
1. Keep ALL technical elements UNCHANGED:
   - Code blocks (bash, python, json, etc.)
   - File paths (e.g., /path/to/file)
   - Command examples (e.g., npm install, git commit)
   - URLs and links
   - Variable names and function names
   - Product names (e.g., "Gemini API", "Webflow", "LinkedIn")
   
2. Translate ONLY:
   - Headings and titles
   - Descriptions and explanations
   - Instructions and steps
   - Feature lists and benefits
   - Comments in code (if any)

3. Maintain EXACT formatting:
   - Keep all markdown syntax (###, -, *, ```, etc.)
   - Preserve line breaks and spacing
   - Keep all links in the same format
   - Maintain table structures

4. Translation style:
   - Use professional technical Chinese
   - Be natural and clear
   - Use standard technical terminology
   - Keep sentences concise

5. DO NOT add or remove content, only translate

Here is the README content to translate:

---
{text}
---

Provide ONLY the translated content, no explanations or comments."""

    headers = {
        "Content-Type": "application/json",
    }
    
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 8000,
        }
    }
    
    url_with_key = f"{url}?key={api_key}"
    
    try:
        print("🔄 Translating with Gemini Flash...")
        response = requests.post(url_with_key, headers=headers, json=data, timeout=120)
        response.raise_for_status()
        
        result = response.json()
        
        # Extract translated text
        if "candidates" in result:
            candidate = result["candidates"][0]
            translated = candidate["content"]["parts"][0]["text"]
            return translated.strip()
        else:
            print(f"❌ Error: Unexpected API response format")
            print(json.dumps(result, indent=2))
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error calling Gemini API: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


def add_language_switcher(content):
    """Add language switcher at the top of the file."""
    switcher = """[English](README.md) | [中文](README.zh.md)

---

"""
    # Check if switcher already exists
    if "[English](README.md)" in content[:200]:
        return content
    return switcher + content


def main():
    parser = argparse.ArgumentParser(
        description="Translate README.md to README.zh.md using Gemini Flash"
    )
    parser.add_argument(
        "readme_path",
        help="Path to README.md file"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output path (default: README.zh.md in same directory)"
    )
    parser.add_argument(
        "--api-key",
        help="Gemini API key (or set GEMINI_API_KEY environment variable)"
    )
    
    args = parser.parse_args()
    
    # Load API key
    api_key = args.api_key or load_api_key()
    if not api_key:
        print("❌ Error: Gemini API key required.")
        print("Add GEMINI_API_KEY to .env in the repository root. See .env.example.")
        sys.exit(1)
    
    # Read README.md
    readme_path = args.readme_path
    if not os.path.exists(readme_path):
        print(f"❌ Error: File not found: {readme_path}")
        sys.exit(1)
    
    print(f"📖 Reading {readme_path}...")
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove existing language switcher if present
    if content.startswith("[English](README.md)"):
        lines = content.split('\n')
        # Find the first content line after switcher and separator
        start_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('#') and i > 0:
                start_idx = i
                break
        content = '\n'.join(lines[start_idx:])
    
    # Translate
    translated = translate_with_gemini(content, api_key)
    
    if not translated:
        print("❌ Translation failed")
        sys.exit(1)
    
    # Add language switcher
    final_content = add_language_switcher(translated)
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        # Same directory, change .md to .zh.md
        dir_path = os.path.dirname(readme_path)
        output_path = os.path.join(dir_path, "README.zh.md")
    
    # Write translated content
    print(f"💾 Writing to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"✅ Translation complete!")
    print(f"   English: {readme_path}")
    print(f"   Chinese: {output_path}")


if __name__ == "__main__":
    main()
