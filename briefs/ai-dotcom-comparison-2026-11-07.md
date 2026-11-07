# AI versus dot-com — complete final video frame

**Category:** AI INVESTING
**Production edition:** November 7, 2026, America/Chicago
**Source post:** November 6, 2026, 5:49:37 a.m. CST / 11:49:37 UTC
**AI data through:** November 5, 2026
**Export:** `exports/ai-dotcom-comparison-2026-11-07.png`

## User request

Create a Moneyberg news graphic from the supplied X post, including a screenshot
of the graph shown at the end of its video. The deliverable is a static 1080 ×
1920 Instagram story. The chart is the exact final frame of the corrected video,
not an invented or redrawn graph.

## Sources and verification

- Selected post: https://x.com/lesse_jivermore/status/2118672148466393341
- Author: **Curbstone Research (@lesse_jivermore)**.
- Official public metadata: https://cdn.syndication.twimg.com/tweet-result?id=2118672148466393341&lang=en&token=0
- Prior methodology post, quoted by the selected post:
  https://x.com/lesse_jivermore/status/2118292012055282037
- Original video:
  https://video.twimg.com/amplify_video/2118672127348101121/vid/avc1/1200x1200/966Ts7OtavDsYeFt.mp4

The public X pages and official metadata were retrieved successfully. The
selected post says: “This is what a bubble looks like. The Dotcom index in the
last post actually started in October 1995. Here is the corrected version
starting from January 1995.” The new corrected video's final frame takes
precedence over numbers in the older post.

The full prior post describes two discretionary, author-selected baskets of
10 stocks, equal weighted and rebalanced quarterly. They are not the Nasdaq
Composite, Nasdaq-100, or an exhaustive set of technology companies.

- Dot-com basket: EMC, AOL, YHOO, DELL, JDSU, AMZN, CSCO, MSFT, CMGI, ORCL.
- AI basket: NVDA, PLTR, AMD, ARM, NBIS, MRVL, LITE, BE, MU, DELL.
- Corrected dot-com period starts January 1995.
- AI period starts October 13, 2022, the author's chosen starting anchor.
- Final chart compares elapsed trading sessions, using daily closes, a linear
  scale and first close normalized to 1×.
- Earlier underlying basket descriptions used base 10; the final chart's
  explicit 1× normalization is preserved.

## Exact final-frame values

| Metric | Dot-com basket | AI basket |
| --- | --- | --- |
| Gain at matched session (1,019) | +4,296.4% | +1,508.8% |
| Calendar date at match | January 14, 1999 | November 5, 2026 |
| Peak gain shown | +15,065.9% | +2,648.6% |
| Peak date shown | March 24, 2000 | October 6, 2026 |
| Trading sessions to peak | 1,320 | 997 |

The source annotations say dot-com peak 151.7×, AI peak 27.5×, and AI last close
16.1×. The data files named in the source chart are `DOTCOM-daily.csv` and
`BUBBLE-daily.csv`; those underlying files were not retrieved or independently
audited. Details of dividends, corporate actions, delistings, pre-IPO treatment,
and retrospective selection bias are not fully disclosed in the public posts.

This is an attributed historical comparison. It does not establish that current
AI stocks are a proven bubble, predict a crash, or guarantee further upside.
The graphic does not interpret the author's analogy as an official index
forecast.

## Original screenshot and reproducibility

- Video: 1,200 × 1,200, 30 fps, 623 frames, duration 20.766667 seconds.
- Extracted final zero-based frame **622**, timestamp approximately **20.733333 s**.
- Source screenshot:
  `assets/ai-dotcom-comparison-final-frame-2026-11-07.png`.
- Screenshot: 1,200 × 1,200, 330,560 bytes.
- Screenshot SHA-256:
  `dc7a372fc315b3d97e743e56a523fc53240362ac3a07cfed6e8d079c0aa57bc1`.
- Video SHA-256:
  `45ac0bb7bba9a6aa6435ed95f19262760a2d1699ab89144936ecb037721fa8cf`.
- Detailed source/extraction provenance:
  `assets/ai-dotcom-comparison-final-frame-2026-11-07.json`.

```sh
ffmpeg -hide_banner -loglevel error -i source-video.mp4 \
  -vf 'select=eq(n\,622)' -frames:v 1 final-frame.png
```

The PNG preserves the full title, legend, axes, dates, comparison marker, table,
annotations and credits. It is uniformly scaled to 857 × 857 at x104, y557.
No source text or chart line is retyped, cropped, or redrawn. Embedded chart
fonts are preserved as part of the authentic screenshot; added editorial text
uses the required Moneyberg fonts.

## Authored on-graphic copy

- MONEYBERG NEWS BRIEF
- AI INVESTING
- NOVEMBER 6, 2026 • VIDEO SNAPSHOT
- AI VS. DOT-COM
- HOW THEY COMPARE
- 10-stock baskets, aligned by trading day.
- Chart: Curbstone Research • Post: Nov. 6
- AI data through Nov. 5 • Historical comparison

## Design and reproduction

A dark navy research-room background contrasts a warm 1990s CRT with cool
modern server racks. The full screenshot is the primary visual. Background
provenance and the exact generation prompt are recorded separately in
`assets/ai-dotcom-comparison-background-2026-11-07.md`.

The original `assets/moneyberg-coin-original.png` is uniformly scaled and seated
in the generated wall's brass recess, with compatible lighting and a contact
shadow. Its original artwork remains unchanged; the whole coin is within the
upper 75% of the canvas. No generated substitute coin is used.

- HTML: `assets/layouts/ai-dotcom-comparison-2026-11-07.html`.
- Renderer: `scripts/render_ai_dotcom_comparison_2026_11_07.py`.
- Audit: `briefs/ai-dotcom-comparison-2026-11-07-layout.json`.
- Actual font files: Lato Black weight 900 and Georgia weight 400.
- Georgia is runtime-only and is not embedded in repository files.
- All authored text and chart content fit x104–961, y164–1536.
- Minimum authored text 33px; body 35px; headlines 51px or greater.
- No background-production credit appears on the story.

```sh
/tmp/moneyberg-render-venv/bin/python scripts/render_ai_dotcom_comparison_2026_11_07.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

The renderer verifies actual browser font selection, required copy, font minima,
text overlap, content bounds, intact chart aspect ratio and hash, original coin
hash and complete upper-75% placement, and the final PNG dimensions.

Rendered and visually inspected: 1080 × 1920 PNG, 1,406,307 bytes. Eight authored
text elements and two content panels passed the layout checks. Original chart
and coin hashes match their source assets. Final output SHA-256:
`b12f15aafd45f1b3e02c6428874c665c5215e9040652ac69d1d869fba2f8904c`.

## Delivery

GitHub release asset after validation:
https://github.com/ryanschullo/create-ig-story-news/releases/download/stories-2026-11-07/ai-dotcom-comparison-2026-11-07.png

Publication and anonymous download are separately verified before sharing the
download link with the user.
