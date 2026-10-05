# Template Residue Audit — the part of the dossier Workstream 1 could not see

**Raised:** 2026-10-04 · **Rule:** [`R-23`](RULES/R-23_LABELS_MAY_REPEAT_VALUES_MAY_NOT.md)
**Tool:** `/home/user/wikitools/tpl.py` · **Scope:** all 303 catalogued dossiers (both wings)

---

## Why this audit exists

The owner's observation, verbatim: *"Some From What You Explain Is Still Templatey Because Of
The Previous AI"* — made after Workstream 1 reported a headline of `0.00%`.

Both statements are true at once, and the reason is a scope boundary rather than a mistake in
the count.

`tools/boilerplate_report.py` measures the `body` scope:

```python
body = lambda s: len(s) > 40 and not s.startswith(('|', '#', '>', '`'))
```

A line that begins with a pipe is a table row, and **no table row was ever counted**. The same
goes for blockquotes and headings. Workstream 1 drove shared *paragraph prose* at a thirty-
dossier threshold from 34.3% to 0.00% across 291 files, and that result stands. It simply never
looked inside the tables, which is where this archive keeps most of its operative text.

## The measurement

Residue = a line shared by **≥ 10 dossiers**, carrying **≥ 10 words** of content, that is **not**
sanctioned furniture. The sanctioned list lives in `tpl.py` and covers table headers and
separators, the five system blockquotes (R.D. Operational Record, R.D. Field Parameters,
Mechanics Reference, M.A.W. definition, Object/Place Work Rule), the rows whose value is forced
by the SECC code or by the entity's role, and the two global combat rules.

Opening baseline, 2026-10-04:

```
dossiers                      303
distinct residue lines        146  (shared by >= 10 dossiers)
residue instances            3745
dossiers carrying residue     292 / 303
clean dossiers                 11
median residue per dossier     13
```

After the first ten entities:

```
distinct residue lines        136
residue instances            3481
dossiers carrying residue     282 / 303
clean dossiers                 21
```

**Counter: 92 / 303 dossiers free of template residue.**

The first ten were chosen from the Workstream 5 pending pool on purpose, so that each clean
closed a disposition row in the same commit: Moktak `N-IIβ-910`, Weighted Silence `O-IIIγ-924`,
Dead Air `N-IIIγ-929`, Dreaming Plague `N-IVδ-927`, Miasma `C-IVδ-922`, Hatred Above `C-IVδ-923`,
Sorrow Mass `C-Vω-925`, Unwaking Block `N-IIIγ-908`, Dawn That Forgot `N-IIIγ-917`, Allhallow
`O-IIIγ-916`. Each went from 13–22 residue lines and 34 verifier residuals to zero on both tools,
growing by 850–1,100 words; none lost a section. The stock-breach-block holding ground named in
the disposition index now holds nobody.

Threshold ten, not thirty, because this defect clusters by *role* rather than across the whole
archive. Six Object/Place dossiers sharing one word-identical breach block is the defect at its
normal size, and a thirty-dossier threshold scores that as zero.

## The eleven clean dossiers

`Soot_Fry` · `Blessing_Giver` · `Apostle_Maker` · `Dawn_of_Mourning (C-Vω-002)` ·
`Wilderness_Tide` · `The_Music_Box_of_Agony` · `The_Unbroken_Pledge` · `The_Ancestral_Guilt` ·
`The_Glass_Silt_Drifter` · `The_Singing_Needle` · `Book_of_Regressor_Log_Dramaturgy`

They matter because they prove the target is reachable inside the existing format. None of them
dropped a section to get there.

## The worst twelve

| Residue lines | Dossier |
|---|---|
| 31 | `SE-N-Iα-686` Torn Window |
| 29 | `SE-O-IIIγ-233` Forgotten Soul |
| 29 | `SE-O-IIβ-119` Homeless Sorrow |
| 29 | `SE-O-Iα-453` Floating Fragment |
| 28 | `SE-N-IVδ-606` Banyan |
| 27 | `SE-C-Vδ-111` The Final Door |
| 27 | `SE-N-IVδ-339` Breach |
| 27 | `SE-O-IIβ-378` Drowned Echo |
| 27 | `SE-O-IIβ-922` Door to Nowhere |
| 26 | `SE-N-IIIβ-200` Chain of Memories |
| 26 | `SE-O-IIIγ-915` Corrosion Dream |
| 23 | `SE-C-IVγ-176` Loom of Unlived Dreams |

## The ten heaviest residue lines

| Dossiers | Line |
|---|---|
| 207 | `| **After use** | Removal or discharge, injuries, lingering effects, cooldown, repair need, reuse authorization. |` |
| 206 | `| **During use** | Activation time, visual feedback, effect strength, target or protected area, first cost. |` |
| 206 | `| **At limit** | Duration, activations, attribute changes, rejection signs, and source behavior. |` |
| 178 | `| Endure it — bear the weight without flinching. | Struggle free — try to throw it off. |` |
| 99 | `| **Recommended response** | Reduce Gauge through the listed valid Work Types; Object/Place entities use Viderehan and Ferrehan only. |` |
| 96 | `| Weep with it — share the sorrow aloud. | Hold your composure — refuse to feel it. |` |
| 61 | `| **Distinctive markers** | Confirm the primary form and elemental signature before contact. |` |
| 60 | `| **Activation or escalation** | The team records the first visible activation, breach, or expansion change … |` |
| 48 | `| **First Target** | The nearest personnel or the one whose sorrow matches the entity's origin. |` |
| 47 | `| **Position / movement** | The subject manifests independently within the registered area; posture and distance must be recorded. |` |

