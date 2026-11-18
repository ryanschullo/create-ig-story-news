# Retail sales growth cools — November 18, 2026

Selection #8 from the November 18 article shortlist. Category: **CONSUMER SENTIMENT**.

## Verified reporting

- Full AP report via PBS, published November 17: https://www.pbs.org/newshour/economy/retail-spending-slowed-in-october-as-high-prices-gave-shoppers-pause
- Primary U.S. Census Bureau release CB26-181, November 17, 2026, 8:30 a.m. EST: https://www.census.gov/retail/marts/www/marts_current.pdf
- October 2026 advance U.S. retail and food-services sales estimated at **+0.2% month over month**, following **+0.8%** in September. October sales $748.2 billion; September $746.6 billion.
- Data adjusted for seasonal variation, holidays and trading-day differences; **not adjusted for inflation**.
- October's 90% confidence interval is ±0.4 percentage points and includes zero. The actual October change is not statistically distinguishable from zero at that confidence level. Graphic makes no consumer-collapse claim or inference about real spending.
- Source publication date (Nov. 17), observation month (October) and graphic edition (Nov. 18) remain distinct.

Structured facts, evidence locations and primary PDF hash are recorded in `retail-sales-2026-11-18-source.json`. The primary Census URL is rolling; the local PDF hash identifies the source reviewed.

## Composition

Warm cream, dark ink and burgundy boutique checkout background generated with image_gen. The two equally sized numerical panels compare monthly growth; panel areas do not encode magnitude. A large headline and large +0.8% / +0.2% figures give the main story first, followed by scope and estimate uncertainty.

The original 2084 × 2084 Moneyberg coin is uniformly scaled to 234 × 234 at x719, y110, seated in the scene's circular brass wall recess with a physical rim and contact shading. Original artwork is preserved, whole coin lies above y344, and it never overlaps authored news content.

All text and panels fit x104–961 and y164–1536. Authored type uses actual Lato Black 900 and Georgia 400. Minimum type is 33 px, main body 35 px, headline 94 px, and primary values 111 px. Brand is one line at 35 px. No background-production credit appears on the image.

## Reproduction and validation

```bash
/tmp/nov18-news-venv/bin/python scripts/render_retail_sales_2026_11_18.py --georgia-font /tmp/nov18-fonts/Georgia.TTF
```

Georgia is a runtime-only font and is not redistributed in the repository. Browser-native HTML/CSS composition preserves exact fonts and the coin; no Python pixel editing was used.

The renderer verified original coin SHA-256, 18 text elements, 3 panels, actual Chrome platform fonts, minimum sizes, bounds, text and coin non-overlap, image loading, PNG format and final 1080 × 1920 dimensions. Final visual inspection checked the complete graphic, readable source/uncertainty, unaltered coin face/lettering, coherent brass installation and unobscured comparison. All checks passed.

- Export: `exports/retail-sales-2026-11-18.png`
- SHA-256: `c01c4a2c71e856a7e2c66be2cdf9849f552b571f670d22cc13c145775d079b72`
- Layout, fonts, exact prompt, source record and hashes: `briefs/retail-sales-2026-11-18-layout.json`
- No Git actions performed; publishing is handled by the coordinating agent.
