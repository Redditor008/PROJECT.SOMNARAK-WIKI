# Work Preference — the whole palette, and what is in the archive today

**Measured 2026-11-03 over 296 graded dossiers** (301 on disk; 5 carry a mixed or prose-only table and are not graded). Read this with `WORK_RESPONSE_LAW.md`, which governs Subjects, and `R-40`, which governs relics.

## 1. The four cells

Every dossier with a response record answers in four cells, in this order, always:

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| **Flerehan** | **Pugnahan** | **Viderehan** | **Ferrehan** |

**The order is the notation.** A vector is never four anonymous numbers: position 1 *is* Flerehan, 2 *is* Pugnahan, 3 *is* Viderehan, 4 *is* Ferrehan, and each cell answers one question only — **what does that work type do to this holding**. Read `-100% : -100% : Neutral : Down` as *"Flerehan is barred and charged in full; Pugnahan is barred and charged in full; Viderehan holds the gauge; Ferrehan brings it down"*, never as a shape with four values. The order is fixed by the four work types themselves, so the same vector in two files says the same thing about the same four approaches, and a reader can compare two holdings cell for cell without opening either table.

Five values are allowed in a cell, and nothing else:

| cell | means |
|---|---|
| **Down** | the gauge falls — the holding is settled by this |
| **Up** | the gauge climbs — this feeds it |
| **Neutral** | the gauge holds — a real effect with no net movement |
| **Net-Neutral** | barred: the work is spent and **nothing is netted**. The threshold does not come down, the gauge does not move, and no benefit is paid for the watch |
| **Negative-Low** | barred and worse: **the attempt is charged in full** — the threshold goes to 0 and the gauge fills to 100%, so it activates on the work |

So a vector reads `Negative-Low : Negative-Low : Neutral : Down`, meaning: *Flerehan and Pugnahan — the two barred registers — are charged in full; Viderehan holds the gauge; Ferrehan brings it down.*

**The words are not decoration.** Batch 156 wrote the two barred cells as `0%` and `-100%`, and they read as statistics on a page that is not a statistics table — a Warden skims `-100%` as a modifier rather than as a verdict. **Net-Neutral** and **Negative-Low** are the same two mechanics under the names they should have had, and no dossier prints a percentage in a response cell (`R-41`).

**Each cell may also carry L Corp's grade**, after the state: `Down · High`, `Neutral · Common`, `Up · Low`. The full ladder is five grades — **`V.H` · `High` · `Common` · `Low` · `V.L`** — and the archive writes with the middle three today. The grade is the *yield* of that work, not a second statement of the state, which is why the two are allowed to disagree (`Neutral · High`: a reading that gives much and settles nothing; `Up · Low`: a work that hurts the worker and pays badly). The table on the page names the work type in each row already — `| **Flerehan** (Tears) | … | Down · High |` — so the vector and the table are the same four facts in two forms, and `tools/auditors/check_work_preference.py` reads both.

## 2. Why Net-Neutral instead of N/A, and what each one does

`N/A` said *not applicable*, which told a Warden nothing about what happens if somebody tries. The two replacements are both answers, they are different answers, and both are mechanical:

| cell | what the work does |
|---|---|
| **Net-Neutral** | **nothing.** The threshold does not come down, the gauge does not move, and no benefit is paid for the watch. |
| **Negative-Low** | **the opposite of work.** The threshold goes to 0 and the gauge fills to 100%: it activates on the work. |

That is the owner's reading exactly — *"won't lower the threshold and won't give benefit"* for the first, and *"literally just dropping the threshold to 0 and filling gauge to 100%"* for the second — and the names are the owner's too: *"You Don't Write 0% or -100% On Dossier It Look Bad Think It Like This Net-Neutral And Negative-Low."*

## 3. One number decides both barred cells — the Threat Score

**The Threat Score is the guide's 2–10**, from `PM_ABNORMALITY_TO_PS_SORROW_ENTITY_CONVERSION_GUIDE.md` §III: *Threat Score is Coherence rank + Potency rank (I/α = 1 … V/ω = 5)*, and the sum sets the L Corp level — **2–3 ZAYIN · 4–5 TETH · 6 HE · 7–8 WAW · 9–10 ALEPH**. Both halves are already filed on the page (`**Coherence**`, `**Potency**`), so the reading needs nothing that is not printed:

| Threat Score | L Corp level | barred cells | what it says |
|---|---|---|---|
| **2–3** | ZAYIN | **Net-Neutral** | the holding is small enough that the attempt simply fails |
| **4–5** | TETH | **Net-Neutral** | still an inconvenience: the work is spent and nothing is netted |
| **6** | HE | **Negative-Low** | the first tier that is a major problem — the attempt is collected in full |
| **7–8** | WAW | **Negative-Low** | heavy enough to charge the whole attempt |
| **9–10** | ALEPH | **Negative-Low** | the attempt is not an attempt |
| **cut** | | | **below 6 → Net-Neutral · 6 and above → Negative-Low** |

