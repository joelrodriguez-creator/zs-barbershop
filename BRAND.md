# Z's Barbershop — Brand Tokens

**Status:** LOCKED as of 2026-05-26. Direction A "The House" + heritage anchors #1, #2, #3, #4, #5 (NOT #6 — Z does not serve coffee).

This file is the single source of truth for design tokens. Future Impeccable / Claude Design / Huashu Design sessions on this project MUST reference this file (per global CLAUDE.md rule). When tokens change, change them here first, then propagate to `prototype/styles.css`.

## Direction summary

**"The House"** — dark cinema, warm brass on near-black, vintage Americana display type, heritage seal logo with Lebanese cedar mark, Damascene geometric pattern as accent. Owner-led narrative anchored in Ziad's Lebanese roots. Inclusive to Cuban-American Westchester and Muslim clientele alike.

Reference exemplars in priority order:
1. House of Heritage (Las Vegas) — primary anchor, cinematic interior photography + brass palette + heritage register
2. Huckle (London) — secondary anchor, owner-led narrative + restrained palette + one earned accent color
3. Wolosky Podiatry refresh (`business/wolosky-podiatry-refresh/`) — stack + workflow exemplar from this workspace

## Palette

```css
:root {
  /* Primary surface — near-black with warmth (not pure #000) */
  --color-primary:   #1a1612;
  /* Card / elevated surface — slightly warmer */
  --color-surface:   #2a221b;
  /* Accent — brass mustard. Used for CTAs, key visual accents, logo highlights. */
  --color-accent:    #c8a35a;
  /* Body text on dark backgrounds (the primary read mode) */
  --color-ink:       #e8dfd0;
  /* Body text on light backgrounds (rare — for the cream cards) */
  --color-ink-dark:  #1a1612;
  /* Light cream — for typographic cards, callouts, contrast blocks */
  --color-cream:     #e8dfd0;
  /* Muted text on dark — for captions, supporting copy, fine print */
  --color-muted:     #7a7165;
  /* Accent-soft — for hover states, subtle backgrounds */
  --color-accent-soft: rgba(200, 163, 90, 0.15);
  /* Border / divider on dark */
  --color-line:      #3a3128;
}
```

Color usage rules:
- `--color-primary` is the dominant background, ~80% of any given page.
- `--color-accent` (brass mustard) is the ONLY saturated color. CTAs, the cedar mark, key headlines accents, and the geometric pattern stroke all use it. Don't introduce a second saturated color.
- `--color-cream` cards on `--color-primary` background = the "House of Heritage card" pattern. Use for important callouts (hours, CTA blocks).
- White is NOT in the palette. If "white" is needed for a logo or icon, use `--color-cream`.

## Typography

### Font stacks

```css
:root {
  /* Display — vintage Americana, bold condensed industrial sans, all caps for headlines */
  --font-display: 'Big Shoulders Display', 'Oswald', 'Impact', sans-serif;
  /* Body — classical serif for prose, bios, service descriptions */
  --font-body:    'Source Serif 4', Georgia, 'Times New Roman', serif;
  /* UI / secondary — clean modern sans for nav, captions, fine print */
  --font-ui:      'Inter', system-ui, -apple-system, sans-serif;
  /* Arabic — for the trilingual welcome line (heritage anchor #1) */
  --font-arabic:  'Amiri', 'Noto Naskh Arabic', serif;
}
```

### Google Fonts include

In `<head>` of every page:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&family=Inter:wght@400;500;600;700&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
```

### Type scale

```css
:root {
  /* Display headlines — Big Shoulders Display, ALL CAPS, weight 800 */
  --text-display-xl: clamp(2.5rem, 6vw, 5rem);    /* h1 hero */
  --text-display-lg: clamp(2rem, 4.5vw, 3.5rem);  /* h1 page title */
  --text-display-md: clamp(1.75rem, 3.5vw, 2.5rem); /* h2 */
  --text-display-sm: 1.5rem;                       /* h3 */

  /* Body — Source Serif 4 */
  --text-body-lg:    1.125rem;  /* lead paragraph */
  --text-body-md:    1rem;      /* default body */
  --text-body-sm:    0.875rem;  /* supporting copy */

  /* UI — Inter */
  --text-ui-sm:      0.875rem;  /* nav links */
  --text-ui-xs:      0.75rem;   /* eyebrow, fine print, all-caps labels */
}
```

Display headlines are ALWAYS uppercase. Body never is. Eyebrow text is uppercase with 0.12em letter-spacing.

## Spacing scale

```css
:root {
  --space-1:  0.25rem;
  --space-2:  0.5rem;
  --space-3:  0.75rem;
  --space-4:  1rem;
  --space-5:  1.25rem;
  --space-6:  1.5rem;
  --space-8:  2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-20: 5rem;
  --space-24: 6rem;
}
```

## Radius + shadow

```css
:root {
  --radius-sm: 4px;   /* buttons, chips */
  --radius-md: 8px;   /* cards */
  --radius-lg: 16px;  /* hero cards, major containers */
  --radius-pill: 999px;

  /* Shadows on dark backgrounds — use subtle warm glow, not black drop shadow */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.5);
  /* Brass glow — for hover states on accent elements */
  --shadow-accent: 0 0 24px rgba(200, 163, 90, 0.25);
}
```

## Logo direction

**Heritage seal monogram** inside an arched frame, with **Lebanese cedar mark** integrated. Final SVG produced in Phase 5.

Concept brief for Phase 5:
- Arched frame (Damascene / vintage barbershop sign register)
- "Z's" or "ZD" monogram in center (Big Shoulders Display style lettering)
- Lebanese cedar tree silhouette as a small element — either above the monogram inside the arch, OR as the "Z" stem replacement, OR as a tiny seal at the bottom of the arch
- Surrounding text in the arch: "BARBERSHOP" (top) + "EST." (bottom) or "WESTCHESTER · MIAMI" (bottom)
- Two-color (brass `#c8a35a` on `--color-primary`) plus an optional cream version
- SVG format, optimizable to <5KB

