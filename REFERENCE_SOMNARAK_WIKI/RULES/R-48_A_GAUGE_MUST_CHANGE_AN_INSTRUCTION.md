# R-48 — The Charge

**Stated by the archive owner, 2026-11-04 → 11-05:**

> *"...TRANSFORMS THE HP NUMBER INTO A MEANINGFUL GAUGE SO WHAT GOOD USED THE GAUGE THAT IS NOT USED
> FOR SE HP SO THINK OF THAT"*

> *"...IT STILL READ ILLOGICAL ... AND FEEL BLOATED ... TRY TO REINVENT IT INTO A MORE LOGICAL
> MECHANIC"*

> *"WHAT IF YOU DIVIDED EXPLANATION AND THE TABLE IN TWO ... EACH TIER OF THE SE HAVE BRAND NEW
> INVENTED GAUGE NUMBER ... WHAT IF THIS GAUGE IS PUNISHMENT + LIMIT OF USING IT ... LIKE HOW IN L
> CORP THERE IS A LIMIT OF HOW LONG AN AGENT CAN USED/HOLD/EQUIP IT ... THERE SHOULD BE HARD LIMIT
> THAT IS UNIVERSAL FOR ALL RELIC SE ... A CONSEQUENCE OF TRYING TO USED IT WHEN IT NOT YET
> 'RECHARGE' AND THE RECHARGE RATE CAN WORK LIKE ... THERE IS A LINE FROM MAX TO 00"*

This is the fourth draft. The first three are superseded in full, and §0 says why.

## 0. Why the third draft was still wrong

Draft 3 displayed the gauge as **charge remaining**, full at rest, and draining to 000 as it was
used. Every consequence of that ran *backwards* against a rule this archive had already written
down:

> **`R-09`:** *"The Sorrow Gauge runs opposite to the Qliphoth Counter: a Flerehan `Decrease` is a
> good result. This is intentional and must not be 'corrected' toward the source."*

**278 relic dossiers** file work responses as `Flerehan | Decrease` and `Pugnahan | Increase`. Under
draft 3 a `Decrease` would have been the *bad* outcome — the gauge draining toward zero is a relic
being used up. The work-response tables, the 36 `Resolution Condition` rows that end a session when
*"the gauge falls below 25%"*, and **155 authored sentences** — *"a rising gauge presents as
volume"*, *"the gauge climbs with the drain"* — all say the same thing: **the gauge rises when
things are going wrong.** Draft 3 made them all liars.

**The archive was right and the draft was wrong.** A gauge that fills is a gauge that can be read as
punishment; a gauge that empties reads as a battery. The owner asked for punishment and limit. This
version is that.

## 1. What the charge is

**The gauge is the load the relic is carrying, and it is both the punishment and the limit.**

- **The punishment** — every second of contact puts load on. The number is what the thing has taken,
  and when it is high, the next hand pays more.
- **The limit** — at **MAX** the relic is **spent**. It will not take a hand at all.

A relic at rest is at **000**: nothing being held, nothing spent. That is why a vault reading is
always low and why the old pinned-at-maximum HP readings were meaningless — a number that never
moved told nobody anything.

**000 is the safe reading. MAX is the wall.** That is the whole orientation, and it is the one the
archive's own prose and `R-09` already assume.

## 2. The number belongs to the tier

No writer picks a relic's ceiling. It comes from the tier and from nothing else:

| tier | the wall | |
|---|---|---|
| **ZAYIN** | **240** | the least a relic can hold and still be one |
| **TETH** | **420** | |
| **HE** | **660** | |
| **WAW** | **880** | |
| **ALEPH** | **1,080** | the most this archive has ever measured |

Every figure sits inside the band `check_stat_bands.py` already enforces. **A reader who knows the
tier knows where the wall is before opening the file**, which is what a tier is for.

## 3. The hard limit is universal: sixty seconds

**No relic may be held for longer than sixty seconds of contact. Any relic. Any tier.**

This is L Corp's work timer: the one figure that is not tiered, not categorised, not negotiable.

