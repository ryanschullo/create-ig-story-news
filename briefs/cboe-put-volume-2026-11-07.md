# Cboe put-volume records — November 7, 2026
**Category:** OPTIONS INVESTING
**Production / source-post day:** November 7, 2026, America/Chicago.
**Export:** `exports/cboe-put-volume-2026-11-07.png`.

## Request and verified scope
The user selected https://x.com/KobeissiLetter/status/2119160893950828791 and requested the original chart, focusing on the approximately 7 million 20-day average, the roughly 4 million comparison in 2022, eight of the ten biggest daily readings occurring in 2026, and unprecedented options activity.

Full public X HTML and official syndication metadata were read. The official metadata provides the publication timestamp **2026-11-07T20:11:43Z**, or **2:11:43 p.m. CST November 7**. Its text is truncated; the full public X HTML supplies the complete post.

- Source post: https://x.com/KobeissiLetter/status/2119160893950828791
- Official metadata: https://cdn.syndication.twimg.com/tweet-result?id=2119160893950828791&lang=en&token=0
- Original image: https://pbs.twimg.com/media/HWjFmhEXMAAlk2_.jpg?format=jpg&name=orig
- Primary daily data: https://www.cboe.com/us/options/market_statistics/daily/?dt=2026-11-05

Primary Cboe daily statistics independently confirm **11,225,416 put contracts on November 5**, rounded to **11.23 million** in the source chart. Its “SUM OF ALL PRODUCTS” comprises index puts **6,267,449**, exchange-traded-product puts **2,527,951**, and equity puts **2,430,016**. This is **Cboe put volume across products**, not all U.S. exchanges, equity options alone, dollar exposure, or open interest.

The post says the **20-day average daily put volume** rose to approximately **7 million contracts**, near its highest on record. Its comparison says the 20-day average oscillated around **4 million in 2022**; that is not a precisely measured whole-year mean. The rolling-average and historical-ranking claims are attributed to The Kobeissi Letter; a full historical series was not independently recomputed.

The chart is a ranking of individual daily volumes, not a moving-average time series. The eight 2026 dates and two 2025 dates visually corroborate the user's requested “8 of 10” point. High put volume by itself does not establish net bearish positioning, panic, net put buying, or future price direction. No such claims are added.

## Original chart
Preserved as `assets/cboe-put-volume-chart-original-2026-11-07.jpg`, 1200 × 801, 83,211 bytes.
SHA-256: `6a36dea23a3c5b7c8376cf3f41c5378cad5cfa9d40e320597e7fd3c508dd5bed`.

| Chart date | Million contracts |
| --- | ---: |
| June 26, 2026 | 8.39 |
| March 20, 2026 | 8.52 |
| June 9, 2026 | 8.96 |
| July 17, 2026 | 9.00 |
| October 30, 2026 | 9.25 |
| October 16, 2026 | 9.62 |
| October 10, 2025 | 10.06 |
| June 5, 2026 | 10.18 |
| April 4, 2025 | 10.22 |
| November 5, 2026 | 11.23 |

The source title, axes, labels, dates, red record highlight, creator mark and source footer are unchanged. Full chart is scaled uniformly to 857 × 572.0475 at x104, y845. It is not cropped, redrawn, retyped or distorted. Original embedded fonts are retained.

## Authored copy
- MONEYBERG NEWS BRIEF
- OPTIONS INVESTING
- NOVEMBER 7, 2026
- UNPRECEDENTED
- OPTIONS ACTIVITY
- ~7 MILLION
- Cboe put contracts • 20-day daily average
- Near record highs; around 4 million in 2022.
- 8 OF THE 10 BIGGEST DAYS
- for daily put volume occurred in 2026.
- Source: The Kobeissi Letter, citing Cboe
- Post: Nov. 7 • Record session: Nov. 5

The near-record rolling average and the record individual session are kept distinct.

## Design and reproduction
A text-free fictional trading office uses ink-plum and indigo with restrained teal accents. The original Moneyberg coin is seated in a physical brass wall recess, uniformly scaled, with contact shadow and compatible lighting. The whole coin remains in the top 75% of the canvas and clear of the chart and news copy. Master coin hash:
`4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.

- Background: `assets/cboe-put-volume-background-2026-11-07.png` (916 × 1717, 1,605,937 bytes).
- Background SHA-256: `40938218531cf7c24131634e0115188fe6961cb544edd6eb00c5660d121316c5`.
- Generation/edit prompts: `assets/cboe-put-volume-background-2026-11-07.md`.
- HTML: `assets/layouts/cboe-put-volume-2026-11-07.html`.
- Renderer: `scripts/render_cboe_put_volume_2026_11_07.py`.
- Audit: `briefs/cboe-put-volume-2026-11-07-layout.json`.

Actual Lato Black 900 and Georgia 400 are loaded and checked through the browser. Georgia is runtime-only. Authored minima: 33px all text, 35px body, 51px headlines. Every news element and chart fits x104–961, y164–1536. No background-production credit is shown.

```sh
/tmp/moneyberg-render-venv/bin/python scripts/render_cboe_put_volume_2026_11_07.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

The renderer checks actual font selection, copy, font sizes, overlap, content bounds, complete chart aspect ratio and hash, original coin identity and placement, and PNG format/dimensions. The final result is visually inspected before publication.

Validated output: 1080 × 1920 PNG, 1,242,492 bytes. Twelve authored text elements and two panels passed all checks. Coin is 130 × 130 at x933, y414. Output SHA-256: `6f09e3b23abc8ef9e64850df08b0fb42b6c6fbb37fd9b28fb46d41aad11e06c4`.

## Delivery
https://github.com/ryanschullo/create-ig-story-news/releases/download/stories-2026-11-07/cboe-put-volume-2026-11-07.png

Only after a successful release workflow and anonymous HTTP200 download with attachment disposition, matching bytes and verified 1080 × 1920 dimensions is this URL shared.
