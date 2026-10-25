# Batch 182 unit 1 — Cenotaph (`N-IVδ-525`)

**Status: HELD.** Eight supported repairs align the dossier to its own span-and-register record: movement no longer claims upright pursuit, not-authorised Pugnahan leaves the valid-work row, combat runs through surface transition, solo/shared crossings and the forbidden over-span attempt instead of liquid wounds and sector flooding, breach effect and consequences use load-sharing, field-use signs split by piece, generic flavor becomes the stone-to-water warning, and the Registrum carries the actual close-the-crossing protocol. Whole design HELD; +0 Types / +0 Weapon / +0 SE.

## Changes made to the primary dossier

- `classification_movement` (short)
- `valid_work_types` (short)
- `combat_actions` (careful-detail)
- `consequences_brace` (short)
- `breach_effect` (short)
- `field_use_split` (careful-detail)
- `flavor_generic` (short)
- `registrum_procedures` (careful-detail)

Movement now follows the breach record (re-spanning, no chase, responsibility-following) instead of upright pursuit. Combat preserves all five names and every number but cannot require stepping onto the span, inflict a liquid wound, or flood every crossing in the sector; it uses the stone-to-water transition, the solo/shared register, the one forbidden over-span attempt, barricade push-through and corridor spread. The stale Registrum boilerplate ('standard containment protocols') is replaced by the file's own close-the-crossing, beneath-not-over, register and gratitude rules. Field Use separates Shrine bruising, Plate step-off delay and Ring unsaved-counting instead of one blended toll. Words 7261 → 7433; lines 433 → 433; bytes 43576 → 44609. R-18 split: 5 short / 3 careful-detail.

## Whole-design reasoning (R-33)

R-33 chain: Subject-Body / Entity-IV / Critical-δ Grudge → a guardian's roster-line promise to keep a crossing safe, broken by an Outside Sorrow surge he could not have prevented → a living bridge-body that spans corridors, holds in stone and fails into moving water, arms still sheltering the absent → the gauge is counted in crossings, solo against shared, and closes only when responsibility is spoken aloud and taken by somebody else → breach is re-spanning a busy route and giving way under solo crossers, never pursuit → equipment distributes the load to named, consenting people; none of it returns the withdrawn span to service. Repairs make movement, combat, breach and the Registrum obey that chain; the Shrine/Fang and humanoid/serpentine forks remain HELD.

## Commentary

The most humane order in the archive may be the one closing this crossing: not unsafe, still on duty. I admire that containment is a traffic register and a named routing office rather than a stronger door — the facility finally takes the load off the guardian by taking the duty onto itself, in writing.

## History and independent credit

Batch 127 unit 5 (commit 30d206d) reviewed the complete primary and exact SE-525-A–D with Registry rows 723–726, Master rows/details 541–543, Entity Codex row 549, Tale 181, both MAW-W-525 archetype rows and disposition row 168; it created a new exact SE-525-B/MAW-W-525-01 disposition and counted full-SE and Weapon. Both sit inside the ledger legacy 240/240 baseline, so B182 earns +0 Types / +0 Weapon. HELD earns +0 SE.

SE Appearance Fix credit +0 because the whole design remains HELD.

## Holds

- Weapon identity remains split at identical statistics (Grudge 3–6 / Speed 2 / Range 2 / max 5 / 15 Echoes): primary, Master table row 541 and archetype row 239 give the forty-centimetre River-Bridge Shrine whose trickling water washes away terror and whose strike carries self-blame, while Side A, item B, Master detailed Entry 541 and archetype row 303 give the Han-iron Cenotaph/Flowing Bridge Fang — a stepped stele blade whose Blame Cut removes only punishment unsupported by actual control. No transformation joins shrine and blade; no Fang function or No Guardian Alone resonance was imported.
- Body form remains forked: Physical Form and Identification describe a humanoid figure (torso a span, arms sheltering the absent) while Appearance's Primary Form and Apex Record describe a long serpentine creature gripping walls with stone pilings. Side A's 'living bridge-body' does not settle which silhouette a worker meets, and Speed 2.45 m/s remains unassigned to a body measured by span.
- Common-name fork stands: the primary is Cenotaph while Master M.A.W., Entity Codex and Tale 181 name the same designation The Flowing Bridge, with matching Flowing Bridge piece names against the primary's Cenotaph Plate/Ring. No naming rule was invented.
- Threshold scopes remain parallel and unconverted: operational threshold 1 (one failed cycle breaches), combat activation at Sorrow Gauge ≥90%, ultimate at 65%, breach gauge ±10 per solo/paired crossing in Escalation Notes against ±5 drain in the Escalation field.
- Over-span work remains unjoined: Behavior, Clash and the crossing register (406 crossings, 91 shared) put workers on the span and end breaches by sending personnel back over in pairs, while Apex Record makes going over absolutely forbidden (passage beneath only, one recorded attempt) and Story Entry 5 withdraws the Gardens span from service entirely. Which crossings the register counts, and where, is not stated.
- Structural scope remains open: the Apex survey says occupied corridors carry load through the body and that if it let go two sections would need immediate shoring and one would be unrecoverable, while disposition row 168 says it affects no other containment. No affected neighbouring containment is identified, so the dependency is neither erased nor reclassified.
- Formation lineage is narrated, not joined: the δ source yields α pieces; Side A says echoes form after rescue responsibility is distributed and an impossible promise formally released, item B forms after the shared review, and the Ring is never manufactured. No single sequence produces Shrine/Fang, Plate and Ring.

