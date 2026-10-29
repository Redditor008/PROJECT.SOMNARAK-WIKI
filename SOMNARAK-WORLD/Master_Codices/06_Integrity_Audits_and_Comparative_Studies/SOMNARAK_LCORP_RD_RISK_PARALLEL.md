# Somnarak — L Corp Risk Level and R.D. Classification Parallel

> **Combined-edition note (2026-10-30):** Owner's laptop original — the creator-reference parallel (Threat Score, multipliers, conversion orders) — filed verbatim from the owner's dump and rearranged by subject into the chapter sequence of the *Universal Sorrow Entity to Abnormality Conversion Table* (chaptered combined overhaul edition) under source tag **[RRP]**. This standalone file remains the archival original.

## Purpose

This document provides a parallel reference between **Lobotomy Corporation Risk Levels** and the **Somnarak Reverie Directorate classification system**.

It is intended to help another AI or compiler understand how to mirror an Abnormality concept into a Somnarak Sorrow Entity, and how to convert a Somnarak Entity into an L Corp Abnormality, without treating the two systems as identical.

**Status:** Creator-reference parallel guide. Updated to reflect the current Threat Score system, HP/ATK multipliers, R.D. Attribute crossover mechanic, and all established conversion formulas. It does not replace Somnarak canon, SECC, the Entity Codex, or the Battle System.

---

## I. Threat Score System (Risk Level Conversion)

L Corp uses a single Risk Level (ZAYIN → ALEPH). Somnarak uses two axes — **Potency** and **Coherence** — that combine into a **Threat Score** mapping to the L Corp system.

### Formula

```
Threat Score = Potency Rank + Coherence Rank
```

| Potency | Rank | Coherence | Rank |
|---|---|---|---|
| α (Minor) | 1 | I (Residue) | 1 |
| β (Moderate) | 2 | II (Echo) | 2 |
| γ (Major) | 3 | III (Fragment) | 3 |
| δ (Critical) | 4 | IV (Entity) | 4 |
| ω (Catastrophic) | 5 | V (Sovereign) | 5 |

### Score → Risk Level

| Score | L Corp Risk Level | Somnarak Threat |
|---|---|---|
| 2–3 | **ZAYIN** | Minor |
| 4–5 | **TETH** | Moderate |
| 6 | **HE** | Major |
| 7–8 | **WAW** | Critical |
| 9–10 | **ALEPH** | Catastrophic |

### All 25 Combinations

| | **I** (Residue) | **II** (Echo) | **III** (Fragment) | **IV** (Entity) | **V** (Sovereign) |
|---|---|---|---|---|---|
| **α** (Minor) | **ZAYIN** (2) | **ZAYIN** (3) | TETH (4) | TETH (5) | HE (6) |
| **β** (Moderate) | **ZAYIN** (3) | TETH (4) | TETH (5) | HE (6) | WAW (7) |
| **γ** (Major) | TETH (4) | TETH (5) | HE (6) | WAW (7) | WAW (8) |
| **δ** (Critical) | TETH (5) | HE (6) | WAW (7) | WAW (8) | **ALEPH** (9) |
| **ω** (Catastrophic) | HE (6) | WAW (7) | WAW (8) | **ALEPH** (9) | **ALEPH** (10) |

### Canon Examples

| Entity | Potency + Coherence | Score | Risk Level |
|---|---|---|---|
| The Kind Echo (000) | α + I | 2 | ZAYIN |
| The Torn Whisper (716) | β + II | 4 | TETH |
| The Frozen Tear (100) | β + II | 4 | TETH |
| The Maw (001) | ω + IV | 9 | ALEPH |
| The Dawn of Mourning | ω + V | 10 | ALEPH |

---

## II. HP Conversion

Somnarak uses **X/X of 1000** for entity HP. L Corp uses absolute HP values. Convert using the multiplier for the entity's Risk Level.

| L Corp Risk Level | HP Multiplier | Formula |
|---|---|---|
| ZAYIN | ×0.2 | `ceil(Somnarak_HP × 0.2)` |
| TETH | ×0.4 | `ceil(Somnarak_HP × 0.4)` |
| HE | ×1.8 | `ceil(Somnarak_HP × 1.8)` |
| WAW | ×4 | `ceil(Somnarak_HP × 4)` |
| ALEPH | ×10 | `ceil(Somnarak_HP × 10)` |