Read them together and the diagnosis is unambiguous. Four of the ten are the authoring
template's **own field list**, published as content — the previous AI filled the entity's name
into the furniture and left the instructions where the values belonged. Two are a binary choice
offered to the reader in words that have nothing to do with the entity in front of them. One,
`**First Target**`, is an *operative* value shared by 48 unrelated entities, and it is the single
line most responsible for Workstream 5's pending pool.

## Re-research: how the reference wikis draw the same line

Re-checked 2026-10-04 against `lobotomycorporation.wiki.gg/wiki/Nothing_There`,
`lobotomycorporationmodded.wiki.gg/wiki/Template:AbnormalityPage`, and
`lobotomycorp.fandom.com/wiki/Example_Page`.

The published page and the template page of the same wiki share **all** their furniture: the
infobox, the section order (Appearance → Ability → Details → E.G.O. → Story → Flavor Text →
Trivia), the work-favour grid, the observation-level list. Nothing about repetition at that
level is a defect; it is the format working.

What separates them is the values:

| | Template page | Published page |
|---|---|---|
| Ability | *"Placeholder for Ability Description"* | *"Decrease by 1 when an employee completes the work with Justice Level 3 or lower. This takes priority over its other mechanics."* |
| Work favour | `"Chance" (%)` in every cell | measured percentages per work and level |
| Escape info | `0 Immune` in every damage type | the entity's actual resistances |
| Story | empty observation levels | distinct in-world text per level |

Our dossiers inherited the furniture correctly, and in roughly 3,700 places they published the
placeholder with it. Where a value is genuinely unknown, the convention on those wikis is a
redaction — `███████`, `<name>` — never a field list and never a trailing instruction.

## What this is not

- **Workstream 1 is not reopened and its counter is not revised.** `291 / 291`, `0.00%`, census
  `[(0, 291)]` remain exactly true of shared body prose at thirty dossiers. This is a different
  measurement of a different region, with its own tool and its own denominator (`R-20`).
- **This is not a formatting complaint.** A dossier is not improved by deleting the `**After
  use**` row. It is improved by that row saying what happens after *this* entity's M.A.W. is
  used. Fixes are growth, as in Workstream 1 (`R-15`).
- **This is not optional for Workstream 5.** The 48 pending dispositions are pending because
  their operative cells are stock. Classifying them requires authoring first; reading harder
  will never produce an answer that the file does not contain.

## Order of work

