#!/usr/bin/env python3
"""
Syncs live metrics, self-hosted dark/light SVG badges, and featured project metadata into README.md.
Can run locally or in GitHub Actions via cron — zero external Shields.io/Camo dependency.
"""

import os
import re
import json
import urllib.request
import urllib.error
import subprocess
from html import escape

GITHUB_USER = "FelixIsaac"
FEATURED_REPOS = [
    {
        "repo": "FelixIsaac/whatsapp-mcp-extended",
        "name": "whatsapp-mcp-extended",
        "lang": "Go",
        "role": "**Production WhatsApp MCP Server** — 26 curated transport tools, webhooks, anti-ban rate limiting, self-healing watchdog, and JID safety allowlists. Built for Claude Code, Cursor, OpenCode, and Codex.",
    },
    {
        "repo": "FelixIsaac/tokenusage",
        "name": "tokenusage",
        "lang": "Rust",
        "role": "**Blazing-Fast AI Telemetry** — Cost & quota tracking across 10 providers (Claude Code, Codex, Antigravity, Gemini, Grok, DeepSeek). Includes TUI dashboard, SQLite WAL cache, & 1-line zero-dep installers.",
    },
    {
        "repo": "FelixIsaac/tandem",
        "name": "tandem",
        "lang": "TypeScript",
        "role": "**Real-Session Browser MCP** — Enables AI agents to drive authenticated Chrome browser sessions cleanly without headless detection blocks. Published on npm as `@felixisaac/tandem`.",
    },
    {
        "repo": "FelixIsaac/claude-code-sync",
        "name": "claude-code-sync",
        "lang": "Go",
        "role": "**Age-Encrypted Agent Config Sync** — Securely syncs Claude Code environments, prompts, and settings across machines via GitHub with cryptographic age encryption.",
    },
    {
        "repo": "FelixIsaac/cmux-orbit",
        "name": "cmux-orbit",
        "lang": "TypeScript",
        "role": "**Agent-First Mobile Mission Control** — Drive Claude Code, Grok CLI, Codex, Pi, and Antigravity sessions from your phone over Tailscale with live thinking & token streaming.",
    },
]

STACK_ITEMS = [
    ("Rust", "#de6e46"),
    ("Go", "#00ADD8"),
    ("TypeScript", "#3178C6"),
    ("Python", "#3b82f6"),
    ("Swift", "#F05138"),
    ("Next.js", "#a1a1aa"),
    ("Cloudflare Workers", "#f38020"),
    ("SQLite WAL", "#38bdf8"),
    ("Docker", "#2496ED"),
    ("Tailscale", "#94a3b8"),
]


def github_api_get(endpoint):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        try:
            res = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
            if res.returncode == 0 and res.stdout.strip():
                token = res.stdout.strip()
        except Exception:
            pass

    url = f"https://api.github.com/{endpoint.lstrip('/')}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "FelixIsaac-Profile-Sync")
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 404 and "releases/latest" in endpoint:
            return None
        print(f"API request failed for {endpoint}: {e}")
        return None
    except Exception as e:
        print(f"API request failed for {endpoint}: {e}")
        return None


def fetch_stats():
    repos_data = github_api_get(f"users/{GITHUB_USER}/repos?per_page=100&type=owner")
    if not repos_data or not isinstance(repos_data, list):
        print("Failed to fetch repositories list.")
        return None

    public_non_fork = [r for r in repos_data if not r.get("fork")]
    total_stars = sum(r.get("stargazers_count", 0) for r in public_non_fork)
    total_forks = sum(r.get("forks_count", 0) for r in public_non_fork)
    active_repos = [r for r in public_non_fork if not r.get("archived")]

    projects_info = []
    for f in FEATURED_REPOS:
        repo_data = github_api_get(f"repos/{f['repo']}")
        if not repo_data:
            continue

        stars = repo_data.get("stargazers_count", 0)
        forks = repo_data.get("forks_count", 0)
        rel_data = github_api_get(f"repos/{f['repo']}/releases/latest")
        release_tag = rel_data.get("tag_name") if rel_data and isinstance(rel_data, dict) else None

        projects_info.append({
            "name": f["name"],
            "url": f"https://github.com/{f['repo']}",
            "lang": f["lang"],
            "stars": stars,
            "forks": forks,
            "release": release_tag,
            "role": f["role"],
        })

    return {
        "total_stars": total_stars,
        "total_forks": total_forks,
        "active_repos": len(active_repos),
        "total_public": len(public_non_fork),
        "projects": projects_info,
    }


def _text_width(text, char_w=6.7):
    return int(round(len(text) * char_w))


