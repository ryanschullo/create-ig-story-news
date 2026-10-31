# Intel's worst day since 1974 — October 30, 2026

**Category:** STOCK MARKET

**Edition:** October 30, 2026, America/Chicago. The reported move is the
completed October 30 trading session.

**Export:** `exports/intel-stock-2026-10-30.png`

## Requested article and verification

Yahoo Finance, Jared Blikre, **Intel stock plunges nearly 29%, its worst day
since 1974**:
https://finance.yahoo.com/markets/article/intel-stock-plunges-nearly-29-its-worst-day-since-1974-205955309.html

Published/modified `2026-10-30T20:59:55Z`, or **October 30, 3:59 p.m. CDT /
4:59 p.m. EDT**. Full body fetched with HTTP 200 and independently refetched.
Local research snapshots: `/tmp/intel-yahoo-2026-10-30.html` and `.txt`.

- Intel shares **closed down nearly 29%** on October 30.
- Yahoo's calculations using Norgate Data closing prices from May 1973 say
  only July 5, 1974 was worse. The graphic retains **worst day since 1974**,
  not an unsupported all-time record.
- The move erased **nearly $140 billion in market value**. This is equity
  market capitalization, not cash spent, an accounting loss or lost revenue.
- Intel's **fourth-quarter revenue forecast** is **$15B–$16B**, versus
  roughly **$17B** expected by analysts. These are forward-looking revenue
  figures, not completed Q4 results.
- Yahoo describes weak PC demand and higher memory prices as pressures on
  the outlook. AI data-center demand is contributing to memory-price pressure.
- The page's dynamic INTC quote shows greater precision, but the graphic uses
  the article's explicit final-session **nearly 29%** rather than importing an
  unverified snapshot into the story.
- Optional PC shipment forecasts, EPS, factory disruption, year-to-date moves
  and government-stake valuation are omitted to protect readability.
- This is a single-company story, not a broad market recap. The separate
  October 30 market graphic carries the three major index results.

## Exact copy

MONEYBERG NEWS BRIEF

STOCK MARKET

OCTOBER 30, 2026

[Official Intel wordmark]

Intel’s worst day / since 1974

SHARES FALL NEARLY / 29%

Nearly $140B in market value erased.

Q4 REVENUE FORECAST

$15B–$16B

vs. ~$17B expected by analysts

Weak PC demand and rising / memory prices weigh on the outlook.

Source: Yahoo Finance • Oct. 30, 2026

## Assets and design

- Official Intel SVG: `assets/logos/intel-wordmark-original.svg`, downloaded
  unchanged from https://www.intel.com/content/dam/logos/intel-header-logo.svg.
- Source HTTP 200, `image/svg+xml`, 2,308 bytes; viewBox `0 0 395.4 155.9`.
- Logo SHA-256:
  `6d81b3bb7b058be27062fda520b5aaf23402db709af3d62d8593a39cad715fca`.
- Logo's official navy and cyan artwork is displayed on a pale placard,
  uniformly scaled to **210 × 82.796875 px**, at **x=140–350,
  y=363–445.796875**. No redrawing or replacement lettering.
- Logo provenance: `assets/logos/intel-wordmark-original.md`.
- Semiconductor-focused midnight navy/cyan/copper background with silicon
  wafer and chip testbed; original Moneyberg coin is physically seated in
  the instrument fixture's brass recess. The background is illustrative,
  not a documentary photograph of Intel facilities.
- Text-free image-tool output:
  `/workspace/generated_images/exec-561ca8e9-c129-492b-a846-7b0bb2e7f18c.png`,
  copied unchanged to `assets/intel-stock-background-2026-10-30.png`.
- Generation prompt: `assets/intel-stock-background-2026-10-30-prompt.txt`,
  also retained in renderer and audit.
- Original coin master: `assets/moneyberg-coin-original.png`, SHA-256
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Coin is uniformly scaled to **182 × 182 px**, bounds **x=869–1051,
  y=630–812**, with matching cool illumination and contact shading.
  Exact portrait and lettering are preserved. Entire coin is above y=1440
  and clear of news content. Master is unmodified.
- No background-production footer appears.

## Layout checks and reproducibility

- HTML: `assets/layouts/intel-stock-2026-10-30.html`.
- Renderer: `scripts/render_intel_stock_2026_10_30.py`.
- Audit: `briefs/intel-stock-2026-10-30-layout.json`.
- All 14 authored text nodes use actual Lato Black 900 or Georgia 400,
  verified through metadata and Chrome's platform-font API.
- Brand 35 px; labels/date/source 33 px; body 35 px; headlines 78 px;
  main figure 184 px; forecast 72 px. Renderer enforces all current
  **33 px global / 35 px body / 51 px headline** minimums.
- Text, logo, placard and separator fit inside **x=104–961, y=164–1536**.
  Source ends at y=1389 on the dark reading wall above the chip imagery.
- Coin and logo hashes, aspect ratios, full placement and loading checked.
  No document overflow or coin/news overlap. Final PNG visually inspected.
- Georgia is runtime-only and not redistributed. Python orchestrates
  browser layout/rendering without editing image pixels.

Reproduce:

```sh
python scripts/render_intel_stock_2026_10_30.py --georgia-font /path/to/Georgia.TTF
```

Final PNG: **1080 × 1920**, **2,067,520 bytes**.
SHA-256: `0bc3ad82d1008e389301c2081f112ab93acd35d6bdec5b40ffd5961f6146e505`.
