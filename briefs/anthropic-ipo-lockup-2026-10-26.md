# Anthropic's planned early IPO releases

Story date: October 26, 2026 (America/Chicago).
Export: `exports/anthropic-ipo-lockup-2026-10-26.png`.
Category: **AI INVESTING**.

## Selected angle and sources

The user selected Bloomberg's article and then supplied the specific angle:
Anthropic plans an unusual IPO lockup with early release milestones on Day 1,
Day 27 and Day 48, allowing some investors and employees to sell before the
typical 180-day period ends. This graphic focuses on those early milestones,
rather than repeating the previous valuation-and-revenue graphic.

- User-selected Bloomberg article, October 26, 2026:
  https://www.bloomberg.com/news/articles/2026-10-26/anthropic-s-ipo-sets-up-defining-moment-for-wall-street-and-ai-boom
  Direct access returned HTTP 403. Bloomberg's full article was not independently
  read; its angle was supplied by the user. The detailed schedule was checked
  against the primary filing below.
- Anthropic, PBC, Form S-1 filed October 26, 2026:
  https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
  The `Shares Eligible for Future Sale` table and the lockup provisions in
  `Underwriting` confirm the first trading day and the 27th- and 48th-day
  milestones, including differing eligibility and partial-release limits.

The previously retrieved primary filing was read for this graphic. Its local
archive is `/tmp/anthropic-ipo-2026-10-26-s1.html` (14,169,264 bytes), SHA-256:
`b6836006abac03a7ab0244b79b968d9bcecde9f49ada9b79be78546d427f541e`.
Relevant excerpts are in
`/tmp/bloomberg-anthropic-ipo-2026-10-26/lockup-primary-excerpts.txt`.

## Timing and eligibility

| Displayed milestone | Primary-filing meaning |
| --- | --- |
| **Day 1** | First trading day following the prospectus date. Certain non-founder directors, officers, current or former employees and consultants may transfer up to 10% of their applicable holdings. |
| **Day 27** | Partial release 27 calendar days after the prospectus date for eligible stockholders; permitted amounts differ by holder group. |
| **Day 48** | Further partial release 48 calendar days after the prospectus date for eligible stockholders; permitted amounts differ by holder group. |

If a specified release date is not a trading day, the filing moves availability
to the next trading day. These are planned terms in a preliminary filing, not
fixed calendar dates, completed sales or days counted from the October 26 filing
date. The finished graphic explains the prospectus-date basis and describes
partial releases for eligible holders, subject to conditions.

The general 180-day comparison is a typical IPO convention, not a universal
legal requirement or the precise restriction on every Anthropic holder. Some
holders have extended 365-day arrangements. The filing also specifies later
milestones beyond Day 48; the three displayed milestones are the user's chosen
early releases, not the complete release schedule. No all-share unlock, price
effect, future selling volume or investment recommendation is inferred.

## Asset and rendering requirements

Use the official Anthropic SVG and the unchanged original Moneyberg coin.
Authored headings and labels use actual Lato Black 900; body and source text use
actual Georgia. Georgia is supplied locally at runtime and not redistributed.
The story is 1080 × 1920, with all news content inside x104–961, y164–1536.
The coin is integrated into the background environment with its entire rim
above y1440. No background-production footer appears on the graphic.

Renderer: `scripts/render_anthropic_ipo_lockup_story.py`.
Template: `assets/layouts/anthropic-ipo-lockup-2026-10-26.html`.
Layout and font audit: `briefs/anthropic-ipo-lockup-2026-10-26-layout.json`.

## Finished design and verification

The generated ivory-and-terracotta environment uses opening doorways as a
visual metaphor for staged access. It is decorative scenery, not an identified
Anthropic property or evidence of an IPO event. The new background was copied
unchanged from
`/workspace/generated_images/exec-c4b69c13-60ee-4ee4-9a48-b4510aa182a7.png`
to `assets/anthropic-ipo-lockup-background.png`. The full image-generation prompt
and asset hashes are preserved in the renderer and layout audit.

The original coin is rendered directly at **x874–1044, y1050–1220**, uniformly
scaled to 170 × 170 px. A bronze seat, inset contact shadow and warm surface
lighting integrate it into the front-facing stone door pier. Its portrait,
lettering and proportions are preserved; the master is unchanged. The entire
coin lies within the upper three-quarters and clears all news content.

The official Anthropic SVG retains its original path geometry and aspect ratio.
Chromium font inspection verifies actual **Lato-Black** and **Georgia** for all
24 authored text elements. The body text accompanying each release milestone
is 32 px; source attribution is 24 px. All text, five panels/rules and the logo
fit the required inner news bounds. The exported PNG is **1080 × 1920**.

Visual review confirmed the three requested days, the 180-day comparison,
planned/partial eligibility, calendar-versus-trading-day timing, readable
attribution and original coin integration. The three rows are an ordered list,
not a time axis or a representation of release quantities. No daily stock-index
results are required for this IPO-specific story.

Final PNG SHA-256:
`e3d7d85c6300551fc6d9c84364bc774be3e65b414c870bf5c59e84299a2dd965`.

```sh
python scripts/render_anthropic_ipo_lockup_story.py --georgia-font /path/to/Georgia.TTF
```
