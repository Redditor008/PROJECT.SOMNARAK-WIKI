# SOMNARAK ↔ LOBOTOMY CORPORATION — Full Conversion Reference
## For AI-Assisted Entity Transformation (Well of Cogito grabs a Somnarak Entity)

> **Combined-edition note (2026-10-30):** Owner's laptop original — the full field-by-field conversion reference — filed verbatim from the owner's dump and, for its SE → Abnormality material, rearranged by subject into the chapter sequence of the *Universal Sorrow Entity to Abnormality Conversion Table* (chaptered combined overhaul edition). This standalone file remains the archival original.

> *Give this document to an AI along with a Somnarak Entity file. The AI can use these mappings to transform the Sorrow Entity into a Lobotomy Corporation Abnormality. Every field in the entity file has an L Corp equivalent listed here.*

---

## I. Core Classification Mapping

| Somnarak Field | L Corp Equivalent | Conversion Notes |
|---|---|---|
| **SECC Designation** (`C-IVδ-001 [GS]`) | **Subject Number** (`O-06-20`) | Different format. Origin letter maps loosely (see Origin below). Number stays the same. |
| **Origin: C (City)** | **O (Original)** or general | City-born abnormalities; catch-all category |
| **Origin: N (Inner)** | **T (Trauma)** | Personal trauma, phobias, intense emotions |
| **Origin: O (Outside)** | **O (Original)** or **M (Mythical)** | Otherworldly, external, unknown cause |
| **Coherence (I–V)** | — | Used WITH Potency to calculate Risk Level (see §II) |
| **Potency (α–ω)** | — | Used WITH Coherence to calculate Risk Level (see §II) |
| **Sorrow Category** | **Classification Code origin letter** | City→O, Inner→T, Outside→O/M (see above) |
| **Element: Lament (Deep Blue)** | **WHITE Damage** | Attacks Mind / Sanity / emotional stability |
| **Element: Grudge (Crimson)** | **RED Damage** | Attacks Body / HP / physical form |
| **Element: Void (White/Pale)** | **PALE Damage** | Attacks Soul / percentage-based / identity erasure |
| **Element: Weight (Black)** | **BLACK Damage** | Attacks both HP and Sanity (mixed) |
| **Element: Mixed** | **Multiple Damage Types** | Entity deals 2+ damage types |
| **Manifestation: Subject** | **Humanoid / Creature** | Can breach, move, act independently |
| **Manifestation: Object** | **Inanimate / Tool-type (code 04/09)** | Fixed, can breach via Transform; may activate |
| **Manifestation: Place** | **Location-type** | The location itself is the abnormality |
| **R.D. Observation Level (0–4)** | **Observation Level (I–IV)** | Direct 1:1. Somnarak 0=Unknown → L Corp locked. Somnarak 4=Mastered → L Corp IV all unlocked. |

---

## II. Risk Level Conversion (Threat Score)

**Formula:** `Threat Score = Potency rank + Coherence rank`

| Potency | Rank | Coherence | Rank |
|---|---|---|---|
| α (Minor) | 1 | I (Residue) | 1 |
| β (Moderate) | 2 | II (Echo) | 2 |
| γ (Major) | 3 | III (Fragment) | 3 |
| δ (Critical) | 4 | IV (Entity) | 4 |
| ω (Catastrophic) | 5 | V (Sovereign) | 5 |

| Score | L Corp Risk Level | Somnarak Threat |
|---|---|---|
| 2–3 | **ZAYIN** | Minor |
| 4–5 | **TETH** | Moderate |
| 6 | **HE** | Major |
| 7–8 | **WAW** | Critical |
| 9–10 | **ALEPH** | Catastrophic |

**Example:** The Maw is Coherence IV + Potency ω = Score 9 = **ALEPH**

---

## III. HP Conversion

| L Corp Risk Level | HP Multiplier | Formula |
|---|---|---|
| ZAYIN | ×0.2 | `ceil(base_HP × 0.2)` |
| TETH | ×0.4 | `ceil(base_HP × 0.4)` |
| HE | ×1.8 | `ceil(base_HP × 1.8)` |
| WAW | ×4 | `ceil(base_HP × 4)` |
| ALEPH | ×10 | `ceil(base_HP × 10)` |

**NOTE: Every number must be a whole number — always round UP (ceil). No decimals.**