1. **Operative values first** — `**First Target**`, breach `**Movement**` / `**Effect**`,
   interaction effect cells. These are the ones that block Workstream 5 and the ones a reader
   would call wrong rather than thin.
2. **Placeholder-instruction cells** — the `**Before/During/After use**` and `**At limit**`
   family, `**Distinctive markers**`, `**Position / movement**`, `**Material / signature**`.
   Highest instance count, most mechanical to fix, lowest risk.
3. **Reader-facing binary choices** — the `Endure it … / Struggle free …` pair and its siblings,
   which should name what *this* entity makes a person want to do.
4. **Slot-filled Origin prose** — the *"Space was the vessel; spirit was the content"* paragraph
   shape in the thin files. Lowest instance count, highest authoring cost, done entity by entity
   alongside its disposition.

Progress is reported as `clean / 303` under `R-16` and `R-20`, re-measured by `tpl.py` each
time, never incremented by hand.

---

# Second measure: generic prose, by 8-gram sharing

**Raised:** 2026-10-05 by the archive owner — *"make sure that a lot of text is not just copy &
paste text … for real info … the Tale section is already fixed."*
**Tool:** `/home/user/wikitools/sect.py`

## Why a second measure was needed

`tpl.py` and `boilerplate_report.py` both compare **whole lines**. A paragraph produced from a
pattern and then given a different noun is not a repeated line, so neither tool can see it. The
owner can. This measure compares **8-word shingles**: a shingle is *shared* when it occurs in ten
or more dossiers, and a dossier's **generic fraction** is the share of its own shingles that are
shared ones.

## The benchmark is the Tale, and the owner was right about it

The standard is not invented; it is taken from the part of the archive that is already finished.

| Section | Score | Dossiers |
|---|---|---|
| `## 이야기 (Narratio)` — **The Tale** | **0.00** | 298 |
| `## 증언 (Testimonium)` | **0.00** | 298 |
| `## Origin` | 0.16 | 298 |
| `## Apex Record` | 0.42 | 80 |
| `## Watch Record` | 0.45 | 71 |
| `## Warden Record` | 0.62 | 82 |
| `## Trivia` | 0.80 | 298 |
| `## Behavior` · `## Breach Behavior` | 0.88 | 298 / 185 |
| `## 감각 묘사 (Flavor Text)` | 0.89 | 298 |
| `## Appearance` | 0.90 | 298 |
| `## 관찰 기록 (Observation Log)` | 0.93 | 298 |
| `## 최종 관찰 (Final Observation)` | 0.96 | 298 |
| `## 기록 (Registrum)` | 0.97 | 298 |
| `## M.A.W. Equipment` · `## 이야기 보고 (Story Log)` | 0.99 | 298 |
| `## Operational Parameters` · `## Combat Record` · `## Activation Behavior` · `## Expansion Behavior` | **1.00** | 302 / 302 / 87 / 45 |

**Not one of the 298 Tale sections shares an eight-word run with ten other dossiers.** It is the
only long-prose section in the archive that is wholly bespoke, and it is therefore the standard
every other narrative section is measured against from here on.

Two things in that table are uncomfortable and are recorded rather than smoothed:

1. **`Operational Parameters` and `Combat Record` score 1.00** — every dossier in the archive.
   Much of that is legitimate furniture (stat labels, the R.D. blockquotes, values forced by the
   SECC code), but not all of it: the Combat Actions rows carry mad-libbed flavour text
   (*"It begins as a whisper in the ‹element›."*, *"All at once, the pressure concentrates."*) and
   the Battle Phases are three sentences with the manifestation word swapped.
2. **The bespoke sections I wrote are not at 0.00 either** — `Warden Record` 0.62, `Watch Record`
   0.45, `Apex Record` 0.42. They are original per entity, but they have acquired a house tic
   (*"the file records that…"*, *"the archivist's note adds…"*). That is the same defect at a
   smaller amplitude and it is mine, not the previous AI's.

## Archive counter

```
dossiers                      303
shared 8-grams (>= 10 files)  3771   (prose only; R-23 furniture excluded)
median generic fraction       0.052
worst                         0.195
clean at <= 0.05              148 / 303   (file level; section-clean is 71)
```

