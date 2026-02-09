# Webflow Blog Publisher

> Publish markdown blog posts to Webflow CMS with automatic image uploading

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

The **Webflow Blog Publisher** automates the process of publishing blog posts to Webflow CMS. It handles markdown-to-HTML conversion, automatic image uploading to Webflow Assets, metadata mapping, and CMS item creation—all via Webflow API v2.

### Key Features

- 📝 **Markdown to HTML** - Automatic conversion with support for tables and code blocks
- 🖼️ **Auto Image Upload** - Local images uploaded to Webflow Assets via presigned S3 URLs
- 👤 **Writer Management** - Random or specified writer profiles with avatars
- 🏷️ **Category Mapping** - Smart category resolution by slug or name
- ⏱️ **Auto Fields** - Calculated read time, timestamps, and sort order
- 🔄 **Retry Logic** - Robust error handling with exponential backoff
- ✅ **Draft/Publish** - Control publishing status with `--publish` flag

## Quick Start

### Prerequisites

```bash
# Install dependencies
pip install requests markdown

# Configure secrets in ~/.claude/lensmor_secrets.json
{
  "WEBFLOW_API_TOKEN": "your_api_token",
  "WEBFLOW_BLOG_COLLECTION_ID": "your_collection_id",
  "WEBFLOW_SITE_ID": "your_site_id"
}
```

See [references/webflow-setup-guide.md](references/webflow-setup-guide.md) for detailed setup instructions.

### Basic Usage

```bash
# Publish as draft (default)
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy

# Publish live immediately
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish

# Specify writer
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --writer "John Doe" \
  --category playbooks
```

## Input Format

The script expects markdown files with this structure (produced by [hubspot-blog-writer](../hubspot-blog-writer)):

```markdown
# Your Blog Post Title

**Slug**: /blog/category/your-post-slug
**Meta Description**: Your SEO-friendly meta description here
**Cover Image**:
![Cover description](images/cover.png)

---

Your article content starts here in markdown format.

## Section Header

Body content with **bold** and *italic* text.

![Inline image](images/diagram.png)

More content...
```

## What the Script Does

### Step-by-Step Process

```
1. Parse Markdown
   └─> Extract title, slug, meta, cover image, body content

2. Upload Images to Webflow Assets
   ├─> Cover image → CDN URL
   └─> Inline images → Replace paths with CDN URLs

3. Convert Markdown to HTML
   └─> With updated CDN image references

4. Map Fields to CMS Schema
   ├─> Auto-detect field names
   ├─> Calculate read time
   ├─> Assign writer and category
   └─> Set timestamps and sort order

5. Create CMS Item
   └─> Draft or published based on --publish flag

6. Return Result
   └─> Item ID and status
```

### Field Mapping

| Source | Webflow CMS Field | Notes |
|--------|-------------------|-------|
| `# Title` | `name` | Post title |
| `**Slug**` | `slug` | Last segment of slug path |
| `**Meta Description**` | `meta-description` | Or first PlainText field |
| `**Cover Image**` | `thumbnail-image`, `large-image` | Uploaded to Assets |
| Body content | First `RichText` field | Usually `details-01` |
| Inline images | Embedded in HTML | Uploaded and CDN URLs inserted |
| Word count ÷ 200 | `read-time` | "6 min read" |
| Current timestamp | `date`, `recently-updated` | ISO 8601 format |
| Writer from JSON | `writer-name`, `writer-image` | From assets/writers/writers.json |
| --category flag | `ref` | Resolved to Webflow item ID |
| Auto-increment | `sort` | Based on existing item count |

## Command-Line Options

```bash
python publish_to_webflow.py [OPTIONS]
```

### Required Options

| Option | Description | Example |
|--------|-------------|---------|
| `--file` | Path to markdown file | `--file article.md` |

### Optional Options

| Option | Description | Default |
|--------|-------------|---------|
| `--category` | Category slug | None |
| `--writer` | Writer name | Random from writers.json |
| `--publish` | Publish immediately | Draft |
| `--collection_id` | Override collection ID | From secrets |

### Categories

Available categories (customize in your Webflow CMS):
- `strategy` - Strategic guides and frameworks
- `playbooks` - Step-by-step tactical guides
- `teardowns` - Case studies and analyses

## Writer Management

### Writer Profiles

Writers are stored in `assets/writers/writers.json`:

```json
[
  {
    "name": "John Doe",
    "image_url": "https://cdn.prod.website-files.com/.../avatar.jpg"
  },
  {
    "name": "Jane Smith",
    "image_url": "https://cdn.prod.website-files.com/.../avatar2.jpg"
  }
]
```

### Adding a Writer

1. **Upload avatar** to Webflow Assets:
   - Go to Webflow Dashboard → Assets
   - Upload image
   - Copy CDN URL

