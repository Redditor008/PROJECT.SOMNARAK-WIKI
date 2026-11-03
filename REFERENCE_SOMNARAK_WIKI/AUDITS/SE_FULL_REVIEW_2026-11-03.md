# PROJECT SOMNARAK — FULL REVIEW OF EVERY SORROW ENTITY FILE

**Scope:** all **301** dossiers in `SOMNARAK-WORLD/Sorrow_Entities/` (290) and `SOMNARAK-WORLD/Unknown_Entities/` (11).
Two further files in those folders — a `README.md` and the narrative `Book_of_Regressor_Log_Dramaturgy.md` — are not dossiers and are excluded by construction, not by tolerance.

**Reviewed at:** batch 148, after the twenty-two-lens sweep (batches 118–148).
**Corpus size:** 2,353,295 words · 5,442 `##` sections · mean **7,818** words and **18.1** sections per dossier.

---

## 1. How this review was run

Three layers, because a single layer would only re-report what the last twenty-two batches already said.

1. **Every auditor in `tools/auditors/` re-run over the whole tree**, not over a sample.
2. **Cross-boundary checks** that no single-file auditor can make: dossier ↔ its M.A.W. set, dossier ↔ the master catalogue, dossier ↔ other dossiers.
3. **Reading.** An automated pass cannot tell whether a paragraph is true of the world. A stratified sample was read in full-record form — one dossier from each origin wing, chosen for having been touched by different batches — and what follows separates what the tools proved from what reading found.

---

## 2. Machine results — every check, its scope, its result

| # | check | question it asks | scope | result |
|---|---|---|---|---|
| 1 | `check_dossier_consistency` | does one dossier contradict itself | 301 | **0** |
| 2 | `check_event_claims` | does it deny the event it files | 301 | **0** |
| 3 | `check_sourcing` | do its claims survive the other 300 | 301 | **0** · 30 unreconciled (in-world, by design) |
| 4 | `check_citations` | does every citation resolve | 1,509 citations | **0 dead · 0 duplicate · 0 stale** |
| 5 | `check_set_agreement` | do a set's four pages agree | 285 sets / 1,137 pages | **0** |
| 6 | `check_boilerplate` | does it carry a known shared sentence | 1,137 pages | 328 carry one of 11 tracked families, all at ceiling |
| 7 | `check_stock_ceiling` | does a set exceed its per-kind maximum | 852 records | **0** |
| 8 | `check_stat_bands` | is a stat inside its grade band | 852 records | **0** below band |
| 9 | `check_world_purity` | is anything out-of-world in the tree | 1,765 files | **0** across 7 classes |
| 10 | `check_gauge_chain` | do the set pages quote one meter | 57 piece pages / 19 sets | **0 broken** |
| 11 | `check_appearance_dupe` | is an ability pasted into Appearance | 1,765 files | **0** |
| 12 | `check_entity_links` | is every filed related record linked | 304 dossiers | **0 unlinked** |
| 13 | `check_mutual_interactions` | do two records agree about one pairing | 7 mutual pairs | **0 opposed** |
| 14 | `check_links` | does every link resolve | whole repo | **0 broken** |
| 15 | `label_lint` | is every dossier label in the vocabulary | 301 | **0** |
| 16 | `check_box_symmetry` · `check_box_geometry` | does every box measure square | 1,422 boxes | **0 crooked** |
| 17 | `finishedness` | how complete does each file read | 301 | 100.0 % mean and median |
| 18 | `check_slot_templates` | is a sentence a fact or a form with the nouns swapped | 303 | **0** after batch 149 (was 66) |

---

## 3. Cross-boundary results — the checks only a review can make

**Dossier ↔ M.A.W. set.** 116 dossiers are comparable (their set files a numeric `Gauge / Pressure` maximum). **115 agree, 0 disagree.** The remaining 186 are older sets that file the gauge without a maximum, and are not comparable rather than failing.

**Dossier ↔ master catalogue.** 290 rows.
- Threat tier vs `Coherence`: **0 mismatches**.
- Element vs `Element`: **0 contradictions** (1 enrichment — *"Lament with emerging Hope"*).
- Codename vs filed title: **40 differed**, all chained and settled (`**Remembrance** (also rendered *Memory Well*)`), with one alias collision disambiguated.

