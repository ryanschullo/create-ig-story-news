# QQQ shorts surge as SPY shorts fall — October 30, 2026

**Category:** STOCK MARKET

**Edition:** October 30, 2026, America/Chicago.

**Export:** `exports/qqq-spy-short-interest-2026-10-30.png`

## Requested source and metric definitions

The user requested this post as a graphic and explicitly requested its graph:
https://x.com/KobeissiLetter/status/2116271956987154764

The full public post was read from HTTP 200 and retained in
`/tmp/kobeissi-2116271956987154764.{html,txt}`. Published
`2026-10-30T20:52:07Z`, October 30, **3:52 p.m. CDT**.

The Kobeissi Letter reports:

- Short interest in **QQQ**, the Nasdaq-100 ETF, is approximately **82 million
  shares**, its highest since March 2023.
- QQQ short interest rose approximately 18 million shares, **28%**, over the
  post's stated “last several weeks.” That is a percent increase, not a
  percentage-point change. This secondary change is omitted from the graphic
  to leave the original chart large and readable.
- Short interest in **SPY**, the S&P 500 ETF, is approximately **92 million
  shares**, down approximately 30 million since March and near a five-year low.
- The reported metric is outstanding **ETF shares sold short**. It is not
  options contracts, trading volume, dollar notional, or percent of float.
- These are the post's reported figures. Its supplied chart cites Bloomberg;
  this work does not claim direct access to or independent verification of
  Bloomberg's underlying dataset.
- No short-squeeze, sell-off or future-return prediction is added. The original
  chart's annotation about hedge funds remains part of the supplied artwork,
  rather than becoming an independently asserted explanation in added copy.
- This is an ETF-positioning story, not a broad market wrap, so a three-index
  closing-results panel is not included.

## Preserved original chart

Actual media URL embedded in the post HTML:
https://pbs.twimg.com/media/HV6CIShXIAA9Wzc.jpg

- Retrieved normally via HTTP 200, `image/jpeg`.
- Stored unchanged at
  `assets/qqq-spy-short-interest-chart-original-2026-10-30.jpg`.
- Dimensions **1200 × 773**; **132,781 bytes**.
- SHA-256:
  `d89bbf285bab02e53d94e1d35f969357acd86b113abdcdb2e8c26026913811d0`.
- Original title: “Tech's Short Interest Has Risen, SPY's Hasn't.”
- **Blue QQQ uses the left axis**, approximately 40–95 million shares.
  **Black SPY uses the right axis**, approximately 80–190 million shares.
  The lower black trace does not mean SPY has fewer shares sold short.
- The whole image is rendered at the maximum usable **857 px width**, height
  **552.046875 px**, bounds **x=104–961, y=793–1345.046875**. Original
  proportions, title, legend, both axes, annotations and Bloomberg credit are
  preserved without cropping, redrawing, retyping, filtering or invented data.
- Original embedded chart typography is preserved as artwork; the current
  authored-text font minimum applies to the surrounding news copy. The main
  figures, explicit dual-axis note and source are repeated in large authored
  text for clarity.

## Exact added copy

MONEYBERG NEWS BRIEF

STOCK MARKET

OCTOBER 30, 2026

QQQ shorts surge / as SPY shorts fall

Shares sold short

QQQ ~82M / SPY ~92M

QQQ: highest since March 2023.

[Full original chart]

QQQ: left axis • SPY: right axis

Post: The Kobeissi Letter • Oct. 30, 2026

Chart: Bloomberg, via the post

## Design, assets and checks

- Subject-specific midnight navy, indigo and cyan institutional-equities
  architecture. The original chart is the main visual; the background contains
  no invented prices, charts, arrows, logos or trading signals.
- Text-free image-tool background:
  `/workspace/generated_images/exec-30be226a-83e6-4793-bd23-b5ac348a6f59.png`.
- Copied unchanged to
  `assets/qqq-spy-short-interest-background-2026-10-30.png`.
- Prompt: `assets/qqq-spy-short-interest-background-2026-10-30-prompt.txt`,
  also saved in the renderer and audit. Generic illustrative architecture,
  not evidence of a particular exchange venue. No production footer.
- Original coin: `assets/moneyberg-coin-original.png`, verified SHA-256
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Exact original coin is uniformly scaled into the upper-right architectural
  panel's brass mounting recess with compatible cool illumination and contact
  shading. Original portrait, lettering and round proportions preserved.
- Coin **162 × 162 px**, bounds **x=889–1051, y=478–640**, entirely within the
  upper 75% and clear of all news text and the original chart.
- HTML: `assets/layouts/qqq-spy-short-interest-2026-10-30.html`.
- Renderer: `scripts/render_qqq_spy_short_interest_2026_10_30.py`.
- Audit: `briefs/qqq-spy-short-interest-2026-10-30-layout.json`.
- All **12** authored text elements use actual Lato Black 900 or Georgia 400,
  verified from font metadata and Chrome's per-node font report. Georgia is
  runtime-only and not redistributed.
- Brand **35 px**, category/date/axes/source **33 px**, body **35 px**,
  headlines **76 px**, hero figures **64 px**. Renderer enforces current
  minimums of **33 px universal / 35 px body / 51 px headline**.
- All added text and full chart fit inside **x=104–961, y=164–1536**. Source
  glyphs end at y=1488, above the wall's lower seam. No document overflow.
- Original chart hash, natural dimensions, aspect ratio and bounds are
  checked; coin hash, round proportions, upper-75% location and lack of
  text/chart overlap are also checked.
- Python orchestrates HTML/CSS browser screenshots without editing pixels.

Reproduce:

```sh
python scripts/render_qqq_spy_short_interest_2026_10_30.py \
  --georgia-font /path/to/Georgia.TTF
```

Final PNG **1080 × 1920**, **1,790,217 bytes**.
SHA-256 `cb7a05e81d8e26198f3e4c6feb6da89042d4f48af446d35263f55bbc5917fbcd`.
