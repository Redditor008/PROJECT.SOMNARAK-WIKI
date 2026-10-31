# Batch 204 unit 1 — Unrung (`C-IIβ-170`)

**Status: HELD.** HELD +0 — 16 repairs make the outside clock, not the bell, the authority in the room.

## Changes made to the primary dossier

- `R01-pressure-composure-op` (short field correction)
- `R02-vessel-no` (short field correction)
- `R03-Han-dust-none` (short field correction)
- `R04-op-note-trigger-distinction` (careful operational correction)
- `R05-resistance-clocked-not-heard` (careful stat correction)
- `R06-resolution-answered-warning` (careful field correction)
- `R07-held-breath-waiting-for-ring` (careful combat correction)
- `R08-swallowed-sound-hand-signals` (careful combat correction)
- `R09-silent-toll-forced-contact` (careful combat correction)
- `R10-absent-peal-no-gauge-surge` (careful combat correction)
- `R11-eternal-silence-threshold-60` (careful combat correction)
- `R12-battle-phase-resolution` (careful phase correction)
- `R13-cassock-ability-outside-thread` (careful equipment correction)
- `R14-tool-log-delay-not-speed` (careful tool correction)
- `R15-use-mode-fixed-site` (careful tool correction)
- `R16-contact-no-resistance-buff` (careful tool correction)

16 repairs (3 short / 13 careful): aligned Composure, removed vessel destruction, separated activation from the 60% threshold, rebuilt five triggers around waiting-for-a-ring, speech in the field, forced contact, thirty-second delay and threshold silence, and made the answered warning the resolution. Words 9250 → 9587; lines 493 → 493; bytes 55337 → 57368. R-18 split: 3 short / 13 careful-detail. Markdown table audit: every table block has equal parsed cell counts; Combat Action final cells and Trigger semantics were read against the Trigger header.

## Whole-design reasoning (R-33)

Unrung does not attack from a body: harm follows protocol breaks inside a delay nobody inside it can measure, so the outside clock and hand signals are the encounter.

The gauge and the arrival delay answer separate questions; a session can only close when the account is separate and any surfaced warning is in a named hand.

Every equipment piece requires a listener outside the silence, which is why partner-held channels and recall authority now govern the combat layer.

## Commentary

Its monster is a correctly followed procedure, which is harder to forgive than a villain.

## History and independent credit

Batch 78 already dispositioned the exact Muffled Resonance-Bell Weapon and Batch 127/unit 2 shipped a full-SE source-led Unrung review, so no fresh Types, Weapon or SE credit is claimed. HELD +0.

SE Appearance Fix credit +0; Types +0; Weapon +0.

## Holds

- Cassock form: midnight velvet/lead-mesh versus pale gossamer. Held.
- Brooch form: bronze lead-clapper pin versus pale clapperless bell. Held.
- Countersignature-free acceptance versus custodian-controlled access. Held.
- Tale failed-alarm account versus Origin correctly-filed warning; Side A leaves it open. Held.
- Han Pressure 7–16 versus Side Void 8–20. Held.

## Reading evidence

R-34 source chain: complete frozen primary at 493 lines / 9,250 words, complete direct SE-170-A/B/C/D and Registry rows 438–441. CHANGELOG shows Batch 78 corrected the exact Weapon and Batch 127/unit 2 completed a full-SE review. All tables parsed equally and all five Trigger cells read under Trigger.

## Five actual validation outputs

- verify: `RESIDUAL 0; seam []; pipe True; dupes []`
- tpl: `RESIDUE 0`
- sectfile: 0 section(s) over 0.05 (full per-section list in the JSON receipt).
- wikistd: `meets True`
- sect: `GENERIC 0.006  (40 shared shingles)  SE-C-IIβ-170_Unrung_침묵의_종.md`

All five commands exited 0 on the final primary. Exact replay from the frozen pre-repair primary equals the final file. Technical PASS does not settle the holds above.

## Sources

- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_170_to_184/170_Unrung/SE-170-A__SIDE_CODEX_Unrung.md` — SHA256 `15c248ccc5ed1524731640d6f6ad18797cc78f76d963502bb9899f199aff5cc7`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_170_to_184/170_Unrung/SE-170-B__MAW-W_The_Silence_Hammer.md` — SHA256 `a83d53a96364a999d88922dbda2f11140c823ce7b42b3e058e14fecb38a150e0`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_170_to_184/170_Unrung/SE-170-C__MAW-S_The_Silence_Veil.md` — SHA256 `00f1d7601166b62e8a04aadfc2d181eea78750b68a39f63b4623f1401d7cbfe6`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_170_to_184/170_Unrung/SE-170-D__MAW-G_The_Silence_Charm.md` — SHA256 `9d66f021dd9f132508e0da67f494c7d4d4db1de3e662004f1bc91ab04bbf042e`

## Continuation

Batch 204 continues with Deadline `N-IIIβ-156` under the same R-34 audit.