**Example:** Somnarak entity has 415/1000 HP, Threat Score 4 (TETH). L Corp HP = ceil(415 × 0.4) = **166 HP**.

---

## IV. ATK / Damage Conversion

| L Corp Risk Level | ATK Multiplier | Formula |
|---|---|---|
| ZAYIN | ×0.5–1.0 | `ceil(base_ATK × rand(0.5, 1.0))` |
| TETH | ×1.2–1.4 | `ceil(base_ATK × rand(1.2, 1.4))` |
| HE | ×1.4–1.8 | `ceil(base_ATK × rand(1.4, 1.8))` |
| WAW | ×1.0–1.8 | `ceil(base_ATK × rand(1.0, 1.8))` |
| ALEPH | ×0.5–1.0 | `ceil(base_ATK × rand(0.5, 1.0))` — but add **Instant Death** mechanics |

**NOTE: Every number must be a whole number — always round UP (ceil). No decimals.**

**Note:** HE-tier entities are the peak raw damage dealers. WAW entities hit hard but with wider variance. ALEPH entities deal less per-hit damage but compensate with **Instant Death / instakill abilities** (Somnarak: Instant Fracture).

**Damage Type Mapping:**

| Somnarak Element | L Corp Damage Type | What It Attacks |
|---|---|---|
| Lament (Deep Blue) | **WHITE** | Sanity / SP / mental health |
| Grudge (Crimson) | **RED** | HP / physical health |
| Void (Pale White) | **PALE** | Percentage of max HP (soul/identity) |
| Weight (Black) | **BLACK** | Both HP and Sanity simultaneously |

**Example:** Somnarak entity deals 10–23 Lament damage, Threat Score 4 (TETH). L Corp damage = WHITE, ceil(10×1.2)–ceil(23×1.4) = **12–33 WHITE damage**.

---

## V. Energy / Resource Mapping

| Somnarak | L Corp | Notes |
|---|---|---|
| **Han-Energy** | **Enkephalin** | The energy produced by working with entities. Powers the city/facility. |
| **Han-Energy yield** (per work cycle) | **PE-Boxes** (Positive Enkephalin boxes) | Successful work produces PE. Amount varies by entity. |
| **Negative Han buildup** | **NE-Boxes** (Negative Enkephalin) | Failed work produces NE, which damages the worker. |
| **Sorrow Gauge %** | **Mood / Energy state** | Low % = Good mood. High % = Bad mood. Determines work outcome quality. |
| **Starting Sorrow Gauge range** | **E-Box outcome ranges** (Good/Normal/Bad) | The gauge range maps to how many PE-Boxes are needed for Good/Normal/Bad results. |
| **Han (the structural force)** | **Enkephalin / Cogito** | The fundamental substance. Han = structural grief. Enkephalin = harvestable energy from grief. Cogito = the raw substance from the Well. |
| **The Weeping** | **The Well / The River** | The source of all entities. Somnarak: underground river of liquid Han. L Corp: the Well of Cogito / the River. |

---

## VI. Work Type Mapping

| Somnarak Work Type | L Corp Work | Axis | Element | What It Does |
|---|---|---|---|---|
| **Flerehan** (Tears) | **Attachment** | Physical + Lament | Empathy / bonding | Approach with emotion; weep alongside the entity |
| **Pugnahan** (Confrontation) | **Repression** | Physical + Grudge | Force / dominance | Confront, resist, suppress aggression |
| **Viderehan** (Observation) | **Insight** | Mental + Void | Study / detachment | Observe from distance; analyze without engaging |
| **Ferrehan** (Endurance) | **Instinct** | Mental + Weight | Patience / presence | Endure the entity's presence; contain through will |

**Work Favor / Preference:**
Somnarak's Work Type table (Response + Gauge Change per type) maps directly to L Corp's **Work Preferences** (success rate percentages per work type per agent level).

- Gauge "Decrease" = high success rate work (entity responds well)
- Gauge "Increase" = low success rate work (entity resists)
- Gauge "Stable" = moderate success rate

---

## VII. Breach & Activation Mapping

