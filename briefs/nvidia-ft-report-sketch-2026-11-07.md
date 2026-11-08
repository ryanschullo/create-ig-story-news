# Nvidia / FT report — Jensen Huang sketch revision
**Category:** AI INVESTING
**Reporting edition:** November 7, 2026, America/Chicago.
**Export:** `exports/nvidia-ft-report-sketch-2026-11-07.png`.

The user requested a sketch of Jensen Huang on the existing Nvidia / FT story. This revision adds a transparent editorial portrait beside the headline and retains every word of the prior news copy, attribution and Nvidia response.

## Sources and editorial scope
The original source verification and full copy are recorded in `briefs/nvidia-ft-report-2026-11-07.md`.
- User-selected FT article: https://www.ft.com/content/a55a2a22-4479-4f93-a445-6147a5c6d790
- Public TechCrunch follow-up: https://techcrunch.com/2026/11/07/chinese-exec-was-recruited-to-spy-on-nvidia-ceo-according-to-us-intelligence-memo/
- Bloomberg report syndicated by NDTV: https://www.ndtv.com/world-news/woman-who-targeted-nvidia-ceo-jensen-huang-was-recruited-by-top-china-spy-agency-report-12295987

FT's page was inaccessible; its allegations and Nvidia's response were verified through the two accessible follow-ups. Attribution remains prominent in the headline, with “reportedly” and “suspected” in the report panel. The company response has the same body font size and panel dimensions. November 7 identifies follow-up coverage, not an independently verified original FT publication date.

The sketch is an ordinary head-and-shoulders portrait. It depicts no alleged relationship, meeting, espionage act or other event. It adds no factual claim or market reaction.

## Portrait asset
- `assets/jensen-huang-sketch-2026-11-07.png`, 1024 × 1536 RGBA, 2,924,558 bytes.
- SHA-256: `8424eb00c44c34b45f12aa88eb7eebcd8ec372497a4dd6d4eee1ac32e39f8ce5`.
- Prompt, reference-photo source and provenance: `assets/jensen-huang-sketch-2026-11-07.md`.
- Created with the image-generation tool using a viewed, publicly served Jensen Huang photograph from TechCrunch as a likeness reference.
- Alpha transparency verified. Uniformly rendered at **250 × 375**, x700–950, y164–539, with no cropping.
- The complete portrait stays within the required content bounds and does not overlap text or coin.

## Layout and reproduction
The original background, original Moneyberg coin and source copy remain unchanged. Headline type is reflowed at the current **51px** minimum to accommodate the portrait; body text remains **38px**, labels **33–35px**, and sources **33px**. All text uses actual Lato Black 900 or Georgia 400. Georgia remains runtime-only and is not redistributed.

The original coin remains integrated into the brass wall recess at x916, y611, 138 × 138, entirely within the upper 75% of the canvas. Every news element fits x104–961, y164–1536.

- HTML: `assets/layouts/nvidia-ft-report-sketch-2026-11-07.html`.
- Renderer: `scripts/render_nvidia_ft_report_sketch_2026_11_07.py`.
- Audit: `briefs/nvidia-ft-report-sketch-2026-11-07-layout.json`.
- Reused background: `assets/nvidia-ft-report-background-2026-11-07.png`.
- Coin: `assets/moneyberg-coin-original.png`.

```sh
/tmp/moneyberg-render-venv/bin/python scripts/render_nvidia_ft_report_sketch_2026_11_07.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

Validated: actual browser fonts, current minimum sizes, content bounds, no text/portrait/coin intersections, portrait aspect ratio and hash, original coin identity and placement, and final PNG dimensions. An independent comparison confirmed all authored text matches the prior graphic. The final image was visually inspected.

Final PNG: **1080 × 1920**, **1,765,226 bytes**.
SHA-256: `813a24c6276a4cdeda1bf95111c916225744ab5c34b42f617046fc0555f36b59`.

## Delivery
https://github.com/ryanschullo/create-ig-story-news/releases/download/stories-2026-11-07/nvidia-ft-report-sketch-2026-11-07.png

Release publication and anonymous attachment download are verified separately before sharing the link. Prior exports are preserved.
