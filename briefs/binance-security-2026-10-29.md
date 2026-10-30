# Binance probes suspected hack — October 29, 2026

User-selected article. Edition uses **America/Chicago**, where the BBC's
October 30 UTC timestamps fall on the evening of **October 29**.
The graphic uses **DEVELOPING** as a status, without assigning this crypto
security story to an unrelated category or changing the saved topic registry.

## Reporting and scope

BBC News, Osmond Chia, **Crypto worth billions frozen after suspected Binance hack**:
https://www.bbc.com/news/articles/cwg7xp8kx4v5o

Full body read from HTTP 200 and independently refetched with unchanged copy
and metadata. Local research snapshots: `/tmp/bbc-cwg7xp8kx4v5o.html` and
`/tmp/bbc-cwg7xp8kx4v5o.txt`.

- Published `2026-10-30T00:37:59.699Z`, or October 29, 7:37 p.m. CDT.
- Updated `2026-10-30T01:20:57.221Z`, or October 29, **8:20 p.m. CDT**.
- BBC reports that Binance said it froze **around $3 billion in digital
  assets to prevent theft** while investigating a security issue.
- Binance said all deposits and withdrawals were **temporarily suspended**
  while teams conducted security checks.
- The incident is described as a **suspected hack**. Its full scale remains
  unclear. This is not a report of $3 billion in confirmed theft or losses.
- BBC also reports about $2.4 billion frozen by Tether and Circle. That figure
  is omitted: the report does not establish whether it overlaps Binance's
  approximately $3 billion, so adding them would be unsupported.
- Binance's promises to cover losses and assurances about user funds are
  company claims, not independently verified guarantees. They are omitted.
- Bitcoin's reported approximately 5% decline is omitted because it is an
  evolving snapshot without a precise observation time in the article.
- The graphic attributes the report to **BBC News, citing Binance**. The BBC
  story does not link the underlying company statements; this work does not
  claim to have independently authenticated Binance's operational status.

## Graphic copy

MONEYBERG NEWS BRIEF

OCTOBER 29, 2026

DEVELOPING

Binance probes / suspected hack

~$3B / ASSETS FROZEN

Binance says it froze digital / assets to prevent theft.

DEPOSITS & WITHDRAWALS

Temporarily suspended.

Full scale of the incident / remains unclear.

Source: BBC News, citing Binance

Updated Oct. 29, 8:20 p.m. CDT

## Design and reproducibility

- Export: `exports/binance-security-2026-10-29.png`, **1080 × 1920**.
- Layout: `assets/layouts/binance-security-2026-10-29.html`.
- Renderer: `scripts/render_binance_security_2026_10_29.py`.
- Audit: `briefs/binance-security-2026-10-29-layout.json`.
- Subject-specific graphite, yellow and warm metal security-vault scene,
  with prominent frozen-assets figure. The background is illustrative, not
  documentary evidence of Binance facilities or a confirmed theft.
- Text-free background generated using the image tool:
  `/workspace/generated_images/exec-3b156c3e-a461-4f43-8dd3-18e9324bb2ff.png`,
  copied unchanged to `assets/binance-security-background-2026-10-29.png`.
  Original generation dimensions: 941 × 1672. Browser composition produces
  the verified 1080 × 1920 final PNG.
- Exact prompt: `assets/binance-security-background-2026-10-29-prompt.txt`,
  also preserved in the renderer and audit.
- Original coin: `assets/moneyberg-coin-original.png`, unchanged 2084 × 2084
  master, SHA-256
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Uniform 214 × 214 px coin, bounds **x=833–1047, y=800–1014**. It is seated
  inside the generated vault column's brass recess with contact shading and
  compatible lighting, preserving original portrait, rim lettering and round
  proportions. Entire coin is above y=1440 and clear of news text.
- Actual **Lato Black 900** and **Georgia 400**, checked from font metadata
  and Chrome's per-node font report. Georgia is runtime-only, not redistributed.
- All 15 text nodes meet the **33 px** universal floor. Body is **37–39 px**,
  headlines **82 px**, hero **220 px**, single-line brand **35 px**.
  Renderer enforces headline ≥51 px and body ≥35 px separately.
- All text and both separator panels are within **x=104–961, y=164–1536**.
  Attribution is positioned on the dark wall above the bright vault mechanism.
- No background-production footer; provenance is documented here.
- Python orchestrates HTML/CSS and browser screenshots, without pixel editing.

Reproduce:

```sh
python scripts/render_binance_security_2026_10_29.py --georgia-font /path/to/Georgia.TTF
```
