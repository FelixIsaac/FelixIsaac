#!/usr/bin/env python3
"""
Syncs live metrics and featured project metadata into README.md.
Can run locally or in GitHub Actions via cron.
"""

import os
import re
import json
import urllib.request
import urllib.error
import subprocess

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
        "repo": "FelixIsaac/youngasians.org",
        "name": "youngasians.org",
        "lang": "Next.js",
        "role": "**Young Asians Official Platform** — Web application empowering the next generation of Asian youth leaders. Built with Next.js App Router, TypeScript, and modern static optimization.",
    },
]

def github_api_get(endpoint):
    token = os.environ.get("GITHUB_TOKEN")
    # If no env token but gh is available locally, use gh auth token
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
    # 1. Fetch user repos (up to 100)
    repos_data = github_api_get(f"users/{GITHUB_USER}/repos?per_page=100&type=owner")
    if not repos_data or not isinstance(repos_data, list):
        print("Failed to fetch repositories list.")
        return None

    public_non_fork = [r for r in repos_data if not r.get("fork")]
    total_stars = sum(r.get("stargazers_count", 0) for r in public_non_fork)
    total_forks = sum(r.get("forks_count", 0) for r in public_non_fork)
    active_repos = [r for r in public_non_fork if not r.get("archived")]

    # 2. Fetch repo details for featured projects
    projects_info = []
    for f in FEATURED_REPOS:
        repo_data = github_api_get(f"repos/{f['repo']}")
        if not repo_data:
            continue

        stars = repo_data.get("stargazers_count", 0)
        forks = repo_data.get("forks_count", 0)

        # Fetch latest release
        rel_data = github_api_get(f"repos/{f['repo']}/releases/latest")
        release_tag = rel_data.get("tag_name") if rel_data and isinstance(rel_data, dict) else None

        projects_info.append({
            "name": f["name"],
            "url": f"https://github.com/{f['repo']}",
            "lang": f["lang"],
            "stars": stars,
            "forks": forks,
            "release": release_tag,
            "role": f["role"]
        })

    return {
        "total_stars": total_stars,
        "total_forks": total_forks,
        "active_repos": len(active_repos),
        "total_public": len(public_non_fork),
        "projects": projects_info
    }

def render_metrics_markdown(stats):
    return (
        f"> ⚡ **Live Metrics:** **{stats['total_stars']}** GitHub Stars · "
        f"**{stats['total_forks']}** Forks · "
        f"**{stats['active_repos']}** Active Open-Source Projects"
    )

def render_projects_markdown(projects):
    lines = [
        "| Project | Lang & Release | Stars | Description |",
        "|:---|:---:|:---:|:---|"
    ]
    for p in projects:
        rel_badge = f"`{p['release']}`" if p['release'] else "—"
        star_str = f"⭐ **{p['stars']}**"
        lines.append(
            f"| **[{p['name']}]({p['url']})** | `{p['lang']}`<br>{rel_badge} | {star_str} | {p['role']} |"
        )
    return "\n".join(lines)

def update_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
    readme_path = os.path.abspath(readme_path)

    if not os.path.exists(readme_path):
        print(f"README.md not found at {readme_path}")
        return False

    stats = fetch_stats()
    if not stats or not stats.get("projects"):
        print("Could not collect stats; skipping update to prevent destructive edits.")
        return False

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace METRICS section
    metrics_md = render_metrics_markdown(stats)
    content = re.sub(
        r"<!-- METRICS:START -->.*?<!-- METRICS:END -->",
        f"<!-- METRICS:START -->\n{metrics_md}\n<!-- METRICS:END -->",
        content,
        flags=re.DOTALL
    )

    # Replace PROJECTS section
    projects_md = render_projects_markdown(stats["projects"])
    content = re.sub(
        r"<!-- PROJECTS:START -->.*?<!-- PROJECTS:END -->",
        f"<!-- PROJECTS:START -->\n{projects_md}\n<!-- PROJECTS:END -->",
        content,
        flags=re.DOTALL
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Successfully updated README.md with live metrics.")
    return True

if __name__ == "__main__":
    update_readme()
