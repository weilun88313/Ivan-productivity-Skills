"""
Shared environment setup for all scripts.

Loads API keys from .env file (preferred) with fallback to legacy JSON secrets file.
"""

import os
import sys

# Alias mapping: old JSON key names → canonical env var names
_ALIASES = {
    "NANO_API_KEY": "GEMINI_API_KEY",
}

_initialized = False


def init_env():
    """
    Load environment variables from .env at the repository root.

    Falls back to ~/.claude/mycompany_secrets.json if .env is missing or
    python-dotenv is not installed, printing a deprecation warning.
    """
    global _initialized
    if _initialized:
        return
    _initialized = True

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dotenv_path = os.path.join(repo_root, ".env")

    loaded_dotenv = False
    try:
        from dotenv import load_dotenv
        if os.path.isfile(dotenv_path):
            load_dotenv(dotenv_path)
            loaded_dotenv = True
    except ImportError:
        pass

    if not loaded_dotenv:
        _fallback_json()

    # Apply alias mapping so scripts can always use the canonical name
    for old_key, new_key in _ALIASES.items():
        if not os.environ.get(new_key) and os.environ.get(old_key):
            os.environ[new_key] = os.environ[old_key]


def _fallback_json():
    """Load secrets from legacy JSON file and inject into os.environ."""
    import json

    secrets_path = os.path.expanduser("~/.claude/mycompany_secrets.json")
    if not os.path.isfile(secrets_path):
        return

    print(
        "WARNING: Loading secrets from ~/.claude/mycompany_secrets.json is deprecated.\n"
        "         Please migrate to a .env file in the repository root.\n"
        "         See .env.example for the expected format.",
        file=sys.stderr,
    )

    try:
        with open(secrets_path, "r") as f:
            secrets = json.load(f)
        for key, value in secrets.items():
            if isinstance(value, str) and not os.environ.get(key):
                os.environ[key] = value
    except Exception:
        pass
