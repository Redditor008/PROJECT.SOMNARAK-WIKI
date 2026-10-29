# Batch 205 unit 3 — Life Behind Glass (`N-Iα-518`)

**Status: HELD.** HELD +0 — 20 repairs take the hinges and floodwater off a pane that only ever harmed people by being looked at.

## Changes made to the primary dossier

- `R01-pressure-clarity` (short field correction)
- `R02-vessel-not-destructible` (short stat correction)
- `R03-secc-capitalization` (short text correction)
- `R04-wearlog-splice` (short text correction)
- `R05-escalation-first-change` (short text correction)
- `R06-resolution-condition-source` (careful field correction)
- `R07-resistance-timekeeper` (careful stat correction)
- `R08-running-pane-clarity` (careful combat correction)
- `R09-rising-damp-unresponsive` (careful combat correction)
- `R10-cold-pane-forced-retrieval` (careful combat correction)
- `R11-deluge-past-shift` (careful combat correction)
- `R12-weeping-audience-threshold` (careful combat correction)
- `R13-consequences-no-feeding` (careful text correction)
- `R14-consequences-distinct-tolls` (careful text correction)
- `R15-use-notes-distinct` (careful equipment correction)
- `R16-field-during-per-piece` (careful equipment correction)
- `R17-field-atlimit-per-piece` (careful equipment correction)
- `R18-form-record-repaired-table` (careful text correction)
- `R19-beforeuse-piece-toll` (short text correction)
- `R20-afteruse-toll-not-composure` (short text correction)

20 repairs (7 short / 13 careful): unified Clarity, removed destructible-vessel framing, rebuilt five triggers around timed gaze events, and unpooled the three watching tolls. Words 8458 → 8760; lines 467 → 467; bytes 50355 → 52048. R-18 split: 7 short / 13 careful-detail. Markdown table audit: every table block has equal parsed cell counts; Combat Action final cells and Trigger semantics were read against the Trigger header.

## Whole-design reasoning (R-33)

The I-Relic mechanism is line of sight and nothing else, so every combat row now begins from a gaze event the gallery can time: first look, speech no longer landing, forced retrieval, past-shift finding, whole-gallery audience.

B148 left the water attacks "unresolved" under a narrow scope; under R-34 they are not certifiable events, so the rows record the duration harms while the slam/flood imagery is kept only as explicitly unwitnessed legacy.

The wear-based Log and Method is still not bridged to gaze-only activation; it remains a held legacy table, which is why the file stays HELD.

## Commentary

The window works best when nothing dangerous visibly happens and the worker simply never returns to their task; the combat table finally says so.

## History and independent credit

Batch 99 already credited the exact SE-518 set review; this R-34 recheck claims no fresh credit. HELD +0.

SE Appearance Fix credit +0; Types +0; Weapon +0.

## Holds

- Wear/equip/detachment log versus gaze-only source. Held.
- Prism tesseract versus Glass Requiem window-blade and Soaking Window names. Held.
- Worker versus Keeper-erasure origins. Held.

## Reading evidence

R-34 recheck of B148_05: complete frozen primary at 467 lines / 8,458 words, complete direct SE-518-A/B/C/D, Registry rows 715-718, B148 receipt checked as claims. All tables parsed equally; all five Trigger cells read under Trigger.

## Five actual validation outputs

- verify: `RESIDUAL 0; seam []; pipe True; dupes []`
- tpl: `RESIDUE 0`
- sectfile: 0 section(s) over 0.05 (full per-section list in the JSON receipt).
- wikistd: `meets True`
- sect: `GENERIC 0.007  (42 shared shingles)  SE-N-Iα-518_Life_Behind_Glass_솟구친_창.md`

All five commands exited 0 on the final primary. Exact replay from the frozen pre-repair primary equals the final file. Technical PASS does not settle the holds above.

## Sources

- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_489_to_519/SE-518-A__SIDE_CODEX_Life_Behind_Glass.md` — SHA256 `b61e2933d768e639caf67d21251f6bd87b764020b1180f20fde4c791542d93fc`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_489_to_519/SE-518-B__MAW-W_The_Glass_Requiem.md` — SHA256 `bff3070e2b228b62395023dcd646e26d054d1152cd04355e981247fb710a2773`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_489_to_519/SE-518-C__MAW-S_The_Glass_Shroud.md` — SHA256 `9f197219670e7ec548a10efa6a4d0ed2776438a387c57218d22f8e626f90f38a`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_489_to_519/SE-518-D__MAW-G_The_Glass_Shard.md` — SHA256 `b2bb45954c8deb93266953e51bfc8aa35fa82a5aa94dca16c16139f3ee49e9e5`

## Continuation

Batch 205 continues with Seething Tundra `C-Iα-884` (O-Relic shape).
