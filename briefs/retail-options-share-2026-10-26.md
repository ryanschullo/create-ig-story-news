# Retail options share — October 26, 2026

Category: **OPTIONS INVESTING**.

Final export: `exports/retail-options-share-2026-10-26.png`, **1080 × 1920**.

User-selected post:
https://x.com/KobeissiLetter/status/2114881746621575597

Published October 27, 2026, 00:47:55 UTC, which is **October 26 at 7:47:55 p.m.
CDT** in America/Chicago. The Story uses that Chicago date.

## Source and scope

The full public post and its attached original chart were read. The Kobeissi
Letter reports that retail options activity reached **61% of total volume on
Citadel Securities' platform last week**, near a record. It describes an
increase of **16 percentage points over the past 12 months** and a share
10 percentage points above the 2020 pandemic peak.

This is a platform-specific report, not an independently verified share of
the entire U.S. options market. Primary Citadel pages returned HTTP 403, and
the underlying series, exact denominator and full retail-classification
methodology were not independently obtained. Attribute the claims to
**The Kobeissi Letter, citing Citadel Securities**.

Do not describe 61% as a share of all U.S. options trading, all retail investors,
investment dollars or profits. A higher share also does not prove record
absolute contract volume. **16 percentage points is not 16% growth.**

The post's observation period is "last week." The chart's printed date ticks
run from March 2020 to September 2026; those ticks do not establish an exact
final observation date. No precise endpoint date is added to the original.

## Original graph

Highest-resolution source:
https://pbs.twimg.com/media/HVj5WtgWoAAWVnS?format=jpg&name=orig

Archived unchanged at
`assets/charts/retail-options-share-kobeissi-2026-10-26-original.jpg`.

- JPEG, **1560 × 1050**, 104,785 bytes.
- SHA-256:
  `bfb420948ae75d489a88fb50a17efb66f6ee5086160a4820d4e22b896c3f97ca`.
- Title: **Retail Options Weekly Trading Volume as % of Total Volume**.
- Vertical scale: **15%–65%**. Latest labeled value: **61%**, highlighted red.
- Printed source: **Citadel Securities**. Credit: **The Kobeissi Letter**.
- Full title, plotted line, axes, tick labels, source and credit are retained.
  The chart is placed as an actual image at uniform scale; it is not redrawn,
  digitized, cropped, or reconstructed by an image model.

Source, retrieval date and original hash are recorded in
`assets/charts/retail-options-share-kobeissi-2026-10-26-provenance.json`.
Embedded chart lettering remains source artwork; Lato Black and Georgia apply
to newly authored text around it.

## Graphic copy

Small one-line brand: **MONEYBERG NEWS BRIEF**.

Date/category: **OCTOBER 26, 2026 · OPTIONS INVESTING**.

Headline: **Retail options share nears a record**.

Hero: **61%** retail share of options volume.

Scope: **On Citadel Securities' platform, last week.**

Change: **Up 16 percentage points in 12 months.**

Attribution: **The Kobeissi Letter, citing Citadel Securities**. The post date
and editorial-illustration label are included with the source text.

## Persistent skill update

`AGENTS.md` and `.agents/skills/ig-story-news/SKILL.md` now establish
**OPTIONS INVESTING** as a recurring category. Daily article searches should
actively seek multiple fresh options candidates and include strong choices
within the requested total when available, alongside the existing subjects.
The rule does not impose a fixed quota or justify stale or unverified filler.

Topics include retail/institutional activity, index/ETF/single-stock options,
0DTE, put/call ratios, volume, open interest, implied volatility, skew, hedging,
expirations and options-based ETFs. The skill records source/denominator
checks, percentage-point distinctions, original-chart preservation, the
separate category label, and an options-specific ink/plum/indigo/teal design.

## Rendering and final QA

The background was created with image generation and copied unchanged from
`/workspace/generated_images/exec-13fbeba2-108c-49af-9515-969a889ed521.png` to
`assets/options-investing-background.png`. It is editorial trading-room scenery
in ink, plum, indigo and teal, with no invented prices or trading data.

`assets/layouts/retail-options-share-2026-10-26.html` is rendered by
`scripts/render_retail_options_story.py` in Chromium. The official source JPEG
and original coin are placed directly; an image model does not redraw them.

- The exported PNG is **1080 × 1920**.
- All **13 authored text elements, four panels/rules and the whole chart** fit
  within x=104–961, y=164–1536. The source panel ends at y=1525.
- The original graph appears at x=112, y=812, width=841 and height approximately
  566.05 px, preserving the 1560:1050 source aspect ratio. Title, axes, dates,
  61% endpoint, source and TKL credit remain intact. Its original hash matches.
- Font-file metadata and Chromium's actual platform-font records confirm
  **Lato Black, weight 900**, and **Georgia** for all newly authored text.
  The original chart retains its embedded lettering. Georgia remains a local
  runtime font and is not embedded in the committed HTML or redistributed.
- The original Moneyberg coin is placed at 230 × 230 px at x=770, y=1650 with
  65% opacity. The original master remains unchanged, SHA-256
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Final visual review confirmed the separate OPTIONS INVESTING badge,
  platform/last-week scope, percentage-point wording, full source graph,
  readable authored copy and citation. This is options participation news,
  so a three-index daily closing-results panel is not relevant.

The complete measurements, platform fonts and hashes are stored in
`briefs/retail-options-share-2026-10-26-layout.json`.

Re-render with the actual local Georgia font:

```sh
python scripts/render_retail_options_story.py --georgia-font /path/to/Georgia.TTF
```
