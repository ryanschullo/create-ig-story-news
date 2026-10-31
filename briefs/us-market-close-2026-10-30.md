# AI sell-off hits Wall Street — October 30, 2026 close

**Category:** STOCK MARKET

**Edition:** October 30, 2026, America/Chicago.

**Export:** `exports/us-market-close-2026-10-30.png`

## User-selected article and verified closing data

Yahoo Finance live coverage, Grace O'Donnell, David Hollerith and Ines Ferré:
https://finance.yahoo.com/markets/live/stock-market-today-friday-october-30-dow-sp-500-nasdaq-amazon-intel-ai-sell-off-191429143.html

Full body read via HTTP 200. Updated October 30 at 4:12 p.m. CDT; live coverage
ended. The 8:09 p.m. UTC / 3:09 p.m. CDT update reports the completed session.
Research archive: `/tmp/market-close-oct30-yahoo.{html,txt}`.

The live article's rounded narrative is internally inconsistent (including
Dow −1.2% and “over 650 points” versus its dated closing quote −1.09% / −572.25).
Therefore the final exact results are taken from the consistent post-close
Reuters report and independently corroborated by AP:

**Reuters**, Stephen Culp and Purvi Agarwal, October 30, 3:23 p.m. CDT,
*Wall Street closes sharply lower as AI cash burn fears spark tech selloff*:
https://finance.yahoo.com/markets/stocks/articles/nasdaq-futures-sink-amazon-intel-114737736.html

**AP**, October 30, 3:21 p.m. CDT, *How major US stock indexes fared Friday*:
https://finance.yahoo.com/markets/stocks/articles/major-us-stock-indexes-fared-202111310.html

Both full bodies fetched via HTTP 200. Archives:
`/tmp/market-close-oct30-reuters.{html,txt}` and
`/tmp/market-close-oct30-ap.{html,txt}`.

| Index | October 30 close | Daily percentage | Point change |
| --- | ---: | ---: | ---: |
| Nasdaq Composite | 25,437.00 | −2.86% | −747.73 |
| S&P 500 | 7,580.07 | −1.82% | −140.32 |
| Dow Jones Industrial Average | 51,770.31 | −1.09% | −572.25 |

- Reuters supplies the exact percentages, closing levels and point changes.
  AP independently matches levels and points, with rounded percentages of
  −2.9%, −1.8% and −1.1%.
- The graphic includes all three indices, their final levels and exact Reuters
  daily percentage changes for the same trading date. Point changes are
  documented here but omitted to keep the image clear.
- Nasdaq is the **Composite**, not Nasdaq-100. “DOW” labels the Dow Jones
  Industrial Average.
- Yahoo's final update and Reuters attribute the sell-off to disappointing
  Amazon/Intel reports and renewed AI-spending concerns, following Alphabet's
  sharp decline the previous day. The graphic preserves this concise focus.
- Monthly changes, intraday company quotes, oil prices and crypto-hack updates
  are omitted rather than mixing observation periods.
- A separate AP BC-Select Stock Indices table is excluded because its Nasdaq
  close is stale and contradicts its own reported session range.

## Exact graphic copy

MONEYBERG NEWS BRIEF

STOCK MARKET

OCTOBER 30, 2026 • CLOSE

AI sell-off hits / Wall Street

Amazon and Intel earnings deepen / worries over AI spending.

NASDAQ COMPOSITE / 25,437.00 / −2.86%

S&P 500 / 7,580.07 / −1.82%

DOW / 51,770.31 / −1.09%

Sources: Yahoo Finance; Reuters

October 30, 2026 • Final close

## Design, provenance and verification

- Subject-specific charcoal, burgundy and warm metal financial trading-desk
  architecture, with a calm dark reading wall and prominent coral daily
  declines. Blank monitors and city architecture are decorative, not evidence
  of a particular venue or fabricated market data.
- Text-free image-tool background:
  `/workspace/generated_images/exec-5b33c3a2-df94-48f3-934e-949580f75ac4.png`,
  copied unchanged to `assets/us-market-close-background-2026-10-30.png`.
- Prompt: `assets/us-market-close-background-2026-10-30-prompt.txt`, also
  retained in renderer and layout audit. No background-production footer.
- Canonical original coin: `assets/moneyberg-coin-original.png`, verified
  SHA-256 `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Exact original artwork, uniformly scaled to **130 × 130 px**, installed in
  the console support's brass seat with warm illumination and contact shading.
  Whole-coin bounds **x=932–1062, y=766–896**, entirely inside the upper 75%
  and clear of all news text. Original portrait, lettering and proportions
  preserved; master unchanged.
- HTML: `assets/layouts/us-market-close-2026-10-30.html`.
- Renderer: `scripts/render_us_market_close_2026_10_30.py`.
- Audit: `briefs/us-market-close-2026-10-30-layout.json`.
- Actual Lato Black 900 and Georgia 400 checked from font-file metadata and
  Chrome's per-node font report. Georgia is runtime-only, not redistributed.
- All **18** authored text nodes meet the **33 px** universal floor; body
  **37 px**, headlines **82 px**, brand **35 px**, index labels **35 px**,
  index levels **48 px**, daily changes **82 px**, sources **33 px**.
- Renderer independently enforces body ≥35 px and headline ≥51 px, all text
  and three separators inside **x=104–961, y=164–1536**, square coin and
  upper-75% placement, no coin/text overlap and no document overflow.
- Sources end above the lower trading-desk scene. Final PNG visually checked
  for legibility, intact coin and correct values.
- Python orchestrates HTML/CSS browser rendering without image pixel editing.

Reproduce:

```sh
python scripts/render_us_market_close_2026_10_30.py --georgia-font /path/to/Georgia.TTF
```

Final PNG **1080 × 1920**, **2,090,280 bytes**.
SHA-256 `ed1dd921750cd784b3e89817efd46288b4d43da0f00f7a4c572d53b0ad9f0afe`.
