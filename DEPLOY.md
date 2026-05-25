# Z's Barbershop — Deploy

## Target architecture

- **Domain:** `zsbarbershop.com` (confirmed available 2026-05-25, NOT yet purchased)
- **Domain registrar:** Cloudflare Registrar (~$10/yr, at-cost pricing)
- **DNS:** Cloudflare-managed
- **Hosting:** Vercel (Hobby plan)
- **Auto-deploy:** on push to `main` (set up via Vercel ↔ GitHub integration)
- **SSL:** auto-provisioned by Vercel
- **Backup domain (if Cloudflare is unavailable):** Porkbun

## Build configuration

| Setting | Value |
|---|---|
| Framework Preset | Other |
| Root Directory | `./` (NOT `prototype/` — Vercel serves the whole repo root) |
| Build Command | _none_ (static site, no build) |
| Output Directory | _none_ (Vercel serves files in-place) |
| Install Command | _none_ |
| Node version | n/a |
| Env vars | none required |

URL rewrites + clean URLs live in `vercel.json` at the repo root.

## Phased deploy plan

### Stage 1 — Vercel preview (happens in Phase 10, doesn't need Z's approval)

1. `gh repo create joelrodriguez-creator/zs-barbershop --public` ✓ (done 2026-05-25)
2. From `clients/zs-barbershop/`:
   ```bash
   vercel link              # link to a new Vercel project named "zs-barbershop"
   vercel --prod            # first deploy
   ```
3. Verify the preview URL: `https://zs-barbershop.vercel.app/`
4. Smoke-test on mobile + desktop. Run Playwright pass per Phase 8.

### Stage 2 — Domain registration + DNS (HOLD until Joel says go)

This stage spends ~$10 and requires Joel's explicit approval before running.

1. Register `zsbarbershop.com` on Cloudflare Registrar:
   - Cloudflare Dashboard → Domain Registration → Search → Register
   - At-cost pricing, no upsells, transfer lock automatic
2. In Cloudflare DNS for `zsbarbershop.com`:
   - Add `A` records for apex (`@`) pointing at Vercel's IP — Vercel publishes the right targets in the project settings after you add the domain
   - Add `CNAME` for `www` → `cname.vercel-dns.com`
   - Proxy status: DNS only (gray cloud), NOT proxied (orange cloud) — Vercel handles SSL
3. In Vercel project settings for `zs-barbershop`:
   - Settings → Domains → Add Domain → `zsbarbershop.com`
   - Settings → Domains → Add Domain → `www.zsbarbershop.com` (set as redirect to apex)
4. Wait for SSL provisioning (~1 minute)
5. Verify `https://zsbarbershop.com/` and `https://www.zsbarbershop.com/` both load and the www version redirects.

### Stage 3 — Post-launch

- Submit `https://zsbarbershop.com/sitemap.xml` to Google Search Console (link Z's Google Business Profile to the search property).
- Verify `LocalBusiness` JSON-LD on the live URL with the [Schema Markup Validator](https://validator.schema.org/).
- Add the live URL to Z's Google Business Profile, Instagram bio, business cards.

## Rollback

If a push breaks the site:
- Vercel → Deployments → previous good deployment → "Promote to Production"
- Then fix on a branch, PR, merge.

The repo is small enough that a `git revert <bad-sha>` + push is also fast.

## Owner content needed before Stage 2

Don't run Stage 2 (domain purchase) until all of these are confirmed:

- [ ] Z confirms `zsbarbershop.com` is the domain he wants
- [ ] Real hours, address, phone are in the site (not placeholders)
- [ ] Real services + prices are in the site
- [ ] Z has reviewed the case-study deliverable doc
- [ ] At least 4 real photos in the gallery (vs Nano Banana 2 placeholders)

Running Stage 2 prematurely means `zsbarbershop.com` resolves to placeholder content, which hurts SEO and looks half-baked.
