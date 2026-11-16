# NVIDIA options signal a big move

- Edition: November 16, 2026.
- Category: OPTIONS INVESTING.
- User selection: item 1 in `briefs/article-options-2026-11-16.md`.
- Export: `exports/nvidia-earnings-options-2026-11-16.png`, 1080 × 1920.

## Source and metric verification

Selected article: https://www.benzinga.com/markets/options/26/11/63277522/nvidia-earnings-without-jensen-huang-could-trigger-341-billion-stock-swing-as-options-traders-brace-for-volatility

The full public body was re-fetched and read for this graphic. Publication and modification are both November 15, 2026 at 15:00:30 Eastern / 14:00:30 Central. The November 16 edition date does not imply a new Monday options-chain quote. The visible source line preserves November 15.

The article says: “Benzinga Pro shows the options market implying an 8.27% move around the report. On Nvidia’s $4.13 trillion market cap, that’s an enormous $341 billion of market value at stake.”

The graphic therefore shows **±8.27%**, **“IMPLIED MOVE AROUND EARNINGS”**, **“In either direction”**, and **“ABOUT $341B.”** The latter is a potential market-capitalization change based on the article's $4.13T valuation, not option premium, cash invested, revenue, or an expected loss. The article's rounded figures give $341.551B if multiplied; this graphic preserves its reported approximately $341B rather than presenting an exact calculated result.

The article does **not** supply an exact option expiry, observation timestamp, strike, straddle methodology, confidence interval, or measurement endpoint. The underlying Benzinga Pro chain was not independently retrieved. No one-day, one-week, November 20 expiry, one-standard-deviation or probability claim is added. The visible qualifier says actual movement may differ from options pricing. This is a reported magnitude estimate, not a directional trading recommendation.

There is no attached quantitative chart in the selected article. No historical graph or supposed source chart is invented. Decorative GPU hardware and translucent background forms are conceptual and carry no numerical data.

## Primary earnings date

NVIDIA Investor Relations press release, October 28, 2026:
https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx

Matching full NVIDIA Newsroom release:
https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873

Specific event page:
https://investor.nvidia.com/events-and-presentations/events-and-presentations/event-details/2026/NVIDIA-3rd-Quarter-FY27-Financial-Results/default.aspx

All three public pages were read and agree on **Tuesday, November 17**. The company says results will be announced at approximately **1:20 p.m. Pacific / 4:20 p.m. Eastern / 3:20 p.m. Central**, followed by a conference call at **2 p.m. Pacific / 5 p.m. Eastern / 4 p.m. Central**. Thus **“NOV. 17 EARNINGS • AFTER THE CLOSE”** is supported. These are upcoming fiscal-Q3-2027 results for the period ended October 25, 2026, not calendar-2027 results.

The graphic concentrates on earnings/options. It makes no unsupported statement about call attendees, current officer titles, personal allegations, or guaranteed earnings outcomes.

## Design and reproduction

Distinct options palette: deep plum and indigo with teal highlights, dark metal and unbranded GPU hardware. Exact imagegen prompt and original-output provenance are in `assets/nvidia-earnings-options-background-2026-11-16.md`. Factual text is typeset separately in actual Lato Black 900 and Georgia 400.

The approved unmodified `assets/moneyberg-coin-original.png` is uniformly scaled into the generated upper-right brass recess, with compatible ambient light and CSS contact shading. It keeps the original portrait, hair, lettering and circular rim; no generated coin is used. The entire coin remains in the upper 75%, clear of news content. Its master SHA256 remains `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.

The renderer verifies required exact copy, actual font metadata and Chromium platform fonts, minimum authored type 33 px (35 px body; 51 px headlines), news-content bounds x104–961/y164–1536, text overlaps, coin integrity/proportions/placement, and the 1080 × 1920 PNG. Georgia is runtime-only and not redistributed. Background-production credits are retained in documentation, not printed on the graphic. No three-index panel is needed because this is a single-stock options story, not a broad market wrap.

```sh
/tmp/moneyberg-render-venv/bin/python scripts/render_nvidia_earnings_options_2026_11_16.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

Layout audit: `briefs/nvidia-earnings-options-2026-11-16-layout.json`. Runtime evidence: `/tmp/nov16-nvidia-graphic-source.md`, `/tmp/nov16-options/nvidia-graphic-recheck.*`, and `nvda-primary-2.*`, `nvda-primary-3.*`, `nvda-primary-10.*` in the same directory. The substantive source facts, links and limitations are retained above if temporary files are cleared.