**Counter: 71 / 303 dossiers section-clean (`R-27`) — every description-bearing section at or
under 0.05. Secondary: 148 / 303 file-clean on the whole-file fraction.**

**Seventh `R-27` batch, 2026-10-05 — six shipped; the `R-26` ratchet fired again.**

| Dossier | Dirty sections | Dirty lines | Instrument the repair gave it |
|---|---|---|---|
| Forgotten God `C-Vδ-265` | 10 | 50 | a 41-second breathing interval, and a count of staff who remember it exists: 19 → 6 |
| Glass Elsewhere `N-IIβ-903` | 6 | 35 | 90-second channels, logged by category — *home*, *workplace*, *public* — never by face |
| Breathing Stone `C-IVδ-907` | 6 | 30 | two respiration series, the wall's and the observer's, deliberately never reconciled |
| Labyrinth of the Unfinished Mind `C-IVδ-909` | 6 | 27 | 41 surveyed rooms, 61 thoughts finished across descents by different people |
| Ninety Seconds `C-IVδ-918` | 5 | 28 | the pass count, and one content-free exit question that works 202 times in 211 |
| Thinking Engine `C-IIIγ-904` | 4 | 22 | 61 unrequested findings, 58 of them verified correct, all of them forbidden to act on |

Six rather than five because five of them were the part-bespoke tier `R-26` calls simple — 22 to 35
dirty lines, four to six sections — and the gate passed first time on each. The seventh slot went on
clearing eight stock phrases out of Thinking Engine's Story Log instead, which was the better use
of it.

A pattern across this batch worth recording: in five of the six, **the containment measure is a
sentence somebody has to say.** The exit question at Ninety Seconds, the category-only log at Glass
Elsewhere, the blank cause-line at Rising Well in the previous batch, the naming count at Forgotten
God, the prohibition on reading a sheet at the Thinking Engine. None of them is a barrier and all of
them are defended annually against people with good reasons.


**Sixth `R-27` batch, 2026-10-05 — the two ω/δ-grade files that had been held.**

| Dossier | Dirty sections | Dirty lines | What the rewrite had to resolve |
|---|---|---|---|
| The Convergence `C-Vδ-010` | 11 | 60 | an entity that has existed for **36 seconds in eleven years** |
| Dawn of Mourning `C-Vω-001` | 11 | 62 | an entity that **has never formed at all** |

These two raised a problem the earlier batches did not. Both files were full of confident
operational prose about things nobody has observed — breach behaviour, escalation rates, sensory
progressions — for entities with, respectively, thirty-six seconds of total observation and none.
The rewrite could not replace that with better-invented detail; it had to **mark the projections as
projections**. Every modelled row in both files now says so on its face, and the sections that
cannot honestly be filled say that instead:

- Convergence: *"There is no observation method for the fused form and the station has stopped
  pretending otherwise."* What it has instead is a drill — 188 timed separations, median eight
  seconds, against a twelve-second window that has twice been met with one second to spare.
- Dawn of Mourning: *"This file documents something that has not happened and is written so that
  nobody mistakes it for something that has."* Its real contents are a blessing register at eleven
  of twelve, a list of four names, a charm that gets colder, and three people who can tell a genuine
  confession from a performed one **38 times in 41**.

Both files also now carry a rule against circular citation: neither may be used as evidence in the
other, and neither may upgrade a projection to a finding on the way in. That had already happened
twice — the Dawn's escalation figure originates in its own file and had been cited back at it as
corroboration from three others.


**Fifth `R-27` batch, 2026-10-05 — three shipped.**

| Dossier | Worst section before | Dirty sections | Instrument the repair gave it |
|---|---|---|---|
| The Echo Compass `C-IIIβ-016` | M.A.W. **0.764** | 7 | settle rate — 94 bearings in 188 two-minute channels |
| Rising Well `C-IVδ-869` | M.A.W. **0.752** | 7 | shaft height above its own collar, and a cause-line that must stay blank |
| Broken Mirror `C-IIα-081` | M.A.W. **0.751** | 8 | 188 shards, 41 authorised viewings, against the Keepers' erasure register |

