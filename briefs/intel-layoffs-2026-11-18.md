# Intel cuts more jobs — November 18, 2026

- Category: **JOBS & EMPLOYMENT**.
- Selection: #12 from `article-options-2026-11-18.md`.
- Source: [Business Insider](https://www.businessinsider.com/intel-layoffs-restructuring-ceo-lip-bu-tan-2026-11), Alice Tecotzky and Shubhangi Goel, published November 17 at 8:00 p.m. Chicago time (November 18 at 02:00 UTC). Full article read.

Intel confirmed additional job reductions as CEO Lip-Bu Tan's restructuring continues. Reports of global IT cuts are attributed to employees; Intel did not identify teams or disclose the affected job count. The graphic explicitly states **“Number of affected jobs not disclosed.”** Historical total headcount and previous layoff rounds are omitted, and no AI-driven causal claim is made.

## Design and provenance

Fresh image-generated, text-free conceptual semiconductor workplace in Intel blue, white, and steel. Empty workplace, silicon wafer, and processor are decorative illustration, not documentary evidence of Intel premises. Prompt archived at `assets/intel-layoffs-background-2026-11-18.md`.

The actual official Intel wordmark, archived unchanged at `assets/logos/intel-wordmark-original.svg`, is used in its original navy and cyan. The canonical original Moneyberg coin PNG is uniformly scaled into the generated wall recess with contact shading, preserving the complete original portrait, lettering, and rim. Whole coin remains in the upper 75% of the canvas. No generated coin or publisher logo is used.

HTML/Chromium composites actual Lato Black 900 and Georgia 400, with all authored news content inside x104–961/y164–1536. Georgia remains runtime-only outside the repository. No image pixel editing in Python.

## Reproduce

```sh
/tmp/nov18-news-venv/bin/python scripts/render_intel_layoffs_2026_11_18.py --georgia-font /tmp/nov18-fonts/Georgia.TTF
```

The renderer validates font identity in the files and browser, minimum sizes, source qualification, content bounds, text collisions, whole-coin placement, logo aspect ratio and exact original asset hashes. The output is `exports/intel-layoffs-2026-11-18.png`; full audit is `briefs/intel-layoffs-2026-11-18-layout.json`.
