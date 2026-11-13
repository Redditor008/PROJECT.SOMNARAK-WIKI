# R-50 — Some Holdings Have One Thing They Do

**Stated by the archive owner, 2026-11-05:**

> *"You Probably Need To Invent New Effect For OUR SE That Basically An Individual Specific SE
> Effect Can Happen In Any Ways Of Forms [When Breach Happen [Any Kind], Finished Working The SE,
> Special Effect Of SE And More] And It Will Be Only On 45% Of The SE"*

## 1. The gap this closes

Three rows now describe a holding from the outside: `**Work Damage**` says what a session costs,
`**Work Gift**` says what it pays back (`R-49`), and `**Activation threshold**` says what makes it
move. None of them says **what this one does that no other one does.** A reader who has finished a
dossier can say how it is worked and still not be able to say what will happen if it gets out.

**`**SE Effect**` is that sentence**, and it is the only row in the Archive that is not derived from
a rule — it is the holding's own law.

## 2. Only 45 % of them have one

**135 of the 301 dossiers.** A holding with no individual effect is not a defective dossier; it is a
holding whose behaviour is fully described by its grade, its element and its work reading. The
plain, well-behaved holdings are the majority on purpose: a bestiary where every entry has a unique
power is a list of exceptions, and nothing can be an exception.

**The 45 % is a constant, not a per-file judgement** — the same discipline as `R-49`'s 65/25/10. The
gate holds the count exactly, and the selection is stratified by wing and grade so the 135 are not
all one colour.

**Absence is the reading.** A dossier without the row is a holding with no individual effect; the
row is not written as `None`. That is the opposite of `R-49`, and deliberately: a work verdict is a
fact about every session and has to be stated, while an individual effect is a fact about one
holding and states itself by being there.

## 3. When it fires — six triggers, and they are the dossier's own

The effect fires on an **occasion**, and the occasion is never invented: it is read off the
`**Activation threshold**` row and the `**Entity Type**` row that every dossier already carries.

| trigger | what it means | where it comes from |
|---|---|---|
| **the breach** | any breach, of any kind — escape, expansion, manifestation, possession taking the wheel | `Entity Type` naming a breach |
| **the counter** | the T Counter reaches zero, or the last ignored condition is ignored | `Activation threshold` counting conditions |
| **the wall** | the gauge reaches its ceiling | `Activation threshold` reading a gauge |
| **the contact** | the first touch, the first reading, the first word spoken to it | `Activation threshold` reading a contact |
| **the completion** | a work cycle or a handling finishes | the work loop |
| **the refusal** | a barred work is attempted, or a watch is refused | the `Refusal` row |

**These six are the minimum, not a form.** A holding whose effect needs a seventh occasion writes
it and says so; what may not happen is an effect with no occasion at all, because an effect that can
happen at any time is not an effect, it is a hazard.

## 4. The shape

```text
| **SE Effect** | **On the wall** — {the holding's own law, in its own terms}. {what it lands on, when the record says} |
```

Three parts:

1. **The trigger**, bold, from §3, opening with `On`.
2. **The law** — a sentence that is already in the dossier and is **not** a restatement of the
   pressure, the work reading or the damage clause. It is what the thing does.
3. **What it lands on**, where the record says — the worker, the room, the district, the record
   itself. Not every effect lands on a person, and the ones that land on a room are the ones that
   make a containment decision.

**The law must be the file's own sentence.** The gate checks the first forty characters of the
effect body against the dossier text, verbatim. That is what makes this row impossible to fill from
a template: an invented sentence that is not in the record fails the gate.

## 5. What it is not

- **Not a second `Work Damage`.** That row is a band; this is a statement.
- **Not the gauge.** An effect that moves the gauge is a work reading and belongs in `R-48`.
- **Not a power on a relic.** A relic's contact is continuous and priced by the second (`R-47`);
  its `**SE Effect**`, where it has one, fires on **the contact** or **the breach**, never on a
  completion it does not have.
- **Not a percentage, not a cooldown, not a dice roll.** The occasion is a state of the world, not
  a chance.

## 6. What the gate enforces

`tools/auditors/check_se_effect.py`:

- exactly **135 of 301** dossiers carry the row;
- the trigger is one of the six and opens with `On`;
- the effect body is at least twelve words and is **verbatim in the dossier**;
- no two dossiers carry the same effect body;
- no `%`, no cooldown, no dice in the cell;
- a dossier with the row has an `**Activation threshold**` that could produce it.
