# Z's Barbershop

Marketing site for Z's Barbershop, a small owner-operated American barbershop. Built as a gift by Joel Rodriguez for his friend Z. Domain: `zsbarbershop.com` (pending registration).

## Features

- 5-page static marketing site: Home, Services, Gallery, About, Contact
- Mobile-first responsive design
- "Call or Text to Book" CTAs (`tel:` and `sms:` links) — no online booking platform today, but the architecture leaves room (`/book` URL reserved in `vercel.json`)
- Contact form for async appointment requests (Formspree or Vercel Forms — TBD in build phase)
- JSON-LD `LocalBusiness` schema on every page for local SEO
- Photography-forward (real photography from Z preferred; Nano Banana 2 gap-fill until then)
- Deployed on Vercel, no build step

## Tech stack

| Layer | Choice |
|---|---|
| Markup | Hand-written HTML5, no framework |
| Styling | Custom CSS with design-token variables |
| Typography | Google Fonts CDN (palette TBD) |
| SEO | JSON-LD `LocalBusiness` + `BreadcrumbList` on every page |
| Hosting | Vercel |
| Domain registrar | Cloudflare Registrar |
| DNS | Cloudflare → CNAME → Vercel |
| Imagery generation | Nano Banana 2 (gap-fill only) |
| Validation | Playwright MCP, mobile + desktop snapshots |

Same stack as `business/wolosky-podiatry-refresh/` — see [`infrastructure/web-design-playbook/PLAYBOOK.md`](../../infrastructure/web-design-playbook/PLAYBOOK.md) for the workflow that produced this pattern.

## Project structure

```
zs-barbershop/
├── README.md
├── PRODUCT.md             # brand register + strategic pillars
├── BRAND.md               # locked design tokens (palette, type, spacing)
├── DEPLOY.md              # domain + hosting plan + cutover checklist
├── NEXT_SESSION.md        # cross-machine handoff
├── design-brief.md        # 3 design direction recommendations (added in Phase 3)
├── inspiration.html       # reference barbershop sites annotated (added in Phase 2)
├── palette.html           # 3 design directions side-by-side (added in Phase 3)
├── logo-options.html      # logo concepts (added in Phase 5)
├── imagery-picker.html    # Nano Banana 2 variant gallery (added in Phase 6)
├── case-study.html        # gift deliverable doc (added in Phase 9)
├── vercel.json            # URL rewrites + cleanUrls
├── prototype/             # the live site (added in Phase 7)
│   ├── index.html
│   ├── services.html
│   ├── gallery.html
│   ├── about.html
│   ├── contact.html
│   └── styles.css
├── inspiration/           # reference site scrapes + screenshots
│   ├── pages/
│   └── screenshots/
└── assets/
    └── generated/         # Nano Banana 2 output
```

## Getting started

This is a pure-static project — no install step, no build.

**Local preview:**
```bash
cd prototype
# any of these works:
python3 -m http.server 8000          # macOS / Linux
python -m http.server 8000           # Windows (if python is on PATH)
npx serve .                          # if you have node
```

Then open `http://localhost:8000/` in a browser.

**Deploy:**
```bash
vercel --prod
```

(Vercel auto-deploys on push to `main` once the project is linked.)

## Project-specific context

- **Owner:** Z (Joel's barber + close friend).
- **Audience:** Local American barbershop walk-ins and call-ahead bookings. Mobile-first matters — most "barbershop near me" searches happen on a phone.
- **No online booking today.** Z handles all booking on his phone. The site has prominent Call/Text CTAs. The `/book` URL is reserved in `vercel.json` for a future booking system (Square Appointments, Booksy, Squire, or a custom form) — when Z chooses one, drop in the embed and update the rewrite.
- **Maintenance:** Joel + Claude maintain this site indefinitely. Z doesn't need to edit anything himself.
- **Owner-supplied content needed before launch:** real hours, address, phone, services + prices, photos of shop + cuts, social handles, Google Business Profile URL. Captured in `NEXT_SESSION.md` as the pending list.

## Related

- Standard workflow this project follows: [`infrastructure/web-design-playbook/PLAYBOOK.md`](../../infrastructure/web-design-playbook/PLAYBOOK.md)
- Closest analog in Joel's portfolio: [`business/wolosky-podiatry-refresh/`](../../business/wolosky-podiatry-refresh/) — same stack, same workflow, different vertical (podiatry, 27 pages).