**Batch 157 read this off the `Sorrow Gauge [HP]` maximum instead** (under 500 → `0%`, 500+ → `-100%`), and the owner corrected the source: *"I Used It From Our Conversion Guide you know the 2–10 things."* The two readings agreed on **144 of 149** dossiers, because HE is also the first band whose gauge begins at 500. The five they disagreed on were re-read in batch 159 and the gauge was the wrong one each time — `N-Iα-905` Lacrima is `I + α = 2` (ZAYIN, 150–300 HP) and files 502.

**Where the dossiers sit on the scale today:** 2 → 44 · 3 → 6 · 4 → 64 · 5 → 19 · 6 → 73 · 7 → 15 · 8 → 70 · 9 → 7 · 10 → 3. **133 graded dossiers read Net-Neutral, 168 read Negative-Low.** The two cells are always equal because they come from one sum, and the file prints the sum beside the vector so a reader can check the arithmetic.

## 4. What variety exists in the archive today

**Measured after the words went in: 296 graded dossiers, 17 distinct vectors.**

### Subjects — 153 dossiers, 12 shapes

| vector | dossiers |
|---|---:|
| `Down : Up : Neutral : Down` | 112 |
| `Down : Neutral : Neutral : Down` | 17 |
| `Net-Neutral : Net-Neutral : Neutral : Down` | 7 |
| `Negative-Low : Negative-Low : Neutral : Down` | 4 |
| `Neutral : Neutral : Down : Down` | 2 |
| `Down : Up : Neutral : Neutral` | 2 |
| `Neutral : Up : Neutral : Up` | 2 |
| `Neutral : Up : Neutral : Down` | 2 |
| `Up : Up : Neutral : Down` | 2 |
| `Neutral : Neutral : Neutral : Down` | 1 |
| `Down : Down : Neutral : Down` | 1 |
| `Neutral : Up : Down : Down` | 1 |

### Relics — 143 dossiers, 7 shapes

| vector | dossiers |
|---|---:|
| `Net-Neutral : Net-Neutral : Neutral : Down` | 57 |
| `Negative-Low : Negative-Low : Neutral : Down` | 52 |
| `Negative-Low : Negative-Low : Down : Down` | 19 |
| `Net-Neutral : Net-Neutral : Down : Down` | 8 |
| `Negative-Low : Negative-Low : Up : Down` | 4 |
| `Negative-Low : Negative-Low : Neutral : Neutral` | 2 |
| `Net-Neutral : Net-Neutral : Up : Down` | 1 |

### The number that matters

**176 of 296 dossiers sit on two vectors** — `Down : Up : Neutral : Down` (112) and `Net-Neutral : Net-Neutral : Neutral : Down` (64). That is the crowding the owner keeps naming, and it has not moved: the first two cells of a subject follow the Element matrix, and the barred pair follows the Threat Score, so **only the cells the guide actually leaves free can vary**. The ratchet was re-taken at 176 in batch 159 because the Threat Score replaced the gauge reading and moved four dossiers; nothing was rewritten to make a shape look different.

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

Seven live pairs × two barred readings (**Net-Neutral** / **Negative-Low**) = **fourteen relic vectors**, plus four subject vectors. **Eighteen in the palette; seventeen in use, but five of them on the live pair.** The count is not the problem — the concentration is.

**The next conversion is `Down : Neutral` and `Down : Up`** — the two shapes for a holding whose pressure is in the witness rather than in the object. Every Void and Lament relic is a candidate, and each one has to be argued from its own record.

## 6. Where the variety comes from, and where it does not

