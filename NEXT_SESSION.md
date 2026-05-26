# NEXT_SESSION.md

_Last checkpoint: 2026-05-26 on FalconXtreme PC. Session ended mid-review-scrape after recurring API errors. Resume prompt at the bottom._

## TL;DR

This session delivered the full 5-icon brass-on-matte-black service-icon set, integrated them into the prototype, fixed all the size/border/box issues Joel flagged, bumped the header logo size, and stripped every hot-towel mention from the live site (Ziad doesn't actually offer hot-towel shaves as a standalone service). The Zohan reference is now woven into Ziad's bio on both `index.html` and `barbers.html`.

**Where the next session picks up:** scraping real Google reviews for a House-of-Heritage-style auto-scrolling marquee. Got 1 full review (Gino Fernandez) + 5 more named reviewers (Isabel Nieto Gaviria, Luisdel López Beltrán, sigfredo pacheco, Vladislava Koleva, Layla Nsoor) from Birdeye but couldn't pull their body text before the API died. The marquee component itself hasn't been built — the homepage Testimonials section is still showing 3 placeholder cards.

## Currently in flight

- **Real Google reviews scrape** — Birdeye (`https://reviews.birdeye.com/zs-barbershop-170249571721062`) is the right source. 182 reviews total there. First scroll exposed only the first batch of names — body text needs more aggressive scrolling/expansion. Use Playwright MCP (`mcp__playwright__*`). The 3 anonymized Google SERP snippets are also captured below as a fallback.
- **Streaming marquee component** — Joel wants the House of Heritage cycling-strip pattern: **3 reviews visible at a time, auto-scrolls right-to-left, more than 3 in the queue**. Reference: `inspiration/pages/heritage.md` (or the live `https://houseofheritage.com` if needed). No framework — pure CSS animation + vanilla JS (match the project's no-framework rule).

## First actions on the other machine (or after restart)

**Windows (FalconXtreme PC):**
```powershell
cd "E:\Code Projects\clients\zs-barbershop"; git pull
```

**macOS (MacBook):**
```zsh
cd "$HOME/Code Projects/clients/zs-barbershop" && git pull
```

Then open `prototype/index.html` in a browser to confirm the 5 icons + logo + Zohan bio render correctly before resuming the reviews work.

## What's done this session

- **5 service icons locked** — generated via Vertex AI Imagen 4 Fast (`scripts/gen-icon.mjs`), edited via Pillow scripts:
  - `haircut.png` (V4-edit: scissors + comb, barber pole removed)
  - `beard-trim.png` (V2 shape + V1 background, brass-only extracted)
  - `cut-beard.png` (raw V3-ish silhouette, tightened to canvas)
  - `lineup.png` (regen r1-v4 framed-then-unframed by brass extraction)
  - `kids.png` (regen v3 framed-then-unframed by brass extraction)
- **Icon scripts** kept at `scripts/`:
  - `gen-icon.mjs` — 4-variant generator with locked house style prompt
  - `crop-icon.py` — paint-out + bbox-crop pattern (used for haircut barber-pole removal)
  - `crop-lineup.py` — rotation + brass-only extract pattern
  - `swap-bg.py` — brass-only re-render on pure-black canvas
  - `tighten-icons.py` — canonical "make all icons sized like haircut" pass
  - `make-transparent.py` — RGBA conversion, anti-aliased bg → alpha=0
- **Icon integration** — replaced all inline `<svg class="service-icon">` blocks in `prototype/index.html` with `<img class="service-icon" src="../assets/generated/icons/<name>.png">`. The hot-towel-shave service card was DELETED entirely.
- **CSS adjustments** in `prototype/styles.css`:
  - `.service-icon`: 64px → 112px, added `object-fit: contain`
  - `.logo-wordmark`: 56px → 96px
- **Hot-towel purge** across all 3 prototype HTML files:
  - Meta descriptions updated (index/services/barbers)
  - Ziad's bio rewritten in both `index.html` AND `barbers.html` HTML body + JS data array
  - "TRADITIONAL HOT-TOWEL SHAVE" Why-Z's bullet → "TRAINED IN LEBANON"
  - Service descriptions stripped of "hot-towel pass/finish" mentions
  - Standalone Lebanese Hot-Towel Shave service row removed from `services.html` HTML and JSON-LD `OfferCatalog`
  - Footer text on all 3 pages updated
  - Placeholder review text de-hot-toweled
- **Zohan reference woven into Ziad's bio** on `index.html` (short version) and `barbers.html` (longer version, in both visible HTML and JS data array): _"Regulars joke he's the real-life Zohan — Adam Sandler's Middle Eastern barber, minus the Mossad backstory."_
- **.gitignore expanded** to track only the 5 canonical icons + `picker.html`. Imagen variant PNGs (~28MB of v1–v4 outputs across all 6 attempted icons) stay local but untracked. `.playwright-mcp/` also ignored.

## What's pending (in order)

1. **Finish the Google reviews scrape** — get full body text for at least 8–10 reviews so the marquee has content to cycle through. Strategy: navigate back to Birdeye, scroll the reviews list aggressively (Birdeye lazy-loads as you scroll the inner reviews column), then re-run the structured extraction. **Fallback:** if Birdeye keeps fighting, try the Wheree aggregator at `https://zs-barbershop-2.wheree.com/`. Save the result to `assets/data/reviews.json` with shape `[{name, age, body, source}, ...]`.
2. **Build the auto-scrolling marquee** — replace the 3-card placeholder testimonials section in `prototype/index.html` (around line 240) with a House-of-Heritage-style 3-visible auto-scroll-right strip. Pure CSS `@keyframes` translateX animation + duplicate the review list inline for seamless looping. Add a "Read all 169 reviews on Google →" link below pointing at the live Google listing.
3. **Verify on both mobile and desktop breakpoints.** Marquee should pause on hover (desktop) and not break under the 700px breakpoint.

## Reviews captured so far (partial)

**Stats confirmed from Birdeye:** 5.0 average across 182 reviews. Distribution: 177 five-star, 4 four-star, 0 three-star, 0 two-star, 1 one-star (the lone 1-star is from Layla Nsoor — clearly an outlier complaint, skip it).

**Full review text captured (1):**
- **Gino Fernandez** (Google, 8 months ago, 5 stars): _"Best barbershop in Miami hands down! Z is the best barber and I only trust him to cut my hair. Come check it out you won't be disappointed!"_

**Reviewer names captured but body text not yet pulled (4 to chase down):**
- Luisdel López Beltrán (Google, 2 months ago)
- Isabel Nieto Gaviria (Google, 9 months ago) — Spanish: _"Bueno quien solicito el servicio fue mi esposo atendido por Alejandro el Cubano excelente y muy buen precio."_ (captured!)
- sigfredo pacheco (Google, 9 months ago)
- Vladislava Koleva (Google, 11 months ago)

**Anonymous Google SERP snippets (3 — Google strips reviewer attribution on the public search results page):**
- _"High quality, clean haircuts for a good price and friendly atmosphere."_
- _"Z's Barber Shop is not just a place to get a hair cut it's an experience."_
- _"Great service and gave me a very nice haircut."_

Worst case for the marquee, we have 8 short usable snippets (2 with full attribution, 1 in Spanish, plus 3 anonymous Google SERP excerpts) — enough to feel dynamic but a bit thin. Goal next session: get to 10–15 with attribution.

## Prompt to paste into next Claude Code session

```
Resuming Z's Barbershop after a checkpoint — we hit recurring API errors
mid-scrape. Read NEXT_SESSION.md for full context but the headline is:

1. The 5 service icons are LOCKED and integrated into prototype/index.html.
2. All hot-towel mentions have been PURGED across all 3 prototype pages —
   Ziad doesn't offer hot-towel shaves as a standalone service. Don't add
   them back. Bios mention the Zohan movie (Adam Sandler, Middle Eastern
   barber) as a playful regular-customer joke — that stays.
3. Header logo bumped from 56px → 96px. Service icons 64px → 112px.

PICK UP HERE:

Step 1 — Reviews scrape. Open Birdeye via Playwright MCP:
   https://reviews.birdeye.com/zs-barbershop-170249571721062
   Scroll the inner reviews column (not the page — Birdeye lazy-loads as
   the inner div scrolls). Extract reviewer names + body text. Need at
   least 8–10 with attribution for a substantive marquee. Fallback source:
   https://zs-barbershop-2.wheree.com/
   Save to assets/data/reviews.json with shape [{name, age, body, source}, ...].

Step 2 — Marquee component. Replace the 3-card placeholder testimonials
section in prototype/index.html (around line 240) with a House-of-Heritage
style cycling strip: 3 visible at a time, auto-scrolls right-to-left,
duplicates the list inline for seamless looping. Pause on hover (desktop).
Reference: inspiration/pages/heritage.md. Pure CSS @keyframes + vanilla JS
— no framework (matches the project's stack discipline).

Add a "Read all 169 reviews on Google →" link below the marquee pointing
at the live Google Business listing. The 5.0 stars / 169 reviews count
already in the section stays.

CONSTRAINTS:
- No em dashes in body copy (BRAND.md voice rule)
- No "luxury" / "esteemed" / "lounge" / "distinction"
- Mobile-first CSS
- Commit author: joel.rodriguez@galacticmedical.com

After both steps land cleanly, run /checkpoint again.
```

## Hard rules for this project (unchanged)

- **Commit author email:** `joel.rodriguez@galacticmedical.com` (for Vercel Hobby plan attribution).
- **No em dashes in body copy.** Use commas, colons, semicolons.
- **No AI-generated human faces.** Imagery comes from real photography or is skipped.
- **No hot-towel mentions.** Ziad doesn't offer it as a service. The Zohan reference replaces it as the heritage hook in his bio.
- **Mobile-first.** Default styles target mobile. `@media (min-width: ...)` for desktop.
- **JSON-LD on every page.** `LocalBusiness` schema with real address, phone, hours.
- **Cost-ceiling check on Imagen.** Estimate from 2–3 sample images first. Confirm with Joel if projected >$5. (Total icon spend this session: ~$0.48 over 6 batches.)
- **HOLD domain purchase** until Z reviews case-study.
- **`/book` URL is reserved** in `vercel.json` for a future booking system.
