# NEXT_SESSION.md

_Last checkpoint: 2026-05-26 evening on FalconXtreme PC. Joel leaving office; picking up on MacBook later._

## TL;DR

This session hardwired three foundational pieces — SEO checklist + tooling (`claude-seo` plugin v2.0.0 installed globally), client-showcase running log (so Ziad gets a polished iteration narrative on demand), and bespoke hero imagery for the first two prototype pages via Nano Banana 2. **Homepage hero** = Variant B "The Chair" (single chair foreground, owner-craftsman intimate) — shipped and approved. **Barbers hero** = Variant C "Workstation Detail" (tools on leather strop + apothecary shelves) — shipped, but with a known image-drift gotcha noted below in "Currently in flight."

**Where the next session picks up:** verify the barbers hero looks right on Mac (the `background-position: center 72%` tweak should show the tools, not the empty mirror top). Then generate + pick + wire the services.html hero (last of the 3). Then `/seo audit https://zsbarbershop.com` for the first real SEO pass. Then an Impeccable polish pass once SEO is clean.

## First actions on the other machine

### macOS (MacBook)
```zsh
cd "$HOME/Code Projects/clients/zs-barbershop"
git pull origin main
# Confirm both hero images render correctly before generating services hero:
open prototype/index.html      # homepage — should show the single chair on right
open prototype/barbers.html    # barbers — should show tools on leather strop
```

### Windows (FalconXtreme)
```powershell
cd "E:\Code Projects\clients\zs-barbershop"
git pull origin main
```

## Recreate local-only files

- `~/.claude.json` `mcpServers.nano-banana-2.env.GEMINI_API_KEY` — Gemini API key for Nano Banana 2 image generation. The PC was wired today (key prefix `AIza...BqFg` from Default Gemini Project = `gen-lang-client-0057489859`, $50 prepay on AI Studio). Mac should already have this from the Apr 19 install. If Mac's key isn't working, regenerate at https://aistudio.google.com/apikey.
- `~/.claude/skills/seo*` — `claude-seo` plugin v2.0.0 already installed on both machines (Mac last session, PC this session). Verify via the `/seo` skills appearing in the Skill tool's available list. Re-run `bash ~/.claude/plugins/marketplaces/agricidaniel-claude-seo/install.sh` on Mac if missing.

## What's done (this session)

- `9ad3031` — Sync: hardwire SEO + showcase + claude-seo; 3 homepage hero variants generated
- `<this checkpoint>` — Checkpoint: integrate homepage + barbers heroes; correct barbers final to match approved variant

Specifically:
- New project-level `CLAUDE.md` hardwiring SEO + showcase + voice/imagery rules
- New `SEO.md` checklist referencing claude-seo plugin v2.0.0, Lighthouse, Unlighthouse
- New `docs/showcase/client-showcase.md` running narrative (foundation phase + 5-icon set + Zohan bio + homepage hero pick + barbers hero pick all documented)
- `.gitignore` updated to whitelist `*-final.jpg/png` heroes, ignore `generated_imgs/`, whitelist `docs/showcase/client-showcase.pdf`
- claude-seo plugin v2.0.0 installed at `~/.claude/skills/seo*` (32 `/seo*` skills now available globally on PC)
- `GEMINI_API_KEY` wired into `~/.claude.json` mcpServers.nano-banana-2.env (was a placeholder string until today)
- $50 AI Studio prepayment added to Default Gemini Project
- Homepage hero: 3 directions explored (House of Z / The Chair / Mediterranean warmth), Joel picked **The Chair**, regen at 4K, optimized to `assets/generated/heroes/index-the-chair-final.jpg` (332KB), wired into `prototype/index.html` `.hero` with left-fading dark gradient
- Barbers hero: 3 directions explored (Lineup / Hands at Work / Workstation Detail), Joel picked **Workstation Detail**, wired into `prototype/barbers.html` via new `.page-hero--barbers` CSS modifier
- Picker pages preserved for the iteration narrative: `prototype/hero-picker.html`, `prototype/barbers-picker.html`

## Currently in flight (paused)

