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
- **Possession** — corruption that works on the agent rather than on the room. The
  holding does not move and does not need to: it takes the person who works it, and
  the person becomes the vector. The native comparisons are the Singing Machine,
  which calls its worker back to it, and the Cherry Blossoms, which keep the one who
  tends them.
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

## Possession (2026-11-01)

**Stated by the archive owner:** *"Now add in Possession — it is still corruption, but it
affects the agent."*

Corruption is written as a property of the room: the zone warps, the entity stays. That
covers a holding which changes the place it occupies. It does not cover the holding that
leaves its room untouched and takes the person working it — the worker who will not hand
over the post, who answers the voice and is answered back in their own voice later, who
stops being able to put the load down. Those files were being written as breaches because
the word *vector* had nowhere to go.

**Possession is still corruption.** The difference is the direction of the effect: a
corrupted zone changes what is inside it, and a possession changes the one who came in and
then moves the change out through them. Nothing leaves containment, which is why the
category belongs beside corruption and not beside escape.

**The evidence test.** The dossier's own text must show the agent acting under the
holding: a worker who declines to hand over, who answers and is retained, who carries the
burden out of the room, who becomes useful and reluctant. A file that only says the worker
is frightened, injured or unwell is not a possession and is not reclassified on the
strength of it.

**What a possession record carries.** The usual non-breaching reclassification — the
`Entity Type` cell states the category and cites the dossier's own evidence, `## Breach
Behavior` becomes `## Containment Event Behavior`, the `Breach type` rows become `Event
type (non-breach)` — plus two rows a corruption record does not need:

- **Who it takes** — the agent, and the selection rule if the file records one. An Atlas
  takes the conscientious first, and the state presents as competence.
- **Recovery** — what returns the person. This is the row that makes the category useful
  in play: a corrupted zone is closed, a possessed agent is *brought back*, and the file
  must say how. Atlas is the worked example: the relief interval is not waivable, the
  incoming pair remove the worker physically, the removal is recorded as a holding event
  and not as misconduct, and nineteen such removals stand in nine years.

The event table is a `### Possession Events` table with the same four columns as a contact
record — what the holding does, what the watch carries out, and what the reading is — and
the watch sequence closes on the file's own suppression condition. A possession record
never says *contain* where it means *recover*.
