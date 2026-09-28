# 19 — BATTLE SCENARIO DEEP TEMPLATE

**Template ID:** `T-19-SCENARIO`  
**Generates:** `GAME_BATTLE/SCENARIO_{{XX}}_{{TITLE}}.md` + `GAME_BATTLE/CANONICAL_ENCOUNTER_{{XX}}_{{TITLE}}.md`  
**Authority:** `GAME_BATTLE/BATTLE_SCENARIO_TEMPLATE.md` (SOP-GB-SPEC-001) + `SOMNARAK_BATTLE_SYSTEM.md` + `SOMNARAK_BATTLE_SYSTEM_STYLES.md` + Laws 1,4,5,8  
**Canonical Model:** Operation Sub-Basalt Anchor & Breach Containment (Zone B -450m vs SE-C-IVγ-044)

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Scenarios are SOP-GB-SPEC-001 compliant** — 6-turn minimum, 10-Node Grid, Speed-to-AP, 4P Framework, Dual-Threshold Stagger, Sorrow Tide tick (+10% Han saturation per 6-turn Phase).
- **Battle Styles:** Generic P.S. Core + 5 Wing Styles — Reverie Directorate (Facility Oversight & Echo-Cores), UCD (Urban CQB & Part Dismantling), SED (Abyssal Depth Pressure & Sonar), Memory Archive (Mnemonic Suture), Horizon Caravan (Trans-Desolate Bastion Warfare). Pick ONE primary style per scenario.
- **Entity must exist** in 292 catalog (no invention). If scenario is UCD, adversary may be syndicate construct; if SED, abyssal entity (Oehan) is appropriate.
- **Range Bands 1–5 + Falloff 100%→70%→50%** must be used for any piercing weapon.

---

## FILE NAMING

```
GAME_BATTLE/SCENARIO_{{XX}}_{{TITLE_IN_CAPS}}.md
GAME_BATTLE/CANONICAL_ENCOUNTER_{{XX}}_{{TITLE}}.md
```

Example: `SCENARIO_03_UNDERWORLD_RUST_VEIL_PURGE.md`

---

## SCAFFOLD — FILL IN ORDER (SOP-GB-SPEC-001 Structure)

~~~markdown
# BATTLE SCENARIO SPECIFICATION — {{TITLE_EN}} — {{KOREAN_TITLE}}

> *“{{Epigraph — the battle’s truth before the first shot.}}”*

## Canonical Battle Model: {{OPERATION_NAME}}
### Reference Scenario Specification — SOP-GB-SPEC-{{NUM}}

```text
+======================================================================+
|           REVERIE DIRECTORATE TACTICAL ENGAGEMENT RECORD             |
+----------------------------------------------------------------------+
| TACTICAL ENGAGEMENT RECORD: BATTLE-SPEC-{{XX}}-{{SLUG}}              |
| OPERATIONAL AREA  : {{Zone + Sector + Depth}}                        |
| DEPTH COORDINATE  : Depth {{Depth}}m {{Surface / Sub-Basalt / Abyss}}|
| THREAT RATING     : Rank {{I–V}} (Grade {{α–ω}} Potency)             |
| STRIKE TEAM       : {{Strike Team {{Name}} (4 Operatives)}}          |
| SQUAD STRENGTH    : 4 Operatives ({{Callsign1, Callsign2, ...}})     |
| PRIMARY OBJECTIVE : {{Breach Containment / Purge / Descent / Siege}} |
| ENGAGEMENT STATUS : {{Standardized / After-Action / Realization}}    |
+======================================================================+
```

## 1. Tactical Overview & Operational Parameters

- **Topological Coordinate:** {{Zone, Sector, Depth — exact.}}
- **Ambient Han Saturation:** {{% Ambient Weeping Density (mMb).}}
- **Environmental Hazard Modifiers:**
  * **{{Hazard 1 — e.g., Acoustic Echo Reverberation:}}** {{Vault resonance amplifies Lament; failed parry → +10% Lament strain.}}
  * **{{Hazard 2 — e.g., Collapsed Basalt Rubble:}}** {{Nodes [N04] and [N05] require 2 AP to traverse.}}
