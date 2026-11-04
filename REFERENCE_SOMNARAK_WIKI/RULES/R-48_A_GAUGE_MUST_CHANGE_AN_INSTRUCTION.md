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

```text
000 ─────────── 60 s ─────────── 660
```

**Down — the recharge.** It runs back the same line, **a tenth of itself a minute**, so ten minutes
from spent back to ready at every tier:

```text
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

## 6. The division: table and explanation

**The table cell is data and nothing else:**

```text
| **Sorrow Gauge [Depth]** | **000/660** · ready · limit 60 s · recharge 10 min |
```

Four readings, no sentences: the reading and its ceiling, the state, the wall, the recharge time.

**The mechanic is a paragraph outside the table**, led in bold so the eye finds it:

> **Charge.** At the rite, the gauge fills the whole of its length in sixty seconds — 000 up to 660
> — and at 660 it is spent and will not take the hand. Left alone it runs back down a tenth a
> minute, so ten minutes from spent to ready. Handled again before it has run down, the Work Damage
> clock resumes where it stopped rather than starting over; handled at 660, the first dose lands at
> once and the run-down begins again from the top.

**A cell that has to be read twice is a paragraph in the wrong place.** Gate 93 fails any cell over
110 characters.

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
- there is no `**Charge.**` paragraph outside the table, or it does not state the sixty-second fill,
  the ceiling, the tenth-a-minute run-down, and the Work Damage consequence;
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
