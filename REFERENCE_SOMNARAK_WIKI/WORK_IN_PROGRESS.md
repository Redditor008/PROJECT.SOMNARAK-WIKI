# Work In Progress

> *"Written down because several days of work does not survive in anybody's head."*

This file is the running state of the project. It is updated at the end of every working turn and is the authority on what has been done, what is open, and what comes next. Where it disagrees with recollection, this file is right.

## Measured state

All figures below are measured by `tools/boilerplate_report.py`, not estimated.

| Measure | Value |
|---|---|
| Dossier body lines | 31308 |
| Lines shared by 30+ dossiers | 0 |
| **Headline** | **0.00%** |
| Dossiers in the measured archive | 291 |
| **Dossiers rewritten (fixed counter)** | **291 / 291** |
| Unfinished-text breaks outstanding | 0 |
| **Dossiers free of template residue (Workstream 6)** | **61 / 303** |
| **Dossiers section-clean (`R-27`, every description-bearing section ≤ 0.05)** | **47 / 303** |
| Dossiers file-clean (`R-24`, whole-file fraction ≤ 0.05 — secondary) | 124 / 303 |
| Archive median prose generic fraction | 0.067 |
| **Dispositions classified (Workstream 5)** | **302 / 302 — CLOSED** |

## Workstream 1 — De-boilerplate (CLOSED)

Whole-file rewriting of every dossier in the archive, bespoke per entity. Rules `R-02`, `R-04`, `R-05`, `R-14`, `R-15` all bind here.

**Closed at clean 291 of 291.** Headline 34.3% → **0.00%**. Growth-only throughout: no deletions, no shared annex, no threshold gaming, and the body line count rose from the opening measurement to 31,308. Every clean was its own commit and its own gate chain, per `R-21`. The workstream is reported as closed because the measure it was defined against returns zero, not because the archive is beyond improvement — residual stock phrasing below the 30-dossier threshold still exists in older files and is logged as ordinary maintenance rather than as this workstream.

**Workstream 5 now takes over as the active line of work, and runs under [`R-22`](RULES/R-22_TEN_DISPOSITIONS_PER_BATCH.md) — ten entities per batch, one commit per entity, the `R-18` split stated before any classifying starts, quoted evidence or pending.**

**Progress: 291 / 291 dossiers rewritten — complete.** This denominator is fixed by [`R-20`](RULES/R-20_ONE_FIXED_DENOMINATOR.md) and does not move. The band fractions used before `R-20` — `73 / 73`, `10 / 10`, `8 / 8`, `1 / 76` — are superseded and are not progress figures; they described the queue, and the queue shrinks partly by spillover from other files' cleans. Headline trajectory 34.3% → 0.00%.

### Queue depth — side figures, not progress

These say where the remaining damage sits and which file to open next. A fall in any of them is **not** a clean and is never written as `x / y`.

| Queue tier | Dossiers |
|---|---|
| at 20+ shared lines | 0 |
| at 15+ shared lines | 0 |
| at 10+ shared lines | 0 |
| at 1+ shared lines | 0 |

### Next targets, in order

_Empty._ The measured queue is exhausted: `tools/boilerplate_report.py` returns a census of
`[(0, 291)]` — every dossier in the archive now carries zero lines shared by 30 or more
dossiers. The last shared line was retired by clean 290 (Ninety Seconds, `C-IVδ-918`), which
took thirty files to zero at once by spillover. Clean 291 (Glass Elsewhere, `N-IIβ-903`) was
selected on residual stock rather than on shared lines, that being the only honest measure
left.

Nothing left to re-rank. Files drop down this list as global counts shift without being touched; that movement is spillover and is never counted against the fixed `N / 291` counter. The queue is never carried over from a previous turn without re-measuring.

### Residual floor

Most cleaned files keep 0–13 lines of genuine cross-reference furniture (`**Cross-References:**`, `- See Origin section…`, `**Threat Assessment:**`). These are not chased. The structural floor is 3.1%.

### Completed cleans

