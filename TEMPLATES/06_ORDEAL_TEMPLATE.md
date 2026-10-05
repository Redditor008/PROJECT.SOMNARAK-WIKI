# 06 — ORDEAL TEMPLATE

**Template ID:** `T-06-ORDEAL`  
**Generates:** `SOMNARAK-WORLD/Ordeals/Ordeal_{{COLOR}}_{{WATCH}}_{{Name}}.md`  
**Authority:** `SOMNARAK_ORDEALS_FRAMEWORK.md` + `SOMNARAK_BATTLE_SYSTEM.md` + Global Primer Laws 1,2,8,9  
**Canonical Count:** 60 Ordeals (5 Colors × 4 Watches × 3 Ordeals per watch)

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **5 Colors = 5 Elements/Pressures:** BLACK (Weight / 비중, crushing), BLUE (Lament / 비탄, despair), GREY (Grudge / 원한, humanoid incursions), PALE (Void / 공허, erasure), PURPLE (Mixed / Raw Han corruption).
- **4 Watches = escalation:** First Watch → Second Watch → Third Watch → Tide Watch (facility-wide). Higher watch = higher Potency (α→ω) and longer battle (8→28 turns).
- **Ordeals are NOT entities.** They are cyclical facility defense events — waves, swarms, harvesters, choirs. They have no SECC. They have Ordeal Codes: `Ordeal-BLACK-First-01` etc.
- **Tripartite Crisis Taxonomy:** Ordeal (external wave) vs Entity Breach (escaped SE) vs Echo-Core Suppression (Floor Realization). Do not conflate.

---

## FILE NAMING

```
SOMNARAK-WORLD/Ordeals/Ordeal_{{COLOR}}_{{WATCH}}_{{Name_With_Underscores}}.md
```

Example: `Ordeal_BLUE_First_Watch_The_Voice.md` (illustrative example — no such file ships)

---

## SCAFFOLD

~~~markdown
# Ordeal — {{ENGLISH_NAME}} — {{KOREAN_NAME}}

> *“{{Epigraph — what the tide sounds like when it comes.}}”*

**Document ID:** `Ordeal-{{COLOR}}-{{WATCH}}-{{NUM}}`  
**Color / Element:** {{BLACK Weight / BLUE Lament / GREY Grudge / PALE Void / PURPLE Mixed}}  
**Watch:** {{First / Second / Third / Tide}}  
**Potency:** {{Minor-α / Moderate-β / Major-γ / Catastrophic-δ}}  
**Battle Length:** {{8 / 16 / 24 / 28 turns}}  
**Author:** {{Floor {{1–8}} Tactical Log, Year {{4,2xx}} }}  
**Classification:** Facility Defense — Cyclical

## TACTICAL OVERVIEW

| Field | Record |
|---|---|
| **Ordeal Code** | `Ordeal-{{COLOR}}-{{WATCH}}-{{NUM}}` |
| **Element** | {{Weight/Lament/Grudge/Void/Mixed}} |
| **Primary Pressure** | {{Structure / Composure / Soul / Mixed}} |
| **Wave Composition** | {{E.g., “12 Lament Wisps + 1 Choir Leader”}} |
| **Spawn Vector** | {{Sector {{A–E}}, floor, or Veil breach}} |
| **Resolution** | {{Suppress all waves / hold line for {{N}} turns / seal breach}} |

### Watch Context

{{1 paragraph: where this Watch sits in the Day. First Watch is Dawn probe, Second is midday pressure, Third is dusk escalation, Tide is night facility-wide. What the previous Watch taught.}}

## WAVE COMPOSITION & PHASES

### Phase 1 — Probe (Turns 1–{{N}})
- **Units:** {{E.g., “6 Weight Siphons (30 HP each)”}}
- **Behavior:** {{Scatter, pressure test, gauge tick +10%}}
- **Counter:** {{Ferrehan / Pugnahan / Viderehan as appropriate}}

### Phase 2 — Surge (Turns {{N}}–{{M}})
- **Units:** {{Heavier, leader appears}}
- **Behavior:** {{Focus fire, part rupture, Composure drain}}
- **Counter:** {{M.A.W. Weapon with {{Element}} + Suit resistance}}

### Phase 3 — Tide (Turns {{M}}–End)
- **Units:** {{Boss wave or endless until seal}}
- **Behavior:** {{Facility-wide debuff, +10% Han saturation per turn}}
- **Resolution:** {{Hold, suppress, or face next Watch escalation}}

## COMBAT RECORD

| Stat | Value |
|---|---|
| **Speed** | {{1.5–3.0 m/s swarm typical}} |
| **Resistance** | {{Element-appropriate}} |
| **Han Pressure** | {{6–24 per hit by Potency}} |
| **Special** | {{Ordeal-specific — e.g., “Weight Ordeal: victims take %HP as Weight”}} |

### Ordeal Ability — {{ABILITY_NAME}}

**Trigger:** {{Wave or turn condition}}

**Effect:** {{Area pressure, gauge tick, stagger}}

**Counter:** {{How the 4 Works + M.A.W. answer it}}

## FIELD REMARKS & AFTERMATH

### Incident — {{TITLE}}

**Date:** Year {{4,2xx}} · Day {{1–365}} Watch {{X}}  
**Squad:** {{Squad name, 4 operatives}}  
**Result:** {{How they held/broke, what M.A.W. was used, what was learned for next Watch}}

**Aftermath:** {{Han stain, repairs, Echo cost, lesson for Tide Watch}}

## WATCH PROGRESSION NOTE

{{If First/Second/Third, tease next Watch: “Surviving this probe without sealing the Veil guarantees a heavier Tide.” If Tide, note facility-wide saturation and boss stance.}}
~~~

---

## VALIDATION CHECKLIST

- [ ] Color is one of 5 and matches element (BLACK=Weight, BLUE=Lament, GREY=Grudge, PALE=Void, PURPLE=Mixed).
- [ ] Watch is one of 4 and Potency escalates with Watch (Tide is highest).
- [ ] No SECC code — Ordeals have Ordeal Codes, not SE- codes.
- [ ] Tripartite taxonomy respected (Ordeal vs Breach vs Suppression not conflated).
- [ ] 3 Phases present (Probe/Surge/Tide or equivalent).
- [ ] Zero banned strings.