**RULE: Every number must be a whole number — always round UP (ceil). No decimals.**

**Example:** Somnarak entity has 415/1000 HP, Threat Score 4 (TETH). L Corp HP = ceil(415 × 0.4) = **166 HP**.

---

## III. ATK / Han Pressure Conversion

Somnarak uses **Han Pressure [ATK]** (native damage per hit, varies per entity). L Corp uses Work Damage values. Convert using the multiplier for the entity's Risk Level.

| L Corp Risk Level | ATK Multiplier | Formula |
|---|---|---|
| ZAYIN | ×0.5–1.0 | `ceil(base_ATK × rand(0.5, 1.0))` |
| TETH | ×1.2–1.4 | `ceil(base_ATK × rand(1.2, 1.4))` |
| HE | ×1.4–1.8 | `ceil(base_ATK × rand(1.4, 1.8))` |
| WAW | ×1.0–1.8 | `ceil(base_ATK × rand(1.0, 1.8))` |
| ALEPH | ×0.5–1.0 | `ceil(base_ATK × rand(0.5, 1.0))` — add **Instant Death** mechanics |

**RULE: Always round UP. No decimals.**

**Note:** HE-tier entities are the peak raw damage dealers. ALEPH entities deal less per-hit but compensate with **Instant Death / Instant Fracture** abilities.

### Damage Type Mapping

| Somnarak Element | L Corp Damage Type | What It Attacks | L Corp Stat |
|---|---|---|---|
| **Lament (Deep Blue)** | **WHITE** | Mind / emotional stability | Sanity (SP) |
| **Grudge (Crimson)** | **RED** | Body / physical form | HP |
| **Void (Pale White)** | **PALE** | Soul / identity (percentage-based) | % of max HP |
| **Weight (Black)** | **BLACK** | Both HP and Sanity | HP + SP |
| **Mixed** | Multiple | Multiple stats | Varies |

---

## IV. Energy / Resource Mapping

| Somnarak | L Corp | Notes |
|---|---|---|
| **Han-Energy** | **Enkephalin** | The energy produced by working with entities |
| **H-Box (Han-Energy Box)** | **E-Box / PE-Box** | One unit of usable energy from successful work |
| **Han-Energy yield** (per cycle) | **E-Box yield / PE-Box yield** | How much energy each work produces |
| **Positive Han-Energy** | **PE-Box (Positive Enkephalin)** | Refined sorrow; powers equipment and infrastructure |
| **Negative Han-Energy** | **NE-Box (Negative Enkephalin)** | Unstable sorrow; damages the worker |
| **Sorrow Gauge [HP]** | **Mood / Energy bar** | Low % = Good mood. High % = Bad mood |
| **Sorrow Gauge %** | **Work outcome ranges (Good/Normal/Bad)** | Determines PE-Box yield quality |
| **Han** (structural grief) | **Cogito / Enkephalin** | The fundamental substance |
| **The Weeping** | **The Well / The River** | Source of all entities |

**Recommended Somnarak entity-file wording:**

```markdown
**Han-Energy Yield:** 12 H-Boxes per successful work cycle
**Sorrow Gauge [HP]:** 415/415 of 1000
**Han Pressure [ATK]:** 10–23 per hit · Lament
```

---

## V. Work Type Mapping

| Somnarak Work Type | L Corp Work | Axis | Element | What It Does |
|---|---|---|---|---|
| **Flerehan** (Tears) | **Attachment** | Physical + Lament | Empathy / bonding | Weep alongside the entity; share grief |
| **Pugnahan** (Confrontation) | **Repression** | Physical + Grudge | Force / dominance | Confront, resist, suppress aggression |
| **Viderehan** (Observation) | **Insight** | Mental + Void | Study / detachment | Observe without engaging emotionally |
| **Ferrehan** (Endurance) | **Instinct** | Mental + Weight | Patience / presence | Endure sustained presence; contain through will |

**Gauge Change → Work Success Rate:**
- **Decrease** = High success rate (entity responds well; best work)
- **Stable** = Moderate success rate (neutral response)
- **Increase** = Low success rate (entity resists; worst work)