| Somnarak | L Corp | Notes |
|---|---|---|
| **Breach Type: Escape** | **Standard Breach** | Entity leaves containment, roams facility |
| **Breach Type: Corrupt** | **Corrupting Breach** | Entity damages the facility/containment |
| **Breach Type: Transform** | **Transformation** | Entity changes form, escalates |
| **Breach Type: Cascade** | **Cascading Breach** | Triggers other entities to breach |
| **Activation threshold** (Gauge ≥ X%) | **Qliphoth Counter** reaching 0 | The trigger condition for breach |
| **Sorrow Tide** (nightly Han surge) | **Qliphoth Meltdown** | Escalation event that pressures containment |
| **Ordeals** | **Ordeals** | External hostile events (already mapped: 5 Colors × 4 Watches) |
| **Instant Fracture** | **Instant Death / Instakill** | ω-grade (ALEPH) entity ability that removes a target instantly |

---

## VIII. Personnel Stats Mapping

| Somnarak Stat | L Corp Equivalent | What It Measures |
|---|---|---|
| **Clarity** | **Prudence / Sanity (SP)** | Mental clarity, ability to resist WHITE/PALE |
| **Composure** | **Temperance** | Emotional stability, ability to resist WHITE |
| **Resilience** | **Fortitude / HP** | Physical toughness, ability to resist RED |
| **Resolve** | **Justice** | Willpower, overall competence |
| **Fracture** (Stage 1–4) | **Panic** (various types) | What happens when Sanity hits 0 |
| **Architect's Mark** | **(no direct equivalent)** | Somnarak-specific: physical changes from Han exposure |

---

## IX. Equipment Mapping

| Somnarak | L Corp | Notes |
|---|---|---|
| **M.A.W.** (Materialized Agony Wear) | **E.G.O** (Extermination of Geometrical Organ) | Equipment extracted from entities. Somnarak = M.A.W. L Corp = E.G.O. Do not mix terms. |
| **M.A.W. Weapon** | **E.G.O Weapon** | Somnarak: M.A.W. Weapon. L Corp: E.G.O Weapon. Changes damage type and attack value. |
| **M.A.W. Suit (Armor)** | **E.G.O Suit** | Somnarak: M.A.W. Suit. L Corp: E.G.O Suit. Changes damage resistances. |
| **M.A.W. Gift (Accessory)** | **E.G.O Gift** | Somnarak: M.A.W. Gift. L Corp: E.G.O Gift. Passive stat buff, random acquisition. |
| **M.A.W. Grade: α** | **E.G.O Grade: ZAYIN** | Lowest tier equipment |
| **M.A.W. Grade: β** | **E.G.O Grade: TETH** | |
| **M.A.W. Grade: γ** | **E.G.O Grade: HE** | |
| **M.A.W. Grade: δ** | **E.G.O Grade: WAW** | |
| **M.A.W. Grade: ω** | **E.G.O Grade: ALEPH** | Highest tier; forbidden/experimental |
| **M.A.W. Corrosion** | **E.G.O Corrosion** | Equipment "turns" on the user; entity personality overtakes wearer |

---

## X. Narrative Section Mapping

| Somnarak Section | L Corp Equivalent | Notes |
|---|---|---|
| **이야기 보고 (Story Log)** | **Story tab entries** | Numbered lore entries unlocked via Observation Levels |
| **최종 관찰 (Final Observation)** | **Final Observation** | Choice-based success/fail observation event |
| **감각 묘사 (Flavor Text)** | **Flavor Text** | In-world sensory descriptions during work |
| **증언 (Testimonium)** | **(part of Story / Managerial Tips)** | First-person quotes from personnel |
| **기록 (Registrum)** | **Abnormality Details page** | Classification, containment, threat assessment |
| **관찰 기록 (Observation Log)** | **Managerial Tips** | Notes on how to handle the entity |
| **상호작용 (Entity Interactions)** | **(no direct equivalent)** | Somnarak-specific: how entities interact with each other |
| **이야기 (Narratio)** | **(part of Story / lore)** | The entity's full narrative tale |
| **Trivia** | **Trivia** | Same concept |
| **Registry Addendum** | **(no direct equivalent)** | Somnarak-specific: operational interpretation + review requirement |

---

## XI. Organization Mapping

