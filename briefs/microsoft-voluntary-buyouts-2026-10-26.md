# Microsoft voluntary buyouts — October 26, 2026

Story date: October 26, 2026 (America/Chicago).
Final Story: `exports/microsoft-voluntary-buyouts-2026-10-26.png`, 1080 × 1920.

## Sources and verification

User-selected CNBC article:
https://www.cnbc.com/2026/10/26/microsoft-msft-voluntary-buyouts.html

Direct access returned **HTTP 403 Forbidden**. Its full body was not read.
The following publisher pages were read directly to verify the story:

- **Business Insider**, Ashley Stewart, October 26, 2026:
  [Microsoft is offering buyouts to around 60,000 employees. Read the memo.](https://www.businessinsider.com/microsoft-is-offering-buyouts-read-the-memo-2026-10)
  Published 15:30:25Z (10:30 a.m. CDT), updated 21:28:53Z (4:28 p.m. CDT).
  Reproduces Chief People Officer Amy Coleman's employee memo and includes
  additional details attributed to a Microsoft spokesperson.
- **Fox Business**, Eric Revell, October 26, 2026:
  [Microsoft offers voluntary buyouts to 60,000 employees as tech giant reshapes its workforce](https://www.foxbusiness.com/markets/microsoft-offers-voluntary-buyouts-60000-employees-tech-giant-reshapes-its-workforce)
  Published 16:03:11 EDT (3:03 p.m. CDT). Corroborates the approximate eligible
  count, voluntary nature, job-level threshold, participating countries and
  organization-specific eligibility.

Source bodies, metadata and access results are retained locally for review in
`/tmp/microsoft-buyouts-source-excerpts-2026-10-26.json`.

## Verified facts and scope

- Microsoft introduced a **Voluntary Exit Offer** on Monday, October 26.
- **Around 60,000 employees are eligible** for offers. This is the number of
  eligible employees, not accepted buyouts, completed departures, mandatory
  layoffs or positions confirmed as eliminated.
- Participation is voluntary. The eventual departure count was not reported in
  the sources read.
- Eligibility covers **selected participating teams** in the **United States,
  Canada, United Kingdom and India**, at **internal job level 70 and below**.
  Level 70 is a job-level classification, not an employee age.
- Membership in one of those countries and job levels does not alone establish
  eligibility: participation varies with business priorities, customer
  commitments and workforce needs.
- Business Insider attributes to a Microsoft spokesperson that eligible
  employees have until **early December to decide**, with exits planned for
  **the end of 2026**. Do not invent a specific calendar deadline.
- Business Insider says offer terms will resemble Microsoft's standard
  severance. Its detailed examples of 60 days and up to 39 weeks describe
  earlier U.S. layoff packages; do not present those as guaranteed terms for
  every participant in all four countries.
- This new voluntary-exit offer follows an earlier age-and-tenure-based
  Voluntary Retirement Program. Do not reuse that older program's eligibility
  criteria or describe this as Microsoft's first-ever buyout.

AI investment and cost pressures provide context in the news reporting.
Coleman's memo frames this program as flexibility and adaptation to workforce
needs. The evidence does **not** establish that AI is directly replacing
60,000 employees or that 60,000 people will leave.

## Final graphic copy

Brand label: **MONEYBERG NEWS BRIEF**.

Headline: **Microsoft offers voluntary buyouts**.

Primary statistic: **~60,000 EMPLOYEES ELIGIBLE**.

Body: **Participation is voluntary. The eventual departure count is unknown.**

**SELECTED TEAMS**
U.S., Canada, U.K., India.

**DECISION WINDOW**
Early December to decide; exits planned for year-end.

Source attribution: **Business Insider (company memo) + Fox Business · Oct. 26,
2026**.

Keep the distinction between eligible employees and actual departures visible
in the final graphic. Country labels describe where participating teams are
located, not universal eligibility across those countries.

## Rendering and final QA

The text-free background was created with image generation and copied unchanged
from `/workspace/generated_images/exec-0e53b043-1fbc-431c-ae62-2e1c697ce665.png`
to `assets/microsoft-voluntary-buyouts-background.png`. It depicts a generic
technology office campus and is labeled as editorial illustration. It is not
evidence of an identified building, a closed office or actual departures.

`assets/layouts/microsoft-voluntary-buyouts-2026-10-26.html` provides the
layout. `scripts/render_microsoft_buyouts_story.py` uses Chromium to render the
HTML with actual font files and the original coin PNG. Python orchestrates
the browser; it does not redraw the logo or edit image pixels.

The renderer confirmed:

- PNG dimensions of **1080 × 1920**.
- All **16 text elements and six panels/rules** fit the required inner area,
  x=104–961, y=164–1536. The complete source panel ends at y=1520.
- Actual **Lato Black, weight 900**, for headings, labels, numbers and date;
  actual **Georgia** for body and source text. Font metadata and Chromium's
  platform-font records verified every text element without fallback.
- The Georgia file remains a runtime-only local font, not embedded into the
  committed HTML or redistributed with the repository.
- The unchanged original coin is placed directly at 230 × 230 px, with 70%
  opacity, near the lower-right edge. It is not image-generated. The master
  retains SHA-256
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.

The measured layout, actual fonts and asset hashes are recorded in
`briefs/microsoft-voluntary-buyouts-2026-10-26-layout.json`.
Final visual review confirmed readable copy, a compact one-line brand label,
the eligibility/departure distinction, selected-team scope, and the timeframe.
This is company employment news, so a three-index market-results panel is not
relevant.

Re-render with the actual local Georgia font:

```sh
python scripts/render_microsoft_buyouts_story.py --georgia-font /path/to/Georgia.TTF
```