---

## VI. Equipment Mapping (M.A.W. ≠ E.G.O)

| Somnarak | L Corp | Notes |
|---|---|---|
| **M.A.W.** (Materialized Agony Wear) | **E.G.O** (Extermination of Geometrical Organ) | Equipment extracted from entities. **Do not mix terms.** Somnarak = M.A.W. L Corp = E.G.O. |
| **M.A.W. Weapon** | **E.G.O Weapon** | Changes damage type and attack value |
| **M.A.W. Suit (Armor)** | **E.G.O Suit** | Changes damage resistances |
| **M.A.W. Gift (Accessory)** | **E.G.O Gift** | Passive stat buff; random acquisition |
| **M.A.W. Grade: α** | **E.G.O Grade: ZAYIN** | Lowest tier |
| **M.A.W. Grade: β** | **E.G.O Grade: TETH** | |
| **M.A.W. Grade: γ** | **E.G.O Grade: HE** | |
| **M.A.W. Grade: δ** | **E.G.O Grade: WAW** | |
| **M.A.W. Grade: ω** | **E.G.O Grade: ALEPH** | Highest tier; forbidden/experimental |
| **M.A.W. Corrosion** | **E.G.O Corrosion** | Equipment turns on the user |

---

## VII. Breach & Activation Mapping

| Somnarak | L Corp | Notes |
|---|---|---|
| **Breach Type: Escape** | **Standard Breach** | Entity leaves containment, roams facility |
| **Breach Type: Corrupt** | **Corrupting Breach** | Entity damages facility/containment |
| **Breach Type: Transform** | **Transformation** | Entity changes form, escalates |
| **Breach Type: Cascade** | **Cascading Breach** | Triggers other entities to breach |
| **Activation threshold** (Gauge ≥ X%) | **Qliphoth Counter** reaching 0 | The trigger condition |
| **Sorrow Tide** (nightly Han surge) | **Qliphoth Meltdown** | Escalation event |
| **Ordeals** | **Ordeals** | External hostile events (5 Colors × 4 Watches) |
| **Instant Fracture** | **Instant Death / Instakill** | ω-grade (ALEPH) entity special |

---

## VIII. Personnel Stats Mapping

| Somnarak Stat | L Corp Equivalent | What It Measures |
|---|---|---|
| **Clarity** | **Prudence** | Mental clarity; resist WHITE/PALE |
| **Composure** | **Temperance** | Emotional stability; resist WHITE |
| **Resilience** | **Fortitude / HP** | Physical toughness; resist RED |
| **Resolve** | **Justice** | Willpower; overall competence |
| **Fracture** (Stage 1–4) | **Panic** (various types) | What happens when Sanity hits 0 |
| **Architect's Mark** | *(no direct equivalent)* | Somnarak-specific: physical changes from Han exposure |

---

## IX. R.D. Attribute System (L Corp Crossover Mechanic)

> When a Somnarak Sorrow Entity is imported to L Corp via the Well of Cogito, L Corp Employees (Nuggets) exposed to its Han Effects can develop **R.D. Attributes** — Somnarak-native stats that do not exist in standard L Corp employees.

### The Four R.D. Attributes

| Composure | Resolve | Clarity | Resilience |
|---|---|---|---|
| Emotional stability — resists Lament/WHITE | Willpower — resists Weight/BLACK | Mental clarity — resists Void/PALE | Physical toughness — resists Grudge/RED |

Each ranges from **1 (lowest) to 100 (highest)**. Points accumulate through sustained Han exposure.

### Attribute Levels

| Level | Name | Points | Description |
|---|---|---|---|
| **Lvl 0** | None | 0 | **Default for ALL L Corp employees** — never exposed to Han |
| **Lvl I** | Fragile | 1–20 | Below civilian average — vulnerable |
| **Lvl II** | Average | 21–40 | Civilian level — can survive daily Han exposure |
| **Lvl III** | Trained | 41–60 | R.D. personnel level — can perform Work Types safely |
| **Lvl IV** | Veteran | 61–80 | Experienced — can handle dangerous entities |
| **Lvl V** | Exceptional | 81–100 | Echo-Core level — withstands what breaks others |

