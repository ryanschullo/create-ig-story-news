---
name: ig-story-news
description: Create sourced Instagram Story news graphics in the user's black-and-green editorial style, with all news content inside their marked content area.
---

# Instagram Story news graphics

## Required content area

The user supplied an annotated example with a red rectangle and asked that all
content stay inside that rectangle. Treat the rectangle as a layout guide, not
an element to render. This preference supersedes the earlier, larger white-panel
layout.

Create a 1080 × 1920 portrait canvas. The marked area, estimated from the user's
reference screenshot, is approximately:

| Boundary | Canvas proportion | 1080 × 1920 coordinate |
| --- | --- | --- |
| Left | 13% | x = 140 |
| Right | 91% | x = 980 |
| Top | 11% | y = 210 |
| Bottom | 80% | y = 1530 |

Use the pixel coordinates above as the working bounds. For another output size,
scale the coordinates proportionally from 1080 × 1920. Keep an additional inset
of at least 24 px, scaled proportionally, between these bounds and visible content.

All news content must fit completely inside this area: the entire headline,
date, photograph or illustration, body, highlights, chart title, axes, tick
labels, legend, source attribution, and any necessary estimate qualifiers.
Move the full headline into the area; do not reproduce the partial overlap in
the annotated example. A card or white panel containing news content must also
fit inside the area. Leave ample background visible below it.

Only decorative background elements may sit outside the area. Keep any brand
label inside too, unless the user explicitly requests a separate header outside
the area. Do not reproduce the red rectangle in finished exports.

## Fit and readability

- Reflow and shorten the summary before reducing type size. Use a concise
  headline, one primary visual, and the most relevant facts.
- Aim for a headline of at least 48 px and body copy of at least 32 px on the
  1080 × 1920 canvas. Keep attribution and chart labels comfortably legible.
- If a chart makes the panel too crowded, simplify it accurately, omit optional
  content, or split the story into multiple slides. Never crop chart labels,
  legends, source lines, or parts of the headline to make them fit.
- Preserve source attribution and distinctions such as estimates versus official
  data when shortening the copy.
- Inspect the generated image before delivery. Check the actual placement of
  every element, not just the prompt. Revise any graphic that overflows.

## Visual style

Use the uploaded examples as references: near-black background, subtle dark
green geometric outlines, white editorial panels, black serif headlines and
body text, and restrained red underlines for key facts. A black text panel with
white sans-serif copy is also supported. Use blue highlights sparingly for
tickers or links. Keep the decorative background quiet.

Use `MARKET BRIEF` as the neutral label unless the user supplies a brand. Do not
copy the examples' personal branding by default. Do not fabricate publisher
logos or present an original summary as a screenshot of a publisher's article.

## News selection and sourcing

Focus on business, finance, stocks, the Federal Reserve, Kevin Warsh, the U.S.
economy, layoffs, Iran-related developments, the Russia–Ukraine war, oil prices,
Trump's economic and market-relevant actions, and AI investing. Prioritize the
user's supplied article or post when one is provided.

Discovery accounts on X: `@KobeissiLetter`, `@unusual_whales`,
`@dudewhoinvests`, `@zerohedge`, `@Kalshi_Finance`, and `@BillAckman`.
These are leads, not substitutes for verification. Check original reporting or
primary sources when accessible. If only the post is available, attribute its
claims to that post and its cited source; do not claim independent verification.
Distinguish estimates, commentary, and prediction-market odds from confirmed
facts. Label intraday figures with their observation time. Use America/Chicago
for deciding what the user means by today, preserving source time zones in
market timestamps.

## Generation and delivery

Use the image generation tool for creation and editing, supplying the content
area explicitly in the prompt. Inspect local reference images before editing.
Do not claim the exact canvas dimensions unless the resulting file was checked.
Do not change the original source chart's data or labels for layout convenience.

Keep the exported PNG in `exports/` with a clear filename. Cloud workspace files
are not automatically added to the user's ChatGPT image Library. Workspace file
links and the artifact viewer failed to download in this session; GitHub raw
image delivery worked. When the user has authorized a GitHub upload, commit only
the intended deliverables, push without force, verify the remote commit and
downloaded file, then give a verified GitHub file or raw image link. Otherwise
do not claim the file was uploaded. Never claim a download succeeded until it
was verified.
