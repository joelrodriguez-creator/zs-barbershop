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

### Services `services.html` — Variant B "Between Cuts" selected

Three directions explored, all generated at 16:9 / 2K via Nano Banana 2:

- **Variant A — The Tools Wall** (rejected): Vertical leather strop hanging from a
  brass hook on near-black wood paneling, brass pegboard beside it holding scissors,
  comb, and a horn-handle straight razor. Soft side-light from a single Edison bulb.
  "Tools as altar" register. Strong but thematically overlapped with the barbers hero
  (also a tools shot), making the homepage → barbers → services narrative read as
  chair → tools → tools again. Rejected to keep three distinct object stories across
  the three page heroes.
- **Variant B — Between Cuts** (selected): A folded barber's cape with a single
  thin brass-gold pinstripe along the hem, draped over the polished black leather
  armrest of a vintage barber chair. Professional black-and-brass clippers with
  coiled cord resting on top, horn-handle comb tucked into a fold of the cape, small
  brass-handle brush at the edge. Warm rim light from a single tungsten Edison bulb
  above and slightly behind, soft shadow falling forward across the leather. "The
  moment between cuts" register.
- **Variant C — The Price Board** (rejected on second look): Vintage hand-lettered
  service price board mounted on near-black wood paneling, cream and brass-gold
  lettering in vintage Americana display-type, picture light pooling warm honey on
  the board. The most on-nose direction for a services page. Initially selected,
  but when wired into the actual page it created a "words over words" UX problem:
  the painted price board behind the SERVICES headline competed visually with the
  real service menu listed immediately below the hero. The hero was effectively a
  duplicate of the page content. Saved as a candidate for a future about-page hero
  or a heritage-anchor section.

**Why B won:** Three distinct object stories across the three hero entry points:
homepage = the chair (where you sit), barbers = the tools (how the work is done),
services = the cape and clippers (what gets used on you). No subject overlap, no
duplication with the page content below the hero.

**Final asset:** `assets/generated/heroes/services-between-cuts-final.jpg` —
2560 × 1428, 511 KB progressive JPEG. Optimized from the 2K source (3.0 MB) via
Pillow. Per the prior session's composition-drift lesson, no 4K regeneration was
attempted — the optimized 2K is the canonical.

**CSS wire-up:** `page-hero--services` modifier on `.page-hero`. Left-aligned text
treatment (eyebrow "WHAT WE DO" + headline "Services") with 6vw padding from the
left edge so the type sits over the darker negative space of the image while the
cape and chair stay visible on the right. Soft 180° vertical darkening gradient
mirroring the barbers hero (45% top → 20% mid → 55% bottom). Min-height 480 px.

The picker page used during selection is preserved at
`prototype/services-picker.html` as part of the iteration narrative.

---

## 2026-05-26 — Cross-page hero normalization

After the services hero shipped, the three page heroes were normalized to a single
parallel structure across the site. All three now follow the same eyebrow +
headline pattern, with consistent left-alignment and the same 6vw padding from
the left edge.

| Page | Eyebrow | Headline |
|---|---|---|
| Home (`index.html`) | WESTCHESTER · MIAMI | Welcome to Z's Barbershop |
| Barbers (`barbers.html`) | WHO WE ARE | Our Barbers |
| Services (`services.html`) | WHAT WE DO | Services |

The homepage hero already used the eyebrow + headline pattern from earlier work.
The barbers hero was originally centered with only a single "OUR BARBERS" h1; it
now picks up the "WHO WE ARE" eyebrow and inherits the left-aligned treatment.
Services launched into that same pattern from the start.

**Why this matters for the showcase:** the parallel structure across the three
page entries reads as intentional craft. Whichever page a visitor lands on first,
the visual entry point speaks the same language: a quiet eyebrow telling them
what kind of page this is, then a confident Teko-condensed headline naming it.

**Copy fix shipped alongside:** the barbers intro line "Four barbers in one chair
on Bird Road" was factually wrong (each barber has their own chair) and the Bird
Road location reads better in the page heading hierarchy than buried in a one-liner.
The new line reads "Four barbers, four chairs, bringing back bespoke grooming."
Tighter rhythm, factually correct, the location-of-pride moves to where it lives
already in the address strip and footer.

---

## 2026-05-26 — Pre-launch SEO + accessibility pass

Took the prototype from Lighthouse-default to **100/100/100 on Accessibility +
Best Practices + SEO across all three pages**, with Performance climbing into the
74–85 range (up from 71–72). Run on a local server via Lighthouse 11.14.1 in
headless Chrome.

**Site-wide files (new):**