### Attribute Display Format

| Attribute | Display | Attribute | Display |
|---|---|---|---|
| Composure | [Level (0/I/II/III/IV/V)] [current/20] | Resolve | [Level (0/I/II/III/IV/V)] [current/20] |
| Clarity | [Level (0/I/II/III/IV/V)] [current/20] | Resilience | [Level (0/I/II/III/IV/V)] [current/20] |

### Attribute ↔ Work Type Interactions

| L Corp Work | Somnarak Equivalent | Primary Attribute | Secondary Attribute | Failure Effect |
|---|---|---|---|---|
| **Attachment** | Flerehan (Tears) | **Composure** | Clarity | Emotional breakdown — crying, withdrawal |
| **Repression** | Pugnahan (Confrontation) | **Resolve** | Resilience | Physical collapse — exhaustion, injury |
| **Insight** | Viderehan (Observation) | **Clarity** | Composure | Mental breakdown — confusion, hallucination |
| **Instinct** | Ferrehan (Endurance) | **Resilience** | Resolve | Total collapse — physical and mental exhaustion |

### How L Corp Employees Gain R.D. Attributes

1. **Survive 3+ consecutive days** sustaining a Somnarak Entity's Han Effect.
2. **Points accumulate automatically** (~1–3/day based on entity Potency).
3. **Attribute gained depends on the entity's Element:**

| Entity Element | Attribute Gained (Primary) | Attribute Gained (Secondary) | L Corp Damage |
|---|---|---|---|
| **Lament (Deep Blue)** | Composure | Clarity | WHITE |
| **Grudge (Crimson)** | Resilience | Resolve | RED |
| **Void (Pale White)** | Clarity | Composure | PALE |
| **Weight (Black)** | Resolve | Resilience | BLACK |
| **Mixed** | Split across all four | Split across all four | Multiple |

4. **All L Corp employees start at Level 0.** The R.D. Attribute system is entirely new to them.
5. **Reach Level III (41+ points)** to safely perform the associated Work Type without Failure Effects.

---

## X. SECC Code System (5 × 5 × 5 × 5)

### Designation Format

```
SE-[Origin]-[Coherence][Potency]-[Number] [Element][Manifestation]
Example: SE-C-IVδ-001 [GS]
```

| Component | Codes (5 each) |
|---|---|
| **Origin** | `C` City · `N` Inner · `O` Outside |
| **Coherence** | `I` Residue · `II` Echo · `III` Fragment · `IV` Entity · `V` Sovereign |
| **Potency** | `α` Minor · `β` Moderate · `γ` Major · `δ` Critical · `ω` Catastrophic |
| **Element** | `L` Lament (Deep Blue) · `G` Grudge (Crimson) · `V` Void (Pale White) · `W` Weight (Black) · `M` Mixed |
| **Manifestation** | `S` Subject · `O` Object · `P` Place · `T` Time · `H` Hybrid |

### Sorrow Category

| Code | Korean | Source |
|---|---|---|
| **C (City)** | 도한 (Dohan) | City systems, institutions, accumulated institutional grief |
| **O (Outside)** | 외한 (Oehan) | Wilderness, Desolate, external forces |
| **N (Inner)** | 내한 (Naehan) | Personal grief, individual trauma |

---

## XI. Narrative Section Mapping

| Somnarak Section | L Corp Equivalent | Notes |
|---|---|---|
| **이야기 보고 (Story Log)** | **Story tab entries** | 5 numbered entries unlocked via Observation Levels |
| **최종 관찰 (Final Observation)** | **Final Observation** | Choice-based success/fail observation |
| **감각 묘사 (Flavor Text)** | **Flavor Text** | Sensory descriptions during work |
| **증언 (Testimonium)** | *(part of Story)* | First-person personnel quotes |
| **기록 (Registrum)** | **Abnormality Details page** | Classification, containment, threat |
| **관찰 기록 (Observation Log)** | **Managerial Tips** | How to handle the entity |
| **상호작용 (Entity Interactions)** | *(no direct equivalent)* | How entities interact with each other |
| **이야기 (Narratio)** | *(part of Story / lore)* | Full narrative tale (350–500 words) |
| **Trivia** | **Trivia** | Same concept |
| **Registry Addendum** | *(no direct equivalent)* | Operational interpretation + review |

