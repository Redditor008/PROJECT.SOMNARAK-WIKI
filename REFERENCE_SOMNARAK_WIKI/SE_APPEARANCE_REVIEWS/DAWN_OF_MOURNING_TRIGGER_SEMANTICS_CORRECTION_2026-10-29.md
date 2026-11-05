# Dawn of Mourning — Combat Action Trigger Semantics Correction

**Date:** 2026-10-29  
**Designation:** `C-Vω-001`  
**Base commit:** `8294d2dd5df0d6536dd9dbe224f6c51d45c4620b`  
**Before SHA-256:** `966feea825c302710ad17ebf5487a859379e93674f28003817b5e69a591c6e5b`  
**Final SHA-256:** `b135dd618293a48708582b404cfbad3d325e4d66a0270dc29c0d331e9125a715`  
**Outcome:** **HELD +0.** Seven careful repairs; 9,241 → 9,267 words. This supplement preserves the earlier R-34 and table-syntax records.

## What the owner found

The owner was correct. Dawn's Trigger column was no longer doing the job the Trigger column does in the other Sorrow Entity records.

The previous R-34 repair correctly removed the burning beam, physical seepage and unsupported reversed-transformation counterattack. It then overcorrected the whole table into five compulsory stages of one judgment. The resulting cells said, in effect:

- first exposure;
- after the first action;
- still exposed after the second;
- after sentence begins;
- culmination.

Those are positions in a sequence. They are not five distinguishable trigger conditions.

## Comparative research

The audit parsed every Combat Actions table in the 301-dossier ledger corpus:

- **301/301** dossiers carry a Combat Actions table.
- **1,471** action rows were parsed.
- **1,223** Trigger cells begin with “When.”
- The Battle System's own examples name conditions such as the entity being agitated or damaged, identifying a threat, being hungry or exhausted, falling below 50% health, or being overwhelmed.
- **256/301** dossiers use `Debuff / Debuff / Attack / Attack / Ultimate`. Dawn had become one of only two `Debuff / Debuff / Debuff / Debuff / Ultimate` tables; the other is Sorrow Seed's deliberately non-attack measurement set.
- **272/299** Ultimate triggers contain an explicit percentage. Most exceptions still name a concrete world event.
- Dawn was the only dossier whose five triggers all function as sequence positions. *No Partial Light* even used the previous action's title — “After *The Four Sorrows*” — as its condition.

Related chain records make the contrast clearer. The Kind Healer triggers on accepting healing, being healed again, rejection, being cornered or a gauge threshold. Blessing Giver and Apostle Maker trigger on approach, nearby marked people, interruption, blessing counts and the twelfth conversion. Their rows can be invoked by identifiable circumstances; Dawn's repaired rows could only be read in table order.

## Row-by-row correction

| Action | New Trigger | Why this condition is distinct |
|---|---|---|
| *The Four Sorrows* | When a target first enters the Dawn's sight or attempts to observe it. | Appearance says it judges all who enter its sight; the Behavior row says observation exposes hidden guilt in the observer. |
| *No Partial Light* | When an exposed target tries to look away, take cover, resume a routine, or compartmentalise what has been revealed. | This gives the duplicated opening-cycle values a separate function: failed attempts to restore partial sight. It follows Ferrehan's pinning response and the file's compartment/routine failure. |
| *The Mourning Light* | When aggression or confrontation is directed at the Dawn (projected Pugnahan response). | SE-044-A says aggression is sentenced immediately. Restoring the `Attack` category does not restore a beam or physical counter-blow. |
| *The Mourners* | When a previously unexposed target encounters one of the twelve Mourners. | Origin says the twelve become Mourners if the chain turns; the repeatable action is relay to a new target, not their one-time role transition. |
| *The Mourning of All Things* | When the historical/projected Sorrow Gauge reaches ≥95%. | Uses the Core Stat Line's existing model threshold and aligns the Ultimate with the corpus's normal threshold/event grammar. |

The section introduction and Battle Phases no longer require a fixed order. A row is resolved when its own condition occurs; rows may overlap, and a row may recur if its condition recurs.

`Attack` was restored on rows 3–4 because the Entity Codex treats category as a Combat Record pressure class. The prose still says the Dawn sentences through revelation. No beam, thermal damage, hunting, seeping, reversed transformation or invented segment values were restored.

## Disposition of the earlier R-34 findings

This supplement partially reverses the implementation choices in prior findings F-05 through F-09, not their source findings:

- the four-sorrow opening remains ordered and non-random;
- *No Partial Light* remains the distinct partial-sight function;
- *The Mourning Light* remains cold sentence, not a burning beam;
- *The Mourners* remains the supported spread mechanism, not a reversed transformation;
- *The Mourning of All Things* remains functional unmaking with no invented values.

What changed is the mistaken inference that those mechanisms had to be arranged as one compulsory sequence with sequence-position triggers.

## Rule correction

`R-34` now requires a separate Trigger-semantics audit:

- a Trigger must state a discrete, checkable invoking condition;
- “after the previous action,” “next stage” and “culmination” are not triggers by themselves;
- escalating rows must differ by condition, scope or function;
- mandatory order must be source-established, not inferred from row order;
- corpus patterns may reveal a format anomaly but cannot override exact-source mechanics.

## Validation

- Complete final primary reread in document order.
- Exact replay from the frozen before-file equals the final file.
- Every Markdown table block has equal parsed cell counts.
- All five parsed Trigger cells were read under the Trigger header.
- `verify.py` — PASS.
- `tpl.py` — PASS (`RESIDUE 0`).
- `sectfile.py` — PASS.
- `wikistd.py` — PASS (`meets True`).
- `sect.py` — `GENERIC 0.002 (12 shared shingles)`.

## Commentary

The table now behaves like a Combat Record again without pretending Dawn throws punches. Looking at it, hiding from it, attacking it, meeting a Mourner and reaching the model ceiling are five different ways to lose. That is both mechanically clearer and truer to an entity whose horror is that several ordinary responses make the sentence worse.

Dawn remains **HELD** for the temporal, equipment, chronology, pressure-semantics and Chronicle forks in the earlier R-34 recheck. No credit changes.
