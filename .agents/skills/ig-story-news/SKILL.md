---
name: ig-story-news
description: Create sourced Instagram Story news graphics with distinct subject-specific designs, Lato Black and Georgia, and all news content inside the user's marked content area.
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

Give each subject its own visual identity through a relevant background,
palette, composition, and panel treatment. Do not apply one fixed coin-dominated
background, green geometric template, or article-card layout to every story. Earlier
examples remain references for editorial clarity and emphasis, not mandatory
templates. White editorial panels and dark panels with light copy are both
supported. Follow the required font assignments and content bounds in every
layout. Keep backgrounds subordinate to legible news content.

## Required fonts

Always use **Lato Black** and **Georgia**. This requirement supersedes the
earlier generic serif-headline and sans-serif-copy guidance.

- **Lato Black** (Lato, weight 900): headlines, headings, brand labels, dates,
  chart labels, axes, and legends. Use the actual Black weight, not Lato Regular
  or another sans-serif font.
- **Georgia**: body text, summaries, captions, source attribution, and estimate
  qualifiers. Use Georgia rather than a generic serif substitute.

Use only these two fonts for authored text. Include these exact font names and
assignments in every generation or editing prompt. Keep both legible within
the required content area; shorten or reflow copy instead of switching fonts.

For a renderer that selects font files, verify that it resolves Lato Black and
Georgia without fallback. Do not silently substitute a missing font. Image
generation alone cannot prove which font files were used; do not claim exact
font verification solely from visual similarity.

## Recurring brand label

Use the exact label **MONEYBERG NEWS BRIEF** for new graphics and requested
revisions. Set all three words on one compact line in Lato Black (weight 900),
approximately 28–34 px on a 1080 px wide canvas, scaled with the output. The
label is secondary to the story headline, not a large masthead. Adjust its
spacing or size to fit without wrapping, cropping, or changing the wording.
Keep it inside the required content bounds with the other authored text.
This supersedes earlier large or two-line label directions. Historical exports
stay unchanged unless the user requests revisions; do not rewrite them merely
to update their label.

## Subtle Moneyberg background accent

The user's most recently uploaded original gold coin is the **only approved coin
artwork**. It is a circular gold medallion with the supplied stylized portrait,
`DEREK MONEYBERG` on the upper rim, and the supplied Latin inscription around the
lower rim. Always use that actual uploaded artwork, preserving its exact face,
hair, lettering, rim, and circular proportions. Do not generate a different
portrait, redraw the coin, retype its inscription, or substitute a similar coin.

Use the original upload as the reference for image generation or editing. Scale
it uniformly and blend it subtly into the background, preferably near an edge
or in the lower background. Subject-specific imagery, palette, and layout remain
primary; the coin must not turn every story into the same generic template or
compete with the text, visual, or chart. Preserve integral logo lettering as
artwork; Lato Black and Georgia apply to newly authored text.

`assets/moneyberg-story-background.png` and coins appearing in earlier generated
exports are **not approved substitutes** for the original. They remain historical
work only. Existing subject examples may guide layout and imagery, not coin
artwork selection. Do not use a generated variant as a master for another image.

The original currently exists as a conversation image reference; it has not been
archived as a local repository asset. Do not claim otherwise. If the actual
original becomes accessible as a file, preserve an unmodified master and record
its location. If it cannot be accessed in a future task, obtain the original file
or a direct source URL before adding the coin rather than inventing a substitute.
Inspect each finished image against the original, including the portrait and
lettering. A generation request alone does not prove exact logo reproduction.

The decorative watermark may extend outside the content area, while all added
text remains inside it. Branding is decoration, not evidence for news claims.

## Subject-specific designs

Use a distinct subject-specific design together with the compact one-line label
and subtle Moneyberg coin accent. The prior blanket coin ban no longer applies.
Retain historical exports unchanged unless the user requests revisions.

Choose a design appropriate to the story's subject. These are starting points,
not rigid templates; vary composition and hierarchy to suit the news:

| Subject | Background and design direction |
| --- | --- |
| Oil and energy | Petroleum black, charcoal, and amber; tanker, refinery, pipeline, or storage-tank illustrations; industrial lines and strong energy-focused composition. |
| Power and infrastructure | Charcoal, steel blue, and restrained electric yellow; transmission towers, substations, power lines, utility meters, or an illustrative electricity grid; a distinct infrastructure-focused composition. |
| AI investing and technology | Cool navy, cyan, or violet; chips, data-center structures, or circuitry; a clean technical composition. |
| Federal Reserve and U.S. economy | Slate, ink, or restrained cream; institutional architecture and macroeconomic motifs; a clear policy-brief hierarchy. |
| Consumer sentiment and cost of living | Warm neutral paper, ink, and burgundy; everyday retail, grocery, receipt, or household-budget illustrations; preserve the survey context and avoid unsupported economic-collapse framing. |
| Layoffs and business employment | Muted office or workplace imagery; distinct company or employment framing with a sober editorial palette. |
| Stocks and finance | A market-focused layout and palette; trading screens or financial motifs with concise market summaries. |
| Geopolitics and wars | A geographically relevant map or clearly illustrative regional imagery; a restrained map-led composition. |

For an oil-specific design reference, use
`exports/oil-iran-fears-2026-10-23.png`. Its petroleum/charcoal/
amber treatment belongs to oil stories; do not make it the default palette or
layout for unrelated subjects.

For a Nasdaq-specific example, use
`exports/nasdaq100-selloff-2026-10-22.png`: cool navy and electric blue,
exchange LED architecture, restrained red loss figures, and modular statistic
panels. Use this treatment for Nasdaq stories only, not as a universal template.

For a power-and-infrastructure example, use
`exports/electricity-prices-2026-10-22-compact-brand.png`. Keep its grid
imagery and charcoal/steel-blue/electric-yellow treatment distinct from oil and Nasdaq
designs. Do not invent project locations, grid maps, demand or generation
figures, or explanations for price changes that the reporting does not support.

For a consumer-sentiment example, use
`exports/consumer-sentiment-2026-10-23.png`: warm cream, ink, burgundy, and
grocery/receipt imagery. Present survey findings as sentiment, not proof of an
economic collapse; distinguish attitudes from measured spending or inflation.

Decorative backgrounds may extend beyond the marked content area or canvas
edges. All authored text and news content, including any brand label, remain
inside the required content bounds. Use `MONEYBERG NEWS BRIEF` as the added
label unless the user requests different wording.

Treat generated backgrounds as editorial illustration, never as evidence of an
actual event. Keep the main photograph or illustration relevant to the story.
Do not invent map boundaries, quantitative chart data, price labels, or event
details for decoration. Charts with numbers must use sourced data. Do not
fabricate publisher logos or present an original summary as a publisher's
screenshot.

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
area and required Lato Black/Georgia assignments explicitly in the prompt.
Include the exact recurring label `MONEYBERG NEWS BRIEF` in the prompt.
Specify that it is small, secondary, and on one line. Include the subject-specific
design and the user's original approved Moneyberg coin as a subtle watermark.
Inspect relevant references before editing; never substitute a coin from a
generated background or prior export for the original artwork.
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