| Somnarak | L Corp | Notes |
|---|---|---|
| **R.D. (Reverie Directorate)** | **Lobotomy Corporation (L Corp)** | The organization that contains entities |
| **The Hand of Change** (facility) | **The Facility** (Lobotomy Corp HQ) | The building where entities are contained |
| **Echo-Cores** (9 leaders) | **Sephirah / Department Heads** | The department leaders, each with unique sorrow |
| **Director Majin** | **Ayin / X / The Manager** | Supreme authority |
| **Secretary Seiyon** | **Angela** | The one who remembers everything, forbidden from acting |
| **Menders** | **(Welfare Team / Healing agents)** | Independent healing contractors |
| **Wardens** | **(Security Team / Captain)** | Enforcement and defense |
| **Keepers** | **(Record Team / Information)** | Memory and record keepers |
| **Collectors** | **(External extraction / Finance)** | Debt/sorrow collection |

---

## XII. World Concepts Mapping

| Somnarak | L Corp | Notes |
|---|---|---|
| **Han** (collective structural grief) | **Enkephalin / Cogito** | The fundamental energy substance |
| **The Weeping** (underground river) | **The Well of Cogito / The River** | Source of all entities |
| **The Alpha Tree** | **The Qliphoth Tree / Sephiroth** | The central structure connecting everything |
| **The Veil** | **Containment barriers** | The system keeping sorrow suppressed |
| **The Raw** (unmanaged areas) | **(uncontained sectors)** | Areas without suppression |
| **Sorrow Tide** (nightly surge) | **Qliphoth Meltdown** | Periodic escalation event |
| **Consolihan** (annual mourning) | **(special event / Ordeal spike)** | Annual sorrow spike |
| **Fracture** (4 stages) | **Panic → Death/Transformation** | What happens when personnel break |
| **Efflorescence** | **E.G.O synchronization** | Positive alternative to breaking |
| **The Cheongula** (First Sorrow) | **(backstory catastrophe)** | The founding trauma |
| **Absolvohan** | **(Tiphereth arc / special project)** | The plan to release all sorrow at once |
| **Echoes** (crystallized memory currency) | **PE-Boxes (as currency)** | The energy used for trade/manufacture |
| **Zones A–E** | **Departments / Floors** | The facility divisions |

---

## XIII. Quick Conversion Example

**Somnarak Entity:** The Torn Whisper — `C-IIβ-716 [GS]`
- Coherence: II (Echo), Potency: β (Moderate)
- Element: Grudge (Crimson) = **RED Damage**
- HP: 415/1000
- Han Pressure [ATK]: 10–23 per hit · Grudge

**Step 1 — Risk Level:**
Score = II(2) + β(2) = 4 → **TETH**

**Step 2 — L Corp HP:**
ceil(415 × 0.4) = **166 HP**

**Step 3 — L Corp Damage:**
RED damage, ceil(10 × 1.2)–ceil(23 × 1.4) = **12–33 RED**

