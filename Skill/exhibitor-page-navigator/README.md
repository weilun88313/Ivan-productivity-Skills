[English](README.md) | [中文](README.zh.md)

---


# Exhibitor Page Navigator

> Automatically find exhibitor directory pages on trade show websites

## Overview

A workflow skill that locates exhibitor directory pages on trade show websites using intelligent navigation strategies and verification checks.

## Use Cases

- 🔍 **Market Research** - Find exhibitor lists for competitive analysis
- 📊 **Lead Generation** - Locate potential prospects at industry events
- 🎯 **Event Planning** - Research company participation
- 🌐 **Web Scraping Prep** - Find the right URL before data extraction

## Quick Start

### Input

Provide a trade show homepage URL:
```
https://www.example-tradeshow.com
```

### Output

JSON with directory URL and verification:

```json
{
  "status": "success",
  "found_directory_url": "https://www.example-tradeshow.com/exhibitors",
  "navigation_method": "Menu Click",
  "verification_reason": "Page has search bar, filters, 200+ exhibitor cards",
  "confidence_level": "high"
}
```

## How It Works

1. **Navigation** - Load homepage, handle popups, scan menus, click exhibitor links
2. **Fallback Strategies** - URL guessing (`/exhibitors`, `/directory`), site search, sitemap check
3. **Verification** - Confirm with search bars, filters, company listings, page title validation

## What It Finds

✅ **Will Find:**
- Public exhibitor directories
- Participating company lists
- Exhibitor search pages
- Floor plans with listings

❌ **Won't Return:**
- Login/portal pages
- Sales pages
- Past event archives
- Sponsor-only lists

## Confidence Levels

| Level | Meaning |
|-------|---------|
| **High** | Menu link + 3+ indicators (search/filters/pagination) |
| **Medium** | URL guess + 2 indicators (cards but no filters) |
| **Low** | Fallback method + 1 indicator |

## Edge Cases

- **Login Required** - Returns failed status with reason
- **Archived Events** - Checks year, looks for "Next Edition" links
- **Multi-language** - Switches to English or tries `/en/` paths
- **PDF Lists** - Returns PDF URL with medium confidence

## Troubleshooting

- **No link found** - Check if list is published, try `/exhibitors` manually, look for "Coming Soon"
- **Login page returned** - Look for "View as Guest" or public directory options
- **Past event shown** - Check year selector dropdown or "Next Edition" links

## Limitations

- Only locates directory URLs (does not extract data)
- Cannot bypass login requirements
- Does not scrape contact information

## Integration Example

```python
# Get URL from skill output
directory_url = "https://www.example.com/exhibitors"

# Then scrape with your preferred tool
import requests
from bs4 import BeautifulSoup

response = requests.get(directory_url)
soup = BeautifulSoup(response.content, 'html.parser')
exhibitors = soup.find_all('div', class_='exhibitor-card')
```

## FAQ

**Q: Can this extract exhibitor data?**
A: No, it only finds the URL. Use scraping tools for extraction.

**Q: What if login is required?**
A: Returns `status: "failed"` with explanation.

**Q: How accurate is URL guessing?**
A: About 60-70% success rate for common patterns.

---

**Note**: Requires AI assistants with web browsing capabilities. Provides structured approach for browser automation or web scraping tools.
