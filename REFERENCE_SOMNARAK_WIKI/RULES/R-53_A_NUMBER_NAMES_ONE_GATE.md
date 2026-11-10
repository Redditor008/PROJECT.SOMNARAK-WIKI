# R-53 — A Number Names One Gate

**Stated by the archive owner, 2026-11-05:**

> *"If You can find other Command That You Forgotten/Ignore"*

## 1. What the hunt found

Three commands were not lost but **mis-stated**, which is harder to notice than a missing one:

**`O-08` claimed work was undone that was done.** It read *"OPEN — 131 of 143 relic dossiers still
carry Work Types"*. The gate had been reading **0** since batch 202, ten batches earlier. The order
was stale in the safe-looking direction — it under-claimed — and nothing compares an order's status
to the gate that measures it.

**`O-14` claimed a partial that no gate can reach.** Subject shape diversity says four shapes must
exist across the subjects; the four shapes are not a recorded field. `**Physical Form**` is `Mixed` on
104 of 158 subjects and free prose on the other four, so classifying them would mean inventing a
keyword scorer — the thing `R-15` forbids and batch 213 refused to do.

**Gate numbers named more than one gate.** Between batches 202 and 212 the archive began citing gates
by number with no register defining what a number meant. Four documents cited two different scripts
by the same number:

| number | claimed by | and by |
|---|---|---|
| `gate 92` | `check_relic_interaction_damage.py` | `check_gate_wiring.py` |
| `gate 93` | `check_relic_gauge.py` | `check_section_registry.py` |

Both citations were links to nothing. The numbers had been assigned batch by batch by whoever was
writing, and no two batches agreed.

## 2. The rule

**A gate number resolves to exactly one script, and the number is derived rather than chosen.**

`REFERENCE_SOMNARAK_WIKI/GATES.md` numbers every gate by **its position in `tools/gate.sh`** — the
order the build runs them. That is the only definition that cannot drift while the build stands: to
add a gate is to append a number, and to reorder the build is to renumber the register.

**Cite the script, not the number.** The filename is the identity and it is unambiguous. A number is a
convenience, and it is only correct if it matches the register.

## 3. A status is a claim

An order's `**Status:**` is measured, not remembered. Where a gate owns the order, the status cites
that gate and its current reading, and the reading wins:

- `**Checked by:**` names the script and its registered number.
- `**Status:**` states the number the gate prints, not the number that was true when the order was
  written.

When a gate reaches zero, the order reaches **DONE** in the same unit — as `O-08` now does.

Where an order genuinely cannot be measured yet, it says so and says why: `O-14` states that the four
shapes are not a recorded field and that closing it needs a schema change, not a sweep. **A PARTIAL
that explains itself is a finding. A PARTIAL with no number is a shrug.**

## 4. What is checked

`check_gate_numbers.py` (gate 49) reconciles `GATES.md` against `tools/gate.sh` in both directions and
fails on any prose citation whose number the register gives to a different script. Every count is
reported on both sides, so a check that matched nothing is visible rather than green.