**Step 4 — L Corp Subject Number:**
`T-02-16` (Trauma origin, animalistic/humanoid shape, #16)

**Step 5 — Work Preferences:**
Flerehan→Attachment (Decrease = High), Pugnahan→Repression (Increase = Low), Viderehan→Insight (Stable = Medium), Ferrehan→Instinct (Decrease = High)

**Result:** A TETH-class Abnormality dealing 12–46 RED damage with 623 HP, best worked via Attachment, worst via Repression.

---

---

## XIV. R.D. Attribute System (L Corp Crossover Mechanic)

> When a Somnarak Sorrow Entity is imported to L Corp via the Well of Cogito, L Corp Employees (Nuggets) exposed to its Han Effects can develop **R.D. Attributes** — Somnarak-native stats that do not exist in standard L Corp employees. This represents the employee's body and mind adapting to sustained Han exposure.

### The Four R.D. Attributes

Each attribute ranges from **1 (lowest) to 100 (highest)**. Points accumulate over time through exposure.

| Composure | Resolve | Clarity | Resilience |
|---|---|---|---|
| Emotional stability — resistance to Lament/WHITE | Willpower — resistance to Weight/BLACK | Mental clarity — resistance to Void/PALE | Physical toughness — resistance to Grudge/RED |

### Attribute Levels

| Level | Name | Point Range | Description |
|---|---|---|---|
| **Lvl 0** | None | 0 | Default for ALL L Corp employees — they have never been exposed to Han |
| **Lvl I** | Fragile | 1–20 | Below civilian average — vulnerable to Han effects |
| **Lvl II** | Average | 21–40 | Civilian level — can survive daily life under Han exposure |
| **Lvl III** | Trained | 41–60 | R.D. personnel level — can perform Work Types safely |
| **Lvl IV** | Veteran | 61–80 | Experienced personnel — can handle dangerous entities |
| **Lvl V** | Exceptional | 81–100 | Echo-Core level — can withstand what breaks others |

### Attribute Display Format (on L Corp Employee)

| Attribute | Display | Attribute | Display |
|---|---|---|---|
| Composure | [Level (0/I/II/III/IV/V)] [current/20] | Resolve | [Level (0/I/II/III/IV/V)] [current/20] |
| Clarity | [Level (0/I/II/III/IV/V)] [current/20] | Resilience | [Level (0/I/II/III/IV/V)] [current/20] |

Each level requires 20 points. Level 0 = 0 points. Level I = 1–20. Level II = 21–40. Etc.

### Attribute Interactions with Work Types

When an L Corp employee performs L Corp Works on an imported Somnarak entity, their R.D. Attributes determine resistance to the entity's Han Effects:

| L Corp Work | Somnarak Equivalent | Primary Attribute | Secondary Attribute | Failure Effect |
|---|---|---|---|---|
| **Attachment** | Flerehan (Tears) | **Composure** | Clarity | Emotional breakdown — crying, withdrawal |
| **Repression** | Pugnahan (Confrontation) | **Resolve** | Resilience | Physical collapse — exhaustion, injury |
| **Insight** | Viderehan (Observation) | **Clarity** | Composure | Mental breakdown — confusion, hallucination |
| **Instinct** | Ferrehan (Endurance) | **Resilience** | Resolve | Total collapse — physical and mental exhaustion |

**If the Primary Attribute is too low for the entity's Han Pressure [ATK], the employee suffers the Failure Effect.**

### How L Corp Employees Gain R.D. Attributes

1. **The employee must survive 3+ consecutive days** while sustaining a Somnarak Entity's Han Effect (working on the entity or being in its containment zone).
2. **Points accumulate automatically** — the employee gains points toward the R.D. Attribute(s) associated with the entity's Element/Work Type they have been sustaining.
3. **The attribute gained depends on the entity's Element:**

| Entity Element | Han Effect Type | Attribute Gained | L Corp Damage Type Equivalent |
|---|---|---|---|
| **Lament (Deep Blue)** | Emotional pressure | **Composure** (primary), Clarity (secondary) | WHITE |
| **Grudge (Crimson)** | Physical pressure | **Resilience** (primary), Resolve (secondary) | RED |
| **Void (Pale White)** | Identity/mental pressure | **Clarity** (primary), Composure (secondary) | PALE |
| **Weight (Black)** | Crushing/burden pressure | **Resolve** (primary), Resilience (secondary) | BLACK |
| **Mixed** | Multiple pressures | Gains split across all four attributes | Multiple |

4. **All L Corp employees start at Level 0** in every R.D. Attribute — they have never been exposed to Han Effects before. The R.D. Attribute system is entirely new to L Corp personnel.
5. **Points accumulate at approximately 1–3 points per day** of sustained exposure, depending on the entity's Potency (higher Potency = faster gain but higher risk).
6. **If an employee's R.D. Attribute reaches Level III (Trained, 41+ points), they can safely perform the associated Work Type on Somnarak entities without the Failure Effect.**

### Example

An L Corp employee works on an imported Somnarak Grudge entity (RED damage) for 5 days:
- Days 1–3: No R.D. Attribute gain (minimum 3-day survival threshold not yet met).
- Day 3: Threshold met. Employee begins accumulating **Resilience** points (primary) and **Resolve** points (secondary).
- Day 5: Employee has accumulated ~6 Resilience points and ~3 Resolve points.
- Display: `Resilience [Level I][6/20] | Resolve [Level I][3/20]`
- The employee is still **Fragile** — vulnerable. They need to reach Level III (41+ points, roughly 20+ more days) to safely handle Grudge entities.

---

*"Give this document and any Somnarak Entity file to an AI. Tell it: 'The Well of Cogito has grabbed this Somnarak Sorrow Entity and is transforming it into a Lobotomy Corporation Abnormality. Use the conversion reference to translate every field. L Corp employees exposed to this entity will develop R.D. Attributes per section XIV.' The AI should output a full L Corp Abnormality wiki page."*
