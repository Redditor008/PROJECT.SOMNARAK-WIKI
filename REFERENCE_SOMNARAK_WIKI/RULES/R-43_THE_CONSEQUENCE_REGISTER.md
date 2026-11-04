# R-43 — The Consequence Register

**Stated by the archive owner, 2026-11-04:** *"I don't see from Low to Special many differentiation
in both how we see them and how they act, and also the consequence ladder from Low to High is all
almost the same — like they all don't have personality and different in anything other than shape
and combat record and story, but they act almost the same everywhere else. They don't act like
their threat tier and they don't have gap of consequence."*

Then, correcting a narrower reading of the first note: *"Consequence in general, not just the
section. I mean consequence in how the SE interacts with agents, other SE, and more — and
consequence in broader terms, not just mechanic."*

## 1. What is being fixed

`R-42` put the stat line on its rung. It did not touch the thing the owner is naming now: **what
the entity leaves behind, and how far the mark reaches.** Measured on 2026-11-04:

| measured | result |
|---|---|
| `### Consequences` present | 297 of 301 |
| Top (WAW) consequences naming no institution at all | **29 of 84** |
| Low (ZAYIN/TETH) consequences claiming city-scale reach | **17** |
| Top-and-above combat records carrying an `[**Ultimate**]` | 52 of 53 |
| Low (ZAYIN) combat records carrying an `[**Ultimate**]` | **27 of 27** |
| Low `[**Ultimate**]` rows that are the same copied AoE line | **27** — `12-20 … DMG (AoE, x3 turns)`, one phrase swapped |

The last line is the clearest single symptom. *The Kind Echo*, *Risus*, *The Silent Child* and
twenty-four others each finish their action table with `All in range suffer … pressure for three
turns — [one phrase] — **[12-20 DMG (AoE, x3 turns)]**`. A ZAYIN holding is a thing found in one
room that one worker can be taken off. It does not sweep a room for three turns, and twenty-seven
of them doing it in the same sentence is a template, not a threat profile.

## 2. The three registers

Consequence is not one section. It is three, and each has to sit on the entity's own rung.

| register | where the file carries it | the question it answers |
|---|---|---|
| **Personnel** | `### Consequences`, `## Behavior`, `### Special Behaviors`, Observation Log | what happens to the worker in the room |
| **Peer** | `### Interaction Pattern`, `### Entity Interaction Record`, related-entity rows | what happens when two holdings are put beside each other |
| **Institution** | `### Consequences`, `### Escalation Notes`, Containment Event Behavior | who signs for the loss, and how far the paperwork travels |

A file that writes only the personnel register at every tier is why the ladder reads flat. The
Maw's file is not frightening because of its damage line; it is frightening because its
consequences are written in the **institution** register — a perimeter surveyed every quarter, a
negotiation held every quarter, ground given up and never recovered, and a record written for the
next generation rather than this one.

## 3. The rungs

| band | personnel | peer | institution |
|---|---|---|---|
| **Low** (ZAYIN) | one worker, one room, reversible by walking out; an afternoon or a small memory | the other holding does not react to it; proximity is the whole relationship | nobody above the wing hears about it, and the file exists because a form required one |
| **Medium** (TETH) | a team; the worker comes back changed and the roster changes with them | the other holding notices it; a second file begins to record the pairing | the wing writes a procedure, not a report |
| **Common** (HE) | a shift; the room is closed afterwards and the closing is logged | a pairing is scheduled, with a baseline series and a witness | the wing loses a working day and the loss is budgeted |
| **Top** (WAW) | a wing; the loss is counted in staff and in rooms | two holdings are held apart on purpose, by order | an order is signed above the wing, and the facility carries it in its posture |
| **High** (ALEPH) | a district; the people are moved, not treated | the relationship is a standing arrangement between wings | ground is given up, a perimeter is drawn, and the loss is permanent and public |
| **SPECIAL** | there is no worker to fail; the failure is the chain completing | the pairings are what summoned it | the archive has no containment, and the file is a contingency register, not a containment record |

**Nothing is required to be dramatic.** A Low entity's consequence is small *and specific* — a coin,
a second look, a letter not answered. The rung is about **reach**, not volume: what a Low file must
not do is claim the city, and what a High file must not do is stop at one tired worker.

## 4. The action rung

An action table is a threat profile, and the rung decides what a file is allowed to have on it.

- **Low** — no `[**Ultimate**]`. A thing found in one room has no finisher. Its last move is an
  `[**Exhaustion**]`: what the holding spends on the person in front of it, single target, and then it
  is spent. *Not* `[**Overload**]` — that word is already the handling-procedure category, and reusing it
  here would have put two different meanings on one label. Damage stays inside the Low band.
- **Medium and Common** — an `[**Ultimate**]` may exist, scoped to a room or a wing.
- **Top** — the `[**Ultimate**]` is an order-level event: it changes what the facility can do next.
- **High and SPECIAL** — the `[**Ultimate**]` changes the map, and the file says what the map looks
  like afterwards.

`R-36` already establishes that a fixed thing carries a `## Contact Record` instead of a fight.
This rule is the other side of it: **a thing that does fight fights at its own rung.**

## 5. What the gate enforces, and what it only reports

`tools/auditors/check_consequence_register.py` (gate 86) enforces the two ends:

- a **High or SPECIAL** file must name an institution-scale payer in its `### Consequences`
  (district, city, perimeter, registry, facility, archive, or an order signed above the wing);
- a **Low** file must not carry an `[**Ultimate**]` at all.

It **reports** without failing: the middle rungs. A Common entity that writes a city-scale
consequence, or a Top entity that never leaves the personnel register, is printed with its count so
the owner can rule on it — which is the same one-directional discipline `check_stat_bands.py` uses,
and for the same reason: the archive is repaired in tranches, and a gate that fails on 60 files
teaches nobody anything.

## 6. Precedents

- **The Maw `C-IVω-001 [GP]`** — the register to copy. Written entirely in the institution register
  and never once raising its voice.
- **The Grieving Colossus `C-Vδ-002`** — a High record whose first four consequences are all
  personnel. It is the clearest case of a file that is frightening in its combat section and tame
  in its consequences, and it is why the register test is not the same test as the stat test.
- **The Forgotten Market Stall `C-IIα-062`** — a Low record done right: the cost is a coin, a
  button, or a memory the buyer judges unimportant, and the drift is one worker finding the goods
  *reasonable*. Nothing in it claims the city.