**The gauge fills its whole length in that minute** — 000 to MAX, whatever MAX is. So a larger
ceiling is a **heavier load held for the same minute**, not a longer leash. An ALEPH does not give
you more time than a ZAYIN; it takes 4.5× more from you in the same sixty seconds.

At **MAX** the relic is spent: not damaged, not suppressed, not dead. Spent. It will not take a
hand.

## 4. The two lines

**Up — the fill.** The whole of it, in sixty seconds, on every relic:

```markdown
000 ─────────── 60 s ─────────── 660
```

**Down — the recharge.** It runs back the same line, **a tenth of itself a minute**, so ten minutes
from spent back to ready at every tier:

```markdown
660 ── 1 min ── 594 ── 2 min ── 528 ── 3 min ── 462 ── ... ── 10 min ── 000
```

**Read it as one line that goes both ways.** The owner asked for "a line from MAX to 00"; this is
that line, and the fill is the same line travelled in the other direction.

## 5. The consequence of using it before it has recharged

Two sizes of mistake.

**Taken up before it has run down** — you do not get a fresh minute. It starts from where it stands,
so you inherit the remaining headroom and **the Work Damage clock resumes where it stopped** instead
of starting over. `R-47` says the clock resets to base the moment contact breaks; that reset is
**conditional on a settled gauge**, and this is the clause that makes it so.

**Taken up at MAX** — it refuses. The attempt is answered the way a suppression would answer it:
**the first dose of Work Damage lands immediately, in full**, and **the recharge restarts from the
top** — every minute of run-down so far is thrown away. This is the punishment for impatience, and
it is the only one in the archive that punishes impatience rather than curiosity.

## 6. Three places, and what each one is for

Draft 3 put the mechanic in the table cell. Draft 4 moved it to a paragraph. **Both were wrong for
the same reason: neither told the reader the gauge's length.** A cell reading `000/420` does not say
whether 420 is the ceiling, the reading, or a pair of unrelated numbers, and a paragraph about a
clock says nothing about how long the line is.

So the mechanic gets **three places**, and each one answers a different question:

| place | answers | size |
|---|---|---|
| **the cell** | *what is it right now, and how long is the line* | one line, under 110 characters |
| **`## The Charge`** | *how does it work, and what happens if I get it wrong* | a standing section, same in every relic |
| **the Work Damage row** | *what does it cost per second* | unchanged from `R-47` |

### The cell

```markdown
| **Sorrow Gauge [Depth]** | **000 of 660** · ready · limit 60 s · recharge 10 min |
```

`000 of 660` — the reading **of** the length, said in words, because a slash reads as a fraction and
a fraction of what is never answered. `ready` is the settled state, `limit 60 s` is the wall, and
`recharge 10 min` is the run-down. Everything a Warden needs at the door is in that line.

### `## The Charge` — the standing section

A relic dossier carries a `## The Charge` section immediately before its Contact or Combat Record.
It is the same section in every relic, with four figures substituted, and it answers the three
questions a reader actually has: **how long is it, how fast does it move, and what happens at the
wall.**

```markdown
## The Charge

The gauge is the load this holding carries, not a reserve it spends. It is read at the instrument
and nowhere else, and every figure below is fixed by the tier — none of it is chosen for this file.

| Field | Value |
|---|---|
| **Length** | **660** — the whole of it. The length is fixed by the grade this file carries, and is not chosen here |
| **At rest** | **000**. Nothing is being held, so nothing has been laid on |
| **Fill** | 000 to 660 across sixty seconds of continuous contact |
| **Wall** | at 660 it is spent and will not take a hand. The refusal is not an injury |
| **Run-down** | a tenth of the length a minute, so ten minutes from spent back to ready |
| **Taken early** | the Work Damage clock resumes where it stopped rather than starting over |
| **At the wall** | the first dose lands at once and the run-down starts again from the top |
| **What it takes** | grief taken down into the person. Nothing breaks; the level sits lower after |

Sixty seconds is the wall on every relic in the archive, at every tier. A longer line is not a
longer leash: the same minute is spent here as everywhere else, and the longer the line, the more
that minute takes out of the handler — and the sooner the wall is reached.

The gauge is read at the instrument. The cost is read on the person.
```