Fallow 50→12, Shard 49→9, Ephemera 48→12, Border Tree 48→11, Tear 48→11, Glass 48→12, Portcullis 47→11, Thralldom 47→12, Aphasia 47→12, Forgotten Tear 47→12, Anonym 47→12, Welcome Haven 47→11, Survivors' Breath 47→10, Quagmire 47→10, Yggdrasil Wound 46→13, Repose 46→11, Grasp 46→10, Uprooted 46→11, Sleeping Tree 46→10, Frozen Mirror 45→11, Heirloom 45→9, Spire 45→10, Memory Chain 45→10, Feu Follet 45→10, Broken Whisper 45→9, Ember Phoenix 44→10, Broken Fragment 44→9, Brume 44→11, Myrmidon 44→9, Broken Ruin 44→11, Errant 43→11, Atlas 43→11, Animus 43→10, Conservatory 43→9, Home to No One 43→9, Broken Door 42→10, Tower Erased Overnight 42→9, Relic Waiting for Its Maker 42→9, Exiles' Wall 41→10, Protest No One Remembers 41→10, Pent 41→9, The Silent Child 39→11, Broken Tear 39→10, Relic of a Thousand Owners 38→9, The Wrath Flame 38→10, Soaking Rope 38→11, Sleeping Shard 38→9, Forgotten Silence 38→9, Spreading Root 37→9, Dormant Monolith 37→9, Scar Walker 36→10, Homecoming Tree 36→1, Cenotaph 35→0, Dismissed Cry 35→0, Well of Unfinished Words 34→0, Bridge to Nowhere 33→0, Perennial 33→0, The Vanished Rope 33→1, Candela 33→1, Gavel 33→1, Mourning a Life I Never Lived 32→1, Torpor 32→1, Friendless Bridge 32→0, Risus 32→1, Labyrinth of Stolen Faces 32→1, Mirror of Soaking 31→0, Swallowed Fury 31→1, Stranded Between Two Shores 31→0, Sorrow Gate 31→1, The Lost Prince 31→1, Banyan 30→8 (residual is the standing cross-reference furniture), First Tear 30→0, The Frozen Veil 30→0, Laughing Mask 29→0, Hums 29→1, Apocrypha 28→10 and Homeless Sorrow 28→9 Driftglass 27→8 and Sehnsucht 27→8 and Breach 26→7 and Floating Fragment 25→10 and Neverlast 25→11 and Forgotten Soul 25→11 and Drowned Echo 24→8 and Corrosion Dream 24→9 and Torn Window 24→9 and Door to Nowhere 23→8 and Seething Tundra 21→4 and Mourner's Bloom 21→2 and Frozen Fury 21→0 and Absent Landmark 20→2 and Pandora's Jar 19→7 and Folly 19→1 and Somnium 19→1 and Collapsed Seed 18→0 and Hollow Echo 18→1 and Bridge of the Unchosen 18→0 and Dreaming Ruin 18→0 and Lacrima 17→0 and Hollowcast 16→0 and Miscast 16→0 and Clapperless 16→0 and Neglect Learned to Listen 15→0 and Aphonia 15→0 and Unwitnessed 15→0 and Anger Underfoot 15→0 and The Angry Maiden 15→0 and Unrung 15→0 and Sky of Borrowed Faces 14→0 and Bulwark 14→0 and The Inherited Debt 14→0 and Fading Fruit 14→0 and Doorway to Nowhere 14→0 and Forgotten Name 14→0 and Mirror of Rising 14→0 and The Debt Chain 14→0 and Deadline 14→0 and Sorrow Seed 14→0 and Midnight Choir 14→0 and Unsaid Blossoms 14→0 and Apnea 13→0 and Memory Lake 13→0 and Hollow Architect 13→0 and Barrier of Nothing 13→0 and Nemo 13→0 and Vanity Asleep 13→0 and Harbinger 13→0 and Deteriorata 13→0 and Cold Burn 13→0 and Redacted 13→0 and The Empty Mask 13→0 and Broken Clocktower 13→0 and Double Mouth 13→0 and Carrying Nothing 13→0 and Crucible 13→0 and Pall 13→0 and Flowing Seed 13→0 and Life Behind Glass 12→0 and Weight of Silence 12→0 and Forgotten Shadow 12→0, Vanished Tree 13→0, Thralldom 12→0, Patina 12→0, Last Fruit 12→0, Remembrance 12→0, Torn Flower 13→0, Aphasia 12→0, Black River 12→0, Broken Compass 12→0, Echo of Kindness 12→0, Holdout 12→0, Frozen Tear 12→0, Cleaved 12→0, Rem 12→0, Floating Tree 12→0, Soaking Shadow 12→0, Aegis 12→0, The Silent Maiden 12→0, Harvest Beyond the Gate 12→0, Unheard 12→0, Hollow Tree 12→0, Melting Rope 11→0, The Kind Healer 11→0, Sorrow Storm 11→0, The Grieving Maiden 12→0, Yggdrasil Wound 11→0, Panopticon 11→0, The Lonely Giant 11→0, Portcullis 11→0, Mirror of Broken 12→0, Loom of Unlived Dreams 11→0, Welcome Haven 11→0, Drowned Roots 11→0, The Guarding Bird 10→0, The Smothering Mother 11→0, The Silent Child 11→0, Walking Calendar 11→0, Every Last Goodbye 11→0, Anonym 10→0, Repose 11→0, Border Tree 11→0, Sleeping Weight 10→0, Restless Gap 11→0, Forgotten Soldier 8→0, Rift 11→0, Quagmire 10→0, Neverlast 10→0, Pyre of Truths 10→0, Whispering Gallery 10→0, Swallow 9→0, The Memory Thief 9→0, The Wrath Flame 9→0, Dormant Monolith 9→0, Relic Waiting for Its Maker 9→0, Forgotten Silence 9→0, Broken Tear 9→0, Sleeping Shard 9→0, Home to No One Who Knew Me 9→0, Pent 9→0, Conservatory 9→0, Soaking Rope 9→0, Tear Too Small to Honor 9→0, Broken Whisper 9→0, Protest No One Remembers 9→0, Memory Rain 8→0, Cracked Mirror 8→0, The Orphaned Bell 8→0, I Alone Crossed 8→0, Soaking Shard 8→0, Collapsed Whisper 8→0, Memorial Flame Mid-Ceremony 8→0, Willing Chains 8→0, Spire of Unanswered Prayer 8→0, Driftglass 8→0, Sehnsucht 8→0, Ember Phoenix 8→0, Brume 8→0, Apocrypha 8→0, Broken Fragment 8→0, Relic of a Thousand Owners 8→0, Feu Follet 8→0, Myrmidon 8→0, Atlas 8→0, Forgotten God 7→0, Forgotten Market Stall 7→0, Sorrow Fountain 7→0, Redcage 7→0, Dancing Chains 7→0, Memory Lock 7→0, Devouring Bloom 6→0, Floating Shard 7→0, Rising Well 7→0, Fading Whisper 7→0, Floating Pillar 6→0, Face Beneath Masks 6→0, Briar 6→0, The Rejector 6→0, Learned Your Face 6→0, Frozen Echo 6→0, The Hollow Knight 6→0, The Debtor 6→0, The Inheritor 6→0, The Hollow Saint 6→0, Flotsam 6→0, Broken Well 6→0, The Echo Compass 5→0, Sunken Pillar 6→0, The Rage Statue 5→0, The Masked Dancer 4→0, Broken Mirror 4→0, The Debt Eater 5→0, Kind Healer's Shadow 4→0, Whispering Walls 4→0, Frozen Window 4→0, Broken Promise 4→0, Debt-Collector's Lantern 2→0, The Debt Scale 1→0, The Hollow Choir 1→0, Owed 1→0, The Grieving Colossus 1→0, The Cracked Hourglass 1→0, Broken Clock 1→0, Weeping Willow 1→0, Spreading Well 1→0, Burning Root 1→0, Floating Well 1→0, Screaming Masonry 1→0, Beating Relic 1→0, Thinking Engine 1→0, Eleven Fifty-Nine 1→0, Backward Hour 1→0, Cracked Flesh 1→0, Lethe 1→0, The Foam Flood 1→0, The Happy Mask 1→0 (residual in the others is the standing cross-reference furniture).

