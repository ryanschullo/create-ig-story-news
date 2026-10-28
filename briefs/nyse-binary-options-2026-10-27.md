# NYSE binary options — October 27, 2026

Category: **OPTIONS INVESTING**.
Final: `exports/nyse-binary-options-2026-10-27.png`, **1080 × 1920**.

## Source and timing

User-selected full public Reuters article, read in full:
https://d2233.cms.socastsrm.com/2026/10/27/nyse-moves-to-bring-all-or-nothing-options-to-stocks-and-company-earnings/

Original Reuters URL:
https://www.reuters.com/legal/government/nyse-moves-bring-all-or-nothing-options-stocks-company-earnings-2026-10-27/

Title: “NYSE moves to bring all-or-nothing options to stocks and company earnings.”
By Laura Matthews; edited by Matthew Lewis.
Published/modified: October 27, 2026, 18:00:58 UTC, or **1:00:58 p.m. CDT**.
The Story uses October 27 in America/Chicago.
Source transcript: `/tmp/nyse-binary-options-2026-10-27.txt`.

## Facts and scope

The story describes **two distinct products at different stages**:

1. **Binary return options**, expected to start trading within days of the
   October 27 report, concern whether a stock or ETF closes above or below a
   specified price. The initial lineup covers **12 underlying securities**,
   including Apple, Nvidia, Tesla and the SPDR S&P 500 ETF Trust. The graphic
   says “EXPECTED WITHIN DAYS”; it does not claim trading has already begun.
2. **A separate binary KPI options proposal** remains **awaiting SEC approval**.
   It would be tied to company metrics such as sales or earnings per share.
   Reuters says these proposed cash-settled, European-style contracts would
   pay **$1 or nothing at expiration**, depending on the specified metric and
   strike level. This payoff is displayed **only inside the separate KPI card**.

The graphic does not apply the KPI payout to the return-options product,
conflate approval with launch, promise profits, quote fabricated contract prices,
or invent a quantitative chart. It is product news, so broad-market index
closing results are not relevant.

## Design and permanent assets

A distinct indigo/plum institutional-exchange treatment uses classical columns,
dark stone, restrained teal and brass. Compact single-line **MONEYBERG NEWS BRIEF**
and separate **OPTIONS INVESTING** badge introduce a three-line headline. Two
contrasting cards explain each product and its status. No background-production
footer appears; Reuters credit and the reporting date remain visible.

The background was created with imagegen and copied unchanged from:
`/workspace/generated_images/exec-33e135e4-9a95-44b0-be3c-6cc164e3ca4d.png`
to `assets/nyse-binary-options-background.png`.
Its natural dimensions are **940 × 1672**; browser proportional cover
fills the final canvas. The architectural scene is a decorative exchange-inspired
illustration, not a documentary photograph of the NYSE. It contains no generated
logos, ticker data or financial chart.

The generation request specified the 1080 × 1920 composition, safe content bounds
x104–961/y164–1536, actual Lato Black 900 and Georgia assignments, compact
MONEYBERG NEWS BRIEF, distinct OPTIONS INVESTING category, and a plain empty
front-facing brass recess entirely above y1440. No coin artwork was generated.

The actual permanent master `assets/moneyberg-coin-original.png` is placed
uniformly at **248 × 248 px**, bounds **x771–1019, y654–902**, inside the
background's circular brass recess. Separate contact shadows and non-destructive
material-light layers integrate it with the stone and brass while preserving
the original portrait, lettering and circular proportions. The master remains
unchanged. All of its rim is within the top 75% of the graphic.

## Verification

- Final PNG: **1080 × 1920**, 2,187,371 bytes.
- All **21 authored text elements and six panels/rules** lie inside the usable
  content bounds. The coin does not overlap news text.
- Font metadata and Chromium platform-font inspection verify actual **Lato Black
  900** and **Georgia** for every authored text element. Georgia is runtime-only,
  not embedded or redistributed in the repository.
- Visual inspection confirms legible headline, independent product statuses,
  source credit and original coin integrated into the brass recess.
- Coin SHA-256: `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Background SHA-256: `0a582d01148e4f9d42ace245d92bc3b21206f6cfc6483c12a31c9173eb11f414`.
- Final PNG SHA-256: `987c59c2d7453dd026291c1e43449ff77f8f0be711c33fdd8812dd3f8b8b6278`.

Template: `assets/layouts/nyse-binary-options-2026-10-27.html`.
Renderer: `scripts/render_nyse_binary_options_story.py`.
Audit: `briefs/nyse-binary-options-2026-10-27-layout.json`.

```sh
python scripts/render_nyse_binary_options_story.py --georgia-font /path/to/Georgia.TTF
```
