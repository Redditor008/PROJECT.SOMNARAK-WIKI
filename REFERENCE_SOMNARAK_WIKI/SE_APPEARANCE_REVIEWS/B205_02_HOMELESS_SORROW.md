# Batch 205 unit 2 — Homeless Sorrow (`O-IIβ-119`)

**Status: HELD.** HELD +0 — 26 repairs make the wandering shadow act on departures and reallocations, never on pursuit.

## Changes made to the primary dossier

- `R01-grade` (short field correction)
- `R02-pressure-clarity-op` (short field correction)
- `R03-pressure-clarity-combat` (short field correction)
- `R04-clash-light-low` (short text correction)
- `R05-escalation-not-always-empty` (short text correction)
- `R06-containment-no-standard` (short text correction)
- `R07-observation-note-substance` (short text correction)
- `R08-trivia-contained-sense` (short text correction)
- `R09-resistance-occupancy` (careful stat correction)
- `R10-following-unacknowledged-departure` (careful combat correction)
- `R11-lengthening-rota-rule` (careful combat correction)
- `R12-cold-touch-overlap` (careful combat correction)
- `R13-swallowed-no-surge` (careful combat correction)
- `R14-shadowless-threshold-reallocation` (careful combat correction)
- `R15-tension-witness-not-no-equipment` (careful text correction)
- `R16-consequences-piece-costs` (careful text correction)
- `R17-breach-effect-belonging` (careful breach correction)
- `R18-response-sequence-keep-occupied` (careful text correction)
- `R19-veil-held-room` (careful equipment correction)
- `R20-hearth-consent` (careful equipment correction)
- `R21-use-notes-distinct-costs` (careful equipment correction)
- `R22-final-observation-fail` (careful text correction)
- `R23-unattended-usual-path` (short text correction)
- `R24-breach-banner-follows` (short text correction)
- `R25-stat-interp-earliest-cost` (short text correction)
- `R26-observation-word-home` (short text correction)

26 repairs (12 short / 14 careful): unified Clarity, rebuilt four triggers around place events, separated pooled equipment costs, and corrected the Final Observation fail path and room-clearing response. Words 6946 → 7348; lines 448 → 448; bytes 41682 → 44145. R-18 split: 12 short / 14 careful-detail. Markdown table audit: every table block has equal parsed cell counts; Combat Action final cells and Trigger semantics were read against the Trigger header.

## Whole-design reasoning (R-33)

This file is the Non-Subject-shaped recheck because its operational role is Object/Place while SECC still says Subject; the recheck preserves that dispute instead of letting either label silently win.

Every harmful row now begins from a place event — unacknowledged departure, reassignment, unwitnessed overlap, eviction by light, sector reallocation — because the shadow does not chase anybody; it has been left nowhere to stay.

The set's shared symptom (address language eroding) is separated from its three distinct costs, and the Veil is demoted from load-bearing dependency to optional witnessed support.

## Commentary

A works schedule repeatedly undoing a rostered chair remains more unsettling than a hunting shadow, and the file is at its best when it trusts that.

## History and independent credit

Batch 90 already reviewed the Weapon title/form pair and Batch 136/148 revisited without credit; this R-34 recheck claims no fresh credit. HELD +0.

SE Appearance Fix credit +0; Types +0; Weapon +0.

## Holds

- Subject versus Object/Place classification. Held — the central B148 hold, retested and still undecidable.
- Kukri versus Lens weapon identity/forms. Held.
- Per-shift versus per-hour reduction and room-assignment dates. Held.
- Veil colour and Hearth material conflicts. Held.

## Reading evidence

R-34 recheck of B148_01: complete frozen primary at 448 lines / 6,946 words, complete direct SE-119-A/B/C/D, Registry rows 358-361, and the B148 receipt treated as claims to verify. All tables parsed equally and all five Trigger cells read under Trigger.

## Five actual validation outputs

- verify: `RESIDUAL 0; seam []; pipe True; dupes []`
- tpl: `RESIDUE 0`
- sectfile: 0 section(s) over 0.05 (full per-section list in the JSON receipt).
- wikistd: `meets True`
- sect: `GENERIC 0.005  (26 shared shingles)  SE-O-IIβ-119_Homeless_Sorrow_떠도는_그림자.md`

All five commands exited 0 on the final primary. Exact replay from the frozen pre-repair primary equals the final file. Technical PASS does not settle the holds above.

## Sources

- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_119_to_127/119_Homeless_Sorrow/SE-119-A__SIDE_CODEX_Homeless_Sorrow.md` — SHA256 `26c8f244a6eece2ed47009dce50de4c7c54db6dc03090fa8068d4f1f2a556d90`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_119_to_127/119_Homeless_Sorrow/SE-119-B__MAW-W_The_Shadow_Lens.md` — SHA256 `28b7e4b4abf5fd902fffc77a7d4b360d401b43c54fb7c10b99a2a037789cf83b`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_119_to_127/119_Homeless_Sorrow/SE-119-C__MAW-S_The_Shadow_Veil.md` — SHA256 `bf9045c586026db188c43bef1d06214cc4aa65a52f80f4cb45f96485bc348596`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_119_to_127/119_Homeless_Sorrow/SE-119-D__MAW-G_The_Shadow_Hearth.md` — SHA256 `d669d6cdecacae8c0c422e0e41a72df2e827d169d302b96a282e73c2bd1a2940`

## Continuation

Batch 205 continues with Life Behind Glass `N-Iα-518` (I-Relic shape).
