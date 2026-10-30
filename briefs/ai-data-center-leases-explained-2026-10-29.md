# Wall Street's AI landlord bet — explanation added

**Category:** ENERGY & INFRASTRUCTURE

**Edition:** October 29, 2026, America/Chicago; revision retains the original
story's edition date.

**Export:** `exports/ai-data-center-leases-explained-2026-10-29.png`

## Requested revision and sourcing

The user requested that the existing Wall Street AI graphic include this exact
sentence:

“Wall Street’s top alternative asset managers are betting on the AI boom by owning the infrastructure behind it and locking in rent through long-term leases.”

This is also the opening sentence of Reuters' report, checked against the full
article and independently reviewed. The graphic includes it verbatim, with
line breaks, directly below the headline and before the lease figures.

Reuters, Arasu Kannagi Basil and Manya Saini, October 29, 2026, 12:04 p.m. CDT:
https://d2233.cms.socastsrm.com/2026/10/29/wall-streets-ai-bet-own-the-infrastructure-collect-the-rent/

Canonical Reuters address:
https://www.reuters.com/business/finance/wall-streets-ai-bet-own-infrastructure-collect-rent-2026-10-29/

Full-text research archive: `/tmp/oct29-ai-jobs/infrastructure.txt`.
Original brief: `briefs/ai-data-center-leases-2026-10-29.md`.

- Blue Owl describes typical **15–20-year** infrastructure leases.
- Blackstone describes the vast majority of its portfolio's **initial**
  data-center lease terms as **15–20 years**.
- Ares separately describes **12–15-year** pre-leased developments.
- Contracted rent is not guaranteed investment income. The existing concise
  construction/tenant-risk line remains. Reuters quotes Moody's on these
  exposures alongside concentration, residual-value and circular-financing risk.
- No numerical chart, capacity totals, market-price snapshots, or stock-return
  implications are added.

## Exact graphic copy

MONEYBERG NEWS BRIEF

ENERGY & INFRASTRUCTURE

OCTOBER 29, 2026

Wall Street’s / AI landlord bet

Wall Street’s top alternative asset managers are betting on the AI boom by owning the infrastructure behind it and locking in rent through long-term leases.

DATA-CENTER LEASE TERMS

15–20 YEARS

Blue Owl: typical lease term

Blackstone: most initial leases

12–15 YEARS

Ares: pre-leased developments

Construction and tenant risks / still matter.

Source: Reuters • Oct. 29, 2026

Lease terms reported by managers

## Design, provenance and checks

- The original graphite/steel-blue/cyan server-cabinet design is reflowed
  around the added explanation. Lease figures now occupy more compact rows.
- The image tool edited the original background to extend the plain dark
  reading surface downward, keeping sources clear of the server aisle.
- Input: `assets/ai-data-center-leases-background-2026-10-29.png`.
- Edited image-tool output:
  `/workspace/generated_images/exec-18965db3-a935-4c81-8fa7-2a6ddce85d5f.png`.
- Saved unchanged as
  `assets/ai-data-center-leases-explained-background-2026-10-29.png`.
- Edit prompt: `assets/ai-data-center-leases-explained-background-2026-10-29-prompt.txt`.
  Initial and edit prompts are retained in the renderer and layout audit.
- The generic data-center scene is decorative illustration, not a documentary
  photograph of a named firm's buildings. No production footer appears.
- Original coin remains `assets/moneyberg-coin-original.png`, verified SHA-256
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
  It is installed in the server cabinet's brass recess with matching cool
  lighting and contact shading, preserving the exact portrait and lettering.
- Coin bounds **x=819–1033, y=799–1013**, uniformly scaled to **214 × 214 px**,
  wholly within the upper 75% and without news overlap.
- Layout: `assets/layouts/ai-data-center-leases-explained-2026-10-29.html`.
- Renderer: `scripts/render_ai_data_center_leases_explained_2026_10_29.py`.
- Audit: `briefs/ai-data-center-leases-explained-2026-10-29-layout.json`.
- All 20 authored text nodes use actual Lato Black 900 or Georgia 400,
  checked from font metadata and Chrome's per-node font report.
- The new explanation is **38 px Georgia**. Other body copy is **35 px**;
  sources, date and category **33 px**; brand **35 px**; headlines **78 px**;
  lease figures **80/51 px**. Every element meets the current 33/35/51 px rules.
- All text and three separator panels fit inside **x=104–961, y=164–1536**.
  Source line ends at y=1493 on the dark reading wall. No clipping or overflow.
- The exact requested sentence is verified against the browser text nodes,
  joined with spaces; no words omitted or paraphrased.
- Georgia stays runtime-only and is not redistributed. Python orchestrates
  browser rendering and validation without editing image pixels.

Reproduce:

```sh
python scripts/render_ai_data_center_leases_explained_2026_10_29.py \
  --georgia-font /path/to/Georgia.TTF
```

Final PNG: **1080 × 1920**, **2,242,507 bytes**.
SHA-256: `a3fb4902405c516d96367864cfc513673936740cef3bf518974dc1afbb9ad0b4`.
