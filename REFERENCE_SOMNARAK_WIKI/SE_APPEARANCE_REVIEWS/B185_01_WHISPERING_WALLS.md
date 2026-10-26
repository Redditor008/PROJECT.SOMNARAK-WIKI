# Batch 185 unit 1 — Whispering Walls (`C-Iα-011`)

**Status: HELD.** HELD with exactly one mechanical repair. Batch 115 unit 3 already performed the full-SE review of this dossier and deliberately wrote its three distinct equipment costs into the Use Notes and field record; reading the exact SE-011-A–D sets now confirmed those assignments rather than overturning them (Shroud 'minor joys feel distant' ↔ primary's loss of small pleasures; Stone +1-on-the-source and background whispers ↔ item D and Master Entry 318; slot Tail and resistances match). The one demonstrable defect found in the whole final read is a duplicated clause-stutter in the Fabric Record ('...and it holds that a containment function It holds that a containment function the facility costed...'), removed without touching any digit. The chalice/blade identity, weapon costs, range strata and nine unusable utterances stay HELD exactly as Batches 88/115 left them. +0 Types / +0 Weapon / +0 SE.

## Changes made to the primary dossier

- `officer_clause_stutter` (short)

One sentence repaired, nothing else moved: the ward officer's objection in the Fabric Record no longer repeats its own opening clause. Every statistic, cost, name and hold in the file stands as Batches 88 and 115 recorded it. Words 7401 → 7395; lines 463 → 463; bytes 45526 → 45489. R-18 split: 1 short / 0 careful-detail.

## Whole-design reasoning (R-33)

R-33 chain: Object/Place I-Relic / Residue-I / Minor-α / City Sorrow → three generations of survival whispering because volume drew the Han → the plaster, being the only listener always in the room, keeps the speech and replays it in the dark over some 1,100 metres of connected wall → work is Viderehan/Ferrehan at a painted boundary: walk it, log the overlap and the dwellings, acknowledge aloud, never scrape the plaster → no breach counter; failure is reach — the field crossing into a wall with somebody living behind it → equipment turns that listening outward (Truth Note, Clear Channel, Hear the Seam) at per-piece human cost. Nothing in that chain supports rewriting B115's recorded cost assignments; the only break is the duplicated clause, which the one repair closes.

## Commentary

The district talks to its walls because it always has; the facility put it in the tenancy agreement. Between the nuisance with no defendant, the truth about a fire that no procedure can receive, and a containment duty transferred entire to unpaid residents, this is the register's quietest indictment of itself — and the sentence making it now at least stutters only once.

## History and independent credit

Batch 88 unit 2 (d7a0967c) dispositioned the exact Weapon pair SE-011-B (39/287) and aligned Side A to The Occlusion Star-Chalice, explicitly holding Master Entry 316's Listening Requiem / blade terminology. Batch 115 unit 3 (2026-10-14) then performed the full-SE review: it rewrote the Use Notes / stat guide to distinguish the three costs, tracked the Stone's seven-day follow-up without inventing a stop threshold, and kept the chalice and Instant-vs-Range-2 holds; the B115 close counts this as one of its 3 full-SE dispositions, with the Weapon pair 'counted earlier'. Both sit inside the independent run's legacy baseline, so Batch 185 earns +0 Types / +0 Weapon; HELD earns +0 SE.

SE Appearance Fix credit +0 because the whole design remains HELD.

## Holds

- Weapon identity stays forked exactly as Batch 88 held it: primary/Registry/archetype The Occlusion Star-Chalice — a carved obsidian chalice hovering over the palm, pulling projectiles into liquid shadow and discharging gravity (Revision 3abe5470 replaced the item's former blade Appearance with this body) — against item B's Type 'short singing blade', its 'blade hums/emits' Truth Note prose, the SE-011-B filename, and Master table row 316 / Entry 316 The Listening Requiem, Resonant Blade. No source records a transition between blade and chalice; Archetype MAW-W-011 gives Range Instant against primary/item Range 2 / Short, also held.
- The weapon's human cost forks: primary unaccounted grief wept without knowing whose it is, reversing on return (Batch 115's recorded assignment), against item B's Wielder Cost — after a Truth Note the bearer hears one of their own unspoken sentences in the nearest quiet surface. Batch 115 wrote the primary line knowing the item; this run does not reverse a recorded review decision on re-read.
- Suit mechanics fork: primary 'works by making the wearer less able to hear' and 'deadens hearing where it crosses the ears', against item C's Clear Channel — it isolates one voice and the rest return as a delayed chorus after removal. The costs agree (minor joys distant / small pleasures lost) but the mechanism and its limit do not; retained as held.
- The Stone's permanence forks softly: primary bears an unquieten-able background even as it records the sentence-told-or-recorded ending from item D, and Master Entry 318 sides with the permanent background that cannot be fully silenced. Both endings stay in the record; and the nine utterances contradicting the official history remain sounds in a wall — preserved, unusable, unreconciled.

## Reading evidence

The complete original primary (464 lines), exact SE-011-A/B/C/D, Master rows/Entries 316–318, Entity Codex row 471, Tale 106, Registry CSV rows 30–33, archetype MAW-W-011 (row 63), disposition row 299 and the Batch 88/115 changelog and WIP records were read before editing. An initial drafted repair set built from prior-session memory was rejected in full after the set files contradicted it; only the verified stutter was applied. The five checks passed and the final file was compared byte-for-byte against the recorded repair. The complete final primary (463 lines) was reread after editing. This is a written-design review only; no rendered artwork was inspected or claimed.

## Five actual validation outputs

- verify: `RESIDUAL 0; seam []; pipe True; dupes []`
- tpl: `RESIDUE 0`
- sectfile: 0 sections over 0.05 (full per-section list in the JSON receipt).
- wikistd: `parity []; condition/series/disposition True; dirty_sections 0; meets True`
- sect: `GENERIC 0.007 (35 shared shingles)`

All five commands exited 0 on the final primary. Technical PASS does not settle the holds above.

## Sources

- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/011_Whispering_Walls/SE-011-A__SIDE_CODEX_The_Whispering_Walls.md` — SHA256 `a4d26f8dacc366087c1ed50fc4c00709f08bdd4bdc208fb3637e7be5b0e5dda6`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/011_Whispering_Walls/SE-011-B__MAW-W_The_Listening_Requiem.md` — SHA256 `75d12d51fb74d1db2281fb9484cc283b768ae9f79907542dcb73a07ea6aabb9b`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/011_Whispering_Walls/SE-011-C__MAW-S_The_Listening_Shroud.md` — SHA256 `b9d22b05574139663118e2a7872d2a2b772f1561e653cc880d17b0b5c5f907a1`
- `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/011_Whispering_Walls/SE-011-D__MAW-G_The_Listening_Stone.md` — SHA256 `cbe1dec0b2915226079db3c1b2b59d7e3d546bc3c1bbb07a9cb98a4a226da79e`
- `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md` — SHA256 `a0c53fbeb8e3bf2b6ea7daae84f309411ddc74f3b0b7cd620042fdecf03d0c98`
- `SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md` — SHA256 `3a1fb6fadc10ea95df9bb6b06a75ef66c344f763f71cc29862b3d6ceb6466c9d`
- `SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_TALES.md` — SHA256 `4e661a10db9631b9d6442ecf50b8fdd430e40cb96570c13bf04f139f02dda782`
- `REFERENCE_SOMNARAK_WIKI/MAW_EQUIPMENT_MASTER_REGISTRY.csv` — SHA256 `338e2d9107ace059d26567f9d31220134751f460862ca9dde6a4d2b20071fdd8`
- `REFERENCE_SOMNARAK_WIKI/MAW_WEAPON_ARCHETYPES.md` — SHA256 `4e79d0152fcbbb9df6c5b274aaacf8e346377a139850dea6da8e8ce546732399`
- `REFERENCE_SOMNARAK_WIKI/ENTITY_DISPOSITION_INDEX.md` — SHA256 `e1dd9f0e39c40fefd3c1d5b80149762820f60039c33e0aa77d331e027116dd30`

## Continuation

Batch 185 continues under the same five-floor/ten-ceiling prompt: Candela next, then Mourner's Bloom, Breach, Hollow Echo. No merge or deployment; draft PR #15 stays open.
