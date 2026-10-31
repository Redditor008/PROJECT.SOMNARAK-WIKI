# R-34 — Full-File Logical Audit Before Any Fix

**Authority:** Direct project-owner instruction, 2026-10-29:

> “WHEN YOU DOING REVIEW THAN FIXED FIX EVERYTHING … FROM NOW ON DO A FULL FILE AUDIT AND REVIEW BEFORE FIXING SO THE FIRST THING IS DO ACTUAL REVIEW AND NOT JUST GLANCING THEN YOU FIX THE FILE AND ALWAYS PUSH NEVER NOT PUSH DO LOGICAL REVIEW NOT AI ONLY REVIEW.”

**Status:** Mandatory for every Sorrow Entity review, recheck, repair and No change decision. This rule strengthens `R-15`, `R-18` and `R-33`; it does not replace them.

## 1. The rule in one sentence

**Audit the whole current file and its identity-resolved sources first, write the findings down, and only then repair the file.**

A search result, a template scan, a section excerpt, an earlier evidence receipt, a `whole_final_reread: true` boolean, or a validator PASS is not a review. A logical review is explicit, checkable reasoning that follows what the entity is, what it can do, what state it is in, what the numbers mean, and whether every later section still agrees. Automated checks may locate evidence; they may not replace that reasoning.

## 2. Freeze the object of review

Before reading for repair:

1. Record the branch, base commit, primary path, designation and display name.
2. Freeze an untouched before-copy outside the repair step.
3. Record its SHA-256, line count, byte count and `LC_ALL=C wc -w` word count.
4. Resolve identity from the exact Side Codex designation, linked-entity field and item codes. Never resolve identity from a number, title fragment or folder name alone.
5. Read the ledger entry and all earlier evidence for the same dossier. An earlier receipt is a claim to be checked, not a substitute for checking.

## 3. Read the complete evidence set

Read, in document order and in full:

- the complete current primary dossier;
- exact Side Codex and Weapon, Suit and Stigma records;
- any parent, predecessor, transformation counterpart or other primary record that the entity's causal chain depends on;
- the exact Master Registry, Entity Codex, Tale, archetype or combat-engine passages that govern a disputed claim;
- the primary's in-file full-set or per-piece review paragraphs and the prior appearance evidence.

Search may locate those passages. Search output is not reading evidence.

## 4. Produce the audit before the first primary edit

The pre-repair audit must give each material finding an ID and must cover every section, including sections the reviewer expects to leave untouched.

At minimum, audit:

1. **Identity and state:** designation, entity type, manifestation, coherence, potency, element, location, comprehension level, contained/uncontained state, current/historical/projected state.
2. **Causal chain:** origin → sorrow → event → people → formation or transformation → present state → Tale → testimony → record.
3. **Appearance:** silhouette, anatomy or non-body organisation, materials, scale, colours, conditional forms, movement, spatial extent, observer conditions and identification method.
4. **Operational Parameters:** every row and every Operational Note, including thresholds, yield, work difficulty, destructibility, drops and recommended response.
5. **Combat Record:** every core stat and operational-record row. State whether each value is observed, historical, projected, simulated or unsupported.
6. **Every Combat Action separately:** name, category, flavour claim, move, target scope, effect, numerical track, duration, trigger and sequence position. Compare each one against form, movement, element, Behavior, Work permissions, breach/activation behaviour, Tale and exact sources. Two rows with the same numbers must still have different logical functions, or the duplication is a finding. **Trigger semantics:** a Trigger must name a discrete, checkable condition that invokes that action — target/entity behaviour, contact or exposure, gauge or threshold, count, time, or a named world event. “After the previous action,” “next stage,” “culmination” and other sequence positions are not triggers by themselves. Escalating rows may share a mechanism, but each must be distinguishable by condition, scope or function; a mandatory order belongs in Battle Phases only when the exact sources establish it. Corpus-wide Combat Actions patterns may identify a format anomaly, but they do not override exact-source mechanics. The Dawn of Mourning trigger-semantics correction of 2026-10-29 is the standing example: all five triggers had been rewritten as positions in one compulsory sequence, so the first three collapsed into the same exposure state and the Ultimate had no checkable condition.
7. **Battle Phases and Consequences:** whether an encounter can occur at all, whether the phase order is possible, and whether the resolution can happen at the point claimed.
8. **Behavior and Work:** every Work Type row, gauge direction, special behaviour, operational work note and reading rule.
9. **Breach, activation or expansion:** every row, movement claim, first target, escalation figure, containment priority and gauge figure.
10. **M.A.W. Equipment:** overview, provenance, and every field of Weapon, Suit and Stigma against the exact item records; then Use Notes, Field Use Record, stat interpretation and any in-file source review.
11. **Observation and Story logs:** dates, counts, witnesses, sequence, method and whether a claimed observation is current, historical or projected.
12. **Final Observation and Flavor:** choices, contact states, activation states and departure states.
13. **Interactions:** every paired entity, the evidence actually held, and whether one file is being used to corroborate itself.
14. **Tale, Testimony and Registrum:** chronology, status, comprehension, handling, factions, originator and review requirements.
15. **Entity-specific chronicles and records:** doctrine, testimony and literary narration must not be silently promoted into observation evidence.
16. **Trivia and Document Information:** “only”, “every”, “never” and other universal claims; dates, authors and classification labels.
17. **All repeated numbers:** build a number ledger for gauges, percentages, thresholds, counts, dates, ranges, probabilities, costs and durations. A number repeated in two sections must mean the same thing in both.
18. **Markdown table integrity:** for every table block, count cells from **unescaped** pipes and confirm that the header, separator and every row have the same number of cells. Then map the parsed cells back to the header—especially the final column—so a pipe inside an effect, duration or range cannot silently push a Trigger or other last field into an orphan sixth cell. A row that merely starts and ends with `|` is not thereby a valid table row.

