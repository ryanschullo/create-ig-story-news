# Four dates to watch — November 16–20, 2026

Edition: **November 15, 2026**. Category: **FEDERAL RESERVE WATCH**.

The selected Associated Press article carried by WTOP previews the coming economic week. The Story turns its four main releases into a readable calendar. It does not imply any of the forthcoming results or minutes are already available.

## Sources and verified facts

- **Selected report:** [AP / WTOP, “Retail sales and Fed minutes in focus next week”](https://wtop.com/national/2026/11/retail-sales-and-fed-minutes-in-focus-next-week/). The complete public body was retrieved and read. Publication and update metadata are both **November 14, 2026, 11:02:04 a.m. EST** (`2026-11-14T11:02:04-05:00`). Unrelated next-story material following the consumer-sentiment section was excluded.
- **Retail sales — Tuesday, November 17:** The [explicit Census 2026 release calendar](https://www.census.gov/economic-indicators/calendar-listview-2026.html) lists “Advance Monthly Sales for Retail and Food Services,” November 17, 2026, 8:30 AM, for the October 2026 observation period. AP reports economists expect **a 0.2% increase**, compared with September's 0.8% and August's 1.3%. The graphic says **“October: +0.2% expected vs. Sept.”** and separately labels this a forecast. The prior-month results are omitted for space. The forecast is attributed to economists cited by AP, not to Census.
- **Fed minutes — Wednesday, November 18:** The [Federal Reserve November calendar](https://www.federalreserve.gov/newsevents/2026-november.htm) lists the October 27–28 meeting's FOMC minutes on the 18th at 2:00 p.m. The [standing FOMC calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) confirms those meeting dates. This is a minutes release, **not a new rate decision**. The graphic makes no claim about the unpublished minutes' conclusions.
- **Jobless claims — Thursday, November 19:** AP explicitly schedules the weekly update for Thursday in the November 16–20 week. The [Labor Department economic-data page](https://www.dol.gov/newsroom/economicdata) and [current weekly-claims release](https://www.dol.gov/ui/data.pdf) were checked. At verification, the PDF was dated November 12, 2026, and showed the regular Thursday 8:30 a.m. Eastern schedule; a specific future November 19 primary schedule was not located. The graphic uses the AP-confirmed day/date and **no release time or forecast number**. Previous claims of 200,000 are not reused as a forthcoming result.
- **Consumer sentiment — Friday, November 20:** The [University of Michigan Surveys of Consumers homepage](https://www.sca.isr.umich.edu/) explicitly said: “Next data release: Friday, November 20, 2026 for Final November data at 10am ET.” The graphic says **“Michigan’s final November reading.”** It does not present the preliminary index or an expected final result as known.

All four entries omit release times for a consistent day/date calendar. The overall week and November 15 as-of date are visible. No stock-index panel is required because this is an economic-release calendar, not a daily market wrap. The AP article has an employment photo, not an attached chart; no source graph is omitted.

## Design and provenance

The distinct policy-calendar design uses midnight slate, dark architectural stone, restrained brass and pale high-contrast type. Four aligned event rows give the dates and release names priority. The lower architectural relief is conceptual decoration, not evidence of a specific named building or actual event. The complete generation prompt is preserved in `assets/economic-week-ahead-background-2026-11-15.md`.

The actual unmodified original Moneyberg coin is uniformly scaled to **220 × 220 px**, at **x777–997, y174–394**, inside the generated bronze recess. Compatible non-destructive tone, surrounding physical rim, contact shading and light integrate it into the stone surface. The original portrait, hair, lettering and circular proportions remain intact; no generated coin is used. Its entire rim is in the upper 75% and overlaps no news content.

All **25 text elements and four panels** fit within **x104–961, y164–1536**. Actual Lato Black 900 is used for headlines, brand, dates and labels; actual Georgia 400 for body and source lines. The renderer checks font metadata and actual Chromium platform fonts. Minimum sizes are **33 px overall, 35 px body and 51 px headlines**. The main headline is 96 px. No background-production footer is included.

## Reproduction and QA

```bash
/tmp/moneyberg-render-venv/bin/python scripts/render_economic_week_ahead_2026_11_15.py --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

Georgia is runtime-only, from the repository-documented Microsoft Core Fonts package; no Georgia bytes are embedded or committed. The renderer uses HTML/CSS in Chromium and does not edit image pixels. It validates the exact copy, computed font sizes, real font families, content bounds, lack of overlaps, original-coin SHA256/dimensions/aspect/placement, and PNG dimensions. The final PNG was visually inspected at full size after the final wording change; dates, text, coin integration and source qualifiers are clear.

- Export: `exports/economic-week-ahead-2026-11-15.png`
- Dimensions: **1080 × 1920**
- Bytes: **2,251,046**
- Export SHA256: `0305c8de43efd9ed212f802028f5a52f08e18ec030c8c7be66d518e3dae23fee`
- Generated background SHA256: `d2d04ce049cd91407af54d565fe94cf9ca6f015518e12558702aa3d3e6edde0a`
- Original coin SHA256: `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`
- Layout audit: `briefs/economic-week-ahead-2026-11-15-layout.json`

Publication is handled separately after review; this document does not claim a GitHub release has been uploaded.