2. **Add to writers.json**:
```json
{
  "name": "New Writer",
  "image_url": "https://cdn.prod.website-files.com/xxx/avatar.jpg"
}
```

3. **Use in publishing**:
```bash
--writer "New Writer"
```

If `--writer` is not specified, a random writer is selected.

## Image Upload Process

### How It Works

```
Local Image → Webflow Assets Upload Request → S3 Presigned URL
    ↓                                               ↓
Get file hash                              Upload to S3
    ↓                                               ↓
Request upload URL                         Webflow CDN URL
    ↓                                               ↓
Upload via presigned URL              Replace in markdown/HTML
```

### Supported Formats

- PNG (`.png`)
- JPEG (`.jpg`, `.jpeg`)
- GIF (`.gif`)
- WebP (`.webp`)
- AVIF (`.avif`)
- SVG (`.svg`)

### Image Requirements

- **Site ID Required**: Images only upload if `WEBFLOW_SITE_ID` is set
- **Local Paths**: Images must be accessible as local files
- **Relative Paths**: Resolved relative to markdown file location
- **Failed Uploads**: Images that fail to upload are removed from content

### Without Site ID

If `WEBFLOW_SITE_ID` is not configured:
- Warning message displayed
- Images stripped from content
- Post created without images
- Manual image upload required

## Configuration

### Secrets File

Create `~/.claude/lensmor_secrets.json`:

```json
{
  "WEBFLOW_API_TOKEN": "your_token_here",
  "WEBFLOW_BLOG_COLLECTION_ID": "collection_id_here",
  "WEBFLOW_SITE_ID": "site_id_here"
}
```

### Environment Variables

Alternatively, use environment variables:

```bash
export WEBFLOW_API_TOKEN='your_token'
export WEBFLOW_BLOG_COLLECTION_ID='collection_id'
export WEBFLOW_SITE_ID='site_id'
```

Environment variables take precedence over secrets file.

## Error Handling

### Automatic Retries

The script includes robust retry logic:

- **Server Errors (5xx)**: Retry up to 3 times with exponential backoff
- **Rate Limiting (429)**: Respect `Retry-After` header
- **Network Errors**: Retry with exponential backoff
- **Timeouts**: 30-second timeout per request

### Common Errors

#### API Token Invalid

```
Error: WEBFLOW_API_TOKEN not found.
```

**Solution**: Check secrets file or environment variable.

#### Collection Not Found

```
Error: Could not fetch collection schema.
```

**Solution**: Verify `WEBFLOW_BLOG_COLLECTION_ID` is correct.

#### Image Upload Fails

```
Warning: WEBFLOW_SITE_ID not set, skipping image uploads.
```

**Solution**: Add `WEBFLOW_SITE_ID` to secrets file.

#### Category Not Found

```
Warning: Category 'xyz' not found. Available: strategy, playbooks, teardowns
```

**Solution**: Use one of the listed available categories.

## Field Auto-Detection

The script automatically detects your CMS schema:

```
Fetching collection schema...
  Found 15 fields: name, slug, details-01, thumbnail-image, ...
```

### Flexible Field Mapping

The script searches for fields using multiple names:

**Meta Description**:
- `post-summary`
- `summary`
- `excerpt`
- `meta-description`
- `description`

**Body Content**:
- First `RichText` field found

**Cover Images**:
- `thumbnail-image`
- `large-image`

This allows the script to work with different Webflow templates.

## Workflow Integration

This skill works seamlessly with [hubspot-blog-writer](../hubspot-blog-writer):

```bash
# Complete workflow
# 1. Write content (AI-assisted)
# 2. Generate images
python Skill/hubspot-blog-writer/scripts/generate_image.py \
  --prompt "..." --output_dir workspace/blog/images

# 3. Publish to Webflow
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/blog/article.md \
  --category strategy \
  --publish
```

See [BLOG_WORKFLOW.md](../BLOG_WORKFLOW.md) for complete guide.

## Advanced Usage

### Custom Collection

Override the default collection:

```bash
python publish_to_webflow.py \
  --file article.md \
  --collection_id custom_collection_id
```

### Testing Without Publishing

Omit `--publish` to create drafts:

```bash
# Creates draft for review
python publish_to_webflow.py --file article.md --category strategy
```

Then publish manually in Webflow CMS dashboard.

### Batch Publishing

Publish multiple articles:

```bash
for file in workspace/blog/*.md; do
  python publish_to_webflow.py --file "$file" --category strategy
done
```

### Update Existing Posts

The script always creates new items. To update:
1. Manually delete old item in Webflow CMS
2. Re-run script to create updated version

Or modify the script to use `PATCH` instead of `POST`.

## Troubleshooting

### Script Hangs During Image Upload

**Problem**: S3 upload timeout

