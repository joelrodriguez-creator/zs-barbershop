# NEXT_SESSION.md

_Last checkpoint: 2026-05-26 late evening on MacBook. Continuing session after the FalconXtreme PC checkpoint earlier in the day; this evening pushed the Mac side forward through 4 more commits._

## TL;DR

The pre-launch SEO + accessibility pass already landed earlier today (commit
`5da5cda` brought all 3 prototype pages to 100/100/100 on A11y + Best
Practices + SEO; performance 74–85). Tonight ran the Impeccable audit queue
on top of that — P1 fixes (`1472ef1`: cream token warmer, thumb-row buttons,
hamburger mobile nav), P2 clarify (`cd42990`: nav CTA "BOOK STYLIST" → "CALL
Z'S" with tel-link), and P2 layout (`f4fd4b8`: footer column rhythm
reweighted + display-font heading-selector bug fixed + "CALL OR TEXT"
eyebrow paired with bigger gold phone). Lighthouse re-verified at session
end: all 3 pages still 100/100/100 across A11y/BP/SEO.

Also shipped one global-config change tonight: audio-chime Stop hook
(`db7a3e6` in `claude-global-config`) — plays a soft system chime when
Claude finishes a turn. Mac is already bootstrapped; PC needs `sync claude
config` + Claude Code restart before the chime fires there.

