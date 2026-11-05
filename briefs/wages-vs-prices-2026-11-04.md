# Prices outpace average hourly pay

Category: **JOBS & EMPLOYMENT**. Edition: **November 4, 2026**, America/Chicago (CST, UTC−6).

## User-selected post

https://x.com/KobeissiLetter/status/2118147600847118353

The exact post was publicly readable through ordinary HTTP with status 200. Its complete body states that consumer prices rose **31.3%** and average hourly earnings rose **25.9%** since April 2020, ending in September. Publication metadata is `2026-11-05T01:05:15.000Z`, or **November 4, 2026, 7:05:15 p.m. CST**. The visible X page displays November 5 in UTC; the graphic uses the user's November 4 Chicago date.

The full post also makes an inflation-streak comparison against the Fed's 2% target. That secondary claim is omitted: the Fed's target is defined in terms of PCE inflation, not CPI, and the historical streak was not independently checked. The graphic does not repeat the post's broad claim that every consumer's wage gains were erased. It accurately summarizes the comparison as **“Prices outpace average hourly pay.”**

## Independent primary verification

Both percentages can be reproduced from publicly readable, seasonally adjusted **U.S. Bureau of Labor Statistics series distributed by FRED**. Full series metadata pages and CSV files returned HTTP 200 and were read.

| Series | Definition | April 2020 | September 2026 | Cumulative change | Display |
|---|---|---:|---:|---:|---:|
| CPIAUCSL | CPI-U, all items, U.S. city average; seasonally adjusted; 1982–84=100 | 256.032 | 336.298 | 31.3499875015623% | **+31.3%** |
| CES0500000003 | Average hourly earnings of all employees, total private; seasonally adjusted; dollars per hour | $30.04 | $37.81 | 25.8655126498003% | **+25.9%** |

Formula: `(September 2026 level / April 2020 level − 1) × 100`, computed using the full downloaded endpoint values and decimal arithmetic, then rounded to one decimal. The CPI result is just below 31.35%, correctly rounding to 31.3%. These are **cumulative changes from April 2020 through September 2026**, not annual growth rates, November readings, or changes since January 2020.

Primary links:

- CPI metadata: https://fred.stlouisfed.org/series/CPIAUCSL
- CPI CSV: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2020-04-01&coed=2026-09-01
- Earnings metadata: https://fred.stlouisfed.org/series/CES0500000003
- Earnings CSV: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CES0500000003&cosd=2020-04-01&coed=2026-09-01

The two original CSV responses are preserved unchanged at `assets/data/wages-vs-prices-2026-11-04-cpi.csv` and `assets/data/wages-vs-prices-2026-11-04-earnings.csv`.

- CPI CSV: 1,501 bytes, SHA-256 `16458955fb2b00e866a703fb119122a2f733ecfef41e66f3ff991272c8923c2f`.
- Earnings CSV: 1,357 bytes, SHA-256 `c703f56a11a27764b16bcd79dc211c26a9544c5fd00c505f90421e39fa6b36d0`.

The earnings series covers **private nonfarm employees**, not government workers, all consumers, household income or median pay. It is a changing workforce average, not a fixed panel tracking identical workers. The graphic explicitly labels the population and says both series are seasonally adjusted. The non-seasonally adjusted CPI series produces a different rounded result, so its scope is not substituted.

### Baseline and interpretation limits

The BLS's original [April 2020 employment release](https://www.bls.gov/news.release/archives/empsit_05082020.htm), read through ordinary public access, explains that the pandemic-era rise in average hourly earnings largely reflected substantial job losses among lower-paid workers. This affects the composition of the April 2020 baseline. The historical preliminary $30.01 average differs from the revised FRED $30.04 used here; no data vintages are mixed.

The graphic makes no universal statement about every worker's purchasing power. It does not subtract 25.9 from 31.3 and call the result a real-pay percentage loss. No derived wage gap, inflation-target claim, historical rank or annualized rate is added.

## Attached-chart access limit

The X HTML identifies a chart at `https://pbs.twimg.com/media/HWUsBHbXUAACSdn?format=webp&name=large`, with 1200 × 808 dimensions in page metadata. The actual media request returned **HTTP 403**. A PNG/original-format request also returned 403. No chart bytes were retrieved, and no access restriction was bypassed.

The user did not explicitly request a chart for this post. The finished graphic therefore presents two independently verified textual metrics. It does not reproduce, redraw, crop, trace or invent the unavailable chart. The metadata dimensions are not presented as a verified downloaded image measurement.

