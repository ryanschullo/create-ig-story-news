# PCE inflation heats up — October 29, 2026

Category: **FEDERAL RESERVE WATCH**. Edition uses America/Chicago.
Selected article #1 from `briefs/article-options-2026-10-29.md`.

## Verified reporting

Primary: BEA, **Personal Income and Outlays, September 2026**, released
October 29, 2026, 8:30 a.m. EDT / 7:30 a.m. CDT.
https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026

Reuters, Lucia Mutikani, October 29, 7:50 a.m. CDT:
https://d2233.cms.socastsrm.com/2026/10/29/us-inflation-heats-up-in-september-consumer-spending-rises/

Both full bodies read and retained in `/tmp/oct29-macro/pce-bea.*` and
`/tmp/oct29-macro/pce-reuters.*`; independently checked before rendering.

- September headline PCE price inflation was **3.6% year over year**, up
  from **3.4% in August**.
- September core PCE, which excludes food and energy, was **3.1% year over
  year**. Both displayed September percentages are annual comparisons.
- These are the PCE price indexes, not CPI. They are not monthly or
  quarterly annualized rates and do not establish a future Fed decision.
- BEA also reported real consumer spending increased less than 0.1% monthly,
  rounded to 0.0%; that would be described as essentially flat. This secondary
  fact is omitted from the graphic to protect readability.

## Graphic copy

MONEYBERG NEWS BRIEF

FEDERAL RESERVE WATCH

OCTOBER 29, 2026

Inflation / heats up

3.6%

HEADLINE PCE · SEPTEMBER 2026

U.S. inflation · Year over year

Up from 3.4% in August.

3.1% / CORE PCE

Excludes food and energy · Year over year

Source: BEA · September 2026 data

Released October 29, 2026

## Design and assets

- Export: `exports/pce-inflation-2026-10-29.png`, verified 1080 × 1920.
- HTML: `assets/layouts/pce-inflation-2026-10-29.html`.
- Renderer: `scripts/render_pce_inflation_2026_10_29.py`.
- Audit: `briefs/pce-inflation-2026-10-29-layout.json`.
- Warm ivory and burgundy grocery-checkout environment relates to everyday
  prices while maintaining a macroeconomic news hierarchy. Decorative
  groceries and blank receipt are not evidence of measured prices.
- Text-free background generated with the image tool and copied unchanged:
  `/workspace/generated_images/exec-4efe6e04-eda1-4f9a-83cc-5e624302a4c7.png`
  → `assets/pce-inflation-background-2026-10-29.png`.
  Exact generation prompt saved in the renderer and audit.
- Original `assets/moneyberg-coin-original.png` is uniformly scaled into the
  burgundy checkout cabinet's brass-lined mount with contact shading and
  compatible warm light. No generated portrait, lettering or replacement logo.
  Master SHA-256 verified:
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Whole coin bounds x=933–1059, y=1040–1166; perfectly square 126 × 126 px.
  Entire rim remains above y=1440 and does not overlap news content.
- The original background is an illustrative retail scene, not a documentary
  photograph. No background-production credit appears on the graphic.

## Current typography and layout verification

- All 14 authored text elements are at least **33 px**. Body is 35–39 px,
  headlines 88 px, hero 198 px. Compact single-line brand is 35 px.
- Actual Lato Black 900 and Georgia 400 files are verified from metadata and
  Chrome's font report for every text node. No fallback or synthetic weight.
  Georgia is runtime-only and not redistributed.
- Explicit role validation enforces headline ≥51 px and body ≥35 px, in
  addition to the 33 px universal floor. Old renderer thresholds were updated.
- Text and all three separator panels fit within x=104–961, y=164–1536.
  Sources sit on clear ivory above the groceries; no clipping or shrinking.
- Final PNG visually inspected against the original coin and source facts.
  Python orchestrates HTML/browser rendering without pixel-editing libraries.

Reproduce:

```sh
python scripts/render_pce_inflation_2026_10_29.py --georgia-font /path/to/Georgia.TTF
```