---

## XII. Organization Mapping

| Somnarak | L Corp | Notes |
|---|---|---|
| **R.D. (Reverie Directorate)** | **Lobotomy Corporation (L Corp)** | Contains and studies entities |
| **The Hand of Change** (facility) | **The Facility** (L Corp HQ) | Where entities are contained |
| **Echo-Cores** (9 leaders) | **Sephirah / Department Heads** | Department leaders, each with unique sorrow |
| **Director Majin** | **Ayin / X / The Manager** | Supreme authority |
| **Secretary Seiyon** | **Angela** | Remembers everything, forbidden from acting |
| **Menders** | *(Welfare Team)* | Independent healing contractors |
| **Wardens** | *(Security Team)* | Enforcement and defense |
| **Keepers** | *(Record Team)* | Memory and record keepers |
| **Collectors** | *(External extraction)* | Debt/sorrow collection |
| **Zones A–E** | **Departments / Floors** | Facility divisions |

---

## XIII. World Concepts Mapping

| Somnarak | L Corp | Notes |
|---|---|---|
| **Han** (structural grief) | **Cogito / Enkephalin** | Fundamental energy substance |
| **The Weeping** (underground river) | **The Well / The River** | Source of all entities |
| **The Alpha Tree** | **The Qliphoth Tree** | Central structure |
| **The Veil** | **Containment barriers** | Suppression system |
| **Sorrow Tide** (nightly surge) | **Qliphoth Meltdown** | Periodic escalation |
| **Consolihan** (annual mourning) | *(special event)* | Annual sorrow spike |
| **Fracture** (4 stages) | **Panic → Death** | Personnel breakdown |
| **Efflorescence** | **E.G.O synchronization** | Positive alternative to breaking |
| **The Cheongula** (First Sorrow) | *(backstory catastrophe)* | Founding trauma |
| **Absolvohan** | *(special project arc)* | Plan to release all sorrow |
| **Echoes** (crystallized memory) | **PE-Boxes (as currency)** | Trade/manufacture unit |

---

## XIV. Conversion Order (Somnarak → L Corp)

When the Well of Cogito grabs a Somnarak Entity:

| Step | Somnarak Field | L Corp Output |
|---|---|---|
| 1 | Potency + Coherence | **Risk Level** (via Score) |
| 2 | HP (X/1000) | **L Corp HP** (× multiplier, ceil) |
| 3 | Han Pressure [ATK] | **Work Damage** (× multiplier, ceil) + Damage Type |
| 4 | Element | **Damage Type** (Lament→WHITE, Grudge→RED, Void→PALE, Weight→BLACK) |
| 5 | Origin (C/N/O) | **Subject Number** first letter |
| 6 | Work Type table | **Work Preferences** (success rates per work) |
| 7 | Han-Energy yield | **PE-Box yield** + E-Box count |
| 8 | Sorrow Gauge | **Qliphoth Counter** / Mood |
| 9 | M.A.W. Equipment | **E.G.O** (Weapon/Suit/Gift) |
| 10 | Story Log | **Story tab entries** |
| 11 | Final Observation | **Final Observation** |
| 12 | Flavor Text | **Flavor Text** |
| 13 | Origin / Narratio | **Story / lore** |
| 14 | Breach Behavior | **Breach mechanics + abilities** |
| 15 | Combat Actions | **Special abilities** |

---

## XV. Conversion Order (L Corp → Somnarak)

When adapting an L Corp Abnormality into Somnarak:

| Step | L Corp Field | Somnarak Output |
|---|---|---|
| 1 | Risk Level | **Starting Potency + Coherence** (via Score reverse-lookup) |
| 2 | Subject Number origin letter | **Origin code** (F→varies, T→N, O→C/O, D→C, M→O) |
| 3 | Work Damage type | **Element** (RED→Grudge, WHITE→Lament, BLACK→Weight, PALE→Void) |
| 4 | HP | **Sorrow Gauge [HP]** (÷ multiplier, ceil, format X/X of 1000) |
| 5 | Work Damage | **Han Pressure [ATK]** (÷ multiplier, ceil) |
| 6 | E-Box count | **Han-Energy yield** (H-Boxes) |
| 7 | Qliphoth Counter | **Activation threshold / Sorrow Gauge trigger** |
| 8 | Work Preferences | **Work Type table** (success → Decrease, failure → Increase) |
| 9 | E.G.O | **M.A.W. Equipment** (Weapon/Suit/Gift) |
| 10 | Story entries | **이야기 보고 (Story Log)** |
| 11 | Breach mechanics | **Breach Behavior + Detailed Record** |
| 12 | Special abilities | **Combat Actions** (6 actions) |
| 13 | Risk Level grade | **M.A.W. Grade** (ZAYIN→α, ..., ALEPH→ω) |
| 14 | Appearance | **Appearance + Detailed Appearance Profile** |
| 15 | Origin story | **Origin + Narratio** |

---

## XVI. Worked Example

### Somnarak → L Corp

**Entity:** The Torn Whisper — `C-IIβ-716 [GS]`
- Coherence: II, Potency: β → Score 4 → **TETH**
- Element: Grudge (Crimson) → **RED Damage**
- HP: 415/1000 → ceil(415 × 0.4) = **166 HP**
- Han Pressure [ATK]: 10–23 → ceil(10 × 1.2)–ceil(23 × 1.4) = **12–33 RED**
- Work Types: Flerehan↓, Pugnahan↑, Viderehan→, Ferrehan↓ → Attachment (High), Repression (Low), Insight (Medium), Instinct (High)
- Han-Energy: 12–18 H-Boxes → **12–18 PE-Boxes**

**Result:** A TETH-class Abnormality, 166 HP, dealing 12–33 RED damage, best worked via Attachment, worst via Repression, yielding 12–18 PE-Boxes.

### L Corp → Somnarak

