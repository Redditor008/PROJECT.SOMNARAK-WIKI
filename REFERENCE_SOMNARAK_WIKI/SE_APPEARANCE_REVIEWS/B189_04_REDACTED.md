# Batch 189 unit 4 — Redacted (`N-IIIγ-184`)

**Status: HELD.** Three source-supported repairs (2 short / 1 careful): both boilerplate movement lines stop claiming the figure 'can breach and pursue' — its two recorded escapes ended at records stores and it has never pursued a worker — and the Registrum Originator no longer supplies 'a citizen erased from records and memory', the one identification the whole file exists to refuse; the field now carries the file's own finding that no originating person can be established. First independent full-set source review of SE-184: fresh +1 Types / +1 Weapon; whole design remains HELD, SE +0.

## Changes made to the primary dossier

- `R1-secc-movement` (short movement correction)
- `R2-appearance-movement` (short movement correction)
- `R3-originator-unestablished` (careful originator correction)

The file no longer fills its own blank: the Originator field records that no originating person can be established, and the figure is no longer said to pursue anyone. Words 7663 → 7745; lines 434 → 434; bytes 45436 → 45910. R-18 split: 2 short / 1 careful-detail.

## Whole-design reasoning (R-33)

Set SE-184 identity resolved from Side A (SECC Designation N-IIIγ-184 [N], set 'Absent History') and item codes MAW-W/S/G-184-01; all four set files read whole. Sentence triage found three unsupported claims: (1) SECC Movement and (2) Detailed Appearance Position/movement both carried the class line 'Mobile — walks upright; can breach and pursue', contradicted by the breach table ('First Target: No personnel. It goes to paper'), the Escalation Notes ('It has never pursued a worker') and Trivia ('Neither involved a worker'); (3) Registrum Originator supplied 'A citizen erased from records and memory', contradicting Origin ('The People: Unknown… a result rather than a gap in research'), Trivia ('No originating person can be established') and Side A's open questions. R-18 split declared before the apply: 2 short (both movement lines) / 1 careful (Originator). Technical PASS on the frozen file (GENERIC 0.005) did not settle any of the three — R-33. No identity, chronology or equipment lineage invented; the repairs remove assertions and replace them with the file's documented record.

## Commentary

Redacted is a dossier about a blank that must not be filled, so the most serious defect in it was a single administrative line that filled one: the Registrum calmly named an Originator — a citizen erased from records and memory — in a file whose Origin, Trivia, breach notes and Set Relationship pages all say, carefully and repeatedly, that whether the destroyed material concerned a person at all cannot be established from any surviving document. The careful repair makes the field say that. The two short repairs take 'can breach and pursue' off a figure that has walked out exactly twice, to paper, and never after a person. Everything else — the tape series, the Withheld Index, the nine restored and the one killed — already stood in its own order and was left alone.

## History and independent credit

Fresh-credit proof by negatives: no in-file cross-source/full-set review block in the primary; no prior evidence file under SE_APPEARANCE_REVIEWS mentions N-IIIγ-184; ledger equipment_reviews has no 184 entry; git path history shows only the B179 import commit 87f1a01. This unit is the first independent exact-pair/full-set source review: Side A (182 lines) and items B/C/D read whole, including their Appearance sections; primary Suit/Stigma machine fields (Head/4%/+2, resistances, costs) agree with item and Side stat cards; Registry rows 454–457 confirm identity (Weapon Variable/-/-; Stigma generic Accessory/5%). Fresh credit: Types +1, Weapon +1, SE +0 (whole design HELD). Counters become 276/301, 274/287, 18/301.

SE Appearance Fix credit +0 because the whole design remains HELD.

## Holds

