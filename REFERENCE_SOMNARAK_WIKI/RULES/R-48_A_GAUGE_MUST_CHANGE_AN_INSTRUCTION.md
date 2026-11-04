# R-48 — The Gauge Is What Is Left In The Hands

**Stated by the archive owner, 2026-11-04:**

> *"WHAT THE USED OF HP ON RELIC SE THAT WONT USED THE HP, YES POSSESSION CAN USED THE HP SO
> FOR RELIC SE THAT WILL NEVER BREACH FIRST ERASE THE [HP] AND TRANSFORMS THE HP NUMBER INTO A
> MEANINGFUL GAUGE SO WHAT GOOD USED THE GAUGE THAT IS NOT USED FOR SE HP SO THINK OF THAT"*

and then, on the first attempt:

> *"IT STILL READ ILLOGICAL AS IN WHEN I TRY TO READ IT IT DOESNT MAKE SENSE AND FEEL BLOATED,
> ALSO TRY TO RETHINK IT AGAIN I LIKE HOW THE SE TYPE IS HOW THE GAUGE AFFECT THE AGENT TRY TO
> REINVENT IT INTO A MORE LOGICAL MECHANIC"*

The first attempt was wrong and this rule replaces it. What was wrong is recorded in §1, because
the mistake is instructive.

## 1. Why the first attempt failed

The first version wrote three bands under a number that **nothing in the file ever moved.** Every
reading in the archive sat at its own ceiling — `506/506`, `653/653`, `420/420` — and then the
row said *"under 170 …"*, *"from 340 …"*. Three thresholds below a figure that never comes down
are not bands. They are decoration, and the reader feels it immediately even without knowing why.

Worse, the row explained itself: *"the tree spends nothing of what it fills with"*, *"the figure
has not moved since the record began"*. **Nineteen dossiers had written an apology for a dead
field**, and an apology in a stat cell is the clearest sign the stat is wrong.

The lesson: **a gauge needs a thing that spends it.** No spender, no gauge.

## 2. The mechanic

A relic is not suppressed, so it has no health. But it is **handled**, and handling costs the
handler. That cost already exists in every dossier — it is the `**Work Damage**` row, a dose per
second that accelerates with contact time (`R-47`).

So the gauge is not the relic's health. It is **what is left in the hands that hold it.**

```text
Work Damage   = the rate the hands are being spent, per second
Sorrow Gauge  = how much of the handler is left to spend
```

One is a rate, one is a reserve. Neither is a repeat of the other, and neither can work alone:
the rate with no reserve lets an operator hold a thing for nine seconds, set it down, and start
over, forever. **The reserve is what closes that hole.** The clock in `R-47` returns to base when
contact breaks — the reserve does not return with it.

### The reading is full because nothing has spent it yet

Every relic reads at its ceiling. That is not a broken meter; **that is the meter at rest**, and
the row says so in two words. The number falls only in the hands, and the dossier records the
vault reading.

### At zero, the hands stop — not the relic

Nothing dies. The relic is intact, the vault is intact. What ends is the ability to pick the thing
up: not that day, and not by the same hands at all.

## 3. The measure: named for what the hands are taking

The gauge is named for **what the holding puts into the handler**, which is the dossier's own
`**Element**`:

| Element | gauge | what the hands are taking |
|---|---|---|
| **Grudge** | `[Pressure]` | force pushed back through the arm that holds it |
| **Weight** | `[Load]` | mass carried on the frame of the carrier |
| **Lament** | `[Depth]` | grief taken down into the person, a level rather than a volume |
| **Void** | `[Saturation]` | absence poured in until there is no room left for anything else |

This is the owner's liked part, kept: **the type decides how the gauge reaches the agent.** A
`[Load]` gauge breaks a carrier's back; a `[Depth]` gauge does not break anything, it just goes
down and stays down. Four elements, four different harms, one mechanism.

## 4. The row

