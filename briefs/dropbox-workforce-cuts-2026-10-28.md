# Dropbox plans job cuts — October 28, 2026

Category: **JOBS & EMPLOYMENT**. Edition date uses America/Chicago.

## Sources and verification

Primary: Dropbox Form 8-K, filed October 28, 2026, Items 2.05 and 5.02.
https://www.sec.gov/Archives/edgar/data/1467623/000146762326000052/dbx-20261028.htm

Secondary: Reuters, Anhata Rooprai, October 28, 2026, 8:38 a.m. CDT.
https://d2233.cms.socastsrm.com/2026/10/28/dropbox-plans-9-workforce-cut-technology-chief-to-exit/

Both full texts were read. Local research archives: `/tmp/dropbox-8k-sec.html`,
`/tmp/dropbox-8k-sec.txt`, and `/tmp/dropbox-reuters-new.html`.

- Dropbox announced a planned reduction of **approximately 9% of its global
  workforce**. The graphic says “plans” and “about”; no exact headcount is
  inferred from the older December 2025 workforce count.
- The company estimates **$27 million–$33 million in total cash expenditures**,
  primarily severance, benefits and related costs. Those payments include
  prorated bonuses, a portion of which was already accrued. Incremental
  accounting expense is separately estimated at $20 million–$25 million.
  The graphic correctly calls $27M–$33M estimated cash costs, not savings or
  incremental accounting expense.
- CTO **Ali Dasdan is scheduled to leave November 18, 2026**.
- The stated purpose is aligning investments and the team with top product and
  growth priorities. No claim that AI caused the cuts is made.
- These are announced plans and estimates, not a claim that all layoffs or
  payments have already occurred.

## Exact graphic copy

MONEYBERG NEWS BRIEF

JOBS & EMPLOYMENT

OCTOBER 28, 2026

Dropbox plans / job cuts

ABOUT / 9% / of its global workforce

$27M–$33M / Estimated severance / and related cash costs.

CTO Ali Dasdan is also / set to leave November 18.

Source: Dropbox Form 8-K • Oct. 28, 2026

## Artwork and production

- Export: `exports/dropbox-workforce-cuts-2026-10-28.png`, verified 1080 × 1920.
- Editable layout: `assets/layouts/dropbox-workforce-cuts-2026-10-28.html`.
- Renderer: `scripts/render_dropbox_workforce_story.py`.
- Layout and font audit: `briefs/dropbox-workforce-cuts-2026-10-28-layout.json`.
- Background: `assets/dropbox-workforce-background-2026-10-28.png`.
  Generated generic software-office scene, not a documentary image of Dropbox.
  Cobalt architecture, off-white plaster and quiet workstations establish a
  distinct employment-news design. First generation:
  `/workspace/generated_images/exec-6ff8c3b1-817c-4d70-ae38-f308152bd4f4.png`.
  Readability edit removes the left plant from the source area; final background:
  `/workspace/generated_images/exec-9ae34474-accf-4dea-ab98-e6c16e649199.png`.
  Generation prompts are retained in the renderer and layout audit.
- Original official Dropbox mark: `assets/logos/dropbox-mark-original.svg`.
  Downloaded unchanged from a first-party asset linked by Dropbox's website:
  https://fjord.dropboxstatic.com/warp/conversion/dropbox/warp/icons/Dropbox-logo-nav.svg?id=d587e174-e284-42e8-a18c-85c0d8e57e9e
  Discovery: https://www.dropbox.com/branding . Original 34 × 34 viewBox,
  784 bytes, SHA-256
  `e2c05d2a02b18dad5859a63a72199f6a4e2650790c74013aaf9155dd9a9cd4ce`.
- The exact `assets/moneyberg-coin-original.png` is uniformly scaled into the
  front-facing blue office panel's brass recess with contact shading and cool
  surface illumination. Portrait, lettering and circular proportions are
  preserved; the original master is unchanged. Whole coin x=926–1048,
  y=953–1075, completely inside the upper three-quarters and clear of news text.
- All 14 authored text elements and four news panels are inside the inner
  x=104–961, y=164–1536 bounds. Minimum type is 30 px; body 35–39 px, headline
  80 px, one-line brand 32 px. Actual browser fonts verified: Lato Black 900
  and Georgia 400. Georgia is supplied at runtime and is not redistributed.
- Final image visually inspected for text clarity, full source attribution,
  factual qualifiers, original coin integrity and unobstructed content. No
  background-production footer appears.

Reproduce with the original Georgia font installed locally:

```sh
python scripts/render_dropbox_workforce_story.py --georgia-font /path/to/Georgia.TTF
```
