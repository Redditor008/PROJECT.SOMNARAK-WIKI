# Comparative Study 01 — Two of Ours, Two of Theirs

**Subjects:** `SE-C-Iα-900` Vellum Man (잊혀진 이야기꾼) · `SE-O-IIβ-757` Broken Door (부서진 문)
**Benchmarks:** `O-04-72` The Burrowing Heaven · `T-09-97` Old Faith and Promise (Lobotomy Corporation Wiki, wiki.gg)
**Written:** Year 4,237 / 2026-10-05 · **Status:** reference, not canon · **Rules in play:** `R-19`, `R-24`

This document does two things. First it sets two of our own entities against each other, picked because they
are the two most recent dossiers to reach the Tale standard and because they are the same thing in two
different registry shapes. Second it sets each of them against a published Abnormality article, to test
whether our dossiers now behave like finished articles or still behave like filled-in forms.

Both of our subjects were rewritten this week: Vellum Man from prose generic fraction **0.224 → 0.000**,
Broken Door from **0.224 → 0.004**, both at `tpl.py` residue **0** and `verify.py` **RESIDUAL 0**.

---

## 1. The two of ours, side by side

| Field | Vellum Man `C-Iα-900` | Broken Door `O-IIβ-757` |
|---|---|---|
| Entity Type | Subject | Object/Place (O-Relic) |
| Coherence / Potency | Residue (I) / Minor (α) | Echo (II) / Moderate (β) |
| Sorrow Category | City Sorrow (도한) | Outside Sorrow (외한) |
| Element | Lament | Grudge |
| Manifestation | Subject-Tale | Place-Grudge |
| Movement | Mobile — has left the sector twice | Stationary — has never moved |
| Siting | SECTOR-C-900, contained, one bolted chair | Open grass, Echo Gardens, painted four-metre radius, public |
| Instrument of record | Transcription register: 309 tales, 11 unique, 41 open | Flame-grade scale every ten minutes + departures ledger: 201 mentions, 4 contacts |
| Working act | Reading a page to its end and writing it down | Watching from the side of the frame and saying no name |
| Hazard | The transcriber who stays past thirty minutes | The worker who turns the handle |
| Recorded harm in service | 0 injuries, 11 stand-downs, 6 withdrawn tales | 4 injuries, all to people holding the handle |
| M.A.W. | 3 pieces, all pages; 11 tales lost permanently | 2 boards + 1 hinge; authorisation lapsed, not renewed |
| Disposition (`R-19`) | **Neutral** | **Neutral** |

### What they share

Both are **records that outlived the people in them**, and both are worked for the record rather than for
energy. Vellum Man's 12–18 Han-Energy and Broken Door's 12–18 are the same unremarkable figure, and in
both files the operational interpretation says in plain words that the yield is not the reason the holding
is on the roster. One is a manuscript of tales nobody alive can still tell; the other is the last standing
piece of a household that divided lawfully and never reassembled. Neither has an antagonist. Neither origin
contains a wrong.

Both are also **Neutral by the same route and for different evidence**. Harm lands only on the person who
performs the voluntary act — sitting too long, or taking hold of the handle — and in both cases every
relationship on file runs *inward*, which `R-19`'s directionality test says cannot move the class. Broken
Door is the cleaner demonstration: the Hand of Hope, the Gentle Flame and the Debt Eater all act on the
Undelivered Thanks and fail; the Collapsed Door's *departure* is what drops Broken Door's flame. Things
done to an entity are not things the entity does.

### What separates them

The difference that matters is not Subject versus Object/Place. It is **who holds the record**.

Vellum Man *is* the archive: the pages are the text, and every extraction is a subtraction — the eleven
tales cut away in Year 4,233 are the only entries in the register written in red. Broken Door is not the
archive; the Echo Gardens office is, and the holding is only the instrument the office reads. You can cut a
board off Broken Door and lose a board. You cannot cut a page off Vellum Man without losing a story.

That asymmetry is why one is `Vessel-Destructible: Yes` at Residue coherence and defended by a thirty-minute
shift, while the other survived a demolition order and is defended by a painted line on grass and a habit
the staff keep among themselves.

---

## 2. The benchmarks

### `O-04-72` The Burrowing Heaven — WAW, instadeath and escape
Source: <https://lobotomycorporation.wiki.gg/wiki/The_Burrowing_Heaven>

The management rule is one sentence of plain instruction: *"Work with The Burrowing Heaven must be done
while the manager has the Containment Unit in sight."* Everything else in the article is the arithmetic of
that sentence — the Qliphoth Counter falls by 1 the moment the unit leaves the screen during work and by a
further 1 every additional 10 seconds off screen; it rises by 1 on a Normal result and by 2 on a Good one;
off screen the work success rate is forced to 0%. At counter 0 it breaches with 800 HP, instantly kills
anyone in the containment room, moves only after 3 seconds out of camera, and deals 150 BLACK to everything
left in the room it leaves. Its breach resistances are given as numbers: RED immune 0.0, WHITE weak 1.2,
BLACK endured 0.5, PALE weak 1.5.

