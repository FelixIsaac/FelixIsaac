# Felix Isaac Lim

**Systems & Agent Infrastructure Engineer** · Singapore 🇸🇬  
*Building lean transport primitives for humans and autonomous AI agents.*

[Website](https://felixisaac.dev) · [Email](mailto:me@felixisaac.dev) · [Repositories](https://github.com/FelixIsaac?tab=repositories) · [Gists](https://gist.github.com/FelixIsaac)

<!-- METRICS:START -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/metrics-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./assets/metrics-light.svg" />
  <img alt="Live GitHub Metrics" src="./assets/metrics-dark.svg" />
</picture>
<!-- METRICS:END -->

```bash
$ felix --status
role:       Systems & Agent Infrastructure Engineer (Singapore)
thesis:     Unix composability over monoliths — small sharp tools that humans & agents can both drive
origin:     "Most of what I make starts as a personal annoyance I wanted gone."
side_note:  Will happily detour from Rust telemetry into Camus, foldable iPhone games, or maths rabbit holes.
```

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/FelixIsaac/FelixIsaac/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/FelixIsaac/FelixIsaac/output/github-contribution-grid-snake.svg" />
  <img alt="GitHub contribution snake" src="https://raw.githubusercontent.com/FelixIsaac/FelixIsaac/output/github-contribution-grid-snake.svg" />
</picture>

---

## 🛠️ Flagship Agent Infrastructure

<!-- PROJECTS:START -->
| Project | Stack | Stars | What it does |
|:---|:---:|:---:|:---|
| **[whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended)** | `Go`<br>`v0.4.0` | ⭐ **45** | **Production WhatsApp MCP Server** — 26 curated transport tools, webhooks, anti-ban rate limiting, self-healing watchdog, and JID safety allowlists. Built for Claude Code, Cursor, OpenCode, and Codex. |
| **[tokenusage](https://github.com/FelixIsaac/tokenusage)** | `Rust`<br>`v1.14.0` | ⭐ **3** | **Blazing-Fast AI Telemetry** — Cost & quota tracking across 10 providers (Claude Code, Codex, Antigravity, Gemini, Grok, DeepSeek). Includes TUI dashboard, SQLite WAL cache, & 1-line zero-dep installers. |
| **[tandem](https://github.com/FelixIsaac/tandem)** | `TypeScript`<br>`v1.0.4` | ⭐ **3** | **Real-Session Browser MCP** — Enables AI agents to drive authenticated Chrome browser sessions cleanly without headless detection blocks. Published on npm as `@felixisaac/tandem`. |
| **[claude-code-sync](https://github.com/FelixIsaac/claude-code-sync)** | `Go`<br>`v0.2.7` | ⭐ **8** | **Age-Encrypted Agent Config Sync** — Securely syncs Claude Code environments, prompts, and settings across machines via GitHub with cryptographic age encryption. |
| **[cmux-orbit](https://github.com/FelixIsaac/cmux-orbit)** | `TypeScript`<br>`v1.0.0` | ⭐ **0** | **Agent-First Mobile Mission Control** — Drive Claude Code, Grok CLI, Codex, Pi, and Antigravity sessions from your phone over Tailscale with live thinking & token streaming. |
<!-- PROJECTS:END -->

---

## 🧭 Side Quests & Oddities

Not everything has to be an MCP server. A few things built out of curiosity, hackathons, or sheer stubbornness:

| Experiment | Stack | What it is |
|:---|:---:|:---|
| **[sisyphus-reader](https://github.com/FelixIsaac/sisyphus-reader)** | `HTML` · [Live](https://sisyphus-reader.pages.dev) | Critical reading companion & modern literary translation of Albert Camus's *The Myth of Sisyphus*. |
| **[shelflife](https://github.com/FelixIsaac/shelflife)** | `Python` | Freshness & provenance verifier for civic directories — catches broken contacts and abstains when uncertain (*Hack for Humanity SF 2026*). |
| **[pop-up-post](https://github.com/FelixIsaac/pop-up-post)** | `Swift` | Endless runner inside a pop-up book — fold the phone to flatten paper walls, open it to raise bridges (*Bitrig Hacks: iPhone Duo*). |
| **[p3-fractions](https://github.com/FelixIsaac/p3-fractions)** | `TypeScript` · [Live](https://p3-fractions.felixisaac.dev) | Interactive Primary 3 fractions practice app for primary-school maths. |

---

## ⚡ 1-Line Installs

```bash
# tokenusage — Rust AI token & cost tracker (10 providers, TUI + CLI)
brew install FelixIsaac/tokenusage/tokenusage

# Standalone zero-dependency binary (macOS / Linux)
curl --proto '=https' --tlsv1.2 -sSf https://github.com/FelixIsaac/tokenusage/releases/latest/download/tokenusage-installer.sh | sh

# tandem — Real-session Chrome Browser MCP for AI agents
npx @felixisaac/tandem
```

---

## 🧠 How I Build

- **Agent-Native Contracts:** Primary repos ship explicit [`AGENTS.md`](https://github.com/FelixIsaac/whatsapp-mcp-extended/blob/main/AGENTS.md) and [`ARCHITECTURE.md`](https://github.com/FelixIsaac/whatsapp-mcp-extended/blob/main/ARCHITECTURE.md) specs defining invariants, safety gates, and deterministic tests.
- **Lean Transport Primitives:** Heavy ML work (transcription, vector search) stays decoupled in modular sidecars instead of bloating core transport servers.
- **Zero-Overhead Portability:** Predominantly **Rust** and **Go** for single-binary deploys, <10ms cold starts, and predictable memory.
- **Automated Downstream Sync:** Community forks are monitored via CI so upstream fixes never drift away.

---

## 🧰 Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/stack-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./assets/stack-light.svg" />
  <img alt="Tech Stack" src="./assets/stack-dark.svg" />
</picture>

---

## 💬 Beyond the Terminal

- **Currently obsessed with:** Local LLM inference on Apple Silicon, Rust async pipelines, and multi-agent coordination.
- **Off-screen:** Science & maths rabbit holes, mechanical keyboards, Star Trek, and cats 🐈.

---

<div align="center">
  <sub>
    <a href="https://felixisaac.dev">felixisaac.dev</a> ·
    <a href="mailto:me@felixisaac.dev">me@felixisaac.dev</a> ·
    <a href="https://github.com/FelixIsaac?tab=repositories">Repositories</a> ·
    <a href="https://gist.github.com/FelixIsaac">Gists</a>
    <br />
    <i>Self-hosted SVG badges & contribution snake auto-refresh via GitHub Actions.</i>
  </sub>
</div>
