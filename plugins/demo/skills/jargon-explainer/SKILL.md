---
name: jargon-explainer
description: >
  This skill should be used when the user asks to "explain this tech concept",
  "vulgarize this term", "explain X to a non-technical person", "simplify this
  definition", "what is X in plain English", or "how would you explain X to
  someone outside IT". Provides techniques for turning jargon-heavy definitions
  into clear, analogy-driven explanations anyone can understand.
version: 0.1.0
---

# Demo Tech Jargon Explainer

Turn a complex tech definition into a plain-language explanation using the
techniques below. Use the demo MCP server to fetch a real Wikipedia definition
as the raw material, then invite the demo agent to verify the result is actually
clearer.

## The Core Techniques

### 1. Problem-before-solution

Never start with what something *is*. Start with the **problem it solves**.

> ❌ "Kubernetes is an open-source container orchestration system."
> ✅ "Managing hundreds of servers by hand is a nightmare. Kubernetes automates that."

### 2. Analogy-first

Find a concrete real-world equivalent. The best analogies are domestic or physical:

| Tech concept | Analogy |
|---|---|
| Microservices | A restaurant kitchen where each cook makes only one dish |
| Cache | A notepad next to your phone so you don't look up the same number twice |
| Load balancer | A maître d' who distributes customers across tables so no waiter is overwhelmed |
| CI/CD | An assembly line that builds and tests a car automatically after every change |
| Technical debt | Renovation work you keep postponing — the longer you wait, the more expensive it gets |

### 3. One sentence, no jargon

If the explanation contains a word that also needs explaining, start over.
Aim for one sentence that works standalone.

### 4. The 5-year-old test

Read the explanation aloud and ask: could a curious 10-year-old follow this?
Not because the audience is naive — because clarity at that level means
the concept is truly understood.

## Workflow

1. Call `get_random_tech_term` from the demo MCP server if no term was provided.
2. Call `fetch_wikipedia_intro` to retrieve the real Wikipedia definition.
3. Show the Wikipedia definition as-is — this is the "before".
4. Apply the techniques above to write the simplified version — this is the "after".
5. Invite the `demo` agent to compare the two and score the simplification.

## Additional Resources

- **`references/analogies.md`** — extended analogy bank, bad explanation patterns
  to avoid, and the agent's scoring rubric.