Two details are worth stealing outright. First, the hazard **is** the instrument: a gaze is both the
containment mechanism and the measurement, so the article never has to tell the reader to "record the first
measurable change" — the change is the counter. Second, the Story section escalates by Observation Level and
is written as address rather than exposition: *"Don't look away, just keep your eyes on it… It lives inside
your gaze. The containment is but a facade."* Flavor text is two lines, uses the `<name>` placeholder, and
describes one thing happening.

### `T-09-97` Old Faith and Promise — ZAYIN, Tool, single use
Source: <https://lobotomycorporation.wiki.gg/wiki/Old_Faith_and_Promise>

A ZAYIN tool that cannot hurt anybody and is nonetheless one of the most dangerous things in the facility,
because what it costs is not health. The employee bets an E.G.O weapon; on a Good result the weapon's damage
is boosted for the day; on a Bad result the weapon is destroyed, **and resetting the day or restarting from
the Memory Imprint will not return it**. The article prints the whole gamble as a table — boost 0 at 85%
success for 2% energy, rising to boost 4 at 200% damage, 25% success and 12% energy — and its Log entries
escalate from a description of a marble to *"However, all that they yielded was only hollowness and
betrayal."*

This is the closest published analogue to our own extraction losses, and it is the model for how to write
them: the irreversibility is stated once, flatly, in the mechanics, without being dramatised.

---

## 3. Findings

**1. A management condition should be one sentence a worker can obey.** Burrowing Heaven: *keep it in
sight*. Old Faith and Promise: *it may not give the weapon back*. Our two now read **thirty-minute shifts,
notebook never closed mid-tale** and **say no name, do not touch the handle**. Both pass. Much of the rest
of the archive still answers this question with a list of fields to record, which is an instruction to the
author, not to the worker.

**2. The hazard and the instrument should be the same thing wherever the fiction allows it.** Burrowing
Heaven measures itself in the one resource that also kills you. Broken Door's flame grade and Vellum Man's
register are close but not identical to their hazards; the next strongest version of each would make the
measurement and the danger one object. This is a design note for Workstream 7, not a defect in these two.

**3. Irreversible loss belongs in the mechanics, stated once.** Old Faith and Promise spends one clause on
the fact that the weapon never comes back. Our equivalents — eleven tales, two boards and a hinge — are now
stated in the same register, in the M.A.W. section and in the register's red entries, and nowhere else.
**Do not repeat an irreversible loss in four sections; it reads as pleading.**

**4. Narrative escalates, it does not accumulate.** The Burrowing Heaven's Story runs 0 → 1 → 2 and each
level is a different *kind* of text: description, instruction, then an unattributed voice. Our Story Log is
the same device and should be held to the same rule — Entry 5 must know something Entry 1 did not, rather
than restating the classification in a different order. Vellum Man's five entries now do this; the
archive-wide Story Log section still scores **0.77** on the league table and is the fourth-worst section we
have.

**5. A finished article may admit the holding is barely a hazard.** ZAYIN exists. Our Minor (α) and Residue
(I) grades are the same admission, and Vellum Man's threat assessment now says plainly: nineteen years, no
injuries, two breaches that ended by themselves. A grade that overstates is as much an error as one that
understates — Broken Door's file says the β on its extraction line has never been tested, and the
Undelivered Thanks' says its β overstates it and has not been revised because a revision would take the
route off the roster.

---

## 4. What this changes

Nothing in canon. Three things in practice, all carried forward to **Workstream 7 — The Reset Pass**:

- The Story Log is the next section to attack after the per-entity queue, on the escalation rule in Finding 4.
- The "record X, Y, Z" phrasing is the single largest remaining source of shared prose; the benchmark shows
  it is not how published articles write procedure, and the reset pass should treat any surviving instance
  of it as residue even when `tpl.py` is silent.
- Instrument-and-hazard unification (Finding 2) is a quality bar for the reset pass, not a requirement for
  per-entity work now.

---

**Counters at time of writing:** dispositions **283 / 303** (20 pending) · cleans 291 / 291 · headline 0.00%
(body scope) · prose Tale standard **85 / 303**, residue-free **29 / 303**, median **0.098**, worst **0.293**
(`SE-N-Iα-686` Torn Window) · 5,031 shared 8-grams · rules 26.

---

## Addendum — tested against twenty pages

`COMPARATIVE_STUDY_02_TWENTY_PAGES_FIVE_LEVELS.md` tested the five findings above against twenty pages at all
five levels and ten pairings. All five stand. Two need correcting. Finding 1: the wiki's management text is a
list that decays into incident reports above ZAYIN, so one obeyable sentence is our improvement on the wiki, not
the wiki's practice. Finding 3: the wiki states the price of the remedy at every level above ZAYIN and the price
rises with level, so an irreversible loss stated once is necessary and is not sufficient. Finding 5 gains a rider:
three of four ZAYIN pages in the sample hide a catch in their Story. The original text above is left as written.