**Solution**:
- Check internet connection
- Reduce image file sizes (< 5MB recommended)
- Try uploading one image manually first

### Draft Not Appearing in CMS

**Problem**: Item created but not visible

**Solution**:
- Check CMS filters (may be filtered out)
- Verify in "All Items" view
- Check `isArchived` and `isDraft` status

### Read Time Incorrect

**Problem**: Shows wrong duration

**Solution**:
- Formula: word_count ÷ 200 WPM
- Adjust `WORDS_PER_MINUTE` constant in script
- Minimum is 1 minute

### Images Not Uploading

**Problem**: `WEBFLOW_SITE_ID` not set

**Solution**:
```json
{
  "WEBFLOW_SITE_ID": "get_from_webflow_dashboard"
}
```

Find Site ID in Webflow Dashboard → Site Settings → General.

## API Rate Limits

Webflow API v2 has rate limits:

- **60 requests per minute** per API token
- **429 status** when limit exceeded
- **Retry-After header** indicates wait time

The script automatically handles rate limiting with exponential backoff.

## Best Practices

### Before Publishing

1. **Review Content**: Always proofread markdown file
2. **Check Images**: Verify all images exist and paths are correct
3. **Test Category**: Use valid category slug
4. **Draft First**: Test without `--publish` flag first

### For Production

1. **Backup**: Keep markdown source files
2. **Version Control**: Commit markdown files to git
3. **Monitor**: Check Webflow CMS after publishing
4. **SEO Check**: Verify meta descriptions and slugs

### Security

1. **Protect Secrets**: Never commit secrets file to git
2. **Token Permissions**: Use token with minimal required permissions
3. **Rotate Keys**: Periodically regenerate API tokens
4. **Environment Separation**: Use different tokens for staging/production

## Output Example

```
Parsing article.md...
  Title: The Ultimate Guide to Email Marketing
  Slug: email-marketing-guide
  Meta: Learn proven strategies to boost your email ROI...
  Cover image: yes
  Inline images: 3
  Read time: 8 min read

Uploading images to Webflow Assets...
  Uploaded: cover.png → https://cdn.prod.website-files.com/.../cover.png
  Uploaded: diagram1.png → https://cdn.prod.website-files.com/.../diagram1.png
  Uploaded: diagram2.png → https://cdn.prod.website-files.com/.../diagram2.png
  Body: 12450 chars HTML
  Writer: John Doe

Fetching collection schema (abc123...)...
  Found 12 fields: name, slug, details-01, thumbnail-image, ...
  Existing items: 47, new sort → 48
  Mapped body → 'details-01'
  Mapped thumbnail-image → cover image
  Mapped large-image → cover image
  Mapped meta-description → 'meta-description'
  Mapped date → '2026-02-08T10:30:00.000Z'
  Mapped read-time → '8 min read'
  Mapped sort → 48
  Mapped writer-name → 'John Doe'
  Mapped writer-image → 'https://cdn.prod.website-files.com/.../avatar.jpg'
  Mapped ref → 'strategy' (ID: xyz789)

Creating CMS item (draft)...

Success! CMS item created.
  Item ID: item_xyz123
  Status: Draft

  To publish, run again with --publish flag,
  or publish manually in Webflow CMS editor.
```

## Architecture

```
webflow-blog-publisher/
├── README.md                     # This file
├── SKILL.md                      # AI workflow instructions
├── scripts/
│   └── publish_to_webflow.py    # Main publishing script (449 lines)
├── references/
│   └── webflow-setup-guide.md   # Setup instructions
└── assets/
    └── writers/
        └── writers.json          # Writer profiles
```

## Version History

### v2.0.0 (2026-02-08)
- ✅ Added comprehensive README documentation
- ✅ Verified robust error handling and retry logic
- ✅ Complete field auto-detection
- ✅ Automatic image uploading via Webflow Assets

### v1.0.0 (2026-02-07)
- Initial release with Webflow API v2 integration
- Markdown to HTML conversion
- Writer profile management
- Category mapping

## Resources

- [SKILL.md](SKILL.md) - Technical documentation and field mapping
- [Setup Guide](references/webflow-setup-guide.md) - Webflow configuration
- [HubSpot Blog Writer](../hubspot-blog-writer) - Content creation skill
- [Blog Workflow](../BLOG_WORKFLOW.md) - End-to-end publishing guide
- [Webflow API Docs](https://developers.webflow.com/) - Official API reference

## Contributing

Improvements welcome! Focus areas:
- Support for updating existing items
- Bulk publishing features
- Additional field mappings
- Custom template support

## License

Proprietary - For internal use

## Support

For issues:
1. Check this README troubleshooting section
2. Review setup guide for configuration
3. Verify API token permissions in Webflow
4. Test with a simple markdown file first

---

**Happy Publishing!** 🚀📄
