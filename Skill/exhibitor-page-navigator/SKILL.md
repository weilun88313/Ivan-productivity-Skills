---
name: exhibitor-page-navigator
description: "Navigate from a trade show's homepage to its official exhibitor directory or list page. Use for: finding where the list of participating companies is located without extracting the data itself."
version: 2.0.0
---

# Exhibitor Page Navigator

## Overview

This skill provides a structured workflow to locate the specific URL of a trade show's **exhibitor directory** starting from its homepage. It's designed to find the page where exhibitors are listed, not to extract the data itself.

## Objective

**Input**: `homepage_url` (e.g., `https://www.example-tradeshow.com`)

**Output**: A JSON object containing:
```json
{
  "status": "success" | "failed",
  "homepage_url": "{input_url}",
  "found_directory_url": "{the_url_you_found}",
  "navigation_method": "Menu Click" | "URL Guessing" | "Search Function",
  "verification_reason": "Brief explanation of why this is the correct page",
  "confidence_level": "high" | "medium" | "low"
}
```

## Critical Constraints

**DO NOT:**
- ❌ Extract exhibitor data (company names, contacts, emails)
- ❌ Return login/portal pages (e.g., "Exhibitor Zone", "Exhibitor Login")
- ❌ Return sales/booking pages (e.g., "Book a Stand", "Why Exhibit")
- ❌ Return archived directories from past events
- ❌ Navigate beyond the directory landing page

**DO:**
- ✅ Find the page that lists all exhibitors
- ✅ Verify the page is functional and current
- ✅ Return the exact URL of the directory
- ✅ Provide clear reasoning for your choice

## Workflow

### Phase 1: Initial Navigation (The Pathfinder)

**Step 1: Load Homepage**
1. Visit `homepage_url`
2. Wait for page to fully load (2-3 seconds)
3. Handle cookie/privacy popups immediately:
   - Look for "Accept All", "Accept", "I Agree", or "Close" buttons
   - Click to dismiss and clear the view

**Step 2: Scan Navigation Menus**

Check the following locations in order:

1. **Header Navigation**
   - Main menu items
   - Dropdown menus (may require hover)
   - "Attend", "Visit", "Visitors", "Exhibition" sections

2. **Footer Navigation**
   - "For Visitors" or "Attend" sections
   - Quick links

3. **Main Content Area**
   - Hero section buttons
   - Featured links
   - Call-to-action buttons

**Target Keywords** (Priority Order):
- ✅ **Primary**: "Exhibitor List", "Exhibitor Directory", "List of Exhibitors"
- ✅ **Secondary**: "Exhibitors", "Who's Exhibiting", "Participating Companies"
- ✅ **Tertiary**: "Directory", "Who's Coming", "Show Directory"
- ✅ **Related**: "Floor Plan" (often links to exhibitor list), "Sponsors & Partners"

**Negative Keywords** (Avoid):
- ❌ "Become an Exhibitor", "Why Exhibit"
- ❌ "Exhibitor Login", "Exhibitor Portal", "Exhibitor Zone"
- ❌ "Book Your Stand", "Reserve Space"
- ❌ "Exhibitor Services", "Exhibitor Resources"

**Step 3: Click Most Relevant Link**
- If multiple matches exist, prioritize exact matches first
- Prefer links with "List" or "Directory" in the text
- Record the `navigation_method` as "Menu Click"

### Phase 2: Fallback Strategies

If no link is found in Phase 1, try these strategies in order:

**Strategy A: URL Guessing**

Append common paths to the base URL:
```
{base_url}/exhibitors
{base_url}/exhibitor-list
{base_url}/exhibitor-directory
{base_url}/directory
{base_url}/exhibitors-list
{base_url}/en/exhibitors (for multilingual sites)
{base_url}/attend/exhibitors
{base_url}/visit/exhibitors
```

Try each URL and check if it loads successfully (status 200).

**Strategy B: Site Search**

If the site has a search function:
1. Click on search icon/input
2. Search for "exhibitor list" or "exhibitors"
3. Look for results that match target keywords
4. Click the most relevant result

**Strategy C: Sitemap Check**

Look for `/sitemap.xml` and scan for URLs containing:
- "exhibitor"
- "directory"
- "list"

### Phase 3: Verification (The Inspector)

Once you reach a candidate page, verify it's the correct directory:

**Visual Indicators** (Check for at least 2):
- 🔍 Search bar or search functionality
- 🎚️ Filters (by category, hall, country, product type)
- 🔤 A-Z index or alphabetical navigation
- 📋 List/Grid view toggle
- 📄 Pagination controls
- 🏢 Company logos displayed in grid/list format

**Content Indicators**:
- Multiple company names visible (at least 5-10)
- Repeated card/tile structure for companies
- Company logos or profile images
- Brief company descriptions or categories

**Title/Heading Check**:
- Page title or H1 contains: "Exhibitor", "List", "Directory", "Participants"
- URL path includes: `/exhibitor`, `/directory`, `/list`

**Year Verification**:
- Check that the event year matches current or upcoming year
- Look for year indicators in:
  - Page title
  - Breadcrumbs
  - Event date displayed on page
