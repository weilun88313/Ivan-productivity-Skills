"""
Sync published articles from Webflow CMS into the content calendar.

Updates only the Published section and Pillar Coverage table in
workspace/content-calendar.md. Does not modify Backlog or Updates Log.

Usage:
    python Skill/content-strategy/scripts/sync_calendar.py
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime

# Paths relative to repository root
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CALENDAR_PATH = os.path.join(REPO_ROOT, "workspace", "content-calendar.md")
LIST_ARTICLES_SCRIPT = os.path.join(
    REPO_ROOT, "Skill", "webflow-blog-publisher", "scripts", "list_articles.py"
)

# ---------------------------------------------------------------------------
# Pillar assignment rules
# ---------------------------------------------------------------------------

PILLAR_RULES = [
    {
        "pillar": "Event Intelligence & Preparation",
        "keywords": [
            "preparation", "prepare", "planning", "plan", "checklist",
            "before the event", "pre-event", "research event", "choose event",
            "event selection", "evaluate trade show", "event calendar",
            "budget", "goal setting", "first-time exhibitor",
        ],
        "slug_patterns": [
            r"prepar", r"plan", r"checklist", r"before", r"pre-event",
            r"select", r"evaluat", r"budget",
        ],
    },
    {
        "pillar": "Trade Show ROI & Measurement",
        "keywords": [
            "roi", "return on investment", "measurement", "measure",
            "benchmark", "attribution", "cost-per-lead", "cpl",
            "performance", "reporting", "metrics", "kpi",
        ],
        "slug_patterns": [
            r"roi", r"measur", r"benchmark", r"attribution",
            r"cost-per-lead", r"cpl", r"metric", r"kpi", r"report",
        ],
    },
    {
        "pillar": "Lead Capture & Conversion",
        "keywords": [
            "lead capture", "lead generation", "conversion", "convert",
            "follow-up", "follow up", "badge scan", "lead scoring",
            "crm integration", "nurture", "booth engagement",
            "lead qualification", "lead routing",
        ],
        "slug_patterns": [
            r"lead", r"capture", r"conver", r"follow-up", r"followup",
            r"badge", r"scor", r"nurture", r"booth", r"qualif",
        ],
    },
    {
        "pillar": "Competitor & Market Analysis",
        "keywords": [
            "competitor", "competitive", "market analysis", "market trend",
            "intelligence", "competitive landscape", "emerging player",
            "floor plan", "exhibitor data",
        ],
        "slug_patterns": [
            r"competitor", r"competitive", r"market-analy", r"intelligen",
            r"landscape", r"floor-plan",
        ],
    },
    {
        "pillar": "Event Technology & Tools",
        "keywords": [
            "technology", "tech stack", "tools", "software", "platform",
            "automation", "ai", "app", "virtual", "hybrid",
            "event management platform", "analytics tool",
        ],
        "slug_patterns": [
            r"tech", r"tool", r"software", r"platform", r"automat",
            r"app", r"virtual", r"hybrid", r"ai-",
        ],
    },
]


def assign_pillar(article: dict) -> str:
    """Assign a content pillar based on keyword/slug pattern matching."""
    title_lower = article.get("title", "").lower()
    slug_lower = article.get("slug", "").lower()
    pk_lower = article.get("primary_keyword", "").lower()
    secondary = " ".join(article.get("secondary_keywords", [])).lower()
    text_blob = f"{title_lower} {pk_lower} {secondary}"

    best_pillar = "Unassigned"
    best_score = 0

    for rule in PILLAR_RULES:
        score = 0
        # Keyword matches in title + keywords
        for kw in rule["keywords"]:
            if kw in text_blob:
                score += 2
            if kw in title_lower:
                score += 1  # bonus for title match
        # Slug pattern matches
        for pat in rule["slug_patterns"]:
            if re.search(pat, slug_lower):
                score += 1

        if score > best_score:
            best_score = score
            best_pillar = rule["pillar"]

    return best_pillar if best_score > 0 else "Unassigned"


# ---------------------------------------------------------------------------
# CMS data fetching
# ---------------------------------------------------------------------------


def fetch_articles() -> list[dict]:
    """Run list_articles.py and return parsed JSON."""
    if not os.path.isfile(LIST_ARTICLES_SCRIPT):
        print(f"Error: {LIST_ARTICLES_SCRIPT} not found.")
        sys.exit(1)

    result = subprocess.run(
        [sys.executable, LIST_ARTICLES_SCRIPT, "--published-only", "--format", "json"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )

    if result.returncode != 0:
        print(f"Error running list_articles.py:\n{result.stderr}")
        sys.exit(1)

    # The script may print a status line before the JSON; find the JSON array
    stdout = result.stdout.strip()
    json_start = stdout.find("[")
    if json_start == -1:
        print("Error: No JSON array found in list_articles.py output.")
        print(f"Output was:\n{stdout}")
        sys.exit(1)

    return json.loads(stdout[json_start:])


# ---------------------------------------------------------------------------
# Calendar template & rendering
# ---------------------------------------------------------------------------

CALENDAR_TEMPLATE = """# Content Calendar

> Auto-managed by `sync_calendar.py`. Do not edit the **Published** or **Pillar Coverage** sections manually.

## Pillar Coverage

{pillar_coverage_table}

## Backlog

<!-- Add Content Briefs here. Format:
| Priority | Topic | Angle | Content Type | Pillar | Funnel Stage | Status |
|----------|-------|-------|-------------|--------|-------------|--------|
-->

| Priority | Topic | Angle | Content Type | Pillar | Funnel Stage | Status |
|----------|-------|-------|-------------|--------|-------------|--------|

