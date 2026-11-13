# A two-speed holiday

Edition: November 12, 2026, America/Chicago. Category: **CONSUMER SENTIMENT**.

## Reporting and scope

Primary research: [Alvarez & Marsal Consumer and Retail Group — Fall 2026 Consumer Sentiment Survey](https://alvarezandmarsal-crg.com/insight/consumer-sentiment-survey-fall-2026/).

Release: [FinanceWire company/research press release via Benzinga](https://www.benzinga.com/content/63186477/alvarez-marsal-releases-fall-2026-consumer-sentiment-survey-highlighting-uneven-spending-recovery), published November 12 at 09:08:40 Eastern / 08:08:40 America/Chicago. This is primary survey research and a company release, not an independently measured retail-sales report.

The complete primary survey page and release were read. Survey fieldwork was in **late August and early September 2026**, among **over 2,000 U.S. adult consumers**. Respondents matched the U.S. adult population by gender, age, ethnicity, region and income.

- Household income **above $100,000**: **+18% net-more** total holiday spending intent.
- Household income **below $100,000**: **−26% net-more** total holiday spending intent.
- Definition: share planning to spend more **minus** share planning to spend less this holiday season compared with last year.
- These are **net respondent balances**, not changes in dollar spending, actual sales, a percentage of all shoppers planning more, or a forecast of retail-sales growth.
- Overall holiday intent was −14% net-more; omitted from the graphic to keep the two-income-group comparison clear and readable. The survey's separate overall all-category spending-intent metric is not used.
- The income boundaries retain the source's strict above/below $100K definitions; no inclusive boundary is invented.

## Final copy

MONEYBERG NEWS BRIEF
CONSUMER SENTIMENT
NOVEMBER 12, 2026

**A TWO-SPEED HOLIDAY**

Holiday shopping plans diverge sharply by household income.

NET HOLIDAY SPENDING INTENT

| Household income | Net balance |
| --- | --- |
| ABOVE $100K | +18% |
| BELOW $100K | −26% |

Net share planning to spend more vs. less than last holiday season.
Intentions, not changes in dollars spent.

Source: Alvarez & Marsal
Survey: late Aug.–early Sept. 2026
2,000+ U.S. adults • Released Nov. 12

## Original charts

Downloaded original images remain byte-for-byte unchanged. Both full artworks preserve their original data, fonts, labels, backgrounds, dimensions and aspect ratios.

- Income split: [original source PNG](https://alvarezandmarsal-crg.com/wp-content/uploads/2026/11/10-Consumer-Sentiment-Survey-fall-2026.png), archived at `assets/source-charts/holiday-spending-divide-2026-11-12-income.png`, **1847 × 1080**, **186198 bytes**, SHA-256 `0d7ab750d0fc39ddb7a31365ff5dbed54b566b0149fb243267c0ee851f244ab5`.
- Overall: [original source PNG](https://alvarezandmarsal-crg.com/wp-content/uploads/2026/11/09-Consumer-Sentiment-Survey-fall-2026.png), archived at `assets/source-charts/holiday-spending-divide-2026-11-12-overall.png`, **1852 × 1026**, **177975 bytes**, SHA-256 `3c6c649828353fe4815f1f1b76827f22dfc7bc40effc9b7c15b6785b36e51388`.

The 9-row income chart was inspected. Its embedded labels would be roughly 15–19px when scaled to the maximum 857px Story content width. The graphic therefore uses a large, clearly attributed numerical summary and the complete original income chart is supplied separately at full resolution. The original chart is **not** cropped, redrawn or retyped. The summary is not presented as the original chart.

## Design and provenance

- Conceptual warm ivory, burgundy and brass holiday-shopping desktop with wrapped presents, a blank receipt and a leather wallet; not documentary evidence of a real event.
- Generated image used for background only. Exact prompts are retained in `assets/holiday-spending-divide-2026-11-12-background.md`.
- Original gold Moneyberg coin is rendered from the unchanged `assets/moneyberg-coin-original.png` master, SHA-256 `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`. It is uniformly scaled and seated in the generated leather wallet's brass recess with contact shading and matching warm light.
- All authored typography uses actual Lato Black 900 and Georgia 400. Georgia remains a runtime-only dependency; no licensed font bytes are committed.
- Authored text/news panels fit the expanded inner bounds x104–961/y164–1536. Minimum text 33px, body 35px, headline 51px.
- Complete coin rim lies within the upper 75% of the 1080 × 1920 canvas. No news overlap or opaque badge placement.
- No background-production credit appears on the graphic; source, survey period and metric qualifier remain visible.

## Reproduction and checks

Renderer: `scripts/render_holiday_spending_divide_2026_11_12.py`.
HTML: `assets/layouts/holiday-spending-divide-2026-11-12.html`.
Audit: `briefs/holiday-spending-divide-2026-11-12-layout.json`.
Export: `exports/holiday-spending-divide-2026-11-12.png`.

```bash
/tmp/moneyberg-render-venv/bin/python scripts/render_holiday_spending_divide_2026_11_12.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

The renderer validates source-chart hashes and dimensions, actual font files and Chromium platform fonts, exact copy, minimum font sizes, text bounds, text overlap, coin hash/aspect/uncropped full-rim upper-75% bounds, scene-integration shading and final PNG dimensions.

## Completed QA

- Export visually inspected after rendering: large income-group figures, clear net-intent qualifier, readable sources and fieldwork dates, no background image through text, intact original coin fitted inside the upper-right wallet's brass recess.
- PNG dimensions verified **1080 × 1920**; **2,199,325 bytes**; SHA-256 `69deecef34ef700e814a64641d00da41f9752c5d60a81ea50ee921b4d4ac4e8a`.
- All 20 authored text elements and both statistic panels pass bounds/overlap checks; lowest authored content ends at y1507 within the y1536 limit.
- Minimum authored text **33px**, minimum body **35px**, headline **83px**, main figures **123px**; actual Lato and Georgia custom fonts verified through Chromium CDP for every text element.
- Original coin master hash unchanged; uniform **204 × 204px**, bounds **x840–1044/y43–247**, whole rim visible inside the upper 75%; no news content overlaps.
- Both original source-chart files pass exact SHA-256 and dimensions checks; no alterations.
- Both original generation/edit prompts are included in the asset documentation and layout audit. Background provenance is not printed on the Story.

Publication and release-asset verification are handled by the coordinating agent. No commit or push was performed by this child agent.
