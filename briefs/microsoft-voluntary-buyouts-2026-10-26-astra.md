# Microsoft voluntary buyouts — Astra redesign

User-requested design comparison for the October 26, 2026 story. The existing
exports remain unchanged. The sourced facts and their scope are preserved from
`briefs/microsoft-voluntary-buyouts-2026-10-26.md`.

## Export and design

- Final: `exports/microsoft-voluntary-buyouts-2026-10-26-astra.png`.
- Canvas: **1080 × 1920**.
- A new graphite-and-slate office corridor provides a restrained workplace
  setting. Large, open typography, fine rules and an oversized eligible count
  replace the previous pale-blue stacked cards. The lower scene depicts an
  empty desk and chair as conceptual workplace imagery.
- Category: **JOBS & EMPLOYMENT**. The compact brand remains one line:
  **MONEYBERG NEWS BRIEF**.

## Source facts retained

Microsoft offers voluntary buyouts to approximately **60,000 eligible
employees**. Participation is voluntary, and the eventual departure count is
unknown. Eligibility covers selected teams in the United States, Canada, the
United Kingdom and India. Employees have until early December to decide, with
exits planned for year-end.

Sources read for the original brief and retained on the graphic:

- [Business Insider, October 26, 2026 — company memo and spokesperson reporting](https://www.businessinsider.com/microsoft-is-offering-buyouts-read-the-memo-2026-10).
- [Fox Business, October 26, 2026](https://www.foxbusiness.com/markets/microsoft-offers-voluntary-buyouts-60000-employees-tech-giant-reshapes-its-workforce).

The user-selected CNBC page was inaccessible in the original verification.
The graphic does not claim 60,000 confirmed departures or mandatory layoffs.

## Background and original coin

Image generation created a new text-free office background, copied unchanged
from `/workspace/generated_images/exec-17bba13a-f1d8-4fc7-bc63-1e94a2ce7ddf.png`
to `assets/microsoft-voluntary-buyouts-background-astra.png`.
It is conceptual editorial scenery, not evidence of an identified office,
office closure or actual departures. Per the saved skill, no background
production credit appears on the graphic.

The generated scene reserved an empty circular recess in a graphite column.
The original `assets/moneyberg-coin-original.png` is rendered directly into it,
with separate metal-rim, contact-shadow and surface-light layers and a
non-destructive blue-hour tone. Its face and lettering are not generated or
redrawn. Uniform scale preserves its circular proportions. The original master
is unchanged, SHA-256:

`4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`

The complete coin is at **x753–967, y987–1201**, entirely within the upper 75%.
It clears every news text element and belongs to the background column above
the desk.

## Rendering and checks

Template: `assets/layouts/microsoft-voluntary-buyouts-2026-10-26-astra.html`.
Renderer: `scripts/render_microsoft_buyouts_astra_story.py`.
Audit: `briefs/microsoft-voluntary-buyouts-2026-10-26-astra-layout.json`.

Chromium renders the actual Lato Black 900 font for headlines, numbers and
labels, and actual Georgia for body and sources. Georgia stays runtime-only
and is not redistributed. Browser platform-font checks verified every text
element without fallback. All 17 text elements, three rules and the restrained
source contrast wash fit the inner
content area **x104–961, y164–1536**. The original coin dimensions and hash,
whole-coin upper-75% bounds, text clearance, and PNG dimensions were checked.
The full-size export was visually inspected for legibility and integration.

Re-render:

```sh
python scripts/render_microsoft_buyouts_astra_story.py --georgia-font /path/to/Georgia.TTF
```
