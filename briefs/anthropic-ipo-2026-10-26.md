# Anthropic IPO filing — October 26, 2026

Story date: October 26, 2026 (America/Chicago).
Final export: `exports/anthropic-ipo-2026-10-26.png`, verified at 1080 × 1920.

## Verified source record

- **Primary filing:** Anthropic, PBC, Form S-1, filed October 26, 2026:
  https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
  Full local archive: `/tmp/anthropic-ipo-2026-10-26-s1.html`.
  Relevant filing excerpts: `/tmp/anthropic-ipo-2026-10-26-s1-excerpts.txt`.
  The excerpts were checked for filing date, proposed listing and comparative
  revenue figures. The operating statement uses millions of dollars.
- **The Guardian**, October 26, 2026:
  https://www.theguardian.com/technology/2026/oct/26/anthropic-files-listing-stock-market
  Published 16:22:28 UTC (11:22 a.m. CDT), updated 23:16:31 UTC (6:16 p.m. CDT).
- **Reuters via CNA:**
  https://www.channelnewsasia.com/business/anthropics-soaring-sales-steep-losses-put-ai-frenzy-ipo-test-6493346
  Source for the approximately $1.5 trillion valuation attributed to some
  current and prospective investors. This estimate is distinct from a priced
  initial public offering.

## Filing status and financial scope

Anthropic filed its S-1 and **applied to list** its Class A common stock on the
**Nasdaq Global Select Market** under proposed ticker **ANT**. The offering
price range and share counts are blank in the filing reviewed.

An application is not confirmation of exchange approval, an IPO price, completed
fundraising or the start of public trading. Do not describe the shares as already
listed, priced or trading, or invent a final offer date or proceeds figure.

| Figure | Meaning and display treatment |
| --- | --- |
| **Approximately $1.5 trillion** | Reported estimate from some current and prospective investors, according to Reuters; not a valuation established by a priced IPO. Render **$1.5T** with that qualification visibly attached. |
| **$16.286 billion** | Revenue for the six months ended June 30, **2026**, reported as $16,286 million in the S-1. Render **$16.3B**. |
| **$1.163 billion** | Revenue for the six months ended June 30, **2025**, reported as $1,163 million. Render **$1.16 billion** or **$1.16B**. |

Both revenue figures cover the same six-month period in their respective years.
They are reported revenue, not full-year totals, annualized run rates, forecasts
or a measure of profit. Avoid adding a calculated growth percentage unless it
is separately checked and explicitly labeled as a calculation.

Do not describe the filing's $80.748 billion first-half net loss as operating
cash burn. That figure includes substantial non-operating fair-value accounting
effects; the operating loss shown for the period is $693 million. The final
graphic makes no net-loss, cash-burn or profitability claim.

## Final content

Recurring brand label: **MONEYBERG NEWS BRIEF**.

Headline treatment: the **official ANTHROPIC wordmark**, followed by authored
Lato Black text **files for IPO**.

Deck: **Applied to list on Nasdaq under proposed ticker ANT.**

Hero label: **REPORTED INVESTOR VALUATION**.

Hero figure: **$1.5T**.

Visible valuation qualifier: **Estimate from some current and prospective
investors. IPO price unset.**

Revenue comparison: **$16.3B first-half 2026 revenue** versus **$1.16 billion
first-half 2025**.

Source line: **Sources: SEC S-1; Reuters; The Guardian** followed by
**October 26, 2026** and **Background: editorial illustration**.

Keep the estimate qualifier close to the $1.5T figure and legible; do not reduce
it to an easily missed disclaimer. Preserve the distinction between filing,
applying to list and an already completed or priced IPO.

## Official logo, background and typography

Use `assets/logos/anthropic-wordmark-original.svg`, extracted from the official
header at https://www.anthropic.com/ . Local verification confirms its
570 × 64 viewBox, nine path elements and SHA-256:

`eb0f063a7a66a42ca0b1db7696555030d1afe80c63896a594ecdbb90e980cb7d`

Preserve the official path geometry and proportions. Do not redraw, retype or
generate a substitute logo. Its integral lettering is source artwork; the
required fonts apply to newly authored text. Full source and retrieval metadata
are archived in `assets/logos/anthropic-wordmark-provenance.json`.

Background asset: `assets/anthropic-ipo-background.png`, a warm ivory
and terracotta server illustration. Treat the imagery as decorative editorial
illustration, not a photograph proving an event or a visualization of revenue.
It was copied unchanged from the generated background at
`/workspace/generated_images/exec-01dc267d-6355-402e-b90a-b0ef641d10ce.png`.

Use actual **Lato Black (weight 900)** for authored headings and labels and
**Georgia** for body copy, sources and qualifiers. Use the unmodified original
Moneyberg master at `assets/moneyberg-coin-original.png` as the subtle coin
accent, preserving its portrait, lettering and circular proportions.

## Rendering and final QA

The browser layout at `assets/layouts/anthropic-ipo-2026-10-26.html` is rendered
by `scripts/render_anthropic_ipo_story.py`. Its output is **1080 × 1920**.
Image generation supplied only the illustrative backdrop; Chromium places
the original artwork and typesets the final content with real font files.

- All **15 text elements, five panels/rules and the official logo** fit the
  required inner bounds, x=104–961, y=164–1536. The source panel ends at y=1525.
- Font metadata and Chromium's actual platform-font records verified **Lato
  Black, weight 900**, and **Georgia** for every authored text element, with
  no substitution. Georgia remains runtime-only and is not embedded into the
  committed HTML or redistributed with the repository.
- The official SVG is placed directly at 680 × approximately 76.34 px,
  preserving its 570:64 aspect ratio. Its original source hash is unchanged.
- The original Moneyberg coin is directly placed at 230 × 230 px at x=770,
  y=1650 with 65% opacity. Its portrait, lettering and proportions are not
  redrawn. The unchanged master retains SHA-256
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Visual review confirmed the official wordmark, filing status, proposed
  ticker, nearby valuation qualifier, comparable revenue periods and readable
  source attribution. No market-results panel is relevant to this IPO story.

The measurements, actual fonts and hashes are recorded in
`briefs/anthropic-ipo-2026-10-26-layout.json`.

Re-render using an actual local Georgia font:

```sh
python scripts/render_anthropic_ipo_story.py --georgia-font /path/to/Georgia.TTF
```
