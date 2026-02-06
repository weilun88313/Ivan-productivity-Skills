# Webflow Setup Guide

## 1. Get Your Site API Token

1. Log in to Webflow and open your site
2. Go to **Site Settings** → **Integrations** → **API Access**
3. Click **Generate API Token**
4. Copy the token

## 2. Find Your Blog Collection ID

1. In Webflow, go to **CMS** → **Blog Posts** (or your blog collection name)
2. The Collection ID is in the URL: `https://webflow.com/dashboard/sites/.../cms/collections/{COLLECTION_ID}`
3. Alternatively, use the API:
   ```bash
   curl -s -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Accept-Version: 2.0.0" \
     "https://api.webflow.com/v2/sites" | python -m json.tool
   ```
   Then list collections for your site:
   ```bash
   curl -s -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Accept-Version: 2.0.0" \
     "https://api.webflow.com/v2/sites/{SITE_ID}/collections" | python -m json.tool
   ```

## 3. Add Credentials to Secrets

Add both values to `~/.claude/lensmor_secrets.json`:

```json
{
  "WEBFLOW_API_TOKEN": "your-token-here",
  "WEBFLOW_BLOG_COLLECTION_ID": "your-collection-id-here"
}
```

Or set as environment variables:
```bash
export WEBFLOW_API_TOKEN=your-token-here
export WEBFLOW_BLOG_COLLECTION_ID=your-collection-id-here
```

## 4. Verify Your Setup

Run a quick test (will fail gracefully if token is invalid):
```bash
python Skill/webflow-blog-publisher/scripts/publish_to_webflow.py \
  --file workspace/event-intelligence-blog/event-intelligence.md
```

The `--collection_id` flag is optional if already set in secrets. You can still pass it to override.

## Field Mapping

The script auto-detects collection fields by type:
- **name** → Blog post title (always mapped)
- **slug** → URL slug (from `**Slug**` in markdown)
- **First RichText field** → Blog body HTML
- **post-summary / summary / excerpt** → Meta description

If your collection uses different field slugs, the script will print all available fields so you can adjust.
