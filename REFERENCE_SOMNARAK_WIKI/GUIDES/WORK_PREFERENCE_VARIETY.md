# Work Preference — the whole palette, and what is in the archive today

**Measured 2026-11-03 over 296 graded dossiers** (301 on disk; 5 carry a mixed or prose-only table and are not graded). Read this with `WORK_RESPONSE_LAW.md`, which governs Subjects, and `R-40`, which governs relics.

## 1. The four cells

Every dossier with a response record answers in four cells, in this order:

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| **Flerehan** | **Pugnahan** | **Viderehan** | **Ferrehan** |

Four words are allowed in a cell, and nothing else:

| cell | means |
|---|---|
| **Down** | the gauge falls — the holding is settled by this |
| **Up** | the gauge climbs — this feeds it |
| **Neutral** | the gauge holds — a real effect with no net movement |
| **0%** | barred: the holding **gives nothing back**. Nothing is returned and the watch is spent for no reading |
| **-100%** | barred and worse: **the attempt is charged in full** — nothing returned, the whole pressure onto the worker |

So a vector reads `-100% : -100% : Neutral : Down`, meaning: *the two barred registers return nothing and cost everything; reading it holds the gauge; handling it brings the gauge down.*

## 2. Why 0% instead of N/A

`N/A` said *not applicable*, which told a Warden nothing about what happens if somebody tries. `0%` and `-100%` are both answers, and they are different answers. A wall that returns nothing is not the same holding as one that takes the whole of what is offered to it.

## 3. One number decides both barred cells — the threat point

**The threat point is the `Sorrow Gauge [HP]` maximum.** One reading sets both barred cells, which is why the rule can be applied without checking the two work types separately:

| threat point | barred cells | what it says |
|---|---|---|
| **under 500** | `0%` | the holding is small enough that the attempt simply fails |
| **500 or more** | `-100%` | the holding is large enough that the attempt is collected in full |

501 is not a coincidence: the corpus's own ladder puts 500 at the floor of the Major (γ) band — Minor medians at 198, Moderate at 415, Major at 653 — so 500 is where a holding stops being a modest one. **61 graded cells read `0%`, 82 read `-100%`** under this cut. The two cells are always equal because they come from one number; the file prints the threat point beside the vector so a reader can check the arithmetic.

## 4. What variety exists in the archive today

**Measured after the percentage alphabet went in: 296 graded dossiers, 17 distinct vectors.**

### Subjects — 153 dossiers, 12 shapes

| vector | dossiers |
|---|---:|
| `Down : Up : Neutral : Down` | 112 |
| `Down : Neutral : Neutral : Down` | 17 |
| `0% : 0% : Neutral : Down` | 7 |
| `-100% : -100% : Neutral : Down` | 4 |
| `Neutral : Neutral : Down : Down` | 2 |
| `Down : Up : Neutral : Neutral` | 2 |
| `Neutral : Up : Neutral : Up` | 2 |
| `Neutral : Up : Neutral : Down` | 2 |
| `Up : Up : Neutral : Down` | 2 |
| `Neutral : Neutral : Neutral : Down` · `Down : Down : Neutral : Down` · `Neutral : Up : Down : Down` | 1 each |

### Relics — 143 dossiers, 7 shapes

| vector | dossiers |
|---|---:|
| `-100% : -100% : Neutral : Down` | 56 |
| `0% : 0% : Neutral : Down` | 53 |
| `-100% : -100% : Down : Down` | 20 |
| `0% : 0% : Down : Down` | 7 |
| `-100% : -100% : Up : Down` | 4 |
| `-100% : -100% : Neutral : Neutral` | 2 |
| `0% : 0% : Up : Down` | 1 |

### The number that matters

Look past the first two cells, because they now split on the threat point and so double the apparent count:

| live pair | dossiers |
|---|---:|
| `Neutral : Down` | **255 of 296 — 86%** |
| `Down : Down` | 30 |
| `Up : Down` | 5 |
| `Neutral : Neutral` | 4 |
| `Neutral : Up` | 2 |

**Five live pairs, one of them holding 86%.** `Down : Neutral`, `Up : Neutral` and `Down : Up` do not exist anywhere in the archive. That is the variety complaint, measured to the cell.

## 5. The palette the rules allow

### Subjects — four shapes, one per element (`WORK_RESPONSE_LAW.md`)

| Element | vector | the one work that settles it |
|---|---|---|
| Lament | `Down : Up : Neutral : Neutral` | Flerehan |
| Grudge | `Up : Down : Neutral : Neutral` | Pugnahan |
| Void | `Neutral : Neutral : Down : Up` | Viderehan |
| Weight | `Neutral : Neutral : Up : Down` | Ferrehan |

### Relics — seven live shapes, and the pressure decides

A relic is not worked (`R-40`), so its two live cells are not work types. They are the only two things that can be done to an object: **read it** (Viderehan) and **handle it** (Ferrehan). Where the holding's pressure sits decides which of the two is load-bearing:

| where the pressure sits | what reading does | what handling does | live pair |
|---|---|---|---|
| **in the object** — Weight, Grudge | nothing, reading is safe | contact | `Neutral:Down` · `Neutral:Up` · `Up:Down` |
| **in the witness** — Void, Lament | the reading is the cost | moving a box | `Down:Neutral` · `Up:Neutral` · `Down:Up` |
| **no gauge governs it** — Special Activation | nothing | nothing | `Neutral : Neutral` |

Seven live pairs × two barred readings (`0%` / `-100%`) = **fourteen relic vectors**, plus four subject vectors. **Eighteen in the palette; seventeen in use, but five of them on the live pair.** The count is not the problem — the concentration is.

**The next conversion is `Down : Neutral` and `Down : Up`** — the two shapes for a holding whose pressure is in the witness rather than in the object. Every Void and Lament relic is a candidate, and each one has to be argued from its own record.

## 6. Where the variety comes from, and where it does not

The rules do not manufacture variety; they **forbid the copy**. A file still has to say what its own holding does — the sign is chosen from the record, and the record has to carry the mechanism (batch 154's five Weight conversions each got theirs: *reconciling three clocks is itself a shift nobody is on the timesheet for*).

What the rules do is stop the shortcut: a Lament Subject cannot be `Down : Up : Neutral : Down` any more, because the element says which register answers it. A relic cannot say `Neutral : Down` by reflex, because the pressure has to be located first.

## 7. How to write it on the page

**Subject** — the `## Behavior` table, four rows, sign in the last column.

**Relic** — no table. The vector goes on one row of the core stat line:

```
| **Work preference** | `-100% : -100% : Neutral : Down` — four cells in file order
(Flerehan : Pugnahan : Viderehan : Ferrehan). The barred pair is read off one number, the threat
point 500/500: nothing is returned and the attempt is charged in full. Reading the beat holds the
gauge; the shift with empty hands brings it down. |
```

`tools/auditors/check_work_preference.py` (gate line 81) enforces the alphabet, the barred-pair equality, and the threat-point rule wherever a dossier prints both; `--variety` prints the live distribution.
