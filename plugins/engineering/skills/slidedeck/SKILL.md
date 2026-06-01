---
name: slidedeck
version: 0.1.0
description: This skill should be used when the user asks to "create a slide deck", "generate a RevealJS presentation", or "make slides". Note: this skill is a work in progress and not yet implemented. Usage: /engineering:slidedeck [topic] [--theme <perso|5th-floor|spw>]
argument-hint: "[topic] [--theme <perso|5th-floor|spw>]"
disable-model-invocation: true
---

> **Work in progress** — this skill is a placeholder. Implementation is planned.

## Planned capabilities

- Generate a RevealJS slide deck from a topic, outline, or document
- Select an audience-specific theme: `perso`, `5th-floor`, `spw`, or custom
- Each theme ships with its own color palette, fonts, and logo placement
- Support configuring a custom visual system via plugin settings

## Planned workflow

1. Receive topic or outline from `$ARGUMENTS`
2. Detect target audience / theme (default: `perso`)
3. Structure content into slides following presentation best practices
4. Generate `slides.html` (or `index.html`) with embedded RevealJS and the selected theme
5. Open or print instructions

## Theme registry (planned)

| Theme | Audience | Notes |
|-------|----------|-------|
| `perso` | Personal / community talks | Neutral, minimal |
| `5th-floor` | Internal eng team | Team branding |
| `spw` | SPW / institutional | Institutional branding |
