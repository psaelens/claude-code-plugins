---
name: illustrate
description: Generate brand-consistent illustrations, hero images, logos, icons, banners, and any visual asset by reading the project's visual system (colors, style, mood, composition rules) and applying it via nano-banana-pro. Use whenever the user asks to generate, create, or design any image — especially when they mention "consistent", "on-brand", "matching the style", or are asking for project assets. Also triggers on "illustrate this", "make an image of", "design a banner", "create a visual", "generate an illustration", "hero image", "OG image", or any request where the output should look like it belongs to the project. Even when the user's phrasing is vague, prefer this skill over calling nano-banana-pro directly — the visual system context is almost always worth it.
---

# Illustrate

Generate coherent, brand-consistent images by combining a project's visual system with nano-banana-pro's image generation.

## Core idea

The visual system is a markdown file that describes the project's brand: colors, typography, illustration style, mood, and composition rules. This skill reads it and translates both the visual system and the user's request into a rich, detailed prompt for nano-banana-pro — so every generated image feels like it belongs to the same visual family.

---

## Step 1: Find the visual system

Search for the visual system file in this order:

1. A path the user explicitly provides (e.g., "use `brand/visual-system.md`")
2. `visual-system.md` in the project root
3. `docs/visual-system.md`
4. `brand/visual-system.md`
5. `.claude/visual-system.md`

**If no file is found**: offer to bootstrap one. Copy the template from `references/visual-system-template.md` to `visual-system.md` in the project root, then help the user fill it in — pull what you can from the existing project (CSS variables, Tailwind config, existing images, README). Proceed once the file has at least a color palette and illustration style.

---

## Step 2: Parse the visual system

Read the file and extract the key brand attributes. The template is a starting point; users may customize it freely — look for intent, not strict schema. Key things to identify:

- **Colors**: Hex codes and their roles (primary, secondary, accent, background, text, neutrals)
- **Illustration style**: The visual language (flat, isometric, photorealistic, watercolor, line art, 3D render, glassmorphism, retro…)
- **Mood / atmosphere**: Emotional tone (warm, minimal, bold, playful, professional, futuristic…)
- **Composition**: Layout preferences (centered, rule-of-thirds, generous whitespace, full-bleed, text overlay zones…)
- **Typography feel**: Even when text won't appear in the image, font personality shapes style (geometric sans → modern/clean; serif → traditional/refined; display → expressive)
- **Dos and don'ts**: Explicit constraints to honor or avoid (e.g., "no gradients", "avoid human faces", "max 3 colors per image")

---

## Step 3: Build the generation prompt

Synthesize the user's request with the extracted brand attributes into a single detailed prompt. Structure it in this order:

1. **Subject** — what the image should show (from the user's request)
2. **Style** — illustration technique and rendering approach (from visual system)
3. **Palette** — colors specified by hex code or precise descriptive name (from visual system)
4. **Mood & lighting** — atmosphere, lighting quality, emotional tone (from visual system + request context)
5. **Composition** — framing, focal point, negative space, text zones (from visual system + output slot)
6. **Negative constraints** — explicit "avoid" rules from the don'ts section

**Example synthesis:**

User asks: *"A hero image for our SaaS homepage"*

Visual system says: flat vector, primary `#2D5BE3` (vivid blue), accent `#F5A623` (amber), white background, professional + trustworthy mood, generous whitespace, no gradients, no human faces

Synthesized prompt:
```
Flat vector illustration of a team collaborating around a glowing dashboard, clean white (#FFFFFF)
background. Vivid blue (#2D5BE3) dominant with warm amber (#F5A623) accents. Solid fills, no
gradients, no drop shadows, no human faces. Professional and trustworthy mood. Soft neutral
lighting, no dramatic contrast. Left third reserved for headline text overlay. Generous whitespace.
```

**Rules when writing the prompt:**
- Always specify hex codes explicitly — "the brand blue" means nothing to the model
- Include all don'ts from the visual system as explicit negation (e.g., "no gradients", "avoid photorealism")
- If the user's request conflicts with a visual system constraint, flag the conflict and ask which to prioritize before generating
- For logos or icon-style outputs, add: `"vector-clean, crisp edges, works on both light and dark backgrounds"`
- For abstract / human-free brand styles, replace people with shapes, objects, or environments that carry the same meaning

---

## Step 4: Invoke nano-banana-pro

Call the generation script directly:

```bash
python3 ~/.claude/skills/nano-banana-pro/generate_image.py \
  "<synthesized prompt>" \
  -o <output-path> \
  --aspect-ratio <ratio> \
  --size 2K
```

**Aspect ratio by output slot:**

| Slot | Ratio |
|------|-------|
| Hero / wide banner | `16:9` |
| OG / social card | `16:9` or `1:1` |
| Logo / icon / avatar | `1:1` |
| Mobile splash / story | `9:16` |
| Blog header | `3:2` |
| Ultra-wide cinematic | `21:9` |

**Output path**: if the user doesn't specify one, save to the project's static asset folder (`public/`, `static/`, `assets/`, `src/assets/`). Use a descriptive filename that reflects the content (e.g., `hero-main.png`, `og-default.png`, `icon-app.png`, `blog-header-intro.png`).

To compose or restyle an existing image, pass it as input:

```bash
python3 ~/.claude/skills/nano-banana-pro/generate_image.py \
  "<prompt>" \
  -o <output-path> \
  --aspect-ratio <ratio> \
  --input <existing-image-path>
```

---


## Prerequisites

The nano-banana-pro skill must be installed and configured:
- `GEMINI_API_KEY` env var set (get one at https://aistudio.google.com/apikey), **or**
- Vertex AI: `GOOGLE_GENAI_USE_VERTEXAI=true`, `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION` set + ADC configured
- python venv has been activated `~/.claude/skills/nano-banana-pro/.venv/bin/activate`


If you see errors, follow the setup guide in `~/.claude/skills/nano-banana-pro/SKILL.md`.
