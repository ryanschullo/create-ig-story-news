# Oil surplus fears — November 17, 2026

Selected article #4 from the November 17 shortlist, category **OIL & GAS**.

## Reporting

Source: Irina Slav, OilPrice, “Oil Prices Slide as Global Glut Fears Eclipse Hormuz Attacks,” published November 17 at 00:10 CST.

https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Slide-as-Global-Glut-Fears-Eclipse-Hormuz-Attacks.html

The complete public article body was read. It reports **Brent $91.70** and **WTI $85.03**, both in U.S. dollars per barrel, at its time of writing. The exact quote observation time is absent. Publication time is not substituted for quote time. The graphic explicitly reads “REPORTED SNAPSHOT • NOV. 17, 2026” and “Exact quote time not provided.” These are not settlement prices. No daily changes or contract months have been invented.

The article describes surplus expectations weighing on prices despite continuing shipping attacks. The graphic retains the conditional wording “potential glut” and “surplus forecasts” and states that attacks keep Gulf shipping at risk; it does not claim the conflict ended, the strait is safe, or oversupply is guaranteed.

Full Reuters corroboration through Investing.com was read in the earlier research: https://www.investing.com/news/commodities-news/oil-slips-on-supply-surplus-outlook-despite-gulf-tensions-5031433 . Reuters’ earlier Brent $92.00 / WTI $85.28 pair is deliberately not mixed into this later source snapshot. Details are preserved in the accompanying source JSON.

## Design and reproducibility

The final PNG is `exports/oil-surplus-fears-2026-11-17.png`, verified at **1080 × 1920**.

A new text-free petroleum/charcoal/amber refinery and storage-terminal background was created with the image generation tool. Its prompt and provenance are in `assets/oil-surplus-fears-background-2026-11-17.md`. Generated infrastructure is conceptual editorial imagery, not documentary evidence of the reported attacks.

The approved original 2084 × 2084 Moneyberg PNG is seated inside the background’s front-facing brass equipment recess. Uniform 262 × 262 scaling, compatible tone, inset contact shadow, and surrounding equipment establish scene integration. The entire original coin lies at x=715–977, y=1150–1412, within the upper 75% of the canvas. Its SHA-256 matches the permanent master; original portrait and lettering are retained. No generated coin replaces it.

HTML layout: `assets/layouts/oil-surplus-fears-2026-11-17.html`.

Renderer: `scripts/render_oil_surplus_fears_2026_11_17.py`.

```sh
/tmp/nov17-news-venv/bin/python scripts/render_oil_surplus_fears_2026_11_17.py --georgia-font /tmp/nov17-fonts/Georgia.TTF
```

Georgia is a runtime-only font from the official Microsoft Core Fonts installer, whose verified SHA-256 is documented in the repository font README. The unmodified font and installer remain outside the repository. The committed template preserves runtime URL placeholders. Python orchestrates Chromium rendering and validation; it does not edit image pixels.

## Verification

The rendered graphic was visually inspected, including the exact coin and all copy. A dark strip was added behind the reported-snapshot line to protect contrast over the refinery lights. All other text has calm dark backing or unobstructed negative space.

Browser checks verify all **20 authored text elements**, **5 news panels**, content within x=104–961/y=164–1536, no text collisions, no overlap with the coin, and no document overflow. Minimum authored size is 33 px; body copy is 36–39 px; headlines are 77 px and benchmark numbers 88 px. The brand is one 35 px line. DevTools verifies actual custom Lato Black 900 and Georgia 400 glyph rendering with no fallback. The original coin is uniformly scaled and uncropped. No background-production footer is displayed.

Independent copy review by the research agent passed, including both prices, source scope, timing disclosure, forecast uncertainty, and continued shipping risk. The audit JSON records exact output/background/font hashes and computed bounds.

No Git operations were performed by this graphic worker; the parent agent handles the batch commit and verified direct-download publication.
