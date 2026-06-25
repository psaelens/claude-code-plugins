# Visual System

A living document describing the brand's visual language. Edit freely — the `illustrate` skill reads this file to generate brand-consistent images. You can reorganize sections, rename headings, and add anything that helps describe the visual identity. The skill reads for intent, not strict schema.

---

## Brand identity

**Project name**: [Your project name]  
**Tagline**: [One-line description]  
**Brand personality**: [2–4 adjectives — e.g., "bold, playful, approachable" or "minimal, professional, trustworthy"]

---

## Color palette

| Role | Hex | Usage |
|------|-----|-------|
| Primary | `#______` | Main brand color — dominant in illustrations |
| Secondary | `#______` | Supporting color — accents and highlights |
| Background | `#______` | Default image background |
| Surface | `#______` | Cards, panels, elevated surfaces |
| Text | `#______` | Body text |
| Accent | `#______` | CTAs, highlights, focal points |

> Add more rows for semantic colors (success, warning, error, etc.) if relevant.

---

## Illustration style

Check the approach that fits the brand. Delete lines that don't apply. Add notes below as needed.

- [ ] **Flat design** — solid fills, no gradients, clean geometric shapes
- [ ] **Isometric 3D** — depth without perspective distortion, technical and precise
- [ ] **Photorealistic** — high-detail photography or photo-render hybrid
- [ ] **Line art** — minimal outlines, sketch-like, low fill
- [ ] **Watercolor / painterly** — soft edges, organic texture, handcrafted feel
- [ ] **Glassmorphism** — frosted glass, translucency, blur and depth
- [ ] **Retro / vintage** — grain texture, muted palette, nostalgic feel
- [ ] **3D render** — volumetric shapes, material-based shading, studio-lit
- [ ] **Geometric abstract** — bold shapes, pattern-driven, non-representational

Additional style notes:
```
[Describe specific visual characteristics here.
Examples:
- "Rounded corners on all shapes, never sharp 90° angles"
- "Characters are abstract blobs, not realistic human figures"
- "Always include a subtle paper texture overlay"
- "Use duotone treatment: primary color + white only"]
```

---

## Mood & atmosphere

**Tone**: [e.g., warm and inviting / cool and technical / energetic and bold / calm and minimal]  
**Lighting**: [e.g., soft diffuse light / bright and airy / dramatic high contrast / neutral flat studio light]  
**Texture level**: [e.g., completely flat / subtle grain / rich material and surface detail]  
**Complexity**: [e.g., minimal with few elements / moderately detailed / rich and layered]

---

## Composition guidelines

**Focal point placement**: [e.g., centered / left-aligned / rule-of-thirds upper-right]  
**Whitespace**: [e.g., generous — at least 30% of frame / tight, edge-to-edge / full-bleed]  
**Text overlay zone**: [e.g., "Leave the right 40% clear for headline text" or "Leave top third clear" or "n/a — images stand alone"]  
**Safe zone for cropping**: [e.g., "Keep key elements within center 60% of frame"]  
**Orientation preference**: [e.g., landscape only / portrait for mobile / flexible]

---

## Typography feel

(Font personality informs illustration style even when no text appears in the image)

**Heading font**: [e.g., "Geist — geometric sans, modern and clean"]  
**Body font**: [e.g., "Inter — neutral, highly readable"]  
**Display / accent**: [e.g., "Fraunces — expressive serif, used for editorial moments" or "n/a"]

---

## Dos and don'ts

### Do
- [e.g., Use rounded, friendly shapes throughout]
- [e.g., Keep compositions clean and uncluttered]
- [e.g., Prefer abstract representations over stock-photo aesthetics]
- [e.g., Use the primary color as the dominant element]

### Don't
- [e.g., Use gradients or color transitions]
- [e.g., Include realistic human faces]
- [e.g., Mix more than 3 colors in a single image]
- [e.g., Add drop shadows, glows, or lens flares]
- [e.g., Use photography — everything should feel illustrated]

---

## Reference images (optional)

Existing project images that represent the brand well. The `illustrate` skill can use these as style references with `--input`.

| File | Why it's on-brand |
|------|-------------------|
| `public/hero.png` | [e.g., Good example of our flat style and color usage] |
| `src/assets/og.png` | [e.g., Shows the right composition and whitespace] |

---

## Asset inventory (optional)

Track generated images here so the skill knows what already exists.

| File | Slot | Last updated |
|------|------|--------------|
| `public/hero.png` | Homepage hero (16:9) | [date] |
| `public/og.png` | OG / social card (16:9) | [date] |