**No tier is ever named inside a dossier.** The length row says *"fixed by the grade this file
carries"* and gives the figure; the grade names themselves live in the guides, which is the
archive's existing convention and the reason `compare_conversion_guide.py` exists.

**`What it takes` is the only row that changes between files**, and it is the one that carries the
Element: force through the arm on a Grudge, mass on the frame on a Weight, grief taken down on a
Lament, absence poured in on a Void. That is the part of this mechanic the owner kept asking for —
**the SE type is how the gauge reaches the agent** — and it is a row here rather than a sentence in
a cell.

### Why the section and not the paragraph

A paragraph stated the clock once and assumed the reader would infer the length. A section states
the length, the fill, the wall, the run-down, both failure modes and the Element in eight short
rows and three sentences — **and it is the same section every time**, so a reader who has read one
relic can read any other in the archive without re-learning the mechanic.

**A cell that has to be read twice is a paragraph in the wrong place; a mechanic that has to be
inferred is a section that was never written.**

## 7. What the measure is called

The gauge is named for what the holding puts into the handler — the dossier's own `**Element**`:

| Element | gauge | what the hands are taking |
|---|---|---|
| **Grudge** | `[Pressure]` | force pushed back through the arm that holds it |
| **Weight** | `[Load]` | mass carried on the frame of the carrier |
| **Lament** | `[Depth]` | grief taken down into the person — a level, not a volume |
| **Void** | `[Saturation]` | absence poured in until there is no room for anything else |

## 8. What rises and what falls — the reading every writer already uses

Because the gauge fills, **the archive's existing language is already correct** and must not be
"fixed" toward the draft-3 orientation:

| already written | still true |
|---|---|
| `Flerehan · Decrease` | a decrease is a good result (`R-09`) |
| *"a rising gauge presents as volume / speed / argument"* | a rising gauge is a worsening relic |
| *"the gauge falls below 25%"* as a Resolution Condition | the session closes when the load comes off |
| `Starting Sorrow Gauge` | **000** — settled. A relic nobody is holding reads at the bottom |

## 9. The nine that keep `[HP]`

- **Possession — 2**, by the owner's word: the bearer is what falls.
- **Breaching relics — 7**: a relic that can breach is suppressible.
- **Subjects** — unchanged; their cost is a work session, already `R-44`.

Their meter runs to 000 by suppression rather than by the minute, and §3's law binds them harder,
not less: **nothing may be used at 000.**

## 10. The gate

`tools/auditors/check_relic_gauge.py` (gate 93) fails a non-breaching, non-possession relic when:

- the label is `[HP]`, is not one of the four measures, or disagrees with the `Element` row;
- the ceiling is not the figure its **tier** dictates;
- the reading is not a settled **000/MAX**;
- the cell does not carry `ready`, `limit 60 s` and `recharge 10 min`;
- the cell runs past **110 characters**;
- `Starting Sorrow Gauge` is not **000** — the percentage band is retired;
- there is no `## The Charge` section, or it fails to state the tier wall, the resting 000, the
  sixty-second fill, the tenth-a-minute run-down, the Work Damage chain, or what it takes out of
  the handler;
- a `**Charge.**` paragraph is still lying in the table area — the section replaced it;
- a possession, breaching relic or subject has lost its `[HP]`.

## Rollout

| | before | after |
|---|---|---|
| reading at rest | 141 relics pinned at their own ceiling | **000 of the tier's wall** |
| ceilings | 134 arbitrary, 198–993 | **5 tier figures** |
| cell | 300–500 characters of prose | **under 110, data only** |
| explanation | inside the cell | **a paragraph under the table** |
| `Starting Sorrow Gauge` | a 35–50% band on 286 rows | **000, settled** |
| orientation | draft 3 inverted `R-09` | **decrease is a good result again** |

## Owner direction

Batch 197, 2026-11-05. Filed as **O-34** in `OWNER_DIRECTIVES.md`. Drafts 1–3 are superseded.
