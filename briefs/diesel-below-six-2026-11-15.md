# Diesel falls below $6 — November 15, 2026

- Category: OIL & GAS.
- Export: `exports/diesel-below-six-2026-11-15.png`, 1080 × 1920.
- User-selected article: https://www.marketscreener.com/news/us-diesel-below-6-a-gallon-at-2-month-low-on-easing-tensions-weaker-demand-ce785ededd80f520

## Diesel reporting

The selected MarketScreener URL returned HTTP 403 and the Reuters original returned 401. The full Reuters report was read through two public republications, without bypassing access controls:

- New Straits Times: https://www.nst.com.my/amp/business/economy/2026/11/1578066/us-diesel-below-us6-gallon-2-month-low-easing-tensions-weaker — November 15, 2026, 09:56:05 +08:00 (01:56:05 UTC).
- Economic Times: https://m.economictimes.com/news/international/business/us-diesel-below-6-a-gallon-at-2-month-low-on-easing-tensions-weaker-demand/articleshow/135845300.cms — November 15, 2026, 07:00 +05:30 (01:30 UTC).

Both bodies report **GasBuddy's U.S. national average retail diesel price of $5.998 per U.S. gallon on Saturday, November 14, 2026**. Diesel first exceeded $6 on September 10; it fell back below that threshold after roughly two months. The report calls this a two-month low. The same GasBuddy series peaked at **$6.519 per gallon on September 22, 2026**. The graphic preserves all three decimals and does not round $5.998 to $6.00 while asserting a below-$6 reading.

Reuters attributes easing prices to lower crude prices, easing geopolitical tensions, seasonal demand weakness, and refinery production recovering as maintenance finishes. The graphic summarizes easing tensions and weaker demand without claiming the war ended, the change is permanent, or a measured consumer-inflation decline occurred. No derived percentage from the diesel peak is displayed. The article contains no chart; its documentary pump photo is not used. This graphic uses a conceptual background.

### Tracker distinction

GasBuddy's own public pages were blocked, so the observation is verified through Reuters reporting, not independently retrieved from the tracker. AAA's accessible primary table for November 14 gives **$6.0366**, a different series. AAA does not corroborate the $5.998 figure and is not mixed into this graphic. **GasBuddy U.S. retail average • Nov. 14** is visible immediately below the hero price.

## Required Brent and WTI context

Both benchmarks are **Friday, November 13 final futures settlements**, not Sunday live prices or diesel per-gallon quotes. They appear in a separately labeled context section.

| Benchmark | Contract | Settlement, US$/barrel | Daily change |
| --- | --- | ---: | ---: |
| Brent | January 2027 | $95.84 | +$0.02 / +0.02% |
| WTI | December 2026 | $88.56 | −$0.18 / −0.20% |

Full public report: https://energynow.com/2026/11/oil-prices-fall-for-second-straight-week-as-global-supply-surplus-emerges-wti-closes-at-88-56-brent-at-95-84/ — November 13, 2026, 15:00 MST. It explicitly supplies the common Friday settlement basis, both delivery months and changes versus Thursday. Daily percentages are reported values, not calculated from rounded prices. EnergyNow says its dollar settlements come from Reuters; direct exchange settlement tables were not independently retrieved.

Both dollar settlements are corroborated in the full public November 15 Peninsula article citing the Al-Attiyah Foundation weekly energy review: https://thepeninsulaqatar.com/article/15/11/2026/oil-prices-set-for-second-straight-weekly-drop-on-signs-of-growing-supply-surplus . It does not supply the contract months or exact daily changes; those remain attributed to EnergyNow.

The graphic includes **CRUDE CONTEXT • NOV. 13 SETTLEMENTS**, separate Brent and WTI labels with contract months, both prices, daily percentage changes and US$/BBL units. Thus the November 14 diesel reading and the November 13 crude settlements are not presented as simultaneous observations of the same instrument.

## Design, assets and validation

Petroleum charcoal, steel and amber industrial design with a conceptual diesel nozzle, tanker truck and refinery. The exact imagegen prompt and background provenance are retained in `assets/diesel-below-six-background-2026-11-15.md`. No numbers, chart or logo were generated as factual imagery.

The permanent original coin `assets/moneyberg-coin-original.png` remains unmodified and is uniformly seated in the upper-right equipment recess with matching warm light and CSS contact shadows. Its full rim is inside the upper 75% of the final canvas, with no news overlap.

Actual Lato Black 900 and Georgia 400 are rendered using Chromium. Georgia is runtime-only and not redistributed. The renderer checks font metadata and actual browser fonts; 33 px minimum authored type, 35 px body and 51 px headline; full content bounds x104–961/y164–1536; overlap; coin integrity and proportions; required benchmark values and time basis; and 1080 × 1920 PNG dimensions. Audit: `briefs/diesel-below-six-2026-11-15-layout.json`.

```sh
/tmp/moneyberg-render-venv/bin/python scripts/render_diesel_below_six_2026_11_15.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

Runtime source evidence was saved in `/tmp/diesel-nov15/` and `/tmp/oil-context-nov15/`. This brief retains the substantive source facts, links, access limitations and observation dates. No background-production footer appears on the graphic.