**Entity:** Nothing There — `O-06-20`, ALEPH, RED 6–9
- Risk Level: ALEPH → Score 9–10 → **δ+V or ω+IV/V**
- Already is: Coherence IV + Potency ω = Score 9 → matches
- Damage: RED → **Grudge (Crimson)**
- L Corp ATK 6–9 → Somnarak: ceil(6 ÷ 0.75)–ceil(9 ÷ 0.75) ≈ **8–12 per hit · Grudge**
- Origin: O → **City or Outside Sorrow**
- Designation: `C-IVω-001 [GP]` (this IS The Maw's designation — they are analogues)

---

## XVII. L Corp Shape / Form Codes

L Corp's second number in the Subject Number (`Letter-XX-YY`) represents the Abnormality's shape/form. Somnarak's Manifestation code maps to these:

| L Corp Code | L Corp Shape | Somnarak Manifestation | Notes |
|---|---|---|---|
| **01** | Humanoid | **Subject** (Subject-Body, Subject-Mind) | Human-like body or appendages |
| **02** | Animalistic | **Subject** (creature/animal forms) | Non-human living entities |
| **03** | Otherworldly / Religious | **Subject** (Subject-Spirit, Subject-Dream) or **Hybrid** | Alien, divine, incomprehensible |
| **04** | Inanimate Object | **Object** (Object-*) | Stationary object entities |
| **05** | Machine / Artifact | **Object** (mechanical) or **Time** | Autonomous mechanical entities |
| **06** | Abstract / Phenomenon | **Place** or **Hybrid** | Intangible, perception-dependent |
| **07** | Breaching Tool | **Object** (Tool-type, code 07) | Conditionally a Tool that can breach (e.g., Yang) |
| **08** | Sin (Peccatula) | *(no Somnarak equivalent)* | L Corp-specific (Limbus Company) |
| **09** | Tool-type | **Object** (Tool-type) | Can breach via Transform; interacted with for benefit |
| **00** | Unknown / Training | **Subject** (training entity) | Special: The Kind Echo = Standard Training-Dummy Rabbit |

---

## XVIII. Tool Abnormality Types (Three Types)

From L Corp wiki research, Tool Abnormalities (code 09) have three distinct use types. Somnarak's Object entities map to these via the **Tool Type** field:

| Tool Type | Somnarak Relic | Behavior | Unlock Info | L Corp Examples |
|---|---|---|---|---|
| **Single Use Tools** | **A-Relic (Arma)** | Give a single instant effect upon use. Consumed or depleted. | **Number of Uses** | Theresia (T-09-09), Old Lady (O-01-12) |
| **Channeled Use Tools** | **O-Relic (Officium)** | Constant work use that can be cancelled when ordered again. Sustained effect. | **Time of Use** | Don't Touch Me (O-05-47) |
| **Equippable Tools** | **I-Relic (Indumentum)** | An Agent equips upon use. Effects persist while equipped. Returned by clicking containment or at end of day. | **Equipped state** | Crumbling Armor (O-05-61) |

**Note:** The Kind Echo (SE-C-Iα-000) is the Somnarak equivalent of the Standard Training-Dummy Rabbit (0-00-00) — both are docile training entities with zero designations.

---

## XIX. Somnarak-Specific Systems (No Direct L Corp Equivalent)

| Somnarak System | Function | Closest L Corp Equivalent |
|---|---|---|
| **R.D. Attributes** (Composure, Resolve, Clarity, Resilience) | Personnel stats for handling Han Effects | Employee stats (Fortitude, Prudence, Temperance, Justice) — see §IX for crossover mechanic |
| **Sorrow Gauge [HP]** | Entity containment pressure (X/X of 1000) | Qliphoth Counter + Mood bar |
| **Han Pressure [ATK]** | Entity damage output per hit | Work Damage value |
| **H-Box (Han-Energy Box)** | Energy unit from successful work | PE-Box (Positive Enkephalin Box) |
| **Fracture** (4 stages: Crack → Spread → Crystallization → Emergence) | Personnel transformation from Han overload | Panic → Death |
| **Efflorescence** | Positive transformation (sorrow becomes strength) | E.G.O synchronization |
| **M.A.W. Corrosion** | Equipment turning on user (4 stages) | E.G.O Corrosion |
| **Sorrow Tide** | Nightly city-wide Han surge | Qliphoth Meltdown |
| **Consolihan** | Annual mourning event (sorrow spike) | *(no equivalent — special event)* |
| **Ordeals** | External hostile events (5 Colors × 4 Watches) | Ordeals (6 Colors × 4 Times) |
| **The Veil / The Raw** | Sorrow suppression system / unmanaged areas | Containment barriers / uncontained sectors |

---

## XX. Crossover Implications

When a Somnarak Sorrow Entity arrives in the L Corp universe through the Well of Cogito:

1. **Classification Crisis:** The entity would be classified as an Abnormality, but the SECC system doesn't map perfectly. The Well would attempt to convert it using the Threat Score system (Potency + Coherence = Score → Risk Level).

2. **Work Type Adaptation:** L Corp employees would map Somnarak Work Types to existing works: Flerehan→Attachment, Pugnahan→Repression, Viderehan→Insight, Ferrehan→Instinct. The entity's Work Type table (Gauge Change per type) determines success rates.

3. **R.D. Attribute Development:** L Corp employees exposed to Han would develop new stats (Composure, Resolve, Clarity, Resilience) that don't exist in standard employees. They start at Level 0 and accumulate points after surviving 3+ days of sustained exposure (see §IX).

4. **Equipment Translation:** M.A.W. would be converted to E.G.O. The M.A.W. trio (Weapon / Suit / Gift) maps directly to E.G.O trio. M.A.W. Grade (α–ω) maps to E.G.O Grade (ZAYIN–ALEPH). Extraction method differs: Somnarak uses resonance; L Corp uses facility extraction systems.

5. **Damage Type Conversion:** Somnarak Elements map to L Corp Damage Types: Lament→WHITE, Grudge→RED, Void→PALE, Weight→BLACK. The entity's Han Pressure [ATK] converts to L Corp Work Damage via the ATK multiplier (§III).

6. **HP Conversion:** Somnarak HP (X/X of 1000) converts to L Corp HP via the HP multiplier (§II). Always round up.

7. **Narrative Translation:** The Somnarak Story Log (5 entries) becomes L Corp Story tab entries. The Final Observation becomes a Final Observation event. The Tale and Testimony sections fold into the Story/lore. Entity Interactions and Registry Addendum have no L Corp equivalent and may be dropped or kept as supplementary lore.

8. **The Terminal (S.A.M.S.):** The Somnarak Abnormality Management System would serve as the bridge terminal between the two systems — containing the conversion tables, R.D. Attribute tracking, and real-time Threat Score calculation for any Somnarak entity the Well of Cogito pulls in. L Corp employees would access S.A.M.S. data through their standard terminal interface.

---

## XXI. Document Structure Comparison

Side-by-side comparison of which sections exist in each system's document:

| Section | Somnarak SE Document | L Corp Abnormality Document |
|---|---|---|
| **Classification** | SECC Designation table | Subject Number + Risk Level |
| **Operational Parameters** | Stats, work difficulty, Han-Energy yield, Han Pressure [ATK] | E-Boxes, Qliphoth Counter, Work Damage |
| **Combat Record** | Core Stat Line, Combat Actions (6), Battle Phases, Consequences | Managerial Works, Escape Information |
| **Appearance** | Detailed physical description + Detailed Appearance Profile | Portrait, basic description |
| **Origin** | Formation, Sorrow, Event, People, Expanded context | Origin story (if available) |
| **Behavior** | Work Type responses (Flerehan/Pugnahan/Viderehan/Ferrehan) | Work Preferences/Favor (Attachment/Repression/Insight/Instinct) |
| **Breach Behavior** | Detailed breach mechanics + Escalation Notes + Detailed Record | Escape Information + defenses |
| **Equipment** | M.A.W. (Weapon, Suit, Gift) + Use Notes + Field Use Record | E.G.O (Weapon, Suit, Gift) |
| **Observation Log** | 관찰 기록 + Observation Progression | Encyclopedia sections (unlockable) |
| **Story Log** | 이야기 보고 — 5 numbered fragmentary entries | Story tab entries |
| **Final Observation** | 최종 관찰 — choice-based success/fail event | Final Observation (some abnormalities) |
| **Flavor Text** | 감각 묘사 — sensory descriptions | In-game flavor text |
| **Entity Interactions** | 상호작용 — how entities interact with each other | *(no equivalent)* |
| **Tale** | 이야기 — full narrative story (350–500 words) | *(no equivalent — folded into Story)* |
| **Testimony** | 증언 — first-person personnel quotes | *(part of Story / Managerial Tips)* |
| **Record** | 기록 — classification, containment, threat, procedures | Abnormality Details page |
| **Registry Addendum** | Operational interpretation + review requirement | *(no equivalent)* |
| **Trivia** | Canon trivia + Registry Trivia | Trivia section |

---

## XXII. Important Rules

1. **Do not treat L Corp Risk Level and SECC as identical systems.** Use the Threat Score to bridge them.
2. **M.A.W. is Somnarak. E.G.O is L Corp.** Never use one term for the other system's equipment.
3. **Always round UP (ceil).** No decimal values in any stat.
4. **HP format in Somnarak is always `X/X of 1000`.**
5. **Han Pressure [ATK]** is the Somnarak term for damage output per hit.
6. **H-Boxes** is the Somnarak term for energy units (equivalent to L Corp E-Boxes/PE-Boxes).
7. Preserve the **5 × 5 × 5** code system: Origin (3+), Coherence (5), Potency (5), Element (5), Manifestation (5).
8. Preserve **Somnarak Elements**: Lament/Grudge/Void/Weight/Mixed.
9. **R.D. Attributes** (Composure/Resolve/Clarity/Resilience) are crossover stats for L Corp employees exposed to Han — they start at Level 0.
10. Every Somnarak entity file follows the **fixed template structure** (SECC Classification → Operational Parameters → Combat Record → Appearance → Origin → Behavior → Breach → M.A.W. → Observation → Story Log → Final Observation → Flavor → Interactions → Tale → Testimony → Record → Trivia → Document Info).
11. External crossover or parody entities go outside the main canon roster.
12. Uploaded canon/reference files remain immutable.

---

*"Give this document and any Somnarak Entity file to an AI. Tell it: 'The Well of Cogito has grabbed this Somnarak Sorrow Entity and is transforming it into a Lobotomy Corporation Abnormality. Use the conversion reference to translate every field. L Corp employees exposed to this entity will develop R.D. Attributes per section IX.' The AI should output a full L Corp Abnormality wiki page."*
