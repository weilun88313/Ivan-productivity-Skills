[English](README.md) | [中文](README.zh.md)

---

# 50k Lead Generation System

> Complete B2B lead generation machine combining Apollo.io, Google Search, and LinkedIn scraping

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

Automated B2B lead generation system that combines multiple data sources (Apollo.io, Google Search, LinkedIn) with AI-powered personalization to generate and qualify leads at scale. Built with n8n workflow automation and Airtable database management.

### Key Features

- 🎯 **Multi-Source Scraping** - Apollo.io, Google Search, LinkedIn data extraction
- 🤖 **AI-Powered Personalization** - Automated outreach message generation
- 📊 **Lead Qualification** - Automated scoring and filtering
- 🔄 **Workflow Automation** - n8n-based pipeline orchestration
- 📁 **Data Management** - Airtable integration for CRM functionality
- ⚡ **Scalable** - Generate up to 50k qualified leads

## Quick Start

### Prerequisites

```bash
# Install dependencies
pip install -r requirements.txt

# Configure API keys
# Add to ~/.claude/lensmor_secrets.json:
{
  "APOLLO_API_KEY": "your_apollo_key",
  "LINKEDIN_COOKIE": "your_linkedin_session",
  "OPENAI_API_KEY": "your_openai_key"
}
```

### Usage

**Basic workflow:**
```
Run the 50k lead generation system for [target industry/role]
```

**With parameters:**
```bash
python scripts/wrapper.py \
  --industry "SaaS" \
  --role "CTO" \
  --company-size "50-200" \
  --limit 1000
```

## How It Works

1. **Data Collection** - Scrapes leads from Apollo.io, Google Search, and LinkedIn
2. **Enrichment** - Cross-references data from multiple sources
3. **Qualification** - Scores leads based on custom criteria
4. **Personalization** - Generates AI-powered outreach messages
5. **Storage** - Stores qualified leads in Airtable CRM

## Configuration

**Required:**
- Apollo.io API key
- LinkedIn session cookie
- OpenAI API key (for personalization)

**Optional:**
- Airtable base ID
- Custom lead scoring rules
- Outreach templates

## Output Format

Leads are stored in Airtable with fields:
- Company name
- Contact name and title
- Email address
- Lead score
- Personalized outreach message
- Source attribution

## Related Skills

| Skill | Purpose |
|-------|---------|
| [keyword-research](../keyword-research/) | Research target markets |
| [content-pipeline](../content-pipeline/) | Full content automation |

## Troubleshooting

### Apollo.io Rate Limiting

- Implement delays between API calls
- Use multiple API keys if available
- Cache results to avoid duplicate calls

### LinkedIn Scraping Blocked

- Rotate user agents
- Use residential proxies
- Respect rate limits

### Low Lead Quality

- Refine qualification criteria
- Adjust scoring weights
- Filter by company size, industry, location

## File Structure

```
50k-lead-generation-system/
├── README.md              # This file
├── SKILL.md               # AI instructions
├── scripts/
│   └── wrapper.py         # Python wrapper
└── workflows/
    └── lead-gen-n8n.json  # n8n workflow
```

## Resources

- [Original Repository](https://github.com/Awaisali36/50k-lead-generation-system)
- [n8n Documentation](https://docs.n8n.io/)
- [Apollo.io API](https://docs.apollo.io/)

---

**Generate leads at scale!** 🚀📊
