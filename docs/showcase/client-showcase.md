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

## (in flight) — Bespoke hero imagery via Nano Banana 2

Iterating per-page hero photography placeholders using Google's Nano Banana 2
(Gemini 3.1 Flash Image) model. Workflow per page:

1. Generate 3 distinct directional drafts at 2K, 16:9 aspect ratio
2. Ziad's chosen direction refined and finalized at 4K
3. Wire into the page's `<header>`

Explicitly placeholder — real photography of Z's actual shop interior will
replace these once the photo session is scheduled. The goal is to give Ziad a
much better "what this could look like once it's done" feel during the review.

Entries to be added as variants land.

---

## (planned next) — Real Google reviews marquee

Replace the 3-card placeholder testimonials on `index.html` with an auto-scrolling
marquee fed by real Google reviews scraped from Birdeye. 8–10 reviews with
attribution, House-of-Heritage-style cycling strip, "Read all 169 reviews on
Google →" link below.

Plan + reviewer captures preserved in `NEXT_SESSION.md` and the parked plan file.
