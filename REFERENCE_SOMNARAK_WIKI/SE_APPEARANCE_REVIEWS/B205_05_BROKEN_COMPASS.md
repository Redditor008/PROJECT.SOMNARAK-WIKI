# Batch 205 unit 5 — Broken Compass (`C-IIβ-290`)

**Status: HELD.** HELD +0 — 21 repairs stop requiring workers to hold, follow, strike or shatter an instrument whose whole protocol is a cradle.

## Changes made to the primary dossier

- `R01-pressure-composure` (short field correction)
- `R02-vessel-never-shatter` (short stat correction)
- `R03-beforeuse-per-piece-toll` (short text correction)
- `R04-stat-interp-distinct` (short text correction)
- `R05-escalation-four-figures` (short text correction)
- `R06-resistance-cradle-protection` (careful stat correction)
- `R07-spinning-uncertain-watcher` (careful combat correction)
- `R08-wrong-way-slowing-as-bearing` (careful combat correction)
- `R09-needle-strike-impact-only` (careful combat correction)
- `R10-full-disorientation-corrected-bearing` (careful combat correction)
- `R11-ultimate-radius-widening` (careful combat correction)
- `R12-consequences-equipment-costs` (careful text correction)
- `R13-consequences-no-holder` (careful text correction)
- `R14-use-notes-distinct` (careful equipment correction)
- `R15-field-atlimit-per-piece` (careful equipment correction)
- `R16-field-after-per-piece` (careful equipment correction)
- `R17-flavor-continued-certainty` (careful text correction)
- `R18-final-observation-fail` (careful text correction)
- `R19-notable-handler` (short text correction)
- `R20-flavor-counting-not-holding` (short text correction)
- `R21-watch-handler-first-count` (short text correction)

21 repairs (8 short / 13 careful): unified Composure, removed destructible framing, rebuilt five triggers around count/slowing/radius events, and unpooled the set's three tolls. Words 7668 → 8038; lines 470 → 470; bytes 46685 → 49000. R-18 split: 8 short / 13 careful-detail. Markdown table audit: every table block has equal parsed cell counts; Combat Action final cells and Trigger semantics were read against the Trigger header.

## Whole-design reasoning (R-33)

The A-Relic discharge is documented precisely so it can be avoided, so combat now records only cradle-observable harms: uncertainty coupling, slowings misread as bearings, prohibited impact, corrected bearings, and radius failure.

B155 held the strike/shatter states "not crosswalked"; under R-34 they cannot stand as operating rows, and the theoretical consumption account stays where the file puts it — in the profile, unperformed.

The greatsword/disc and single-use-versus-centuries conflicts were retested and remain genuinely unresolvable from the joined records.

## Commentary

A compass that measures the person counting it is the design; the old table kept trying to turn it into a weapon.

## History and independent credit

Batch 108 already credited the exact SE-290 set/pair; this R-34 recheck claims no fresh credit. HELD +0.

SE Appearance Fix credit +0; Types +0; Weapon +0.

## Holds

- Consumption/discharge theory versus undiminished centuries of observation. Held.
- Never-settled needle versus two historical settled bearings. Held.
- Greatsword versus Lost Lens; needleless charm versus rejecting needle. Held.

## Reading evidence

R-34 recheck of B155_05: complete frozen primary at 470 lines / 7,668 words, complete direct SE-290-A/B/C/D, Registry rows 579-582, B155 receipt checked as claims. All tables parsed equally; all five Trigger cells read under Trigger.

## Five actual validation outputs

- verify: `RESIDUAL 0; seam []; pipe True; dupes []`
- tpl: `RESIDUE 0`
- sectfile: 0 section(s) over 0.05 (full per-section list in the JSON receipt).
- wikistd: `meets True`
- sect: `GENERIC 0.008  (48 shared shingles)  SE-C-IIβ-290_Broken_Compass_부서진_나침반.md`

All five commands exited 0 on the final primary. Exact replay from the frozen pre-repair primary equals the final file. Technical PASS does not settle the holds above.

## Sources

- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_290_to_310/SE-290-A__SIDE_CODEX_Compass_Without_North.md` — SHA256 `597c52d0e022cc957c055d32c88a7f66ee301988931c2ae2a2853937cf92fedb`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_290_to_310/SE-290-B__MAW-W_The_Lost_Lens.md` — SHA256 `6775986b9188493762cb5183904e0ebaf5b5700edc56f6a16a67a53ffa44842e`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_290_to_310/SE-290-C__MAW-S_The_Lost_Veil.md` — SHA256 `09c4692b4993f3888eb58fbf6586685557d8a497b337985249d2bebe3364cf4e`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_290_to_310/SE-290-D__MAW-G_The_Lost_Compass.md` — SHA256 `f3db8899c57574d2e2545819e49590ba0129e8b848bbcfb88b95ac204fe48a3a`

## Continuation

Batch 205 has completed its five-shape recheck pass (5/5, No change 0/5) and closes next; no Batch 206 without fresh authorization.
