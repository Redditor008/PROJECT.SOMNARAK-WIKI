# R-28 — Not Everything Breaches

**Stated by the archive owner, 2026-10-05:** *"Can You Make Sure Not All SE is Breaching SE Because
We Have Category For It Like Corruption And Such … At Minimum 75% Of RE is Non-Breaching RE and At
Minimum 25% Of Normal SE Is Non Breaching And 50% Of O/P-SE Is Non-Breaching O/P-SE"*.

## The problem

Measured the day this rule was written: **of 302 entity dossiers, 285 declared themselves capable of
breaching.** 138 Subjects read *Can breach*; 83 Object/Places read *Can breach via Transform*. The
archive already has categories for everything a holding can do short of escaping — Corruption,
Expansion, Activation, Manifestation — and almost none of them were used in the Entity Type cell.

The inconsistency was not subtle. **72 of the 83 relic dossiers have no Breach Behavior section at
all** — they have an Activation Behavior section and a Stationary movement row — and still declared
*Can breach via Transform*. The cell was generator output, not a finding.

## The floors

| Group | Definition | Non-breaching floor |
|---|---|---|
| **RE** | a Tool Type is declared (I-Relic, O-Relic, A-Relic) | **≥ 75%** |
| **SE** | Subject, Time, Hazard, Phenomenon — no Tool Type | **≥ 25%** |
| **OP** | Object/Place with no Tool Type | **≥ 50%** |

`tools/breach.py` reports all three and exits non-zero if any floor is unmet.

## The evidence test — a quota is not a licence to relabel

A dossier may be reclassified non-breaching **only** where its own text already shows it does not
escape. One of:

1. No `## Breach Behavior` section — the dossier documents activation or expansion instead.
2. A `Breach type` of **Corrupt** (the zone warps; nothing leaves it) or an equivalent bespoke line
   recording that the entity relocates, spreads, lengthens or sounds without leaving containment.
3. A body that states in terms that it has never left, never pursued, or cannot move.

A dossier whose breach type is **Escape** is not touched, whatever the quota says. If the floors
could not be met from qualifying dossiers alone, the honest answer would be to report the shortfall
— not to relabel an entity that roams.

## The categories used instead

- **Activation only** — a relic that is used, not contained against.
- **Corruption** — the zone warps, degrades or turns; the entity stays in it.
- **Expansion** — it grows, spreads or lengthens in place.
- **Manifestation** — it appears where it appears and does not travel.

The replacement cell states the category and cites that dossier's own evidence, so no two read alike
(`R-23`: labels may repeat, values may not).

## What a reclassification changes inside the dossier

- The **Entity Type** cell states the category and cites that dossier's own evidence.
- Any `- **Breach type:**` line becomes `- **Event type (non-breach):**`, keeping its text, because
  that text was already describing a corruption or a transformation in place rather than an escape.
- Prose claiming a breach capability is corrected (`can breach and pursue` → what the dossier
  actually records).
- The `## Breach Behavior` **heading becomes `## Containment Event Behavior`** in a reclassified
  dossier. This was initially deferred on the grounds that document builders key off the string;
  the owner's follow-up instruction settled it — *"that also mean edit it Behavior + Combat Action +
  Operational Work Notes + Escalation Notes + everything under Field Use Record up to Entity
  Interaction Record"* — so the heading was renamed in all 36 affected files and
  `tools/auditors/sample_work_notes.py` was taught to accept either boundary.
- **Every dependent section is brought into line, not just the classification cell.** Behavior,
  Combat Record and Combat Actions, Operational Notes and Operational Work Notes, Escalation Notes,
  Consequences, M.A.W. Use Notes, Field Use Record, Observation Log, Registry Addendum and the
  Entity Interaction Record are all swept for language that asserts an escape the dossier does not
  record.

## Enforcement

`gate.sh` runs `tools/breach.py` and refuses the commit if any floor is unmet, so the balance cannot
regress silently as new dossiers are written.

## The consequential sweep (2026-10-05)

Reclassifying the cell alone would have left 716 lines across the 112 dossiers still describing a
breach. Three passes fixed them:

| Pass | What it corrected | Dossiers touched |
|---|---|---|
| 1 | section heading, `Breach Type` row, `Breach type` line, the stock *"is the event a breach, activation, or expansion"* sentences | 68 |
| 2 | every remaining use of *breach* as a noun or verb in prose — review requirements, operational interpretations, gauge-on-breach labels, M.A.W. use notes | 99 |
| 3 | the section's flavour quote and movement row where they asserted escape — *"X has broken free. Hunts personnel indiscriminately."* became an event call naming what the entity is actually doing | 26 |

Five lines survive the scan and are correct as written: they say the entity *expands rather than
escaping*, or *does not rupture or roam*. Those are the sentences the sweep existed to protect.

A flavour quote is now category-specific: a corruption event reads *"…is turning the zone it stands
in; nothing has left it"*, an expansion *"…is widening where it is; the boundary is moving, not the
entity"*.