## Workstream 6 — Template residue (OPEN, newly measured)

Raised by the archive owner on 2026-10-04, after Workstream 1 closed: *"Some From What You Explain Is Still Templatey Because Of The Previous AI"*. Governed by [`R-23`](RULES/R-23_LABELS_MAY_REPEAT_VALUES_MAY_NOT.md); full finding in [`TEMPLATE_RESIDUE_AUDIT.md`](TEMPLATE_RESIDUE_AUDIT.md).

The owner is right and the `0.00%` is also right. `tools/boilerplate_report.py` measures the `body` scope — `len(s) > 40 and not s.startswith(('|', '#', '>', '`'))` — so **no table row, blockquote or heading was ever counted**. The previous AI's slot-filled cells live exactly there. Workstream 1 is not reopened and its counter is not revised; this is a second measurement of a region the first one never looked at.

**Measured by `/home/user/wikitools/tpl.py`** — a line shared by ≥ 10 dossiers, ≥ 10 words of content, not on the sanctioned-furniture list (table headers, the five system blockquotes, values forced by the SECC code or the entity's role, the two global combat rules).

| Measure | Value |
|---|---|
| Distinct residue lines | 135 |
| Residue instances | 3382 |
| Dossiers carrying residue | 278 / 303 |
| **Dossiers clean (fixed counter)** | **61 / 303** |

Opening baseline was 146 distinct / 3,745 instances / 11 clean. The first ten entities taken under this workstream were all drawn from the Workstream 5 pending pool, so each one closed a disposition row in the same commit as its clean.

Threshold is ten, not thirty, because this defect clusters by entity *role*: six Object/Place dossiers sharing one word-identical breach block is the normal size of it, and a thirty-dossier threshold scores that as zero.

### Order of work

1. **Operative values** — `**First Target**` (48 dossiers), breach `**Movement**` / `**Effect**`, the stock interaction effect cells. These block Workstream 5.
2. **Placeholder-instruction cells** — `**Before/During/After use**`, `**At limit**`, `**Distinctive markers**`, `**Position / movement**`, `**Material / signature**`. ~1,200 instances, mechanical, low risk.
3. **Reader-facing binary choices** — `Endure it … / Struggle free …` (178) and siblings.
4. **Slot-filled Origin prose** in the thin files, done entity by entity alongside its disposition.

Fixes are **growth, not deletion** (`R-15`). A cell is not fixed by removing it or by rewording it just under the threshold.

### Second measure — the Tale standard (`R-24`)

Raised by the owner on 2026-10-05: *"make sure that a lot of text is not just copy & paste … the Tale
section is already fixed."* He is right twice over. The Tale **is** finished — measured across all
298 dossiers that carry one, **no Tale section shares an eight-word run with ten other dossiers** —
and the sections around it are not. Measured with [`sect.py`](RULES/R-24_THE_TALE_STANDARD.md):

| Section | Score | Section | Score |
|---|---|---|---|
| `이야기 (Narratio)` — **The Tale** | **0.00** | `Behavior` | 0.64 |
| `증언 (Testimonium)` | **0.00** | `관찰 기록 (Observation Log)` | 0.65 |
| `SECC Classification` (all furniture) | **0.00** | `Breach Behavior` · `Story Log` | 0.77 |
| `Origin` | 0.16 | `Trivia` · `Expansion Behavior` | 0.80 |
| `Apex` / `Watch` Record | 0.42 / 0.45 | `감각 묘사 (Flavor Text)` | 0.89 |
| `Appearance` | 0.52 | `Registrum` · `Final Observation` | 0.96 |
| `Warden Record` | 0.62 | `M.A.W.` · `Operational Parameters` · `Combat Record` | **0.97–0.98** |

**First two files taken under this rule.** Moktak `N-IIβ-910` went 0.116 → **0.001** and Chain of
Memories `N-IIIβ-200` — then the most generic dossier in the archive — went 0.386 → **0.001** across
seventy rewritten lines, which also released the last entity held pending under Reason 1.
Nine dossiers have now been taken under this rule, worst first:

| Dossier | Before | After | Subs | Words |
|---|---|---|---|---|
| Chain of Memories `N-IIIβ-200` | 0.386 | **0.001** | 70 | 5,476 → 6,607 |
| Survivor's Span `N-IIβ-993` | 0.360 | **0.002** | 62 | 4,859 → 5,966 |
| The Unconsoled `C-IIIγ-248` | 0.298 | **0.000** | 57 | 5,213 → 6,142 |
| The Extinguished `N-IVγ-250` | 0.253 | **0.000** | 55 | 5,623 → 6,396 |
| The Unspoken Line `C-IVδ-251` | 0.247 | **0.001** | 56 | 5,739 → 6,665 |
| The Undelivered Thanks `N-IIIβ-247` | 0.243 | **0.000** | 49 | 5,385 → 6,199 |
| Broken Door `O-IIβ-757` | 0.224 | **0.004** | 62 | 6,625 → 7,760 |
| Vellum Man `C-Iα-900` | 0.224 | **0.000** | 63 | 2,880 → 4,106 |
| Moktak `N-IIβ-910` | 0.116 | **0.001** | 14 | 4,114 → 4,665 |

All nine kept `RESIDUAL 0` and residue 0 and all nine grew. Eight of the nine closed a Workstream 5
row in the same commit, because a dossier cannot be classified while its interaction cells are
instructions to an observer rather than observations. Vellum Man also lost a verbatim duplication
of its Tale inside its Origin section, which `verify.py --dupes` had been reporting for weeks.

**Comparative study.** `COMPARATIVE_STUDY_01_VELLUM_MAN_AND_BROKEN_DOOR.md` sets the two most recent
completions against each other and against two published Abnormality articles (`O-04-72` The
Burrowing Heaven, `T-09-97` Old Faith and Promise). Its three carried-forward findings — Story Log
escalation, the "record X, Y, Z" phrasing as residue even when `tpl.py` is silent, and
instrument-and-hazard unification — are quality bars for Workstream 7.

An earlier version of this block claimed the ten batch-2 dossiers were still generic at 0.103–0.129.
That was the first, furniture-blind cut of the metric. On prose they measure **0.014–0.041** and all
ten are at the standard; the claim has been corrected here and in `R-24` rather than quietly dropped.
What survives in a typical unrewritten file is the Combat Actions flavour text, the Battle Phases,
the M.A.W. appearance and ability lines, the observation-stage cells and the stock interaction
effects — 182 dossiers still sit above 0.05.

One generator artefact was found and repaired by this pass: 29 dossiers published an unevaluated
Python expression in the Combat Record `Difficulty` row, with the entity's numeric suffix standing
where the difficulty word belonged. All 29 were rebuilt from each file's own `Work difficulty` row.

## Workstream 5 — Entity Disposition Index: CLOSED (2026-10-05)

**302 / 302 entity dossiers classified, 0 pending.** The last three were Grasp `O-IVδ-762` (Neutral),
Once Told `O-IVδ-930` (Neutral) and Dawn of Mourning `C-Vω-002` (**Negative** — Breach `Secondary
Effect` raises every other holding's gauge 10% a turn and `First Target` inverts Hope Bearers, which
is the `R-19` Negative mechanism on both limbs).

Three corrections were made at closure and they matter more than the last three rows:

1. **The denominator was wrong.** The index counted against 303 catalogued files, but one of them —
   `Book_of_Regressor_Log_Dramaturgy.md` — is a side-story log with no SECC code and no mechanics.
   It can never carry a disposition. It is now declared out of scope and the denominator is 302.
2. **Ten entities had two rows each**, written in different batches, all in the Neutral section. The
   old counter counted rows rather than distinct codes, so it read 300 when 299 entities were
   covered. The thinner row of each pair was removed and the counter now counts codes.
3. **The tooling now lives in the repository.** `verify.py`, `disp.py` and `gate.sh` had been kept
   outside the repo and were lost when the sandbox reset; everything they had produced survived in
   the working tree, but the tools themselves did not. They have been rebuilt in `tools/` and
   `gate.sh` now fails the commit on an unclosed table row — the check that silently passed three
   times during the `R-25` batches.

## Workstream 7 — The Reset Pass (PLANNED, not started)

**Instructed by the archive owner, 2026-10-05:** *"Later do a reset fixed based the two re-research."*
Scheduled deliberately for later and recorded here now so that the sequencing is not lost.

**What it is.** A single archive-wide pass that re-fixes every dossier against **both** measures at
once, replacing the current one-entity-at-a-time progress:

1. **`tpl.py` — template residue** (`R-23`): a line shared by ten or more dossiers that is not
   sanctioned furniture. Labels may repeat; values may not.
2. **`sect.py` — the Tale standard** (`R-24`): prose generic fraction ≤ 0.05, furniture excluded,
   measured against the one section of the archive that already reads as written rather than
   generated.

**Why it waits.** Three things have to be true before a reset is worth running, and two of them are
not yet:

- The measures must be stable. `sect.py` was recalibrated once already, on its first real use, and a
  reset built on a metric that is still moving would have to be run twice.
- The per-entity method must be proven across enough shapes of dossier. Five are done; the Object,
  Place, Time and Hazard roles each carry a different stock skeleton and at least one of each should
  be finished by hand before the pattern is generalised.
- The rewrite must stay authored. `R-15` growth-only and `R-05` no-paraphrase both still bind: the
  reset is a schedule for doing the work in one sweep, **not** a licence to generate replacement
  text mechanically. A reset that produced a new shared skeleton would simply move the defect.

**Shape it will take when it runs.** Worst-first by `sect.py --files`, one commit per dossier, both
checkers to zero plus the prose measure under 0.05 before the commit, and a disposition row in the
same commit wherever the dossier is still pending — which is what the last five have done.

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

