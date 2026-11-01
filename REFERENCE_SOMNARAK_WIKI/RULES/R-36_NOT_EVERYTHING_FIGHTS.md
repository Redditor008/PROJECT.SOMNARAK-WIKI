# R-36 — Not Everything Fights

**Stated by the archive owner, 2026-11-01:** *"Can you fix a lot of SE that should never have combat
section and escape section, and HP and counter and combat move that need to have a logically fixed —
logically meant the fix has to go into the logic path, not the template path."*

## The problem

Measured the day this rule was written: **301 of 301 dossiers carry `## Combat Record`.** Every one
of them carries `### Combat Actions`, a `Han Pressure [ATK]` line, `Battle Length`, `Threat Role`,
and a five-row action table whose categories include `[**Attack**]` and `[**Ultimate**]`.

For a third of them the file's own text denies the section it is carrying. The Sorrow Fountain's
basin **has never moved**. Apocrypha is a frozen patch of ground holding the outline of nothing. The
Portcullis says in its own Battle Phases that *the Door does not strike at anyone*. Hums records in
its Resistance row that *the stone does not attack, and the two resistances are recorded because the
encounter sheet has the field* — the sheet, not the entity. Then the same dossiers file
`{ *The Ice Shard* [**Attack**] }`, `Han Pressure 3–10 per hit`, and `Battle Length: Short — 10
turns`.

That is generator output wearing a bespoke costume. It is the same defect `R-28` found in the breach
cell, in a different section: the prose was corrected one row at a time while the scaffolding stayed
and kept asserting an encounter that never happened.

## The test — a fixed object is not a licence to delete a fight

A dossier converts **only** where all three of these are true of its own text:

1. **It cannot close distance.** The `Movement` row records `Stationary`, `Fixed`, `Motionless`,
   `Seated`, `Recumbent`, or `Rooted`, or the body states in terms that it has never moved.
2. **It does not strike.** The record says it does not attack, has never been fought, has never
   struck, or the combat text itself denies the move it is filed under.
3. **Nothing on the file records pursuit, aim, or a blow.** No range, no target selected, no
   strike landed — not in the Combat Record, not in Behavior, not in the Story Log.

An entity that moves, hunts, or aims keeps its Combat Record whatever else is true of it, and an
entity whose moves were directed by the owner — the Walking District's two event-form moves — keeps
them. **A conversion is never made to hit a number.** If the three tests are not all satisfied, the
combat section stays and the work is to fix its numbers instead.

## The replacement — `## Contact Record`

The section is replaced, not emptied. Its function in the dossier is *what happens when a person
meets this thing*, and that function survives even when the fight does not.

**What a Contact Record carries**

- **A reason line, first.** One or two sentences, in the dossier's own terms, saying why this file
  has no combat actions and what it has instead. It cites the movement row or the record's own
  denial. It is not a template sentence and no two read alike.
- **One `| Field | Value |` table**, in place of the double table. It keeps `Mode of presence`,
  `Perceptible to`, `Activation threshold`, `Sorrow Gauge [HP]`, `Starting Sorrow Gauge`, `Valid Work
  Types`, `Location`, and `Resolution Condition`. It **drops** `Speed` (a fixed thing has none),
  `Han Pressure [ATK]` (nothing is being hit), `Battle Length` (there are no turns), `Threat Role`
  (there is no encounter), and the coherence and potency *modifiers*, which restate the
  classification the dossier already carries.
- **`### Contact Events`** in place of `### Combat Actions`. Three to five rows, each one drawn from
  what the file already records happening to a person: the register, the exposure, the refusal, the
  overload. Categories come from the entity's own behaviour — `Register`, `Exposure`, `Refusal`,
  `Overload`, `Contagion`, `Attachment` — never `Attack`, `Ultimate` or `Barrage`. Numbers stay only
  where the dossier already has them (a Composure cost, a gauge threshold, a count of what was
  taken); nothing is converted into damage against a target, because there is no target.
- **`### Watch Sequence`** in place of `### Battle Phases`, with the same three movements — what is
  confirmed, what the watch does, how it closes — written as a watch rather than a clash.
- **`### Consequences` stays**, unchanged. It was never the template's.

**The Sorrow Gauge stays and keeps its band.** `R-36` removes an attack line, not the entity's
pressure meter: the Gauge is what the Behavior thresholds and the resolution condition are read
against, and every converted dossier already uses it that way. `Sorrow Gauge [HP]` therefore remains
in the table, inside its tier band, under `R-22`-style checking by
[`check_stat_bands.py`](../../tools/check_stat_bands.py) — which now treats a Contact Record as
requiring a Gauge and no `Han Pressure [ATK]` row at all.

## What a conversion changes outside the dossier

- **`tools/wikistd.py`** — the ninth-section parity test accepts `## Contact Record` in the stats
  slot, because the slot's purpose is *what meeting this thing does*, not the word "combat".
- **`tools/check_stat_bands.py`** — a Contact Record dossier is checked for Gauge-in-band and exempt
  from the ATK row; a dossier with neither is still a failure.
- **The Side Codex** that mirrors the dossier — its `Gauge / Pressure` row loses the `per hit` band
  and says what the entity does instead, e.g. `462/462; starts 35–50% · Lament — no attack pattern`.
- **The Conversion Guide** — a Contact Record maps to L Corp Basic Info and a filed **absence** of
  Escape Information: there is no movement, no strike, and no breach to convert. It is not a short
  Combat Record and it is not read as one.
- **The prose everywhere else.** A converted dossier's Behavior, Consequences, Field Use Record and
  Observation Log are swept for a strike, an aim, a pursuit or a damage figure that the record no
  longer supports. `R-28`'s lesson applies: the section is the smallest part of the change.

## Enforcement

`gate.sh` fails on an under-band Gauge in either shape, and `check_stat_bands.py` reports a Contact
Record that still carries a `Han Pressure [ATK]` row as a contradiction. The shape is not policed by
a quota, because there is no floor to meet: an entity either satisfies the three tests or it does
not, and the dossier says which.

## The queue

The first sweep under this rule converts the fixed things whose own text already refuses the fight.
The remaining candidates are named in the CHANGELOG entry that opens the sweep and are converted in
filed order, each on its own evidence, never in a batch whose size was chosen before the files were
read.