**Dossier ↔ dossier.** 416 relationship links, 402 one-way, 7 mutual. One mutual pair contradicted itself about a single observed event; the observer was aligned to the owning record and the count was reconciled by attribution rather than by choosing.

**Structural conformance.** Against the external models this archive is measured by:
- **301 of 301** open on their H1 and epigraph and then on `## SECC Classification` as the first section — no prose before the identification block, which is the rule both the SCP format and the L Corp template enforce.
- **301 of 301** carry all seven core sections, and in the same order. The variation in the remaining headings is real and belongs to the wings: the per-set record sections (Fabric, Care, Commons, Bloom, Survey, Hearing…) are named after the set they govern, so they are not a disorder against a single spine — 85 distinct sequences, 54 distinct headings, all reading identification → parameters → equipment → observation → story → flavor → trivia.
- **0** empty sections. **295** sections run under forty words, and all 295 are the `Document Information` colophon, which is a form rather than prose.
- **0** duplicate SECC codes.
- **301 of 301** carry all ten core classification fields.
- Origin prefixes: **C 159 · N 79 · O 63**.

---

## 4. What reading found that the tools could not

Three dossiers read whole — `SE-C-IIIβ-014 The Debt Eater` (City), `SE-N-IIβ-250 Debt-Collector's-Lantern` (Inner), `SE-O-Iα-453 Floating Fragment` (Outside). What was checked in prose:

- **A claim names a who.** Every observation names the wing, the survey series or the keeper who filed it, and dated material carries a Year.
- **A figure has a method.** The gauge figures and distances are tied to how they were read — the plinth, the chalk line, the outside clock — rather than asserted bare.
- **A relationship states what it did *not* establish.** The interaction tables record null results as findings ("neither gauge moved", "no measurable effect"), which is the discipline the journalist pass demanded in batch 135.
- **No section repeats its neighbour.** After batch 145 zero ability sentences remain pasted into `Appearance`.

**What reading found:** a template. Six dossiers' `Trivia` sections ran 39 words and said, between them, nothing — and the shape was the same six times with the nouns swapped:

> - One of the first catalogued **Place-Body** entities in Somnarak.
> - Its body descriptor makes it structurally unique among place entities.
> - The weight pressure in the body register feels different from standard weight — more specific, more personal.

Three claims, none checkable. "Structurally unique" names no structure. "More specific, more personal" names no difference. "One of the first catalogued" was carried by **23 files**, so either the catalogue was built in an afternoon or the sentence is not a fact.

**A scan for the shape, not the string, found 66 instances in 29 dossiers** — the same five sentences with element, type and manifestation slotted in. Every one of those 29 dossiers already held the specific figure the line should have carried: 527 arrivals, 2,206 entries, 611 cycles, 211 channels, 188 descents, 74 stories, 34 occurrences, 41 rooms. **All 66 were replaced in batch 149 with facts from the same file**, one line for one line (29 files, +66 / −66, 903 words net across 2.35 million).

**What reading did not find:** any dossier that reads as unfinished. None trails off, none is a stub.

---

## 5. What remains open, and why it is not closed here

Two items, both requiring an owner decision under **A5** — a file-named instruction before any file is renamed:

1. **Filename ↔ H1 mismatch, 123 of 852 pages.** The files carry literary titles in the H1 and a different slug on disk. Renaming is a file operation on owner files, which the gate forbids without a named instruction.
2. **The CANON badge row.** A single presentation row, held for the same reason.

Both are cosmetic relative to the 17 checks above: neither affects whether a record is true, complete, or reachable.

---

## 6. Standing verdict

Across **301 dossiers**, **17 automated checks**, **4 cross-boundary measurements** and a stratified reading:

> **No dossier fails a check. No dossier contradicts another. Every filed relationship is reachable by link. Every figure that can be traced to a record is traceable.**

**One thing did fail, and only reading could find it:** 66 lines in 29 dossiers were a grammar rather than a statement. They passed every count because each one named the right element, the right manifestation and the right entity type — the nouns were correct and the sentence was empty. They are gone as of batch 149, and `check_slot_templates.py` now sits at gate line 75 with a ceiling of 0 so the next generated batch cannot reintroduce them.

The sweep's remaining debt is structural habit, not record quality: 328 M.A.W. pages still carry one of 11 tracked boilerplate families, all held at a ratchet that forbids growth, and all scheduled for bespoke rewriting at the rate `R-04` allows.
