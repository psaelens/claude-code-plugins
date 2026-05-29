# demo plugin

A tech jargon explainer that demonstrates all three main Claude Code plugin
component types in one cohesive story.

## What's Inside

| Component | Type | Purpose |
|-----------|------|---------|
| `demo` skill | Skill | Techniques for explaining tech concepts in plain language (analogy-first, problem-before-solution, jargon-free). Auto-loads when the user asks to simplify a tech term. |
| `demo` agent | Agent | A clarity judge that scores your explanation against the Wikipedia original on four dimensions. Triggers when the user asks for a review. |
| `demo` MCP server | MCP | Calls the real Wikipedia REST API to fetch jargon-heavy definitions. Also picks random tech terms. No API key needed. |

## Prerequisites

- Python 3.10+

```bash
cd plugins/demo
export CLAUDE_PLUGIN_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Installation

```bash
claude --plugin-dir /path/to/plugins/demo
```

## Live Demo Script (AI Meetup)

**Act 1 — Skill** *(automatic knowledge loading)*
> "Explain microservices to someone who has never worked in IT."

Claude loads the demo skill and applies the analogy-first technique.

**Act 2 — MCP** *(live external API call)*
> "First fetch the Wikipedia definition so we can compare."

Claude calls `fetch_wikipedia_intro("microservices")` — a real HTTP request to
Wikipedia's REST API, visible live.

**Act 3 — Agent** *(autonomous sub-agent)*
> "Have the demo agent score my explanation against the Wikipedia version."

The clarity judge launches, scores both versions on four dimensions, and
delivers a verdict.

The contrast — Wikipedia's dense paragraph vs. a one-sentence analogy — is
the "aha moment" for the audience.

## MCP Server Tools

| Tool | Description |
|------|-------------|
| `get_random_tech_term` | Returns a random term from a curated list |
| `fetch_wikipedia_intro` | Calls Wikipedia REST API and returns the real summary |
