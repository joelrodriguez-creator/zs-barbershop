# NEXT_SESSION.md

_Last checkpoint: 2026-05-26 on FalconXtreme (Windows PC). Mac handoff ready._

## TL;DR

Z's Barbershop is now through **Phase 5 — four logo concepts shipped**. Working state:

- **Direction LOCKED:** A "The House" (dark cinema + brass mustard + Big Shoulders Display + Source Serif 4 body + heritage seal logo).
- **Heritage layer LOCKED:** anchors #1–5 (trilingual welcome / Lebanese cedar mark / heritage-named services / bio language / Damascene pattern). **NOT #6** — Ziad doesn't actually serve coffee, decision was: don't misrepresent.
- **BRAND.md fully locked** — palette, type stack, spacing, radius, shadow, heritage anchor copy strings, logo direction, imagery brief, voice rules.
- **`logo-options.html` shipped** — four logo concepts (Arched Seal / Damascene Roundel / Type Lockup with Cedar / Vintage Sign Plate), each at three scales on dark + cream.

**Next action: Joel picks 1 of 4 logo concepts. Then refine the winner (Phase 5b), generate atmospheric imagery (Phase 6), build the 5-page prototype (Phase 7).**

## First actions on the other machine

### macOS (MacBook) — FIRST TIME ONLY (initial clone)

The `clients/` directory and these two new repos don't exist yet on your Mac. The session-start hook only pulls existing repos — it doesn't clone new ones. One-time setup:

```zsh
# Pull latest claude-global-config (includes clients/ category support + hook patches)
cd "~/Code Projects/infrastructure/claude-global-config" && git pull origin main && bash bootstrap.sh

# Create the clients/ workspace directory if it doesn't exist
mkdir -p "~/Code Projects/clients"

# Clone the new web-design-playbook repo
cd "~/Code Projects/infrastructure" && git clone https://github.com/joelrodriguez-creator/web-design-playbook.git

# Clone the Z's Barbershop repo
cd "~/Code Projects/clients" && git clone https://github.com/joelrodriguez-creator/zs-barbershop.git

# Confirm
cd "~/Code Projects/clients/zs-barbershop" && git log --oneline -5
```

After that first-time clone, the auto-sync hook handles everything going forward — just `cd "~/Code Projects/clients/zs-barbershop"` and start a Claude Code session, and pulls happen automatically on session start.

### macOS (MacBook) — RETURNING (already cloned)

```zsh
cd "~/Code Projects/clients/zs-barbershop"
git pull origin main
```

### Windows (FalconXtreme) — RETURNING

```powershell
cd "E:\Code Projects\clients\zs-barbershop"
git pull origin main
```

## What's done (across sessions)

- **Phase 0** — `clients/` workspace category + `infrastructure/web-design-playbook/` repo (PLAYBOOK + EXEMPLARS + README). Hook patches (4 files) for `clients/<repo>` recognition. Pushed to `claude-global-config`.
- **Repo setup** — `joelrodriguez-creator/zs-barbershop` on GitHub. Initial scaffold (README + PRODUCT + BRAND + DEPLOY + NEXT_SESSION + .gitignore + .claude/settings.json + vercel.json).
- **Real shop info** — Ziad Dib, 8455 SW Bird Rd Miami FL, (786) 281-8181, Mon-Sat 9-7:30, \$35 cuts, hot-towel-shave specialty, 5.0 stars / 169 reviews, family-friendly, no existing website. Also Lebanese roots + Muslim clientele in Hispanic Westchester. Captured in PRODUCT.md.
- **Phase 2 — Inspiration** — 6 references scraped + screenshots + annotated markdown + `inspiration.html` side-by-side board. Joel picked **House of Heritage (primary)** + **Huckle (secondary)**.
- **Phase 3 — Direction exploration** — `palette.html` with 3 directions (A The House / B The Storefront / C The Chair) + Heritage Layer section with 6 anchor options. Joel picked **Direction A + heritage anchors #1–5 (NOT #6, no coffee)**.
- **Phase 4 — Tokens locked** — `BRAND.md` fully populated with palette (5 colors + accent-soft + line), type stack (Big Shoulders Display + Source Serif 4 + Inter + Amiri), spacing/radius/shadow scales, voice rules, heritage anchor copy strings, logo direction, imagery brief. `design-brief.md` documents the rationale + Phase 7 home page layout preview.
- **Phase 5 — Logo concepts** — `logo-options.html` with 4 hand-coded inline SVG concepts: Arched Seal / Damascene Roundel / Type Lockup with Cedar / Vintage Sign Plate. Each shown at 3 scales (large 200px / nav 48px / favicon 32px) on dark + cream backgrounds.

