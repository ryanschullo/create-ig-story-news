# October 26 graphics — integrated coin revisions

The user requested revised versions of the Anthropic, Microsoft and Options
Investing graphics after updating the skill. The revised exports integrate the
original Moneyberg coin into the background environment, keep its entire rim
within the upper 75% of the canvas, and omit the background-production footer.
Source credits, dates and factual qualifiers remain visible.

## Revised exports

All three PNGs are **1080 × 1920**. Original exports remain available as history;
the filenames below identify the requested revised versions.

| Story | Revised export | Coin integration | Full coin bounds |
| --- | --- | --- | --- |
| Anthropic IPO | `exports/anthropic-ipo-2026-10-26-integrated.png` | Bronze socket recessed into a warm limestone pier, with contact shadow, surrounding reveal and matching light glaze | x=858–1032, y=32–206; 174 × 174 px |
| Microsoft buyouts | `exports/microsoft-voluntary-buyouts-2026-10-26-integrated.png` | Front-facing seal within office glass architecture, with inset metal rim, contact shadow and pane reflections | x=828–1028, y=64–264; 200 × 200 px |
| Retail options share | `exports/retail-options-share-2026-10-26-integrated.png` | Medallion within a glass-wall recess, with a metal bevel, surrounding contact shadow and glass-lighting layers | x=813–977, y=483–647; 164 × 164 px |

Every coin's vertical bounds fall between y=0 and y=1440, the three-quarter
boundary. The original artwork is scaled uniformly and placed
directly by the browser. Surrounding materials and light treatments integrate
it into each scene; none of the final portraits or rim lettering is generated
or retyped. Each coin remains clear of news text, source lines and charts.

The original master remains unchanged:
`assets/moneyberg-coin-original.png`, SHA-256
`4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.

## Content and artwork preserved

- **Anthropic:** official wordmark, preliminary filing/proposed ANT ticker,
  qualified $1.5 trillion investor estimate with IPO price unset, and comparable
  first-half revenue of $16.3 billion versus $1.16 billion remain unchanged.
  Sources: SEC S-1, Reuters and The Guardian. See
  `anthropic-ipo-2026-10-26.md` for the original source record.
- **Microsoft:** approximately 60,000 eligible employees, voluntary
  participation, unknown final departure count, selected teams in four
  countries, early-December decision period and year-end exits remain
  unchanged. Its category is now the saved **JOBS & EMPLOYMENT** label.
  See `microsoft-voluntary-buyouts-2026-10-26.md`.
- **Options Investing:** the 61% retail share is still explicitly limited to
  Citadel Securities' platform during the post's stated last week. The change
  remains **16 percentage points in 12 months**. The complete original graph
  is directly embedded, including its title, axes, dates and source credits.
  See `retail-options-share-2026-10-26.md`.

The Anthropic wordmark and original options graph retain their source hashes:

- Logo: `eb0f063a7a66a42ca0b1db7696555030d1afe80c63896a594ecdbb90e980cb7d`.
- Chart: `bfb420948ae75d489a88fb50a17efb66f6ee5086160a4820d4e22b896c3f97ca`.

## Background provenance

Image generation edited only the illustrative background environments. The
exact original coin, logo and graph were subsequently placed in Chromium.
These are decorative scenes, not evidence of identified company facilities.
Production details are documented here instead of printed on the graphics.

| Archived background | Generated edit source |
| --- | --- |
| `assets/anthropic-ipo-background-integrated.png` | `/workspace/generated_images/exec-d20c05f4-ab0d-48eb-9266-1d38ff3d88d5.png` |
| `assets/microsoft-voluntary-buyouts-background-integrated.png` | `/workspace/generated_images/exec-6f309e2e-43a3-4ea6-b652-931e0b9647c4.png` |
| `assets/options-investing-background-integrated.png` | `/workspace/generated_images/exec-e07fdf42-3359-496d-aa2d-cf55edbe4882.png` |

## Rendering and verification

Each export has a new `-integrated.html` template under `assets/layouts/`, a
corresponding `*_integrated_story.py` renderer under `scripts/`, and a measured
`-integrated-layout.json` audit under `briefs/`. Run its renderer with
`--georgia-font /path/to/Georgia.TTF`; the actual Georgia font remains a local
runtime dependency and is not embedded in committed files.

Font metadata and Chromium's platform-font records confirm actual **Lato
Black, weight 900**, and **Georgia** for every authored text element. Original
chart and logo lettering remains source artwork. All news text, panels, logo
and graph fit inside x=104–961, y=164–1536; only background decoration and the
coin can extend outside that news-content area.

Root review compared each revised text inventory with its original: the only
changes were removal of the background-production line and Microsoft's
category label. The source graph, official wordmark and coin master hashes
match. All three final images passed visual review for scene integration,
readability, source visibility and full coin placement within the upper 75%.

Output SHA-256 values:

- Anthropic: `75167d4b26e9fdaa2f5a3fd9f580e50b8e9ea344d0403fe11e0b51ceacc12f4a`.
- Microsoft: `7a5bb8cf9b8e28bd5fbc2f8b9e050cf84eb416c83263c2121142abfbd4b310f4`.
- Options: `a49dee263d8c33663e1afc338d37a3bf355f55a7b15a0c66217eb74e595e5193`.
