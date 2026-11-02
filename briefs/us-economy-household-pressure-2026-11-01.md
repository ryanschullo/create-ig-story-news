# Growth is strong. Households feel squeezed.

User-selected article: [The American Economy Rockets Ahead, but Doesn't Take Everyone With It — WSJ](https://www.wsj.com/economy/us-economic-data-growth-9a4f7690). Category: **CONSUMER SENTIMENT**. Edition November 1, 2026, America/Chicago.

## Access and attribution

The full WSJ article was not accessible through ordinary public HTTP (proxy 403). No restrictions were bypassed. The user was informed before production that the graphic would use WSJ's public framing supported by independently verified official figures.

WSJ's [own public X post](https://x.com/WSJ/status/2117099529489060139) was read in full and links the exact requested article. It says voters benefit from a stable job market and higher salaries while remaining frustrated by the cost of living. That supports the central editorial framing, not any specific numeric claims. The article's November 1 date was corroborated by discovery metadata; the publisher's X post appeared November 1 at 9:40 p.m. CST.

The graphic clearly separates **Data: BEA · University of Michigan** from **Context: WSJ · November 1, 2026**. It is an original synthesis, not a claimed reproduction of the inaccessible article. No unverified article anecdotes, subgroup statistics, polling figures or quotes are included.

## Independently verified figures

1. **Q3 real GDP +3.4%:** [BEA's October 29 advance estimate](https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026). Seasonally adjusted, quarter-over-quarter annualized real growth, compared with +2.2% in Q2. Not year-over-year growth, nominal growth or an actual 3.4% increase within three months. The graphic retains “Q3 2026 · Annualized” and “Advance estimate.”
2. **October consumer sentiment 48.0, down 10.4% year over year:** [University of Michigan final October results](https://www.sca.isr.umich.edu/). October 2026 index 48.0 versus October 2025 index 53.6; the table reports −10.4% year over year. This is an index, not 48% of respondents. The accompanying commentary identifies purchasing power, affordability and interest-rate concerns. The graphic retains the October period and final status.
3. **Real disposable personal income −0.3% from August to September:** [BEA's October 29 income/outlays release](https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026). This is total inflation-adjusted income after personal current taxes, a monthly aggregate. It is not median household income, annual wage growth or proof that every household lost income. The graphic uses “Total inflation-adjusted income after taxes fell 0.3% from August to September.”

The two large figures are separate labeled measures, without a shared chart axis. The data do not establish a specific rich-versus-poor split; the graphic makes no such claim. Household sentiment is distinguished from measured GDP and income.

Full source bodies were read and archived temporarily in `/tmp/wsj-growth-primary/`; publisher-summary research in `/tmp/wsj-growth-syndication/`. Public primary links and durable findings are recorded above.

## Design and production

- `exports/us-economy-household-pressure-2026-11-01.png`: **1080 × 1920**.
- Subject-specific warm ivory, petrol teal and muted burgundy design, with retail-store doorway, groceries, wallet and soft city architecture. These are decorative generated imagery, not a photograph of an economic event.
- Text-free background generated with the image tool; unchanged source copied to `assets/us-economy-household-pressure-background-2026-11-01.png`. Complete prompt in its companion Markdown file.
- Actual Lato Black 900 for headlines, metrics, date and labels; actual Georgia 400 for explanatory text, captions and sources. Headline 72 px; numbers 118/123 px; body 35 px; all remaining text at least 33 px. The compact one-line brand is 35 px.
- All news content and panels fit in x=104–961, y=164–1536. A light source backing protects legibility over the lower scene. No background-production footer.
- Exact approved original coin `assets/moneyberg-coin-original.png` is uniformly scaled into the doorway's brass recess. Full portrait/rim/lettering retained; compatible lighting and contact shadows establish physical integration. Master hash unchanged: `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Complete coin bounds: x=929–1033, y=593–697, wholly within the upper three-quarters. It overlaps no news text.
- Georgia is runtime-only, verified family/weight and browser use, not committed or redistributed. Python orchestrates Chromium rendering and verifies layout; no pixel-editing library is used.

Renderer: `scripts/render_us_economy_household_pressure_2026_11_01.py`. Editable layout: `assets/layouts/us-economy-household-pressure-2026-11-01.html`. Machine-readable audit: `briefs/us-economy-household-pressure-2026-11-01-layout.json`.

Automated validation checks actual rendered fonts, minimum sizes, complete bounds, PNG dimensions, original coin hash/aspect/position and scene integration. Independent visual/factual review passed; the final income sentence explicitly states the August-to-September comparison.

## Reproduction and delivery

```sh
python scripts/render_us_economy_household_pressure_2026_11_01.py \
  --georgia-font /path/to/Georgia.TTF
```

Publish the committed export through `publish-graphic-download.yml`, edition `2026-11-01`, filename `us-economy-household-pressure-2026-11-01.png`. Verify anonymous HTTP 200, attachment filename, PNG dimensions and exact bytes before delivering:

https://github.com/ryanschullo/create-ig-story-news/releases/download/stories-2026-11-01/us-economy-household-pressure-2026-11-01.png
