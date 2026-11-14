# Reported institutional equity-futures positioning — November 13, 2026

## Deliverable and editorial scope

`exports/institutional-equity-futures-2026-11-13.png` is a 1080 × 1920 Instagram Story in **STOCK MARKET**, revised to follow the user's instruction to always include available charts on Kobeissi stories. It shows two figures explicitly attributed to **The Kobeissi Letter**: approximately **$330 billion** of non-dealer net long U.S. equity-index futures positioning and **+$100 billion over six months**. The visible `KOBEISSI REPORTS` attribution precedes the headline and statistics. The complete original attached chart is included unchanged, with a clear visible note about its date conflict. The optional second-highest ranking is omitted to provide space for the chart and readable qualifications.

This is futures positioning, not options activity, gross long holdings, cash-equity inflows, or an amount of newly invested cash. It is not a daily market wrap, so a Nasdaq/S&P/Dow close panel is not required. No independent verification of the underlying Goldman Sachs series is claimed.

## Source and timing

- User-selected post: https://x.com/KobeissiLetter/status/2121282186816913716
- Full public post read from saved HTML/text; source agent independently checked the attached chart and timestamp metadata.
- Exact `article:published_time`: **2026-11-13T16:40:59.000Z**, equal to **November 13, 2026, 10:40:59 a.m. CST**. The edition follows America/Chicago.
- Both displayed figures are stated directly in the post. The original attached chart legend defines the metric as **Non-Dealers in US Index Futures ($bn net length)**.
- Complete source investigation: `/tmp/institutional-equity-futures-2026-11-13-source.md`; public-page evidence: `/tmp/kobeissi-2121282186816913716/x.html` and `x.txt`.

## Original chart and visible date qualification

The attached original Goldman Sachs-credited chart has a visible ending label **9Dec2026**, later than the verified November 13 post and research date. The cause is unresolved. It also appears to exceed $150 billion around 2018, conflicting with the post's claim that positioning never exceeded $150 billion in 2010–2023. The chart's summary values, `Last 329.6` and `High 342.14`, imply a $12.54 billion gap rather than an exact $10 billion gap.

The user's subsequent instruction expressly requires available charts on Kobeissi stories. The revision therefore reproduces the complete original chart without changing any date, data or label. Directly below it, readable Georgia text states **“Chart label: Dec. 9, 2026; post: Nov. 13.”** and **“Chart observation date unverified.”** The full November 13, 2026 edition date remains at the top. This preserves the source artwork while making the unresolved mismatch visible; it does not present the chart as an independently verified November 13 observation.

The graphic still omits the contradictory 2010–2023 historical comparison and exact peak-gap claim. The six-month change remains an attributed statement in the post; the underlying time series and Goldman methodology were not obtained. Targeted corroboration searches did not independently verify the current series.

The unchanged CDN PNG representation is `assets/source-charts/institutional-equity-futures-2026-11-13.png`: **1200 × 724**, **393,460 bytes**, SHA-256 `8c40b0f452dd1f07ac66f2dd84735da9b1044f65366951c35f8d20beceb4d60c`. The renderer places the entire image at **x=104–961, y=850–1367.046875**, a proportional **857 × 517.046875** rendering. The full title, axes, date labels, legend, summary table and Goldman Sachs source credit remain intact. No cropping, filters, border radius, redraw, retyping or source-pixel edits are applied. Embedded original-chart typography is preserved as required. Actual posted media was JPEG; the PNG is an unchanged CDN representation, not the uploader's original PNG.

## Design and asset provenance

The image-generation tool created a new conceptual institutional trading hall in warm ivory limestone, dark teal and antique brass, then edited that background for the chart revision to soften the central stone texture. A quiet wall supports the actual source chart and large typography; lower-frame trading desks identify the financial subject without fabricated chart data. The generated environment is decorative conceptual imagery, not a photograph of an actual institution or a factual trading event. No background-production footer appears on the Story, per the user's preference.

- Generated background: `assets/institutional-equity-futures-background-2026-11-13.png`.
- Background dimensions: **941 × 1672**; browser-rendered full-canvas background at the verified Story dimensions.
- Background SHA-256: `32fd0d17848f5b1a72a85c4000439090730f6a8d28f5e1cd0977c4a7e1cb8caf`.
- Final edited background copied unchanged from `/workspace/generated_images/exec-5338f1b1-c7a3-4848-800e-f52661eb31cf.png`; initial output retained at `/workspace/generated_images/exec-778c382c-e17e-4bb5-a5cf-b7f3e7dd5fb1.png`.
- Exact generation and editing prompts and provenance: `assets/institutional-equity-futures-background-2026-11-13.md`.
- Layout: `assets/layouts/institutional-equity-futures-2026-11-13.html`.
- Renderer: `scripts/render_institutional_equity_futures_2026_11_13.py`.
- Machine-readable validation: `briefs/institutional-equity-futures-2026-11-13-layout.json`.

The only coin is the unchanged original `assets/moneyberg-coin-original.png`, 2084 × 2084, SHA-256 `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`. It is seated inside the generated front-facing brass recess with compatible tone, contact shadow and reflected light, not a detached badge. Its exact original portrait and rim lettering remain unmodified; it is uniformly scaled and not clipped or warped. Full rendered bounds are **x=775–969, y=221–415**, entirely within the upper 75%.

## Validation

The edited background, original chart, original coin and completed export were visually inspected. The full original chart is readable at the maximum permitted width, including its title, axes, dates and summary table; its smaller embedded source typography remains untouched. The circular original coin sits inside the physical recess. The date-conflict note is clearly visible below the chart. No generated quantitative decoration is present.

Chromium/Playwright verified all **13 authored text elements**, the complete original chart and actual platform fonts. Headlines and labels use the actual **Lato Black 900** file; body, qualifier and source lines use actual **Georgia 400**, supplied at runtime without redistribution. No fallback fonts are used. The smallest authored text is **33 px**; body copy is **35 px** and headlines are at least **65 px**, meeting the respective 35/51 px minimums. The source chart retains its original embedded fonts rather than being retyped.

All news text and the complete chart fit **x=104–961, y=164–1536**. Text does not overlap other text, the chart or the coin. The chart passes natural-resolution, SHA-256, aspect-ratio, unaltered-style and viewport-boundary checks. The document and export are exactly **1080 × 1920**, without overflow or clipped content. The one-line `MONEYBERG NEWS BRIEF` brand is 35 px. No Python image editing was used; Python only orchestrates HTML/CSS rendering and asset-integrity checks.

Export size: **2,008,102 bytes**. Export SHA-256: **`9d61362ffcb52f7739fb830b1f401e2cd4a4a5bd865ad980f4154bba2baf8bf3`**.

Reproduce locally:

```sh
/tmp/moneyberg-render-venv/bin/python scripts/render_institutional_equity_futures_2026_11_13.py --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

Publish the reviewed export through `publish-graphic-download.yml`, edition `2026-11-13`, filename `institutional-equity-futures-2026-11-13.png`. Verify the unauthenticated release download's status, attachment filename, dimensions and bytes before delivering its URL.
