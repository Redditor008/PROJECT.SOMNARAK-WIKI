# 20 — BOSS MECHANICS TEMPLATE

**Template ID:** `T-20-BOSS`  
**Generates:** `GAME_BATTLE/BOSS_MECHANICS_{{NAME}}.md`  
**Authority:** `GAME_BATTLE/BOSS_MECHANICS_GRIEVING_COLOSSUS.md` (Sovereign exemplar) + Laws 5,8

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Boss Mechanics folios are sovereign adversary deep-dives** — Rank IV–V, full modular anatomy, intention deck, phase transitions, stagger geometry, Veil/Vessel handling, and squad counter-mandatory.
- **Bias to 3–5 Parts, not 1 blob.** E.g., Colossus has Crown/Heart/Foundation; Weeping Mirror has Frame/Reflection/Crack. Each part has independent HP, Rupture threshold (60%), and resistances (4 multipliers).
- **Phase transitions at 60% and 25% HP (or Composure 0)** — boss stance changes, new intention unlocked, arena Veil shifts, Sorrow Tide intensity steps.
- **Must reference the SECC dossier** — do not invent lore that contradicts `Sorrow_Entities/SE-*.md` Origin/Behavior/Breach.

---

## FILE NAMING

```
GAME_BATTLE/BOSS_MECHANICS_{{NAME_IN_CAPS}}.md
```

Example: `BOSS_MECHANICS_WEEPING_MIRROR.md`

---

## SCAFFOLD

~~~markdown
# Sovereign Boss Mechanics Folio — {{BOSS_EN}} — {{KOREAN}} (`SE-{{ID}}`)

> *“{{Epigraph — the sovereign’s law, as the facility learned it.}}”*

**Folio ID:** `BOSS-{{ID}}`  
**Linked Entity:** `SE-{{ID}}` — {{Name}} ({{Rank}} {{Potency}})  
**Threat Class:** {{Rank V Sovereign / Rank IV Entity + Sovereign-tier mechanics}}  
**Author:** {{Fleet Tactician / Containment Lead Dekan}}  
**Date:** Year {{4,23x}}  
**Classification:** Sovereign Engagement — Facility-Wide Protocol

## I. SOVEREIGN THESIS

{{1 paragraph: what makes this sovereign sovereign — what it demands of the facility, not just its damage.}}

## II. MODULAR ANATOMY & RESISTANCE MATRIX

| Part | Max HP | Rupture At (60%) | Lament | Grudge | Void | Weight | Failure Effect |
|---|---|---|---|---|---|---|---|
| **{{Part 1 — Crown/Frame}}** | {{1200}} | {{720}} | {{0.8x}} | {{1.0x}} | {{1.5x}} | {{0.5x}} | {{Crown shatters → Lament aura disabled}} |
| **{{Part 2 — Heart/Reflection}}** | {{1800}} | {{1080}} | {{1.2x}} | {{0.6x}} | {{1.0x}} | {{0.4x}} | {{Heart ruptures → Void chain disabled}} |
| **{{Part 3 — Foundation/Crack}}** | {{1000}} | {{600}} | {{1.0x}} | {{1.2x}} | {{0.8x}} | {{1.0x}} | {{Foundation ruptures → Weight stomp disabled}} |

- **Part size on grid:** {{Boss occupies N07–N09 (3-node Sovereign typical vs 2-node Fragment).}}
- **Vessel:** {{Destructible / Indestructible — Han Dust Drop if destructible.}}

## III. INTENTION DECK (Sovereign Actions)

| Intention | AP | Target Band | Element / Power | Effect |
|---|---|---|---|---|
| **{{Basic — e.g., Grieving Step}}** | {{2}} | {{Band 1–2}} | {{Weight 18}} | {{Stomp, knockback to N05 Cover destruction}} |
| **{{Heavy — e.g., Spire Collapse}}** | {{3}} | {{Band 1–4}} | {{Grudge 28}} | {{Skewer line, falloff 100/70/50}} |
| **{{Disrupt — e.g., Unvoiced Toll}}** | {{1}} | {{Area}} | {{Lament}} | {{Composure −15 all, Veil strain +5%}} |
| **{{Sovereign — e.g., Foundation Shard}}** | {{4}} | {{Band 4–5}} | {{Weight}} | {{Facility-wide, unlocked at Phase 3 only}} |

## IV. PHASE GEOMETRY & SORROW TIDE

### Phase 1 — Sovereign Vigil (100%–60% HP)

{{Squad probe, Veil intact, intentions 1–3 only. Sorrow Tide 0%.}}

### Phase 2 — Part Rupture Cascade (60%–25% HP)

{{First part at 60% triggers rupture: disabled intention, +50% vulnerability to that part, Veil thins, boss stance shifts.}}

### Phase 3 — Meltdown / Sovereign Unleashed (25%–0% HP or Composure 0)

{{Meltdown (2.0× vulnerability all parts), facility-wide intention unlocked, Sorrow Tide +10% per 6-turn sub-phase, Veil breach risk.}}

## V. SQUAD COUNTER-MANDATORY

| Counter | Why It Works | Who Executes |
|---|---|---|
| **{{Flank to N06 + Viderehan}}** | {{Exposes rupture seam}} | {{Specialist / Vanguard}} |
| **{{M.A.W.-W {{Element}} piercing line}}** | {{Ruptured part 1.5×}} | {{Striker with Band 4–5}} |
| **{{Warden Bastion at N05}}** | {{Holds Weight stomp}} | {{Warden Min-Jae archetype}} |
| **{{Archive Suture (post-Dawn)}}** | {{Ends Phase 3 without Veil loss}} | {{Scribe / Seiyon engram}} |

## VI. AFTERMATH & DIRECTORATE FOOTNOTE

{{What the facility learned: casualties, Veil repairs, M.A.W. costs, and the line that enters Council doctrine.}}

*Dossier: `SOMNARAK-WORLD/Sorrow_Entities/SE-{{ID}}*.md`  ·  Scenario: `GAME_BATTLE/SCENARIO_*.md`*
~~~

---

## VALIDATION CHECKLIST

- [ ] Linked SECC exists; folio lore does not contradict dossier Origin/Behavior/Breach.
- [ ] 3–5 Parts with HP + 60% Rupture + 4 resistance multipliers each.
- [ ] 4-intention deck with AP / Band / Element / Power; Sovereign intention gated to Phase 3.
- [ ] Phase geometry at 60% + 25%/Composure 0 with stance/Veil/Tide effects.
- [ ] Counter-mandatory maps to squad roles + M.A.W. bands.
- [ ] Sovereign occupies 2–3 grid nodes (not 1).
