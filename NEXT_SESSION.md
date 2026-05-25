# NEXT_SESSION.md

_Last checkpoint: 2026-05-25 evening on FalconXtreme (Windows PC). Resuming on MacBook tonight._

## TL;DR

Z's Barbershop project is through **Phase 2 (inspiration) and Phase 3 (direction exploration is BUILT, awaiting Joel's pick)**. Joel already locked his primary anchor = **House of Heritage** and secondary = **Huckle** from Phase 2. He also flagged that Ziad is Lebanese with a strong Muslim clientele, and asked for ways to anchor that heritage inclusively (not exclusively).

`palette.html` is ready to view — it shows three design directions (A "The House" / B "The Storefront" / C "The Chair") plus a "Heritage Layer" section with 6 concrete anchor options (trilingual welcome, Lebanese cedar mark, heritage-named services, bio language, Arabic geometric pattern accent, "have a coffee" hospitality framing).

**Next action on MacBook: open `palette.html` in a browser, pick A/B/C + which heritage anchors to fold in, then I write `BRAND.md` (Phase 4).**

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

- **Phase 0** — Created `clients/` workspace category. Created `infrastructure/web-design-playbook/` repo (PLAYBOOK.md = 10-phase workflow, EXEMPLARS.md = pointers into existing projects, README.md). Patched session-start + checkpoint-nudge hooks (Mac + PC) to recognize `clients/<repo>`. Both commits pushed to `claude-global-config`.
- **Repo setup** — Created `joelrodriguez-creator/zs-barbershop` on GitHub. Local scaffold pushed (README, PRODUCT, BRAND placeholder, DEPLOY, NEXT_SESSION, .gitignore, .claude/settings.json, vercel.json with `/book` reserved).
- **Captured real shop info** from Z's Google Business Profile: Ziad Dib, 8455 SW Bird Rd Miami FL, (786) 281-8181, Mon-Sat 9-7:30, \$35 cuts, hot-towel-shave specialty, 5.0 stars / 169 reviews, family-friendly, no existing website. Committed to PRODUCT.md.
- **Phase 2 — Inspiration sourcing** — 6 references scraped (Huckle / Fruits / Birds / Fresh / THE HOFS / House of Heritage). Each with desktop + mobile screenshots + annotated markdown in `inspiration/pages/*.md`. Side-by-side board in `inspiration.html`. Joel picked **House of Heritage (primary)** + **Huckle (secondary)**.
- **Phase 3 — Direction exploration** — `palette.html` built with 3 directions:
  - **A — The House** (dark cinema + brass mustard + Big Shoulders Display + heritage seal)
  - **B — The Storefront** (cream + deep navy + pole-red + Cinzel serif)
  - **C — The Chair** (cognac + cream + mustard + Alfa Slab One sign-painter)
- **Heritage Layer section in palette.html** — 6 options for anchoring Ziad's Lebanese roots and welcoming his Muslim clientele inclusively (trilingual welcome / Lebanese cedar mark / heritage-named services / bio language / Arabic geometric pattern / "have a coffee" hospitality). Includes a "recommended starter combo" (#1 + #3 + #4, optionally #5 if A wins, always #6).

## Currently in flight (paused)

- **Phase 3 awaiting Joel's pick.** `palette.html` is built and pushed. Joel needs to open it, pick a direction (A / B / C), and pick which heritage anchors (any subset of #1–#6, or the recommended starter combo: #1 + #3 + #4 + #6). The pick gets written into `BRAND.md` in Phase 4.

## What's pending (in priority order, post-pick)

1. **Phase 4 — Palette lock.** Take Joel's A/B/C + heritage anchor picks. Write final tokens (palette, type stack, spacing, radius, shadow) into `BRAND.md`. Document the chosen direction's rationale in `design-brief.md`.
2. **Phase 5 — Logo concepts** in `logo-options.html`. 3–5 concepts in the chosen direction. If heritage anchor #2 (Lebanese cedar mark) was picked, include cedar in the concepts. Joel picks one. Finalize SVG.
3. **Phase 6 — Imagery.** Nano Banana 2 pass for hero + service teaser placeholders. Cost-ceiling check first (estimate ≤\$1, confirm if >\$5). No human faces (rule). Atmospheric/interior-leaning prompts.
4. **Phase 7 — Prototype build.** 5 HTML pages (index, services, gallery, about, contact) + `styles.css` from BRAND.md tokens + JSON-LD `LocalBusiness` on every page + `vercel.json` already-existing. Bake in the 3 Phase-2 locks (3-column trust strip, sticky phone bar, call-or-text CTA). Bake in chosen heritage anchors (trilingual welcome / heritage service names / Ziad's bio / etc.).
5. **Phase 8 — Playwright validation** on mobile (375x812) + desktop (1440x900). No console errors. `tel:` and `sms:` links resolve. JSON-LD validates at schema.org.
6. **Phase 9 — Case-study HTML** as Joel's gift deliverable to Z. Exportable to PDF via Chrome headless.
7. **Phase 10 — Vercel deploy** to `zs-barbershop.vercel.app`. HOLD on `zsbarbershop.com` domain purchase (~\$10) and DNS cutover until Z reviews case-study and approves.

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

## Prompt to paste into next Claude Code session (MacBook)

```
I'm resuming Z's Barbershop on my MacBook. The project is at
~/Code Projects/clients/zs-barbershop/ — pull latest first (git pull origin main).

Read NEXT_SESSION.md at the repo root for full context. Short version: we're
through Phase 2 (inspiration) and Phase 3 is BUILT in palette.html, awaiting
my pick.

Please open palette.html in my browser so I can see the three directions
(A "The House" / B "The Storefront" / C "The Chair") plus the six heritage-
layer options for anchoring Ziad's Lebanese roots inclusively. Then ask me:

  1. Which direction (A / B / C)?
  2. Which heritage anchors (any subset of #1–#6, or the recommended combo)?

Once I answer those, the next action is Phase 4 — lock the chosen tokens
into BRAND.md and write design-brief.md with the rationale. Then we move
on to Phase 5 (logo concepts) through Phase 10 (Vercel deploy) per
infrastructure/web-design-playbook/PLAYBOOK.md.

Real shop info already captured: Ziad Dib, 8455 SW Bird Rd Miami FL,
(786) 281-8181, Mon-Sat 9-7:30, $35 cuts, hot-towel-shave specialty,
Lebanese roots with Muslim clientele in Hispanic Westchester.

Don't change my prior picks (House of Heritage primary + Huckle secondary)
— those are locked. Heritage anchors and A/B/C direction are still open.
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
