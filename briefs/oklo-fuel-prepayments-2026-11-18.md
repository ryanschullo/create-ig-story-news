# Oklo fuel prepayments — November 18, 2026

Category: **NUCLEAR ENERGY INVESTING**. Selection **10** from the November 18 article list.

## Editorial focus

Oklo's November 17 SEC filing disclosed a contract calling for two prepayments totaling **$35 million** to Centrus, credited against future purchases. The agreement supports development of commercial uranium-enrichment capacity at Piketon, Ohio. Enrichment purchases for deliveries during **2029–2031** use take-or-pay terms, subject to conditions.

The agreement was signed **November 11** and announced November 12. The graphic explicitly distinguishes the filing date from the signing date. The $35 million is not the total contract value. The graphic makes no assertion about how much has already been paid, because the first payment date is redacted, and it does not imply delivered fuel or an operating Oklo reactor.

## Sources

- [Oklo SEC 8-K filed November 17](https://www.sec.gov/Archives/edgar/data/1849056/000184905626000055/oklo-20261111.htm), Item 1.01.
- [Underlying redacted HALEU Supply Agreement](https://www.sec.gov/Archives/edgar/data/1849056/000184905626000055/redacted-oklohaleusupply.htm).
- [Techi discovery article, November 17](https://www.techi.com/oklo-centrus-haleu-fuel-contract-prepayment-cash/).

Detailed facts, scope and URLs are saved in `briefs/oklo-fuel-prepayments-2026-11-18-source.json`.

## Design and production

- 1080 × 1920 Story with all news copy and panels inside x104–961 / y164–1536.
- Fresh image-generated graphite and navy nuclear-fuel facility with teal process lighting and a closed fuel transport cask. Conceptual infrastructure, not a photograph of an actual facility. No weapons.
- Actual Lato Black 900 headings and Georgia 400 body/source text. Minimum authored text 33px; body at least 35px; headlines at least 51px. Brand is one 35px line.
- Original Moneyberg coin uniformly scaled into the physical brass recess on the upper-right wall with matching shadow and gentle scene lighting. Entire rim remains inside the upper 75% of the canvas; original portrait and lettering are preserved.
- No generated text, invented chart, recreated coin, or background-production footer.
- Browser composition via HTML/CSS and Playwright. No Python pixel editing; Georgia remains outside the repository.

## Reproduction

```sh
/tmp/nov18-news-venv/bin/python scripts/render_oklo_fuel_prepayments_2026_11_18.py --georgia-font /tmp/nov18-fonts/Georgia.TTF
```

Deliverables: `assets/layouts/oklo-fuel-prepayments-2026-11-18.html`, `assets/oklo-fuel-prepayments-background-2026-11-18.png` and `.md`, `briefs/oklo-fuel-prepayments-2026-11-18-layout.json`, and `exports/oklo-fuel-prepayments-2026-11-18.png`.

## Verification

Chromium validation passed for all 15 text elements and four content panels: required bounds, text-size floors, actual font families and weights, no text overlap, no coin/content overlap, full original coin aspect ratio and upper-75% placement, and 1080 × 1920 output. Final PNG was visually reviewed for legibility and accurate coin integration. An independent factual review changed the timing caption to **ENRICHMENT DELIVERY WINDOW**, matching the SEC's delivery timing rather than suggesting when orders or payments occur.
