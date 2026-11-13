# R-57 — The Extended File Is Built From the Dossier

**Stated by the archive owner, 2026-10-25:**

> *"NO I MEAN WHAT YOU WROTE IN THE BACKSTORY AS THE EXTENDED VERSION OF HIS DOSSIER ONE LIKE WHEN
> READ IT DOESNT MAKE SENSE AND WHEN LOOK IT NOT AT ALL MAKE LOGICAL SENSE YOU SHOULD HAVE READ THE
> DOSSIER FIRST THAN MAKE THE BACKSTORY EXTENDED VERSION AND IF YOU ALREADY FORGET WE USED L CORP
> STYLE OF WHAT IT LOOK IT LOOK LIKE AND THE GUIDE STYLE HOW ITS READ"*

## 1. What was wrong

`Backstory_Extended/01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md` ran **14,700 words** and never once
showed the man.

The fusion is the most visual event in his life. The Extended wrote it as:

> *"he remembers heat, and the smell of the lamp, and the ceiling"*

His dossier `THE_DIRECTOR.md` § Appearance devotes a full section to what that night did to him: black
veins coming up the inside of the left upper arm, across the elbow, down to a scythe-shaped mark
between wrist and forearm; three hooked scars on the upper left of his face that darken under Reaper
Hungered; deep blue eyes; silver reached the temples; a sleeve cut open so the mark can be checked.

The Extended used **two of twenty-three** of those descriptors, and both of them were in a HOLD
table saying they were *not* being used.

That is the failure the owner named. Not the length — the *order of work*. The file had been written
as a story that happened to be about a man, rather than as the dossier's man given a life. Batch 216
had answered the same complaint against § Backstory in the dossier, which was the wrong file; the
complaint was always about the Extended.

**L Corp style** is what he named for the *look*: in Lobotomy Corporation a Sephirah's history is
inseparable from the body you are shown — the plating, the visor, the damage. **The guide style**
(`SOURCE_Unified_Narrative_Writing_Rules_for_AI.md` § 1) is what he named for the *reading*: show the
thing, not the feeling; facts over adjectives; humans are not narrators.

## 2. The rule

**An Extended file is built from its dossier, not beside it.**

Five things follow:

**A. Read the dossier first.** The dossier is tier 1 authority. Every physical fact in the Extended
must be traceable to the dossier's own words. If the Extended needs a fact the dossier does not have,
the dossier is amended — the two must not disagree.

**B. § Appearance is a writing brief, not a note.** A dossier's Appearance section lists what a reader
must be able to *see*. Every item on it is an obligation on the Extended, not a decoration. The test
is not whether the words occur — it is whether the reader finishes the file knowing what he looks
like.

**C. The appendix is not the story.** The old file named *three hooked scars* and *scythe mark* in its
own HOLD table while never showing either in a scene. A table that says *"not dramatized"* is an
admission, not a use. Appearance is measured over the narrative body only.

**D. The dossier's own contradictions are settled once, by class.** The dossier said his loss was
*"the event that, at the founding, grew the Alpha Tree"* — Year 234–245 — while he is 126 in the final
Cycle. Resolution: **two Solidifications, one class.** The founding freezing (234–245) grew the Tree;
his was a second freezing of the same substance some four thousand years later. The year of his loss
stays unstated. It is not averaged, and it is not invented.

**E. Arithmetic on the page.** Where two figures in the file disagree — a projected thirty-six tons
against an actual 49.88 — the Extended states the relationship and the cause. It does not quietly
change the number.

## 3. What this does not license

Showing the man does not license stopping to describe him. The guide's § 1.4 (trust the reader) still
governs: a scar is shown once, in the scene where it means something, and then it is part of the room.
A file that recites the Appearance section back at the reader has failed differently, not better.

## 4. The gate

`tools/auditors/check_backstory_appearance.py` (gate 53). For each Extended file it finds the matching
dossier, takes the physical descriptors from that dossier's `## Appearance`, and counts how many the
Extended file uses **in its narrative body**. Floor 50 %. A file below the floor must be recorded in
the gate's `DEBT` table, so the remainder is always printed rather than pretended away.

Measured 2026-10-25:

| file | before | after |
|---|---|---|
| `01_MAJIN` | 8 of 22 (36 %) | **19 of 22 (86 %)** |
| `02_SEIYON` | — | 4 of 14 (29 %) *debt* |
| `03_DEKAN` | — | 10 of 24 (42 %) *debt* |
| `04_ZYRAK` | — | 13 of 28 (46 %) *debt* |
| `05_AYSHUK` | — | 9 of 27 (33 %) *debt* |
| `06_MELLDA` | — | 17 of 29 (59 %) |
| `07_MARJUK` | — | 6 of 24 (25 %) *debt* |
| `08_ISHALL` | — | 10 of 23 (43 %) *debt* |
| `09_XYAN` | — | 8 of 25 (32 %) *debt* |

The gate cannot tell whether a word is used to show the character or merely named in passing. That is
the reader's pass (`O-29`, `R-38`). A gate passing is not a reading.
