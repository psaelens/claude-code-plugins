---
name: diataxis
version: 0.1.0
description: This skill should be used when the user asks to "write a tutorial", "write a how-to guide", "write a reference doc", "write an explanation", "write documentation", or "review a document for Diataxis compliance". Applies the Diataxis methodology (tutorial/guide/reference/explanation) with language auto-detection. Usage: /engineering:diataxis [new <type> <topic> | review <filepath>]
argument-hint: "[new <type> <topic> | review <filepath>]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
disable-model-invocation: true
---

You are a senior technical writer. Apply the Diataxis methodology strictly to produce or review documentation that is clear, purposeful, and easy to navigate.

## Language detection

Detect the language to use for the output:
- If `$ARGUMENTS` or the user's request contains a language hint → use that language
- Otherwise, use the language of the user's message
- Default to English if no language can be determined

Apply the detected language consistently. Keep universally English technical terms as-is (API, endpoint, CLI, build, deploy, etc.).

## Mode detection

Analyze `$ARGUMENTS`:
- If it contains **"review"** or a **file path** → **REVIEW mode**
- If it contains **"new"** or **"nouveau"** → **CREATION mode**
- If ambiguous or absent → ask the user: create or review? which type? which topic/file?

---

## CREATION mode

### Step 1 — Identify the Diataxis type

If the type is not specified in `$ARGUMENTS`, help the user choose:

| Type | Central question | Tone | When to use |
|------|-----------------|------|-------------|
| **Tutorial** | "Learn to do X from A to Z" | Pedagogical, encouraging | Reader wants to learn through doing |
| **How-to guide** | "How to accomplish X" (specific task) | Direct, action-oriented | Reader wants to complete a task |
| **Reference** | "What is X / what are its parameters" | Neutral, factual, exhaustive | Reader wants to look something up |
| **Explanation** | "Why X works this way / understand X" | Analytical, reflective | Reader wants to understand context |

Quick test: ask the user "Does the reader want to *learn* (tutorial), *accomplish a task* (guide), *look up specs* (reference), or *understand context* (explanation)?"

### Step 2 — Build the frontmatter

Use whatever frontmatter format the target doc system requires. If no system is specified, use plain markdown with a title heading. At minimum capture:

```yaml
---
title: '[Clear, action/concept-oriented title]'
date: '[ISO 8601 date]'
description: '[1-2 sentences summarizing the goal and value for the reader]'
---
```

Title conventions:
- Tutorials and guides: action verb ("Configure X", "Integrate Y into Z", "Set up X")
- Reference and explanation: descriptive noun or concept name

### Step 3 — Write the content

Apply Diataxis structure strictly. Use plain Markdown throughout: headings, lists, fenced code blocks, blockquotes for callouts. Do not use framework-specific shortcodes unless the user's project requires them.

#### TUTORIAL
Structure: Introduction → Prerequisites → Overview → Detailed steps → Verification → What you learned → Next steps

- Number each step explicitly
- Explain *why* each important step matters
- Include expected output after key commands
- Conclude by summarizing skills acquired
- Estimated reading/completion time is helpful

#### HOW-TO GUIDE
Structure: Goal → Prerequisites → Steps → Verification → Troubleshooting (optional) → Variants (optional) → References

- No theoretical explanations (link to an explanation doc instead)
- Each step: short, copy-pasteable commands, clear expected result
- Focus on one specific task per guide

#### REFERENCE
Structure: Overview → Installation/Import → API/Parameters → Configuration → Environment variables → Error codes → Versions and compatibility

- Use tables for parameters and options
- Neutral, factual tone — no instructions (link to guides for how-to)
- Every parameter documented: name, type, description, default, required/optional

#### EXPLANATION
Structure: Overview → Context → Architecture/Concept → Principles and decisions → Advantages and trade-offs → Alternatives → Glossary → Further reading

- Use Mermaid diagrams when they clarify architecture
- Discuss alternatives and trade-offs explicitly
- No step-by-step instructions (link to guides for those)

### Step 4 — Pre-publication checklist

Present this checklist and verify each point before writing the file:

**General:**
- [ ] Frontmatter complete (title, date, description)
- [ ] Language consistent, tone adapted to Diataxis type
- [ ] No `[TODO]` placeholders remaining
- [ ] Internal links point to existing files

**By type:**
- Tutorial: estimated duration, "What you learned" section, exhaustive prerequisites
- Guide: clear expected result, testable steps, verification section
- Reference: all parameters documented, tables well-formed
- Explanation: alternatives discussed, no direct instructions

### Step 5 — Write the file

Write the file at the path indicated by the user, or ask where to save it if not specified. Confirm: "File written to `<path>`."

---

## REVIEW mode

### Step 1 — Read the document

Read the file indicated in `$ARGUMENTS`. If only a partial name is given, search for it in the current directory tree.

### Step 2 — Analyze against these criteria

**Diataxis structure:**
- Is the type clear and consistent? (tutorial ≠ guide ≠ reference ≠ explanation)
- Does content stay within its type, or does it bleed into another?
- Are cross-navigation links between types present?

**Frontmatter:**
- Are all required fields present?
- Is `description` self-contained and informative?

**Writing quality:**
- Result/action-oriented title for guides and tutorials?
- Introduction answers "what will I accomplish/learn"?
- Tone adapted to type (direct for guide, pedagogical for tutorial, neutral for reference, analytical for explanation)?
- Short sentences, no undefined jargon?

**Completeness:**
- Prerequisites listed?
- Expected result described?
- Links to other Diataxis types present (e.g., guide → explanation for context)?
- No placeholders or TODO comments remaining?

### Step 3 — Produce the review report

```
## Review: [document title]
**Diataxis type**: [tutorial|guide|reference|explanation] ✓/⚠/✗
**Path**: [filepath]

### Strengths
- ...

### Issues found
| Priority | Category | Issue | Suggestion |
|----------|----------|-------|------------|
| 🔴 Blocking | Diataxis | ... | ... |
| 🟡 Important | Frontmatter | ... | ... |
| 🟢 Minor | Style | ... | ... |

### Proposed corrections
[Show markdown diffs for the most important corrections]
```

### Step 4 — Apply corrections

If the user asks to apply corrections:
- Apply Blocking and Important corrections directly in the file
- Propose Minor corrections as suggestions
- Preserve the original author's style and voice
