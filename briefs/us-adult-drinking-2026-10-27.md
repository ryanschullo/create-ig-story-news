# U.S. adult drinking remains at a record low

Story edition: October 27, 2026, America/Chicago.
Category: **CONSUMER SENTIMENT**.
Output: `exports/us-adult-drinking-2026-10-27.png`, 1080 × 1920.

## Sources and scope

User-selected coverage:
https://www.foodandwine.com/us-adult-drinking-rate-at-record-low-gallup-poll-12194613

The Food & Wine page returned HTTP 402. Its full body and publisher metadata
were not accessible. Google News RSS indexes the story on October 27 at
10:01 UTC, but that is discovery evidence, not independent publisher-page
verification. This graphic uses the fully accessible original Gallup research
instead of assuming details from the blocked article.

Primary report, fully read:
https://news.gallup.com/poll/713534/americans-drinking-remains-record-low.aspx

Lydia Saad, “Americans’ Drinking Remains at Record Low,” August 20, 2026.
Original survey topline, also read:
https://news.gallup.com/file/poll/713558/20260820_Consumption%20Habits%20Topline_Alcohol.pdf

Gallup's July 1–19, 2026 telephone survey of 1,200 U.S. adults aged 18+
found that 54% say they drink alcohol, matching 2025's low in a trend dating
to 1939. National sampling margin of error is ±4 percentage points at 95%
confidence. Respondents live in all 50 states and the District of Columbia.

The question asks whether respondents have occasion to use alcoholic beverages
such as liquor, wine or beer, or are total abstainers. It does not measure
daily drinking, alcohol sales, or per-capita alcohol volume. Do not relabel
the sample as adults 21+ or infer exactly 46% abstainers: the reported
abstainer figure is 45%, with rounding/nonresponse accounting for the remainder.

## Published copy and chart

Headline: **America’s drinking rate holds at a record low**.

Hero: **54%** — “of U.S. adults say they drink alcohol.”

The chart uses these Gallup observations without interpolation:

| Year | Share of U.S. adults who say they drink alcohol |
| --- | ---: |
| 2023 | 62% |
| 2024 | 58% |
| 2025 | 54% |
| 2026 | 54% |

Bars start at a common zero baseline (y=1225) with a linear scale of three
pixels per percentage point. Each bar has its full value and year label.
The 2025 and 2026 bars have identical height. A note says “Matches 2025’s low
in a series begun in 1939.” This avoids implying a new year-over-year decline.

The source footer identifies Gallup, July 1–19 survey dates, adults 18+,
sample size, sampling error, August 20 release date, and self-reporting.
The October date is the Story edition, not a claim of a newly fielded poll.

## Design and provenance

New warm ivory, oxblood and oak bar-interior composition with a wine glass,
rocks glass, bottle and softly lit stone counter. Decorative background was
generated with the image tool and saved unchanged as
`assets/us-adult-drinking-background.png`. Original generated source:
`/workspace/generated_images/exec-a5b596aa-ec96-42d2-a5de-b292c8062c7d.png`.
The complete generation prompt is recorded in the renderer and layout audit.
The scene does not document actual respondents or survey activity.

The original master `assets/moneyberg-coin-original.png` is loaded directly
in the browser, uniformly scaled and seated within the bar's circular
brass-lined wood recess. Separate non-destructive shadow and warm-light
layers integrate it into the setting. The portrait and inscription are not
generated or retyped. Full coin bounds: x=881–1035, y=1051–1205, entirely
within the upper 75% of the canvas. The master remains unchanged.

Real Lato Black 900 is used for headlines, brand, category, date and chart
labels. Real Georgia is used for body, note and source text. Georgia is
supplied locally at render time and is not redistributed. The compact
`MONEYBERG NEWS BRIEF` label is one line. All news is inside the required
inner bounds x=104–961, y=164–1536. No background-production footer appears.

## Verification and reproduction

`scripts/render_us_adult_drinking_story.py` renders the committed HTML template
through Chromium. It checks the original coin hash and dimensions, verifies
font family and weight, uses browser font inspection to reject substitution,
checks every news text/panel bound, rejects text/coin overlap, and verifies
the final PNG is 1080 × 1920. The render was visually inspected for legibility,
chart values and proportions, and integrated coin placement.

Full audit and asset/output hashes:
`briefs/us-adult-drinking-2026-10-27-layout.json`.

Re-render with the actual local Georgia font:

```bash
python scripts/render_us_adult_drinking_story.py --georgia-font /path/to/Georgia.TTF
```

Python orchestrates the browser; no Python pixel-editing library is used.
