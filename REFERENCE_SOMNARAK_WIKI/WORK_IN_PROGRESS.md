# Work In Progress

> *"Written down because several days of work does not survive in anybody's head."*

This file is the running state of the project. It is updated at the end of every working turn and is the authority on what has been done, what is open, and what comes next. Where it disagrees with recollection, this file is right.

## Measured state

All figures below are measured by `tools/boilerplate_report.py`, not estimated.

| Measure | Value |
|---|---|
| Dossier body lines | 28126 |
| Lines shared by 30+ dossiers | 4917 |
| **Headline** | **17.48%** |
| Dossiers still at 30+ shared lines | 19 |
| Dossiers fully cleaned | 68 |
| Unfinished-text breaks outstanding | 0 |

## Workstream 1 — De-boilerplate (open)

Whole-file rewriting of the worst-affected dossiers, one file per turn, bespoke per entity. Rules `R-02`, `R-04`, `R-05`, `R-14`, `R-15` all bind here.

**Progress: 68 / 87.** Headline trajectory 34.3% → 17.48%.

### Next targets, in order

| Shared lines | Dossier |
|---|---|
| 31 | `SE-C-IVδ-252_Sorrow_Gate_슬픔의_문.md` |
| 31 | `SE-C-IVδ-103_The_Frozen_Veil_얼어붙은_베일.md` |
| 31 | `SE-C-IVγ-091_The_Lost_Prince_잃어버린_왕자.md` |
| 31 | `SE-C-IIβ-210_Laughing_Mask_웃는_가면.md` |
| 30 | `SE-N-IVδ-967_Pandoras_Jar_사라진_유물.md` |
| 30 | `SE-N-IVδ-606_Banyan_가라앉은_나무.md` |
| 30 | `SE-N-IIβ-170_Aphonia_침묵의_비명.md` |
| 30 | `SE-N-IIIγ-283_Barrier_of_Nothing_녹슨_벽.md` |

Re-rank after every clean. Files drop into the top band as global counts shift; the queue is never carried over from a previous turn without re-measuring.

### Residual floor

Every cleaned file keeps 9–13 lines of genuine cross-reference furniture (`**Cross-References:**`, `- See Origin section…`, `**Threat Assessment:**`). These are not chased. The structural floor is 3.1%.

### Completed cleans

Fallow 50→12, Shard 49→9, Ephemera 48→12, Border Tree 48→11, Tear 48→11, Glass 48→12, Portcullis 47→11, Thralldom 47→12, Aphasia 47→12, Forgotten Tear 47→12, Anonym 47→12, Welcome Haven 47→11, Survivors' Breath 47→10, Quagmire 47→10, Yggdrasil Wound 46→13, Repose 46→11, Grasp 46→10, Uprooted 46→11, Sleeping Tree 46→10, Frozen Mirror 45→11, Heirloom 45→9, Spire 45→10, Memory Chain 45→10, Feu Follet 45→10, Broken Whisper 45→9, Ember Phoenix 44→10, Broken Fragment 44→9, Brume 44→11, Myrmidon 44→9, Broken Ruin 44→11, Errant 43→11, Atlas 43→11, Animus 43→10, Conservatory 43→9, Home to No One 43→9, Broken Door 42→10, Tower Erased Overnight 42→9, Relic Waiting for Its Maker 42→9, Exiles' Wall 41→10, Protest No One Remembers 41→10, Pent 41→9, The Silent Child 39→11, Broken Tear 39→10, Relic of a Thousand Owners 38→9, The Wrath Flame 38→10, Soaking Rope 38→11, Sleeping Shard 38→9, Forgotten Silence 38→9, Spreading Root 37→9, Dormant Monolith 37→9, Scar Walker 36→10, Homecoming Tree 36→1, Cenotaph 35→0, Dismissed Cry 35→0, Well of Unfinished Words 34→0, Bridge to Nowhere 33→0, Perennial 33→0, The Vanished Rope 33→1, Candela 33→1, Gavel 33→1, Mourning a Life I Never Lived 32→1, Torpor 32→1, Friendless Bridge 32→0, Risus 32→1, Labyrinth of Stolen Faces 32→1, Mirror of Soaking 31→0, Swallowed Fury 31→1, Stranded Between Two Shores 31→0.

## Workstream 2 — Unfinished text (closed on both scans)

**391 breaks completed.** 312 that ended a line, and 79 more that did not — cut mid-clause with another fragment fused on after the break, so the line ended on a full stop and read as finished. Both scans now return zero. Detail in `UNFINISHED_TEXT_REGISTER.md`.

26 mid-line ellipses remain and are deliberate: dramatic pauses in dialogue and testimony. They were each read before being left alone.

Two defects here were invisible to the scan written for them — thirty `| **Form** |` cells cut at 150 characters with no mark, and these 79. Both were found by reading a file, not by scanning the archive.

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
- Changing a Story Log entry tag without changing the entry under it leaves the document claiming to be one thing and reading as another. Caught in Forgotten Silence after the tag was rewritten and the paragraph was not.
- Measuring on a hand-rolled line scan gives the wrong population. Use `br.collect`.

