# Nvidia / FT intelligence report — November 7, 2026
**Category:** AI INVESTING
**Reporting edition:** November 7, 2026, America/Chicago.
**Export:** `exports/nvidia-ft-report-2026-11-07.png`.

## User-selected story and source access
User URL:
https://www.ft.com/content/a55a2a22-4479-4f93-a445-6147a5c6d790?syn-25a6b1a6=1

Canonical:
https://www.ft.com/content/a55a2a22-4479-4f93-a445-6147a5c6d790

Search identifies the FT headline as “US believes Nvidia’s Huang had romantic relationship with alleged Chinese spy.” The supplied and canonical FT pages returned HTTP403. Direct FT full-text access is not claimed. The same report and the company response were verified in two fully accessible public follow-ups:

1. **TechCrunch, Anthony Ha:** “Megaspeed exec was recruited to spy on Nvidia CEO, according to US intelligence memo.”
   https://techcrunch.com/2026/11/07/chinese-exec-was-recruited-to-spy-on-nvidia-ceo-according-to-us-intelligence-memo/
   Published November 7 at 21:17:08 UTC / 3:17:08 p.m. CST; updated 21:17:49 UTC. Full body HTTP200. This article links the exact FT article supplied by the user.
2. **Bloomberg News, syndicated by NDTV:**
   https://www.ndtv.com/world-news/woman-who-targeted-nvidia-ceo-jensen-huang-was-recruited-by-top-china-spy-agency-report-12295987
   Published November 7 at 06:15:22 UTC / 12:15:22 a.m. CST; updated 06:36:34 UTC. Full body HTTP200. NDTV explicitly credits a syndicated feed to Bloomberg News.

Bloomberg says the FT report appeared Friday night, November 6. The exact original FT publication timestamp was not independently retrieved. The graphic therefore identifies **follow-up coverage on November 7**, rather than claiming FT first published on that date.

## Verified claims and limitations
TechCrunch reports that a U.S.-intelligence-based memo alleged an executive at Singapore-based Megaspeed had been recruited by China's Ministry of State Security to spy on Nvidia CEO Jensen Huang. It says FT subsequently reported that the memo also alleged a romantic relationship between Huang and that executive.

These are attributed allegations. No independent finding of espionage, classified-information transfer, illegal chip diversion, or a romantic relationship is asserted. The graphic does not depict a purported meeting or add a share-price effect.

Bloomberg reports that when asked about the FT relationship allegation, Nvidia referred to Huang's prior comments describing a typical business relationship. His comments about “normal and not unusual” dealings were made in an interview the previous week, not a new blanket denial issued November 7.

Nvidia also stated: “We neither have nor share classified information with customers.” The graphic paraphrases that response accurately and gives it the same body font size and panel dimensions as the allegation summary. It does not claim this statement independently disproves every allegation.

The executive is not named on the graphic; the business context is sufficient. A separate New Matrix chip-export report mentioned by TechCrunch is excluded rather than conflated with the FT relationship allegation.

## Final on-graphic copy
- MONEYBERG NEWS BRIEF
- AI INVESTING
- NOVEMBER 7, 2026
- FT: MEMO ALLEGES
- HUANG RELATIONSHIP
- WITH SUSPECTED SPY
- THE REPORT
- U.S. intelligence reportedly linked
- Nvidia CEO Jensen Huang romantically
- to a Megaspeed executive suspected
- of working for Chinese intelligence.
- NVIDIA’S RESPONSE
- Nvidia points to Huang’s description
- of a typical business relationship
- and says it neither has nor shares
- classified information with customers.
- Sources: FT, via TechCrunch / Bloomberg
- Follow-up coverage • November 7, 2026

## Design and validation
Fictional GPU/server architecture uses graphite and muted emerald, with no generated people or depiction of the alleged events. The exact approved Moneyberg coin is integrated into a physical brass wall recess, with compatible lighting and contact shadow. It is uniformly scaled to **138 × 138**, x916, y611–749, entirely within the upper three-quarters of the story.

- Background: `assets/nvidia-ft-report-background-2026-11-07.png`, 916 × 1717, 1,957,368 bytes.
- Background SHA-256: `67de3bd14c279bcb27dd2beb0263d638511fbf447af987c3e3aa90e44e534493`.
- Prompt/provenance: `assets/nvidia-ft-report-background-2026-11-07.md`.
- HTML: `assets/layouts/nvidia-ft-report-2026-11-07.html`.
- Renderer: `scripts/render_nvidia_ft_report_2026_11_07.py`.
- Audit: `briefs/nvidia-ft-report-2026-11-07-layout.json`.

Actual Lato Black 900 is used for labels and 58px headlines, with Georgia 400 for both 38px body sections and 33px source lines. Georgia remains runtime-only and is not distributed in the repository. All authored text and panels fit x104–961, y164–1536. No background-production credit is shown.

Eighteen authored text elements and three panels passed actual browser font, minimum-size, content-boundary and overlap checks. The two main panels have equal 302px heights, with the same body and label sizes. Original coin hash and complete upper-75% placement were verified. No numerical chart is required for this story.

```sh
/tmp/moneyberg-render-venv/bin/python scripts/render_nvidia_ft_report_2026_11_07.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

Final PNG: **1080 × 1920**, **1,679,092 bytes**.
SHA-256: `354cd325dddd47048774c88a13d3ae07781a5600c8656620929aed83a2ba1a54`.

## Delivery
https://github.com/ryanschullo/create-ig-story-news/releases/download/stories-2026-11-07/nvidia-ft-report-2026-11-07.png

The release is published only after validation. Its anonymous download must return HTTP200, attachment disposition, expected dimensions and bytes identical to the local PNG before the link is shared.
