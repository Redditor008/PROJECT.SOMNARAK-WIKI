# R-47 — A Relic Charges By The Second

**Stated by the archive owner, 2026-11-04:**

> *"Also Do Relic SE Need HP, ATK Still Can But It Interaction Dmg As In The Longer The Agent
> Used/Equip/Hold It The Higher The Dmg Taken And The Dmg Is x Dmg/x Second/ect.[Based Of What
> Category Of Relic It Is] To Learn Much More Research Tool Abno"*

## 1. The three answers

### HP — yes, every relic, always

The `**Sorrow Gauge [HP]**` row is not a combat hit point and was never meant to be one. It is
**the containment meter** — the number the containment is read against, taken at the door and at
the plinth, and the thing that tells a Warden whether the watch is going well. Every relic has
one because every relic is contained, and containment is a reading, not a fight.

### ATK — no, not on the dossier

**A relic does not strike.** It has no attack value in its own record, and an `**ATK**` row on a
relic dossier is the same category of error as a Work Type table on one: it describes a thing
that can only happen to a subject. Measured at the moment the rule was made, **0 of 301 dossiers
carry an ATK row**, which is the archive having this right without having written it down.

Where a relic genuinely has an offensive form, that value lives in its **weapon record** — the
`-B` page of its M.A.W. set — which is a separate document with its own damage line. The dossier
does not duplicate it. *"A balance-scale is not a fist"* is the whole of the rule.

### Interaction Damage — yes, and this is the relic's real cost

The `**Work Damage**` row on a relic is **a dose, not a session.** A subject's work damage is
what a session costs, paid once and over. A relic's is what **contact** costs, and it is paid
continuously for as long as the contact lasts.

> *"The longer the agent used / equips / holds it, the higher the damage taken."*

So the relic's row states **X damage per Y seconds**, and it states what happens to the clock as
the contact goes on.

## 2. The clock is set by the relic's category

This archive already files relics by category in the `**Tool Type**` row. The category is not
decoration — it decides **how the dose accrues**, because it decides what "using" the thing
physically is.

| category | what the relic is | clock | what the clock measures |
|---|---|---|---|
| **I-Relic (Indumentum)** | worn on the body | **10 s** | continuous contact with skin — the fastest clock, because there is no interval in which the wearer is not touching it |
| **O-Relic (Officium)** | a rite performed | **15 s** | each act of the rite, timed from the first movement to the last |
| **A-Relic (Arcanum)** | consulted for an answer | **20 s** | each reading taken — the dose runs while the answer is being given |
| **O-Relic (Offertorium)** | a votive thing left in place | **30 s** | standing within its reach — the slowest clock, because the relic is not being touched and the operator is only near it |

### Where there is no Tool Type

A relic that is a Place, a Time or a Hazard carries no `**Tool Type**` row, because it is not a
tool — you do not pick it up. Measured 2026-11-04: **61 of 143 relic dossiers** are in this
position. Their clock is read off `**Entity Type**` instead, which every dossier already files:

| Entity Type | clock | what the clock measures |
|---|---|---|
| **Object/Place**, **Place** | **30 s** | standing within it — nothing is touched, and the dose runs on presence |
| **Time** | **20 s** | being inside the interval — the clock runs while the operator is in it |
| **Hazard** | **15 s** | exposure in the field — the dose runs while the operator is in the air it has taken |
| **Possession** | **10 s** | worn or entered — the fastest, for the same reason an Indumentum is |

A Place and an Offertorium therefore share a clock, and that is correct: both charge you for
standing still, and neither charges you for holding anything.

The four clocks are 10 / 15 / 20 / 30. They are not a ladder of severity — an Officium at 15 s
can be worse than an Indumentum at 10 s — they are four different physical situations, and the
number in front of the clock is what carries the severity.

## 3. The acceleration

**The damage per interval stays inside the `R-44` band. What changes is the interval.**

