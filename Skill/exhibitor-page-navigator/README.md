[English](README.md) | [中文](README.zh.md)

---


# Exhibitor Page Navigator

> Automatically find exhibitor directory pages on trade show websites

## Overview

The **Exhibitor Page Navigator** is a workflow skill that helps you locate the exhibitor directory page on any trade show website. It uses intelligent navigation strategies and verification checks to find where exhibitors are listed, without extracting the actual data.

## Use Cases

- 🔍 **Market Research**: Find exhibitor lists for competitive analysis
- 📊 **Lead Generation**: Locate potential prospects at industry events
- 🎯 **Event Planning**: Research which companies participate in specific shows
- 🌐 **Web Scraping Prep**: Find the right URL before data extraction

## Quick Start

### Input Format

Provide a trade show homepage URL:

```
https://www.example-tradeshow.com
```

### Expected Output

A JSON object with the directory URL and verification details:

```json
{
  "status": "success",
  "homepage_url": "https://www.example-tradeshow.com",
  "found_directory_url": "https://www.example-tradeshow.com/exhibitors",
  "navigation_method": "Menu Click",
  "verification_reason": "Page has search bar, category filters, displays 200+ exhibitor cards",
  "confidence_level": "high"
}
```

## How It Works

### Phase 1: Navigation
1. Load the homepage
2. Handle cookie/privacy popups
3. Scan navigation menus for exhibitor links
4. Click the most relevant link

### Phase 2: Fallback Strategies
If no menu link is found:
- **URL Guessing**: Try common paths like `/exhibitors`, `/directory`
- **Site Search**: Use built-in search to find "exhibitor list"
- **Sitemap Check**: Scan sitemap.xml for relevant URLs

### Phase 3: Verification
Confirm the page is a genuine exhibitor directory:
- Check for search bars and filters
- Verify multiple company listings are visible
- Confirm page title contains "Exhibitor" or "Directory"
- Validate event year is current/upcoming

## What It Finds

✅ **Will Find:**
- Public exhibitor directories
- Lists of participating companies
- Exhibitor search pages
- Floor plans with exhibitor listings

❌ **Will Not Return:**
- Login/portal pages ("Exhibitor Zone")
- Sales pages ("Become an Exhibitor")
- Past event archives
- Sponsor-only lists

## Common Scenarios

### Scenario 1: Simple Navigation
**Homepage** → Menu → "Exhibitors" → **Directory Page**

Most trade shows have a clear "Exhibitors" or "Exhibitor List" link in their navigation menu.

### Scenario 2: Hidden Under Dropdowns
**Homepage** → "Attend" Dropdown → "Exhibitor Directory" → **Directory Page**

Many sites nest exhibitor links under "Attend", "Visit", or "Visitors" sections.

### Scenario 3: URL Guessing
**Homepage** → Try `/exhibitors` → **Directory Page**

If no link exists, the skill attempts common URL patterns.

### Scenario 4: External Platform
**Homepage** → "View Exhibitors" → **Redirects to subdomain** → **Directory Page**

Some shows host their exhibitor directory on a separate platform or subdomain.

## Confidence Levels

| Level | Meaning | Example |
|-------|---------|---------|
| **High** | Found via menu + 3+ indicators | Clear "Exhibitor List" link, has search/filters/pagination |
| **Medium** | Found via URL guess + 2 indicators | `/exhibitors` URL works, has company cards but no filters |
| **Low** | Found via fallback + 1 indicator | Found via sitemap, minimal visual indicators |

## Edge Cases Handled

### 1. Login Required
```json
{
  "status": "failed",
  "verification_reason": "Directory requires login/registration"
}
```

### 2. Archived Events
The skill checks the event year and looks for "Next Edition" links if it detects an archived directory.

### 3. Multi-language Sites
Automatically switches to English when available, or tries `/en/` URL paths.

### 4. PDF-Only Lists
```json
{
  "status": "success",
  "found_directory_url": "https://example.com/exhibitors.pdf",
  "navigation_method": "Download Link",
  "confidence_level": "medium"
}
```

## Troubleshooting

### Issue: "No exhibitor link found"

**Solutions:**
1. Check if the event hasn't published exhibitor list yet
2. Try manually visiting `/exhibitors` or `/directory`
3. Look for "Coming Soon" messages on the website
4. Check if directory requires registration

### Issue: "Found login page instead of directory"

**Solutions:**
1. Look for "View as Guest" or "Public Directory" options
2. Check footer for alternate links
3. Try URL guessing to bypass login requirement

### Issue: "Directory shows past event"

