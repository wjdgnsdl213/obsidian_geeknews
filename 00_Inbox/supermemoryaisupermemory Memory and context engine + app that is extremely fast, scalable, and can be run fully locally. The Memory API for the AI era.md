---
title: "supermemoryai/supermemory: Memory and context engine + app that is extremely fast, scalable, and can be run fully locally. The Memory API for the AI era."
source: "https://github.com/supermemoryai/supermemory"
author:
published:
created: 2026-06-11
description: "Memory and context engine + app that is extremely fast, scalable, and can be run fully locally. The Memory API for the AI era. - supermemoryai/supermemory"
tags:
  - "clippings"
---
![Supermemory](https://github.com/supermemoryai/supermemory/raw/main/apps/web/public/logo-fullmark.svg)

**State-of-the-art memory and context engine for AI. And yes - you can use it as a company/personal brain.**

[Docs](https://supermemory.ai/docs) · [Quickstart](https://supermemory.ai/docs/quickstart) · [Self-host](https://supermemory.ai/docs/self-hosting/overview) · [Dashboard](https://console.supermemory.ai/) · [Discord](https://supermemory.link/discord)

**English** · [简体中文](https://github.com/supermemoryai/supermemory/blob/main/README.zh-CN.md)

---

Supermemory is the memory and context layer for AI. **#1 on [LongMemEval](https://github.com/xiaowu0162/LongMemEval), [LoCoMo](https://github.com/snap-research/locomo), and [ConvoMem](https://github.com/Salesforce/ConvoMem)** — the three major benchmarks for AI memory.

We are a research lab building the engine, plugins and tools around it.

Your AI forgets everything between conversations. Supermemory fixes that.

It automatically learns from conversations, extracts facts, builds user profiles, handles knowledge updates and contradictions, forgets expired information, and delivers the right context at the right time. Full RAG, connectors, file processing — the entire context stack, one system.

|  |  |
| --- | --- |
| 🧠 **Memory** | Extracts facts from conversations. Handles temporal changes, contradictions, and automatic forgetting. |
| 👤 **User Profiles** | Auto-maintained user context — stable facts + recent activity. One call, ~50ms. |
| 🔍 **Hybrid Search** | RAG + Memory in a single query. Knowledge base docs and personalized context together. |
| 🔌 **Connectors** | Google Drive · Gmail · Notion · OneDrive · GitHub — auto-sync with real-time webhooks. |
| 📄 **Multi-modal Extractors** | PDFs, images (OCR), videos (transcription), code (AST-aware chunking). Upload and it works. |

All of this is in our single memory structure and ontology.

[![image](https://private-user-images.githubusercontent.com/63950637/556472473-8863b6d9-c043-4c75-b200-4f1759e7edaf.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODExNDE1MDEsIm5iZiI6MTc4MTE0MTIwMSwicGF0aCI6Ii82Mzk1MDYzNy81NTY0NzI0NzMtODg2M2I2ZDktYzA0My00Yzc1LWIyMDAtNGYxNzU5ZTdlZGFmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjExVDAxMjY0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFhMDU2ODgxZjY4ODZlNDBjZGM3MmY5NGQ3Njk5MGRmNTU4NDIzOTM4NTJiMDQ3OGUzMzUxOWJkNGNmYzEyNzQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.B8HP8_P5i9mfBgxUEw6G9uP3RehBqQyaIduwZqd2vI0)](https://private-user-images.githubusercontent.com/63950637/556472473-8863b6d9-c043-4c75-b200-4f1759e7edaf.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODExNDE1MDEsIm5iZiI6MTc4MTE0MTIwMSwicGF0aCI6Ii82Mzk1MDYzNy81NTY0NzI0NzMtODg2M2I2ZDktYzA0My00Yzc1LWIyMDAtNGYxNzU5ZTdlZGFmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjExVDAxMjY0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFhMDU2ODgxZjY4ODZlNDBjZGM3MmY5NGQ3Njk5MGRmNTU4NDIzOTM4NTJiMDQ3OGUzMzUxOWJkNGNmYzEyNzQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.B8HP8_P5i9mfBgxUEw6G9uP3RehBqQyaIduwZqd2vI0)

---

## Use Supermemory

<table><tbody><tr><td width="50%"><h3>🧑💻 I use AI tools</h3><p>Build your own personal supermemory by using our app. Builds <strong>persistent memory graph across every conversation</strong>.</p><p>Your AI remembers your preferences, projects, past discussions — and gets smarter over time.</p><p><strong><a href="#give-your-ai-memory">→ Jump to User setup</a></strong></p></td><td width="50%"><h3>🔧 I'm building AI products</h3><p>Add memory, RAG, user profiles, and connectors to your agents and apps with <strong>a single API</strong>.</p><p>No vector DB config. No embedding pipelines. No chunking strategies.</p><p><strong><a href="#build-with-supermemory-api">→ Jump to developer quickstart</a></strong></p></td></tr><tr><td colspan="2"><h3>🖥️ I want to run it myself</h3><p>State-of-the-art memory, on your machine. <strong>One binary. Zero config.</strong> Bring any model — or run fully offline with Ollama.</p><pre><code>curl -fsSL https://supermemory.ai/install | bash</code></pre><p><strong><a href="#supermemory-local--run-it-yourself">→ Jump to Supermemory local</a></strong></p></td></tr></tbody></table>

---

## Give your AI memory

The Supermemory App, browser extension, plugins and MCP server gives any compatible AI assistant persistent memory. One install, and your AI remembers you.

### The app

You can use supermemory without any code, by using our consumer-facing app for free.

Start at [https://app.supermemory.ai](https://app.supermemory.ai/)It also comes with an agent embedded inside, which we call Nova.

### Supermemory Plugins

Supermemory comes built with Plugins for Claude Code, OpenCode, OpenClaw, and Hermes.These plugins are implementations of the supermemory API, and they are open source!

You can find them here:

- Openclaw plugin: [https://github.com/supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)
- Claude code plugin: [https://github.com/supermemoryai/claude-supermemory](https://github.com/supermemoryai/claude-supermemory)
- OpenCode plugin: [https://github.com/supermemoryai/opencode-supermemory](https://github.com/supermemoryai/opencode-supermemory)
- Hermes agent (Supermemory memory provider): [https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

### MCP - Quick install

```
npx -y install-mcp@latest https://mcp.supermemory.ai/mcp --client claude --oauth=yes
```

Replace `claude` with your client: `cursor`, `windsurf`, `vscode`, etc.

Read more about our MCP here - [https://supermemory.ai/docs/supermemory-mcp/mcp](https://supermemory.ai/docs/supermemory-mcp/mcp)

### What your AI gets

| Tool | What it does |
| --- | --- |
| `memory` | Save or forget information. Your AI calls this automatically when you share something worth remembering. |
| `recall` | Search memories by query. Returns relevant memories + your user profile summary. |
| `context` | Injects your full profile (preferences, recent activity) into the conversation at start. In Cursor and Claude Code, just type `/context`. |

### How it works

Once installed, Supermemory runs in the background:

1. **You talk to your AI normally.** Share preferences, mention projects, discuss problems.
2. **Supermemory extracts and stores the important stuff.** Facts, preferences, project context — not noise.
3. **Next conversation, your AI already knows you.** It recalls what you're working on, how you like things, what you discussed before.

Memory is scoped with **projects** (container tags) so you can separate work and personal context, or organize by client, repo, or anything else.

### Supported clients

**Claude Desktop** · **Cursor** · **Windsurf** · **VS Code** · **Claude Code** · **OpenCode** · **OpenClaw** · **Hermes**

The MCP server is open source — [view the source](https://supermemory.ai/docs/supermemory-mcp/mcp).

### Manual configuration

Add this to your MCP client config:

```
{
  "mcpServers": {
    "supermemory": {
      "url": "https://mcp.supermemory.ai/mcp"
    }
  }
}
```

Or use an API key instead of OAuth:

```
{
  "mcpServers": {
    "supermemory": {
      "url": "https://mcp.supermemory.ai/mcp",
      "headers": {
        "Authorization": "Bearer sm_your_api_key_here"
      }
    }
  }
}
```

---

## Build with Supermemory (API)

If you're building AI agents or apps, Supermemory gives you the entire context stack through one API — memory, RAG, user profiles, connectors, and file processing.

### Install

```
npm install supermemory    # or: pip install supermemory
```

### Quickstart

```
import Supermemory from "supermemory";

const client = new Supermemory();

// Store a conversation
await client.add({
  content: "User loves TypeScript and prefers functional patterns",
  containerTag: "user_123",
});

// Get user profile + relevant memories in one call
const { profile, searchResults } = await client.profile({
  containerTag: "user_123",
  q: "What programming style does the user prefer?",
});

// profile.static  → ["Loves TypeScript", "Prefers functional patterns"]
// profile.dynamic → ["Working on API integration"]
// searchResults   → Relevant memories ranked by similarity
```
```
from supermemory import Supermemory

client = Supermemory()

client.add(
    content="User loves TypeScript and prefers functional patterns",
    container_tag="user_123"
)

result = client.profile(container_tag="user_123", q="programming style")

print(result.profile.static)   # Long-term facts
print(result.profile.dynamic)  # Recent context
```

Supermemory automatically extracts memories, builds user profiles, and returns relevant context. No embedding pipelines, no vector DB config, no chunking strategies.

### Framework integrations

Drop-in wrappers for every major AI framework:

```
// Vercel AI SDK
import { withSupermemory } from "@supermemory/tools/ai-sdk";
const model = withSupermemory(openai("gpt-4o"), { containerTag: "user_123", customId: "conv-1" });

// Mastra
import { withSupermemory } from "@supermemory/tools/mastra";
const agent = new Agent(withSupermemory(config, "user-123", { mode: "full" }));
```

**Vercel AI SDK** · **LangChain** · **LangGraph** · **OpenAI Agents SDK** · **Mastra** · **Agno** · **Claude Memory Tool** · **n8n**

### Search modes

```
// Hybrid (default) — RAG + Memory in one query
const results = await client.search.memories({
  q: "how do I deploy?",
  containerTag: "user_123",
  searchMode: "hybrid",
});
// Returns deployment docs (RAG) + user's deploy preferences (Memory)

// Memories only
const results = await client.search.memories({
  q: "user preferences",
  containerTag: "user_123",
  searchMode: "memories",
});
```

### User profiles

Traditional memory relies on search — you need to know what to ask for. Supermemory automatically maintains a profile for every user:

```
const { profile } = await client.profile({ containerTag: "user_123" });

// profile.static  → ["Senior engineer at Acme", "Prefers dark mode", "Uses Vim"]
// profile.dynamic → ["Working on auth migration", "Debugging rate limits"]
```

One call. ~50ms. Inject into your system prompt and your agent instantly knows who it's talking to.

### Connectors

Auto-sync external data into your knowledge base:

**Google Drive** · **Gmail** · **Notion** · **OneDrive** · **GitHub** · **Web Crawler**

Real-time webhooks. Documents automatically processed, chunked, and searchable.

### API at a glance

| Method | Purpose |
| --- | --- |
| `client.add()` | Store content — text, conversations, URLs, HTML |
| `client.profile()` | User profile + optional search in one call |
| `client.search.memories()` | Hybrid search across memories and documents |
| `client.search.documents()` | Document search with metadata filters |
| `client.documents.uploadFile()` | Upload PDFs, images, videos, code |
| `client.documents.list()` | List and filter documents |
| `client.settings.update()` | Configure memory extraction and chunking |

Full API reference → [supermemory.ai/docs](https://supermemory.ai/docs)

---

## Supermemory local — run it yourself

State-of-the-art memory, on your machine. One binary. Zero config.

```
curl -fsSL https://supermemory.ai/install | bash
# or
npx supermemory local
```
```
supermemory-server
```

First boot sets up the embedded Supermemory graph engine, local embeddings, and your credentials, then prints an API key. The full Memory API — documents, memories, user profiles, hybrid search — runs against `http://localhost:6767`.

```
const client = new Supermemory({
  apiKey: "sm_...",
  baseURL: "http://localhost:6767", // that's the only change
});
```
- **Bring any model** — OpenAI, Anthropic, Gemini, Groq, or any OpenAI-compatible endpoint. An interactive wizard walks you through it on first boot.
- **Fully offline if you want** — point it at Ollama (`gpt-oss:20b` works great) and nothing leaves your machine.
- **Your data, one directory** — everything lives in `./.supermemory`, easy to back up or move.
- **Same API as the platform** — prototype locally, ship on the hosted platform by changing `baseURL`.

Read the [self-hosting docs](https://supermemory.ai/docs/self-hosting/overview) — quickstart, configuration, and [local vs. Enterprise](https://supermemory.ai/docs/self-hosting/local-vs-enterprise).

---

## Benchmarks

Supermemory is state of the art across all major AI memory benchmarks:

| Benchmark | What it measures | Result |
| --- | --- | --- |
| **[LongMemEval](https://github.com/xiaowu0162/LongMemEval)** | Long-term memory across sessions with knowledge updates | **81.6% — #1** |
| **[LoCoMo](https://github.com/snap-research/locomo)** | Fact recall across extended conversations (single-hop, multi-hop, temporal, adversarial) | **#1** |
| **[ConvoMem](https://github.com/Salesforce/ConvoMem)** | Personalization and preference learning | **#1** |

We also built **[MemoryBench](https://supermemory.ai/docs/memorybench/overview)** — an open-source framework for standardized, reproducible benchmarks of memory providers. Compare Supermemory, Mem0, Zep, and others head-to-head:

```
bun run src/index.ts run -p supermemory -b longmemeval -j gpt-4o -r my-run
```

### Benchmarking your own memory solution

We provide an Agent skill for companies to benchmark their own context and memory solutions against supermemory.

```
npx skills add supermemoryai/memorybench
```

Simply run this and do `/benchmark-context` - Supermemory will automatically do the work for you!

---

## How memory works under the hood

```
Your app / AI tool
        ↓
   Supermemory
        │
        ├── Memory Engine     Extracts facts, tracks updates, resolves contradictions,
        │                     auto-forgets expired info
        ├── User Profiles     Static facts + dynamic context built from engine, always fresh
        ├── Hybrid Search     RAG + Memory in one query
        ├── Connectors        Real-time sync from Google Drive, Gmail, Notion, GitHub...
        └── File Processing   PDFs, images, videos, code → searchable chunks
```

**Memory is not RAG.** RAG retrieves document chunks — stateless, same results for everyone. Memory extracts and tracks *facts about users* over time. It understands that "I just moved to SF" supersedes "I live in NYC." Supermemory runs both together by default, so you get knowledge base retrieval *and* personalized context in every query. Read more about this here - [https://supermemory.ai/docs/concepts/memory-vs-rag](https://supermemory.ai/docs/concepts/memory-vs-rag)

**Automatic forgetting.** Supermemory knows when memories become irrelevant. Temporary facts ("I have an exam tomorrow") expire after the date passes. Contradictions are resolved automatically. Noise never becomes permanent memory.

---

## Links

- 📖 [Documentation](https://supermemory.ai/docs)
- 🚀 [Quickstart](https://supermemory.ai/docs/quickstart)
- 🖥️ [Self-hosting (Supermemory local)](https://supermemory.ai/docs/self-hosting/overview)
- 🧪 [MemoryBench](https://supermemory.ai/docs/memorybench/overview)
- 🔌 [Integrations](https://supermemory.ai/docs/integrations)
- 💬 [Discord](https://supermemory.link/discord)
- 𝕏 [Twitter](https://twitter.com/supermemory)

---

**Give your AI a memory. It's about time..**