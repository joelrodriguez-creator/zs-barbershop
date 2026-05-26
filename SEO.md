# Z's Barbershop — SEO checklist

Hardwired via [CLAUDE.md](CLAUDE.md): read this before editing any
`prototype/*.html` `<head>` block, and run the pre-launch gate before deploying
to a real domain.

## Tooling installed

- **claude-seo plugin v2.0.0** — Claude Code skill family installed at
  `~/.claude/skills/seo*` (PC: 2026-05-26). 32 `/seo*` skills now invokable
  in any Claude Code session, including:
  - `/seo audit <url>` — full-site audit with parallel sub-agents
  - `/seo page <url>` — deep single-page analysis
  - `/seo schema <url>` — detect, validate, and generate Schema.org JSON-LD
  - `/seo geo <url>` — AI search / AI Overviews optimization
  - `/seo local <url>` — Google Business Profile, NAP, local pack
  - `/seo sitemap generate` — XML sitemap generator
  - `/seo image-gen` — OG / social-card image generation (requires Banana
    extension; uses the same `GEMINI_API_KEY` as our `nano-banana-2` MCP)
  - `/seo unlighthouse <url>` — multi-page Lighthouse via Unlighthouse CLI
    (free, runs locally, no API quota)
  - `/seo google setup` — credential wizard for Google APIs (GSC, PageSpeed,
    CrUX, Indexing, GA4)
- **Lighthouse CLI** — `lighthouse` on PATH (PC: v13.1.0+ global npm). Single-page
  audits, used by the pre-launch gate below.
- **Unlighthouse** — no install needed; runs on demand via
  `npx unlighthouse --site <url>` (or via `/seo unlighthouse`).
- **Schema Markup Validator** — https://validator.schema.org/ (web, no install).
- **Rich Results Test** — https://search.google.com/test/rich-results (web).

## Per-page `<head>` requirements

For every `prototype/*.html` page:

- [ ] `<title>` — page-specific, under 60 chars, includes "Z's Barbershop"
- [ ] `<meta name="description">` — 140–160 chars, page-specific, mentions
      "Westchester, Miami" and the primary action verb
- [ ] `<link rel="canonical" href="https://zsbarbershop.com<path>">`
- [ ] Open Graph block:
      - `og:title`, `og:description`, `og:url`, `og:type` (`website`),
        `og:site_name` (`Z's Barbershop`),
        `og:image` (1200×630 hero crop), `og:image:alt`
- [ ] Twitter Card block:
      - `twitter:card` (`summary_large_image`), `twitter:title`,
        `twitter:description`, `twitter:image`
- [ ] Font preconnect to `fonts.googleapis.com` + `fonts.gstatic.com` (already
      present everywhere)
- [ ] `<html lang="en">` (already set)

## Structured data (JSON-LD) per page

- [ ] `LocalBusiness` on EVERY page — currently on `index.html` + `services.html`,
      **MISSING on `barbers.html`**. Includes full address, phone, hours, geo,
      `aggregateRating` 5.0/169.
- [ ] `BreadcrumbList` on every non-home page (services, barbers). Currently
      missing on both.
- [ ] `OfferCatalog` on `services.html` (already present, post-hot-towel-purge).
- [ ] `Person` schema on `barbers.html` for each barber (Ziad first, the 3 others
      once Z names them) — links to barber card via `@id`.

## Site-wide files

- [ ] `sitemap.xml` at repo root, listing index/services/barbers with `lastmod`
      dates and priorities (homepage 1.0, services 0.8, barbers 0.8).
- [ ] `robots.txt` at repo root: `User-agent: *` + `Allow: /` + `Sitemap:` line.
- [ ] Both reachable at production URLs after Vercel deploy — verify
      `vercel.json` rewrites don't shadow them.

## Local SEO (Google Business)

- [ ] NAP (Name, Address, Phone) consistent between site JSON-LD and Google
      Business Profile.
- [ ] Google Business Profile claimed + verified by Ziad.
- [ ] Site URL added to GBP.
- [ ] Post-launch: submit `https://zsbarbershop.com/sitemap.xml` to Google
      Search Console; verify domain ownership via DNS TXT or HTML tag.

## Pre-launch gate

Run before any deploy that touches prototype HTML. Two paths:

### Fast path — claude-seo full-site audit

```
/seo audit https://zsbarbershop.com
```

Spawns up to 15 parallel sub-agents across technical SEO, content quality,
schema, GEO, local, and image optimization. Produces a prioritized action
plan with falsifiability checks per recommendation. Best single-shot
pre-launch verification.

### Manual path — Lighthouse per page

```bash
# Audit each page individually
lighthouse https://zsbarbershop.com/ \
  --only-categories=seo,accessibility,best-practices \
  --output=html --output-path=./lighthouse-index.html \
  --chrome-flags="--headless"

lighthouse https://zsbarbershop.com/services \
  --only-categories=seo,accessibility,best-practices \
  --output=html --output-path=./lighthouse-services.html \
  --chrome-flags="--headless"

lighthouse https://zsbarbershop.com/barbers \
  --only-categories=seo,accessibility,best-practices \
  --output=html --output-path=./lighthouse-barbers.html \
  --chrome-flags="--headless"

# OR: multi-page Lighthouse in one shot
npx unlighthouse --site https://zsbarbershop.com
```

**Targets (gate the deploy):**
- SEO: 100
- Accessibility: ≥95
- Best Practices: ≥95

After Lighthouse passes, paste each page URL into the Schema Markup Validator
and Rich Results Test to confirm structured data is healthy.

## Status snapshot (2026-05-26)

| Item | Status | Notes |
|---|---|---|
| `<title>` per page | Present | Page-specific. |
| `<meta description>` per page | Present | Updated last session. |
| Canonical `<link>` | Missing | Not on any page. |
| Open Graph meta | Missing | Not on any page. |
| Twitter Card meta | Missing | Not on any page. |
| `LocalBusiness` JSON-LD | Partial | index + services. **Missing on barbers.html.** |
| `BreadcrumbList` JSON-LD | Missing | Not on services or barbers. |
| `OfferCatalog` JSON-LD | Present | On services.html, hot-towel-purged. |
| `Person` JSON-LD | Missing | Add to barbers.html when barber list is final. |
| `sitemap.xml` | Missing | DEPLOY.md mentions but nothing generates it. |
| `robots.txt` | Missing | Same. |
| Lighthouse pass | Not run | Pre-launch gate. |
| GBP linked | TBD | Ziad's profile, not on Joel. |

## Reference

- [Schema.org LocalBusiness](https://schema.org/LocalBusiness)
- [Schema.org BarberShop](https://schema.org/BarberShop)
- [Open Graph protocol](https://ogp.me/)
- [Twitter Cards docs](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)
- [Lighthouse SEO scoring](https://developer.chrome.com/docs/lighthouse/seo/)
- [Google Search Central](https://developers.google.com/search)
