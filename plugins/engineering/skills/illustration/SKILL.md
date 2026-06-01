---
name: illustration
version: 0.1.0
description: This skill should be used when the user asks to "generate an illustration", "create an icon", "make a diagram", or "illustrate" something for documentation or tooling. Note: this skill is a work in progress and not yet implemented. Usage: /engineering:illustration [subject] [--style <default|custom>]
argument-hint: "[subject] [--style <default|custom>]"
disable-model-invocation: true
---

> **Work in progress** — this skill is a placeholder. Implementation is planned.

## Planned capabilities

- Generate illustrations and icons for documentation, README files, and tooling integrations
- Maintain visual coherence across a project using a configurable visual system
- Ship a default visual system (color palette, icon style, illustration style)
- Support defining a custom visual system via plugin settings
- Integrate with image generation APIs (Replicate, nanobana, or similar)

## Planned workflow

1. Receive subject/description from `$ARGUMENTS`
2. Load the active visual system (default or custom from plugin settings)
3. Build a prompt aligned with the visual system constraints
4. Call the image generation API
5. Save the output and report the file path

## Visual system (planned)

A visual system defines:
- Color palette (primary, secondary, accent, background)
- Icon style (flat, outlined, filled, isometric, etc.)
- Illustration style (minimal, technical, playful, etc.)
- Typography hints (for text-bearing illustrations)

The default visual system will be bundled with the plugin. Custom visual systems will be configurable via `.claude/engineering.local.md`.

## API integrations (planned)

- Replicate (model TBD)
- nanobana or equivalent
- Configurable via plugin settings (API key, model, endpoint)