- **Mission Briefing:**
  {{At {{HH:MM}}, {{sensor/event}} registered {{pressure spike / Veil breach}}. Strike Team {{Name}} deployed via {{rail/shaft/crawler}} to {{objective}} before {{consequence}. Entity is `SE-{{ID}}` — {{one-line sorrow core}}. Battle Style is {{Generic / R.D. / UCD / SED / Archive / Caravan}} because {{justification}.}}

## 2. Combatant Rosters & Technical Profiles

### 2.1 Allied Strike Team {{NAME}} (4 Operatives)

| Operative Callsign | Tactical Role | Base Spd | Max HP | Composure | Posture | Equipped M.A.W. Set | Range Band |
|---|---|---|---|---|---|---|---|
| **{{Warden}}** | {{Citadel Vanguard}} | {{5}} | {{160}} | {{100}} | {{120}} | {{M.A.W. Set Name (Grade {{α–ω}})}} | {{Band 1 (Melee)}} |
| **{{Vanguard}}** | {{Kinetic Striker}} | {{4}} | {{140}} | {{90}} | {{100}} | {{...}} | {{Band 2 (Short)}} |
| **{{Specialist}}** | {{Acoustic Flanker}} | {{4}} | {{120}} | {{110}} | {{80}} | {{...}} | {{Band 3 (Medium)}} |
| **{{Tech}}** | {{Sensor Anchor}} | {{3}} | {{110}} | {{100}} | {{90}} | {{...}} | {{Band 4 (Long)}} |

> Every Operative must list Base Speed (→ AP), Max HP, Composure, Posture, exact M.A.W. Registry Code, and Range Band (1–5).

### 2.2 Hostile Entity: {{ENTITY_EN}} (`SE-{{ID}}`)

- **Coherence Rank & Potency:** Rank {{I–V}} {{Name}} · Grade {{α–ω}}
- **Total Composure Pool:** {{250 Points typical}} · Meltdown Threshold: 0
- **Base Speed:** {{1–6}} (Generates {{1–5}} AP per turn)
- **Modular Body Part Anatomy:**

| Modular Part Name | Part Max HP | Rupture Threshold (60%) | Lament Def | Grudge Def | Void Def | Weight Def |
|---|---|---|---|---|---|---|
| **{{Part 1 — e.g., Brass Dial Face}}** | {{500 HP}} | {{300 HP}} | {{0.8x}} | {{1.0x}} | {{1.2x}} | {{0.5x}} |
| **{{Part 2 — e.g., Escapement Core}}** | {{800 HP}} | {{480 HP}} | {{...}} | {{...}} | {{...}} | {{...}} |
| **{{Part 3 — e.g., Pendulum Arm}}** | {{400 HP}} | {{240 HP}} | {{...}} | {{...}} | {{...}} | {{...}} |

- **Hostile Intention Deck:**
  * **{{Ability 1 (Basic Attack):}}** {{AP}} · Target Band {{1–5}} · Element: {{Lament/Grudge/Void/Weight}} · Base Power {{N}}.
  * **{{Ability 2 (Heavy Strike):}}** {{AP}} · Target Band {{1–5}} · Element: {{...}} · Base Power {{N}}.
  * **{{Ability 3 (Buff/Disrupt):}}** {{AP}} · Self/Area · {{Effect}}.

## 3. Initial 10-Node Grid Topography Map

```text
+========================================================================+
|                       SPATIAL GRID TOPOGRAPHY                          |
+------------------------------------------------------------------------+
| INITIAL 10-NODE GRID TOPOGRAPHY: {{ZONE}} TACTICAL CORRIDOR            |
|     [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]        |
| [{{Ops}}] [{{Ops}}] [{{Ops}}] [{{Ops}}] [COVER]   [ENTITY BODY]        |
| Allied Deployment [N01-03] | Center [N04-06]                           |
|        | Hostile Presence [N07-08]                                     |
+========================================================================+
```

- **Allied Starting Nodes:** {{Who at N01, N02, N03, N04.}}
- **Environmental Markers:** {{Cover at N05 — basalt bulkhead / Drift Throne Bastion plate / archive shelf.}}
- **Hostile Position:** {{Entity occupies N07–N08 (2-node Boss typical).}}

## 4. Turn-by-Turn Operational Chronicle (6 Turns Minimum, 10-Node + 4P + Dual-Threshold)

### Battle Turn 01: {{Title — e.g., Initial Advance & Reconnaissance}}

#### 1. Initiative & Action Point Allocation
- **{{Op1}}:** Speed {{5}} → {{4}} AP.
- **{{Op2}}:** Speed {{4}} → {{3}} AP.
- *(Entity: Speed {{3}} → {{3}} AP.)*

#### 2. Node Maneuvers & Tactical Positioning
- {{Who advances from N04→N05 (cover, {{AP}} spent), who holds, who flanks to N06.}}

#### 3. Clash & Parry Resolutions (P3)
- **Clash 01:** {{Op}} [{{Parry}}] vs Hostile [{{Attack}}] targeting [{{Node}}].
  * {{Op}} Roll: Speed {{5}} + Power {{12}} = {{17}}.
  * Hostile Roll: Speed {{3}} + Power {{11}} = {{14}}.
  * Result: **{{Op Deflects (Margin +3)}}**. {{Posture strain, cancel, or damage.}}

#### 4. Modular Part Damage & Composure Tracking (P4)
- {{Op}} fires from [{{Node}}] targeting {{Part}} at [{{Node}}] (Distance = {{N}}, Band {{valid}}).
  * Damage: {{45 Grudge (  원한  / Wonhan [Grudge])}}.
  * {{Part}} HP: {{400→355}} (Rupture: {{240}}).
- Hostile Composure: {{250→230}}.

*(Repeat for Battle Turn 02–06. At least one Part must Rupture at 60% and one Meltdown/Full Stagger at 25%/Composure 0 must occur. Include Sorrow Tide tick: +10% Han saturation per 6-turn Phase and boss stance change.)*

### Battle Turn 06: {{Title — e.g., Stagger Exploitation & Sealing}}

{{Final resolution: sealing, suture, Bastion hold, or Realization trigger. Document Echo Cost if sealing requires Veil reseal.}}

## 5. Aftermath & Lessons

| Field | Record |
|---|---|
| **Result** | {{Containment Resealed / Purge Complete / Descent Aborted / Bastion Held / Realization Achieved}} |
| **Casualties** | {{Composure loss, injuries, Han saturation lingering}} |
| **M.A.W. Cost Paid** | {{Memory/voice/warmth per Bearer}} |
| **Sorrow Tide** | {{Facility/zone saturation after}} |
| **Lesson for Next Operation** | {{What the 4 squad roles learned}} |
~~~

*Battle Style: {{Primary style}} — {{One sentence justification}}.*

---

## VALIDATION CHECKLIST

- [ ] 6 turns minimum (2 Phases) with +10% Sorrow Tide tick per Phase and stance change.
- [ ] Every Operative has Speed→AP + M.A.W. Registry Code + Range Band 1–5.
- [ ] Every Hostile has 3 Parts + Rupture at 60% + Intentions with AP/Band/Element/Power.
- [ ] 10-Node map (N01–N10) with Cover at N05 and Entity Body at N07–N08; all moves cost AP.
- [ ] P3 Parry clashes have opposed rolls (Speed + Power) and margin; P4 Posture tracked.
- [ ] At least one Part Rupture (1.5× vuln) and one Meltdown/Composure-0 (2.0×) occur.
- [ ] No invented SE; Two-Work-Type respected in briefing if Object/Place.
- [ ] Style is one of 6 (Generic + 5 Wings) with justification.
