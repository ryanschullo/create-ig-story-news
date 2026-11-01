# Consumer spending outpaces income; saving rate at 3.8%

Category: **CONSUMER SENTIMENT**. Edition: **November 1, 2026**, America/Chicago. All displayed economic figures refer to **September 2026**; the comparison figures are **nominal month-over-month changes**, not annual growth rates.

## Source verification and correction

- User-selected post: [The Kobeissi Letter on X](https://x.com/KobeissiLetter/status/2116630555135517067), published **October 31, 2026, 3:37 p.m. CDT** (`2026-10-31T20:37:04.000Z`). Its full substantive text was read through ordinary public X HTTP and timestamp corroborated through official public syndication.
- Primary data: [BEA — Personal Income and Outlays, September 2026](https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026), released **October 29, 2026, 8:30 a.m. EDT**. Full public [release PDF](https://www.bea.gov/sites/default/files/2026-10/pi0926.pdf) and [historical comparison workbook](https://www.bea.gov/sites/default/files/2026-10/pi0926-hist.xlsx) corroborate the displayed figures.
- Important correction: the post's text says **4.2%**, but its original attached savings chart ends at **3.8%**, agreeing with BEA's September release. The graphic uses **3.8%**. The parent informed the user of this correction.
- The post's **4.1% personal-income / 6.3% spending year-over-year growth** was not independently corroborated in the official release or historical workbook, so it is omitted. The parent informed the user that this graphic uses the verified official **monthly** comparison instead.

Verified September figures:

| Measure | Value | Definition/period |
| --- | --- | --- |
| Consumer spending / personal consumption expenditures | **+0.5%** | Current-dollar, nominal change from August to September 2026 |
| Personal income | **+0.2%** | Current-dollar, nominal change from August to September 2026 |
| Personal saving rate | **3.8%** | Personal saving divided by disposable personal income |
| Saving-rate change | **−0.2 percentage points** | Revised August 4.0% to September 3.8%, same release vintage |
| Historical comparison | **Lowest since October 2022** | Official historical workbook: last lower observation October 2022, 3.6% |

The saving rate measures the flow of new saving relative to disposable income. It does not measure total savings-account balances, wealth, or the fraction of households who save. Do not mix the older August release's 4.1% rate with the revised August 4.0% used in September's release.

BEA also reports PCE inflation **3.6% year over year**. That supports elevated inflation, but the verified release does not establish an all-time price-index high. Therefore the user's “record prices” wording is changed minimally to **“high prices.”** No consumer-credit/debt growth data was supplied, so **“potentially increasing reliance on borrowing”** presents an interpretation rather than claiming a measured increase in borrowing.

Full research note and source archives: `/tmp/consumer-spending-nov1.md`, `/tmp/consumer-spending-nov1/bea-full.txt`, `bea-full.pdf`, `historical.xlsx`, `x-page.txt`, and `chart-original.jpg`. The original chart was checked to resolve the mismatch but is not included; the user requested statistics, not a chart.

## Final graphic copy

**MONEYBERG NEWS BRIEF**
**CONSUMER SENTIMENT**
**NOVEMBER 1, 2026**

**Spending outpaces income growth**

**SEPT. 2026 · MONTH OVER MONTH · NOMINAL**

**SPENDING (PCE): +0.5%**
**PERSONAL INCOME: +0.2%**

**3.8% PERSONAL SAVING RATE**
**−0.2 PERCENTAGE POINTS**
of disposable income

Lowest since October 2022.

Consumer spending continues to outpace income growth, putting pressure on household savings and potentially increasing reliance on borrowing. Elevated inflation and high prices put further pressure on consumer savings.

Source: BEA · Released October 29
Context: The Kobeissi Letter, Oct. 31

## Design and asset provenance

- Distinct overhead home-budget still life: warm ivory blotter, walnut desk rail, burgundy wallet, blank calculator and receipts, house keys and a pen. The scene is decorative and does not show actual balances or financial records.
- Background generated with the image tool and copied unchanged to `assets/consumer-spending-savings-background-2026-11-01.png`. Exact prompt and provenance are in its companion Markdown file.
- Exact approved original coin: `assets/moneyberg-coin-original.png`, 2084 × 2084 PNG, SHA-256 `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`. Uniform scaling and matched light/contact shadows seat it within the brass recess in the wooden desk rail. No portrait, lettering or circular rim is redrawn; master remains unchanged.
- Whole original coin bounds: **x935–1073, y963–1101**, entirely inside the canvas and upper three-quarters, clear of news text.
- Final export is **1080 × 1920**. All authored news content/panels fit within **x104–961, y164–1536**. The original coin and other background decoration can extend beyond those inner news bounds.
- Actual Lato Black 900 and Georgia 400 verified from file metadata and Chromium rendered-font reports. Brand 35 px; category 34 px; date/labels/period/source 33 px; headline 69 px; monthly figures 88 px; saving-rate hero 133 px; body and historical note 35 px. No authored text falls below its current minimum.
- Georgia is runtime-only, not embedded in committed HTML or redistributed. The export contains readable news attribution and dates, without a background-production footer.

## Reproduction and QA

```bash
python scripts/render_consumer_spending_savings_2026_11_01.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

Renderer validates actual font files and browser fonts, **23 text nodes**, **two panels**, current minimum sizes and complete safe bounds, canvas overflow, PNG dimensions, the coin's exact identity/aspect ratio/upper-three-quarters placement and nonoverlap with text. The audit identifies BEA as the statistical source and records the corrected rate and monthly comparison. Machine-readable results and final SHA-256 are in `briefs/consumer-spending-savings-2026-11-01-layout.json`.

Full-size visual review passed: periods/units, spending versus personal-income distinction, saving-rate denominator and sources are legible; all news content is complete; the original coin fits its physical brass recess. No GitHub publication is claimed in this rendering brief.

## Deliverables

1. `assets/consumer-spending-savings-background-2026-11-01.png`
2. `assets/consumer-spending-savings-background-2026-11-01.md`
3. `assets/layouts/consumer-spending-savings-2026-11-01.html`
4. `scripts/render_consumer_spending_savings_2026_11_01.py`
5. `briefs/consumer-spending-savings-2026-11-01.md`
6. `briefs/consumer-spending-savings-2026-11-01-layout.json`
7. `exports/consumer-spending-savings-2026-11-01.png`