```text
| **Sorrow Gauge [Saturation]** | 506/506 at rest — what one holder can carry out of it.
The Work Damage above is what spends it. Under 340 the keeper is relieved and read before going
back. Under 170 nobody handles it again until that keeper has been cleared. At 0 it is not handled
again that day, and not by the same hands at all. Comes back half when an offering is taken back;
the rest stays given. |
```

Six sentences. Each does one job, and no two do the same job:

| # | what it says |
|---|---|
| 1 | **the reading, and that it is the resting reading** — `N/N at rest`, what one holder can carry |
| 2 | **what spends it** — a pointer to the Work Damage row, not a copy of it |
| 3 | **band one** — at two thirds, rotation: relieved and read before going back |
| 4 | **band two** — at one third, supervision: nobody takes it over until the keeper is cleared |
| 5 | **band three** — at zero, prohibition: not that day, not the same hands |
| 6 | **recovery** — half, on a category condition, and the rest is gone |

**Thresholds descend**, because a reserve is spent downward. This was the other thing the first
attempt got backwards: it wrote ascending thresholds on a value that only ever fell.

## 5. Recovery is the category's condition, and it is only half

A reserve that refills completely is not a reserve. Recovery returns **half**, once, and the
condition that returns it is set by the holding's own category — which is where the SE type
reaches the agent a second time:

| category | comes back half when |
|---|---|
| **Indumentum** (worn) | the piece is off, and what the skin kept stays kept |
| **Officium** (rite) | the rite is closed and signed, and the rest stays with the ground |
| **Arcanum** (reading) | the reading is written and filed, and what was answered is not un-answered |
| **Offertorium** (votive) | an offering is taken back, and the rest stays given |
| **Object / Place** | the boundary is re-probed, and the rest stays with the ground |
| **Time** | the operator is outside the interval, and time spent inside does not come back |
| **Hazard** | the crew is rotated out, and the air taken is not given back |

**What is not recovered is the mechanic.** A rock that costs you a third of your hands does not
give the third back because you went to lunch.

## 6. What keeps `[HP]`

- **Possession — 2 dossiers**, by the owner's word. *"YES POSSESSION CAN USED THE HP."* The bearer
  is what falls, and there is a zero to reach.
- **Breaching relics — 7 dossiers.** A relic that can breach is suppressible, and suppression is
  what HP is for.
- **Subjects** — unchanged; their cost is a work session, already `R-44`.

Those nine still spend a holder's reserve through `R-47`; they simply do not get a second cell for
it. The reserve is stated once, in the Work Damage row's reset clause, and that is enough.

## 7. What this does not do

- It does not change a single ceiling. `506/506` keeps its 506 — only what the number means, and
  what moves it, changes.
- It does not touch `R-47`. The rate rule stands; this rule supplies the reserve the rate drains.
- It does not put worldbuilding in a stat cell. If a clause described how poetic the number was,
  it is gone. Prose belongs in Appearance, where there is room for it.

## 8. The gate

`tools/auditors/check_relic_gauge.py` (gate 93) fails a non-breaching, non-possession relic when:

- the label is `[HP]`, or is not one of the four measures;
- the label disagrees with the `Element` row;
- the reading is not `N/N` — a dossier records the **resting** reading;
- the phrase `at rest` is missing;
- the row does not point at `Work Damage` as the spender;
- there are not **three descending thresholds**, the last being `0`;
- there is no recovery clause, or it is not the clause its own category requires.

## Rollout

| | on `[HP]` | on a reserve gauge |
|---|---|---|
| before the rule | 141 | 0 |
| after | **9** (2 possession + 7 breaching) | **134** |

By measure: **Depth 43 · Saturation 33 · Pressure 32 · Load 26.**

## Owner direction

Batch 194, 2026-11-04. Filed as **O-34** in `OWNER_DIRECTIVES.md`. This is the second draft; the
first is superseded in full.
