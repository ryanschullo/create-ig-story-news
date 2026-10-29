# Warsh reshapes the Fed’s meeting calendar

**Category:** FEDERAL RESERVE WATCH

**Story edition:** October 28, 2026, America/Chicago

**Export:** `exports/fed-meeting-playbook-2026-10-28.png`

## Requested source and verification

The user selected The Kobeissi Letter’s post:
https://x.com/KobeissiLetter/status/2115518969012789494

The complete public X HTML was read. Its publication metadata is
2026-10-28T19:00:01Z (2:00 p.m. CDT). The post is a six-point summary of
Chairman Kevin Warsh’s statement, addressing future meeting agendas, financial
conditions, elevated inflation, and waiting for more information. There is no
attached source chart or photograph. The platform’s syndication response only
includes a shortened text preview; the full public page supplied the complete
post. Responses and comments are not evidence for the graphic.

The meeting changes and macroeconomic context were verified against the
Federal Reserve’s full, four-page preliminary opening-statement transcript:
https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20261028.pdf

Pages 1–2 state that inflation remains elevated and that additional information
will help determine the appropriate policy stance. Page 3 states that eight
meetings a year remain the right number, with the agenda change beginning next
fall. In 2027, one meeting will be dedicated exclusively to strategy, with
neither a federal funds rate vote nor a policy statement anticipated. The
remaining seven will be regular policy-setting meetings. Warsh expects two
strategy meetings and six policy-setting meetings in 2028.

Reuters independently corroborates the agenda change:
https://www.reuters.com/markets/us/feds-warsh-announces-changes-how-future-fomc-meetings-will-go-2026-10-28/

Full body read; Michael S. Derby; October 28, 2026, 20:44 UTC publication.
Reuters also notes that the Fed retains the ability to change monetary policy
outside scheduled FOMC meetings. The graphic does not imply otherwise.

## Editorial scope

This complements the separately requested rate-hold graphic by focusing on
Warsh’s meeting-agenda changes. It does not say the total number of meetings
falls to six. The central line explicitly reads **Still 8 meetings a year.**
2027 is labeled planned; 2028 is labeled expected. The note retains the
conditional word **anticipated** for strategy-session rate votes/statements.

The equal-size tile diagram is an authored summary of sourced annual counts,
not an original source chart. Seven teal plus one brass tile represent 2027;
six teal plus two brass represent 2028. Tile positions do not identify months,
specific dates, an exact meeting sequence, or the probability of rate changes.
No rate path, December decision, numerical forecast, or investment return is
inferred. The exact “monetary medicine” quotation is not necessary to this
focused visual and is not reproduced.

## Design and permanent assets

- Ivory plaster, dark teal, walnut, and restrained brass create an institutional
  boardroom treatment distinct from the dark rate-hold graphic.
- Generated background is decorative, not a documentary photograph of an
  actual Fed boardroom. Initial text-free source:
  `/workspace/generated_images/exec-7ff4adf4-8dc0-47b0-9d00-7dfe88371520.png`.
- Readability edit moved furniture down and kept the mounting recess:
  `/workspace/generated_images/exec-fc47ac10-772b-48d6-bd3e-2a360d1dbccf.png`.
  The latter is archived as
  `assets/fed-meeting-playbook-background-2026-10-28.png`.
- Only the unchanged original `assets/moneyberg-coin-original.png` is used,
  uniformly scaled into the physical brass-lined walnut pilaster recess with
  contact shading. No generated portrait or lettering. Master SHA-256:
  `4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716`.
- Actual Lato Black 900 and Georgia are rendered in Chromium. Georgia is loaded
  from an external runtime font file and is not redistributed.
- Compact one-line MONEYBERG NEWS BRIEF, 32 px. Headline 72 px. Body notes
  32–34 px. All authored text is at least 30 px, including the sources.
- No background-production footer appears on the graphic.

## Validation and reproduction

Run:

```bash
python scripts/render_fed_meeting_playbook_2026_10_28.py \
  --georgia-font /tmp/moneyberg-georgia-font/extracted/Georgia.TTF
```

The renderer checks the original coin hash, actual font families and weights,
browser-loaded fonts for every text element, the 30 px floor, news bounds,
absence of overflow, image dimensions, coin circular proportions, lack of
coin/text overlap, and whole-coin placement above y=1440. Audit:
`briefs/fed-meeting-playbook-2026-10-28-layout.json`.

Final export inspected visually at full size. An earlier composition placed
sources over chairs; the final composition uses a two-line headline and
reflows all text upward without reducing any font sizes. The source lines now
sit on clear ivory plaster above the furniture. All news content is inside
x=104–961 and y=164–1536; actual text bounds are x=114–659, y=184–1372.
Diagram and separator bounds also pass the inset. Original coin bounds are
x=892–1010, y=793–911, 118 × 118 px, entirely in the upper three-quarters.

Export is **1080 × 1920 PNG**, **1,962,115 bytes**. SHA-256:
`2d608a06148fd4102c218665da9e5a679dafad45c872a625161e237b7e2d1ef9`.

Publication and GitHub raw-byte verification are handled by the coordinating
agent after the final review.
