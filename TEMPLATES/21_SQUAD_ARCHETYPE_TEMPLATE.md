# 21 — SQUAD ARCHETYPE TEMPLATE

**Template ID:** `T-21-SQUAD`  
**Generates:** `GAME_BATTLE/SQUAD_ARCHETYPE_{{NAME}}.md`  
**Authority:** `GAME_BATTLE/SQUAD_ARCHETYPE_REVERIE_CONTAINMENT.md` + `SQUAD_ARCHETYPE_UCD_PACIFICATION.md` + `SOMNARAK_BATTLE_SYSTEM_STYLES.md` + Laws 1,4

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Squad Archetypes are 4-operative cadre manuals** — standardized 4-person tactical cultures, not “party builds.” Two canonical archetypes exist: Reverie Containment (Facility 01, Warden-led Bastion) and UCD Pacification (Raw, 4-Breacher CQB).
- **Archetype defines:** Creed, composition (Role + Speed → AP + Range Band + M.A.W. loadout per operative), deployment doctrine (10-Node), inter-role synergy (pincer, cover, resonance), and wing-specific gear (SED sonar, Caravan Bastion, Archive suture, etc.).
- **No 5th operative.** Somnarak tactical doctrine is 4-wardens / 4-breachers. Do not write 5- or 6-person squads.
- **Promote Han-flow tech appropriately:** SED uses acoustic sonar + depth pressure, UCD uses evidence custody + targeted part dismantling, R.D. uses containment + echo-core suppression, Caravan uses Bastion + Han-flow navigation, Archive uses mnemonic suture.

---

## FILE NAMING

```
GAME_BATTLE/SQUAD_ARCHETYPE_{{NAME_IN_CAPS}}.md
```

Example: `SQUAD_ARCHETYPE_HORIZON_BASTION.md`

---

## SCAFFOLD

~~~markdown
# Squad Archetype Manual — {{ARCHETYPE_EN}} — {{KOREAN_TITLE}}

> *“{{Creed — one line the squad says before breach.}}”*

**Archetype ID:** `SQUAD-{{WING}}-{{NUM}}`  
**Wing / Decor:** {{Reverie Directorate / UCD / SED / Memory Archive / Horizon Caravan}}  
**Battle Style:** {{One of 6 — Generic P.S. + 5 Wing Styles — justify why this archetype embodies it}}  
**Doctrine:** {{Bastion Hold / CQB Purge / Depth Survey / Mnemonic Suture / Trans-Desolate Escort}}  
**Date:** Year {{4,23x}} — {{Pre- or Post-Dawn as appropriate for Wing}}  
**Author:** {{Squad Lead / Wing Trainer — e.g., “Training Cadre, Floor 5 Border Watch”}}

## I. CREED & HERITAGE

{{1 paragraph: what this squad believes about sorrow that other squads do not.}}

## II. COMPOSITION — 4 OPERATIVES

| Callsign | Role | Base Speed → AP | Range Band | M.A.W. Loadout (Grade) | Signature Trait |
|---|---|---|---|---|---|
| **{{Op1 — e.g., Warden Min-Jae}}** | {{Citadel Vanguard}} | {{5→4 AP}} | {{Band 1 Melee}} | {{MAW-W-{{NUM}} + MAW-S-{{NUM}} + MAW-G-{{NUM}}}} | {{Threshold Vow — one-meter Sacred Blade}} |
| **{{Op2 — e.g., Vanguard Taeho}}** | {{Kinetic Striker}} | {{4→3 AP}} | {{Band 2 Short}} | {{...}} | {{Ancestral Signet — sunder}} |
| **{{Op3 — e.g., Specialist Seol-A}}** | {{Acoustic Flanker}} | {{4→3 AP}} | {{Band 3 Medium}} | {{...}} | {{Silenced Requiem — flank}} |
| **{{Op4 — e.g., Tech Jinho}}** | {{Sensor Anchor}} | {{3→2 AP}} | {{Band 4 Long}} | {{...}} | {{Calibrated Dampener — harmonic pulse}} |

> Each row must state Role + Speed→AP + Band + exact M.A.W. Registry Codes.

## III. DEPLOYMENT DOCTRINE (10-Node Grid)

```text
+=====================================================================+
|                 SQUAD DEPLOYMENT — 10-NODE DOCTRINE                 |
+---------------------------------------------------------------------+
| N01    N02    N03    N04    N05    N06    N07    N08    N09    N10  |
| [{{Op4}}] [{{Op3}}] [{{Op2}}] [{{Op1}}] [COVER]   [ENTITY BODY]     |
| Principle: {{E.g., Warden at Cover, Striker behind, Flanker later}} |
+=====================================================================+
```

- **Initiative Order:** {{Speed high → AP high → first to clash (P3 Parry).}}
- **Movement Doctrine:** {{Who holds N05 Cover, who flanks to N06, who stays at N01 for long Band 4–5 M.A.W.-W piercing.}}
- **Pincer & Resonance:** {{How the 4 create line resonance or suture.}}

## IV. WING-SPECIFIC KIT & RITE

| Kit | Function | Cost |
|---|---|---|
| **{{Kit 1 — e.g., Bastion Plate (Caravan)}}** | {{Mobile Cover, +2 DEF line}} | {{Movement −1 AP while braced}} |
| **{{Kit 2 — e.g., Acoustic Sonar (SED)}}** | {{Depth pressure reveal, +1 Viderehan}} | {{Han filter drain}} |
| **{{Kit 3 — e.g., Sealing Tongs (UCD)}}** | {{Part dismantling, evidence custody}} | {{Evidence weight}} |
| **{{Kit 4 — e.g., Suture Needle (Archive)}}** | {{Mnemonic suture, +10% Archive resonance}} | {{Composure tick}} |

**Rite:** {{One ritual before deployment — naming, Veil check, memory write, Bastion lock.}}

## V. SYNERGY & STAGGER EXPLOITATION

{{1–2 paragraphs: how the 4 together trigger Dual-Threshold — e.g., “Warden holds so Flanker can Viderehan rupture seam at 60%, Striker pierces 1.5×, Anchor confirms Composure 0 Meltdown for 2.0× team burst.” Include Sorrow Tide handling.}}

## VI. AFTER-ACTION & LINEAGE

**Notable Deployment:** {{Date, theater, what this archetype proved.}}

**Lineage Note:** {{What this archetype teaches the next generation — and its limit.}}
~~~

---

## VALIDATION CHECKLIST

- [ ] Exactly 4 operatives, each with Role + Speed→AP + Band + M.A.W. Registry Codes.
- [ ] 10-Node deployment with Cover at N05 and Body at N07–N08; doctrine explains who moves where and why.
- [ ] Wing Style is one of 6 with coherent kit (Bastion/Sonar/Custody/Suture as appropriate).
- [ ] No 5th member; no modern ordnance slips; no invented SE.
- [ ] In-world cadre manual voice, not game build notes.