M.A.W. Equipment has now replaced Behaviour at the head of the section league: the stock
*"Appearance: a [shape] of [element] Han-[material]"* / *"Cost: the wielder loses small nameless
memories"* block is the densest surviving generated text in the archive.

Three shipped rather than five: each of these carried 43–45 dirty lines across seven or eight
sections, and the two remaining files at this level — The Convergence `C-Vδ-010` and Dawn of
Mourning `C-Vω-001` — carry 60 and 62. Those two are ω/δ-grade canon with eleven dirty sections
apiece and are first in the next batch.


**Fourth `R-27` batch, 2026-10-05 — three shipped, two held, and three repairs to my own earlier work.**

| Dossier | Worst section before | Dirty sections | Instrument the repair gave it |
|---|---|---|---|
| Vanished Tree `C-Iα-622` | Behavior **0.845** | 7 | visible seconds per pass, 19 → 4, against the frontier map reissues |
| Rift `C-IVδ-193` | Behavior **0.827** | 9 | the gap where two sides stop matching, 1.1 m → 2.9 m |
| Flotsam `C-IIβ-782` | M.A.W. **0.806** | 10 | 611 outlined objects, 41 with a use anybody can still state |

**Held: Broken Compass `C-IIβ-290` and Melting Rope `N-IIIγ-447`.** The turn went instead on three
corrections to work done in earlier turns, which was the better use of it:

1. **`every a manifestation`** — the `R-28` word sweep had produced ungrammatical stock in 36 files
   (*"every a manifestation, every Sorrow Tide"*). Repaired.
2. **`after any a transformation in place`** — the same fault in another 12 files. Repaired.
3. **The sweep's own replacement sentences had become residue.** `R-28` wrote the same
   `Event type (non-breach)` sentence into sixteen dossiers, which pushed it over the ten-file
   sharing threshold and made it exactly the kind of generated line this workstream exists to
   remove. Each is now built from the dossier's own name, location and recorded effect; maximum
   repeat is 1.

That third one is the lesson worth keeping: **a corrective sweep that writes the same sentence into
more than nine files has created new boilerplate, and `R-23` applies to the fix as much as to the
original.**


**Third `R-27` batch, 2026-10-05 — five dossiers, worst section first.**

| Dossier | Worst section before | Dirty sections | Instrument the repair gave it |
|---|---|---|---|
| Remembrance `C-IIIγ-115` | Behavior **0.855** | 9 | rim gauge against the Grand Archive's own backlog of unentered deposits |
| Weight of Silence `N-IIα-285` | Behavior **0.855** | 6 | words per hour, counted by hand, against consultations closed without a reply |
| Holdout `C-IIβ-240` | Behavior **0.854** | 8 | a stone count rising with the city's demolitions, falling on a memorial reading |
| The Guarding Bird `C-IIIγ-033` | Behavior **0.851** | 7 | the grey measured at four bearings, 4 m to 11 m in nine years |
| Mirror of Broken `N-IIIγ-127` | Behavior **0.845** | 7 | a shard count against the Gate's exit register |

**A regression from the `R-28` sweep was caught here and fixed.** The bare-word pass had replaced
the entity name *Breach* (`N-IVδ-339`) with *event* inside Holdout's Interaction Record, and had
left Memory Lock reading *"does not open, event, or spread"*. An archive-wide scan found eight
candidate lines, six of them legitimate sentence-internal substitutions and two genuine damage; both
are repaired. The lesson is recorded: a word-level sweep over an archive that contains an entity
**named** for that word needs a name list, not a word boundary.


**Second `R-27` batch, 2026-10-05 — five dossiers, worst section first.**

| Dossier | Worst section before | Dirty sections before | After |
|---|---|---|---|
| Hollow Tree `C-IVγ-205` | Behavior **0.891** | 7 | all clean |
| Pall `C-IIβ-280` | Behavior **0.886** | 8 | all clean |
| Panopticon `C-IIβ-235` | Behavior **0.875** | 8 | all clean |
| Last Fruit `C-IIβ-777` | Behavior **0.870** | 7 | all clean |
| Sleeping Weight `C-IVδ-357` | Behavior **0.859** | 7 | all clean |