The band (`Low 1–3` · `Medium 1–4` · `Common 2–6` · `Top 3–8` · `High 5–10`) is the archive's
existing cost scale, and a relic's dose starts at the bottom of its band and stays inside it. The
horror is not the number — it is that **the clock halves at the end of each further minute of
continuous contact**, to a floor of one second.

```text
| **Work Damage** | 2 Grudge / 10 s while worn; the clock halves at the end of each further
minute — 10 s, then 5 s, then 2 s. It resets the moment the piece comes off. Nobody takes it off. |
```

Read that as a Warden would: two points in the first ten seconds, two points in the next ten,
then the same two points every five seconds, then every two. The dose per minute goes
**12 → 24 → 60** without a single number leaving the band.

**Why halving rather than a rising number.** An escalating number needs a ceiling or it breaks
the band the archive already checks. An escalating *rate* has no such problem — it is bounded by
the interval floor of one second, which is bounded by arithmetic, not by taste.

## 4. The reset is the mechanic

**Put it down and the clock goes back to the base interval.** That is the only thing that works,
and it works immediately.

**It is not free, and it is not a way out — the reset is conditional.** The clock goes back to base
only when the gauge has **run back down to 000** (`R-48` §5). Short of that it resumes at the
interval it had reached, so an operator who holds a thing for nine seconds of every ten and never
lets it settle climbs the ladder anyway.

Read the two rules as one: `R-47` is how fast the gauge fills. `R-48` is how long the line is, how
long it takes to run back down, and what happens to anybody who does not wait.

Which is why every relic file has to answer one question, in its own terms:

> **Has anyone ever put it down?**

For most of these the answer is no, and the reason is in the file already — the strap has to be
on skin, the rite has to be finished, the reading has to be taken to the end. The reset is what
makes the horror a choice instead of a condition. A relic that simply hurts you is weather. A
relic that hurts you and stops the moment you let go is a file about **why nobody lets go**.

## 5. What the row may not do

| forbidden | why |
|---|---|
| a session range with no clock — `3–5 Lament — the cost is …` | that is a subject's cost. A relic's cost is per second or it is not a relic's cost |
| a clock with no acceleration | *"per 10 s"* with no second clause is a metronome, not a dose; `R-47` §3 requires the clock to tighten |
| an acceleration with no reset | removes the only thing the reader can act on |
| a ceiling outside the `R-44` band | breaks the archive's cost scale to make a sentence land |
| `per use` with no seconds | *"per use"* is not a duration and cannot be planned for |
| an `**ATK**` row | §1 |

## 6. Why Project Moon's Tool Abnormalities are the model

Researched 2026-11-04, and the owner's instinct was exact. In Lobotomy Corporation:

- **Tool Abnormalities** are the `09` type (`07` where the tool can breach, which is one entity
  in the whole game). There are **16** of them.
- *"The Tools don't possess work preferences but instead have a single work to use them."* — no
  Instinct/Insight/Attachment/Repression ladder, exactly as `R-40` says a relic has no Work Type.
- They are **mounted or equipped**, not worked at: the wiki files one as *"Mounting type"*.
- *"Tools give positive effects … often for a cost."* The cost is the point.
- And the cost is charged **while the thing is on you** — the same shape as the owner's
  *"the longer the agent used / equips / holds it."*

The archive's four relic categories are a finer reading of the same idea: L Corp has one Tool
type, this archive has four, and the four exist because an Indumentum and an Offertorium do not
charge you the same way.

## 7. The gate

`tools/auditors/check_relic_interaction_damage.py` (gate 92) reads every non-subject dossier's
`**Work Damage**` row and requires three things:

1. **a clock** — `/ N s` or `/ N s`-equivalent (`per N s`, `every N s`);
2. **an acceleration** — a minute horizon and the clock tightening;
3. **a reset** — the row says what stops it.

It also fails any dossier, relic or subject, that carries an `**ATK**` row.

## Owner direction

Batch 193, 2026-11-04 — the instruction quoted at the top of this file. Filed in
`OWNER_DIRECTIVES.md` as **O-33**.