- **Barbers hero crop / composition fit** — known gotcha to verify on Mac:
  1. The 4K regeneration produced a DIFFERENT composition than the 2K Joel picked (Nano Banana 2 doesn't preserve composition across calls even with identical prompts). To work around this, the canonical `barbers-workstation-final.jpg` is the **optimized 2K** (2752×1536, 570KB), NOT a 4K regen. Future heroes should either: (a) skip the 4K regen entirely and use the optimized 2K, or (b) use `mcp__nano-banana-2__edit_image` with the 2K as input to upscale-and-refine without composition drift.
  2. Joel flagged the original wire-in as "too cropped — too much nothing, very little of the instruments." The CSS now uses `background-position: center 72%` to shift the visible window down toward the bottom of the image where the tools sit on the leather strop, and `min-height: 480px` instead of 420px. Verify this reads right on Mac at desktop AND mobile widths. If still wrong, options: (a) bump min-height further (550-650px), (b) shift to `bottom` position, (c) regenerate at a different angle.

## What's pending (in priority order)

1. **Verify barbers hero on Mac** — refresh `prototype/barbers.html`, judge whether the new `background-position: center 72%` + `min-height: 480px` shows enough of the tools. Adjust if not.
2. **Services page hero (`services.html`)** — last of the 3. Same 3-variant workflow. Suggested directions:
   - A: Tools macro on a wooden bench (different angle than barbers — vertical strop, scissors hanging on hooks, soft side-light)
   - B: Cape + clippers detail (a folded barber's cape draped over a chair arm, clippers + cord coiled beside it)
   - C: Pricing-board / signage-style — a vintage hand-lettered price board on the wall, brass + black, prices visible
3. **`/seo audit https://zsbarbershop.com`** — first real SEO pass via the freshly-installed claude-seo plugin. Per [SEO.md](SEO.md), the deploy-blockers are: canonical links missing, OG/Twitter meta missing, BreadcrumbList JSON-LD missing, LocalBusiness JSON-LD missing on barbers.html, sitemap.xml missing, robots.txt missing.
4. **Impeccable polish pass** — once SEO is clean, run `/impeccable polish` on the homepage to tighten any remaining visual issues (typography, spacing, the trilingual welcome strip, anything that doesn't earn its place).
5. **Add `/seo-first` rule to `infrastructure/claude-global-config/workspace-CLAUDE.md`** — so future web projects default to the `/seo*` skill family over hand-rolling. Joel authorized this in the session; deferred from /checkpoint as not blocking.
6. **Rotate exposed `GEMINI_API_KEY`** — the key (`AIzaSyA9hdz-OQX4MVmLswZ39WahQbUMFD_BqFg`) was shared in a screenshot earlier in this chat transcript. Hygiene: delete it in AI Studio, create a fresh one, update `~/.claude.json` on both machines.
7. **Parked: real Google reviews marquee** — the ORIGINAL session pickup brief, deferred behind heroes. Plan: scrape 8–10 reviews from Birdeye via Playwright, save to `assets/data/reviews.json`, replace 3-card placeholder testimonials with an auto-scrolling marquee. Full plan in `C:/Users/Trader/.claude/plans/after-restart-paste-this-graceful-fairy.md` "Parked: reviews marquee" section.

## Prompt to paste into next Claude Code session

```
I'm resuming Z's Barbershop on my MacBook. Read NEXT_SESSION.md at the repo
root for full context.

Quick state: this session installed claude-seo + locked the homepage hero
(Variant B, The Chair) + locked the barbers hero (Variant C, Workstation
Detail). The barbers wire-in had a composition-drift issue (4K regen
diverged from the approved 2K), now fixed by using the 2K directly +
background-position: center 72%. Verify the barbers hero looks right
first — if the tools are visible and not too cropped, we proceed.

Next actions in order:
1. Verify prototype/barbers.html hero looks right in browser
2. Generate 3 services.html hero variants via Nano Banana 2 (same workflow
   as the other two — see docs/showcase/client-showcase.md for the pattern,
   suggested directions in NEXT_SESSION.md "What's pending")
3. Run /seo audit on the project (claude-seo plugin is installed globally)
4. Run /impeccable polish pass

Hard constraints (also in CLAUDE.md):
- No AI human faces
- No hot-towel mentions (already purged)
- No em dashes in body copy
- Forbidden words: "luxury", "esteemed", "lounge", "distinction"
- Commit author: joel.rodriguez@galacticmedical.com
- /book URL is reserved in vercel.json
- HOLD domain purchase until Ziad reviews case-study
```

## Hard rules for this project

- **Commit author email:** `joel.rodriguez@galacticmedical.com` (Vercel Hobby attribution).
- **No em dashes in body copy.** Use commas, colons, semicolons.
- **No AI-generated human faces.** Anywhere.
- **No hot-towel mentions.** Ziad doesn't offer it as a service. Zohan reference replaces it.
- **Mobile-first CSS.** Default styles target mobile, `@media (min-width: ...)` for desktop.
- **JSON-LD on every page.** `LocalBusiness` schema with real address, phone, hours. Currently missing on barbers.html — fix during SEO pass.
- **Default to `/seo *` skills** over hand-rolling SEO checks (claude-seo plugin installed globally on both machines).
- **Append to `docs/showcase/client-showcase.md`** when a design move ships (icon set, hero, logo, major copy lockdown, new component). The running narrative is what Ziad reviews; render to PDF via Claude Design when polished output is needed.
- **HOLD domain purchase** until Z reviews case-study.
- **`/book` URL** is reserved in `vercel.json` for the future booking system; do not wire to anything else.
- **Cost ceiling on image gen** — under $5 just run, $5–$50 confirm, >$50 propose splitting. Nano Banana 2 is ~$0.067/1K image, ~$0.151/4K. This session: ~$2 across heroes + iterations (well within $50 prepay).
