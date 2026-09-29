# Tactical Engine

> *“Every battle is a conversation between sorrow and survival.”*

**Tactical Engine** is the battle rites system for containment encounters.

Tactical Engine is the battle rites system that translates the Watch into executable Turns. Three phases — Tension (identify threat, assess Gauge and SECC, position on a ten-node grid with Range Bands), Clash (perform Work, activate M.A.W., deploy one of sixteen systems), Resolution (containment, pacification, Fracture, or death) — govern every containment encounter, whether the encounter is a Sorrow Worked for Lumen, an Ordeal suppressed for Veil, or a Reverberation resolved for a Floor. Turn bands — Short 10 (minor), Medium 16 (standard), Long 20-plus (Sovereign) — and damage elements — Grudge, Lament, Void (where one percent Pale equals five percent of Max HP), Weight — are not flavor but arithmetic, as priced in `SOMNARAK_WARDEN_GUIDE.md` and `Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md` and as executed through the decoupled state machine and JSON battle schema documented in `Tactical_Combat_Engine/README.md` and `GAME_BATTLE/`’s sixteen scenarios.

Work resolution is the tactical analogue of dossier Behavior. Viderehan  [비데레한]  (Biderehan) for Observation and Clarity, Ferrehan  [페레한]  (Perehan) for Endurance and Resilience, Flerehan and Pugnahan for Subjects only — a division that is 100.0 percent compliant across 283 entities — determine which Turn Bands are legal that encounter; Pressure interaction determines which Pressures will be dealt and which M.A.W. resistances will be checked; Watch accounting determines whether the Work increments Lumen (roughly 8 LU for a successful Viderehan on a Whisper Place such as `SE-C-IIIβ-014`) or raises Fracture and Containment Level (Tranquil through Rupture). The state machine therefore treats a Relic Place that expands rather than breaches differently from a Subject that breaches; the Relic is quarantined — seal sectors, stabilize Lumen at 5,000 LU per floor and 40,000 LU primary, resume Viderehan and Ferrehan from threshold — while the Subject is suppressed, a distinction that keeps Tactical from becoming merely a damage race.

Full doctrine lives where the system can be run, not merely read. `Tactical_Combat_Engine/README.md` documents the JSON schema that sixteen scenarios instantiate, and each scenario prices Han density, atmosphere, and Fracture warnings per Pressure band so that a Warden who learns Pressure Types before M.A.W. before Research, as [21-Game Mechanics](21-Game%20Mechanics.md) teaches, can translate a dossier’s story into a Turn without forgetting the city. To practice the engine is to rehearse the day: see [16-Daily Cycle](16-Daily%20Cycle.md) for the four Watches that the engine executes, [17-Pressure Types](17-Pressure%20Types.md) for the four Pressures it prices, and [31-Behavior](31-Behavior.md) for the tables that make the dosing of each Turn falsifiable rather than theatrical. The same filing is maintained in `SOMNARAK_ENTITY_CODEX.md`, `CANONICAL_METRICS.json`, and `CANONICAL_REGISTRY.json`, where Origin, Rank, Potency, Element, and Manifestation are kept sortable for watch planning across the sixteen battle systems and forty-four Master Codices.

```text
+========================================================================+
| TACTICAL ENGINE — BATTLE RITES                                         |
+------------------------------------------------------------------------+
| Phases                   | Tension to Clash to Resolution              |
| Turn Bands               | Short 10 · Medium 16 · Long 20 and beyond   |
| Grid                     | 10-node and Range Bands                     |
+========================================================================+
```

## Phases

- **Tension** — identify threat, assess Gauge and SECC, position
- **Clash** — perform Work, activate M.A.W., deploy systems
- **Resolution** — containment, pacification, Fracture, or death

Each turn tracks Han density, atmosphere, and Fracture warnings.

## System

Battle lengths are Short (10, minor), Medium (16, standard), Long (20 and beyond, Sovereign). Damage elements are Grudge, Lament, Void, Weight.

The decoupled state machine and JSON schema are in `Tactical_Combat_Engine/README.md` and `GAME_BATTLE/` — 16 scenarios.

Relic Entities expand rather than breach — quarantine, do not pursue.

## See also

- [17-Pressure Types](17-Pressure%20Types.md)
- [34-M.A.W. Equipment](34-M.A.W.%20Equipment.md)