- If year is past, look for a "Next Edition" or year selector

### Phase 4: Final Output

Return a strict JSON object:

```json
{
  "status": "success",
  "homepage_url": "https://www.example-tradeshow.com",
  "found_directory_url": "https://www.example-tradeshow.com/exhibitors",
  "navigation_method": "Menu Click",
  "verification_reason": "Page contains search bar, A-Z filter, and displays 50+ exhibitor logos in grid format. Page title is 'Exhibitor Directory 2026'.",
  "confidence_level": "high"
}
```

**Confidence Levels**:
- **High**: Found via clear menu link + 3+ visual indicators + correct year
- **Medium**: Found via URL guessing + 2 visual indicators + year uncertain
- **Low**: Found via fallback method + 1 visual indicator + no year confirmation

**If Failed**:
```json
{
  "status": "failed",
  "homepage_url": "https://www.example-tradeshow.com",
  "found_directory_url": null,
  "navigation_method": "None",
  "verification_reason": "Tried menu navigation, URL guessing (/exhibitors, /directory, /exhibitor-list), and site search. No exhibitor directory page found. Possible reasons: directory not yet published, requires login, or uses external platform.",
  "confidence_level": "n/a"
}
```

## Best Practices

### 1. Handle Modals & Popups
- **Cookie Banners**: Look for "Accept All", "Accept", "I Agree" buttons
- **Newsletter Popups**: Find "Close", "X", or "No Thanks" buttons
- **Language Selectors**: Choose English if available for easier keyword matching

### 2. Hover for Hidden Menus
- Many trade show sites use hover-activated dropdowns
- Use `browser_move_mouse` to trigger hover states
- Wait 500ms after hover before looking for links

### 3. Check Event Year
- Always verify the directory is for current/upcoming event
- Look for year selectors or dropdowns
- Check breadcrumbs: "Home > Events > 2026 > Exhibitors"
- If archived, look for "Latest Edition" or "Upcoming Event" links

### 4. Handle Multi-language Sites
- If landing on non-English homepage, look for language switcher
- Common paths: `/en/`, `/en-us/`, `/english/`
- Check URL structure and try adding `/en/` before exhibitor paths

### 5. Distinguish Similar Pages
- **Exhibitor Directory** ✅: Lists all exhibitors (your target)
- **Floor Plan** ⚠️: May link to exhibitor list (follow if promising)
- **Sponsors Page** ❌: Only lists sponsors, not all exhibitors
- **Exhibitor Services** ❌: Information for exhibitors, not a list

## Common Edge Cases

### Case 1: Login Required
If you encounter a login page:
```json
{
  "status": "failed",
  "verification_reason": "Exhibitor directory requires login/registration to access"
}
```

### Case 2: External Platform
If exhibitors are on a subdomain or external site:
```
www.example-show.com → exhibitors.example-show.com
www.example-show.com → directory.anotherplatform.com
```
Follow the link and verify as usual.

### Case 3: Multiple Directories
If there are separate directories (e.g., "Exhibitors" vs "Sponsors"):
- Choose the one labeled "Exhibitors" or "Participants"
- Return the most comprehensive list
- Note in `verification_reason` if multiple directories exist

### Case 4: PDF or Downloadable Lists
If the only option is a downloadable PDF/Excel:
```json
{
  "status": "success",
  "found_directory_url": "https://example.com/exhibitor-list.pdf",
  "navigation_method": "Download Link",
  "verification_reason": "Exhibitor list only available as downloadable PDF",
  "confidence_level": "medium"
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Cookie banner blocks view | Look for "Accept All" or "X" button in corners |
| No exhibitor link visible | Try URL guessing: `/exhibitors`, `/directory` |
| Hover menu doesn't show | Use `browser_move_mouse` on menu items |
| Found login page instead | Try backing up and looking for "View List" or public directory link |
| Directory shows past event | Look for year selector dropdown or "Next Edition" link |
| Multiple languages | Switch to English using language selector (usually in header/footer) |
| External platform redirect | Follow redirect and verify the external page |

## Success Metrics

A successful navigation should result in:
- ✅ URL that displays exhibitor list/directory
- ✅ Page is publicly accessible (no login required)
- ✅ Event year is current or upcoming
- ✅ At least 2 visual indicators confirmed
- ✅ Confidence level of "medium" or higher

## Example Workflow

**Input**: `https://www.ces.tech`

1. **Load Homepage**: Accept cookie banner
2. **Scan Header**: Find "Attend" dropdown
3. **Hover on "Attend"**: Menu expands
4. **Click**: "Exhibitor Directory" link
5. **Verify**: Page shows search bar, filters, 2000+ exhibitor cards
6. **Output**:
```json
{
  "status": "success",
  "homepage_url": "https://www.ces.tech",
  "found_directory_url": "https://www.ces.tech/exhibitor-directory",
  "navigation_method": "Menu Click",
  "verification_reason": "Page has search bar, category filters, and displays 2000+ exhibitor cards in grid format with logos and descriptions",
  "confidence_level": "high"
}
```
