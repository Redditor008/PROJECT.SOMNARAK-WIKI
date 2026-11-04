# R-48 — A Gauge Must Change An Instruction

**Stated by the archive owner, 2026-11-04:**

> *"WHAT THE USED OF HP ON RELIC SE THAT WONT USED THE HP, YES POSSESSION CAN USED THE HP SO
> FOR RELIC SE THAT WILL NEVER BREACH FIRST ERASE THE [HP] AND TRANSFORMS THE HP NUMBER INTO A
> MEANINGFUL GAUGE SO WHAT GOOD USED THE GAUGE THAT IS NOT USED FOR SE HP SO THINK OF THAT"*

## 1. What HP is for, and why it is wrong here

`HP` means one thing: **there is a number, it can be taken to zero, and at zero the thing stops.**
That is a suppression mechanic. It exists so a Warden knows when a breach is over.

A relic that never breaches is never suppressed. Nothing takes it to zero. At zero, nothing
happens — not because the scale is gentle, but because **there is no event that zero refers to.**
The number is not a bad gauge. It is a number with no referent, which is worse, because it looks
like information.

**Measured 2026-11-04, before this rule:** all **141** non-possession relic dossiers carried
`Sorrow Gauge [HP]`, and **all 141 read at their own ceiling** — `506/506`, `653/653`, `500/500`,
`420/420`. Not one of them had ever read anything else. A meter pinned at maximum has never been
read by anybody to decide anything, and a page that has never been read to decide anything is
decoration with a number in it.

## 2. The answer: what a gauge is for

**A gauge earns its ink only at a band boundary that changes an instruction.**

That is the whole test, and it is why HP works on a subject: at zero the instruction changes from
*hold the perimeter* to *the perimeter is gone*. If crossing a line changes nothing the file says
to do, the line is a decoration.

So a relic's gauge is not a health bar. It is **the state meter that tells a Warden whether the
procedure in this file is still the right procedure.**

Three bands. Three instructions. In ascending order:

| band | what it means | what the file must say changes |
|---|---|---|
| **under `a`** | the holding is inside ordinary tolerance | the handling as written stands, and nothing is added |
| **from `b`** | the holding is carrying more than ordinary tolerance | one named thing is added, widened, witnessed or rotated |
| **from `c`** (the ceiling) | the holding is at what it can carry | handling stops, and the file names who may lift that |

**The ceiling is a decision, not a death.** Nothing dies at the top of a relic's gauge. What
happens is that the file stops being permissions and becomes a prohibition, and one named
authority is left able to reverse it.

## 3. The measure follows the Element

The gauge is named for **what the holding is made of**, which the dossier already files in its
`**Element**` row. The name is not chosen for flavour; it is what the number physically reads:

| Element | the gauge is | what it reads |
|---|---|---|
| **Grudge** | **`[Pressure]`** | force pushed against a boundary — how hard the thing leans on what is holding it |
| **Weight** | **`[Load]`** | mass carried on a support — how much it is holding up, and how much more it can take |
| **Lament** | **`[Depth]`** | how far down the grief has gone — the distance from the surface, not the volume |
| **Void** | **`[Saturation]`** | how much absence has been poured in, until there is no room for anything else |

Four elements, four measures. The bracket is a verdict about **what kind of strain this is**, so a
Warden reading `[Load]` and a Warden reading `[Depth]` are being told different things about what
will happen at the ceiling — which is the point of naming it at all.

## 4. Why the number never moved, and what the bands do about it

A relic in this archive does not discharge. It accumulates — that is the whole cosmology, and it
is why every one of the 141 read full.

So the bands are not a future ladder. Most of these files open **already at their ceiling**, and
the band clause is the place where the file says **what the ceiling cost.** The three bands still
have to be written, because a Warden who has never seen the thing below its ceiling still needs
to be told what the lower bands would have looked like — and because the handful of holdings with
a real discharge (a rite that empties them, a season, a flood) do move, and their files use all
three.

## 5. The row

```text
| **Sorrow Gauge [Pressure]** | 340/600 — read at the vault door as force against the frame,
both readings taken a minute apart. Under 200 the handling in this file stands as written and
nothing is added. From 200 an outside reader stands at every watch and signs the pair. From 600
the vault is not entered, and only the Standing Order may lift that. |
```

Five things, and the gate checks all five:

1. **no `[HP]`** — the label is gone from a thing that is never suppressed;
2. **the bracket is one of the four measures**, and it matches the `Element` row;
3. **the number** is written `value/ceiling`, as before — the ceiling does not change;
4. **what it reads**, in this file's own terms, and where it is taken;
5. **three band thresholds, ascending**, with what changes at each, and the third being the ceiling.

## 6. Possession is the exception, by the owner's word

> *"YES POSSESSION CAN USED THE HP"*

Possession is the one relic type that gets inside a person. There is something to lose and a
number that can reach zero, because the thing that falls is the *bearer* — so `Sorrow Gauge [HP]`
stays, and two dossiers keep it: `SE-N-IIβ-270` and `SE-O-Iα-108`.

**Breaching relics also keep HP.** A relic that can breach is suppressible, and suppression is
exactly what HP is for. Measured at the rule's making: 8 relics can breach (`Can breach via
Expansion` ×4, an annexation, an overrun, a corrupt-breach, and one device-hazard), and all 8
keep `[HP]`.

Everything else — **133 dossiers** — is non-breaching and converts.

## 7. What this does not do

- It does not change a single ceiling. `506/506` keeps its 506; only what the number *means*
  changes.
- It does not invent a current reading. Where a file read at its ceiling it still reads at its
  ceiling, and the band clause now says what that costs.
- It does not touch subjects. A subject's cost is a work session, already governed by `R-44`.

## 8. The gate

`tools/auditors/check_relic_interaction_damage.py` and `check_gauge_chain.py` remain as they
were. The new reading is `tools/auditors/check_relic_gauge.py` (gate 93):

- fails any **non-breaching, non-possession relic** that still carries `[HP]`;
- fails a bracket that is not one of the four measures, or that disagrees with the `Element` row;
- fails a row with fewer than **three ascending band thresholds**;
- fails a row with no reading clause;
- fails a **subject** or **breaching relic** that has lost its `[HP]`;
- fails a **possession** that has lost its `[HP]`.

## Owner direction

Batch 194, 2026-11-04 — the instruction quoted at the top. Filed as **O-34** in
`OWNER_DIRECTIVES.md`.

## Rollout

| reading | on `[HP]` | on a state meter |
|---|---|---|
| before the rule | 141 | 0 |
| after batch 194 | **9** (2 possession + 7 breaching) | **134** |

By measure: **Depth 43 · Saturation 33 · Pressure 32 · Load 26.**