**Where the next session picks up:** continue the Impeccable queue. Next
in line is `/impeccable typeset` (body weight audit, ease 700 → 500 where
readability benefits), then `/impeccable critique` on the SaaS-template
shapes (Why Choose Z's 4-bullet, 3-cell trust strip, 3-card testimonials),
then OKLCH color conversion, then the P3 items.

## First actions on the other machine

### macOS (MacBook)
```zsh
cd "$HOME/Code Projects/clients/zs-barbershop"
git pull origin main
python3 -m http.server 8000 &
open http://localhost:8000/prototype/index.html
```

### Windows (FalconXtreme)
```powershell
# Pull global-config FIRST so the audio chime + bootstrap idempotent re-run lands
git -C "E:\Code Projects\claude-global-config" pull
powershell -ExecutionPolicy Bypass -File "E:\Code Projects\claude-global-config\bootstrap.ps1"
# Restart Claude Code to register the new Stop hook (chime won't fire until restart)

# Then pull the project
cd "E:\Code Projects\clients\zs-barbershop"
git pull origin main
python -m http.server 8000
# In another terminal:
start http://localhost:8000/prototype/index.html
```

## Recreate local-only files

No new local-only files this session. Previously-noted:

- `~/.claude.json` `mcpServers.nano-banana-2.env.GEMINI_API_KEY` — already
  present on both machines. Not used this session (no image generation).
- `~/.claude/skills/seo*` — claude-seo plugin v2.0.0 installed globally on
  both machines. Verify via the `/seo` skills appearing in the Skill tool.

## What's done (this session)

This evening's commits on top of the morning PC work:

- `db7a3e6` (claude-global-config) — Add audio chime Stop hook (Mac + PC). New `hooks/audio-chime.sh` + `.ps1`. Wired into both `bootstrap.sh` and `bootstrap.ps1` as a second Stop entry alongside the existing checkpoint nudge. Bootstrap ran on Mac → live this session restart onward.
- `f4fd4b8` (zs-barbershop) — P2 layout: footer rhythm + h3 selector fix. Reweighted footer grid from uniform `1.5fr 1fr 1fr 1.5fr` to asymmetric `1.3fr 1.6fr 0.85fr 1.05fr` so the Contact column (phone CTA) outweighs Useful Links and Hours. Added "CALL OR TEXT" gold eyebrow above the phone tel-link. Lifted phone size 1.4rem → 1.65rem (second-largest type after wordmark). Folded in a bug fix: `.footer-col h4` selector targeted a tag the markup doesn't contain — corrected to `.footer-col h3`, so the intended display-font small-caps treatment now applies to CONTACT/USEFUL LINKS/HOURS headings.

Earlier today on the PC (already shipped, summarized here for continuity):

- `5da5cda` — Services hero (Variant B "Between Cuts") + cross-page hero normalization (WHO WE ARE / WHAT WE DO eyebrows) + pre-launch SEO/a11y pass to 100/100/100.
- `1472ef1` — Impeccable P1 fixes: `--color-cream` pure white → `#fafaf6` (warm-tinted off-white); thumb-row divs → semantic `<button>` with `aria-pressed`; hamburger mobile nav (button + slide-down drawer + `nav.js` + `inert` attribute for proper a11y).
- `cd42990` — Impeccable P2 clarify: nav CTA "BOOK STYLIST" → "CALL Z'S" (tel-link) on desktop nav + mobile drawer across all 3 pages.

## What's pending (in priority order)

1. **P2 `/impeccable typeset`** — audit body font-weight per section; ease long-form prose from 700 to 500 where readability benefits. Apply to index/services/barbers consistently.
2. **P2 `/impeccable critique`** — UX heuristic deep-dive on the SaaS-template shapes: the "Why Choose Z's" 4-bullet feature list + 3-cell trust strip + 3-card testimonials trio. Goal: break the template into more editorial brand-register layouts.
3. **P2 OKLCH conversion** — leftover piece of the P1 #2 colorize work. Convert hex tokens in `styles.css` to OKLCH (visually near-identical, no user-facing change, future-proofs the palette).
4. **P3 `/impeccable optimize`** — convert 3 hero JPEGs (`assets/generated/heroes/*-final.jpg`) to WebP for ~30% weight savings. Should lift Performance score (currently 74–85) toward 90+.
5. **P3 `/impeccable polish`** — final pass after all of the above land.
6. **Footer parity fix** — `services.html` and `barbers.html` brand columns are missing the Instagram social icon block that `index.html` has. Pre-existing markup drift, surfaced during the P2 layout pass. Small fix (`<div class="footer-social">…</div>` block, ~6 lines).
7. **Inline-style cleanup** — `prototype/index.html:281` has `<p style="margin-top:.75rem;opacity:.7;">` inline style flagged by IDE diagnostic. Move to a class in `styles.css` if doing a CSS-pass sweep.
8. **Add `/seo-first` rule to `infrastructure/claude-global-config/workspace-CLAUDE.md`** — so future web projects default to the `/seo*` skill family over hand-rolling. Joel authorized this earlier; deferred again as not blocking.
9. **Rotate exposed `GEMINI_API_KEY`** — the key (`AIzaSyA9hdz-OQX4MVmLswZ39WahQbUMFD_BqFg`) was shared in a screenshot earlier in this chat transcript. Hygiene: delete it in AI Studio, create a fresh one, update `~/.claude.json` on both machines.
10. **Parked: real Google reviews marquee** — scrape 8–10 reviews from Birdeye via Playwright, save to `assets/data/reviews.json`, replace 3-card placeholder testimonials with an auto-scrolling marquee. Full plan in `C:/Users/Trader/.claude/plans/after-restart-paste-this-graceful-fairy.md` "Parked: reviews marquee" section.

## Prompt to paste into next Claude Code session

```
I'm resuming Z's Barbershop. Read NEXT_SESSION.md at the repo root for full
context.

Quick state: the pre-launch 100/100/100 SEO/A11y/BP scores are locked in
across all 3 pages, the Impeccable P1 fixes shipped, and tonight the P2
clarify (nav CTA → CALL Z'S) and P2 layout (footer rhythm + h3 selector
fix) also shipped. All 3 pages still at 100/100/100 Lighthouse-verified at
session end.

Next in the Impeccable queue (in order): P2 typeset (body weight audit), P2
critique (SaaS-template-shape break), P2 OKLCH conversion, P3 optimize
(JPEG → WebP), P3 polish. Plus a small footer parity fix (services and
barbers brand columns are missing the Instagram icon block that index has).

Hard constraints (also in CLAUDE.md):
- No AI human faces
- No hot-towel mentions (already purged)
- No em dashes in body copy
- Forbidden words: "luxury", "esteemed", "lounge", "distinction"
- Commit author: joel.rodriguez@galacticmedical.com (per-commit via git -c)
- /book URL is reserved in vercel.json
- HOLD domain purchase until Ziad reviews case-study
- Design moves that ship → append dated entry to docs/showcase/client-showcase.md

Start by asking me which Impeccable item to run first — they're sequential
but the parity fix is a 2-minute aside that could land first if it fits.
```

## Hard rules for this project

- **Commit author email:** `joel.rodriguez@galacticmedical.com` (Vercel Hobby attribution). Use `git -c user.email=...` per-commit; do NOT update git config.
- **No em dashes in body copy.** Use commas, colons, semicolons, middle-dots.
- **No AI-generated human faces.** Anywhere. Silhouettes / hands-only / back-of-head only.
- **No hot-towel mentions.** Ziad doesn't offer it as a service.
- **Mobile-first CSS.** Default styles target mobile, `@media (min-width: …)` for desktop.
- **JSON-LD on every page.** `LocalBusiness` schema. All 3 pages currently have it (added in `5da5cda`); preserve it.
- **Default to `/seo *` skills** over hand-rolling SEO checks (claude-seo plugin installed globally on both machines).
- **Append to `docs/showcase/client-showcase.md`** when a design move ships (icon set, hero, logo, major copy lockdown, new component). The running narrative is what Ziad reviews; render to PDF via Claude Design when polished output is needed.
- **HOLD domain purchase** until Z reviews case-study.
- **`/book` URL** is reserved in `vercel.json` for the future booking system; do not wire to anything else.
- **Pre-deploy gate** on touched prototype HTML: SEO=100, A11y≥95, BP≥95 (per project CLAUDE.md). Use `lighthouse <url> --only-categories=accessibility,best-practices,seo --preset=desktop`. Currently all 3 pages at 100/100/100.
- **Cost ceiling on image gen** — under $5 just run, $5–$50 confirm, >$50 propose splitting. Nano Banana 2 is ~$0.067/1K image, ~$0.151/4K.
