# R-51 — A Table Row Answers One Question

**Stated by the archive owner, 2026-11-05:**

> *"I Think There Is Something Missing Example SECC Refinement"*

## 1. The gap this closes

`R-45` §3 gives every section one question and forbids a section answering a different one. Applied
to `SECC Classification` it said **"values only, read off the code"** and forbade *"a description, a
clause of behaviour, or an explanation."*

That is not what the archive was built to. `TEMPLATES/SE/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md`
lines 70–71 specify:

> **`Coherence`** — `{{Rank Written}} ({{I-V}}) — {{Behaviour descriptor}}`
>
> **`Potency`** — `{{Potency Written}} ({{α/β/γ/δ/ω}}) — {{Threat descriptor}}`

(both rows quoted verbatim from the template, lines 70–71)

Two documents, both binding, saying different things about the same two rows, and **no gate reading
either of them**. Measured across the 301 dossiers the archive had split along the seam: seven
files wrote the pair backwards — `I — Residue (barely formed)` where the template asks
`Residue (I) — Barely formed` — and five had let the descriptor become a sentence with its own
finite verb, which is the thing `R-45` was right to object to and the thing a table cell cannot hold.

**The rule is the narrow reading both documents can hold:** a row carries **one value and, at most,
one descriptor**. The value is read off the code and is not negotiable. The descriptor is a phrase —
it names what the cell is for, it does not explain it.

## 2. What a cell may hold

    Value (Symbol)                      Coherence: Residue (I)      Potency: Minor (α)
    Value (Symbol) — Descriptor         Coherence: Fragment (III) — Personality shaped by origin
                                        Potency:   Moderate (β) — Manageable with standard precautions

**The value is drawn from the world pages, not from memory:**

| row | symbols | words | stated at |
|---|---|---|---|
| `Coherence` | `I`·`II`·`III`·`IV`·`V` | Residue · Echo · Fragment · Entity · Sovereign | `Pages/38-Classification Code.md` §3 |
| `Potency` | `α`·`β`·`γ`·`δ`·`ω` | Minor · Moderate · Major · Critical · Catastrophic | `Pages/38-Classification Code.md` §4; `Pages/07-Sorrow Entities.md` line 64 |

Three faults follow, and each one has a name:

**The pair is in the template's order.** `Rank (Numeral)`, never `Numeral — Rank`. The code reads
`SE-C-IIIβ-014`; the row reads `Fragment (III)`.

**Word and symbol agree with each other and with the `Designation` field.** `Fragment (IV)` is not a
filing, it is two filings. `C-IIIβ-014` fixes both the rank and the potency, so the row has nothing
left to decide.

**A descriptor is a phrase, twelve words at most, with no full stop.** *"Self-aware, ancient, hungry"*
is a descriptor. *"Self-aware, and aware of the watching: the cycle it runs is the sign of it, and it
has never once been recorded as surprised to find itself alive again"* is a paragraph that has been
put in a cell by mistake — the behaviour belongs in `Behavior`, where it already is.

## 3. What the descriptor is not

It is **not** a second answer to the row's question. `Coherence` asks *how formed is this?* and the
descriptor says what that formation looks like in this one; it does not say what the holding does,
what it wants, or why it exists.

It is **not required.** 175 coherence cells carry the value alone and are correct. A holding whose
rank is the whole truth about its coherence does not need a phrase bolted on to look finished.

It is **not** a place to save a sentence that was cut from the prose. If a clause is worth keeping,
it is kept in the section that owns it; the table is not an overflow.

## 4. Where the fault is measured

`check_secc_shape.py` (gate 45) reads the `SECC Classification` table of all 301 dossiers, matches
both rows against the template's shape, cross-checks each symbol against the dossier's own
`Designation` code, and counts descriptors that have grown into sentences. It reports the number of
codes it cross-checked, so a check that matched nothing is visible rather than green.

It is registered in `how_finished.py` as *"SECC answers one question per row (R-51)"* and invoked by
`tools/gate.sh` — which `O-37` now requires of every gate the archive cites.
