# Rush to hedge the AI selloff — November 5, 2026

Category: **OPTIONS INVESTING**. User selected item2 from the saved November5 shortlist. Story date is November5 in America/Chicago; host UTC date is November6.

## Sources and verified facts

- Reuters, full public AOL syndication: https://www.aol.com/articles/wall-street-fear-gauge-jumps-183219000.html . Current headline: “Phones 'explode' on Wall Street as 'steamroller' shows up for the AI trade.” Published November5 at12:32:19p.m.CST, updated5:03:47p.m.CST (`2026-11-05T18:32:19Z` / `23:03:47Z`). Full public body read. Direct Reuters returned401 in initial research; no restricted body or access-control bypass was used.
- Original Reuters canonical for identification: https://www.reuters.com/business/wall-street-fear-gauge-jumps-most-since-liberation-day-ai-trade-stumbles-2026-11-05/ . Do not claim direct access to this version.
- Cboe primary daily index data: https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv . The primary CSV independently matches the report: **November5 VIX close28.18**, intraday high28.36; **November4 close16.61**. The graphic displays the closing level, not the intraday high.
- Exact two-day excerpt saved as `assets/data/vix-ai-hedging-2026-11-05.csv`. Original full research CSV in `/tmp/nov5-options/VIX_History.csv`, SHA256 `89d2c4f6015903fa1c86f0ace7d37393d2eb9fd037183688eb35bdeb25b2f0b7`. Excerpt preserves source values and columns; no chart was requested or fabricated.
- Reuters: “put premiums ... running at about two times what is typical across index products, according to options analytics service Mercury Alerts.” The graphic preserves **INDEX PUT PREMIUMS**, **ABOUT2×TYPICAL**, and **Mercury Alerts, via Reuters**. This is an attributed report, not independently reconstructed Mercury Alerts data. The article does not identify an exact observation time for this estimate, so it is not represented as a precise closing statistic.
- This is not a claim that all options volume, open interest, every put contract, or realized volatility doubled. The VIX is option-implied expected S&P500 volatility; it does not predict a certain crash. No investing recommendation is made.
- Underlying accessible text archives: `/tmp/nov5-options/vix-aol.html`, `.txt`, `-metadata.json`; full research dossier `/tmp/nov5-options.md`. The broader selloff has a separate market-wrap graphic, so this graphic concentrates on hedging and volatility.

## Approved copy

MONEYBERG NEWS BRIEF

OPTIONS INVESTING

NOVEMBER 5, 2026

**Rush to hedge / the AI selloff**

**28.18**

VIX CLOSING LEVEL

Up from 16.61 a day earlier.

Investors seek downside protection.

INDEX PUT PREMIUMS

**ABOUT 2× TYPICAL**

Mercury Alerts, via Reuters

VIX: Cboe • Report: Reuters

November 5, 2026

## Design and validation

- Export: `exports/vix-ai-hedging-2026-11-05.png`, checked1080×1920.
- Template: `assets/layouts/vix-ai-hedging-2026-11-05.html`.
- Renderer: `scripts/render_vix_ai_hedging_2026_11_05.py`.
- Machine audit: `briefs/vix-ai-hedging-2026-11-05-layout.json`.
- Background and exact image-tool prompt: `assets/vix-ai-hedging-background-2026-11-05.png` and `.md`.
- Ink/plum/indigo workstation environment with restrained teal accents. Large VIX close and separate index-put-premium panel emphasize the sourced metrics. Generated environment contains no fabricated chart or market data, and does not document a specific venue/event.
- Coin: canonical `assets/moneyberg-coin-original.png`, SHA256 `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`, original2084×2084, unchanged. Uniformly scaled in the generated workstation's round metal recess, with compatible lighting and contact shading. Complete coin is within upper75% of canvas and clear of all news text.
- Actual font metadata and Chromium platform-font checks verify Lato Black900 and Georgia400; Georgia is runtime-only and not redistributed. All authored text is33px or larger; body40px, headlines85px, compact one-line brand35px. All news text/panels fit x104–961,y164–1536. Pairwise text-range overlap checks pass.
- Final PNG visually inspected for clear content, exact circular coin proportions and integrated scene placement. No background-production footer appears.

Reproduction (requires Chromium, Playwright, fontTools and authorized Georgia font):

```sh
python scripts/render_vix_ai_hedging_2026_11_05.py --georgia-font /path/to/Georgia.TTF
```
