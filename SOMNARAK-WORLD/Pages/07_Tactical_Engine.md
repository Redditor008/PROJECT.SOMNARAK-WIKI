# Tactical Engine — The Battle Rites

**Page ID:** `Pages/07_Tactical_Engine`  
**Archive Path:** `SOMNARAK-WORLD/Pages/07_Tactical_Engine.md`  
**Parent Archive:** [[SOMNARAK-WORLD](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/tree/arena/01a0b699-project-somnarak-wiki/SOMNARAK-WORLD "SOMNARAK-WORLD")]  
**Backing Codices:** `Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md` + `Tactical_Combat_Engine/` + `GAME_BATTLE/`

```text
+========================================================================+
| TACTICAL ENGINE — BATTLE RITES                                         |
+------------------------------------------------------------------------+
| Phase Doctrine | Tension → Clash → Resolution                          |
| Turn Bands | Short 10 / Medium 16 / Long 20+ turns                     |
| Grids | 10-node grid with Range Bands                                  |
| Watch States | Green / Amber / Red (see 04_Lumen)                      |
| Core Loop | Work → M.A.W. → Suppression → Log                          |
+========================================================================+
```

## Summary

Combat in Somnarak is **containment as conversation** — each turn is a Work, a veil-stone, a gauge check, and a psychological beat. The engine is a decoupled state machine documented in `Tactical_Combat_Engine/README.md` and playable in `GAME_BATTLE/`.

## Description — The Three Phases

From `SOMNARAK_BATTLE_SYSTEM.md`:

1. **Tension (긴장):** Identify threat (entity / Fractured / Ordeal / Echo-Core Crisis), assess Sorrow Gauge and SECC, position, check M.A.W.
2. **Clash (충돌):** Perform Work, activate M.A.W., deploy specialized weaponry; entity responds per `Behavior` and per `Pages/08_Relic_Entities.md` if stationary.
3. **Resolution:** Containment, pacification, Fracture, or death — logged with gauge residue and lingering pressure.

Each phase tracks Han density, atmospheric shift, Fracture warnings, and environmental corruption.

## Information — System Registry

- **Battle Lengths:** Short 10 (minor), Medium 16 (standard), Long 20+ (Sovereign / Core Suppression).
- **Damage Elements:** Grudge (Crimson), Lament (Blue), Void (Pale White), Weight (Black) — see `SOMNARAK_ENTITY_CODEX.md` elemental matrix.
- **Ordeal Handling:** Ordeals are suppressed via Border Lead protocols, not Worked (see `Pages/06_Mugenhan_and_Ordeals.md`).
- **Playable Spec:** `Tactical_Combat_Engine/WHAT_CAN_BE_DONE.md` — JSON schema, formulas, GBS decoupled state, 16 `GAME_BATTLE/` scenarios and realization meltdowns.

## Operational Notes

- **Reading Work:** Gauge fall ≠ cure — sorrow remains, entity is calmer not healed.
- **Relic exception:** Relic Entities expand rather than breach — quarantine, do not pursue (see `08_Relic_Entities.md`).
- **Cycle law:** 1,778 cycles exist ONLY in R.D./Absolvohan — external frontiers use Year 4,238.

## Related Pages

- `02_Behavior.md` — Work Types and family resonance.
- `05_MAW.md` — equipment costs and rejection.
- `Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md` — real tactical codex.

---
*Backing is a real codex — `SOMNARAK_BATTLE_SYSTEM.md` + 16 `GAME_BATTLE/` scenarios.*