- Weapon name fork: primary and Registry 'The Arboretum Lance' vs item SE-184-B identity table and Side A 'Redacted Lens' (the item's own title line says Lance; its combat file operates a Lens) — both names stand; nothing renamed.
- Suit appearance fork: primary veil 'so light it reads as a change in the light' with a tape-mark hem vs item 'full-length suit of pale, half-transparent cloth' with the identity-card collar — the primary already carries the collar rule in its Ability; the descriptions are not merged.
- Stigma Head / 4% / +2 (primary, item and Side stat card agree) vs Registry's generic Accessory / 5% — Registry value never imported.
- Girth↔unattributable-destruction-count correspondence remains the file's own three-year hand reconstruction; the archivist's refusal of a projection stands, as does the Withheld Index's unresolved ledger (nine restored, one killed, four informants before them).
- Side A's breach 'Field effect: Void roots entangle personnel' vs the primary's two escapes with no worker pursued — the primary's incident record governs the primary; Side A left untouched.

## Reading evidence

Complete frozen primary read (435 lines, 7,663 words) including Warden Record and the Withheld Index; Side SE-184-A read whole (182 lines); items SE-184-B/C/D read whole (75/73/72 lines) including Appearance sections and Histories of Use; Registry rows 454–457 inspected; negative searches run across all prior evidence files, equipment_reviews and git path history before fresh credit was claimed. The complete final primary (434 lines) was reread after editing. This is a written-design review only; no rendered artwork was inspected or claimed.

## Five actual validation outputs

- verify: `RESIDUAL 0; seam []; pipe True; dupes []`
- tpl: `RESIDUE 0`
- sectfile: 0 sections over 0.05 (full per-section list in the JSON receipt).
- wikistd: `parity []; condition/series/disposition True; dirty_sections 0; meets True`
- sect: `GENERIC 0.005 (28 shared shingles)`

All five commands exited 0 on the final primary. Technical PASS does not settle the holds above.

## Sources

- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_170_to_184/184_Redacted/SE-184-A__SIDE_CODEX_Redacted.md` — SHA256 `7764660b2b8152d20ee002f4018f1c6fd3a8dd1c8c2d96da084774709ac59f42`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_170_to_184/184_Redacted/SE-184-B__MAW-W_Redacted_Lens.md` — SHA256 `adb35076b933f43d9e3ff3931d1c29d080974ab8f2d29cd8997978a550605a3b`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_170_to_184/184_Redacted/SE-184-C__MAW-S_Redacted_Veil.md` — SHA256 `a252736fa2d8225db92f400b7d58b2ffd68935e0ecda5c1cb964e9d71d7547fa`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_170_to_184/184_Redacted/SE-184-D__MAW-G_Redacted_Ring.md` — SHA256 `cccee2e807028e290e8821ae662a62e1c72db1fa6e544b0e5bb1f350cc72df28`
- `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md` — SHA256 `a0c53fbeb8e3bf2b6ea7daae84f309411ddc74f3b0b7cd620042fdecf03d0c98`
- `SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md` — SHA256 `3a1fb6fadc10ea95df9bb6b06a75ef66c344f763f71cc29862b3d6ceb6466c9d`
- `SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_TALES.md` — SHA256 `4e661a10db9631b9d6442ecf50b8fdd430e40cb96570c13bf04f139f02dda782`
- `REFERENCE_SOMNARAK_WIKI/MAW_EQUIPMENT_MASTER_REGISTRY.csv` — SHA256 `338e2d9107ace059d26567f9d31220134751f460862ca9dde6a4d2b20071fdd8`
- `REFERENCE_SOMNARAK_WIKI/MAW_WEAPON_ARCHETYPES.md` — SHA256 `4e79d0152fcbbb9df6c5b274aaacf8e346377a139850dea6da8e8ce546732399`
- `REFERENCE_SOMNARAK_WIKI/ENTITY_DISPOSITION_INDEX.md` — SHA256 `e1dd9f0e39c40fefd3c1d5b80149762820f60039c33e0aa77d331e027116dd30`

## Continuation

Batch 189 Unit 5 `N-IIβ-627` follows in this prompt (review 6 of 10), then Batch 189 closure. Draft PR #15 remains open; nothing merged, drawn or deployed.
