# October 28 Fed decision — one month of Polymarket history

User-selected market:
https://polymarket.com/event/fed-decision-in-october-20260617190323537

Final Story: `exports/polymarket-fed-decision-2026-10-28.png` — 1080 × 1920.
Chart-only artifacts:
`assets/charts/polymarket-fed-october-2026-month.png` (1800 × 1250), plus SVG.

## Source and date

The user supplied October 28 as the decision date. The market's resolution
rules also identify the October 27–28, 2026 FOMC meeting and point to the
Federal Reserve calendar. Direct access to the official Fed calendar returned
403, so no unverified decision-release time is added to the graphic.

Gamma event ID: 606422. There are **five** mutually exclusive outcome brackets:
50+ basis-point cut, 25 bp cut, no change, 25 bp hike, and 50+ bp hike.

## Actual month-long history

The chart uses 3,528 observed YES-token historical prices from the official
Polymarket CLOB `/prices-history` endpoint. Requests used seven-day chunks and
`fidelity=60`. Ordinary curl worked; Python urllib received 403. Source URLs,
token IDs, conditions, request windows and retrieval times are archived in:

`assets/data/polymarket-fed-october-2026/manifest.json`

All 25 original response files, original event metadata, combined and individual
CSVs, a gap report and the distinct newer Gamma snapshot are preserved in that
directory. Original source files are retained unchanged; absolute temporary
paths inside the acquisition manifest record their original download location.
The archived files use those same basenames.

The plotted window runs from September 25 at approximately midnight Chicago
through October 25 at approximately 10 p.m. Chicago. Label it **Sep. 25–Oct. 25**
or a month, not exactly 30×24 hours. All displayed historical endpoints are
approximately October 25, 10 p.m. CDT.

| Outcome | Observations | First price × 100 | Last price × 100 |
| --- | ---: | ---: | ---: |
| No change | 708 | 32.5% | 93.5% |
| 25 bp hike | 709 | 66.5% | 5.5% |
| 50+ bp hike | 701 | 1.25% | 0.35% |
| 25 bp cut | 707 | 0.45% | 0.15% |
| 50+ bp cut | 703 | 0.25% | 0.05% |

The five histories have 143 gaps exceeding 90 minutes, up to about five hours.
NaN path separators break lines at those gaps. No missing observations are
filled; no prices are smoothed, normalized or fabricated. Extra live points
outside requested API windows were excluded from the chart data.

## Snapshot basis and interpretation

The later Gamma snapshot, updated October 25 at 10:30 p.m. CDT, lists 94.5%
for no change. It is a different observation and is **not** appended to the
historical series or mixed into the headline. The Story's 93.5% figure comes
from its actual final hourly historical point and is timestamped accordingly.

Official pricing documentation:
https://docs.polymarket.com/concepts/prices-orderbook

Displayed odds generally use bid–ask midpoints, with last-trade fallback when
the spread exceeds $0.10. Buy buttons represent execution quotes. The history
API describes historical token prices without specifying that every sample is
a midpoint or a last trade, so the chart does not call them daily closes.

History documentation:
https://docs.polymarket.com/api-reference/markets/get-prices-history

The graph shows historical token price × 100 as market-implied probabilities.
It explicitly says these are **not a Fed forecast**, and that market prices
may not total 100%. Do not silently normalize independent market quotes or
describe a prediction-market outcome as the Fed's announced decision. Ignore
the market page's experimental AI summary as a history/quote source.

## Rendering and asset integrity

The illustrative background was created with image generation and archived at
`assets/fed-rate-decision-background.png`. Numerical paths and labels were
rendered from the archived observations using standard plotting tools. The
Story places that actual chart bitmap directly; an image model does not redraw
or invent the plotted history.

- Chart renderer: `scripts/render_polymarket_fed_chart.py`.
- Story renderer: `scripts/render_fed_probability_story.py`.
- Actual Lato Black weight 900 is bundled with its OFL license in
  `assets/fonts/lato/` and is used for chart labels, headlines and brand text.
- Actual Georgia was obtained from Microsoft's official Core Fonts project
  installer for runtime use; it is used for body/source text, without font
  fallback. Georgia files and the installer are **not** redistributed here.
- The Story script requires an explicit `--georgia-font` path; it fails rather
  than silently substituting a font.
- The original coin is directly placed as a uniformly scaled, translucent
  annotation. It is not redrawn by the image model. The original master remains
  unchanged: SHA-256
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- All 12 authored text items and the full chart panel passed renderer bounds
  checks against x=104–961, y=164–1536. The full source text is readable on a
  dark footer panel. Decorative background and coin may extend outside it.
- Layout/font-family bounds are recorded in
  `briefs/polymarket-fed-decision-2026-10-28-layout.json`.

Final visual review confirmed five outcome labels, source dates, probability
endpoints, missing-data gaps, and full chart/legend visibility. No Nasdaq/Dow/
S&P daily closing-results panel is relevant to this Fed prediction-market chart.
