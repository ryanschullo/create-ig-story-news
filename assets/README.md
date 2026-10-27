# Design assets and references

## Anthropic IPO

`logos/anthropic-wordmark-original.svg` is the exact, unmodified wordmark
extracted from the official Anthropic homepage header. Its nine vector paths
preserve the original lettering without retyping or font substitution. Source,
retrieval date, dimensions and hash are recorded alongside it in
`logos/anthropic-wordmark-provenance.json`. Anthropic's wordmark identifies the
company in editorial coverage; it is not a generated logo.

`anthropic-ipo-background.png` is a generated editorial computing illustration
in warm ivory, charcoal and terracotta, not an identified company facility.
The browser layout places the official wordmark and original Moneyberg coin
directly, with actual Lato Black and runtime-only Georgia typography. See
`../briefs/anthropic-ipo-2026-10-26.md` for filing facts and valuation qualifiers.

## Microsoft voluntary buyouts

`microsoft-voluntary-buyouts-background.png` is a generated editorial office
illustration, not a photograph of an identified Microsoft building. The layout
at `layouts/microsoft-voluntary-buyouts-2026-10-26.html` is rendered in a browser
with actual Lato Black and Georgia font files. The original coin PNG is placed
directly, with equal width and height; it is not redrawn by the image model.
Georgia is provided locally at render time and is not redistributed here.
See `../briefs/microsoft-voluntary-buyouts-2026-10-26.md` for sourcing and
`../scripts/render_microsoft_buyouts_story.py` for the reproducible renderer.

## Fed prediction-market data figure

`fed-rate-decision-background.png` is generated editorial background imagery.
The quantitative chart at `charts/polymarket-fed-october-2026-month.png` is
rendered from actual archived Polymarket observations in
`data/polymarket-fed-october-2026/`, with explicit gaps for missing observations.
It is not an image-model reconstruction. The final Story places that actual
chart and the original coin as annotations, using explicit Lato Black and
Georgia font files. See `../briefs/polymarket-fed-decision-2026-10-28.md`.

## Earlier background reference

`moneyberg-story-background.png` is a generated background treatment based on
the user's supplied gold Moneyberg coin reference. It combines a subdued
antique-gold emblem with near-black and green geometric lines. It is derived
artwork, not an archived copy of the original logo.

The user's newly supplied original coin is the only approved coin artwork.
Do not use this generated background or coins in earlier exports as substitutes.
Always use the actual original, preserving its portrait, lettering, rim, and
circular proportions. Integrate it subtly while the subject-specific background
remains primary. Earlier exports remain historical work and need no automatic
revisions.

## Permanent original coin master — verified

Canonical path: `assets/moneyberg-coin-original.png` at the repository root.

Direct source:
https://raw.githubusercontent.com/ryanschullo/create-ig-story-news/main/assets/moneyberg-coin-original.png

The actual original was uploaded and committed by the user in
`29326334dd57ec2fdb26b6564231e35b8deeffe7`. It is now archived unchanged. The
local file and raw download were compared byte for byte and visually verified.

- Format: PNG (RGBA)
- Dimensions: 2084 × 2084 pixels
- File size: 1,538,597 bytes
- SHA-256: `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`

Reuse this master without asking the user for another upload. If missing
locally, restore it from the repository or direct source with normal TLS
verification, then check its dimensions and hash. Check history and the verified
source before requesting help if a download fails. Never use generated exports
or a similar-looking coin as the master.

Preserve the master unmodified. Keep any resized, cropped, background-removed,
or edited working derivatives under separate filenames. A generation reference
does not guarantee an exact reproduction in the finished graphic.

## Subject-specific examples

Future graphics use distinct subject-specific palettes, layouts, and relevant
background imagery. For an oil design example, see
`../exports/oil-five-month-high-2026-10-22-oil-design.png`: petroleum black,
charcoal, amber, and industrial energy imagery. Do not apply the oil treatment
to unrelated subjects.

The compact-label power-and-infrastructure example is
`../exports/electricity-prices-2026-10-22-compact-brand.png`. New graphics use
the small single-line label `MONEYBERG NEWS BRIEF` in Lato Black (weight 900),
secondary to the story headline, together with a subtle coin accent.
Use this example for its layout and power imagery only; its generated coin is
not a replacement for the user's approved original artwork.

All added news content and text must follow the safe-area and exact Lato
Black/Georgia assignments in `.agents/skills/ig-story-news/SKILL.md` at the
repository root. Decorative backgrounds may extend beyond the content area.
Keep all panels readable and generated scenery clearly illustrative; do not
fabricate quantitative data or visual evidence of a news event.