Five rather than seven: these carried 35–44 dirty lines each across seven to nine sections, which is
whole-file work by `R-26`'s test and not the section repair the first `R-27` batch was. The ratchet
holds at five until the queue returns to part-bespoke files.

Behaviour has replaced 최종 관찰 at the head of the section league — the stock *"Work Type data is one
input among many"* / *"Work success is measured by the entity's response"* pair, which scores 0.85
to 0.89 wherever it survives.


The headline moved because the measure did. `R-27` (2026-10-05) holds that the Tale standard
applies to every section that carries description — Behaviour being one example, not the list —
and measuring that way found **81 dossiers that passed at file level with at least one section
still above 0.05**, nine of them with a section at **1.000**. The file-level number is kept beside
it because it still measures total archive drift honestly; it is simply not the standard.

**First `R-27` batch, 2026-10-05 — seven dossiers, the `R-26` ratchet's first firing.**

| Dossier | Worst section before | After |
|---|---|---|
| Endless Shift `C-IVδ-915` | 최종 관찰 **1.000** | all 19 sections clean |
| Grimoire `C-IIβ-906` | 최종 관찰 **1.000** | all clean |
| Duri's Heart `C-IIβ-901` | 최종 관찰 **1.000** | all clean |
| Lethe `C-IIIγ-928` | 최종 관찰 **1.000** | all clean |
| Cracked Flesh `C-IIIγ-921` | 최종 관찰 **1.000** | all clean |
| Backward Hour `C-IIIγ-913` | 최종 관찰 **1.000** | all clean |
| Eleven Fifty-Nine `C-IIIγ-912` | 최종 관찰 **1.000** | all clean |

Seven rather than five because `R-26`'s second test was finally met: all seven were already
part-bespoke at file level, so the work was section repair rather than whole-file rewriting —
20 to 30 keyed lines each instead of 50 to 60.

**Section league, worst first, measured the day `R-27` was written:**

| Dirty in | of | Section |
|---|---|---|
| 248 | 298 | 최종 관찰 (Final Observation) |
| 225 | 297 | M.A.W. Equipment |
| 221 | 302 | Combat Record |
| 185 | 298 | 감각 묘사 (Flavor Text) |
| 156 | 298 | Trivia |
| 145 | 297 | 기록 (Registrum) |
| 132 | 298 | Behavior |


**Second `R-26` batch, 2026-10-05 — five shipped, all by the keyed-line method.**

| Dossier | Before | After | Instrument |
|---|---|---|---|
| The Final Door `C-Vδ-111` | 0.228 | **0.001** | a thirteen-second whisper, forty-one transcripts, no two alike |
| Laughing Mask `C-IIβ-210` | 0.215 | **0.003** | the length of each silence against the district's demeanour standards |
| Pandora's Jar `N-IVδ-967` | 0.211 | **0.002** | air temperature at four bearings against the facility's disposal register |
| Sorrow Tide `C-Vγ-260` | 0.198 | **0.000** | nine gauge stations, a printed almanac, and shelter attendance |
| Banyan `N-IVδ-606` | 0.197 | **0.005** | root depth at eleven points against the district's public-display record |

**The ratchet still has not fired, and the reason has changed.** Last batch the five worst were
simply hard. This time a scan established something structural: **there are no short-form dirty
dossiers left at all.** Every one of the 182 files still above 0.05 is long-form. `R-26`'s first
route to seven and ten — short-form simplicity — is therefore closed for the rest of this
workstream, and the ratchet can only fire on the second route, part-bespoke files under about 0.15.
Those exist in quantity and will be reachable once the worst-first queue drops below that line.

**No duplicated-Tale files remain anywhere in the archive**; the last of the seven was cleared in
an earlier batch, and the scan now returns a single file with any repeated paragraph at all.


**First `R-26` batch, 2026-10-05 — five shipped; the ratchet did not fire, and why.**