def build_metrics_svg(stats, dark=True):
    bg = "#161b22" if dark else "#f6f8fa"
    border = "#30363d" if dark else "#d0d7de"
    label_fg = "#8b949e" if dark else "#57606a"
    val_fg = "#f0f6fc" if dark else "#1f2328"

    pills = [
        ("STARS", str(stats["total_stars"]), "#de6e46"),
        ("FORKS", str(stats["total_forks"]), "#58a6ff"),
        ("ACTIVE OSS", f"{stats['active_repos']} repos", "#3fb950"),
        ("BASE", "Singapore", "#a371f7"),
    ]

    h = 30
    gap = 8
    x = 0
    parts = []
    for label, value, dot in pills:
        lw = _text_width(label, 6.2)
        vw = _text_width(value, 6.9)
        w = 14 + 8 + lw + 10 + vw + 12
        parts.append(
            f'<g transform="translate({x},0)">'
            f'<rect width="{w}" height="{h}" rx="6" fill="{bg}" stroke="{border}" stroke-width="1"/>'
            f'<circle cx="12" cy="{h//2}" r="3.2" fill="{dot}"/>'
            f'<text x="21" y="19" fill="{label_fg}" font-size="10.5" font-weight="600" letter-spacing="0.4">{escape(label)}</text>'
            f'<text x="{21 + lw + 8}" y="19" fill="{val_fg}" font-size="11.5" font-weight="700">{escape(value)}</text>'
            f'</g>'
        )
        x += w + gap

    total_w = max(1, x - gap)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{h}" viewBox="0 0 {total_w} {h}" role="img" aria-label="Live GitHub Metrics">\n'
        f'  <style>text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}</style>\n'
        f'  {"".join(parts)}\n'
        f'</svg>\n'
    )


def build_stack_svg(dark=True):
    bg = "#161b22" if dark else "#f6f8fa"
    border = "#30363d" if dark else "#d0d7de"
    fg = "#e6edf3" if dark else "#1f2328"

    h = 28
    gap_x = 8
    gap_y = 8
    max_w = 720
    x = 0
    y = 0
    parts = []
    used_w = 0

    for label, dot in STACK_ITEMS:
        tw = _text_width(label, 6.8)
        w = 12 + 8 + tw + 12
        if x > 0 and x + w > max_w:
            x = 0
            y += h + gap_y
        parts.append(
            f'<g transform="translate({x},{y})">'
            f'<rect width="{w}" height="{h}" rx="6" fill="{bg}" stroke="{border}" stroke-width="1"/>'
            f'<circle cx="12" cy="{h//2}" r="3.2" fill="{dot}"/>'
            f'<text x="22" y="18" fill="{fg}" font-size="11.5" font-weight="600">{escape(label)}</text>'
            f'</g>'
        )
        x += w + gap_x
        used_w = max(used_w, x - gap_x)

    total_h = y + h
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{used_w}" height="{total_h}" viewBox="0 0 {used_w} {total_h}" role="img" aria-label="Tech Stack">\n'
        f'  <style>text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}</style>\n'
        f'  {"".join(parts)}\n'
        f'</svg>\n'
    )


def render_metrics_markdown():
    return (
        '<picture>\n'
        '  <source media="(prefers-color-scheme: dark)" srcset="./assets/metrics-dark.svg" />\n'
        '  <source media="(prefers-color-scheme: light)" srcset="./assets/metrics-light.svg" />\n'
        '  <img alt="Live GitHub Metrics" src="./assets/metrics-dark.svg" />\n'
        '</picture>'
    )


def render_projects_markdown(projects):
    lines = [
        "| Project | Stack | Stars | What it does |",
        "|:---|:---:|:---:|:---|",
    ]
    for p in projects:
        rel_badge = f"`{p['release']}`" if p["release"] else "`main`"
        star_str = f"⭐ **{p['stars']}**"
        lines.append(
            f"| **[{p['name']}]({p['url']})** | `{p['lang']}`<br>{rel_badge} | {star_str} | {p['role']} |"
        )
    return "\n".join(lines)


def update_readme():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    readme_path = os.path.join(repo_root, "README.md")
    assets_dir = os.path.join(repo_root, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    if not os.path.exists(readme_path):
        print(f"README.md not found at {readme_path}")
        return False

    stats = fetch_stats()
    if not stats or not stats.get("projects"):
        print("Could not collect stats; skipping update to prevent destructive edits.")
        return False

    # Write self-hosted SVGs (never broken by external badge proxy rate limits)
    with open(os.path.join(assets_dir, "metrics-dark.svg"), "w", encoding="utf-8") as f:
        f.write(build_metrics_svg(stats, dark=True))
    with open(os.path.join(assets_dir, "metrics-light.svg"), "w", encoding="utf-8") as f:
        f.write(build_metrics_svg(stats, dark=False))
    with open(os.path.join(assets_dir, "stack-dark.svg"), "w", encoding="utf-8") as f:
        f.write(build_stack_svg(dark=True))
    with open(os.path.join(assets_dir, "stack-light.svg"), "w", encoding="utf-8") as f:
        f.write(build_stack_svg(dark=False))

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    metrics_md = render_metrics_markdown()
    content = re.sub(
        r"<!-- METRICS:START -->.*?<!-- METRICS:END -->",
        f"<!-- METRICS:START -->\n{metrics_md}\n<!-- METRICS:END -->",
        content,
        flags=re.DOTALL,
    )

    projects_md = render_projects_markdown(stats["projects"])
    content = re.sub(
        r"<!-- PROJECTS:START -->.*?<!-- PROJECTS:END -->",
        f"<!-- PROJECTS:START -->\n{projects_md}\n<!-- PROJECTS:END -->",
        content,
        flags=re.DOTALL,
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Successfully updated README.md and self-hosted SVG badges.")
    return True


if __name__ == "__main__":
    update_readme()
