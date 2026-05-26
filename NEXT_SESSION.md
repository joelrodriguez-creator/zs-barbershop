# NEXT_SESSION.md

_Last checkpoint: 2026-05-26 on FalconXtreme PC. Switching to fresh Claude context window — see resume prompt at the bottom._

## TL;DR

Z's Barbershop is through **Phase 5b/7-preview — 3 pages built and pushed, copying House of Heritage's design language as closely as legally allowed**. Working state:

- **Direction LOCKED:** A "The House" — but the visual specs were re-extracted directly from HoH's computed CSS:
  - Background **`#191818`** (HoH's actual value; the earlier `#161413` was too warm/brown)
  - Display font **Teko** (was Big Shoulders Display)
  - Body font **Montserrat at weight 700** (was Source Serif 4 at 400)
  - Body color **pure white #ffffff** (was cream)
  - Brass `#c8a35a` for CTAs, icons, eyebrow labels, dividers (NOT cream as earlier draft had it — HoH uses brass for icons)
- **Heritage layer LOCKED:** anchors #1–5 (trilingual welcome / Lebanese cedar mark / heritage-named services / bio language / Damascene 8-point star pattern). **NOT #6 (coffee)** — Ziad doesn't serve coffee.
- **Logo concept LOCKED:** #3 "Type Lockup with Cedar," lowercase "s" (Z's, not Z'S), cream color, Lebanese cedar to the left of the wordmark.
- **3 pages built and pushed:**
  - `prototype/index.html` — homepage with trilingual welcome strip, sticky nav, hero, About, Pricing (6 services with brass monoline SVG icons + "MORE SERVICES →" button), trust strip, Why Choose, 2× Damascene pattern dividers, Testimonials (PLACEHOLDER review text), 4-column footer
  - `prototype/services.html` — HoH-faithful two-column services list, 9 services (Haircut/Kids/Senior/Beard Trim/Cut+Beard/Lebanese Hot-Towel Shave/Line-Up/Father+Son/Eyebrow Threading), original copy, JSON-LD offer catalog
  - `prototype/barbers.html` — 4 thumbnail row + featured-barber card with click-to-swap vanilla JS. Ziad is real; barbers 2/3/4 are placeholders awaiting names + bios + photos
- **`prototype/styles.css`** extracted and shared by all 3 pages
- **`vercel.json`** updated: `/services`, `/barbers`, `/our-barbers`, `/book` all routed
- **BRAND.md fully refreshed** with HoH-extracted specs

## Open items (where the next session picks up)

1. **Icons need a redesign pass via Nano Banana 2.** Joel called the current SVG icons "absolutely hideous" — they're hand-coded brass monoline SVGs and don't compare well to HoH's professional icons. Plan: one icon at a time, **4 variants per icon from Nano Banana 2**, Joel picks one, move to the next. Six total icons: scissors, beard trim, cut+beard combo, hot-towel shave, line-up, kids' cut. **Style prompt should be locked across all 6** so the set hangs together (suggested house prompt below in the resume block).
   - **DO NOT feed HoH's actual icon files into Nano Banana 2 as reference images** — that creates a derivative-work problem. Use text-only prompts.
   - Cost ceiling: ~$0.067/image × 4 variants × 6 icons = **$1.60 total**, under the $5 confirm-with-Joel threshold per global rule.

2. **Real Google reviews need to replace the placeholder testimonials.** The 3 review excerpts on `prototype/index.html` testimonials section are made up. The 5.0 stars / 169 reviews count IS real (from Ziad's Google Business Profile). Pull 3–5 real reviews via Playwright on Ziad's Google Maps listing and update the testimonials section. Keep them short, attribute by reviewer's first name as shown on Google, link "Read all 169 reviews →" to the Google listing.

3. **Phase 6 — atmospheric placeholder imagery** for hero, About storefront slot, and Meet-Ziad photo slot. Nano Banana 2, no human faces (hard rule from BRAND.md), atmospheric/interior leaning. Currently all three slots are CSS-gradient placeholders.

4. **Three barber names + bios + photos** for `barbers.html`. Ziad knows the other three but Joel hasn't relayed the info yet.

5. **Domain purchase** — `zsbarbershop.com` on Cloudflare Registrar (~$10/yr). Joel was deciding whether to lock it early or wait. Not blocking site work.

6. Phases 8–10 (Playwright validation, case-study deliverable, Vercel deploy) remain pending.

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

## Prompt to paste into next Claude Code session

Open Claude Code at `E:\Code Projects\clients\zs-barbershop` (Windows) or `~/Code Projects/clients/zs-barbershop` (Mac), pull latest with `git pull origin main`, then paste this:

```
I'm resuming Z's Barbershop in a fresh context window. The project is at
clients/zs-barbershop in this workspace. Read NEXT_SESSION.md at the repo
root FIRST — full state, locked decisions, and pending items are there.

Then open these three local files in my browser so I can see current state:
- prototype/index.html
- prototype/services.html
- prototype/barbers.html

We're at Phase 5b/7-preview. Three pages are built copying House of
Heritage (houseofheritagelv.com) as closely as legally allowed — matching
their functional design specs (background #191818, Teko + Montserrat
fonts from their computed CSS, brass #c8a35a accent) without lifting
any of their copyrighted assets (icon graphics, photographs, verbatim
service descriptions). HoH IS the design anchor; everything we build
references their visual register but with original assets and original
copy for Ziad.

Two open work items, in priority order:

(1) ICONS — Joel called the current hand-coded SVG icons "absolutely
hideous." Replace them via Nano Banana 2, one at a time, 4 variants
each, Joel picks one before moving to the next. The first icon is
HAIRCUT / SCISSORS. Locked style prompt prefix (use this verbatim for
all 6 icons so they hang together):

  "Vintage barbershop pictogram icon, minimalist monoline line drawing,
  single thin clean line in brass gold color (hex #c8a35a) on
  transparent background, centered composition, no shadows, no
  gradients, no fill, simple geometric forms, elegant heritage
  barbershop aesthetic, suitable for a $35 Miami neighborhood
  barbershop website. Square 1:1 aspect ratio."

Then append a subject-specific second sentence per icon:
  1. Haircut — "Open angled barber scissors with finger loops, side view."
  2. Beard Trim — "Stylized mustache and goatee silhouette only, no comb."
  3. Cut + Beard — "Side-profile portrait silhouette of a man's head
     with stylized hair and beard."
  4. Lebanese Hot-Towel Shave — "Folded hot towel with three rising steam
     wisps above it."
  5. Line-Up — "Electric barber clipper, top-down view, with cord."
  6. Kids' Cut — "Smaller side-profile silhouette of a child's head with
     a small star or sparkle accent."

CRITICAL: Do NOT pass HoH's actual icon files as reference inputs to
Nano Banana 2. Use text-only prompts. (This avoids creating derivative
works from their copyrighted graphics.) Cost ceiling for the full set:
$0.067 × 4 variants × 6 icons = ~$1.60 total — under the $5 confirm-with-
Joel threshold. Save outputs to assets/generated/icons/ with names like
haircut-v1.png, haircut-v2.png, etc. After generating 4 variants of icon
1, show me the paths or open the folder so I can pick.

(2) REAL GOOGLE REVIEWS — replace the 3 placeholder testimonial cards on
prototype/index.html. Use Playwright to navigate to Ziad's Google
Business profile (search "Z's Barbershop 8455 SW Bird Rd Miami" on
Google Maps), pull 3–5 real review excerpts with reviewer first names,
keep each short (~2 sentences), update the .review cards. Add a "Read
all 169 reviews on Google →" link below the grid pointing to the Google
listing. The 5.0 stars / 169 reviews count in the section is already
correct — only the placeholder review text needs replacement.

LOCKED (do not revisit unless I bring it up):
- Direction A "The House" — dark cinema, brass on near-black, vintage
  Americana register, Lebanese heritage anchors
- Stack: vanilla HTML + Vercel, no framework
- Background #191818, fonts Teko + Montserrat (extracted from HoH
  computed CSS), body weight 700, body color pure white
- Brass #c8a35a — used for CTAs, icons, eyebrow labels, dividers
- Logo concept #3 (Type Lockup with Lebanese Cedar) — cream color,
  lowercase "s" in Z's
- Heritage anchors #1–5: trilingual welcome (English/Spanish/Arabic) /
  Lebanese cedar mark in logo + footer / heritage-named services
  (Lebanese Hot-Towel Shave, Eyebrow Threading) / "Cubans, Lebanese,
  anyone who needs a fade and a story — the door is open" bio line /
  Damascene 8-point star pattern dividers. NOT #6 — Ziad does NOT serve
  coffee, so don't mention "coffee on" anywhere on the site.
- 4 barbers total: Ziad + 3 placeholders. The other 3 names/bios/photos
  TBD from Z.
- All tokens in BRAND.md. Rationale + Phase 7 layout in design-brief.md.
- Workflow reference: ../../infrastructure/web-design-playbook/PLAYBOOK.md

Real shop info: Ziad Dib (Lebanese, Muslim clientele included), 8455 SW
Bird Rd, Miami FL 33155, Westchester neighborhood, phone (786) 281-8181,
Mon-Sat 9 AM - 7:30 PM, $35 cuts, traditional hot-towel-shave specialty,
5.0 stars / 169 Google reviews, no current website, IG @zbarbershop1.

HARD RULES (per BRAND.md voice rules):
- Body copy: no em dashes (use commas/colons/semicolons)
- No "luxury" / "esteemed" / "lounge" / "distinction" — Z's pricing is
  mid-market $35, copy should match
- No human faces in Nano Banana 2 imagery (the model can't synthesize
  real people; faces come from real photography later)
- Commit author email is joel.rodriguez@galacticmedical.com (set in
  this repo's git config already for Vercel attribution)

Start with the Haircut/scissors Nano Banana 2 batch.
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
