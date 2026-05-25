# NEXT_SESSION.md

_Last checkpoint: 2026-05-25 on FalconXtreme (Windows PC)_

## TL;DR

Z's Barbershop is a NEW client website project just scaffolded. The repo, GitHub remote, and standard project docs (README, PRODUCT, BRAND placeholder, DEPLOY, this file) are in place. No HTML pages exist yet. The next active phase is **Phase 2 — inspiration sourcing** from the [`infrastructure/web-design-playbook/PLAYBOOK.md`](../../infrastructure/web-design-playbook/PLAYBOOK.md) 10-phase workflow.

## First actions on the other machine

### macOS (MacBook)
```zsh
cd "~/Code Projects/clients/zs-barbershop"
git pull origin main
```

### Windows (FalconXtreme)
```powershell
cd "E:\Code Projects\clients\zs-barbershop"
git pull origin main
```

## What's done (this session)

- Created `clients/` workspace category and `infrastructure/web-design-playbook/` shared knowledge repo
- Patched session-start + checkpoint-nudge hooks (Mac + PC) to recognize `clients/<repo>`
- Created `joelrodriguez-creator/zs-barbershop` on GitHub
- Scaffolded `clients/zs-barbershop/` with `README.md`, `PRODUCT.md`, `BRAND.md` (placeholder), `DEPLOY.md`, `NEXT_SESSION.md`, `.gitignore`, `.claude/settings.json`, `vercel.json`

## What's pending (in priority order)

### From Joel (next session)

1. **Phase 2 — Inspiration sourcing.** Build `inspiration.html` with 5 reference barbershop sites scraped + annotated. Candidates already identified: Huckle (London), Ilya Barbershop (Tribeca), Bruno's Barbers, Barber & Co (Miami), Assembly Barbershop. Joel picks 1 primary + 1 secondary anchor.
2. **Phase 3 — Direction exploration.** 3 design directions in `palette.html` (Classic Warm Traditional / Modern Minimal Monochrome / Edgy Editorial Bold). Joel picks one. Rationale → `design-brief.md`.
3. **Phase 4 — Palette lock.** Finalize tokens in `BRAND.md`.
4. **Phase 5 — Logo concepts** in `logo-options.html`. Joel picks one, finalize SVG.
5. **Phase 6 — Imagery.** Nano Banana 2 pass for hero / atmospheric / service teaser placeholders. Cost-ceiling check first (estimate ≤$1).
6. **Phase 7 — Prototype build.** 5 HTML pages + styles.css + JSON-LD + vercel.json.
7. **Phase 8 — Playwright validation** on mobile + desktop.
8. **Phase 9 — Case-study HTML** as deliverable.
9. **Phase 10 — Vercel deploy** to `zs-barbershop.vercel.app`. HOLD on domain purchase until Z reviews case-study.

### From Z (owner-supplied content)

✓ Captured from Z's Google Business Profile (2026-05-25):
- Owner: **Ziad Dib** (IG: @zbarbershop1)
- Address: **8455 SW Bird Rd, Miami, FL 33155** (Westchester)
- Phone: **(786) 281-8181**
- Hours: **Mon–Sat 9:00 AM – 7:30 PM** (Sunday TBD)
- Standard cut: **$35**
- Specialty: **Old-school hot-towel shave**
- Reputation: **5.0 stars, 169 Google reviews**
- Family-friendly: yes
- Booking: phone + walk-in (no online platform exists)
- No existing website

Still needed from Z (capture in upcoming session with him):
- Sunday hours (closed? open?)
- Full services + prices (beard trim, line-up, kids', senior, hot-towel shave prices)
- Ziad's bio: years cutting, training, what drew him to it
- Real photos: shop interior, Ziad at work, recent cuts, beard work, hot-towel shave action
- Whether the site should be bilingual / Spanish-friendly (Westchester is heavily Cuban-American)
- Color/vibe preference (will be presented in Phase 3 direction exploration first)
- Whether to add online booking later (Square Appointments / Booksy / Squire), or stay phone-only

## Prompt to paste into next Claude Code session

```
I'm resuming work on Z's Barbershop (clients/zs-barbershop). Read NEXT_SESSION.md
at the repo root for full context. Phase 0 (workspace prep) and the initial
scaffold are done. Next action is Phase 2 — inspiration sourcing — per
infrastructure/web-design-playbook/PLAYBOOK.md.
```

## Hard rules for this project

- **Commit author email:** `joel.rodriguez@galacticmedical.com` (for Vercel Hobby plan attribution — matches Wolosky pattern).
- **No em dashes in body copy.** Use commas, colons, semicolons. (Em dashes fine in markdown headers and signatures.)
- **No AI-generated human faces.** Nano Banana 2 cannot synthesize Z's actual face or real customers. Faces in imagery come from real photography or are skipped.
- **Mobile-first.** Default styles target mobile. `@media (min-width: ...)` for desktop.
- **JSON-LD on every page.** `LocalBusiness` schema with real address, phone, hours, geo, opening hours.
- **Cost-ceiling check on Nano Banana 2.** Estimate from 2–3 sample images first. Confirm with Joel if projected >$5.
- **HOLD domain purchase until Z reviews case-study.** Don't spend the $10 on `zsbarbershop.com` until Z has seen and approved the deliverable.
- **`/book` URL is reserved** in `vercel.json` for a future booking system. Don't repurpose it.
- **Maintenance:** Joel + Claude maintain this indefinitely. Z doesn't need to edit anything.