Research archives: `/tmp/nov4-kobeissi-2118147/`, including the public X HTML/plain text, FRED metadata and CSV responses, BLS historical context, and `primary-check.md`. Those temporary archives are not permanent repository assets; the essential sources, calculations, limits and unchanged CSV files are preserved in this brief and audit.

## Displayed copy

```text
MONEYBERG NEWS BRIEF
JOBS & EMPLOYMENT
NOVEMBER 4, 2026

Prices outpace
average hourly pay

APRIL 2020–SEPTEMBER 2026

CONSUMER PRICES (CPI)
+31.3%

AVERAGE HOURLY EARNINGS
+25.9%

Earnings cover private nonfarm employees.
Both series seasonally adjusted.

Sources: BLS/FRED; @KobeissiLetter
```

## Design and provenance

Warm ivory, burgundy, muted green and walnut distinguish this household-cost story from the market, oil and options graphics. The background depicts an imagined kitchen/workday setting with ordinary groceries, a notebook and a blank receipt. It is decorative editorial imagery, not documentary photography or evidence about particular purchases. All numerical content is added separately using verified text.

Background generated with the image-generation tool. The original `/workspace/generated_images/exec-09c60644-8a7d-4d91-9ae9-a39ae20f8fb2.png` remains unchanged and is copied to `assets/wages-vs-prices-background-2026-11-04.png`. It is **916 × 1717**, **2,214,990 bytes**, SHA-256 `973e9d72212e85cea52be9bd9917c3bec5279ec3db3c2191d7d9c843db70b59a`. Exact prompt: `assets/wages-vs-prices-background-2026-11-04.md`; also included in the layout audit.

The exact original coin is `assets/moneyberg-coin-original.png`, SHA-256 `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`. It is uniformly scaled into a brass recess in the walnut wall trim, with compatible lighting and contact shading. The master is unchanged; portrait, lettering and circular rim are preserved. Whole coin bounds are **x954–1060, y475–581**, **106 × 106 px**, entirely in the upper 75% and clear of news text.

All 13 authored text nodes and two panels fit inside **x104–961, y164–1536** on a **1080 × 1920** canvas. Actual **Lato Black 900** and **Georgia 400** are verified through font metadata and Chromium's per-node platform-font reporting. No fallback font is used. Georgia is runtime-only and not redistributed.

Type sizes: brand 35 px on one line; category/date/sources 33 px; date window 34 px; headline 83/77 px; metric labels 35 px; figures 112 px; body/qualifiers 35 px. Required minimums are **33 px all authored text / 35 px body / 51 px headlines**. Source text is deliberately placed above the grocery imagery for contrast. No background-production credit appears.

## Rendering and validation

```bash
python scripts/render_wages_vs_prices_2026_11_04.py \
  --georgia-font /path/to/Georgia.TTF
```

The HTML template retains runtime font/asset placeholders. Chromium via Playwright renders the final PNG; Python orchestrates browser rendering without editing image pixels. The renderer checks the original coin hash, natural dimensions, circular aspect, upper-three-quarter placement and text separation; exact required copy and source scope; actual fonts and weights; minimum font sizes; all content/panel bounds; no canvas overflow; background provenance; and final PNG dimensions. It also reads the two preserved CSVs, verifies endpoints, recomputes cumulative changes with decimal arithmetic, and checks that displayed one-decimal values match. The audit records those computations and CSV hashes.

Final export: `exports/wages-vs-prices-2026-11-04.png`, **1080 × 1920**, **2,134,410 bytes**, SHA-256 `7ce23ee2305cd91dbc1419262f160957d17713c668c666b0ead098a41c780ca9`. Visual inspection confirms that the headline, period, figures, population/adjustment qualifications and attribution are readable, and that the original coin is integrated into its wall recess.

## Deliverables

1. `assets/wages-vs-prices-background-2026-11-04.png`
2. `assets/wages-vs-prices-background-2026-11-04.md`
3. `assets/layouts/wages-vs-prices-2026-11-04.html`
4. `assets/data/wages-vs-prices-2026-11-04-cpi.csv`
5. `assets/data/wages-vs-prices-2026-11-04-earnings.csv`
6. `scripts/render_wages_vs_prices_2026_11_04.py`
7. `briefs/wages-vs-prices-2026-11-04.md`
8. `briefs/wages-vs-prices-2026-11-04-layout.json`
9. `exports/wages-vs-prices-2026-11-04.png`
