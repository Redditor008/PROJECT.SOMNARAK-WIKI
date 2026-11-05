# R-49 — A Work Can Cost, Cost Nothing, or Give

**Stated by the archive owner, 2026-11-05:**

> *"Can You Add Work Dmg/Buff To Normal SE TOO So Like L Corp When Working With SE Agent Can Get
> Hurt Or Buff Base Of The SE And Buff Is Rare So Either Dmg/Neutral/Buff The Agent Who Is Doing
> Work On The SE And For Percentage Dmg 65%/ Neutral 25% / Buff 10% Of All SE"*

## 1. Three answers, one row

`R-44` gave every worked holding a `**Work Damage**` row, and every one of them charged the worker.
Measured at the moment of this rule: **158 subjects, 158 charges, 0 that cost nothing.** A ladder
where every rung bites is not a ladder; it is a wall with numbers on it.

The row now carries **one of three verdicts**, and the verdict is read off the row itself:

| verdict | what the row says | share of the ladder |
|---|---|---|
| **Damage** | a band and the holding's own element — unchanged from `R-44` | **103 of 158** |
| **Neutral** | `None`, and a clause saying what the holding does with the cost instead | **39 of 158** |
| **Gift** | `None`, plus a second row `**Work Gift**` saying what the worker takes out | **16 of 158** |

Two of the three verdicts begin with the same word. That is deliberate: **the default is that the
worker is not charged**, and a `None` is not a missing reading — it is the reading. A dash, a
`N/A`, or an empty cell would be the defect this rule replaces.

## 2. The split is the rule; which file gets which is the reading

**65 / 25 / 10 is a constant of the setting, not a per-file judgement.** A gift you can count on is
not a gift, and a chamber where two in five holdings are harmless is not the Desolate. The counts
are therefore fixed and the gate enforces them exactly:

```
Damage   103     Neutral   39     Gift   16        (158 subjects)
```

**The percentages live in this rule and nowhere else.** `R-44` §2 and the `printing a percentage`
standard already bar a proportion in a response cell: a dossier states what *this* holding does, in
words and bands. A reader who wants the distribution reads the rule.

**Who goes where is decided from the file's own record**, in this order:

1. **Gift** goes to the holdings whose own text already pays something out — return-language in the
   Operational Notes and the Behaviour responses — and never to a holding whose clause is about
   consumption, erasure or burial. The gift is what the record was already doing.
2. **Neutral** goes to the quietest readings: the smallest bands and the least violent clauses. A
   holding that charges `1–2` and describes a stillness is the one that costs nothing.
3. **Damage** is everyone else, and their existing rows are **not rewritten**. The split is applied
   by moving the two quiet outcomes onto the files that earn them, not by re-authoring 158 clauses.

## 3. Damage — unchanged

`R-44` §2 stands: an amount inside the band for the entity's grade, the entity's own `Element`, and
one clause naming the mechanism. Nothing about the damage reading moves in this rule.

## 4. Neutral — the row says `None` and the clause says who pays

```text
| **Work Damage** | None — {the mechanism the holding would have charged}, and it is the room that
pays it, not the worker |
```

The mechanism is kept **verbatim** from the file's existing clause, with `the cost is` struck. That
is what makes a neutral reading specific: the lightness, the borrowed name, the cold — the same
thing the damage reading describes — and it settles on the chamber instead of on the person. A
neutral that reads *"no effect"* is not a reading and fails the gate.

## 5. Gift — a loan with a ceiling, an end, and a price

A gift is the rarest thing in the archive, and it is never free. Four things are stated, and a
`**Work Gift**` row missing any one of them fails the gate:

| part | shape | why |
|---|---|---|
| **the amount** | a band — `+5–10` | `R-44` bands, not a single number |
| **the stat** | `Composure` or `Resilience` — the two this archive already uses | a number that lands on a named stat |
| **the end** | `for the rest of the cycle` | a loan, never a permanent line on the worker's sheet |
| **the price** | one clause, in the holding's own element | the cost is paid by the bearer |

**Precedent — L Corp `T-09-78`, Notes from a Crazed Researcher.** The first Abnormality whose
effect triggers when the employee is hurt: equipped, it gives *Temperance +20 to success rate and
work speed* — and the cost is paid by the body over the equipped period. A positive effect with a
bearer's price is the shape this archive already researched; `R-49` is that shape with the ceiling
and the end written down.

**Gifts are paid in the holding's own currency**, and the price is read off the `Element` row:

| element | what the loan is paid in |
|---|---|
| **Grudge** | the loan is debt: it is entered against the worker's name and read at the next review |
| **Lament** | it is paid in the memory it was drawn from, and the worker cannot check which one |
| **Void** | what it lends it takes back at the end of the cycle, and names no interest rate |
| **Weight** | the loan is carried: it must be set down before the door or it leaves with the worker |

**What a gift may not do.** It may not raise a stat permanently, may not make working the holding
strictly better than not working it, and may not change the gauge. A gift is paid to the *worker*,
not to the work.

## 6. What the gate enforces

`tools/auditors/check_work_effect.py`:

- every subject carries a `**Work Damage**` row — a holding with no work loop is out of scope
  (`R-35`, `R-40`);
- the value begins with a band inside the grade's range (`R-44` §3) or with the word `None`;
- a `None` carries a clause of at least eight words, and never reads as a bare `no effect`;
- a `**Work Gift**` row exists **exactly** on the gift verdict, states a band, a named stat, an
  end, and a price;
- neither row prints `%`;
- the three counts are **103 / 39 / 16**, enforced as a ratchet so they can only move deliberately.

## 7. What this changes elsewhere

The subject template carries the three verdicts and the optional gift row. `R-44` §2 gains a
pointer here. The `how_finished.py` dashboard gains an eighteenth standard. Relics are **not** in
scope: a relic's contact is already continuous and is priced by the second under `R-47`, and a relic
offers no work to be buffed by.
