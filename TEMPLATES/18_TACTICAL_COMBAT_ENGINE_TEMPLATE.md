# 18 — TACTICAL COMBAT ENGINE TEMPLATE

**Template ID:** `T-18-TCE`  
**Generates:** `SOMNARAK-WORLD/Tactical_Combat_Engine/{{FILE}}.md`  
**Authority:** `SOMNARAK-WORLD/Tactical_Combat_Engine/README.md` + `SOMNARAK_BATTLE_SYSTEM.md` + `SOMNARAK_BATTLE_SYSTEM_STYLES.md` + `WHAT_CAN_BE_DONE.md` + Laws 6,8

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Tactical Combat Engine (TCE) is the playable implementation spec** — decoupled state machine, data schemas (Operative, Entity, Veil), 10-Node Spatial Grid, and math that makes `GAME_BATTLE/` scenarios executable.
- **10-Node Grid (N01–N10) is the spatial atom:** Line (N01→N10) with Cover, Entity Body, and Flank nodes. Movement costs AP. Range Bands 1–5 map to Node distance. Skewer firing through Cover uses falloff 100%→70%→50%.
- **The 4 P-Framework is mandatory for every combat spec:** Passives (P1), Panic (P2), Parry (P3), Posture (P4). Dual-Threshold Stagger: **60% Part Rupture** and **25% Meltdown** (or Composure 0).

---

## FILE NAMING

```
SOMNARAK-WORLD/Tactical_Combat_Engine/{{TOPIC}}.md
```

Example: `WHAT_CAN_BE_DONE.md` (roadmap + formulas + JSON schemas) or `GRID_BASTION_WARFARE.md` (illustrative example — no such file ships)

---

## SCAFFOLD

~~~markdown
# Tactical Combat Engine — {{TITLE_EN}} — {{KOREAN_TITLE}}

> *“{{Epigraph — the math that keeps a warder alive for one more breath.}}”*

**Engine ID:** `TCE-{{DOMAIN}}-{{NUM}}`  
**Author:** {{Research Lead Ayshuk / Tactical Analyst}}  
**Date:** Year {{4,23x}}  
**Status:** {{Playable Spec / Draft Schema / Roadmap}}  
**Dependencies:** `SOMNARAK_BATTLE_SYSTEM.md` + `SOMNARAK_BATTLE_SYSTEM_STYLES.md`

## I. SYSTEM THESIS

{{1 paragraph: what this engine piece governs — grid, AP economy, P-framework, stagger, M.A.W. modifiers, or JSON schemas. What it does NOT govern (point to other TCE files).}}

## II. MECHANICAL SPECIFICATION

### A. {{Mechanic Name}} (e.g., 10-Node Grid Topography)

{{2–3 paragraphs: Node definitions, Cover at N05, Entity Body at N07–N08, Flank vector, movement AP cost, range-band mapping.}}

| Parameter | Value | Note |
|---|---|---|
| Grid Size | 10 Nodes (N01–N10) | Line, not 2D board |
| Cover | N05 | Destructible, +2 DEF while held |
| Entity Body | N07–N08 | Part-based (Head/Core/Limb) |
| Range Bands | 1 Melee → 5 Line | Skewer falloff 100/70/50 |

### B. {{Mechanic Name}} (e.g., Speed-to-AP & Action Economy)

{{AP mapping table, initiative order, how M.A.W.-W modifies Speed/Range.}}

| Speed | AP | Examples |
|---|---|---|
| 5 | 4 AP | Warden, Vanguard |
| 4 | 3 AP | Specialist, Tech |
| 3 | 2 AP | Support, Heavily Laden |

### C. {{Mechanic Name}} (e.g., Four P-Framework)

{{P1 Passives, P2 Panic (Composure 0 triggers Berserk/Despair/Catatonic), P3 Parry (opposed clash roll), P4 Posture (Poise 0–120, stagger thresholds).}}

**Dual-Threshold Stagger:**
- **60% Part Rupture (Part HP):** Limb/weapon disabled, Vulnerability +50% (1.5×).
- **25% Meltdown OR Composure 0:** Full stagger, Vulnerability ×2.0 across all parts.

## III. DATA SCHEMA (JSON if applicable)

~~~json
{
  "operative": {
    "callsign": "{{Min-Jae}}",
    "baseSpeed": 5,
    "maxHP": 160,
    "composure": 100,
    "posture": 120,
    "rangeBand": 1,
    "mawSet": "MAW-W-001-01 / MAW-S-001-01 / MAW-G-001-01",
    "passives": ["{{Momentum Surge}}"]
  },
  "entity": {
    "secc": "SE-C-Vδ-002",
    "parts": [
      {"name": "Tectonic Crown", "hp": 800, "ruptureAt": 480, "resistances": {"grudge": 0.5, "lament": 1.0, "void": 1.2, "weight": 0.8}}
    ],
    "speed": 4,
    "composure": 250
  }
}
~~~

## IV. PLAYABLE INTEGRATION & ROADMAP

{{What can be done NOW (decoupled state machine), what needs UI, what JSON is ready for `GAME_BATTLE/` scenario import.}}

## V. CROSS-REFERENCES

- Battle Styles: `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM_STYLES.md`
- M.A.W. Codex: `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md`
- Scenario Template: `GAME_BATTLE/BATTLE_SCENARIO_TEMPLATE.md` (and `TEMPLATES/19_BATTLE_SCENARIO_DEEP_TEMPLATE.md`)

**Engine Seal:** {{Analyst Seal}}
~~~

---

## VALIDATION CHECKLIST

- [ ] 10-Node Grid (N01–N10) defined with Cover + Body + Flank.
- [ ] Speed-to-AP mapping present and consistent with `SOMNARAK_BATTLE_SYSTEM.md`.
- [ ] Four P-Framework (P1–P4) + Dual-Threshold (60% + 25%) present.
- [ ] M.A.W.-W modifiers and/or Workshop curve where loot is involved.
- [ ] JSON schema uses Operative + Entity + Parts (if combat).
- [ ] Zero banned strings.
