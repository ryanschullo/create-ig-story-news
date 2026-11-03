# Leveraged ETF inflows — November 2, 2026

## Story and scope

- Category: **STOCK MARKET**.
- User-selected source: https://x.com/KobeissiLetter/status/2117410080240898110
- Edition date: **November 2, 2026, America/Chicago**. The public post displays November 3, 2026 at 12:14 a.m. UTC, corresponding to November 2 at 6:14 p.m. CST.
- This is a fund-flow story, not a daily market-close wrap. No unsupported Nasdaq Composite, S&P 500 or Dow closing figures are added.
- The graphic distinguishes the **rolling one-month** U.S. leveraged-ETF flow figure from SOXL's **calendar-October** flow figure. These are not presented as the same period or as a numerator and denominator.

## Source evidence and verification limits

The ordinary public X page returned HTTP 200 and exposed the complete post body and original embedded chart URL. Relevant exact post excerpts:

> US leveraged ETFs have attracted +$15 billion in inflows over the last month, their largest 1-month rolling inflow in at least 2 years.

> The 3x leveraged long Semiconductor ETF, $SOXL, alone attracted +$7.3 billion in October, its largest monthly inflow on record.

The chart is Bloomberg artwork titled **US Leveraged ETF Fund Flows**, with a legend identifying the series as **1-month rolling total leveraged ETF fund flows**. It preserves the original October retail-inflow annotation, negative values, date labels, right-side scale and Bloomberg credits.

Flow amounts and the at-least-two-years comparison are attributed to The Kobeissi Letter and its Bloomberg chart. The underlying subscription dataset and SOXL's monthly flow total were **not independently reconstructed**. The graphic explicitly says “per Kobeissi” for the record comparison and attributes the flows. It does not claim that Direxion independently verified the $7.3 billion figure.

Issuer source:
https://www.direxion.com/product/daily-semiconductor-bull-bear-3x-etfs

The issuer page returned HTTP 200 and states that SOXL seeks daily results, before fees and expenses, equal to 300% of the NYSE Semiconductor Index. Its Daily Target is +300%. It also says that this is a single-day objective and that the fund should not be expected to provide three times the cumulative benchmark return over periods greater than a day. The graphic's “Targets 3× its index’s daily return” retains the daily limitation and describes an objective, not a guaranteed return.

Working source captures, outside the repository:

- /tmp/kobeissi-2117410080240898110/post.html
- /tmp/kobeissi-2117410080240898110/post.txt
- /tmp/kobeissi-2117410080240898110/direxion.html
- /tmp/kobeissi-2117410080240898110/direxion.txt

## Final graphic text

MONEYBERG NEWS BRIEF
STOCK MARKET
NOVEMBER 2, 2026

**Leveraged ETFs draw**
**$15B in one month**

U.S. rolling 1-month net inflows.
Largest in at least 2 years, per Kobeissi.

[Full original Bloomberg chart]

SOXL: $7.3B in October inflows.
Targets 3× its index’s daily return.

Flows: Kobeissi Letter · Chart: Bloomberg
SOXL mandate: Direxion

## Original chart

- Public embedded media: https://pbs.twimg.com/media/HWILagmWMAEjWp2?format=webp&name=large
- Local preserved file: assets/leveraged-etf-inflows-chart-original-2026-11-02.webp
- Original: **697 × 466**, **18,938 bytes**, WebP.
- SHA-256: `a5882b90ebe0e5c90949e657cdd912330006bf3711a906a11e381ef86a74820c`.
- Copied unchanged from the actual publicly embedded image. An initially guessed JPEG/original variant returned HTTP 403; it was not bypassed. The public embed succeeded normally.
- Rendered at x104, y679, width857, height572.96875; full image preserved with no redraw, cropping, recoloring or retyping. Original embedded fonts are retained as source artwork and enlarged by approximately 1.23×.

## Design and original coin

Fresh text-free graphite/amber exchange architecture and a semiconductor/trading-workstation still life were generated for this subject. This is decorative illustration, not an event photograph or evidence of fund flows. Imagegen was used for the background only. No background-production credit appears on the graphic.

- Background: assets/leveraged-etf-inflows-background-2026-11-02.png
- Background generation prompt: assets/leveraged-etf-inflows-background-2026-11-02.md
- Generated source retained: /workspace/generated_images/exec-3e2fdd3a-41f2-4607-a5b2-aea8690da84a.png
- Background: 941 × 1672, 1,926,802 bytes.
- Background SHA-256: `ed6f73fe6c756fe339e3df27b533ec96eae08b98f1e404e3a15658d0007d13c8`.

The exact original assets/moneyberg-coin-original.png is uniformly scaled and installed inside the background's brass-lined mounting recess on the metal exchange column. Surrounding recess/contact shadows and mild CSS lighting/tone treatment integrate it into the surface. The original portrait and rim lettering remain unchanged; the master file is not edited or replaced.

- Coin master: 2084 × 2084, 1,538,597 bytes.
- Master SHA-256: `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Rendered coin bounds: **x917–1059, y364–506**, 142 × 142.
- Entire circular coin is within the top three-quarters of the canvas and clear of all news text and the chart.

## Rendering and validation

- HTML template: assets/layouts/leveraged-etf-inflows-2026-11-02.html
- Renderer: scripts/render_leveraged_etf_inflows_2026_11_02.py
- Audit: briefs/leveraged-etf-inflows-2026-11-02-layout.json
- Export: exports/leveraged-etf-inflows-2026-11-02.png

Reproduce with:

```bash
python scripts/render_leveraged_etf_inflows_2026_11_02.py --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

The Georgia font is provided at runtime; its bytes are not redistributed in the committed HTML or other files. Python orchestrates the browser and verifies metadata; it does not edit image pixels.

Chromium/Playwright checks passed:

- PNG dimensions exactly **1080 × 1920**.
- All news text and panels within **x104–961, y164–1536**; no content clipped.
- Eleven authored text elements: brand35px, category/date33px, headlines66/76px, body35px and sources33px.
- Actual Lato Black weight900 and Georgia weight400 verified through font metadata and browser platform-font reporting; no fallback.
- Source chart aspect ratio and SHA-256 preserved; title, legend, axes, dates and credits visible.
- Entire original coin within y0–1440, circular, no overlap with news content, and recess/contact shading present.
- Visual inspection confirmed readable copy, full chart, integrated original coin and unobstructed sources.
- Parent agent independently reviewed the exported PNG and approved its visual layout.

Final PNG: **1,546,246 bytes**.
SHA-256: `bd866c1a26162e54f7d3cd6c62dd5d548622d51318015096f54e9e188d477ba7`.

No unrelated historical export or existing coin master was changed. Publication is handled by the parent task.
