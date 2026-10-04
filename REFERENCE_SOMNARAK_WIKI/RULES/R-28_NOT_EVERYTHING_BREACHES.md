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
- The `## Breach Behavior` **heading is left alone** where it exists. Four document builders key off
  that string as a section boundary, and renaming it would break generated output for a cosmetic
  gain. The heading is a container; the type line inside it now says what the event is.

## Enforcement

`gate.sh` runs `tools/breach.py` and refuses the commit if any floor is unmet, so the balance cannot
regress silently as new dossiers are written.
