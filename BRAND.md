# Z's Barbershop — Brand Tokens

**Status:** PLACEHOLDER. Tokens are finalized in Phase 4 (palette lock) after Joel picks a direction from Phase 3 (`palette.html`).

This file is the single source of truth for design tokens. Future Impeccable / Claude Design / Huashu Design sessions on this project MUST reference this file (per global CLAUDE.md rule). When tokens change, change them here first, then propagate to `prototype/styles.css`.

## Palette (TBD)

```css
:root {
  --color-primary:   /* deep navy / charcoal / etc. — TBD Phase 4 */;
  --color-accent:    /* brass gold / single bright / etc. — TBD Phase 4 */;
  --color-surface:   /* warm cream / off-white / etc. — TBD Phase 4 */;
  --color-ink:       /* near-black body text — TBD Phase 4 */;
  --color-muted:     /* mid-gray supporting text — TBD Phase 4 */;
}
```

## Typography (TBD)

```css
:root {
  --font-serif:   /* headline serif — TBD Phase 4 */;
  --font-sans:    /* body sans — TBD Phase 4 */;
  --font-mono:    /* used only for hours / address blocks, if at all */;
}
```

## Spacing scale (will follow Wolosky pattern)

```css
:root {
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
}
```

## Radius + shadow (will follow Wolosky pattern)

```css
:root {
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.06);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
  --shadow-lg: 0 12px 32px rgba(0,0,0,0.12);
}
```

## Direction candidates (from Phase 3, not yet picked)

- **A — Classic Warm Traditional** — deep navy + brass gold + warm cream, serif headlines, warm-light interior photography. Personal, established, "trust this guy."
- **B — Modern Minimal Monochrome** — charcoal + off-white + single accent, geometric sans, high-contrast B&W photography. Cool, intentional, design-conscious.
- **C — Edgy Editorial Bold** — dramatic dark palette, bold display typography, fashion-forward photography. High-end, urban, statement-making.

The chosen direction's rationale will be documented in `design-brief.md`.