The cedar must be recognizable as a Lebanese cedar, not a generic Christmas tree — broad-spreading horizontal branches, distinctive silhouette.

## Damascene geometric pattern accent (heritage anchor #5)

8-pointed star (Khatim Sulayman / Damascene star) used as:
- A repeating border strip above the footer (thin band, ~24px tall, brass on near-black)
- A section divider between major content blocks (single star centered with thin lines extending left and right)
- A subtle background pattern on the contact card (very low opacity, brass on near-black)

Finalized in Phase 5 alongside logo. CSS-generated where possible (background-image with linear gradients + SVG masks), single SVG fallback for the star.

The pattern is widely recognized as Islamic / Damascene / Andalusian art across religions — it appears in cathedrals, synagogues, mosques, and secular buildings throughout the Mediterranean and Middle East. Used here as cultural heritage signal, not religious symbol.

## Heritage anchor copy (locked)

These exact pieces of copy will appear in the prototype. Marked with which page.

### Trilingual welcome (anchor #1) — header or footer strip on EVERY page

```html
<div class="welcome">
  <span>Welcome</span>
  <span class="sep">·</span>
  <span>Bienvenidos</span>
  <span class="sep">·</span>
  <span lang="ar" dir="rtl" class="arabic">أهلاً وسهلاً</span>
</div>
```

Styled in `--font-ui` 14px on dark backgrounds, brass `·` separators, Arabic in `--font-arabic`.

### Heritage-named services (anchor #3) — services.html

Service names use heritage-honoring framing where authentic:

- **Lebanese Hot-Towel Shave** ($price TBD)
- **Eyebrow Threading** ($price TBD) — uniquely Middle Eastern technique
- **Traditional Beard Sculpting** ($price TBD) — Middle Eastern grooming heritage
- Standard Cut — $35
- Kids' Cut — $price TBD
- Senior Cut — $price TBD
- Line-Up — $price TBD
- Father & Son Cuts — $price TBD (resonates with both Cuban and Lebanese family cultures)

### Bio language (anchor #4) — about.html (excerpt locked, full bio TBD from Ziad)

```
Ziad learned to cut hair in Lebanon, where the hot-towel shave isn't a
special service — it's how every barber works. He brought the old-school
tradition to Westchester, and ten years later, he's still working out of
the same chair on Bird Road. Cubans, Lebanese, anyone who needs a fade
and a story — the door is open.
```

The closing line "Cubans, Lebanese, anyone who needs a fade and a story — the door is open" is locked. It's the inclusivity statement that holds the entire heritage layer together.

### Cedar mark (anchor #2) — logo + footer

See Logo direction section above. Cedar appears inside the heritage seal arch and as a small footer accent.

## Imagery direction

**Cinematic dim interior shots of Z's actual shop** — warm bulb lighting, deep shadows, herringbone-or-tile floor visible, barber chairs in symmetric composition where possible. This is the House-of-Heritage aesthetic translated to Z's space.

Until real photography exists, **Nano Banana 2** generates atmospheric placeholders:
- Hero: warm-lit interior, empty barber chair foreground, mirrors and tools background, no human faces, cinematic depth-of-field
- Service teasers: tools (straight razor, hot towel, scissors, brush), close-up macro, brass + leather + wood props, warm side-lighting
- Gallery placeholder: shop details (barber pole exterior, shelf of products, hot-towel cart) — atmospheric, no faces

Cost ceiling per global rule: estimate from 2–3 samples, confirm with Joel if total >$5. Expected $0.30–$1.00 for the placeholder pass.

**Photo session with Ziad before launch:** schedule for real interior + service shots + Ziad at work. Nano Banana 2 imagery is placeholder, not final.

## Voice and tone

- **Confident, not boastful.** "Old-school done right." beats "Best barbershop in Miami!"
- **Specific, not generic.** "8455 SW Bird Rd" beats "convenient Miami location."
- **Conversational, not corporate.** "Walk in or give us a call" beats "Schedule your appointment today."
- **Inclusive by default.** "Cubans, Lebanese, anyone who needs a fade" beats "We welcome diverse customers."
- **Heritage is texture, not a sales pitch.** Mention Lebanon. Don't lecture about it.

## Voice rules (hard)

- No em dashes in body copy. Use commas, colons, semicolons. (Em dashes fine in markdown headers and signatures.)
- No "luxury" / "esteemed" / "distinction" / "lounge" — those words make $35 cuts feel like upselling.
- No "premium grooming experience" — corporate speak.
- No "we" without an antecedent — clarify Z + the shop early.
- Spanish phrases used sparingly, naturally — "vecinos" or "el barbero" are fine in context, full-Spanish sentences require translation alongside.
- Arabic appears in the welcome line + service name "Lebanese Hot-Towel Shave" + Ziad's bio. Don't sprinkle elsewhere.

## What's still TBD

Captured from Z directly in upcoming session:
- Full price list for services beyond standard cut ($35)
- Ziad's full bio (years cutting, training in Lebanon, what brought him to Westchester)
- Sunday hours (closed or open?)
- Real photos: interior, exterior, Ziad at work, recent cuts
- Spanish-language depth (single welcome line vs. fuller Spanish content?)
- Whether the Arabic service-name framing feels right to Ziad (he may prefer simpler "Hot-Towel Shave")