The rules do not manufacture variety; they **forbid the copy**. A file still has to say what its own holding does — the sign is chosen from the record, and the record has to carry the mechanism (batch 154's five Weight conversions each got theirs: *reconciling three clocks is itself a shift nobody is on the timesheet for*).

What the rules do is stop the shortcut: a Lament Subject cannot be `Down : Up : Neutral : Down` any more, because the element says which register answers it. A relic cannot say `Neutral : Down` by reflex, because the pressure has to be located first.

## 7. How to write it on the page

**Subject** — the `## Behavior` table, four rows, sign in the last column.

**Relic** — no table. The vector goes on one row of the core stat line:

```
| **Work preference** | `Negative-Low : Negative-Low : Neutral : Down` — four cells in file order
(Flerehan : Pugnahan : Viderehan : Ferrehan). The barred pair is read off one number, the threat
point 500/500: nothing is returned and the attempt is charged in full. Reading the beat holds the
gauge; the shift with empty hands brings it down. |
```

`tools/auditors/check_work_preference.py` (gate line 81) enforces the alphabet, the barred-pair equality, and the threat-point rule wherever a dossier prints both; `--variety` prints the live distribution.


---

## 8. The L Corp benchmark, and why their variety is bigger

Researched 2026-11-03 against Cogitopedia's abnormality pages. L Corp's containment loop has four work types — **Instinct, Insight, Attachment, Repression** — and every abnormality carries a preference table over them.

**Their ladder is four tiers with a percentage attached:**

| tier | value |
|---|---|
| **High** | 60% |
| **Common** | 40–55% |
| **Low** | 20–35% |
| **Very Low** | **0%** — and, on some abnormalities, **−80%** |

*(Bloodbath T-05-51: Instinct Common 50–55, Insight Common 40–45, Attachment High 60, Repression Very Low 0. Porccubus: High/Common/Common/Low. Forsaken Murderer T-01-54: Repression Very Low **−80%** at levels IV–V. Knight of Despair: Instinct Very Low 0 across all five levels. Fragment of the Universe: Instinct Low, Insight Low, Attachment High, Repression Common.)*

**Four work types × four tiers = 4⁴ = 256 possible profiles**, and the game's own list ranges across them: a `High/Common/Common/Low` here, a `Low/Common/High/Common` there, a `Very Low/Common/Common/Common` on another. The tiers also **move with the employee's stat level** (I–V), so the same abnormality reads differently at Attachment level 2 and level 5.

**Two things about their table matter more than the arithmetic.**

1. **The tier is a yield, not a state.** A preference says how much the work *gives back* — success rate, E-boxes. It says nothing about what the holding does to the worker; the counter behaviour is written separately, in the managerial guidelines.
2. **The negative is real.** `−80%` is not "no effect" — it is worse than not working. That is precisely the owner's **Negative-Low**, arrived at independently.

**Ours conflated the two.** One number — the gauge sign — carried *both* what the work yields and what the holding does, so a file could not say *"this is the best work and it costs me"* or *"this is the safest and it gives almost nothing"*. That is why five live pairs hold 86% of the archive: the two axes were forced to move together.

## 9. The fix: two judgements per cell

A cell now reads **`state · preference`**:

```
| **Viderehan** | Sets the whole arrangement out — terms, dates, amounts — accurately. | Neutral · High |
```

- **state** — what the holding does: `Down`, `Up`, `Neutral`, or the barred **Net-Neutral** / **Negative-Low**.
- **preference** — what the work gives back: `High`, `Common`, `Low`. Barred cells carry no preference, because nothing is given back.

**Two rules, so the axis cannot collapse again:**

1. **At most one `High` per dossier.** A holding answers to one register best; where the file shows two, the stronger is High and the other is Common.
2. **Preference does not have to follow the state.** `Neutral · High` is a good reading that settles nothing. `Up · Low` is a work that is bad for the worker *and* yields little. `Down · Common` settles the gauge while giving a thin yield. These were unsayable before.

**Four states × three tiers per cell**, four cells, so the space is large; the useful count is how many *distinct* shapes the archive actually writes. **5 of 296 dossiers carry a tier so far** — the first five are `C-IIIγ-021`, `032`, `033`, `062`, `081`, chosen for the spread they give:

| dossier | element | vector |
|---|---|---|
| Hollow Choir `C-IIIγ-021` | Lament | `Down·High : Up·Low : Neutral·Common : Down·Common` |
| Weighting Bird `C-IIIγ-032` | Grudge | `Down·High : Up·Low : Neutral·Common : Down·Common` |
| Guarding Bird `C-IIIγ-033` | Void | `Down·High : Up·Low : Neutral·Common : Down·Low` |
| The Inheritor `C-IIIγ-062` | Grudge | `Down·Common : Up·Low : Neutral·High : Down·Common` |
| The Hollow Saint `C-IIIγ-081` | Void | `Down·Common : Up·Low : Neutral·High : Down·Common` |

Note the last two: **the High cell is Viderehan, not the element's own work** — the Inheritor's gift is that it sets out the whole arrangement accurately, and the Hollow Saint's is that it lets you see in. The element says what the holding *is*; the preference says where it *pays*, and those are allowed to differ. That is the whole of L Corp's variety, and it is the axis this archive never had.

**Next:** the remaining 291 dossiers get their four tiers from their own prose, one file at a time. `check_work_preference.py --variety` prints the tally; `carrying a preference tier: N of 296` is the line to watch.
