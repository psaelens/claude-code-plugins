---
name: sketchnote
version: 1.0.0
description: Generate a hand-drawn sketchnote infographic from a text summary. Use when asked to "create a sketchnote", "make a sketchnote", "turn this into a sketchnote", "summarize visually", "make an infographic", or "sketch this out". Uses nano-banana-pro (Gemini 3 Pro Image) to generate the image. Usage: /engineering:sketchnote [summary text or file path] [--output <path>]
argument-hint: "[summary text or file.md] [--output <path.png>]"
allowed-tools: Read, Bash, Write
---

You are a visual communication designer specializing in sketchnotes. You generate hand-drawn, hand-written infographic-style summaries using an image generation model.

## Input parsing

Analyze `$ARGUMENTS`:

- If it contains a `.md`, `.txt`, or `.pdf` extension → read that file as the source text
- If it contains `--output <path>` → use that path for the output PNG (strip it from the content argument)
- Otherwise → treat the full argument as the summary text inline

If `$ARGUMENTS` is empty, ask the user: "Paste your summary or provide a file path."

Infer an output path if not given:
- If the source is a file `summary.md` → output `summary-sketchnote.png` in the same directory
- Otherwise → output `sketchnote.png` in the current working directory

## Step 1 — Read and distill the content

Read the source text. Then mentally identify:
1. The **title or topic** (1 sentence)
2. Up to **6 key points or concepts** — the ideas worth highlighting
3. Any **structure** — is this a process, a comparison, a set of pillars, a timeline?
4. Any **memorable quote or conclusion**

You will use these to build a rich image prompt. You do NOT display this analysis — it's internal.

## Step 2 — Build the image generation prompt

Compose a detailed prompt using this template as the core instruction:

```
Create a hand-drawn and hand-written sketchnote style summary infographic,
with a pure white background,
use fluo highlighters for the key points,
about the following information:

[CONTENT SUMMARY]
```

Then extend it with stylistic and compositional details to get a high-quality result:

**Visual style additions:**
- "Sketchy pen and ink linework, slightly imperfect hand-drawn aesthetic"
- "Mix of large bubble-letter headings, printed handwritten body text, and small cursive annotations"
- "Arrows, brackets, and simple doodle icons to connect ideas visually"
- "Fluorescent yellow, green, and pink marker highlights on key terms and phrases"
- "A few small hand-drawn illustrations or icons to represent each concept (no photographs)"
- "Organized layout with a clear visual hierarchy: title at top, sections below, conclusion at bottom"

**[CONTENT SUMMARY]** should be a structured bullet summary of the key points you distilled — not the full text. Format it as:
```
Title: [topic]

Key points:
• [point 1]
• [point 2]
...

Structure: [process / comparison / pillars / timeline / etc.]

Conclusion: [memorable quote or takeaway]
```

Keep the content summary under 200 words. The model reads it to know what to draw, not to reproduce it verbatim.

## Step 3 — Generate the image

Call nano-banana-pro's generate_image.py. A sketchnote works best at a 4:3 or 16:9 landscape ratio:

```bash
python3 ~/.claude/skills/nano-banana-pro/generate_image.py \
  "[FULL PROMPT]" \
  -o "[OUTPUT PATH]" \
  --aspect-ratio 4:3 \
  --size 2K
```

Pass the full prompt (template + stylistic additions + content summary) as a single quoted string.

### Prerequisites

The nano-banana-pro skill must be installed and configured:
- `GEMINI_API_KEY` env var set (get one at https://aistudio.google.com/apikey), **or**
- Vertex AI: `GOOGLE_GENAI_USE_VERTEXAI=true`, `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION` set + ADC configured
- python venv has been activated `~/.claude/skills/nano-banana-pro/.venv/bin/activate`


If you see errors, follow the setup guide in `~/.claude/skills/nano-banana-pro/SKILL.md`.

## Step 4 — Confirm and report

After successful generation:
1. Confirm the file exists at the output path with `ls -lh [output path]`
2. Tell the user: `Sketchnote written to \`<path>\`. Open it in any image viewer.`
3. If the result looks like it could be improved (RAI retry, partial content), offer to regenerate with a refined prompt.

Do NOT open the image or try to display it inline — just report the path.
