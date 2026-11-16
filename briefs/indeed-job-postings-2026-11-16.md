# Indeed new U.S. job postings — November 16, 2026 edition

Category: **JOBS & EMPLOYMENT**. User-selected source: [The Kobeissi Letter post](https://x.com/KobeissiLetter/status/2122078940093427779). The user requested the chart; the final graphic includes the complete, unchanged original chart.

## Reporting scope and independent verification

The selected post was published November 15, 2026 at 21:27 UTC / 3:27 p.m. CST. This November 16 edition reports the post's **week ending October 16, 2026** snapshot; it does not label the data as current November 16 observations. The date and seasonal adjustment are visibly stated on the graphic.

Indeed Hiring Lab's [primary U.S. aggregate CSV](https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/aggregate_job_postings_US.csv) reports the seasonally adjusted **new postings** index at 99.19 on October 16, 2026, compared with 104.16 on October 16, 2025. The resulting −4.7715% change rounds to the displayed **−4.8% year over year**. The baseline is February 1, 2020 = 100, so 99.19 represents −0.81%, displayed as **−0.8% vs. February 1, 2020**. The original chart's endpoint label of 99.2 agrees with the rounded primary observation.

The [Indeed methodology](https://github.com/hiring-lab/job_postings_tracker/blob/master/README.md) defines the new-posting index as a seasonally adjusted seven-day trailing average; new postings are advertisements on Indeed for seven days or fewer. These are **ads, not actual hires**, completed employment changes, jobs lost, total Indeed postings, or official BLS vacancy counts. The final graphic visibly retains the ads-versus-hires distinction. [FRED's corresponding series](https://fred.stlouisfed.org/series/IHLIDXNEWUS) independently confirms the source and indexing approach. The current Indeed methodology supersedes older historical explanatory notes when seasonal-adjustment methodology differs.

Newer observations exist: November 6, 2026 is 94.39 in the primary CSV (94.38977 on FRED). Those values are not silently substituted into the selected dated post/chart. Historical series revisions are possible.

### Source claim deliberately omitted

The post says new postings have declined 46.7% since April 2022. The current primary CSV does not corroborate that specific start month: April 2022 peaks at 179.77, giving a decline of approximately 44.8% to 99.19. The series peak at 186.22 is February 23, 2022 and produces approximately −46.7%. The graphic omits the unsupported April comparison, rather than silently changing the source's date. The original chart contains no April comparison annotation and remains untouched. The post's interpretations about BLS hiring recovery are also not presented as measured facts.

## Final copy

- MONEYBERG NEWS BRIEF
- JOBS & EMPLOYMENT
- NOVEMBER 16, 2026 EDITION
- NEW JOB POSTINGS / SLIP BELOW 2020
- −4.8% / YEAR OVER YEAR
- −0.8% / VS. FEB. 1, 2020
- U.S. • Week ending October 16, 2026
- Seasonally adjusted • 7-day average
- Source: Indeed / The Kobeissi Letter
- X post: Nov. 15 • Chart shown in full
- New postings are ads, not actual hires.

## Original source chart

Original URL: `https://pbs.twimg.com/media/HXK1x7mbgAAfpOh.jpg?format=jpg&name=orig`.

Saved without pixel editing as `assets/source-charts/indeed-job-postings-2026-11-16.jpg`: JPEG, 1200 × 801, 69,023 bytes; SHA256 `0ecdd9cc78aea88157b04b689ac2524ce8f392dd5e319d5eb7aee0be372e634d`. Rendered proportionally at x104, y827, width857, height572.047. The title, 2020–2026 x-axis, 0–200 y-axis, line, red endpoint box, 99.2 label, Indeed credit, TKL logo and full footer are all preserved. No clipping, redrawing, retyping, stretching, generated chart, or reply media. Original source-chart typography is retained; authored typography follows the size minima separately.

The chart and post were inspected via the selected public post, its original attached media, official syndication, and a full-note public mirror. Primary source data and methodology were accessed without bypassing authentication or access controls. Source observations and discrepancy details are archived in `briefs/indeed-job-postings-2026-11-16-source.json`.

## Design, typography and asset provenance

The subject-specific imagegen background depicts a muted slate office reception wall, a desk and work materials, with an integrated brass architectural recess. It is a conceptual workplace environment, not a documentary photograph of an employer, layoffs or specific hiring event. Exact generation prompt and source output path are recorded in `assets/indeed-job-postings-background-2026-11-16.md`; no background-production footer is added to the graphic.

The approved original `assets/moneyberg-coin-original.png` is preserved byte-for-byte and uniformly rendered at x818, y121, 218 × 218. Its actual location is adapted to the generated recess; the whole circular rim ends at y339, inside the upper75% of the story. CSS ambient tone and contact shading seat the original artwork inside the architectural recess while retaining the portrait, lettering and proportions. It does not overlap news text or the chart. Master SHA256: `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.

All authored text uses genuine Lato Black900 or Georgia400. Minimum label/source size33px; body35px; headline66px; large metrics96px. The compact masthead is a single line at35px. Georgia is loaded from a runtime-only font file and is not redistributed or embedded in the committed HTML. Chromium CDP verifies actual custom font usage per text element. All news content, including the complete chart, stays within x104–961,y164–1536 on the1080 ×1920 canvas.

## Reproduction and validation

Run `scripts/render_indeed_job_postings_2026_11_16.py --georgia-font /path/to/genuine/Georgia.TTF` using Python with Playwright and fontTools and Chromium at `/usr/bin/chromium`. The generated background is already committed alongside its exact prompt. The renderer uses HTML/CSS screenshot compositing; no Python pixel-editing library is used.

The renderer validates exact source-chart/coin hashes, natural asset dimensions, aspect ratio, full chart width, no clipping, no chart/news or coin/news overlap, no text overlap, required factual text, role-specific font minima, actual browser fonts, source scope, inner content bounds, and final1080 ×1920 PNG dimensions. It records the complete generation prompt and detailed measurements in `briefs/indeed-job-postings-2026-11-16-layout.json`.

Final PNG was visually inspected after rendering: complete chart, readable hierarchy, unchanged coin integrated into the recess, source date and data date separated, and no clipping or omitted artwork. No existing historical graphic or skill was modified.
