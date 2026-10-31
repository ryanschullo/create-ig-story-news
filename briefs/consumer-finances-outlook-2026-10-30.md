# Record financial pessimism — October 30, 2026

**Category:** CONSUMER SENTIMENT

**Edition:** October 30, 2026, America/Chicago

**Export:** `exports/consumer-finances-outlook-2026-10-30.png`

## User request and source

The user requested a graphic of this post **including its original chart**:
https://x.com/KobeissiLetter/status/2116313518911668301

The public X page was fetched directly with HTTP 200. Full post text and
original media references were read; no mirror or screenshot reconstruction
was needed. Research snapshots are `/tmp/kobeissi-2116313518911668301.html`
and `/tmp/kobeissi-2116313518911668301.txt`.

The page's `article:published_time` metadata is
`2026-10-30T23:37:16.000Z`, or **October 30, 6:37:16 p.m. CDT**.

- The Kobeissi Letter reports that **a record 41% of U.S. consumers expect
  their financial situation to worsen over the next 12 months**.
- The post's original chart plots the proportion of Americans expecting
  their financial situation to be worse in a year, with 1960–2026 labels.
- The chart explicitly cites **University of Michigan**. The accessible
  Michigan release did not independently establish this specific series or
  its 41% endpoint; the graphic therefore attributes the report to The
  Kobeissi Letter and says the chart cites Michigan.
- These are personal-finance expectations. They do not establish realized
  losses, a measured recession, or a decline in 41% of households' incomes.
- The post also discusses a five-year horizon, a comparison with Q2 2024,
  and 2008's peak. These secondary claims are omitted from the added copy.
  Original chart annotations remain intact as part of the source artwork.

## Exact graphic copy

MONEYBERG NEWS BRIEF

CONSUMER SENTIMENT

OCTOBER 30, 2026

Record financial / pessimism

41%

of U.S. consumers / expect worse finances / in the next 12 months.

[Full, unchanged original chart]

Source: The Kobeissi Letter • Oct. 30, 2026

Chart cites University of Michigan.

Survey of personal financial expectations.

## Original chart preservation

Original media URL, read from the public post and downloaded HTTP 200:
https://pbs.twimg.com/media/HV4vLBhWoAAjZoa?format=jpg&name=orig

- Asset: `assets/consumer-finances-outlook-chart-original-2026-10-30.jpg`.
- Original **1560 × 1050** JPEG, **138,918 bytes**.
- SHA-256: `2a9aa85774ded27ee424bfd327d65950b5cc98b72311df9f9c58a7db03d40603`.
- The original bytes are preserved, with no redrawing, cropping, retyping,
  changed values, altered colors or removed source credits.
- The chart occupies the **full permitted inner width, 857 px**, with its
  original aspect ratio: bounds **x=104–961, y=752–1328.8125**.
- Original title, axes, percentages, dates, point labels, red emphasis,
  University of Michigan source, TKL mark and follow credit remain visible.
- Embedded chart type is retained as original artwork under the skill's
  original-chart exception; newly authored text meets the current minimums.
  The untouched full-resolution JPEG is also saved for direct inspection.

## Design and validation

- Warm ivory, burgundy, walnut and brass household-budget still life relates
  to consumer finances. The scene is illustrative, not a photograph of survey
  respondents or evidence of financial outcomes.
- Text-free image-tool background:
  `/workspace/generated_images/exec-2eaf6200-e2aa-4274-b422-aa475d2a9234.png`,
  copied unchanged to `assets/consumer-finances-outlook-background-2026-10-30.png`.
- Prompt: `assets/consumer-finances-outlook-background-2026-10-30-prompt.txt`,
  also recorded in the renderer and audit. No production footer appears.
- The exact original coin `assets/moneyberg-coin-original.png` is seated in
  the burgundy cabinet's brass recess with contact shading and compatible
  warm light. Master SHA-256 is verified:
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Coin is uniformly scaled to **172 × 172 px**, bounds **x=895–1067,
  y=249–421**. Entire rim remains in the top 75%, clear of text and chart.
- Layout: `assets/layouts/consumer-finances-outlook-2026-10-30.html`.
- Renderer: `scripts/render_consumer_finances_outlook_2026_10_30.py`.
- Audit: `briefs/consumer-finances-outlook-2026-10-30-layout.json`.
- All 12 authored text nodes use real Lato Black 900 or Georgia 400,
  verified from font metadata and Chrome's per-node font report.
- Brand **35 px**, labels/date/sources **33 px**, body **35 px**, headlines
  **74 px**, hero **146 px**. Renderer enforces **33/35/51 px** minimums.
- All news text and the complete chart are inside **x=104–961,y=164–1536**;
  the source lines are placed on clear ivory. No text, chart or coin overlap.
- Renderer verifies chart bytes, natural dimensions and aspect ratio, original
  coin hash/aspect/placement, font files/roles, content bounds, document
  overflow and the final **1080 × 1920** PNG.
- Georgia is runtime-only, not redistributed. Python orchestrates browser
  rendering and validation without editing image pixels.

Reproduce:

```sh
python scripts/render_consumer_finances_outlook_2026_10_30.py \
  --georgia-font /path/to/Georgia.TTF
```
