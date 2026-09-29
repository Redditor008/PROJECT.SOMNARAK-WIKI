# Tactical Engine

> *“Every battle is a conversation between sorrow and survival.”*

**Tactical Engine** is the battle rites system for containment encounters.

```text
+========================================================================+
| TACTICAL ENGINE — BATTLE RITES                                         |
+------------------------------------------------------------------------+
| Phases | Tension → Clash → Resolution                                  |
| Turn Bands | Short 10 · Medium 16 · Long 20+                           |
| Grid | 10-node · Range Bands                                           |
+========================================================================+
```

## Overview

36-Tactical Engine is a mechanics article that presents a 4-row infobox (Work Types 4 Ferrehan/Flerehan/Pugnahan/Viderehan, Pressures 4 Grudge/Lament/Void/Weight, Watches 1–4, Archive WARDEN_GUIDE) and 3 sections (Work Resolution, Pressure Interaction, Watch Accounting) plus See also to 17-Pressure Types and 16-Daily Cycle. The article's data is sourced from `SOMNARAK_WARDEN_GUIDE.md` (16 battle systems) and `GAME_BATTLE/` (16 scenarios), `Sorrow_Entities/README.md` (Four Han Affinities), and `Master_Codices/03_Systems_Combat_Engine_and_Physics` (Lumen tally ~8 per Viderehan on SE-014, Fracture on failure).

## Phases

- **Tension** — identify threat, assess Gauge and SECC, position.
- **Clash** — perform Work, activate M.A.W., deploy systems.
- **Resolution** — containment, pacification, Fracture, or death.

Each turn tracks Han density, atmosphere, and Fracture warnings.

## System

Battle lengths are Short (10, minor), Medium (16, standard), Long (20+, Sovereign). Damage elements are Grudge, Lament, Void, Weight. The decoupled state machine and JSON schema are in `Tactical_Combat_Engine/README.md` and `GAME_BATTLE/` (16 scenarios).

Relic Entities expand rather than breach — quarantine, do not pursue.

## See also

- `31-Behavior.md`
- `34-M.A.W. Equipment.md`
- `Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md`