## Published

{published_table}

## Updates Log

<!-- Record updates to existing articles here. Format:
| Date | Article | Changes | Reason |
|------|---------|---------|--------|
-->

| Date | Article | Changes | Reason |
|------|---------|---------|--------|
"""


def build_pillar_coverage(articles: list[dict]) -> str:
    """Build the Pillar Coverage table from articles with assigned pillars."""
    pillar_names = [r["pillar"] for r in PILLAR_RULES] + ["Unassigned"]
    counts: dict[str, dict[str, int]] = {
        p: {"published": 0, "backlog": 0} for p in pillar_names
    }

    for a in articles:
        pillar = a.get("_pillar", "Unassigned")
        counts[pillar]["published"] += 1

    # Parse backlog from existing calendar if it exists
    backlog_pillars = _parse_backlog_pillars()
    for pillar, count in backlog_pillars.items():
        if pillar in counts:
            counts[pillar]["backlog"] = count

    total_pub = sum(c["published"] for c in counts.values())
    total_bl = sum(c["backlog"] for c in counts.values())

    lines = [
        "| Pillar | Published | Backlog | Total |",
        "|--------|-----------|---------|-------|",
    ]
    for p in pillar_names:
        c = counts[p]
        total = c["published"] + c["backlog"]
        if total == 0 and p == "Unassigned":
            continue  # hide Unassigned row if empty
        lines.append(f"| {p} | {c['published']} | {c['backlog']} | {total} |")

    lines.append(f"| **Total** | **{total_pub}** | **{total_bl}** | **{total_pub + total_bl}** |")
    return "\n".join(lines)


def _parse_backlog_pillars() -> dict[str, int]:
    """Parse pillar counts from existing calendar backlog section."""
    if not os.path.isfile(CALENDAR_PATH):
        return {}

    with open(CALENDAR_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the Backlog section
    backlog_match = re.search(r"## Backlog\n(.*?)(?=\n## )", content, re.DOTALL)
    if not backlog_match:
        return {}

    pillar_counts: dict[str, int] = {}
    for line in backlog_match.group(1).split("\n"):
        line = line.strip()
        if not line.startswith("|") or line.startswith("| Priority") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.split("|")]
        # Format: | Priority | Topic | Angle | Content Type | Pillar | Funnel Stage | Status |
        if len(cells) >= 7:
            pillar = cells[5]  # 0 is empty before first |
            if pillar and pillar != "Pillar":
                pillar_counts[pillar] = pillar_counts.get(pillar, 0) + 1

    return pillar_counts


def build_published_table(articles: list[dict]) -> str:
    """Build the Published articles table."""
    lines = [
        "| # | Title | Primary Keyword | Pillar | Slug | Updated |",
        "|---|-------|----------------|--------|------|---------|",
    ]
    for i, a in enumerate(articles, 1):
        title = a.get("title", "Untitled")
        pk = a.get("primary_keyword", "")
        pillar = a.get("_pillar", "Unassigned")
        slug = a.get("slug", "")
        updated = a.get("updated", "")[:10]  # YYYY-MM-DD
        lines.append(f"| {i} | {title} | {pk} | {pillar} | {slug} | {updated} |")

    lines.append(f"\n*{len(articles)} published articles. Last synced: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Calendar file operations
# ---------------------------------------------------------------------------


def read_calendar() -> str | None:
    """Read existing calendar content, or None if it doesn't exist."""
    if not os.path.isfile(CALENDAR_PATH):
        return None
    with open(CALENDAR_PATH, "r", encoding="utf-8") as f:
        return f.read()


def update_calendar(articles: list[dict]) -> None:
    """Update (or create) the content calendar with fresh CMS data."""
    existing = read_calendar()
    pillar_table = build_pillar_coverage(articles)
    published_table = build_published_table(articles)

    if existing is None:
        # Create from template
        content = CALENDAR_TEMPLATE.format(
            pillar_coverage_table=pillar_table,
            published_table=published_table,
        )
    else:
        content = existing
        # Replace Pillar Coverage table
        content = _replace_section(
            content,
            "## Pillar Coverage",
            pillar_table,
        )
        # Replace Published table
        content = _replace_section(
            content,
            "## Published",
            published_table,
        )

    os.makedirs(os.path.dirname(CALENDAR_PATH), exist_ok=True)
    with open(CALENDAR_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def _replace_section(content: str, heading: str, new_body: str) -> str:
    """Replace the body of a markdown section (between its heading and the next ## heading)."""
    # Pattern: heading line, then everything until the next ## or end of file
    pattern = re.compile(
        rf"({re.escape(heading)}\n)(.*?)(?=\n## |\Z)",
        re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        # Section not found — append it
        return content.rstrip() + f"\n\n{heading}\n\n{new_body}\n"

    return content[: match.start(2)] + "\n" + new_body + "\n" + content[match.end(2) :]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print("Fetching published articles from CMS...")
    articles = fetch_articles()
    print(f"  Found {len(articles)} published articles.")

    # Assign pillars
    for a in articles:
        a["_pillar"] = assign_pillar(a)

    pillar_summary = {}
    for a in articles:
        p = a["_pillar"]
        pillar_summary[p] = pillar_summary.get(p, 0) + 1

    print("\nPillar assignment:")
    for pillar, count in sorted(pillar_summary.items()):
        print(f"  {pillar}: {count}")

    # Update calendar
    update_calendar(articles)
    print(f"\nCalendar updated: {CALENDAR_PATH}")


if __name__ == "__main__":
    main()
