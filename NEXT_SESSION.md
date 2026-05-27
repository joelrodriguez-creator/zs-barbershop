# NEXT_SESSION.md

_Last checkpoint: 2026-05-27 on FalconXtreme PC. Polish pass shipped + deployed to a Vercel preview, and a branded founder-handoff PDF was built for Ziad. Joel is forwarding the PDF + preview link to Z and will relay his editorial feedback next session._

## TL;DR

The light polish + speed-up pass shipped and is **live on a Vercel preview**:
`https://zs-barbershop.vercel.app/` (also `/services`, `/barbers`). All three
pages are at **100/100/100** Lighthouse (A11y/BP/SEO) and **96–98** Performance
(up from 74–85, thanks to WebP heroes). A branded 4-page **Founder Handoff PDF**
(`docs/showcase/founder-handoff.pdf`) was built and is being forwarded to Z.

**Where the next session picks up: awaiting Z's editorial feedback.** Nothing
new should ship to the site until Z responds, because the next queued items
(testimonials re-layout, real reviews) are gated on his input. The
custom domain `zsbarbershop.com` is **bought (Cloudflare) but deliberately NOT
attached to Vercel** — it stays out of production until Z approves the site.

## First actions on the other machine

### macOS (MacBook)
```zsh
cd "$HOME/Code Projects/clients/zs-barbershop"
git pull origin main
python3 -m http.server 8000 &
open http://localhost:8000/prototype/index.html
# Live preview (already deployed): https://zs-barbershop.vercel.app/
```

### Windows (FalconXtreme)
```powershell
cd "E:\Code Projects\clients\zs-barbershop"
git pull origin main
python -m http.server 8000
# In another terminal:
start http://localhost:8000/prototype/index.html
# Live preview (already deployed): https://zs-barbershop.vercel.app/
```

## Recreate local-only files

No local-only files required for site work this session. Notes:

- **Vercel CLI auth** — already present on PC at
  `C:/Users/Trader/AppData/Roaming/com.vercel.cli/Data/auth.json`. The project is
  linked (a `.vercel/` dir exists locally, gitignored). Redeploy with
  `vercel --prod` from the repo root. Do NOT add the custom domain.
- `~/.claude.json` `GEMINI_API_KEY` — present on both machines; not used this
  session. (Rotation of the exposed key is still an open hygiene item, deprioritized
  by Joel.)

## What's done (this session)

- `e02d400` — **P2/P3 polish**: body prose eased to weight 500 (medium, more legible
  on dark; hierarchy stays bold); Instagram footer block added to services + barbers
  (parity with index); footer-note inline style moved to `.footer-note` class; 3 hero
  JPEGs converted to WebP via `scripts/webp-heroes.py` (40–53% lighter, perceptually
  lossless), wired with `image-set()` + JPEG fallback, preloads point at WebP.
- `e35e491` — **Vercel routing fix**: removed `cleanUrls` (was 308-redirecting rewrite
  destinations → 404s) and added a `/:path*` catch-all so the pages in `/prototype/`
  resolve their relative refs when served at clean root URLs. Verified live: all
  routes 200, homepage fully styled, zero console errors.
- `7d9c7ab` — **Founder handoff doc**: `docs/showcase/founder-handoff.html` + rendered
  `founder-handoff.pdf` (4 pages, branded). Whitelisted the PDF in `.gitignore`.
- **Deployed** to Vercel production alias `zs-barbershop.vercel.app` (custom domain
  intentionally NOT attached). Lighthouse re-verified live at 100/100/100 + 96–98 perf.
- Showcase log updated (`docs/showcase/client-showcase.md`) with the 2026-05-27 entry.

## What's pending (in order)

1. **Z's editorial feedback (BLOCKER for most below).** Joel forwarded the handoff
   PDF + preview link. Resume when Z responds. His handoff covers: real photos, his
   real bio, confirm prices, Sunday hours, confirm the domain name, and the reviews
   question.