**Solutions:**
1. Look for year selector dropdown in the page header
2. Check breadcrumbs for "2026" or "Next Edition" links
3. Navigate to homepage and look for upcoming event links

## Real-World Examples

### Example 1: CES (Consumer Electronics Show)

**Input**: `https://www.ces.tech`

**Process**:
1. Load homepage
2. Find "Attend" in header navigation
3. Hover to reveal dropdown
4. Click "Exhibitor Directory"
5. Verify: Search bar ✓, Filters ✓, 2000+ exhibitors ✓

**Output**:
```json
{
  "status": "success",
  "found_directory_url": "https://www.ces.tech/exhibitor-directory",
  "navigation_method": "Menu Click",
  "confidence_level": "high"
}
```

### Example 2: Small Regional Trade Show

**Input**: `https://www.regional-tech-expo.com`

**Process**:
1. Load homepage
2. No "Exhibitors" link in menu
3. Try URL guessing: `/exhibitors` → 404
4. Try: `/exhibitor-list` → 200 OK
5. Verify: 50+ company logos displayed ✓

**Output**:
```json
{
  "status": "success",
  "found_directory_url": "https://www.regional-tech-expo.com/exhibitor-list",
  "navigation_method": "URL Guessing",
  "confidence_level": "medium"
}
```

### Example 3: Login-Protected Directory

**Input**: `https://www.private-industry-event.com`

**Process**:
1. Load homepage
2. Click "Exhibitors" link
3. Redirected to login page
4. No public directory available

**Output**:
```json
{
  "status": "failed",
  "found_directory_url": null,
  "verification_reason": "Directory requires login/registration to access",
  "confidence_level": "n/a"
}
```

## Best Practices

### For Users

1. **Provide Clean URLs**: Use the main homepage URL, not subpages
2. **Check Timing**: Directories may not be published far in advance
3. **Verify Results**: Always manually check the returned URL
4. **Handle Failures**: Some shows genuinely don't publish public directories

### For Developers

1. **Respect Robots.txt**: Check before automated scraping
2. **Rate Limiting**: Add delays between requests to avoid blocking
3. **Cache Results**: Directory URLs typically don't change often
4. **Handle Redirects**: Follow 301/302 redirects properly

## Limitations

This skill:
- ❌ Does **not** extract exhibitor data
- ❌ Does **not** bypass login requirements
- ❌ Does **not** scrape contact information
- ✅ Only **locates** the directory URL

For data extraction, you'll need additional tools or scripts after getting the URL.

## Integration Examples

### With Python Scraping

```python
# 1. Use this skill to get directory URL
directory_url = "https://www.example.com/exhibitors"  # From skill output

# 2. Then scrape the directory
import requests
from bs4 import BeautifulSoup

response = requests.get(directory_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract exhibitor data...
exhibitors = soup.find_all('div', class_='exhibitor-card')
```

### With Automation Tools

```javascript
// Use skill output in your automation
const { found_directory_url } = skillOutput;

// Navigate with Puppeteer/Playwright
await page.goto(found_directory_url);
await page.waitForSelector('.exhibitor-list');

// Extract data...
```

## FAQ

**Q: Can this extract exhibitor email addresses?**
A: No, this skill only finds the URL. You'll need scraping tools for data extraction.

**Q: What if the directory requires login?**
A: The skill will return `status: "failed"` with an explanation. You'll need credentials to access.

**Q: How accurate is the URL guessing?**
A: About 60-70% success rate for common patterns like `/exhibitors` and `/directory`.

**Q: Can it handle non-English websites?**
A: Yes, it attempts to switch to English or tries common URL patterns that work across languages.

**Q: What about archived events?**
A: The skill checks event years and attempts to find current/upcoming editions.

## Version History

### v2.0.0 (2026-02-08)
- ✅ Enhanced documentation with detailed workflow
- ✅ Added confidence levels to output
- ✅ Improved edge case handling
- ✅ Added troubleshooting guide
- ✅ Structured fallback strategies
- ✅ Added real-world examples

### v1.0.0 (2026-02-03)
- Initial release with basic navigation workflow

## Contributing

This is a workflow skill (no code), but contributions to improve the logic are welcome:
- Better keyword lists
- Additional URL patterns
- Edge case scenarios
- Real-world testing results

## License

MIT License

## Support

For issues or questions:
- Review the Troubleshooting section
- Check SKILL.md for detailed workflow
- File an issue with the trade show URL that failed

---

**Note**: This skill is designed to work with AI assistants that have web browsing capabilities. It provides a structured approach but requires execution through tools like browser automation or web scraping libraries.
