# Jensen climbs in NVIDIA CEO odds — November 16, 2026

Category: **AI INVESTING**. User requested the original 1 Week chart, Jensen’s
rising trend, and the top three candidates. Edition and snapshot:
**November 16, 2026, 12:45 a.m. CST** (06:45 UTC).

## Source and verified scope

- [Original Kalshi market](https://kalshi.com/markets/kxnvdaceo/next-nvidia-ceo/kxnvdaceo-29jan)
- [Public event and rules API](https://api.elections.kalshi.com/trade-api/v2/events/KXNVDACEO-29JAN)
- [Public candidate markets API](https://api.elections.kalshi.com/trade-api/v2/markets?event_ticker=KXNVDACEO-29JAN&limit=100)

The website’s displayed top-three chances at screenshot capture are **Rene Haas
21%, Jensen Huang 17%, Ian Buck 14%**. A consistent single API response at
06:41:22 UTC and the page snapshot at 06:45:11 UTC agree. These are Kalshi
market-implied chances, not NVIDIA’s announced shortlist or an official
appointment. Additional outcomes exist; the top three are not normalized to 100%.

Event `KXNVDACEO-29JAN` asks who will be the next permanent NVIDIA CEO
**before January 1, 2029**. An official announcement by NVIDIA is sufficient;
the appointee need not yet have started. Interim and acting appointments do not
qualify. Graphic includes the deadline and interim/acting exclusion.

The actual **1W** control was selected before capturing the original chart.
Available history begins November 11–12, when these contracts launched; the
graphic explicitly says history starts November 11. No earlier values are
invented or backfilled. Jensen’s rising trend is apparent in the original blue
line and corroborated by hourly YES-ask closes: 3% on Nov. 12 at 23:00 UTC,
7% Nov. 13, 9% Nov. 14, 14% Nov. 15, 17% Nov. 16 at 06:00 UTC. The graphic
does not describe a default daily change as a one-week change or mix the candle
trade-price close with the current displayed chance.

## Original chart

`assets/source-charts/kalshi-nvidia-ceo-1w-2026-11-16.png` is the unmodified
**1536 × 692** screenshot of the public website’s complete chart, with legend,
dates, percentage axis, source branding, volume, and selected 1W control.
Capture details and evidence are in `kalshi-nvidia-ceo-2026-11-16-source.json`.
SHA-256: `f8316efb1168cb396da0a5d255a4a9ea5e65d9e596633b9c2d20339b4a02fc14`.
It is displayed at 857 px wide at its original aspect ratio. No source labels,
lines, legend, chart dates, percentages or source marks were redrawn or edited.

Public resources were retrieved with normal TLS verification using the
environment’s CA trust and rendered in Chromium. No login, trading, paid action,
security challenge bypass or certificate-verification disabling was used.

## Design and reproducibility

Light mineral ivory, petroleum-green type, executive boardroom and silicon
processor imagery. Background is an editorial illustration, with provenance and
exact imagegen prompt in `assets/kalshi-nvidia-ceo-background-2026-11-16.md`.
No production-credit footer appears on the graphic.

Lato Black 900 is used for headings, labels and date; genuine Georgia 400 for
scope, captions and sources. All authored text is at least 33 px, body at least
35 px and headline at least 51 px. News and panels remain inside x104–961,
y164–1536. Brand stays compact on one line.

The permanent original coin `assets/moneyberg-coin-original.png` is used
unchanged, uniformly scaled into the upper-right architectural recess, with
non-destructive tonal and contact-shadow treatment. Its complete rim remains
within y0–1440, outside news text and chart. Original SHA-256:
`4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.

Render with `scripts/render_kalshi_nvidia_ceo_2026_11_16.py`. The script checks
actual fonts, computed sizes, full content bounds, overlap, chart integrity and
aspect ratio, original coin integrity and placement, and final PNG dimensions.
Machine-readable results are in `kalshi-nvidia-ceo-2026-11-16-layout.json`.

Export: `exports/kalshi-nvidia-ceo-2026-11-16.png`, 1080 × 1920.
Direct-download release asset:
https://github.com/ryanschullo/create-ig-story-news/releases/download/stories-2026-11-16/kalshi-nvidia-ceo-2026-11-16.png
