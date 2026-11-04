# R-48 — The Charge

**Stated by the archive owner, 2026-11-04:**

> *"WHAT THE USED OF HP ON RELIC SE THAT WONT USED THE HP, YES POSSESSION CAN USED THE HP ..."*

> *"... IT STILL READ ILLOGICAL ... AND FEEL BLOATED ... TRY TO REINVENT IT INTO A MORE LOGICAL
> MECHANIC"*

> *"WHAT IF YOU DIVIDED EXPLANATION AND THE TABLE IN TWO AND ALSO REINVENT WHAT THE NUMBER IS FOR
> RELIC SE THAT USED THIS NEW GAUGE AND SO EACH TIER OF THE SE HAVE BRAND NEW INVENTED GAUGE
> NUMBER AND WHAT IF THIS GAUGE IS PUNISHMENT + LIMIT OF USING IT, YOU KNOW LIKE HOW IN L CORP
> THERE IS A LIMIT OF HOW LONG AN AGENT CAN USED/HOLD/EQUIP IT ... THERE SHOULD BE HARD LIMIT THAT
> IS UNIVERSAL FOR ALL RELIC SE, AND ... IF THE LIMIT REACH THERE A CONSEQUENCE OF TRYING TO USED
> IT WHEN IT NOT YET 'RECHARGE' AND THE RECHARGE RATE CAN WORK LIKE ... THERE IS A LINE FROM MAX
> TO 00"*

This is the third draft and it replaces both earlier ones.

## 0. The three faults this fixes

| draft | fault |
|---|---|
| 1 | three bands under a number nothing moved — decoration |
| 2 | a real spender, but the explanation sat **inside** the table cell, so a nine-word mechanic took ninety words to say |
| 3 | — |

**The division is the point.** A table is for what a Warden reads at the cell door in two seconds.
A mechanic is for the page under it, once, on the night before. Draft 2 wrote both into the same
cell and called the result a gauge.

## 1. What the charge is

**The gauge is the relic's charge, and the charge is both the punishment and the limit.**

- It is **the punishment** because the number is the size of what the thing takes out of whoever
  holds it. A ZAYIN costs 240. An ALEPH costs 1,080.
- It is **the limit** because when it reaches 000 the relic is **spent**, and a spent relic will
  not take a hand at all.

That is the whole answer to *"what good is a gauge that isn't HP"*. HP told you when the **thing**
would stop. This tells you when **you** stop — and it is the same number doing both jobs, so there
is no second stat to learn.

## 2. The number is invented by the tier, never by the file

No writer picks a relic's charge. It comes from the tier, and from nothing else:

| tier | charge | the minute costs you |
|---|---|---|
| **ZAYIN** | **240** | the least it can cost and still be a relic |
| **TETH** | **420** | |
| **HE** | **660** | |
| **WAW** | **880** | |
| **ALEPH** | **1,080** | the most this archive has ever measured |

Every tier's figure sits inside the band `check_stat_bands.py` already enforces, so the archive's
existing scale keeps its meaning. **143 dossiers renumber to five numbers.** A reader who knows
the tiers can now guess a relic's charge before opening the file, which is what a tier is for.

## 3. The hard limit is universal: sixty seconds

**No relic may be held for longer than sixty seconds of contact. Any relic. Any tier.**

This is L Corp's work timer and it is the one figure in this archive that is not tiered, not
categorised and not negotiable. Sixty seconds of continuous contact and the charge is at 000,
whatever its size — the thing spends its whole length in that minute, so a longer charge is a
heavier draw, not a longer leash.

**At 000 the relic is spent.** Not damaged, not suppressed, not dead: spent. It will not take a
hand.

**The universal law underneath the sixty.** Whatever fills a relic's gauge, **nothing may be used
at 000.** For the 134 charge gauges that zero arrives through contact time; for the 9 that keep
`[HP]` it arrives through suppression. Two roads to one rule.

## 4. The two lines

**Down — discharge.** The whole of it, in sixty seconds, on every relic:

```text
660 ─────────── 60 s ─────────── 000
```

**Up — recharge.** It climbs the same line back, a **tenth of itself a minute**, so ten minutes
from spent to brim at every tier. This is the "line from max to 00" the owner asked for, read in
reverse:

```text
000 ── 1 min ── 066 ── 2 min ── 132 ── 3 min ── 198 ── ... ── 10 min ── 660
```

