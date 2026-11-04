# R-44 — The Cost of the Session

**Stated by the archive owner, 2026-11-04:** *"The meaning of consequence to all SE is: there will be
a cost on working on them, and what the cost is based on what they are and what they do. Try to
research L Corp stuff — work damage, work interaction, and much more."*

## 1. What L Corp actually files, and what this archive was missing

A Lobotomy Corporation Abnormality page carries, in its basic information, four things that decide
what a work session costs:

| L Corp field | what it is | does this archive have it? |
|---|---|---|
| **Work Damage** | a damage **type** (Red / White / Black / Pale) and an **amount** (`1-3`, `6-8`, `5-10`) taken by the employee *while working* | **no — 0 of 301 dossiers carry it** |
| **Work Preferences** | the four works ranked best to worst — Instinct, Insight, Attachment, Repression | yes — Flerehan / Pugnahan / Viderehan / Ferrehan, matrix-bound by `R-41` |
| **Maximum E-Boxes** and outcome ranges | Good / Normal / Bad thresholds | yes — Han-Energy yield, and the barred cells |
| **Qliphoth Counter** | the number the work can move, and what happens at zero | yes — the **T Counter**, read against the Threshold |
| *work cooldown, work speed* | pacing | partly — `Work difficulty`, R.D. level |

**The missing one is the one the owner named.** The archive could say which work a holding answers
to, and how much energy the session produced, and it could not say what the session **cost the
person doing it**. That is why every holding felt the same to work: the only thing a session ever
produced was a number going up.

## 2. The field

```
| **Work Damage** | 6–9 Grudge — the cost is carried weight: the session is walked, not stood |
```

Three parts, in this order:

1. **An amount**, inside the band for the entity's tier (§3).
2. **A type**, which is the entity's own `Element` row. L Corp has four damage types; this archive
   has four sorrows, and they are the same four. A holding whose element is `All four` cycles
   through them and says so.
3. **A clause saying where the cost comes from** — one sentence, in the entity's own terms, naming
   the mechanism. *Not* a restatement of the element. The Maw's cost is being named by the
   thousand; the Final Door's is hearing the whisper and speaking first; the Ancestral Guilt's is
   genealogical and comes out of the vault with the keeper.

The row sits in the statistics table, directly under `Work difficulty`.

## 2.1 The preference tier — how well it answers to each work

L Corp does not stop at ranking the four works. Each work carries a **level** — the holding
answers to Instinct *very high* and to Repression *low*, and a manager plans a session off that
level and not off the raw listing. The archive had the four works and no levels, so
*"ranked best to worst"* was a claim the page never actually made.

The level is written as a third element on the cell, after the gauge word:

```
| **Flerehan** | …prose… | Decrease · High |
```

| level | what it means | when it is the right reading |
|---|---|---|
| `V.H` | the work the holding was built around | rare; the file says the holding exists to be met this way |
| `High` | the work that matters most | the cell moves the gauge furthest, or the file calls it the primary Work Type |
| `Common` | a work that holds | the gauge is stable, or the work is routine and unremarkable |
| `Low` | a work that costs | the cell raises the gauge, or the work is prohibited and charged |
| `V.L` | a work that cannot be done | refused outright; use the barred word instead where the cell is barred |

**Three standings, and no more:**

1. **At most one `High`.** A holding answers to one register best. Two Highs is a page that has
   not decided what the entity is.
2. **A barred cell carries no level.** `Negative-Low` and `Net-Neutral` already say the attempt
   does not happen; a level on top of that is a second verdict about a non-event.
3. **Every open cell carries a level.** A table with three levels and one blank has not been
   finished.

**Where the level comes from.** It is read off the cell the dossier already wrote, in this order:
a `Decrease` cell that names itself primary is `High`; failing that the first `Decrease` is
`High`; a `Stable` cell is `Common`; an `Increase` cell is `Low`; remaining `Decrease` cells are
`Common`. Nothing is added to the prose to justify a level — the level is a reading of the
sentence that is already there, and a dossier whose prose contradicts its level is the dossier
that gets rewritten, not the level.

**Measured, batch 191:** 5 of 294 dossiers carried a level. The requirement was also
unsatisfiable as written — the auditor demanded four levels and forbade a level on a barred cell,
which most dossiers have. Both are fixed; the count below is the rollout.

## 3. The bands

Read off the same scale as `R-42`, and deliberately the same shape as L Corp's own spread — a TETH
object that costs `1-3` and an ALEPH that costs `5-10`:

| band | Work Damage |
|---|---|
| **Low** (ZAYIN) | 1–3 |
| **Medium** (TETH) | 1–4 |
| **Common** (HE) | 2–6 |
| **Top** (WAW) | 3–8 |
| **High** (ALEPH) | 5–10 |

**A Special Abnormality has none.** `R-35` says a terminus is never worked; there is no session to
cost, and a `Work Damage` row on one would be the same defect as a work table on one. Their yield
row already opens with `—`.

## 4. What is enforced now, and what is measured

`tools/auditors/check_work_damage.py` (gate 87):

- **fails** any holding whose `Work Damage` amount falls outside its band, or whose type does not
  match its own `Element` row;
- **fails** any holding that carries no work loop (yield opens `—`) and a `Work Damage` row anyway,
  which is how a terminus or a relic gets caught;
- **fails** a High holding that carries a work loop and no `Work Damage` row at all;
- **reports** every lower band that has not been rolled out yet, counted per band.

## 5. Why the rollout is staged

The row has to be written from what each holding is, which is 301 separate readings. This batch
does the **High** band completely — the seven worked ALEPH holdings — and establishes the rule and
the gate. The 288 below it are counted in the gate's report so the remainder is a number, not an
intention.
