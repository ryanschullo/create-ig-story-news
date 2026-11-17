# Nasdaq leads Wall Street lower

**Category:** STOCK MARKET
**Edition:** November 17, 2026
**Observation:** Final U.S. cash-market close, Monday November 16, 2026

## Verified facts

Source: Associated Press, updated November 16, 2026, 16:16 Central.

- Main article: https://apnews.com/article/stocks-markets-ai-nvidia-oil-us-35786b8f539ec95f16ae0500f71cfcc7
- AP follow-up: https://apnews.com/article/stock-markets-ai-earnings-oil-4d5a35288288389d894e63e6bebe8240
- Nasdaq Composite: **−2.5%, close 24,509.76**.
- S&P 500: **−1.9%, close 7,416.59**.
- Dow Jones Industrial Average: **−1.4%, close 51,608.17**.
- Nvidia: **−4.1%**, ahead of November 17 earnings. AI stocks were the largest weights on the broader market, according to AP.

Full article bodies were read. Percentages retain AP's published one-decimal precision. Independently reported point changes are preserved in the source JSON but omitted from the graphic to keep the layout readable. No index values are derived from rounded percentages, and no live/futures quote is substituted. Unrelated personal allegations in the reporting are omitted.

## Design

Original conceptual trading-hall background generated with image_gen: midnight navy and steel blue with crimson semiconductor reflections. The entire original Moneyberg coin is seated within the front-facing architectural wall recess, uniformly scaled with restrained contact shading and matching reflected light. The coin master is unchanged. Its full bounds are **x805–1042, y109–346**, safely within the upper 75% of the canvas and clear of all news copy.

All authored content and four panels fit inside **x104–961, y164–1536**. Typography uses actual **Lato Black 900** and **Georgia 400** files. Authored type is at least 33 px; body is 37–38 px; headline lines are 79 and 66 px. The compact 35 px `MONEYBERG NEWS BRIEF` stays on one line. No background-production credit appears on the graphic.

## Reproduce and audit

```sh
/tmp/nov17-news-venv/bin/python scripts/render_us_market_selloff_2026_11_17.py --georgia-font /tmp/nov17-fonts/Georgia.TTF
```

Georgia is runtime-only and is not redistributed in the repository. Python orchestrates Chromium and checks metadata; it does not edit image pixels. Layout/font checks use actual browser text bounds and platform font inspection.

- Export: `exports/us-market-selloff-2026-11-17.png`
- Canvas: **1080 × 1920 PNG**
- Size: **1,906,586 bytes**
- SHA-256: `aa56c66020802e6a34200ae1e25a503c54fdf4dab4053d8d6ae8a08c296a1d3e`
- Source record: `briefs/us-market-selloff-2026-11-17-source.json`
- Computed layout and font audit: `briefs/us-market-selloff-2026-11-17-layout.json`
- Background provenance and complete generation prompt: `assets/us-market-selloff-2026-11-17-background.md`

Visually inspected the completed PNG for readability, exact original coin appearance, scene integration, date scope, and the three final index panels. Automated checks passed for all 20 text elements, four panels, no overlapping text, whole-coin bounds, exact font families and weights, minimum sizes, and canvas dimensions. Publication and unauthenticated download verification are handled by the parent task after committing the batch.
