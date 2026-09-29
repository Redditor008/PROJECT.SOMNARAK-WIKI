# Containment Levels

> *“The gauge does not measure time; it measures the facility's patience running out.”*

**Containment Levels**  [격리 과부하 등급]  (_Gyeokri Gwabuha Deunggeup_), commonly referred to as **Mugenhan Meltdown Levels**, represent the facility-wide stability gauge that escalates throughout an operational shift.

Every time a specialist completes a work session with a [Sorrow Entity](07-Sorrow%20Entities.md), the meltdown gauge fills by one segment. When the gauge fills completely, the facility advances to the next Meltdown Level, triggering random containment cell overloads and summoning hazardous [Ordeals](10-Ordeals.md).

```text
+========================================================================+
| SOMNARAK - CONTAINMENT & MELTDOWN LEVELS                               |
+------------------------------------------------------------------------+
| Overload Scale         | Meltdown Level I to Level X (10 Tier Gauge)   |
| Advance Mechanism      | Fills by 1 segment per completed work session |
| Hazard State           | Random Cell Overloads with 60-Second Timers   |
| Failure Penalty        | Lumen Drain & Entity Escape Counter Reduction |
| Ordeal Correlation     | Dawn (Level II-III) - Noon - Dusk - Midnight  |
+========================================================================+
```

## Contents

- [1 The Meltdown Escalation Gauge](#1-the-meltdown-escalation-gauge)
- [2 Meltdown Levels 1 through 10 Breakdown](#2-meltdown-levels-1-through-10-breakdown)
- [3 Cell Overload Mechanics and 60-Second Timers](#3-cell-overload-mechanics-and-60-second-timers)
- [4 Overload Mitigation and Dispatch Prioritization](#4-overload-mitigation-and-dispatch-prioritization)
- [5 Interaction with Ordeal Incursions](#5-interaction-with-ordeal-incursions)
- [6 Gallery](#6-gallery)
- [7 See also](#7-see-also)

## 1 The Meltdown Escalation Gauge

The Meltdown Gauge is prominently displayed at the top of the Warden's HUD:
- **Work Segments:** The gauge requires a specific number of completed work sessions to advance (typically 4 to 8 works per level depending on facility size).
- **Escalating Pressure:** With each higher meltdown level, the number of simultaneous containment cell overloads increases.
- **Relic Exemption:** Tool Relics utilizing the Two-Work-Type Rule (such as [28-The Echo Compass](28-The%20Echo%20Compass.md)) do not generate meltdown overloads, though working with them still advances the gauge.

## 2 Meltdown Levels 1 through 10 Breakdown

| Meltdown Level | Overloaded Cells | Triggered Ordeal Event | Operational Threat Level |
|---|---|---|---|
| **Level I** | 1 Cell | None | Negligible; routine orientation. |
| **Level II** | 2 Cells | First Watch (Dawn) Ordeal | Low; minor corridor pests. |
| **Level III** | 3 Cells | None (or Dawn on late days) | Moderate; cell management required. |
| **Level IV** | 4 Cells | Second Watch (Noon) Ordeal | High; combat squads required. |
| **Level V** | 5 Cells | None | Substantial; multiple cell alarms. |
| **Level VI** | 6 Cells | Third Watch (Dusk) Ordeal | Critical; multi-floor breaches possible. |
| **Level VII** | 7 Cells | None | Extreme; facility near boiling point. |
| **Level VIII** | 8 Cells | Tide Watch (Midnight) Ordeal | Lethal; existential crisis. |
| **Level IX** | 9 Cells | Simultaneous Multi-Breaches | Catastrophic; absolute lockdown. |
| **Level X** | 10+ Cells | Total Resonance Collapse | Terminal; facility-wide cascade breach. |

## 3 Cell Overload Mechanics and 60-Second Timers

When a meltdown level triggers, crimson overload glyphs attach to random containment chambers:
1. **The 60-Second Countdown:** A glowing red timer begins ticking down from 60 seconds above the overloaded cell.
2. **Required Action:** The Warden must order a specialist into the cell before the timer expires. The moment an operative enters the chamber, the overload is cleared.
3. **Failure Penalty:** If the timer reaches zero:
   - A substantial chunk of harvested [Lumen](33-Lumen.md) energy evaporates instantly.
   - The entity's **Mugenhan Escape Counter** is reduced by 1. If reduced to zero, the entity immediately breaches into the hallways.

## 4 Overload Mitigation and Dispatch Prioritization

Experienced Wardens employ several tactical doctrines to mitigate overload risks:
- **Clustered Dispatch:** Group specialists near high-risk containment cells prior to triggering the final work session that advances the meltdown gauge.
- **Work-Type Compatibility:** When clearing an overload on dangerous entities, choose the protocol with the highest success rate to prevent secondary agitation.
- **Sacrificial Clearance:** If a high-risk entity overloads and no qualified specialist is nearby, dispatching a rookie recruit to reset the timer can save the facility from a full Sovereign breach, even if the rookie perishes inside.

## 5 Interaction with Ordeal Incursions

Meltdown levels serve as the heralds for Ordeal incursions:
- Instead of random cell overloads, specific milestone levels (II/IV/VI/VIII) replace or supplement overloads with sudden Ordeal invasions.
- Wardens must quickly decide whether to dispatch personnel to clear ticking cell timers or concentrate firepower on roaming Ordeal monoliths.

## 6 Gallery

![Meltdown Gauge Display](https://via.placeholder.com/320x180?text=Meltdown+Gauge+HUD)
![Overloaded Cell Alarm](https://via.placeholder.com/320x180?text=Overloaded+Cell+Glyph)
![Emergency Dispatch Action](https://via.placeholder.com/320x180?text=Emergency+Dispatch)

*Left: meltdown HUD gauge; Center: 60-second overload warning glyph; Right: emergency response dispatch.*
---

## 7 See also

- [16-Daily Cycle](16-Daily%20Cycle.md) — operational shift architecture and daily phases
- [10-Ordeals](10-Ordeals.md) — timed incursion events across the four watches
- [19-Lumen Surge](19-Lumen%20Surge.md) — energy harvesting and quota loss penalties
- [21-Game Mechanics](21-Game%20Mechanics.md) — core facility game loop
