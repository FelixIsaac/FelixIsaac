# Felix Isaac Lim

<div align="left">

**Systems & Agent Infrastructure Engineer** · Singapore 🇸🇬  
*Building lean transport primitives for humans and autonomous AI agents.*

[Website](https://felixisaac.dev) · [Email](mailto:me@felixisaac.dev) · [Projects](https://github.com/FelixIsaac?tab=repositories) · [Gists](https://gist.github.com/FelixIsaac)

</div>

<!-- METRICS:START -->
> ⚡ **Live Metrics:** **57** GitHub Stars · **32** Forks · **10** Active Open-Source Projects
<!-- METRICS:END -->

```bash
$ felix status
Focus:      Agent infrastructure, high-performance transports, & autonomous tooling
Philosophy: Unix composability over monoliths — build lean primitives agents can orchestrate
Motto:      "Most of what I make starts as a personal annoyance I wanted gone."
```

---

## 🛠️ Flagship Systems & Open-Source

<!-- PROJECTS:START -->
| Project | Lang & Release | Stars | Description |
|:---|:---:|:---:|:---|
| **[whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended)** | `Go`<br>`v0.4.0` | ⭐ **42** | **Production WhatsApp MCP Server** — 26 curated transport tools, webhooks, anti-ban rate limiting, self-healing watchdog, and JID safety allowlists. Built for Claude Code, Cursor, OpenCode, and Codex. |
| **[tokenusage](https://github.com/FelixIsaac/tokenusage)** | `Rust`<br>`v1.11.8` | ⭐ **2** | **Blazing-Fast AI Telemetry** — Cost & quota tracking across 10 providers (Claude Code, Codex, Antigravity, Gemini, Grok, DeepSeek). Includes TUI dashboard, SQLite WAL cache, & 1-line zero-dep installers. |
| **[tandem](https://github.com/FelixIsaac/tandem)** | `TypeScript`<br>`v1.0.4` | ⭐ **3** | **Real-Session Browser MCP** — Enables AI agents to drive authenticated Chrome browser sessions cleanly without headless detection blocks. Published on npm as `@felixisaac/tandem`. |
| **[claude-code-sync](https://github.com/FelixIsaac/claude-code-sync)** | `Go`<br>`v0.2.7` | ⭐ **8** | **Age-Encrypted Agent Config Sync** — Securely syncs Claude Code environments, prompts, and settings across machines via GitHub with cryptographic age encryption. |
| **[cmux-orbit](https://github.com/FelixIsaac/cmux-orbit)** | `TypeScript`<br>`v1.0.0` | ⭐ **0** | **Agent-First Mobile Mission Control** — Run Claude Code, Grok CLI, Codex, and Antigravity sessions directly from your phone over secure Tailscale mesh networking. |
<!-- PROJECTS:END -->

---

## ⚡ Quick 1-Line Installs

```bash
# Install tokenusage (Rust AI token tracker) via Homebrew
brew install FelixIsaac/tokenusage/tokenusage

# Or install standalone binary (macOS / Linux)
curl --proto '=https' --tlsv1.2 -sSf https://github.com/FelixIsaac/tokenusage/releases/latest/download/tokenusage-installer.sh | sh

# Launch Browser MCP server for autonomous agents
npx @felixisaac/tandem
```

---

## 🧠 Engineering & Systems Philosophy

I design software built to be reliably consumed by both humans and autonomous agents:

- 🤖 **Agent-Native Contracts:** Primary repos feature explicit [`AGENTS.md`](https://github.com/FelixIsaac/whatsapp-mcp-extended/blob/main/AGENTS.md) and [`ARCHITECTURE.md`](https://github.com/FelixIsaac/whatsapp-mcp-extended/blob/main/ARCHITECTURE.md) files defining invariants, safety gates, and deterministic test targets.
- 🧱 **Lean Transport Primitives:** Heavy ML tasks (transcription, vector search) are decoupled into modular sidecars rather than bloating core transport servers.
- ⚡ **Zero-Overhead Reliability:** Written predominantly in **Rust** and **Go** for single-binary portability, instant cold-starts (<10ms), and predictable memory usage.
- 📡 **Automated Downstream Sync:** Satellite forks across community ecosystems are continuously monitored via automated CI workflows to pull community fixes upstream.

---

## 🧰 Technical Foundations

* **Languages:** Rust · Go · TypeScript · Python · SQL
* **Architectures:** Model Context Protocol (MCP) · SSE / stdio transports · REST & Webhooks · WebSockets
* **Ecosystems:** Next.js / React · SQLite (WAL mode) · Docker · Linux / macOS Systems Programming

---

## 💬 Beyond the Terminal

* **Currently exploring:** Local LLM inference, Rust async pipelines, and multi-agent consensus protocols.
* **Off-screen:** Science and maths rabbit holes, mechanical keyboards, Star Trek, and cats 🐈.

📫 **[me@felixisaac.dev](mailto:me@felixisaac.dev)** · 🌐 **[felixisaac.dev](https://felixisaac.dev)**

---

<div align="center">
  <sub><i>Automatically refreshed via GitHub Actions · Building lean primitives and shipping software that compounds.</i></sub>
</div>
