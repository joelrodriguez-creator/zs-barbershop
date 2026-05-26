# NEXT_SESSION.md

_Last sync: 2026-05-26 on FalconXtreme PC. Mid-session save: foundation work (SEO + showcase + claude-seo plugin) shipped; bespoke homepage hero variants 2 of 3 generated, Variant A retry blocked on a transient Google 503 (model capacity). Resume prompt at the bottom._

## TL;DR

This session pivoted from the planned Google-reviews-marquee work into two foundational hardwirings + a bespoke hero imagery iteration:

1. **SEO + showcase log hardwired** — new project-level [CLAUDE.md](CLAUDE.md), [SEO.md](SEO.md) checklist, and [docs/showcase/client-showcase.md](docs/showcase/client-showcase.md) running log. Project CLAUDE.md auto-loads on every future session in this directory. Showcase markdown is the source-of-truth log; render to PDF via Claude Design when Ziad needs a polished snapshot.
2. **claude-seo plugin v2.0.0 installed globally** on PC at `~/.claude/skills/seo*` (Mac was already done). 32 `/seo*` skills now available in every Claude Code session. Lighthouse v13.1.0 already global. `npx unlighthouse` available on demand.
3. **Bespoke homepage hero generation via Nano Banana 2** — wired the `GEMINI_API_KEY` into `~/.claude.json` (was a placeholder string until today), Joel added $50 AI Studio prepay, restarted Claude Code, MCP respawned with new key. 2 of 3 variants generated successfully at 2K/16:9. Variant A failed first because billing hadn't propagated; retries blocked on transient Google 503 (model high demand).

**Where the next session picks up:** retry Variant A (House of Z), build hero-picker.html for side-by-side compare, get Joel's pick, finalize at 4K, wire into `prototype/index.html`. Then move on to barbers.html + services.html heroes. THEN `/seo audit https://zsbarbershop.com` once heroes land. THEN Impeccable polish pass.

## Currently in flight

- **Homepage hero generation** — 2 of 3 variants at `assets/generated/heroes/`:
  - `index-the-chair-2k.jpg` (Variant B, owner-craftsman intimate) — landed
  - `index-mediterranean-warmth-2k.jpg` (Variant C, Damascene tile + cedar + arched mirrors) — landed
  - Variant A (House of Z, wide cinematic interior) — needs retry. First attempt 429 (credits not propagated); retries 503 (Gemini high demand). Try again in 5–10 minutes via `mcp__nano-banana-2__generate_image`. Prompt preserved in [plans/after-restart-paste-this-graceful-fairy.md](C:/Users/Trader/.claude/plans/after-restart-paste-this-graceful-fairy.md).
- **Hero picker** — once Variant A lands, build `prototype/hero-picker.html` showing all 3 side-by-side at 16:9 with A/B/C labels, open in Chrome for Joel to pick. Then finalize the winner at 4K, wire into `prototype/index.html` `.hero` block.
- **Parked: real Google reviews marquee** — original session pickup brief. Birdeye scrape + auto-scroll marquee at `index.html` testimonials. Resume after heroes land. Full plan preserved in [plans/after-restart-paste-this-graceful-fairy.md](C:/Users/Trader/.claude/plans/after-restart-paste-this-graceful-fairy.md) "Parked: reviews marquee" section.
- **API key hygiene rotation** — `GEMINI_API_KEY` (`AIzaSyA9hdz-...BqFg`) was shared in a screenshot earlier in the chat transcript. After heroes are done, delete it in AI Studio and create a fresh one, then update `~/.claude.json`. Not urgent, hygiene.
- **Workspace CLAUDE.md /seo-first rule** — Joel authorized adding "default to /seo skill family for web project SEO" to `infrastructure/claude-global-config/workspace-CLAUDE.md` plus claude-seo entry in Known installed tools. Defer to /checkpoint phase; not blocking heroes.

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