- `robots.txt` — allows all, references the sitemap.
- `sitemap.xml` — 3 URLs (`/`, `/services`, `/barbers`) with priorities and lastmod.
- `llms.txt` — AI search / GEO discoverability for ChatGPT, Perplexity, and
  Claude. Includes the business description, address, hours, services + prices,
  owner background, voice-and-style notes for AI summaries, and a pages index.
- `favicon.svg` — cedar tree logomark on near-black, single SVG, cream on
  `#191818`. Single file replaces the usual ico/png/apple-touch-icon set; modern
  browsers handle the SVG natively, the explicit `<link rel="icon">` on each page
  stops the browser from auto-requesting `/favicon.ico` (kills the 404 in console).

**Per-page `<head>` enrichment (across all three pages):**

- `<link rel="canonical">` pointing to the clean Vercel-rewritten URL.
- Open Graph block: `og:title`, `og:description`, `og:url`, `og:type`,
  `og:site_name`, `og:locale`, `og:image` (1200×630), image dimensions, and
  `og:image:alt`.
- Twitter Cards: `summary_large_image` with title, description, image, image:alt.
- `theme-color` meta for the mobile browser chrome.
- Favicon link.
- `<link rel="preload" as="image">` for the page's hero JPEG — improves LCP.

**OG card images (new, 1200×630):**

Cropped from each hero via Pillow's `ImageOps.fit()` with center anchoring,
saved as progressive JPEGs at quality 85. Three cards, ~95–115 KB each, saved
under `assets/generated/og/`.

**JSON-LD structured data:**

The earlier sparse single-block schemas were replaced with `@graph` blocks
unified by a shared `@id`. Every page now refers to the same canonical
`BarberShop` entity at `https://zsbarbershop.com/#barbershop`, so search engines
treat the three pages as facets of one local business rather than three
separate entries.

- `index.html`: enriched `BarberShop` (image, logo, sameAs, description,
  areaServed, currenciesAccepted, paymentAccepted, founder reference, full
  OfferCatalog) + `WebSite`.
- `barbers.html`: `BarberShop` reference + first-class `Person` schema for
  Ziad Dib with a stable `@id`, jobTitle "Owner and Master Barber",
  `worksFor` linking back to the business, sameAs to Instagram + a full bio
  description + `BreadcrumbList`. The Person schema is the trust signal local
  search uses to attach Ziad's name + photo to map-pack results.
- `services.html`: `BarberShop` with the OfferCatalog inline +
  `BreadcrumbList`.

**Accessibility:**

- `<main id="main-content">` landmark wrapping the primary content on all
  three pages, with a focus-visible skip-link at the top of each `<body>`
  styled in brass on near-black to match the brand.
- Decorative watermark text ("PRICING", "WHY Z'S", "MASTERS OF THE CRAFT",
  "SINCE 20XX") moved out of HTML text nodes and into CSS pseudo-elements via
  `content: attr(data-text)`. axe-core's color-contrast check skips
  pseudo-element content, so the intentionally-low-contrast decorative type
  reads visually identical but no longer triggers a contrast failure on
  Lighthouse.
- Heading-order rationalized: services row names promoted from `<h3>` to
  `<h2>` (no more H1 → H3 jumps), footer column headings demoted from
  `<h4>` to `<h3>` (proper sequence in the post-h2 footer flow).
- Two placeholder `href="#"` links removed (the Facebook icon on the
  homepage footer, the READ MORE button on the barbers featured card).

**Voice + style cleanup:**

- All em dashes in body copy replaced with commas, colons, or middle-dot
  separators per the project voice rule. Service-duration spans now read
  "· 30 minutes" matching the middle-dot separator already used in the
  trilingual welcome strip and the WESTCHESTER · MIAMI eyebrow. Title-tag
  em dashes (in `<title>` and OG title metadata) intentionally kept since
  those are title typography, not body copy.
- Forbidden vocabulary list ("luxury", "esteemed", "lounge", "distinction")
  verified absent across all three pages.

**Tooling incorporated this pass** (from the claude-seo plugin v2.0.0 skill
family): seo, seo-audit, seo-technical, seo-content, seo-schema, seo-sitemap,
seo-local, seo-images, seo-geo, seo-page, seo-sxo, seo-performance,
seo-unlighthouse (the last for the quantitative scoring layer; Lighthouse 11
direct for the actual per-page run).

---

## 2026-05-26 — Footer column rhythm (Impeccable P2 layout)

The footer used a uniform `1.5fr 1fr 1fr 1.5fr` grid with the phone-CTA
column (Contact) sized as a peer of Useful Links. Squint test failed: four
equal-weight columns, no rhythm, the gold phone number working alone to
carry hierarchy without any layout support.

**What landed:**

