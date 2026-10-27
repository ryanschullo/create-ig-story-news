# Retail options share — Astra redesign — October 26, 2026

Final: `exports/retail-options-share-2026-10-26-astra.png`, **1080 × 1920**.

This is a new art-direction version of the existing October 26 story for the
user's requested comparison after switching models. Earlier exports remain intact.
No fresh news claim or changed observation period is implied by the redesign.

## Source and unchanged facts

User-selected post:
https://x.com/KobeissiLetter/status/2114881746621575597

The verified original source record is `briefs/retail-options-share-2026-10-26.md`.
The post was published October 27, 2026, 00:47:55 UTC: October 26 at 7:47:55 p.m.
CDT. The artwork retains the October 26 post date.

- Retail options share nears a record: **61% of total options volume on Citadel
  Securities’ platform, last week** according to the post.
- Increase: **16 percentage points in 12 months**. This is not 16% growth.
- Attribution: **The Kobeissi Letter, citing Citadel Securities**.
- Platform scope is visible alongside the large 61%; no all-U.S.-market claim,
  absolute-volume record, dollar-notional claim or investment recommendation.
- The original source chart is embedded whole, unchanged. Its title, axes,
  labels, source and TKL credit remain visible. No underlying series was obtained
  and no data was inferred from the plotted line.

## Visual direction

The design changes from the prior violet glass architecture to a tactile
analyst's desk: dark-plum leather, black walnut, restrained brass and teal type.
The original chart moves into the upper-middle as the primary visual; the 61%
and percentage-point comparison form a compact summary below. Thin editorial
rules replace rounded UI cards. All authored text uses actual **Lato Black 900**
or **Georgia**, verified through font metadata and Chromium's rendered font records.

The original Moneyberg PNG is seated inside a brass-lined recess in the generated
leather desk pad. Contact shadow and non-destructive material lighting match the
surrounding leather and metal. The complete original coin is **208 × 208 px at
x780–988, y1142–1350**, wholly above y1440, with no warp, redrawn portrait or
retyped lettering. It does not overlap news copy or the original chart.

The generated background is decorative scene imagery. It was generated with
imagegen and copied unchanged from:
`/workspace/generated_images/exec-929fd539-7494-4106-9f65-b74d7dbe7ba9.png`
to `assets/options-investing-background-astra.png`.
Its natural size is 941 × 1672 and it is displayed with proportional cover on
1080 × 1920. It contains no invented prices or numerical trading charts.
Background-production credit is omitted from the graphic per the latest skill;
news-source and post-date attribution remain visible.

## Verification

- All **14 text elements, five panels/rules and the full source chart** fit
  within x104–961, y164–1536. The footer ends at y1508.
- Original chart rendered at x112, y531, width841, height566.046875;
  its full 1560:1050 ratio is preserved.
- Original coin SHA-256: `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Original chart SHA-256: `bfb420948ae75d489a88fb50a17efb66f6ee5086160a4820d4e22b896c3f97ca`.
- Background SHA-256: `49c4501cbf4db25c886e53d8d60f6bc625eaeb81069c1fc64bdc31aea956105c`.
- Final PNG SHA-256: `70dcba353496fb6a083c449d40382174b594f875cbf906d45aefc6585f24efe9`.
- Actual Lato Black and Georgia were verified on every authored text element.
  Georgia remains runtime-only and is not distributed in committed files.
- No historical exports, master assets or shared skill rules were changed.

Renderer: `scripts/render_retail_options_astra_story.py`.
HTML: `assets/layouts/retail-options-share-2026-10-26-astra.html`.
Measurements and font proof: `briefs/retail-options-share-2026-10-26-astra-layout.json`.

```sh
python scripts/render_retail_options_astra_story.py --georgia-font /path/to/Georgia.TTF
```
