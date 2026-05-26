# Z's Barbershop — Client Showcase Log

A running record of design moves, iterations explored, and decisions made on the
Z's Barbershop website project, built for Ziad Dib by Joel Rodriguez.

Updated every session a design move ships. When Ziad needs a polished snapshot
to review, this markdown gets rendered to a branded PDF via Claude Design (or
Huashu Design as fallback). The PDF lives at
[client-showcase.pdf](client-showcase.pdf).

---

## How to read this log

Each entry is dated and structured as:

- **What landed** — the approach we shipped
- **What we explored** — directions considered and rejected, and why
- **Image references** — visual snapshots where relevant

The "what we explored" sections matter most for Ziad: they show the editorial
avenues we went down before settling on the final choice. Even when an option
gets rejected, the thinking behind it shows the project got considered work,
not just the first thing that came to mind.

---

## 2026-05-23 to 2026-05-26 — Foundation phase

### Direction lock: "The House"

After exploring three high-level design directions, locked on **Direction A —
"The House"**: dark cinema register, warm brass on near-black, vintage Americana
display type, heritage seal logo with Lebanese cedar mark, Damascene geometric
pattern accent.

**Reference exemplars (priority order):**
1. House of Heritage (Las Vegas) — primary anchor, cinematic interior photography
2. Huckle (London) — secondary anchor, owner-led narrative + restrained palette
3. Wolosky Podiatry refresh — workspace stack + workflow exemplar

**What we explored:**
- Direction B: brighter, more Cuban-Miami-coded register with terracotta and
  cream. Rejected — overplays the Cuban side at the expense of the Lebanese
  heritage story.
- Direction C: minimalist Apple-product aesthetic, white-on-white. Rejected —
  too cold for an old-school neighborhood barber shop. Loses the warmth of
  the actual space.

### Palette (locked from House of Heritage)

Pulled directly from HoH's computed styles for 1:1 visual fidelity:

- Background: `#191818` (near-black, faintest warm undertone)
- Body / headlines / logo: pure white `#ffffff`
- Brass mustard accent (CTAs, eyebrows, icons): `#c8a35a`
- No warm-brown surface colors (an earlier draft used `#2a221b`; retired).

### Typography (locked from House of Heritage)

- **Display:** Teko, bold condensed sans, all caps, oversized — reads "carved
  on a sign," vintage Americana.
- **Body:** Montserrat at weight 700, which is HoH's distinctive choice. Crisp
  readability on the dark background.
- **Arabic:** Amiri / Noto Naskh for the trilingual welcome strip.

### Hero anchors implemented

1. **Trilingual welcome strip:** "Welcome · Bienvenidos · أهلاً وسهلاً" appears
   at the top of every page. Brass `·` separators, Arabic in `--font-arabic`,
   `dir="rtl"` for proper rendering. Heritage anchor #1.
2. **Cedar logo mark:** Stylized Lebanese cedar silhouette flanks the Z's
   wordmark. Cream color (not brass — brass is reserved for CTAs). Heritage
   anchor #2.
3. **Damascene 8-point star divider:** Used as a section divider and pre-footer
   strip. Cross-cultural Mediterranean motif, recognized in architecture across
   religions (cathedrals, synagogues, mosques, secular buildings). Heritage
   anchor #5.
4. **Inclusivity statement:** "Cubans, Lebanese, anyone who needs a fade and a
   story, the door is open." Holds the heritage layer together without
   overplaying it.

### Bio: the Zohan reference

Ziad's bio on both `index.html` and `barbers.html` includes the playful regulars'
joke: "Regulars joke he's the real-life Zohan, Adam Sandler's Middle Eastern
barber, minus the Mossad backstory." Lands the heritage hook with humor that
matches Z's personality (per Joel: "fun, quirky") without lecturing.

**What we explored:**
- Straight-laced "trained in Lebanon" bio. Rejected as too dry for Z's voice.
- Long-form personal history. Deferred — the short version reads better on a
  homepage; the longer treatment lives on the future about page.

---

