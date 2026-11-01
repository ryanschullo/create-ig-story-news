# Kalshi's $1B Series G at a $40B post-money valuation

Category: **ENTREPRENEURSHIP**. News-brief edition: **October 31, 2026**, America/Chicago. The funding announcement was **October 29, 2026**, explicitly stated on the graphic.

## Source and verification

- Primary source: [Kalshi News — Building the next-generation financial exchange: Kalshi raises $1 billion at a $40 billion valuation](https://news.kalshi.com/p/kalshi-series-g-40-billion-valuation).
- Verified against the full company announcement, source HTML metadata and embedded FAQ. Publication timestamp: `2026-10-29T17:33:46.925Z`; page updated October 30.
- Kalshi announced a **$1 billion Series G** at a **$40 billion post-money valuation**.
- The round was co-led by **Wellington Management** and **Sequoia Capital**. Their full names were confirmed in the embedded FAQ.
- Planned uses include new products, institutional adoption and international expansion. These are described as plans, not completed product launches.
- No annualized revenue, annualized trading volume, market-share claims, or company operating run rates are included. The brief attributes the funding information to Kalshi's announcement; no independent audit of company figures is implied.
- The edition date is separate from the announcement date. The graphic does not claim Kalshi announced this financing on October 31.

## Final copy

**MONEYBERG NEWS BRIEF**

**ENTREPRENEURSHIP**

**OCTOBER 31, 2026**

**Kalshi reaches**
**$40B**
**POST-MONEY VALUATION**

**$1B Series G**

The prediction-market platform plans new products, institutional adoption and international expansion.

Co-led by Wellington Management and Sequoia Capital.

Source: Kalshi News
Announced October 29, 2026

## Design and provenance

- Bright ivory and cream, chartreuse green and dark forest typography. Fintech/exchange architecture with translucent green glass gives this story a distinct visual treatment.
- The background was generated with the image tool, then copied unchanged to `assets/kalshi-series-g-background-2026-10-31.png`. It is an illustrative environment, not a photograph of Kalshi's offices or evidence of company assets. Exact prompt and provenance are in the corresponding background Markdown file.
- Actual original coin master: `assets/moneyberg-coin-original.png`, 2084 × 2084 PNG, SHA-256 `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`. Uniform scaling retains the original portrait, lettering and circular proportions. Scene lighting and contact shadows integrate it into the generated green/brass mount; the original master is unchanged.
- Coin bounds: **x866–1034, y995–1163**. The whole original coin is inside the upper three-quarters of the canvas and clear of news text.
- All news content and panels fit within **x104–961, y164–1536** on the verified **1080 × 1920** export. The lower cream panel preserves source and co-lead contrast against the glass background.
- Exact Lato Black 900 and Georgia 400 were verified from the files and Chromium's actual rendered-font reports. Brand 35 px; category 34 px; date and sources 33 px; headline 82 px; valuation 190 px; valuation label 41 px; funding 64 px; body 38 px; co-leads 35 px. No authored text is below the minimum.
- Georgia is loaded only at runtime, never embedded in the committed HTML or redistributed. No background-production footer appears on the export.

## Reproduction and QA

```bash
python scripts/render_kalshi_series_g_2026_10_31.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

The renderer verifies font metadata, actual Chromium fonts, all 14 authored text elements and four news panels, current font minima, complete safe bounds, canvas size and absence of overflow, exact original coin hash/dimensions/aspect ratio, coin placement and text separation. Full audit and final PNG hash: `briefs/kalshi-series-g-2026-10-31-layout.json`.

Full-size visual review passed: headline and funding/valuation distinction are clear; source and announcement date are readable; nothing is clipped; the exact original coin sits within the physical mount. Parent review also approved the composition. No GitHub publication is claimed in this rendering brief.

## Deliverables

1. `assets/kalshi-series-g-background-2026-10-31.png`
2. `assets/kalshi-series-g-background-2026-10-31.md`
3. `assets/layouts/kalshi-series-g-2026-10-31.html`
4. `scripts/render_kalshi_series_g_2026_10_31.py`
5. `briefs/kalshi-series-g-2026-10-31.md`
6. `briefs/kalshi-series-g-2026-10-31-layout.json`
7. `exports/kalshi-series-g-2026-10-31.png`
