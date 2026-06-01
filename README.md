# Claude Code Plugins

A personal collection of plugins for [Claude Code](https://github.com/anthropics/claude-code) — skills, agents, and MCP servers that extend the CLI for real developer workflows.

## Prerequisites

- Claude Code CLI installed and authenticated
- Python 3.10+ (required by the `demo` plugin)

## Plugins

| Plugin | Description |
|--------|-------------|
| [`demo`](plugins/demo) | Tech jargon explainer showcasing all three plugin component types: skill, agent, and MCP server |
| [`engineering`](plugins/engineering) | Writing and documentation toolkit for developers and technical writers |

### demo

| Component | Type | What it does |
|-----------|------|--------------|
| `jargon-explainer` | Skill | Explains tech concepts using analogy-first, jargon-free techniques |
| `Clarity Judge` | Agent | Scores plain-language explanations against a Wikipedia original |
| `demo_server` | MCP | Fetches real Wikipedia summaries and picks random tech terms via the Wikipedia REST API |

### engineering

| Skill | Command | What it does |
|-------|---------|--------------|
| `deslopify` | `/engineering:deslopify` | Rewrites AI-generated text to sound human — removes LLM tropes in English and French |
| `diataxis` | `/engineering:diataxis` | Writes or reviews documentation following the Diataxis methodology (tutorial / guide / reference / explanation) |
| `readmeify` | `/engineering:readmeify` | Generates or improves a `README.md` by analyzing the project structure |
| `illustration` | `/engineering:illustration` | *(work in progress)* Generates illustrations for documentation |
| `slidedeck` | `/engineering:slidedeck` | *(work in progress)* Generates a RevealJS slide deck |

## Installation

Load a plugin by passing its directory to Claude Code at startup:

```bash
claude --plugin-dir /path/to/claude-code-plugins/plugins/engineering
```

To load multiple plugins at once:

```bash
claude --plugin-dir /path/to/plugins/demo --plugin-dir /path/to/plugins/engineering
```

The `demo` plugin requires a Python virtual environment:

```bash
cd plugins/demo
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Architecture

```
plugins/
├── demo/                        # Demo plugin
│   ├── .claude-plugin/
│   │   └── plugin.json          # Plugin manifest (name, version, description)
│   ├── agents/
│   │   └── Clarity Judge.md     # Agent definition
│   ├── servers/
│   │   └── demo_server.py       # MCP server (Wikipedia REST API)
│   └── skills/
│       └── jargon-explainer/
│           └── SKILL.md         # Skill definition and instructions
│
└── engineering/                 # Engineering toolkit plugin
    ├── .claude-plugin/
    │   └── plugin.json
    └── skills/
        ├── deslopify/
        ├── diataxis/
        ├── illustration/
        ├── readmeify/
        └── slidedeck/
```

Each plugin is self-contained under its own directory. The `.claude-plugin/plugin.json` manifest is what Claude Code uses to discover and load the plugin. Skills are Markdown files (`SKILL.md`) with a YAML frontmatter block that defines the trigger conditions and metadata.

---

> Personal project, not affiliated with Anthropic.
