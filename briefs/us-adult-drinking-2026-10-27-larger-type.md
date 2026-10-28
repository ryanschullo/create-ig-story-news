# Drinking-rate graphic — larger type revision

Requested change: update the saved skill to reject the drinking graphic's
smallest text sizes, increase them by at least four points, then redo the graphic.

Final PNG: `exports/us-adult-drinking-2026-10-27-larger-type.png`.
Canvas: 1080 × 1920. Category: **CONSUMER SENTIMENT**.

## Saved rule and implemented sizes

`.agents/skills/ig-story-news/SKILL.md` and `AGENTS.md` now require a hard
30 px minimum for all newly authored text at this canvas size, including
dates, labels, chart annotations, sources and qualifiers. Headlines remain
at least 48 px and body copy at least 32 px. Other output sizes scale
proportionally. The compact brand range is now 30–34 px. Source-chart
artwork must stay intact and be enlarged as a whole when its labels need it.

Four typographic points equal 5.33 CSS pixels at 96 px/in. The 30 px minimum
raises the old 22–24 px text by 6–8 px, exceeding the requested increase.

| Element | Previous size | Revised size |
| --- | ---: | ---: |
| Date | 22 px | 30 px |
| Source / survey notes | 23 px | 30 px |
| Category | 24 px | 30 px |
| Chart title and zero label | 24 px | 30 px |
| Chart years | 27 px | 33 px |
| Chart note | 29 px | 34 px |
| Compact brand | 29 px | 32 px |

Source details are reflowed to four lines, with darker text for contrast.
The chart note is shortened to “Ties 2025’s low. Tracked since 1939.”
The headline, 54% hero, 36 px body and 33 px chart values remain legible
without a reduction. No source facts or survey qualifiers are dropped.

## Factual provenance

All reporting and scope remain as documented in
`briefs/us-adult-drinking-2026-10-27.md`. Primary sources:

- https://news.gallup.com/poll/713534/americans-drinking-remains-record-low.aspx
- https://news.gallup.com/file/poll/713558/20260820_Consumption%20Habits%20Topline_Alcohol.pdf

Gallup: 54% of U.S. adults aged 18+ self-report drinking alcohol, matching
2025's low in its series dating to 1939. Chart: 62% in 2023, 58% in 2024,
54% in 2025, and 54% in 2026. Bars share a zero baseline and a scale of
three pixels per percentage point. Survey: July 1–19, 2026; n=1,200;
sampling error ±4 percentage points; released August 20. October 27 is
the Story edition date, not the poll's fieldwork date.

## Design, assets and verification

The image tool edited the existing text-free bar background to even out the
lower-left reading area. It preserved the scene and blank cabinet mounting
seat. Generated edit:
`/workspace/generated_images/exec-9dc1a62c-ff4c-4ec3-a455-26cdf1bf5d0b.png`.
Committed as `assets/us-adult-drinking-larger-type-background.png`.
The original and editing prompts are recorded in the renderer and audit.

The exact original Moneyberg coin is loaded from the unchanged master and
integrated with the brass-lined cabinet recess and warm contact lighting.
Full coin bounds remain x=881–1035, y=1051–1205, inside the upper 75%.

Actual Lato Black 900 and Georgia are verified through browser font inspection.
The renderer additionally rejects any authored text below 30 px. All 24 text
elements and seven panels satisfy the inner content bounds, and the output
is verified as 1080 × 1920. Visual review confirmed the larger footer and
chart labels, unclipped text, proportional bars and intact coin.

Layout: `assets/layouts/us-adult-drinking-2026-10-27-larger-type.html`.
Audit: `briefs/us-adult-drinking-2026-10-27-larger-type-layout.json`.
Renderer: `scripts/render_us_adult_drinking_larger_type_story.py`.
Georgia stays runtime-only and is not redistributed. No Python pixel editing.

```bash
python scripts/render_us_adult_drinking_larger_type_story.py --georgia-font /path/to/Georgia.TTF
```