## Reading evidence

The complete original primary (434 lines), exact SE-525-A/B/C/D, Master M.A.W. table rows and detailed Entries 541–543, Entity Codex row 549, Tale 181 complete, Registry CSV rows 723–726, archetype rows 239 and 303, disposition row 168 and Batch 127 unit-5 records in both logs were read before editing. The complete final primary (433 lines) was reread after editing. This is a written-design review only; no rendered artwork was inspected or claimed.

## Five actual validation outputs

- verify: `RESIDUAL 0; seam []; pipe True; dupes []`
- tpl: `RESIDUE 0`
- sectfile: 0 sections over 0.05 (full per-section list in the JSON receipt).
- wikistd: `parity []; condition/series/disposition True; dirty_sections 0; meets True`
- sect: `GENERIC 0.006 (34 shared shingles)`

All five commands exited 0 on the final primary. Technical PASS does not settle the holds above.

## Sources

- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_525_to_559/SE-525-A__SIDE_CODEX_Cenotaph.md` — SHA256 `6e66d364219986104685d838d8c626c31087fd4d7ece0a3b4eb3c927941101be`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_525_to_559/SE-525-B__MAW-W_Cenotaph_Fang.md` — SHA256 `3b71a57cf82a653f3ca05c1e2e096e8347f3d62ae7fcf48a44c9f1f3dc995a36`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_525_to_559/SE-525-C__MAW-S_Cenotaph_Plate.md` — SHA256 `1f449f3d69bab7b4f295d1de274b96047fe6fbd55daa1c3adc74cc7df58c17ef`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_525_to_559/SE-525-D__MAW-G_Cenotaph_Ring.md` — SHA256 `b840a2a666b5637d0682c4e33e5038e4804180dc2265448f3b8d9c9ae4337270`
- `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md` — SHA256 `a0c53fbeb8e3bf2b6ea7daae84f309411ddc74f3b0b7cd620042fdecf03d0c98`
- `SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md` — SHA256 `3a1fb6fadc10ea95df9bb6b06a75ef66c344f763f71cc29862b3d6ceb6466c9d`
- `SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_TALES.md` — SHA256 `4e661a10db9631b9d6442ecf50b8fdd430e40cb96570c13bf04f139f02dda782`
- `REFERENCE_SOMNARAK_WIKI/MAW_EQUIPMENT_MASTER_REGISTRY.csv` — SHA256 `338e2d9107ace059d26567f9d31220134751f460862ca9dde6a4d2b20071fdd8`
- `REFERENCE_SOMNARAK_WIKI/MAW_WEAPON_ARCHETYPES.md` — SHA256 `4e79d0152fcbbb9df6c5b274aaacf8e346377a139850dea6da8e8ce546732399`
- `REFERENCE_SOMNARAK_WIKI/ENTITY_DISPOSITION_INDEX.md` — SHA256 `e1dd9f0e39c40fefd3c1d5b80149762820f60039c33e0aa77d331e027116dd30`

## Continuation

Batch 182 reaches 1/5 with No change 0/1, so no ladder movement. Unit 2 is the frozen Kind Healer's Shadow `N-IIβ-280`. Do not start Batch 183, merge, make artwork, or deploy without new owner authorization.
