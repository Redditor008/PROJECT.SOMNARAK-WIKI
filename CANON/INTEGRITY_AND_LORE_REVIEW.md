V5 RESULTS

V5-1 (Dawn of Mourning HP): FIXED. It is 12,000 in both the dossier and the side codex, and the CHANGELOG is corrected.

V5-2 (chronology): FIXED. The loop end and Hand of Hope are Year 4,238 everywhere, including the Absolvohan README and Part 9. UCD is Year 4,039 and the Katabagil descent is Year 3,970. Lint guards were added.

V5-3 (old "292" counts): FIXED for the TEMPLATES, the SOMNARAK-WORLD README, Pages/README.md, Pages/42 and the Unknown_Entities README. A few leftovers are in V7-4.

V5-4 (README counts and audit): FIXED. The README now says 49 codices and 16 volumes, and the audit expects 52.

V5-5, V5-6, V5-7 and V5-8: FIXED.

The ID letter is now defined as City, Outside and Inner.
The catalog has no Project Moon risk names left.
The rules doc says Rank IV runs 390–1,000.
The rules doc says "At or below 15" for the Transform line.
V5-9, V5-10 and V5-11: FIXED. The retired-rank lint, the path lint (now covering docs/ and DEVELOPMENT.md) and the chronology lint all work.

V5-12 (boilerplate "39% → 2%"): the figure was not real. The author retracted it in the CHANGELOG and reverted the label decoration. The real boilerplate was not reduced (see V7-5).

V5-13 (Absolvohan story share): FIXED. Story is about 12–15%. There are 38 bespoke interludes of about 500 words each, with 0% sentence reuse.

V5-14 (length ladder): FIXED. The medians are Rank I 4,730, II 5,019, III 5,166, IV 5,471 and V 6,967. The 13 Rank V chronicles are bespoke.

V5-15 (Ordeals): FIXED. All 60 have distinct leads, and no old template line is left. The median is about 1,416 words.

V5-16 (merge and main): not a defect. The branch uses its own separate main, and a merge only happens if the other AI breaks down.

V6 RESULTS

V6-1 (label damage and code tags): FIXED. The audit passes with 0 scope mismatches. A 20-file sample shows the labels are identical to before the V5-12 change, and no bare [SE-code] tags remain.

V6-2 (boilerplate): PARTLY FIXED. The CHANGELOG now honestly retracts the false figure. By my measure about 37% of prose lines are still shared by 30 or more dossiers, against the author's 13.4% (see V7-5).

V6-3 (recycled stories): FIXED, and well done.

Apex Record (80 files), Warden Record (82) and Watch Record (70) show 0% sentence reuse, and almost every ### title is distinct.
I read a Warden Record sample. It was specific to its entity and the writing was good.
V6-4 (stale counts): PARTLY FIXED. The root README, Pages/README.md, the Main Page, Pages/42 and the TEMPLATES are corrected. The leftovers are in V7-3 and V7-4.

V6-5 (Ordeal template line): FIXED.

V6-6 (label lint): PARTLY FIXED. tools/label_lint.py exists with 7 tests and the real repo passes it. It isn't run as a CI step (see V7-2).

V6-7 (merge and main): not a defect, as above.

V7 - FIX LIST

V7-1. The metrics-parity step in CI fails.

tools/label_lint.py and its fixtures added 3 files, and the metrics weren't regenerated. CANONICAL_METRICS.json, CANONICAL_METRICS.md and the README say 2,217 files. The repo has 2,220.
Fix: run python3 tools/generate_canonical_metrics_registry.py and python3 tools/sync_readme_metrics.py. Then commit CANONICAL_METRICS.json, CANONICAL_METRICS.md and README.md.
V7-2. Add the label linter to CI.

.github/workflows/ci.yml has no step for tools/label_lint.py. Only its fixture tests run, so the real repo isn't checked. The commit message calls it a "seventh gate", but it isn't one yet.
Fix: add a step that runs python3 tools/label_lint.py.
V7-3. The catalog header is stale.

REFERENCE_SOMNARAK_WIKI/SORROW_ENTITIES_CATALOG.md now has 291 rows. Lines 4, 11 and 13 still say "284 Unique" and "284 rows ... pending indexation".
SOMNARAK-WORLD/Pages/01-Main Page.md, line 5, says "284 cataloged SECC".
Fix: change these to 291 and delete the "pending indexation" sentence.
V7-4. Leftover old counts.

README_STORY_REFERENCE_GUIDE.md, lines 18 and 56, say "292". Change them to 291.
SOMNARAK-WORLD/Pages/07-Sorrow Entities.md, line 234, says "all 285 SECC codes".
Optional, historical: REFERENCE_SOMNARAK_WIKI/REGISTRY_MASTER_STATUS.md, line 330.
V7-5. Boilerplate (low priority).

Agree one measure, because the author's figure is 13.4% and mine is about 37%. A small tool could report both.
Most shared lines are procedural scaffolding. The worst offenders are:
the "must be assessed as part of an entity network" interaction intro, in 240 files
the Trivia "Recognition detail" and "Record detail" bullets, in 244 files
the Story Log header "Progressive declassified records...", in 282 files
Operational Parameters, which is about 97% shared, Combat Record about 70% and M.A.W. Equipment about 45%
Fix: move the shared doctrine into one reference page and link to it.
V7-6. Rank V is just under the 7,000-word mark.

The median is 6,967, and only 3 of the 13 Rank V dossiers reach 7,000. The count dropped slightly when the label decorations were removed.
Fix: either top up about 10 files by roughly 100 words each, or restate the target as "about 7,000".
Everything else from V1–V6 is verified fixed.