## Currently in flight (paused)

- **Phase 5 awaiting Joel's pick.** `logo-options.html` is built and pushed. Joel needs to open it, pick 1 of 4 logo concepts (Arched Seal / Damascene Roundel / Type Lockup with Cedar / Vintage Sign Plate). Then we refine the winner — adjust proportions, fine-tune the cedar silhouette (current cedar SVG path is intentionally a rough first-pass), tighten the lockup.

## What's pending (in priority order, post-pick)

1. **Phase 5b — Logo refinement.** Iterate on the chosen concept until it lands. Adjust cedar silhouette to be more recognizably Lebanese (broad spreading horizontal branches). Tighten proportions. Finalize SVG, save as `assets/logo.svg` + `assets/logo-cream.svg` (light variant for dark-background placements) + favicon variants.
2. **Phase 6 — Imagery.** Nano Banana 2 pass for hero + service teaser + gallery placeholders. Cost-ceiling check first (estimate ≤\$1, confirm if >\$5). No human faces (hard rule). Atmospheric cinematic interior, brass + wood + tools, warm bulb light. Phase 6 saves to `assets/generated/`.
3. **Phase 7 — Prototype build.** 5 HTML pages (`prototype/{index,services,gallery,about,contact}.html`) + `prototype/styles.css` from BRAND.md tokens + JSON-LD `LocalBusiness` on every page + the Damascene pattern band above footer. Bake in the 3 Phase-2 locks (3-column trust strip / sticky phone bar / call-or-text CTA) and all 5 heritage anchors (trilingual welcome strip / cedar in logo+footer / heritage-named services / Ziad's bio with "the door is open" closing / Damascene 8-point star section dividers).
4. **Phase 8 — Playwright validation** on mobile (375x812) + desktop (1440x900). No console errors. `tel:` and `sms:` links resolve. JSON-LD validates at schema.org.
5. **Phase 9 — Case-study HTML** as Joel's gift deliverable to Z. Exportable to PDF via Chrome headless. 9-section structure per Wolosky pattern.
6. **Phase 10 — Vercel deploy** to `zs-barbershop.vercel.app`. HOLD on `zsbarbershop.com` domain purchase (~\$10) and DNS cutover until Z reviews case-study and approves.

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

**If this is your first time touching the project on Mac, do the first-time clone steps above first.** Then in a Claude Code session opened at `~/Code Projects/clients/zs-barbershop/`:

```
I'm resuming Z's Barbershop on my MacBook. Read NEXT_SESSION.md at the
repo root for full context.

Quick state: we're through Phase 5 — four logo concepts shipped in
logo-options.html. I need to pick one of the four (Arched Seal / Damascene
Roundel / Type Lockup with Cedar / Vintage Sign Plate). Please open
logo-options.html in my browser so I can see them side-by-side at three
scales on dark + cream backgrounds.

Once I pick, the next action is Phase 5b — refine the winner (cleaner
cedar silhouette, tighter proportions, finalize SVG + variants).
Then Phase 6 (Nano Banana 2 imagery) → Phase 7 (5-page prototype build) →
Phase 8 (Playwright validation) → Phase 9 (case-study deliverable) →
Phase 10 (Vercel deploy, HOLD domain purchase until Ziad reviews).

Locked already (don't revisit unless I bring it up):
- Direction A "The House" — dark cinema + brass mustard + Big Shoulders
  Display + heritage seal logo with Lebanese cedar
- Heritage anchors #1–5: trilingual welcome / cedar mark / heritage-named
  services / "the door is open" bio language / Damascene pattern accent
- NOT #6 (Z doesn't serve coffee — confirmed)
- All tokens in BRAND.md. Rationale in design-brief.md.

Real shop info: Ziad Dib, 8455 SW Bird Rd Miami FL, (786) 281-8181,
Mon-Sat 9-7:30, $35 cuts, hot-towel-shave specialty, Lebanese roots
with Muslim clientele in Hispanic Westchester.
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