## 2026-05-26 — Service icon set (5 brass-on-matte-black icons)

Generated and locked the canonical service icon set via Vertex AI Imagen 4 Fast,
post-processed via Pillow scripts for brass-only extraction and canvas
tightening:

- `haircut.png` — scissors + comb composition (V4-edit, barber pole removed)
- `beard-trim.png` — V2 shape + V1 background blend
- `cut-beard.png` — combined cut + beard service, raw V3-ish silhouette
- `lineup.png` — regen r1-v4 frame-then-unframed by brass extraction
- `kids.png` — regen v3 frame-then-unframed by brass extraction

Final sizing: 112px each in the service grid (up from 64px in an earlier cut).
The larger size gives them the brass presence they need against the matte
black background.

**What we explored and rejected:**
- **Hot-towel shave icon** — generated 4 variants. All retired when we learned
  Ziad does not offer hot-towel shaves as a standalone service. We followed
  through and **purged every hot-towel mention** from all 3 prototype pages
  (meta descriptions, hero copy, service rows, JSON-LD `OfferCatalog`, Ziad's
  bio, footer text, placeholder review text). The Zohan reference replaces it
  as the heritage hook in Z's bio.
- **Multi-color icon palette** — early concepts used brass + cream + a deep
  red accent. Rejected — the brand discipline calls for brass as the *only*
  saturated color (HoH's pattern, single earned accent).
- **Photographic icons** (real tool photographs). Rejected at this stage —
  illustrated icons read more cohesive across a service grid and don't need
  photography rights/sourcing.

**Total generation cost:** ~$0.48 across 6 batches (5 final + 1 retired).

### Generation toolchain (preserved for future regenerations)

- `scripts/gen-icon.mjs` — 4-variant generator with locked house-style prompt
- `scripts/crop-icon.py` — paint-out + bbox-crop pattern
- `scripts/crop-lineup.py` — rotation + brass-only extract pattern
- `scripts/swap-bg.py` — brass-only re-render on pure-black canvas
- `scripts/tighten-icons.py` — canonical "size like haircut" pass
- `scripts/make-transparent.py` — RGBA conversion, anti-aliased bg → alpha=0

---

## 2026-05-26 — Header logo bumped to 96px

The logo grew from 56px to 96px in the header to land with more brass presence
on the nav strip. Cream wordmark (matches HoH's white/cream approach), not
brass — brass stays reserved for CTAs.

---

## 2026-05-26 — Bespoke hero imagery via Nano Banana 2

Iterating per-page hero photography placeholders using Google's Nano Banana 2
(Gemini 3.1 Flash Image) model. Workflow: generate 3 distinct directional
drafts at 2K, 16:9 widescreen → pick the keeper → regenerate at 4K → optimize
via Pillow to ~2560px progressive JPEG → wire into the page `<header>`.

Real photography of Z's actual shop interior will replace these once the
photo session is scheduled. These placeholders give Ziad a much sharper
"what this could look like once finished" feel during the prototype review.

### Homepage `index.html` — Variant B "The Chair" selected

Three directions explored, all generated at 16:9 / 2K:

- **Variant A — House of Z** (rejected): Wide cinematic interior, long row of
  vintage chairs marching down the right side with Edison bulbs above each,
  herringbone parquet floor, vintage framed photos on dark left wall, deep
  vanishing point to the back of the shop. The most House-of-Heritage-faithful
  of the three. Strong, but reads as "the shop as venue" rather than the
  artisan voice we want.
- **Variant B — The Chair** (selected): Single vintage barber chair photographed
  3/4 angle from the side. Heavy black leather seat foreground, polished brass
  armrests + crank handle glowing under one low-hanging tungsten Edison bulb.
  Wall of mirrors framed in dark walnut behind, blurred warmly with shelves of
  vintage glass product bottles. Owner-craftsman register, intimate. Lands the
  "this is Ziad's chair" framing.
- **Variant C — Mediterranean warmth** (rejected): Same wide composition as A,
  but with explicit Z's-coded touches — Damascene 8-point star tile pattern in
  the floor, cedar wood shelving, arched mirrors in dark Mediterranean wood,
  exposed brick accent wall. Most identifiably "Z's" of the three. Beautiful
  but heritage-anchored architecture risks reading "Lebanese-themed" rather
  than "Lebanese-influenced." Saved as a candidate for a future about-page
  hero or a heritage-anchor section.

**Why B won:** The intimate single-chair framing matches Z's actual product
(one chair, one barber, hands-on relationship) more honestly than the wide-shop
shots, which sell "venue" rather than "barber." It also creates a stronger
contrast with the multi-chair imagery we'll likely use on `barbers.html` and
the tool / service imagery on `services.html`.

**Final asset:** `assets/generated/heroes/index-the-chair-final.jpg` —
2560×1429, 332 KB progressive JPEG. Optimized from the 4K source (8.1 MB)
via Pillow for Lighthouse-friendly weight.

**CSS wire-up:** background-image on `.hero`, stacked with a 90° darkening
gradient (78% black on the left fading to 8% black on the right) so the
headline + CTA read cleanly against the dark mirror-bokeh while the chair
stays bright. Mobile breakpoint shifts to a centered text layout with a
top-to-bottom darkening gradient to keep the image legible at narrow widths.

The picker page used during selection is preserved at
`prototype/hero-picker.html` as part of the iteration narrative.

### Barbers `barbers.html` — Variant C "Workstation Detail" selected

Three directions explored, all generated at 16:9 / 2K:

- **Variant A — The Lineup** (rejected): Empty four-chair scene with brass-detailed
  chairs in symmetric arrangement, vintage framed barber portraits on the back
  wall, Edison bulbs hanging from dark ceiling, herringbone parquet. Communicates
  "team of barbers" without faces. Strong but felt redundant against the homepage
  hero, which already sells the shop interior.
- **Variant B — Hands at Work** (rejected): Tight macro of a barber's working-class
  hands holding brass-loop scissors mid-cut, comb in the off-hand, leather watch
  strap visible on the wrist. Customer's dark hair visible but no face, no
  recognizable features. Deep warm bokeh shop interior behind. The strongest
  "skill of the work" framing of the three. Saved as a candidate for a future
  in-page card or about-section asset.
- **Variant C — Workstation Detail** (selected): Macro of a single barber's counter
  — vintage straight razor with brass handle, two pairs of scissors, comb,
  boar-bristle shaving brush, porcelain shaving mug, amber tonic bottle, all
  arranged on a worn brown leather strop. Wood-framed mirror behind reflecting
  warm bulb glow. Apothecary shelves on either side holding "Bay Rum", "Hair
  Elixir", "Talc". Owner-craftsman / artisan register.

**Why C won:** The workstation detail sells the *artisanship of the trade* in a
way the homepage's single chair complements rather than competes with. The
homepage answers "is this a real barber shop?" — the barbers page answers "do
they care about how they do the work?" C delivers that craft-and-tools answer
without showing people, which keeps the no-faces rule clean.

**Final asset:** `assets/generated/heroes/barbers-workstation-final.jpg` —
2560×1429, 281 KB progressive JPEG. Optimized from the 4K source (7.8 MB) via
Pillow.

**CSS wire-up:** `page-hero--barbers` modifier on `.page-hero`, min-height
bumped from the default 320 px to 420 px to give the still-life room to
breathe. Background image stacked under a top-to-bottom darkening gradient
(55% black top → 35% mid → 65% bottom) so the centered "OUR BARBERS" headline
reads cleanly over the warm brass + leather + bottle clutter.

### Services `services.html` — in flight

Coming next session. Same 3-variant workflow.

---

## (planned next) — Real Google reviews marquee

Replace the 3-card placeholder testimonials on `index.html` with an auto-scrolling
marquee fed by real Google reviews scraped from Birdeye. 8–10 reviews with
attribution, House-of-Heritage-style cycling strip, "Read all 169 reviews on
Google →" link below.

Plan + reviewer captures preserved in `NEXT_SESSION.md` and the parked plan file.