| Dossier | Before | After | Instrument |
|---|---|---|---|
| Seething Tundra `C-Iα-884` | 0.266 | **0.006** | tear count in the shard against the Gardens' deposit register |
| Door to Nowhere `O-IIβ-922` | 0.256 | **0.002** | handle height against the district's movement orders |
| The Maw `C-IVω-001` | 0.241 | **0.000** | 41 perimeter markers and a roll of 61 names out of a thousand |
| Forgotten Soul `O-IIIγ-233` | 0.232 | **0.003** | track length and brightness against the facility's unnamed totals |
| Drowned Echo `O-IIβ-378` | 0.232 | **0.005** | the interval between calls against the tunnel log's acknowledgement column |

`R-26` allows seven, then ten, when the files are *simple*. These five were the opposite: 5,400–6,600
words each, full Interaction Records, prose 0.23–0.27. By the rule's own test they are the hard
category, and five was the honest number. The ratchet is live and will fire on the first batch that
is genuinely short-form.

**Method change, adopted mid-batch and worth keeping.** Seething Tundra was rewritten by replacing
*sentences* and scored 0.048 — barely clean — because each rewritten line kept the tail of its
generic original (*"Personnel should not transfer assumptions…"*, *"The R.D. record describes a
living sorrow pattern…"*). Those tails are themselves shared text. Every file after it was rewritten
by replacing **whole lines, keyed on a unique prefix**, and scored 0.000–0.005 on the first pass with
no follow-up heredoc. The keyed-line form is now the default.


**Fourth `R-25` batch, 2026-10-05 — three of five shipped, two held.**

| Dossier | Before | After | Instrument |
|---|---|---|---|
| Torn Window `N-Iα-686` | **0.291** | **0.002** | forty-one hands in the glass, against the lower network's patrol sheet |
| Floating Fragment `O-Iα-453` | 0.281 | **0.005** | audible radius in metres against the Row registry's open-file count |
| Homeless Sorrow `O-IIβ-119` | 0.278 | **0.006** | occupancy hours in the assigned room against the sector's reallocation register |

Torn Window had been the archive's worst file since the measure was introduced; the new worst is
Seething Tundra `C-Iα-884` at 0.266. **Held: Seething Tundra `C-Iα-884` and Door to Nowhere
`O-IIβ-922`** — not for any defect in the dossiers, but because the turn had already absorbed a
sandbox reset and the rebuilding of the tooling, and `R-25`'s quality clause is worth more than its
size clause. They are first in the next batch.


**Final `R-25` batch, 2026-10-05 — the three remaining unclassified dossiers.**

| Dossier | Before | After | Instrument |
|---|---|---|---|
| Grasp `O-IVδ-762` | 0.136 | **0.002** | gap width against the figure's reach — short by a metre at all eleven positions |
| Once Told `O-IVδ-930` | 0.130 | **0.001** | the utterance log: what was said, by whom, what arrived, and the lag in seconds |
| Dawn of Mourning `C-Vω-002` | 0.013 | 0.013 | already bespoke; only a stock Stigma line was replaced |

Dawn of Mourning needed no rewrite — it was written as canon from the start and scores 0.013. It had
simply never been classified, which is worth recording: a dossier can sit unclassified for reasons
that have nothing to do with its prose.


**Third `R-25` batch, 2026-10-05 — five dossiers, five commits, all gated.**

| Dossier | Before | After | Instrument |
|---|---|---|---|
| Once Upon `O-IIIγ-920` | 0.165 | **0.001** | a register of 74 stories, nine with no living recogniser |
| Heirloom `O-IVδ-909` | 0.160 | **0.004** | four wall-survey pins: 3.1 m in Year 4,226, 4.4 m now |
| Uprooted `O-IIIγ-959` | 0.151 | **0.004** | the nightly route plotted against nineteen abandoned plots |
| Sleeping Tree `O-IIIγ-374` | 0.148 | **0.005** | quarterly girth at four stations and the four-minute creak interval |
| Passing Bell `N-IIβ-919` | 0.140 | **0.001** | a ledger of 61 warnings, nine matched after the fact |

All five Neutral. Once Upon and Passing Bell each lost a verbatim Tale-inside-Origin duplication,
bringing that total to six — every one of them in a short-form dossier. Two follow-up commits
(`754adcc7`, `1333850b`) restored closing pipes dropped from Once Upon's tables during the rewrite;
`gate.sh` does not fail on `verify.py pipe False`, so the check must be read by eye after every
table edit.


**Second `R-25` batch, 2026-10-05 — five dossiers, five commits, all gated.**

| Dossier | Before | After | Instrument |
|---|---|---|---|
| Animus `O-Iα-108` | 0.189 | **0.008** | a lexicon of 61 words with no proper noun in it |
| Forgotten Tear `O-Iα-709` | 0.185 | **0.003** | a laboratory balance: 11 g untouched, up to 34 g held |
| Memory Chain `O-IIβ-467` | 0.175 | **0.005** | transit time along one axis, 41 s baseline, and the word order |
| Never Discharged `O-IIβ-911` | 0.173 | **0.001** | a 47-minute loop clock and a discharge book that cannot be completed |
| Shard of a Broken Promise `O-IVδ-851` | 0.172 | **0.001** | hum pitch in hertz against a declaration book |

All five classified Neutral. Never Discharged also lost a verbatim Tale-inside-Origin duplication —
the fourth found so far, and all four were in the short-form dossiers.


**Batch under `R-25`, 2026-10-05 — five dossiers, five commits, all gated.**

| Dossier | Before | After | Subs | Disposition |
|---|---|---|---|---|
| Frozen Mirror `O-Iα-643` | 0.208 | **0.003** | 58 | Neutral |
| Amnesia `O-IIβ-914` | 0.194 | **0.000** | 60 | Neutral |
| Fallow `O-Iα-554` | 0.194 | **0.001** | 50 | Neutral |
| Broken Ruin `O-IIIγ-559` | 0.191 | **0.009** | 56 | Neutral |
| Exiles' Wall `O-IIIγ-617` | 0.190 | **0.008** | 52 | Neutral |

Two of the five (Amnesia, and earlier Vellum Man) also lost a verbatim duplication of the Tale
inside the Origin section, which `verify.py --dupes` had been reporting unaddressed.


The threshold is set at 0.05 because that is what the eleven already-bespoke dossiers achieve
(0.012–0.046) with all their furniture intact. Zero is not reachable at file level and is not the
target; the furniture is supposed to match.

**Corrected 2026-10-05.** The first cut of this measure hashed whole files, so a dossier was scored
on the `R-23` furniture it is supposed to share — the R.D. Operational Record blockquote alone
contributes twenty-five shared shingles to every file carrying it. On that basis the batch-2 ten
looked unfinished at 0.103–0.129. `sect.py` now excludes furniture before shingling and those ten
measure **0.014–0.041**: they were at the standard already. The counters above and in
`WORK_IN_PROGRESS.md` are the prose-only figures.

What the corrected measure does find is a long tail of dossiers that passed Workstream 1 and both
line-level tools and are still written from a pattern. Chain of Memories `N-IIIβ-200` read
**0.386** at `RESIDUAL 0`; seventy of its lines were generated prose, including four whole
paragraphs and every cell of its observation and interaction tables. Rewritten, it reads **0.001**.

## A generator artefact found by this pass

Twenty-nine dossiers published an **unevaluated Python expression** in the Combat Record table:

```
| **Difficulty** | 910  · R.D. Comprehension Level {"I":"1 — Trace","II":"2 — Basic",
"III":"3 — Advanced","IV":"4 — Deep","V":"5 — Sovereign"}.get("II", "2 — Basic") |
```

The difficulty word had been replaced by the entity's numeric suffix and the level lookup had
never run. All 29 were repaired from each dossier's own `Work difficulty` row and coherence key —
`| **Difficulty** | Moderate · R.D. Comprehension Level 2 — Basic |`. This is the clearest single
piece of evidence for the owner's point: in those files the table was not wrong about the entity,
it was *not about the entity at all*.