2. **Reviews marquee (PARKED — gated on Z).** The Google listing is unclaimed and shows
   a 5.0 rating with **no written reviews** to scrape; the "169 Google reviews" figure
   isn't reflected on the live listing (may be stale or from Facebook). Yelp has 66 real
   reviews but TOS prohibits republishing + it's not Google. Plan: Z claims his Google
   Business Profile and gathers real reviews, then build the auto-scroll marquee from
   real data. Until then, the 3 placeholder testimonial cards stay as-is. (The site copy
   still says "169 Google reviews" / `aggregateRating` 169 in JSON-LD — correct this to
   the real number once confirmed.)
3. **P2 `/impeccable critique` (DEFERRED — gated on Z).** Re-layout the SaaS-template
   shapes (Why Choose 4-bullet, 3-cell trust strip, 3-card testimonials) into more
   editorial layouts. Held until after Z reacts to the current look (he likes it as-is).
4. **P2 OKLCH conversion** — convert hex tokens in `styles.css` to OKLCH. Invisible,
   future-proofing. Safe to do anytime; low priority.
5. **P3 `/impeccable polish`** — final pass after the above land.
6. **Domain go-live (Stage 2, gated on Z's approval).** `zsbarbershop.com` is bought at
   Cloudflare. When Z approves: attach the domain in Vercel + point Cloudflare DNS
   (see DEPLOY.md Stage 2). Do NOT run prematurely.
7. **Rotate exposed `GEMINI_API_KEY`** — hygiene, deprioritized by Joel.

## Prompt to paste into next Claude Code session

```
I'm resuming Z's Barbershop. Read NEXT_SESSION.md at the repo root for full context.

Quick state: the polish + speed-up pass shipped and is live on a Vercel preview
(https://zs-barbershop.vercel.app/), 100/100/100 + 96-98 perf across all 3 pages.
A branded founder-handoff PDF (docs/showcase/founder-handoff.pdf) was forwarded to
Ziad. We're now AWAITING his editorial feedback — most pending work is gated on it.

Key finding to remember: Z's Google Business Profile is unclaimed and shows no real
written reviews, so the reviews marquee is parked until he claims it + gathers
reviews. The "169 Google reviews" on the site isn't reflected on the live Google
listing and needs correcting to the real number once confirmed.

Hard constraints (also in CLAUDE.md):
- No AI human faces; no hot-towel mentions
- No em dashes in body copy; forbidden words: luxury, esteemed, lounge, distinction
- Commit author: joel.rodriguez@galacticmedical.com (per-commit via git -c)
- Domain zsbarbershop.com is BOUGHT but must NOT be attached to Vercel / go to
  production until Z approves
- Redeploy preview via `vercel --prod`; do NOT add the custom domain
- Design moves that ship → append dated entry to docs/showcase/client-showcase.md

Start by asking me what Z said, before doing any new work.
```

## Hard rules for this project

- **Commit author email:** `joel.rodriguez@galacticmedical.com` (per-commit via `git -c user.email=...`; do NOT change git config).
- **No em dashes in body copy.** Commas, colons, semicolons, middle-dots.
- **No AI-generated human faces.** Silhouettes / hands-only / back-of-head only.
- **No hot-towel mentions.** Ziad doesn't offer it.
- **Mobile-first CSS.**
- **JSON-LD `LocalBusiness` on every page** — preserve it.
- **Default to `/seo *` skills** over hand-rolling SEO checks.
- **Append to `docs/showcase/client-showcase.md`** when a design move ships; render to PDF for milestones.
- **Domain `zsbarbershop.com`: bought but HOLD.** Not attached to Vercel; no DNS pointing at Vercel until Z approves the site.
- **`/book` URL** reserved in `vercel.json`.
- **Pre-deploy gate** on touched prototype HTML: SEO=100, A11y≥95, BP≥95. Currently all 3 pages at 100/100/100, 96–98 perf.
- **Vercel deploys are CLI-based** (`vercel --prod`), not yet wired to GitHub auto-deploy. The `vercel.json` routing relies on a `/:path*` catch-all into `/prototype/`; do not re-add `cleanUrls`.
