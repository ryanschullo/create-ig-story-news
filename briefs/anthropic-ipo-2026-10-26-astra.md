# Anthropic IPO — new editorial design

Export: `exports/anthropic-ipo-2026-10-26-astra.png` (1080 × 1920).
This is a separate design requested after the user switched models, preserving
all substantive facts from the October 26 story and leaving prior exports intact.

## Editorial treatment and source scope

An open ivory editorial composition replaces the former stacked statistic cards.
The official Anthropic wordmark leads into the filing headline; an oversized
terracotta valuation is followed by its estimate qualifier and a separate
same-period revenue comparison. Fine rules, tactile paper, copper and terracotta
computing architecture form the visual treatment. A quiet ivory footer backing
keeps attribution readable against the illustrated foreground.

The source record remains `briefs/anthropic-ipo-2026-10-26.md`:

- SEC Form S-1: https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
- The Guardian: https://www.theguardian.com/technology/2026/oct/26/anthropic-files-listing-stock-market
- Reuters via CNA: https://www.channelnewsasia.com/business/anthropics-soaring-sales-steep-losses-put-ai-frenzy-ipo-test-6493346

The company **filed** for an IPO and **applied** for a Nasdaq listing under the
proposed ticker ANT. It is not presented as already trading or as a completed,
priced IPO. The displayed **$1.5T** is explicitly an estimate from some current
and prospective investors; **IPO price unset** remains visible beside the figure.
The **$16.3B first-half 2026 revenue** compares with **$1.16B first-half 2025**.
No full-year run rate, profit, cash-burn figure or calculated growth rate is added.

## Original assets and scene integration

- Official wordmark: `assets/logos/anthropic-wordmark-original.svg`, placed at
  746 px wide, maintaining its 570:64 proportions. Original SHA-256:
  `eb0f063a7a66a42ca0b1db7696555030d1afe80c63896a594ecdbb90e980cb7d`.
- Original coin: `assets/moneyberg-coin-original.png`, directly rendered at
  **x850–1030, y1170–1350 (180 × 180)**. Its whole rim lies within the upper
  three-quarters. Source SHA-256 remains
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- The original artwork is set in a shallow bronze socket on the front-facing
  generated clay pier. The bevel, inset contact shadow and warm soft-light glaze
  follow the stone scene's lighting. Uniform scaling and non-destructive multiply
  blending preserve the original portrait and inscription; no generated coin or
  retyped lettering is used. The master remains unchanged.
- Background: `assets/anthropic-ipo-background-astra.png`, copied unchanged from
  `/workspace/generated_images/exec-5372fab9-fa34-451c-a1c2-8037ccff7359.png`, created
  with `image_gen.imagegen`. This is decorative editorial illustration, not a
  depiction of an actual Anthropic location or evidence of a business event.
  Background SHA-256:
  `f930e74449a758e20e7b3ca1c722f4879e9c3b8c7e504551bcb3f1d8de046136`.

## Rendering and checks

Renderer: `scripts/render_anthropic_ipo_astra_story.py`.
Template: `assets/layouts/anthropic-ipo-2026-10-26-astra.html`.
Audit: `briefs/anthropic-ipo-2026-10-26-astra-layout.json`.

Chromium typesets authored headlines, labels and figures using actual Lato Black
900, and body copy, estimate qualifiers and sources with actual Georgia. Browser
platform-font inspection verifies all 16 text elements without fallback. Georgia
is runtime-only and not redistributed. The logo retains its original artwork.

All authored text, four rules/panels and the official logo fit the required
**x104–961, y164–1536** inner news bounds. The original coin occupies its separate
background recess and intersects no news text or logo. No background-production
footer appears. Visual review checked source readability, valuation scope,
comparable revenue periods, physical coin integration and overall spacing.

Output SHA-256:
`b82ac630cc1e7834e000c885b125dcb93bcfd8605166cbb226a644e11aed6429`.

Re-render with the actual local Georgia font:

```sh
python scripts/render_anthropic_ipo_astra_story.py --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```
