# Medical-care inflation since 2000 — November 1, 2026

User-selected [Kobeissi Letter post](https://x.com/KobeissiLetter/status/2117106764550214038), with the explicit request to include the graph. The full substantive public post and original media were retrieved using ordinary public HTTP. Visible post timestamp is November 2, 04:09 UTC, which is **November 1, 10:09 p.m. CST**; the graphic follows the saved America/Chicago news-day preference.

Category: **CONSUMER SENTIMENT**, covering household affordability and health-care costs.

## Chart and factual scope

The post and attached chart report cumulative changes since 2000:

| Series | Change shown |
| --- | ---: |
| Medical care | +132% |
| Shelter | +127% |
| Food | +112% |
| All-items CPI | +99% |

These figures are attributed to **The Kobeissi Letter's chart citing the Bureau of Labor Statistics**. The underlying BLS series and exact starting/ending months were not independently reconstructed. Do not change the scope to year-over-year growth, monthly inflation, medical insurance premiums alone, or all health spending. The original graph labels the period “since 2000,” with a final 2026 year tick; no more precise endpoint is invented.

The post calls medical care the largest increase among major spending categories. The graphic deliberately omits that universal ranking: the provided graph compares only its four selected series. It also omits the unverified “never been higher” superlative.

Original chart URL:
https://pbs.twimg.com/media/HV4uQtmWAAA5By3?format=jpg&name=orig

Stored unchanged as `assets/medical-care-inflation-chart-original-2026-11-01.jpg`, **1560 × 1041**, 128,926 bytes, SHA-256:
`9c0afd46c735874a946edf2ff7030fcd77d786d2c4a390263fa379eb4550f080`.

The full image is displayed at **857 × 571.875 px**, x=104–961, y=647–1218.875, retaining its original aspect ratio. Title, y-axis, year ticks, all four lines and their endpoint labels, legend, red source annotation, TKL logo and source/follow credits remain visible. It is not cropped, redrawn or relabeled. Its embedded original fonts are preserved. Large authored headline/comparison text makes the main 132% versus 99% takeaway readable independently of the smaller embedded chart type.

## KFF verification and correction

Primary public source: [KFF — Americans' Challenges with Health Care Costs](https://www.kff.org/health-costs/americans-challenges-with-health-care-costs/), page updated October 23, 2026. Full body and the source labeling of its original figure were read.

The relevant finding is **three in ten insured adults ages 18–64** who skipped or postponed needed care due to cost **in the 12 months before the survey**. It comes from the **KFF Survey of Health Access and Caregiving, May 4–26, 2026**.

The social post omits the age restriction. The graphic restores **ages 18–64** and identifies the May 2026 survey, rather than presenting it as a fresh survey of all insured adults. The separate all-adult figure is 28%, not the denominator used here. The graphic presents the survey alongside the price chart without asserting that the chart proves causation.

## Final copy

- MONEYBERG NEWS BRIEF
- CONSUMER SENTIMENT
- NOVEMBER 1, 2026
- Medical care prices / up 132% since 2000
- Overall CPI: +99% over the same period.
- Full original chart
- 3 in 10 insured adults ages 18–64 delayed / or skipped needed care because of cost.
- Prior 12 months · KFF, May 2026 survey
- Chart: The Kobeissi Letter · BLS data

## Design, rendering and QA

Deep petrol teal, muted sage and brushed clinical steel distinguish the health-care subject. A decorative medical still life includes a stethoscope and unbranded containers; it is not evidence of actual costs or an actual event photograph. The text-free background was generated with the image tool, copied without alteration to `assets/medical-care-inflation-background-2026-11-01.png`; its exact prompt is in the companion Markdown file.

The exact approved original `assets/moneyberg-coin-original.png` is uniformly scaled into the clinical equipment frame's brass mounting seat. Compatible illumination, rim and contact shading establish scene integration. The master is unchanged, with the original portrait and lettering intact. Full coin bounds are **x=900–1046, y=374–520**, entirely within the upper 75% and clear of text and the chart.

Export: **1080 × 1920** PNG. All ten authored text nodes and all three news panels fit inside x=104–961, y=164–1536. Compact brand is 35 px; headlines 68/76 px; body 35 px; labels, survey qualifier and source 33 px. Lato Black 900 and Georgia 400 are verified from the actual font files and Chromium platform-font reports. Original chart typography is retained as artwork. Georgia is used only at runtime and is not redistributed.

Dark backing below the chart protects survey and source contrast. The renderer verifies original chart and coin hashes, chart aspect and dimensions, the full coin's upper-75% bounds, lack of coin overlap, text sizes, actual browser fonts, canvas bounds and final PNG dimensions. The final image was visually inspected for chart preservation, accurate endpoint figures, survey scope, readable copy and original coin fidelity.

Python orchestrates Chromium and validation; no Python image-pixel editing is used.

```sh
python scripts/render_medical_care_inflation_2026_11_01.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

Detailed source snapshots are in temporary research folders `/tmp/kobeissi-2117106764550214038/` and `/tmp/kff-care-verify/`; durable URLs, definitions and verified figures are preserved above. Machine-readable rendering results are in `briefs/medical-care-inflation-2026-11-01-layout.json`.

The root agent handles commit, GitHub release publication and anonymous remote-byte verification before delivery. This brief does not claim publication.
