# Z's Barbershop — Project-level Claude rules

Augments the global CLAUDE.md + workspace CLAUDE.md for this project. Auto-loaded
into every Claude Code session in this directory.

## Required reads per task type

| When touching... | Read first |
|---|---|
| Any `prototype/*.html` `<head>` block | [SEO.md](SEO.md) |
| Any design token / color / type / spacing | [BRAND.md](BRAND.md) |
| Hero imagery, service icons, photography | [BRAND.md](BRAND.md) §Imagery direction, §Voice |
| Any commit before deploy | [SEO.md](SEO.md) §Pre-launch gate |
| Anything you'd want Ziad to see when reviewing the project | [docs/showcase/client-showcase.md](docs/showcase/client-showcase.md) |

## Hardwired workflow rules

### SEO refinements (hardwired)

- Before editing any `prototype/*.html` `<head>`, read [SEO.md](SEO.md) and apply
  the checklist.
- Tooling installed on this PC (2026-05-26):
  - **claude-seo plugin v2.0.0** — 32 `/seo*` skills at `~/.claude/skills/seo*`
  - **Lighthouse v13.1.0+** — `npm i -g lighthouse`
  - **Unlighthouse** — npx-on-demand, no install
- Pre-deploy gate: run `/seo audit https://zsbarbershop.com` (or per-page
  Lighthouse from SEO.md). Confirm SEO=100, A11y≥95, BP≥95 before any push
  to `main` that touches prototype HTML.
- Items currently missing (status snapshot in SEO.md): canonical links, OG meta,
  Twitter Card meta, BreadcrumbList JSON-LD, LocalBusiness JSON-LD on barbers.html,
  sitemap.xml, robots.txt. Treat these as deploy-blockers, not nice-to-haves.
- When asked to "do SEO" / "audit SEO" / "fix SEO" on this project, prefer the
  `/seo *` skill family over hand-rolling — that's why we installed it.

### Client showcase log (hardwired)

- When a design move ships (icon set, hero image, logo iteration, copy lockdown,
  significant CSS pass, new component), append a dated entry to
  [docs/showcase/client-showcase.md](docs/showcase/client-showcase.md). Capture:
  - What landed (the accepted approach)
  - What got explored and rejected, and why (the editorial avenue)
  - Image references where relevant
- This is the running narrative we show Ziad. When a polished PDF render is
  needed (Z meeting, milestone review), use **Claude Design** to render the
  markdown into a branded PDF (Huashu Design as fallback if CD tokens are tight,
  Open Design if CD credits are blocked — see global CLAUDE.md design-tools matrix).
- The rendered PDF lands at `docs/showcase/client-showcase.pdf` and is committed
  at milestones (gitignore whitelists it).

### Imagery rules

- **No AI-generated human faces.** Ever. Silhouettes / hands-only / back-of-head
  only, never as focal subject.
- **No hot-towel iconography.** Ziad does not offer hot-towel shaves as a
  standalone service. See NEXT_SESSION.md and BRAND.md for the full purge rationale.
- See [BRAND.md](BRAND.md) §Imagery direction for the cinematic dim interior register.

### Voice rules

- No em dashes in body copy. Use commas, colons, semicolons.
- Forbidden words in body copy: "luxury", "esteemed", "lounge", "distinction".
- Heritage is texture, not a sales pitch.

### Commit + deploy rules

- **Commit author:** `joel.rodriguez@galacticmedical.com` (Vercel Hobby attribution).
- **`/book` URL:** Reserved in vercel.json for the future booking system — do not
  wire to anything else.
- **Domain purchase:** HOLD until Ziad reviews the case-study.

### Cost-aware generation

- Nano Banana 2 image gen: ~$0.067 / 1K image, ~$0.151 / 4K. Cost ceiling check
  per global CLAUDE.md: under $5 just run, $5–$50 confirm, >$50 propose splitting.
- Vertex AI Imagen 4 Fast (used for the service icons): ~$0.02 / image.