## 5. Classify every finding honestly

Use these classes:

- **Supported — retain:** the primary and exact sources support the claim.
- **Contradiction:** two claims cannot both be true in the same state and time frame.
- **Unsupported or template residue:** the claim has no provenance in the file or exact sources, or survives only because a form required a value.
- **Mechanical inconsistency:** the prose, trigger, target, track, duration or arithmetic do not implement the stated effect.
- **Ambiguous / source fork:** exact sources preserve incompatible accounts, forms, names, chronology or functions.

Mark each finding **essential** when it changes what the entity is, whether it exists now, how it forms, how it moves, what work is permitted, what its equipment is, or whether the file's resolution can work. Essential ambiguity remains **HELD**.

## 6. Credit is decided from history, not from effort

Before any edit, prove whether the exact equipment set has already had a full-set or per-piece source review. Search the primary, exact sources, ledger and evidence history. A missing ledger entry does not erase an in-file review. A dated review banner is not the only possible proof when the primary already integrates item-level dispositions.

No fresh Types, Weapon or SE Appearance credit may be inferred from a recheck.

## 7. Repair only after the audit and R-18 split

Only after the findings are written:

1. Declare the `R-18` batch-short / careful-detail split.
2. Map every repair to one or more audit finding IDs.
3. Repair every source-supported defect in the unit, not only the defect that prompted the review.
4. Do not bridge an essential fork by inventing anatomy, chronology, transformation, permission, equipment lineage or a numerical mechanism.
5. Do not edit cited sources to make the primary look consistent.
6. If no source-supported repair is required after the full audit, report exactly **No change**. Do not manufacture an edit.

“Fix everything” means every finding receives a disposition: repaired, retained as supported, or held with the missing evidence named. It does not mean pretending an unresolved fork has been fixed.

## 8. Re-audit the final file

After repairs:

1. Re-read the complete final primary in document order.
2. Repeat the section audit and the per-action Combat Action audit on the final text, including a separate Trigger-semantics read: every parsed Trigger cell must state the condition that invokes its own row, not merely the row's place after another action.
3. Rebuild the number ledger and confirm that no repair created a new contradiction.
4. Parse every Markdown table block in the final primary. Header, separator and every row must have the same unescaped-pipe cell count, and the reviewer must read the parsed final cell of representative rows against its header (for Combat Actions, the Trigger). The Dawn of Mourning syntax correction of 2026-10-29 is the standing example: four rows passed the ordinary validators while an internal duration pipe created six cells in a five-column table and displaced the Trigger.
5. Confirm that every planned repair happened exactly once and that replay from the frozen before-file reproduces the final file.
6. Run `verify`, `tpl`, `sectfile`, `wikistd` and `sect`. These are technical checks only; they cannot settle narrative or mechanical logic.
7. Write evidence that contains the audit reasoning, repairs, retained claims, holds, credit decision, reading record and final outcome. A boolean is not reasoning.

If the primary changes after the final re-reading, the final audit is void for every affected dependency and must be repeated.

## 9. Correcting an earlier incomplete review

When a recheck shows that an earlier review missed material defects:

- preserve the earlier evidence as history;
- create a dated recheck supplement rather than rewriting the old receipt;
- state plainly which sections or actions the earlier review failed to audit;
- do not repeat equipment or appearance credit;
- do not describe the recheck as proof that all earlier dossiers received an R-34 audit.

After the current pending pass is finished, previously reviewed dossiers remain candidates for a later R-34 full recheck. That later pass must start from the current files and exact sources, not from old summaries.

## 10. Push discipline

Push the audit/rule record and each repaired unit through `tools/gate.sh`. Verify that local `HEAD` equals the remote session-branch commit. **Always push. Never not push.** A local audit, local repair or local commit is not shipped work.

## 11. Report discipline

Report under `R-31`. The chatroom report must say, in readable substance:

- what the full audit found;
- what was actually changed;
- what remains held and why;
- the reviewer's **Commentary**;
- the checks and verified push state.

Do not report only repair counts, validator names or a claim that the whole file was reread.
