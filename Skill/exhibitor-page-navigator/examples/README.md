# Example Scenarios

This directory contains real-world example scenarios for the Exhibitor Page Navigator skill.

## Files Overview

| File | Scenario | Status | Confidence |
|------|----------|--------|------------|
| `success-high-confidence.json` | Large trade show with clear navigation | ✅ Success | High |
| `success-medium-confidence.json` | Regional show found via URL guessing | ✅ Success | Medium |
| `success-external-platform.json` | Directory on external subdomain | ✅ Success | High |
| `success-pdf-only.json` | Small fair with PDF list | ✅ Success | Medium |
| `failed-login-required.json` | Login-protected directory | ❌ Failed | N/A |
| `failed-not-published.json` | Directory not yet available | ❌ Failed | N/A |

## Example Structure

Each example file contains:

```json
{
  "scenario": "Brief description of the use case",
  "input": {
    "homepage_url": "The trade show homepage URL"
  },
  "navigation_steps": [
    "Step-by-step description of navigation process"
  ],
  "verification_checks": {
    "search_bar": true/false,
    "filters": true/false,
    "pagination": true/false,
    "company_logos": true/false,
    "exhibitor_count": "Approximate count",
    "page_title_contains_exhibitor": true/false,
    "current_year": true/false
  },
  "output": {
    "status": "success" | "failed",
    "homepage_url": "Input URL",
    "found_directory_url": "Found URL or null",
    "navigation_method": "Menu Click | URL Guessing | etc.",
    "verification_reason": "Explanation of findings",
    "confidence_level": "high | medium | low | n/a"
  },
  "notes": "Additional context or observations"
}
```

## Success Examples

### High Confidence
**Scenario**: Large international trade show (CES-style)
- Clear menu navigation
- Comprehensive directory features
- 2000+ exhibitors
- Full search and filter functionality

**File**: `success-high-confidence.json`

### Medium Confidence
**Scenario**: Regional trade show found via URL guessing
- No menu links available
- Found via `/exhibitor-list` URL pattern
- 50+ exhibitors visible
- Basic display, no advanced filters

**File**: `success-medium-confidence.json`

### External Platform
**Scenario**: Directory hosted on subdomain
- Redirects to `directory.example.com`
- Full featured platform
- 300+ exhibitors
- Successfully handled external redirect

**File**: `success-external-platform.json`

### PDF Only
**Scenario**: Small trade fair with downloadable list
- No web directory interface
- PDF file with exhibitor data
- 80 exhibitors listed
- Common for smaller events

**File**: `success-pdf-only.json`

## Failure Examples

### Login Required
**Scenario**: Private/member-only directory
- All paths redirect to login
- No public access option
- No URL guessing bypass available

**File**: `failed-login-required.json`

### Not Yet Published
**Scenario**: Future event with pending directory
- Event 12+ months away
- "Coming Soon" messaging
- No exhibitor data available yet

**File**: `failed-not-published.json`

## Using These Examples

### For Testing
Use these examples to validate your implementation:

```python
import json

# Load example
with open('examples/success-high-confidence.json') as f:
    example = json.load(f)

# Test your implementation
input_url = example['input']['homepage_url']
expected_output = example['output']

# Run your skill...
actual_output = run_navigator_skill(input_url)

# Compare results
assert actual_output == expected_output
```

### For Documentation
Reference specific examples when explaining edge cases or success scenarios.

### For Training
Use as training data for improving navigation strategies or verification logic.

## Contributing New Examples

To add a new example:

1. Create a new JSON file following the structure above
2. Name it descriptively: `[status]-[scenario-name].json`
3. Include all required fields
4. Add realistic navigation steps
5. Provide clear verification reasoning
6. Update this README with a summary

## Notes

- All examples use fictional URLs to avoid external dependencies
- Navigation steps describe what an AI assistant would do
- Verification checks reflect real-world directory characteristics
- Scenarios cover the most common success and failure patterns