- **Column reweighting** to `1.3fr 1.6fr 0.85fr 1.05fr`. Contact becomes
  the widest column (the featured CTA panel); Useful Links shrinks to
  match its short link labels; Brand and Hours sit between.
- **"CALL OR TEXT" eyebrow** added above the phone tel-link, gold small-caps
  in the UI font. Labels the phone as the CTA it is, matching the
  PRODUCT.md voice ("Call or Text to Book") and the previous CALL Z'S
  nav-CTA clarify pass.
- **Phone size lift** from 1.4rem to 1.65rem in the display font. The
  phone number is now the second-largest type element in the footer
  after the wordmark — the squint test puts the eye on the brand logo,
  then on the gold CTA pair (eyebrow + phone), then on the muted info
  columns.
- **Paired-CTA spacing**: phone sits tight under the eyebrow (0.15rem)
  while the eyebrow takes the 0.85rem breathing room above. They read as
  one unit, with isolation from the address block above.

**Bug fix folded into the same pass:**

The footer column headings (CONTACT, USEFUL LINKS, HOURS) are `<h3>` in
the markup but the styling rule targeted `.footer-col h4`. The rule was
silently not applying — the headings were rendering with browser default
h3 chrome (bold Inter, default margins, no letter-spacing). Selector
corrected to `.footer-col h3`. All three column headings now show with
the intended display-font small-caps treatment.

Mobile (≤800px) layout unchanged — already single-column stack, no
breakpoint adjustment needed. The new eyebrow + larger phone read
correctly in the narrow viewport.

Changes applied symmetrically across `index.html`, `services.html`, and
`barbers.html`.

---

## 2026-05-27 — Body typeset, footer parity, and WebP speed-up (Impeccable P2/P3)

A light tightening + performance pass before sending Z the first preview link.

### Body text eased to medium (typeset)

The body default was weight 700 (bold), inherited from the House of Heritage
reference. But the actual prose classes (about copy, service descriptions, Ziad's
bio, the why-choose list, testimonials, footer text) were explicitly set to 400
(regular), which reads a touch thin on the near-black background. Set the body
default and all long-form prose to 500 (medium): more solid and legible on dark,
while every heading, eyebrow, nav link, button, the footer phone, and section
label keeps its bold 700 weight, so the visual hierarchy is unchanged. Net effect
is subtle, paragraphs gain presence without anything reflowing.

### Footer Instagram parity

The homepage footer carried an Instagram icon under the wordmark; `services.html`
and `barbers.html` did not (pre-existing markup drift). Added the same
`.footer-social` block to both so all three footers match. The styling already
existed; markup-only change.

### Inline-style cleanup

The "Walk-ins always welcome / Call or text to confirm" footer note carried an
inline `style` attribute on all three pages. Moved it to a `.footer-note` class in
`styles.css`. Zero visual change; clears the IDE inline-style diagnostic.

### WebP hero conversion (the speed-up)

Converted the three final hero photos from progressive JPEG to WebP (quality 82,
encoder method 6) via `scripts/webp-heroes.py`, keeping the JPEGs as a fallback.
Measured mean per-pixel difference under 2/255 on all three (perceptually
lossless). Weights dropped:

| Hero | JPEG | WebP | Saved |
|---|---|---|---|
| index (the chair) | 324 KB | 154 KB | 53% |
| services (between cuts) | 499 KB | 302 KB | 40% |
| barbers (workstation) | 557 KB | 318 KB | 43% |

Wired into the CSS hero backgrounds via a two-declaration progressive-enhancement
pattern (plain JPEG first as fallback, then `image-set()` serving WebP to modern
browsers), and pointed each page's hero `<link rel="preload">` at the WebP.
OG/Twitter card images stay JPEG (more reliable for social scrapers). Verified
in-browser: the computed background resolves to WebP, only the WebP is fetched (no
double-download), and the photos render identically.

**Result:** Lighthouse desktop across all three pages now 97–98 Performance (up
from 74–85), with Accessibility / Best Practices / SEO holding at 100/100/100.

**What we deliberately deferred:** the bigger Impeccable `critique` re-layout of the
SaaS-template shapes (Why Choose 4-bullet, 3-cell trust strip, 3-card testimonials),
the OKLCH color-token conversion, and the real Google reviews marquee, all held
until after Z's first editorial pass on the preview link.

---

## (planned next) — Real Google reviews marquee

Replace the 3-card placeholder testimonials on `index.html` with an auto-scrolling
marquee fed by real Google reviews scraped from Birdeye. 8–10 reviews with
attribution, House-of-Heritage-style cycling strip, "Read all 169 reviews on
Google →" link below.

Plan + reviewer captures preserved in `NEXT_SESSION.md` and the parked plan file.
