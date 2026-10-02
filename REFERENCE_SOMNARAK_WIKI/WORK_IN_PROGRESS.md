# Work In Progress

> *"Written down because several days of work does not survive in anybody's head."*

This file is the running state of the project. It is updated at the end of every working turn and is the authority on what has been done, what is open, and what comes next. Where it disagrees with recollection, this file is right.

## Measured state

All figures below are measured by `tools/boilerplate_report.py`, not estimated.

| Measure | Value |
|---|---|
| Dossier body lines | 28092 |
| Lines shared by 30+ dossiers | 6302 |
| **Headline** | **22.43%** |
| Dossiers still at 30+ shared lines | 83 |
| Dossiers fully cleaned | 47 |
| Unfinished-text breaks outstanding | 105 |

## Workstream 1 — De-boilerplate (open)

Whole-file rewriting of the worst-affected dossiers, one file per turn, bespoke per entity. Rules `R-02`, `R-04`, `R-05`, `R-14`, `R-15` all bind here.

**Progress: 47 / 130.** Headline trajectory 34.3% → 22.43%.

### Next targets, in order

| Shared lines | Dossier |
|---|---|
| 38 | `SE-N-IVδ-489_Forgotten_Silence_잊혀진_침묵.md` |
| 37 | `SE-O-IVδ-693_Spreading_Root_스며든_뿌리.md` |
| 37 | `SE-N-IVδ-909_Dormant_Monolith_잠든_기둥.md` |
| 36 | `SE-O-IIIδ-011_Scar_Walker_흉터의_행자.md` |
| 36 | `SE-C-Iα-869_Homecoming_Tree_돌아온_나무.md` |
| 35 | `SE-N-IVδ-525_Cenotaph_흐르는_다리.md` |
| 35 | `SE-N-IIβ-560_Dismissed_Cry_솟구친_절규.md` |
| 34 | `SE-N-Iα-519_Mourning_a_Life_I_Never_Lived_스며든_씨앗.md` |

Re-rank after every clean. Files drop into the top band as global counts shift; the queue is never carried over from a previous turn without re-measuring.

### Residual floor

Every cleaned file keeps 9–13 lines of genuine cross-reference furniture (`**Cross-References:**`, `- See Origin section…`, `**Threat Assessment:**`). These are not chased. The structural floor is 3.1%.

### Completed cleans

Fallow 50→12, Shard 49→9, Ephemera 48→12, Border Tree 48→11, Tear 48→11, Glass 48→12, Portcullis 47→11, Thralldom 47→12, Aphasia 47→12, Forgotten Tear 47→12, Anonym 47→12, Welcome Haven 47→11, Survivors' Breath 47→10, Quagmire 47→10, Yggdrasil Wound 46→13, Repose 46→11, Grasp 46→10, Uprooted 46→11, Sleeping Tree 46→10, Frozen Mirror 45→11, Heirloom 45→9, Spire 45→10, Memory Chain 45→10, Feu Follet 45→10, Broken Whisper 45→9, Ember Phoenix 44→10, Broken Fragment 44→9, Brume 44→11, Myrmidon 44→9, Broken Ruin 44→11, Errant 43→11, Atlas 43→11, Animus 43→10, Conservatory 43→9, Home to No One 43→9, Broken Door 42→10, Tower Erased Overnight 42→9, Relic Waiting for Its Maker 42→9, Exiles' Wall 41→10, Protest No One Remembers 41→10, Pent 41→9, The Silent Child 39→11, Broken Tear 39→10, Relic of a Thousand Owners 38→9, The Wrath Flame 38→10, Soaking Rope 38→11, Sleeping Shard 38→9.

## Workstream 2 — Unfinished text (reopened)

**312 end-of-line breaks completed; that scan returns zero.** Then a second kind surfaced that the scan could not see: the sentence is cut mid-clause and another fragment is fused on after the break, so the line ends on a full stop. **105 remain in the dossier wings, across 97 files.** Detail in `UNFINISHED_TEXT_REGISTER.md`.

This is the second defect here to be invisible to the scan written for it. The first was thirty `| **Form** |` cells cut at 150 characters with no mark. Both were found by reading, not by scanning.

## Workstream 4 — Splice seams (queued, not started)

Six shared instruction paragraphs carry a dangling fragment left over from a splice — a clause repeated at the end of a sentence that had already said it.

| Fragment | Field it sits in | Files |
|---|---|---|
| `such as "strange" or "anomalous."` | Appearance protocol | 204 |
| `to repeat;` | Interaction method | 209 |
| trailing `alone.` | Observation method | 281 |
| `. before Work or contact.` | Identification cell | 223 |
| `. a Sorrow Tide, breach, Ordeal, or transformation event.` | Interaction method | 204 |
| `....` | various | 24 |

These are **not** batchable, by `R-18`. The broken grammar is currently the only visible mark on paragraphs that are boilerplate underneath; repairing the grammar across all of them at once would clear the tell and leave the boilerplate. All six fields are already on the per-file rewrite list, so Workstream 1 retires them as it goes. The census is kept here so the scale is not forgotten.

## Workstream 3 — Rules (standing)

`RULES/` holds one file per standing rule. A rule is written there the moment it is stated. Nothing is kept only in conversation.

## Deliberately untouched

- `REGISTRY_MASTER_STATUS.md` lines 324 and 330.
- `**Entry 1 — Containment Description**`, present in 256 files: structural, ruled out of scope.
- Entry numbering across Story Logs: structural furniture, kept (`R-10`).

## Standing blemishes in pushed history

Not repaired, because history is not rewritten (`R-17`).

- A commit message reading `48->??`.
- A commit pushed with two open `label_lint` violations, fixed in a later commit.
- A commit message reading `45->10` where the measured figure was 9.

## Traps that have cost time

- Local git history truncates between turns. `git fetch` + `git reset --mixed FETCH_HEAD` runs first in every commit block.
- `label_lint.py` exits 0 while printing violations.
- `set -e` does not abort on a failing left-hand side of `&&`.
- Two cleaner patterns sharing an opening fragment will eat each other; the assert catches it and aborts before writing.
- Measuring on a hand-rolled line scan gives the wrong population. Use `br.collect`.

