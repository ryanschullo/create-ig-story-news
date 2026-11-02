# The week's biggest market events — November 2–6, 2026

User request: create a graphic from [The Kobeissi Letter's weekly events post](https://x.com/KobeissiLetter/status/2116885664780231025), including “only the big ones.” The complete substantive public post was read directly on X. This is an editorial selection of major events, not the entire calendar or a ranking by market capitalization.

## Selected content

- **Monday, November 2:** Apple and Palantir earnings.
- **Tuesday, November 3:** U.S. midterm elections and AMD earnings.
- **Friday, November 6:** October jobs report at **8:30 a.m. ET**, followed by preliminary November University of Michigan consumer sentiment at **10 a.m. ET**.

These are scheduled events, not reported results. The design uses the full week date range; omitted days do not imply that no other events are scheduled. To honor the user's request for only major highlights, omit SMCI, ISM releases, JOLTS, ADP, the approximate S&P earnings share and the aggregate Fed-speaker count. Michigan inflation expectations are part of the sentiment release, rather than an additional event row.

## Primary verification

All source pages below were read through ordinary public HTTP. Public feeds explicitly used by company pages were consulted for their displayed calendar content. No access controls were bypassed.

1. **Apple:** [Investor earnings-call page](https://www.apple.com/investor/earnings-call/) links its [public current-event JSON](https://events-delivery.apple.com/15pijbsdfvpiqhb10/js_files/event/url.json). The event states Q4 2026, November 2, 2026, 2 p.m. PT / 5 p.m. ET. This verifies the earnings-call date; the graphic does not mislabel the call time as the release time.
2. **Palantir:** [Investor events page](https://investors.palantir.com/events) lists Q3 2026 earnings on November 2. Its October 12 announcement, read in the site's ordinary [public IR feed](https://investors.palantir.com/feed/PressRelease.svc/GetPressReleaseList?languageId=1&bodyType=1&year=2026&includeTags=true&pressReleaseDateFilter=1), specifies release after U.S. market close and a 5 p.m. ET webcast. The direct historical article path redirects to a 404; the accessible company feed and current event page are the evidence.
3. **AMD:** [October 6 company announcement](https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results) confirms Tuesday, November 3, after market close, with a 5 p.m. ET call.
4. **Midterms:** [Federal Election Commission election information](https://www.fec.gov/introduction-campaign-finance/election-and-voting-information/) states Tuesday, November 3, 2026 as the next regularly scheduled federal general election. No nationwide closing time or result timing is asserted.
5. **Jobs:** [BLS November 2026 release calendar](https://www.bls.gov/schedule/2026/11_sched.htm) lists Employment Situation, October 2026, on Friday November 6 at 8:30 a.m. All times on the calendar are Eastern. October is the data month, not the publication month.
6. **Sentiment:** [University of Michigan Surveys of Consumers](https://www.sca.isr.umich.edu/) states: “Next data release: Friday, November 6, 2026 for Preliminary November data at 10am ET.” No current October values are passed off as future November results.

## Design and verification

- Export: `exports/key-events-week-2026-11-02.png`, confirmed **1080 × 1920**.
- Category: **STOCK MARKET**; small single-line **MONEYBERG NEWS BRIEF** brand.
- Distinct midnight-navy weekly calendar with ice-blue dates and restrained gold election emphasis; decorative Capitol/exchange architecture below. Scene is an illustration, not evidence of actual events.
- Three large day rows: Monday 02, Tuesday 03 and Friday 06. Newly authored type is at least 33 px; headline 80 px, event names 48–52 px, body 35–39 px. Actual Lato Black 900 and Georgia 400 are verified through font metadata and browser font inspection.
- All authored content and panels stay in the required inner bounds x=104–961, y=164–1536. A dark source backing preserves contrast over the architectural scene.
- The verified original `assets/moneyberg-coin-original.png` is uniformly scaled into the generated brass rail's mounting recess with contact shadow and compatible lighting. Full original face, rim and lettering are retained. The complete coin is at x=916–1062, y=441–587, within the upper 75% of the canvas; original master unchanged.
- Text-free background was created with the image generation tool; exact prompt and provenance in `assets/key-events-week-background-2026-11-02.md`.
- HTML/CSS and browser rendering place the real font files and original coin. Python orchestrates the browser and verifies output; no image-pixel editing library is used.
- Georgia is runtime-only, retrieved from the freely distributed Microsoft Core Fonts package (`https://downloads.sourceforge.net/corefonts/georgi32.exe`), family Georgia, weight 400, SHA-256 `7d0bb20c632bb59e81a0885f573bd2173f71f73204de9058feb68ce032227072`. No Georgia font bytes are committed.
- Automated validation checks text sizes, actual fonts, content bounds, image dimensions, coin aspect/position and master hash. Independent visual review confirmed readable sources, full content, correct calendar and integrated original coin.

## Reproduction and delivery

```sh
python scripts/render_key_events_week_2026_11_02.py \
  --georgia-font /path/to/Georgia.TTF
```

The layout audit is `briefs/key-events-week-2026-11-02-layout.json`. Publish the committed PNG through `.github/workflows/publish-graphic-download.yml`, with edition `2026-11-02` and filename `key-events-week-2026-11-02.png`.

Direct-download target:
https://github.com/ryanschullo/create-ig-story-news/releases/download/stories-2026-11-02/key-events-week-2026-11-02.png

Verify anonymous HTTP 200, attachment disposition, exact bytes and 1080 × 1920 PNG dimensions before delivery. The edition date denotes the start of the covered week.