**Below half it is worth less than half**, because it is still filling: a relic at 330 of 660
gives thirty seconds, not sixty. The charge is read, never assumed.

## 5. The consequence of using it before it has recharged

Two cases, and they are different sizes of mistake.

**Taken up before the brim, but not spent** — you do not get a fresh minute. **The Work Damage
clock resumes where it stopped instead of starting over.** `R-47` says the clock resets to base
the moment contact breaks; this is the clause that makes that reset conditional. Put a HE relic
down after forty seconds, pick it up ninety seconds later, and you are back on the tight interval
with twenty seconds of charge left.

**Taken up at 000** — it refuses. The attempt is answered the same way it would answer a
suppression: **the first dose of the Work Damage lands immediately, in full**, and **the refill
restarts from 000.** Two hundred marks of refill are wiped because someone would not wait. This
is the punishment, and it is the only one in the archive that punishes impatience rather than
curiosity.

## 6. The division: table and explanation

**The table cell is data and nothing else:**

```text
| **Sorrow Gauge [Depth]** | **660/660** · full · limit 60 s · refill 10 min |
```

Four readings, no sentences: the charge and its size, the state, the wall, and the refill time.

**The explanation is a paragraph outside the table**, under the stat block, led in bold so the
eye finds it:

> **Charge.** At the rite, it spends the whole of itself in sixty seconds — 660 down to 000 — and
> at 000 it is spent and will not take the hand. Left alone, it climbs back a tenth a minute, so
> ten minutes from spent to brim. Handled again before the brim, the Work Damage clock resumes
> where it stopped rather than starting over; handled at 000, the first dose lands at once and the
> refill begins again from nothing.

A cell that has to be read twice is a paragraph in the wrong place.

## 7. What the measure is called

Unchanged from draft 2, because this part was right: the gauge is named for what the holding puts
into the handler, which is the dossier's own `**Element**`.

| Element | gauge | what the hands are taking |
|---|---|---|
| **Grudge** | `[Pressure]` | force pushed back through the arm that holds it |
| **Weight** | `[Load]` | mass carried on the frame of the carrier |
| **Lament** | `[Depth]` | grief taken down into the person — a level, not a volume |
| **Void** | `[Saturation]` | absence poured in until there is no room for anything else |

Four elements, four harms, one gauge shape.

## 8. The nine that keep `[HP]`

- **Possession — 2**, by the owner's word: the bearer is what falls.
- **Breaching relics — 7**: a relic that can breach is suppressible.
- **Subjects** — unchanged; their cost is a work session, already `R-44`.

Their gauge runs to 000 by suppression rather than by the minute, and **§3's law binds them
harder, not less**: nothing may be used at 000.

## 9. The gate

`tools/auditors/check_relic_gauge.py` (gate 93) fails a non-breaching, non-possession relic when:

- the label is `[HP]`, is not one of the four measures, or disagrees with the `Element` row;
- the charge is not the figure its **tier** dictates;
- the reading is not full, or the cell does not carry `full`, `limit 60 s` and `refill 10 min`;
- the cell runs past **110 characters** — the table is data, and a sentence in it is draft 2's
  fault returning;
- there is no **explanation paragraph** outside the table, or it does not state the sixty-second
  wall, the 000, the tenth-a-minute refill, or the Work Damage consequence;
- a possession, breaching relic or subject has lost its `[HP]`.

## 10. What this does not do

- It does not change a category. `R-47`'s per-second dose and its tightening clock are untouched;
  the charge is what the dose is drawn from.
- It does not invent a sixth tier or move a relic between tiers.
- It does not touch a subject's numbers.

## Rollout

| | before | after |
|---|---|---|
| relic gauges | 134 arbitrary ceilings, 198–993 | **5 tier figures**, 240 / 420 / 660 / 880 / 1,080 |
| table cell | 300–500 characters of prose | **under 110 characters, data only** |
| explanation | inside the cell | **a paragraph under the table** |
| `[HP]` retained | 9 | 9 |

By tier, of the 134 converted: **ZAYIN 240 ×20 · TETH 420 ×43 · HE 660 ×33 · WAW 880 ×34 · ALEPH 1,080 ×4.**

## Owner direction

Batch 196, 2026-11-04. Filed as **O-34** in `OWNER_DIRECTIVES.md`. Drafts 1 and 2 are superseded
in full.
