# Reported institutional equity-futures positioning — November 13, 2026

## Deliverable and editorial scope

`exports/institutional-equity-futures-2026-11-13.png` is a 1080 × 1920 Instagram Story in **STOCK MARKET**. It shows three figures explicitly attributed to **The Kobeissi Letter**: approximately **$330 billion** of non-dealer net long U.S. equity-index futures positioning, **+$100 billion over six months**, and **second-highest on record**. The visible `KOBEISSI REPORTS` attribution precedes the headline and statistics. A dated news-source credit is retained.

This is futures positioning, not options activity, gross long holdings, cash-equity inflows, or an amount of newly invested cash. It is not a daily market wrap, so a Nasdaq/S&P/Dow close panel is not required. No independent verification of the underlying Goldman Sachs series is claimed.

## Source and timing

- User-selected post: https://x.com/KobeissiLetter/status/2121282186816913716
- Full public post read from saved HTML/text; source agent independently checked the attached chart and timestamp metadata.
- Exact `article:published_time`: **2026-11-13T16:40:59.000Z**, equal to **November 13, 2026, 10:40:59 a.m. CST**. The edition follows America/Chicago.
- The three displayed figures are stated directly in the post. The original attached chart legend defines the metric as **Non-Dealers in US Index Futures ($bn net length)**.
- Complete source investigation: `/tmp/institutional-equity-futures-2026-11-13-source.md`; public-page evidence: `/tmp/kobeissi-2121282186816913716/x.html` and `x.txt`.

## Why the chart is omitted

The attached original Goldman Sachs-credited chart has a visible ending label **9Dec2026**, later than the verified November 13 post and research date. The cause is unresolved. It also appears to exceed $150 billion around 2018, conflicting with the post's claim that positioning never exceeded $150 billion in 2010–2023. The chart's summary values, `Last 329.6` and `High 342.14`, imply a $12.54 billion gap rather than an exact $10 billion gap.

The user did not expressly require a chart in this request. The graphic therefore uses an attributed statistics layout, omits the contradictory historical comparison and peak-gap claim, and does not modify or reproduce the chart's future date label. The rank and six-month change remain attributed statements in the post; the underlying time series and Goldman methodology were not obtained. Targeted corroboration searches did not independently verify the current series.

For provenance only, the source agent archived the unchanged CDN PNG representation at `assets/source-charts/institutional-equity-futures-2026-11-13.png`: **1200 × 724**, **393,460 bytes**, SHA-256 `8c40b0f452dd1f07ac66f2dd84735da9b1044f65366951c35f8d20beceb4d60c`. It is not used by the renderer. Actual posted media was JPEG; do not call the PNG representation the uploader's original PNG.

## Design and asset provenance

The image-generation tool created a new conceptual institutional trading hall in warm ivory limestone, dark teal and antique brass. A quiet stone wall supports the large typography; lower-frame trading desks identify the financial subject without fabricated chart data. This is decorative conceptual imagery, not a photograph of an actual institution or a factual trading event. No background-production footer appears on the Story, per the user's preference.

- Generated background: `assets/institutional-equity-futures-background-2026-11-13.png`.
- Background dimensions: **941 × 1672**; browser-rendered full-canvas background at the verified Story dimensions.
- Background SHA-256: `34f145b8e24321aca3257d37d8336fc379448a94ffb3a2de8e8b0ae76529192b`.
- Original generation output retained at `/workspace/generated_images/exec-778c382c-e17e-4bb5-a5cf-b7f3e7dd5fb1.png`.
- Exact generation prompt and provenance: `assets/institutional-equity-futures-background-2026-11-13.md`.
- Layout: `assets/layouts/institutional-equity-futures-2026-11-13.html`.
- Renderer: `scripts/render_institutional_equity_futures_2026_11_13.py`.
- Machine-readable validation: `briefs/institutional-equity-futures-2026-11-13-layout.json`.

The only coin is the unchanged original `assets/moneyberg-coin-original.png`, 2084 × 2084, SHA-256 `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`. It is seated inside the generated front-facing brass recess with compatible tone, contact shadow and reflected light, not a detached badge. Its exact original portrait and rim lettering remain unmodified; it is uniformly scaled and not clipped or warped. Full rendered bounds are **x=775–969, y=221–415**, entirely within the upper 75%.

## Validation

The background, original coin and completed export were visually inspected with the image-viewing tool. The final image is clear and readable, the circular coin sits inside the physical recess, and no source chart or unsourced quantitative decoration is present.

Chromium/Playwright verified all **14 authored text elements**, the news panel and actual platform fonts. Headlines and labels use the actual **Lato Black 900** file; body, qualifier and source lines use actual **Georgia 400**, supplied at runtime without redistribution. No fallback fonts are used. The smallest authored text is **33 px**; body copy is at least **38 px** and headlines at least **53 px**, exceeding the respective 35/51 px minimums.

All news text and the news panel fit **x=104–961, y=164–1536**. Text does not overlap other text or the coin. The document and export are exactly **1080 × 1920**, without overflow or clipped content. The one-line `MONEYBERG NEWS BRIEF` brand is 35 px. No Python image editing was used; Python only orchestrates HTML/CSS rendering and asset-integrity checks.

Export size: **2,399,507 bytes**. Export SHA-256: **`961fda38f76c5040aaca6b0bb4139dff484032303f979c72d73230e649864592`**.

Reproduce locally:

```sh
/tmp/moneyberg-render-venv/bin/python scripts/render_institutional_equity_futures_2026_11_13.py --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

Publish the reviewed export through `publish-graphic-download.yml`, edition `2026-11-13`, filename `institutional-equity-futures-2026-11-13.png`. Verify the unauthenticated release download's status, attachment filename, dimensions and bytes before delivering its URL.
