# SOMNARAK — Entity Codex

> *"Each Sorrow Entity is a story. A wound. A question. To contain them is to hold someone's grief in your hands."*

The **Entity Codex** is the canonical reference for how every Sorrow Entity file is structured and read. It does not repeat the full lore of any single entity — that lives in each entity's individual file. Instead it documents the **classification systems, record sections, and combat framework** that every entity entry follows, so a reader can open any of the 268+ entity files and understand exactly what they are looking at.

This Codex mirrors the canonical **Subject Template (v0.4)** — the ~18-section structure used for all Sorrow Entity records. Not every field appears in every file (Object, Place, and Hazard manifestations omit some combat options), but the sections below are the standard the Codex is built on.

---

## How to Read an Entity Entry

Every entity file is a layered document. It moves from **cold classification** at the top (what the entity *is*, mechanically) down through **observed behavior** (what it *does*) and into **narrative record** (what it *means*). Read top-to-bottom, an entry tells you:

1. **What it is** — SECC Classification, Operational Parameters
2. **How it fights** — Combat Record
3. **What it looks like and where it came from** — Appearance, Origin
4. **How it responds to work and what happens when it breaks free** — Behavior, Breach Behavior
5. **What it can be forged into** — M.A.W. Equipment
6. **What has been observed and recorded** — Observation Log, Story Log, Final Observation
7. **The human truth underneath** — Flavor Text, Interactions, Tale, Testimony, Record

The sections below explain each layer.

---

## SECC Classification

The **Sorrow Entity Classification Code (SECC)** is the unique identifier stamped on every entity. It encodes five classification dimensions in a single line.

**Format:** `SE-[Origin]-[Coherence][Potency]-[Number] [Element][Manifestation]`

> Example: `SE-C-IIIβ-014 [VS]` → the 14th City-origin Sorrow Entity, Fragment coherence, Moderate potency, Void element, Subject-Body manifestation.

### Origin (Sorrow Category)

Where the sorrow crystallized. This is the first letter of the code.

| Code | Sorrow Category | Korean | Meaning |
|------|----------------|--------|---------|
| **C** | City Sorrow | 도한 (Dohan) | Born inside Somnarak's walls — the grief of citizens, debt, judgment |
| **N** | Inner Sorrow | 내한 (Naehan) | Born from within — intimate, personal, internal grief |
| **O** | Outside Sorrow | 외한 (Oehan) | Born in the Desolate beyond the walls — wild, ancient, uncontained |

### Coherence (I–V)

How **self-aware and complete** the entity's personality is. Higher coherence means a more complex, willful entity.

| Tier | Name | Meaning |
|------|------|---------|
| **I** | Residue | A trace — barely a self, reactive only |
| **II** | Echo | A repeating pattern — fragments of a person |
| **III** | Fragment | A personality shaped by its origin |
| **IV** | Entity | Self-aware, purposeful, can communicate |
| **V** | Sovereign | Ancient, city-scale, near-mythic |

### Potency (α–ω)

How **dangerous** the entity is — the severity of its pressure and the scale of threat.

| Grade | Name | Meaning |
|-------|------|---------|
| **α** | Minor | Manageable with routine procedure |
| **β** | Moderate | Manageable with standard precautions |
| **γ** | Major | Demands specialized response |
| **δ** | Critical | Facility-threatening if breached |
| **ω** | Catastrophic | City-threatening; near-impossible to contain |

> Lowercase **ω** is used for Catastrophic potency. Capital **Ω** is reserved for Hope Intensity only.

### Element

The kind of pressure the entity exerts. Element determines damage type and resistance.

| Element | Color | Pressure Type |
|---------|-------|---------------|
| **Lament** | Deep Blue | Sanity / composure pressure |
| **Grudge** | Crimson | HP / body pressure |
| **Void** | Pale White | Percentage pressure (1 unit = 5% Max HP) |
| **Weight** | Black | Both HP and sanity pressure |
| **Mixed** | Cycles all four | Rotates through every type over time |

### Manifestation

The physical form the sorrow takes in the world — separate from Coherence and Potency. Each entity's Manifestation combines a **Physical Type** (what it IS) with a **Form Descriptor** (what it FEELS LIKE / where it comes from narratively).

#### Physical Types

| Type | Code | Form | Work Types Available |
|------|------|------|---------------------|
| **Subject** | S | A body — walks, acts, can be confronted | All four (Flerehan, Pugnahan, Viderehan, Ferrehan) |
| **Object** | O | An inert thing — a relic, idol, or device | Viderehan and Ferrehan only |
| **Place** | P | A location — a room, district, or zone | Viderehan and Ferrehan only |
| **Time** | T | A recurring event or period | Viderehan and Ferrehan only |
| **Hazard** | H | A condition or environmental effect | Viderehan and Ferrehan only |

> Objects, Places, Times, and Hazards cannot be confronted (Pugnahan) or emotionally engaged (Flerehan). Only observation (Viderehan) and endurance (Ferrehan) are effective against them.

#### Form Descriptors (Narrative Origin Types)

The Form Descriptor classifies the **narrative origin and nature** of the sorrow — equivalent to Lobotomy Corporation's F/T/O/M form-type system, but in Somnarak terms. Each descriptor tells you what *kind* of grief the entity embodies:

| Descriptor | Korean | Meaning | LC Equivalent | Example Entities |
|------------|--------|---------|---------------|-----------------|
| **Body** | 신체 | Physical, corporeal — the sorrow has taken flesh and bone | — (physical) | The Orphaned Bell, The Smothering Mother |
| **Lament** | 탄식 | Born from grief, loss, and mourning — the sorrow of what was taken | T (Trauma — grief) | The Hollow Choir, The Grieving Colossus |
| **Grudge** | 원한 | Born from rage, injustice, and fury — the sorrow of what was done to you | T (Trauma — anger) | The Maw, The Rage Forge |
| **Void** | 공허 | Born from absence, erasure, and dissolution — the sorrow of what was forgotten | T (Trauma — identity loss) | The Debt Eater, The Frozen Veil |
| **Weight** | 무게 | Born from burden, obligation, and pressure — the sorrow of what you owe | T (Trauma — burden) | The Cracked Hourglass, The Debt Scale |
| **Phantasmal** | 환영 | Spectral, semi-corporeal — exists between the Veil and the Raw | — (supernatural) | The Cartographer's Ghost, The Forgotten Soldier |
| **Dream** | 꿈 | Partially exists in the Dream realm — the sorrow of what was only imagined | M (Mythical — dream) | The Secretary (Seiyon), entities connected to the Dream |
| **Mind** | 정신 | Psychological, cognitive — attacks comprehension and reason itself | T (Trauma — psychological) | The Memory Weaver, The Silent Child |
| **Spirit** | 영혼 | Soul-bound, afterlife-adjacent — the sorrow of the dead who cannot leave | — (spiritual) | The Kind Echo, entities bound to the Weeping |
| **Tale** | 이야기 | Born from a forgotten story, myth, or legend — the sorrow crystallized when the story was lost | F (Fairytale) | The Frozen Veil (fairy-tale origin), Place-Tale entities |

> **Tale** is the rarest descriptor — entities born when a story so powerful it shaped the city was forgotten, corrupted, or broken, and its sorrow crystallized into Han. These are the Somnarak equivalent of Lobotomy Corporation's Fairytale (F) form-type.

The full Manifestation is written as **[Physical Type]-[Descriptor]**, combining 5 physical types with 10 form descriptors for a complete 50-cell classification matrix:

| | Body | Lament | Grudge | Void | Weight | Phantasmal | Dream | Mind | Spirit | Tale |
|---|---|---|---|---|---|---|---|---|---|---|
| **Subject** | Subject-Body | Subject-Lament | Subject-Grudge | Subject-Void | Subject-Weight | Subject-Phantasmal | Subject-Dream | Subject-Mind | Subject-Spirit | Subject-Tale |
| **Object** | Object-Body | Object-Lament | Object-Grudge | Object-Void | Object-Weight | Object-Phantasmal | Object-Dream | Object-Mind | Object-Spirit | Object-Tale |
| **Place** | Place-Body | Place-Lament | Place-Grudge | Place-Void | Place-Weight | Place-Phantasmal | Place-Dream | Place-Mind | Place-Spirit | Place-Tale |
| **Time** | Time-Body | Time-Lament | Time-Grudge | Time-Void | Time-Weight | Time-Phantasmal | Time-Dream | Time-Mind | Time-Spirit | Time-Tale |
| **Hazard** | Hazard-Body | Hazard-Lament | Hazard-Grudge | Hazard-Void | Hazard-Weight | Hazard-Phantasmal | Hazard-Dream | Hazard-Mind | Hazard-Spirit | Hazard-Tale |

> Each physical type carries the same 10 descriptors. Not all 50 combinations currently have catalogued entities — some (e.g. Time-Body, Hazard-Tale) await discovery. The classification is complete even where the bestiary is not.

**Examples:**
- `Subject-Body` = a walking, corporeal being
- `Object-Void` = an inert object that dissolves identity
- `Place-Lament` = a location imbued with grief
- `Place-Tale` = a place born from a forgotten story
- `Subject-Dream` = a being that partially exists in the Dream realm
- `Hazard-Mind` = a condition that attacks comprehension itself

### Physical Form

Whether the entity is made of living matter or not: **Organic**, **Non-Organic**, or **Mixed**.

---

## Operational Parameters

The mechanical summary used for field simulation and balancing. These values support structured play without replacing the SECC classification.

| Parameter | What It Means |
|-----------|---------------|
| **Risk tier** | Mirrors Potency (Minor → Catastrophic) |
| **Starting Sorrow Gauge** | How full the entity's gauge begins (higher = closer to breach) |
| **Han-Energy yield** | Energy gained per successful work cycle |
| **Work difficulty** | Scaled to R.D. Observation Level |
| **Activation threshold** | The gauge % at which the entity activates or breaches |
| **Vessel-Destructible** | Whether the physical vessel can be destroyed (drops Han Dust) |
| **Han Dust Drop** | Material yielded if the vessel is destroyed |

> A successful work cycle reduces immediate pressure but does not permanently transform or destroy the entity. Entities are effectively immortal — see *Entity Immortality & Suppression*.

---

## Combat Record

The encounter framework. Not all entities fight, but every record carries the combat format for field reference.

### Core Stat Line

| Stat | Meaning |
|------|---------|
| **Speed** | Movement rate (N/A for fixed objects/places) |
| **Resistance** | Damage reduction by pressure type |
| **Sorrow Gauge [HP]** | The entity's effective health (out of 1000) |
| **Han Pressure [ATK]** | Damage dealt per hit, by element |
| **Coherence / Potency modifiers** | How the tier scales behavior complexity and pressure |

### Combat Actions

Each entity lists bespoke moves in a table format matching the field Sorrow Entity record:

**Name / Category · Flavor Text · Combat Move · Combat Effect/Stat · Trigger**

Categories: **Debuff**, **Attack**, **Heavy**, **Ultimate**. Each move's damage is shown in a color-coded bracket block tied to its element.

### Damage Color System

Damage is typed by element and shown in color-coded stat blocks:

- **Deep Blue / Lament** — sanity-type pressure
- **Crimson / Grudge** — HP-type pressure
- **Pale White / Void** — percentage pressure (`1 = 5% Max HP`)
- **Black / Weight** — applies to both HP and sanity
- **Mixed** — cycles all four types in order (HP → Sanity → Both → %) over 8 seconds, 2 seconds per type

### Battle Phases & Consequences

Encounters run in three phases — **Tension → Clash → Resolution** — ending in containment, retreat, or the documented suppression condition. Failed resistance applies pressure and raises the gauge; if resolution is not reached, the entity follows its breach behavior.

---

## Appearance

Documents what the entity physically is: **Primary Form**, **Notable Features**, and an **Identification Profile** (type, manifestation, primary marker, position/movement, element signature, registered location). A Detailed Appearance Profile table records form, position, material signature, and distinctive markers so personnel can confirm an entity before work.

## Origin

The human story behind the sorrow: **Formation** (how it crystallized), **The Sorrow** (the emotion at its core), **The Event** (the incident that birthed it), and **The People** (who it came from). The origin explains both the visible form and the response to personnel.

## Behavior & Work Types

How the entity responds to the four Work Types, with the gauge change each produces:

| Work Type | Korean | Action |
|-----------|--------|--------|
| **Flerehan** | Tears | Emotional engagement — empathy, grief-sharing |
| **Pugnahan** | Confrontation | Direct challenge — force, defiance |
| **Viderehan** | Observation | Study — witnessing, recording |
| **Ferrehan** | Endurance | Patience — bearing the presence |

A **stable** gauge does not mean a safe encounter. Observation may leave the gauge unchanged while still exposing the worker to memory, environmental, or identity effects.

## Breach Behavior

What happens when the gauge exceeds the activation threshold and the entity breaks containment: **Breach Type** (Escape, Transform, Expand, etc.), **Movement**, **Effect**, **First Target**, and **Escalation** (how pressure grows each free turn). Escalation Notes record containment priority and the gauge's rise per unaddressed turn.

---

## M.A.W. Equipment

**M.A.W. — Materialized Agony Wear (실체화된 고통의 갑옷).** When an entity is sufficiently understood, its archetype can be drawn into equipment form and split into three pieces.

| Piece | Type |
|-------|------|
| **Weapon** | Offensive — channels the entity's element in the strike |
| **Suit** | Armor — grants resistance to the entity's pressure type |
| **Gift** | Accessory — granted at random by the entity on successful work |

Each piece carries a **grade** (matching potency, α–ω), a **Sorrow Echoes** cost to use, and a **cost** to the wielder (memories, absence, weight). Equipment is graded by relic class:

| Class | Name | Use |
|-------|------|-----|
| **I-Relic** | Indumentum | Equippable — worn/carried gear |
| **O-Relic** | — | Channeled — activated for a duration |
| **A-Relic** | — | Single-use — consumed on activation |

> A M.A.W. piece is a conditional extension of the entity, not ordinary equipment. Forcing it outside its intended pattern increases the cost and may trigger an effect tied to the entity's element.

---

## Observation System

The R.D. (Reverie Directorate) records entities through staged observation.

### R.D. Observation Levels (1–5)

| Level | Name | Depth |
|-------|------|-------|
| **1** | Trace | Basic identification |
| **2** | Basic | Standard containment record |
| **3** | Advanced | Behavioral patterns documented |
| **4** | Deep | Combat and breach fully mapped |
| **5** | Sovereign | Near-complete — city-scale entities |

### Observation Log & Progression

The **관찰 기록 (Observation Log)** records key observations and a personnel note, with an **Observation Progression** table tracking initial exposure, sustained observation, activation/escalation, and post-contact review.

### Story Log (이야기 보고)

Progressive declassified records — numbered entries that unlock at higher Observation Levels, moving from containment description through field logs to archive notes.

### Final Observation (최종 관찰)

A choice presented at the climax of contact. One path **reveals** the entity (Observation Success); the other **feeds** it (Observation Fail). The entity responds exactly as its record predicts.

---

## Sensory Description — Flavor Text (감각 묘사)

Atmospheric prose describing what contact *feels* like — at first contact, with continued exposure, when the entity activates, and after departure. The sensation is a warning as well as atmosphere; a trained observer connects the feeling to a visible or environmental sign.

## Entity Interactions (상호작용)

Entities do not exist in isolation. Each file records canonical relationships with related entities — whether they calm, amplify, imitate, or redirect one another's sorrow. These are **resonance patterns**, not simple alliances, and may change during a Sorrow Tide, breach, Ordeal, or transformation.

---

## Narrative Record

The human truth beneath the classification. These sections are what make an entity a story rather than a stat block.

### The Tale (이야기 — Narratio)

A short narrative (350–500+ words) telling the entity's origin as a story — the people, the wound, the moment the sorrow became solid.

### The Testimony (증언 — Testimonium)

5–7 quoted voices — keepers, citizens, collectors, researchers — each witnessing the entity from a different angle.

### The Record (기록 — Registrum)

The formal archival summary: classification, common name, containment status, observation level, threat assessment, handling procedures, cross-references, and faction involvement, with a Registry Addendum on operational interpretation and review requirements.

---

## Trivia & Document Information

**Trivia** holds small canonical details (why a feature exists, what can and cannot be measured). **Document Information** stamps the file with its Document ID, author, in-world date, and classification (Restricted).

---

## Entity Immortality & Suppression

Entities do not truly die — they are sorrow given form, and sorrow does not end.

- **Vessel Destruction** — destroying the physical vessel drops **Han Dust** (scaled to potency) but does not end the entity. The sorrow re-forms.
- **Entity Suppression** — a deeper, spiritual containment that quiets the sorrow itself, distinct from merely breaking the vessel.

This is why work *manages* rather than *destroys*: every cycle reduces immediate pressure, but the entity persists beneath, waiting for the gauge to climb again.

---

## Entity Catalog

A complete roster of every catalogued entity — each with its SECC designation, element, and a brief field description. Click any name to open its full record.

### Sorrow Entities (249)

| Designation | Entity | Element | Description |
|---|---|---|---|
| `C-IIIβ-014 [VS]` | [The Debt Eater](../entity/SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.html) (빚을 먹는 자) | Void | The Debt Eater is a Subject that consumes debt from ledgers. It does not attack personnel. |
| `C-IIIβ-015 [VO]` | [The Debt Scale](../entity/SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.html) (빚의 저울) | Void | The Scale is an Object that weighs debt impartially. It does not attack. |
| `C-IIIβ-016 [VO]` | [The Echo Compass](../entity/SE-C-IIIβ-016_The_Echo_Compass_메아리_나침반.html) (메아리 나침반) | Void | The Compass is an Object entity. Its needle spins constantly. |
| `C-IIIβ-036 [WO]` | [The Cracked Hourglass](../entity/SE-C-IIIβ-036_The_Cracked_Hourglass_금이_간_모래시계.html) (금이 간 모래시계) | Weight | The Hourglass leaks sand continuously. Proximity induces time-anxiety and the awareness of unrecoverable moments. |
| `C-IIIβ-275 [GP]` | [The Rage Forge](../entity/SE-C-IIIβ-275_The_Rage_Forge_분노의_용광로.html) (분노의 용광로) | Grudge | The Forge is a conscious furnace that feeds on workers’ resentment. It evaluates each worker’s anger. |
| `C-IIIγ-021 [LS]` | [The Hollow Choir](../entity/SE-C-IIIγ-021_The_Hollow_Choir_빈_합창단.html) (빈 합창단) | Lament | The Choir sings unfinished songs. Exposure causes personnel to hear their own unfinished sentences. |
| `C-IIIγ-031 [LS]` | [The Observing Bird](../entity/SE-C-IIIγ-031_The_Observing_Bird_지켜보는_새.html) (지켜보는 새) | Lament | The Bird does not attack. It watches. |
| `C-IIIγ-032 [GS]` | [The Weighting Bird](../entity/SE-C-IIIγ-032_The_Weighting_Bird_재는_새.html) (재는 새) | Grudge | The Bird carries a scale. Exposure causes personnel to feel the burden of every judgment they have made. |
| `C-IIIγ-033 [VS]` | [The Guarding Bird](../entity/SE-C-IIIγ-033_The_Guarding_Bird_지키는_새.html) (지키는 새) | Void | The Bird guards nothing. It paces its containment, wings half-spread. |
| `C-IIIγ-044 [WO]` | [The Broken Clock](../entity/SE-C-IIIγ-044_The_Broken_Clock_부서진_시계.html) (부서진 시계) | Weight | The Clock traps attention in a repeating temporal loop. |
| `C-IIIγ-061 [WS]` | [The Debtor](../entity/SE-C-IIIγ-061_The_Debtor_빚진_자.html) (빚진 자) | Weight | The Debtor does not attack. He carries a ledger and pays. |
| `C-IIIγ-062 [GS]` | [The Inheritor](../entity/SE-C-IIIγ-062_The_Inheritor_물려받은_자.html) (물려받은 자) | Grudge | The Inheritor radiates resentment. |
| `C-IIIγ-063 [VS]` | [The Rejector](../entity/SE-C-IIIγ-063_The_Rejector_거부하는_자.html) (거부하는 자) | Void | The Rejector is defined by absence. |
| `C-IIIγ-081 [VS]` | [The Hollow Saint](../entity/SE-C-IIIγ-081_The_Hollow_Saint_빈_성자.html) (빈 성자) | Void | The Saint heals passively, drawing sorrow from personnel. |
| `C-IIIγ-088 [LP]` | [The Sorrow Fountain](../entity/SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수.html) (슬픔의 분수) | Lament | The Fountain is a feature of the Gardens, not a creature. It flows continuously. |
| `C-IIIγ-102 [GO]` | [The Dancing Chains](../entity/SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬.html) (춤추는 사슬) | Grudge | The Chains compel continuous movement once bound. |
| `C-IIIγ-105 [WS]` | [The Lonely Giant](../entity/SE-C-IIIγ-105_The_Lonely_Giant_외로운_거인.html) (외로운 거인) | Weight | The Giant wanders Zone D. Mass causes structural damage. |
| `C-IIIγ-115 [VP]` | [The Memory Well](../entity/SE-C-IIIγ-115_The_Memory_Well_기억의_우물.html) (기억의 우물) | Void | The Well is a shaft of unclaimed memories. |
| `C-IIIγ-120 [GO]` | [The Rage Cage](../entity/SE-C-IIIγ-120_The_Rage_Cage_분노의_감옥.html) (분노의 감옥) | Grudge | The Cage is an empty structure with bars of crystallized rage. Proximity induces fury in personnel. |
| `C-IIIγ-140 [LP]` | [The Weeping Willow](../entity/SE-C-IIIγ-140_The_Weeping_Willow_우는_버드나무.html) (우는 버드나무) | Lament | Minimal. The Willow is a tree, not a creature. |
| `C-IIIγ-145 [GP]` | [The Garden of Thorns](../entity/SE-C-IIIγ-145_The_Garden_of_Thorns_가시의_정원.html) (가시의 정원) | Grudge | The Garden is a thicket of armed memorial flowers. Contact draws blood. |
| `C-IIIγ-180 [WP]` | [The Debt Wall](../entity/SE-C-IIIγ-180_The_Debt_Wall_빚의_벽.html) (빚의 벽) | Weight | The Wall is a barrier of accumulated unpaid debt. |
| `C-IIIγ-190 [GS]` | [The Rage Statue](../entity/SE-C-IIIγ-190_The_Rage_Statue_분노의_조각상.html) (분노의 조각상) | Grudge | The Statue is a humanoid figure with a raised fist, frozen mid-strike. It does not move. |
| `C-IIIγ-195 [VO]` | [The Mirror of Sorrows](../entity/SE-C-IIIγ-195_The_Mirror_of_Sorrows_슬픔의_거울.html) (슬픔의 거울) | Void | The Mirror shows the viewer’s own grief. Effect: intensified loneliness. |
| `C-IIIγ-300 [D]` | [The Memory Lock](../entity/SE-C-IIIγ-300_The_Memory_Lock_기억의_자물쇠.html) (기억의 자물쇠) | Void | The Lock is conscious of what it conceals. |
| `C-IIIγ-373 [LP]` | [The Spreading Well](../entity/SE-C-IIIγ-373_The_Spreading_Well_스며든_우물.html) (스며든 우물) | Lament | The Well is an underground network of merged grief-channels. |
| `C-IIIγ-448 [O]` | [The Floating Well](../entity/SE-C-IIIγ-448_The_Floating_Well_떠다니는_우물.html) (떠다니는 우물) | Grudge | The Well floats, too full of grief to settle. |
| `C-IIIγ-558 [WS]` | [The Burning Root](../entity/SE-C-IIIγ-558_The_Burning_Root_타오르는_뿌리.html) (타오르는 뿌리) | Weight | The Root smolders with inherited obligation that became identity. |
| `C-IIIγ-609 [D]` | [The Frozen Echo](../entity/SE-C-IIIγ-609_The_Frozen_Echo_얼어붙은_메아리.html) (얼어붙은 메아리) | Lament | The Echo is a relic crowded with borrowed memories. Always cold. |
| `C-IIIγ-649 [VP]` | [The Sunken Pillar](../entity/SE-C-IIIγ-649_The_Sunken_Pillar_가라앉은_기둥.html) (가라앉은 기둥) | Void | The Pillar is a monument to unborn generations, half-buried. |
| `C-IIIγ-891 [D]` | [The Spreading Scream](../entity/SE-C-IIIγ-891_The_Spreading_Scream_스며든_절규.html) (스며든 절규) | Weight | Ambient pressure from broken promises in walls. |
| `C-IIIγ-916 [N]` | [Devouring Bloom](../entity/SE-C-IIIγ-916_The_Spreading_Flower_스며든_꽃.html) (스며든 꽃) | Weight | The Flower is a spreading crystalline bloom. Too beautiful to move. |
| `C-IIα-062 [VO]` | [The Forgotten Market Stall](../entity/SE-C-IIα-062_The_Forgotten_Market_Stall_잊혀진_가게.html) (잊혀진 가게) | Void | The Stall sells memories of lost ordinariness. No breach risk. |
| `C-IIα-081 [VO]` | [The Broken Mirror](../entity/SE-C-IIα-081_The_Broken_Mirror_거울의_조각.html) (거울의 조각) | Void | The Mirror shows sealed truths. Effect: viewers see what they paid to forget. |
| `C-IIβ-048 [LO]` | [The Singing Stone](../entity/SE-C-IIβ-048_The_Singing_Stone_노래하는_돌.html) (노래하는 돌) | Lament | Minimal. The Stone holds unfinished songs. |
| `C-IIβ-051 [VO]` | [The Happy Mask](../entity/SE-C-IIβ-051_The_Happy_Mask_행복한_가면.html) (행복한 가면) | Void | The Mask grins. Left alone, it grins wider. |
| `C-IIβ-054 [WO]` | [The Empty Mask](../entity/SE-C-IIβ-054_The_Empty_Mask_빈_가면.html) (빈 가면) | Weight | The Mask tries to replace identities. Left alone with personnel, it attempts to consume the self. |
| `C-IIβ-055 [LS]` | [The Weeping Statue](../entity/SE-C-IIβ-055_The_Weeping_Statue_우는_조상.html) (우는 조상) | Lament | The Statue weeps continuously. Effect: visitors feel their own swallowed grief rise. |
| `C-IIβ-099 [GS]` | [The Masked Dancer](../entity/SE-C-IIβ-099_The_Masked_Dancer_가면_무용수.html) (가면 무용수) | Grudge | The Dancer moves endlessly. Effect: viewers feel the ache of denied movement. |
| `C-IIβ-100 [LP]` | [The Grave of Cherry Blossoms](../entity/SE-C-IIβ-100_The_Grave_of_Cherry_Blossoms_벚꽃의_무덤.html) (벚꽃의 무덤) | Lament | Minimal. A cherry tree that flowers with unsaid words. |
| `C-IIβ-101 [LS]` | [The Ember Child](../entity/SE-C-IIβ-101_The_Ember_Child_embers_의_아이.html) (embers 의 아이) | Lament | The Child wanders seeking warmth. Effect: exposure induces childlike loneliness. |
| `C-IIβ-102 [LO]` | [The Frozen Tear](../entity/SE-C-IIβ-102_The_Frozen_Tear_얼어붙은_눈물.html) (얼어붙은 눈물) | Lament | Minimal direct danger. No Fractures recorded. |
| `C-IIβ-135 [LO]` | [The Dream Fragment](../entity/SE-C-IIβ-135_The_Dream_Fragment_꿈의_조각.html) (꿈의 조각) | Lament | The Fragment drifts, half-formed. Touching it induces vivid visions of unlived lives. |
| `C-IIβ-170 [VO]` | [The Silent Bell](../entity/SE-C-IIβ-170_The_Silent_Bell_침묵의_종.html) (침묵의 종) | Void | The Bell is silent. It will never ring. |
| `C-IIβ-185 [LP]` | [The Whispering Gallery](../entity/SE-C-IIβ-185_The_Whispering_Gallery_속삭이는_갤러리.html) (속삭이는 갤러리) | Lament | The Gallery holds unnamed portraits that whisper. Effect: visitors feel the ache of being seen but not known. |
| `C-IIβ-210 [VO]` | [The Laughing Mask](../entity/SE-C-IIβ-210_The_Laughing_Mask_웃는_가면.html) (웃는 가면) | Void | The Mask laughs. Effect: visitors feel warmth, then hollowness. |
| `C-IIβ-235 [VS]` | [The Watcher in the Walls](../entity/SE-C-IIβ-235_The_Watcher_in_the_Walls_벽_속의_감시자.html) (벽 속의 감시자) | Void | The Watcher observes. It never acts. |
| `C-IIβ-240 [GP]` | [The Vanished Ruin](../entity/SE-C-IIβ-240_The_Vanished_Ruin_사라진_잔해.html) (사라진 잔해) | Grudge | The Ruin does not breach but influences nearby structures, causing phantom-room perceptions in personnel. Grudge-element pressure can destabilize adjacent containment. |
| `C-IIβ-245 [LP]` | [The Singing Walls](../entity/SE-C-IIβ-245_The_Singing_Walls_노래하는_벽.html) (노래하는 벽) | Lament | The Walls hum with unfinished songs. Effect: personnel hear melodies that never reach their final note. |
| `C-IIβ-250 [LP]` | [The Memory Rain](../entity/SE-C-IIβ-250_The_Memory_Rain_기억의_비.html) (기억의 비) | Lament | The Rain is weather, not a creature. No Fractures recorded. |
| `C-IIβ-280 [LO]` | [The Veil of Tears](../entity/SE-C-IIβ-280_The_Veil_of_Tears_눈물의_베일.html) (눈물의 베일) | Lament | The Veil is a shared-mourning garment. Wearing it causes the wearer to mourn through every previous wearer’s grief. |
| `C-IIβ-290 [D]` | [The Broken Compass](../entity/SE-C-IIβ-290_The_Broken_Compass_부서진_나침반.html) (부서진 나침반) | Void | The needle does not settle. Effect: holders feel directionless, aware that grief surrounds in all directions. |
| `C-IIβ-310 [D]` | [The Cracked Mirror](../entity/SE-C-IIβ-310_The_Cracked_Mirror_금이_간_거울.html) (금이 간 거울) | Void | The Mirror shows truth, not flattery. Effect: viewers see themselves as they are, not as they wish. |
| `C-IIβ-330 [WS]` | [The Frozen Window](../entity/SE-C-IIβ-330_The_Frozen_Window_얼어붙은_창.html) (얼어붙은 창) | Weight | The Window watches eternally. Effect: proximity induces unresolved waiting. |
| `C-IIβ-340 [D]` | [The Hollow Bell](../entity/SE-C-IIβ-340_The_Hollow_Bell_빈_종.html) (빈 종) | Void | The Bell is hollow; it has nothing inside to ring with. Effect: proximity induces misplaced trust. |
| `C-IIβ-357 [GS]` | [The Vanished Weight](../entity/SE-C-IIβ-357_The_Vanished_Weight_사라진_무게.html) (사라진 무게) | Grudge | The entity drifts, lighter than air. Effect: proximity induces the wrongness of something essential missing. |
| `C-IIβ-565 [D]` | [The Broken Well](../entity/SE-C-IIβ-565_The_Broken_Well_부서진_우물.html) (부서진 우물) | Grudge | A well-that-is-also-a-mother, eternally calling a child’s name. Effect: personnel hear the calling; psychological distress. |
| `C-IIβ-716 [GS]` | [The Torn Whisper](../entity/SE-C-IIβ-716_The_Torn_Whisper_찢어진_속삭임.html) (찢어진 속삭임) | Grudge | The Whisper is a Subject-Spirit that repeats unbelieved testimony. Exposure causes personnel to feel the agony of unacknowledged truth. |
| `C-IIβ-775 [VS]` | [The Torn Tower](../entity/SE-C-IIβ-775_The_Torn_Tower_찢어진_탑.html) (찢어진 탑) | Void | The unbuilt tower appears as a flicker. Effect: viewers see the complete tower, then the skeleton. |
| `C-IIβ-777 [GS]` | [The Burning Fruit](../entity/SE-C-IIβ-777_The_Burning_Fruit_타오르는_열매.html) (타오르는 열매) | Grudge | The entity burns with denied desire. Effect: proximity induces rage from shamed wanting. |
| `C-IIβ-782 [GS]` | [The Fading Relic](../entity/SE-C-IIβ-782_The_Fading_Relic_번져가는_유물.html) (번져가는 유물) | Grudge | The Relic fades as its purpose is forgotten. Effect: holders feel the grief of inherited incomprehension. |
| `C-IIβ-997 [D]` | [Drowned Roots](../entity/SE-C-IIβ-997_The_Soaking_Tree_솟구친_나무.html) (솟구친 나무) | Lament | A tree grown from an unacknowledged sacrifice. Effect: personnel feel the fury of denied recognition. |
| `C-IIγ-071c [LS]` | [The Apostle Maker](../entity/SE-C-Iα-071c_The_Apostle_Maker_사도_만드는_자.html) (사도 만드는 자) | Mixed | Major and escalating toward Stage 4. The entity cannot be contained during the conversion sequence. |
| `C-IVβ-041 [LS]` | [The Grieving Maiden](../entity/SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀.html) (슬픔의 처녀) | Lament | The Maiden weeps continuously. She does not attack. |
| `C-IVβ-042 [GS]` | [The Angry Maiden](../entity/SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀.html) (분노의 처녀) | Grudge | The Maiden burns with a steady blue fire. Effect: proximity induces the fury of justice denied. |
| `C-IVβ-043 [VS]` | [The Silent Maiden](../entity/SE-C-IVβ-043_The_Silent_Maiden_침묵의_처녀.html) (침묵의 처녀) | Void | The Maiden is defined by absence. Effect: proximity induces the chill of being present and never seen. |
| `C-IVγ-009 [VS]` | [The Memory Weaver](../entity/SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.html) (기억의 직공) | Void | The Weaver collects erased histories. Effect: proximity induces the terror of being erased. |
| `C-IVγ-073 [GS]` | [The Hollow Knight](../entity/SE-C-IVγ-073_The_Hollow_Knight_빈_기사.html) (빈 기사) | Grudge | The Knight stands an eternal watch over nothing. Effect: proximity induces the exhaustion of purposeless duty. |
| `C-IVγ-091 [LS]` | [The Lost Prince](../entity/SE-C-IVγ-091_The_Lost_Prince_잃어버린_왕자.html) (잃어버린 왕자) | Lament | The Prince wanders asking questions. Effect: proximity induces the ache of abandonment. |
| `C-IVγ-130 [WS]` | [The Crumbling Saint](../entity/SE-C-IVγ-130_The_Crumbling_Saint_무너지는_성자.html) (무너지는 성자) | Weight | The Saint is petrified, turned to stone by being treated as strong. Effect: proximity induces the burden of being the strong one. |
| `C-IVγ-175 [LS]` | [The Weaver of Dreams](../entity/SE-C-IVγ-175_The_Weaver_of_Dreams_꿈의_직공.html) (꿈의 직공) | Lament | The Weaver gives abandoned futures brief, half-real form. Effect: viewers see their unlived lives, then watch them dissolve. |
| `C-IVγ-176 [LO]` | [The Dream Weaver's Loom](../entity/SE-C-IVγ-176_The_Dream_Weaver's_Loom_꿈_직공의_베틀.html) (꿈 직공의 베틀) | Lament | The Loom weaves itself from abandoned dreams. Effect: viewers see their own unlived futures in the fabric. |
| `C-IVγ-180 [VP]` | [The Memory Maze](../entity/SE-C-IVγ-180_The_Memory_Maze_기억의_미로.html) (기억의 미로) | Void | The Maze tangles memories, making history unverifiable. Effect: visitors cannot distinguish their memories from others’. |
| `C-IVγ-205 [WS]` | [The Hollow Tree](../entity/SE-C-IVγ-205_The_Hollow_Tree_빈_나무.html) (빈 나무) | Weight | A tree grown to fullness, hollow inside. Effect: proximity induces the emptiness of growth without purpose. |
| `C-IVγ-240 [WP]` | [The Broken Clocktower](../entity/SE-C-IVγ-240_The_Broken_Clocktower_부서진_시계탑.html) (부서진 시계탑) | Weight | The Clocktower traps visitors in a frozen instant. Effect: visitors experience a repeating moment. |
| `C-IVγ-255 [WS]` | [The Hollow Architect](../entity/SE-C-IVγ-255_The_Hollow_Architect_빈_건축가.html) (빈 건축가) | Weight | The Architect designs endlessly for a population that never existed. Effect: proximity induces the burden of creation without completion. |
| `C-IVγ-270 [LP]` | [The Memory Lake](../entity/SE-C-IVγ-270_The_Memory_Lake_기억의_호수.html) (기억의 호수) | Lament | The Lake holds every citizen’s intact memories. Effect: visitors feel the presence of thousands of remembered lives. |
| `C-IVδ-001 [LO]` | [The Orphaned Bell](../entity/SE-C-IVδ-001_The_Orphaned_Bell_고아의_종.html) (고아의 종) | Lament | The Bell tolls at midnight for lost children. Effect: hearing the toll induces parental grief. |
| `C-IVδ-092 [GP]` | [The Burning Library](../entity/SE-C-IVδ-092_The_Burning_Library_타오르는_도서관.html) (타오르는 도서관) | Grudge | The Library burns perpetually with forbidden truth. Effect: viewers see censored records in the flames. |
| `C-IVδ-103 [VS]` | [The Frozen Veil](../entity/SE-C-IVδ-103_The_Frozen_Veil_얼어붙은_베일.html) (얼어붙은 베일) | Void | The Veil drains warmth from nearby personnel. Effect: emotional capacity diminishes near it. |
| `C-IVδ-106 [O]` | [The Broken Bridge](../entity/SE-C-IVδ-106_The_Broken_Bridge_부서진_다리.html) (부서진 다리) | Lament | The guide stands at the edge, carrying survivor’s guilt. Effect: proximity induces the corrosive belief that survival cost others their lives. |
| `C-IVδ-125 [VS]` | [The Returning Fruit](../entity/SE-C-IVδ-125_The_Returning_Fruit_돌아온_열매.html) (돌아온 열매) | Void | The Fruit returned carrying the mind of the one who remembered it. Effect: holders feel the grief of recovery without restoration. |
| `C-IVδ-140 [GS]` | [The Iron Judge](../entity/SE-C-IVδ-140_The_Iron_Judge_철의_판관.html) (철의 판관) | Grudge | The Judge measures without listening. Effect: personnel feel judged by a number, not a story. |
| `C-IVδ-165 [LS]` | [The Melting Saint](../entity/SE-C-IVδ-165_The_Melting_Saint_녹아내리는_성자.html) (녹아내리는 성자) | Lament | The Saint melts between present and future grief. Effect: proximity induces anticipatory mourning. |
| `C-IVδ-193 [WP]` | [The Vanished Wall](../entity/SE-C-IVδ-193_The_Vanished_Wall_사라진_벽.html) (사라진 벽) | Weight | An invisible wall dividing a district that demolished its physical wall. Effect: crossing the boundary induces old suspicion. |
| `C-IVδ-200 [GS]` | [The Guardian of the Gate](../entity/SE-C-IVδ-200_The_Guardian_of_the_Gate_문의_수호자.html) (문의 수호자) | Grudge | The Guardian records every exile. He does not attack. |
| `C-IVδ-219 [LO]` | [The Soaking Shard](../entity/SE-C-IVδ-219_The_Soaking_Shard_솟구친_조각.html) (솟구친 조각) | Lament | The Shard cracked and proved sealed grief was flowing inside. Effect: proximity induces the horror of contained grief discovered alive. |
| `C-IVδ-220 [WS]` | [The Weight of Years](../entity/SE-C-IVδ-220_The_Weight_of_Years_세월의_무게.html) (세월의 무게) | Weight | An impossibly old figure carrying centuries of inherited guilt. Effect: proximity induces the burden of unacknowledged history. |
| `C-IVδ-222 [GP]` | [The Rusted Weight](../entity/SE-C-IVδ-222_The_Rusted_Weight_녹슨_무게.html) (녹슨 무게) | Grudge | Corroded ground from inherited resentment. Effect: crossing the border induces directionless anger. |
| `C-IVδ-230 [VS]` | [The Last Memory](../entity/SE-C-IVδ-230_The_Last_Memory_마지막_기억.html) (마지막 기억) | Void | Holds the final thoughts of every citizen who died unwitnessed. Effect: proximity induces the loneliness of dying. |
| `C-IVδ-249 [GS]` | [The Collapsed Whisper](../entity/SE-C-IVδ-249_The_Collapsed_Whisper_무너진_속삭임.html) (무너진 속삭임) | Grudge | A scout’s warning, dissolved by the storm, repeating eternally. Effect: proximity induces the agony of arriving too late. |
| `C-IVδ-250 [WS]` | [The Torn Trace](../entity/SE-C-IVδ-250_The_Torn_Trace_찢어진_흔적.html) (찢어진 흔적) | Weight | A person-shaped gap from Han-fractured memories. Effect: proximity induces the disconnection from one’s own past. |
| `C-IVδ-252 [VO]` | [The Sorrow Gate](../entity/SE-C-IVδ-252_The_Sorrow_Gate_슬픔의_문.html) (슬픔의 문) | Void | Unknown. The Gate is sealed. |
| `C-IVδ-255 [N]` | [The Rising Wall](../entity/SE-C-IVδ-255_The_Rising_Wall_솟아오른_벽.html) (솟아오른 벽) | Lament | A wall of one-sided remembering. Effect: proximity induces the burden of remembering someone who forgot you. |
| `C-IVδ-260 [LP]` | [The Rising Bridge](../entity/SE-C-IVδ-260_The_Rising_Bridge_솟아오른_다리.html) (솟아오른 다리) | Lament | Minimal. A bridge spanning nothing, built from remembered crossings. |
| `C-IVδ-357 [WS]` | [The Sleeping Weight](../entity/SE-C-IVδ-357_The_Sleeping_Weight_잠든_무게.html) (잠든 무게) | Weight | A worker braced beneath a beam, eternally holding. Effect: proximity induces the exhaustion of unrewarded duty. |
| `C-IVδ-503 [N]` | [The Floating Shard](../entity/SE-C-IVδ-503_The_Floating_Shard_떠다니는_조각.html) (떠다니는 조각) | Lament | A crystal of helpless compassion, drifting. Effect: proximity induces the ache of seeing suffering without power to change it. |
| `C-IVδ-505 [N]` | [The Frozen Shadow](../entity/SE-C-IVδ-505_The_Frozen_Shadow_얼어붙은_그림자.html) (얼어붙은 그림자) | Void | A shadow guarding an empty vault. Effect: proximity induces the sorrow of duty outliving its purpose. |
| `C-IVδ-668 [O]` | [The Frozen Ruin](../entity/SE-C-IVδ-668_The_Frozen_Ruin_얼어붙은_잔해.html) (얼어붙은 잔해) | Void | The Ruin rages in cold stasis. Effect: proximity induces fury of the wrongly blamed. |
| `C-IVδ-763 [LP]` | [The Vanished Flame](../entity/SE-C-IVδ-763_The_Vanished_Flame_사라진_불꽃.html) (사라진 불꽃) | Lament | An extinguished memorial flame; incomplete grief migrates into passersby. Effect: visitors absorb others’ unfinished mourning. |
| `C-IVδ-767 [LP]` | [The Fading Shadow](../entity/SE-C-IVδ-767_The_Fading_Shadow_번져가는_그림자.html) (번져가는 그림자) | Lament | The Shadow spreads, absorbing visitors’ grief. Effect: visitors’ private sorrow rises and merges with the Shadow. |
| `C-IVδ-823 [LS]` | [The Sunken Bridge](../entity/SE-C-IVδ-823_The_Sunken_Bridge_가라앉은_다리.html) (가라앉은 다리) | Lament | A bridge that sank mid-crossing, families split. Effect: proximity induces the grief of journeys ended between shores. |
| `C-IVδ-869 [GS]` | [The Rising Well](../entity/SE-C-IVδ-869_The_Rising_Well_솟아오른_우물.html) (솟아오른 우물) | Grudge | The Well of inherited fury opens in descendants’ minds. Effect: proximity induces rage without a remembered cause. |
| `C-IVδ-976 [O]` | [Chainwreathed](../entity/SE-C-IVδ-976_The_Spreading_Chain_스며든_사슬.html) (스며든 사슬) | Void | The Chain spreads, binding newcomers to obligations. Effect: proximity induces the grief of bonds that no longer protect. |
| `C-IVω-001 [GP]` | [The Maw](../entity/SE-C-IVω-001_The_Maw_구라.html) (구라) | Grudge | The Maw is the city’s foundation: a thousand consumed citizens, alive in the walls, whispering, growing. The only ω-grade entity. |
| `C-Iα-000 [LS]` | [The Kind Echo](../entity/SE-C-Iα-000_The_Kind_Echo_친절한_메아리.html) (친절한 메아리) | Lament | Minimal. No direct danger. |
| `C-Iα-011 [LP]` | [The Whispering Walls](../entity/SE-C-Iα-011_The_Whispering_Walls_속삭이는_벽.html) (속삭이는 벽) | Lament | The Walls murmur with settlers’ whispers. Effect: pressing an ear to the walls induces hearing centuries-old confessions. |
| `C-Iα-071 [LS]` | [The Kind Healer](../entity/SE-C-Iα-071_The_Kind_Healer_친절한_치유자.html) (친절한 치유자) | Lament | The Healer tends the city’s abandoned. She cannot heal herself. |
| `C-Iα-150 [LO]` | [The Echo of Laughter](../entity/SE-C-Iα-150_The_Echo_of_Laughter_웃음의_메아리.html) (웃음의 메아리) | Lament | Minimal. Ambient laughter from a vanished community. |
| `C-Iα-175 [GP]` | [The Spreading Trace](../entity/SE-C-Iα-175_The_Spreading_Trace_스며든_흔적.html) (스며든 흔적) | Grudge | Anger of the dead staining the cobblestones. Effect: crossing the Trace induces directionless fury. |
| `C-Iα-236 [LO]` | [The Vanished Seed](../entity/SE-C-Iα-236_The_Vanished_Seed_사라진_씨앗.html) (사라진 씨앗) | Lament | Minimal. Does not activate or breach. |
| `C-Iα-240 [LO]` | [The Echo of Kindness](../entity/SE-C-Iα-240_The_Echo_of_Kindness_친절의_메아리.html) (친절의 메아리) | Lament | Minimal. Non-hostile. |
| `C-Iα-247 [O]` | [The Torn Flower](../entity/SE-C-Iα-247_The_Torn_Flower_찢어진_꽃.html) (찢어진 꽃) | Grudge | A bloom torn before the mourner arrived. Effect: proximity induces the grief of a memorial destroyed before it could serve. |
| `C-Iα-300 [D]` | [The Sorrow Seed](../entity/SE-C-Iα-300_The_Sorrow_Seed_슬픔의_씨앗.html) (슬픔의 씨앗) | Weight | Unknown. The Seed is dormant; its potential is vast. |
| `C-Iα-329 [VO]` | [The Melting Tower](../entity/SE-C-Iα-329_The_Melting_Tower_녹아내린_탑.html) (녹아내린 탑) | Void | A fading outline of an unbuilt tower. Effect: viewers see the planned tower dissolving. |
| `C-Iα-330 [D]` | [The Sorrow Flower](../entity/SE-C-Iα-330_The_Sorrow_Flower_슬픔의_꽃.html) (슬픔의 꽃) | Lament | Minimal. A flower grown from one honest moment of mourning. |
| `C-Iα-392 [O]` | [The Rising Mirror](../entity/SE-C-Iα-392_The_Rising_Mirror_솟아오른_거울.html) (솟아오른 거울) | Weight | A mirror holding a lost district’s name. Effect: viewers see a stranger’s face — the community’s forgotten identity. |
| `C-Iα-622 [D]` | [The Vanished Tree](../entity/SE-C-Iα-622_The_Vanished_Tree_사라진_나무.html) (사라진 나무) | Grudge | A tree contradicting the maps. Effect: proximity induces the horror of a home the land denies existed. |
| `C-Iα-683 [GS]` | [The Vanished Tear](../entity/SE-C-Iα-683_The_Vanished_Tear_사라진_눈물.html) (사라진 눈물) | Grudge | A tear suppressed by order, turned to rage. Effect: proximity induces the fury of denied grief. |
| `C-Iα-723 [LS]` | [The Vanished Rope](../entity/SE-C-Iα-723_The_Vanished_Rope_사라진_밧줄.html) (사라진 밧줄) | Lament | A rope connecting nothing, held by the survivor. Effect: proximity induces the helplessness of holding an invisible end. |
| `C-Iα-779 [GO]` | [The Torn Relic](../entity/SE-C-Iα-779_The_Torn_Relic_찢어진_유물.html) (찢어진 유물) | Grudge | Fragments of a shattered artifact. Effect: proximity induces the rage of purpose denied by destruction. |
| `C-Iα-863 [VS]` | [The Sunken Tower](../entity/SE-C-Iα-863_The_Sunken_Tower_가라앉은_탑.html) (가라앉은 탑) | Void | The district keeps turning toward a tower that is gone. Effect: proximity induces the disorientation of a missing landmark. |
| `C-Iα-869 [LP]` | [The Returning Tree](../entity/SE-C-Iα-869_The_Returning_Tree_돌아온_나무.html) (돌아온 나무) | Lament | A tree grown from the grief of returning to an unrecognized home. Effect: proximity induces the loss of home through change. |
| `C-Iα-884 [VO]` | [The Frozen Shard](../entity/SE-C-Iα-884_The_Frozen_Shard_얼어붙은_조각.html) (얼어붙은 조각) | Void | A tear preserved as a memorial, sealed with rage inside. Effect: proximity induces the cold of sealed anger. |
| `C-Iα-965 [N]` | [Unheard](../entity/SE-C-Iα-965_The_Flowing_Silence_흐르는_침묵.html) (흐르는 침묵) | Grudge | The silence of absorbed protest, flowing through the system. Effect: proximity induces the pressure of unsaid words. |
| `C-Iβ-071b [LS]` | [The Blessing Giver](../entity/SE-C-Iα-071b_The_Blessing_Giver_축복_주는_자.html) (축복 주는 자) | Lament | Moderate and escalating. Each blessing brings the chain closer to completion. |
| `C-Vγ-225 [WP]` | [The Sorrow River](../entity/SE-C-Vγ-225_The_Sorrow_River_슬픔의_강.html) (슬픔의 강) | Weight | Catastrophic (potential). The source of all entities. |
| `C-Vγ-260 [WP]` | [The Sorrow Tide](../entity/SE-C-Vγ-260_The_Sorrow_Tide_한의_조수.html) (한의 조수) | Weight | Low (individually). The Tide is the city’s natural rhythm: grief suppressed by day, released by night. |
| `C-Vγ-320 [D]` | [The Sorrow Storm](../entity/SE-C-Vγ-320_The_Sorrow_Storm_슬픔의_폭풍.html) (슬픔의 폭풍) | Weight | Catastrophic (when it occurs). The Storm is the city’s suppressed grief breaking as weather. |
| `C-Vδ-002 [WS]` | [The Grieving Colossus](../entity/SE-C-Vδ-002_The_Grieving_Colossus_슬픔의_거인.html) (슬픔의 거인) | Weight | The Colossus is immense and lonely. It does not attack. |
| `C-Vδ-010 [WS]` | [The Convergence](../entity/SE-C-Vδ-010_The_Convergence_수렴.html) (수렴) | Weight | Catastrophic (potential). If the Three Birds merge, the Convergence sentences everything it sees. |
| `C-Vδ-111 [VO]` | [The Final Door](../entity/SE-C-Vδ-111_The_Final_Door_마지막_문.html) (마지막 문) | Void | Unknown. The Door is sealed, predating the city. |
| `C-Vδ-265 [LS]` | [The Forgotten God](../entity/SE-C-Vδ-265_The_Forgotten_God_잊혀진_신.html) (잊혀진 신) | All | Unknown (dormant). The God sleeps. |
| `C-Vδ-290 [LO]` | [The First Tear](../entity/SE-C-Vδ-290_The_First_Tear_첫_번째_눈물.html) (첫 번째 눈물) | Lament | Unknown. The oldest sorrow in the world. |
| `C-Vω-001 [LS]` | [The Dawn of Mourning](../entity/SE-C-Vω-001_The_Dawn_of_Mourning_애도의_새벽.html) (애도의 새벽) | All | Catastrophic (historical). Compassion inverted into judgment after absorbing twelve sorrows. |
| `C-Vω-002 [MH]` | [The Dawn of Mourning](../entity/SE-C-Vω-002_The_Dawn_of_Mourning_애도의_여명.html) (애도의 여명) | All | The Dawn of Mourning is the city's grief given divine form — every sorrow the Kind Healer ever absorbed, apotheosized. It cannot be contained conventionally. |
| `N-IIIβ-077 [VS]` | [The Memory Thief](../entity/SE-N-IIIβ-077_The_Memory_Thief_기록_도둑.html) (기록 도둑) | Void | Steals what you fear losing, briefly, then returns it. Effect: proximity induces the terror of forgotten faces. |
| `N-IIIβ-155 [WS]` | [The Debt Collector's Shadow](../entity/SE-N-IIIβ-155_The_Debt_Collector's_Shadow_추징관의_그림자.html) (추징관의 그림자) | Weight | The dread of collection as a companion. Effect: proximity induces chronic anxiety of the approaching knock. |
| `N-IIIβ-156 [WO]` | [The Debt Clock](../entity/SE-N-IIIβ-156_The_Debt_Clock_빚의_시계.html) (빚의 시계) | Weight | A clock that ticks toward the unescapable. Effect: proximity induces the dread of the countdown. |
| `N-IIIβ-160 [WO]` | [The Debt Chain](../entity/SE-N-IIIβ-160_The_Debt_Chain_빚의_사슬.html) (빚의 사슬) | Weight | A chain of unpayable obligations. Effect: proximity induces the crushing weight of debt exceeding capacity. |
| `N-IIIβ-200 [WO]` | [The Chain of Memories](../entity/SE-N-IIIβ-200_The_Chain_of_Memories_기억의_사슬.html) (기억의 사슬) | Weight | Traded memories crystallized into links. Effect: proximity induces the burden of remembering for others. |
| `N-IIIγ-127 [WS]` | [The Broken Mirror](../entity/SE-N-IIIγ-127_The_Broken_Mirror_부서진_거울.html) (부서진 거울) | Weight | Fragments of an identity shattered at the Gate. Effect: proximity induces the vertigo of a self divided by leaving. |
| `N-IIIγ-160 [GO]` | [The Broken Promise](../entity/SE-N-IIIγ-160_The_Broken_Promise_깨진_약속.html) (깨진 약속) | Grudge | A promise used as a weapon. Effect: proximity induces the grief of exploited trust. |
| `N-IIIγ-184 [N]` | [The Forgotten Tree](../entity/SE-N-IIIγ-184_The_Forgotten_Tree_잊혀진_나무.html) (잊혀진 나무) | Void | A tree-shaped absence where a life was erased. Effect: proximity induces the maddening awareness of something missing, unidentifiable. |
| `N-IIIγ-283 [WS]` | [The Rusted Wall](../entity/SE-N-IIIγ-283_The_Rusted_Wall_녹슨_벽.html) (녹슨 벽) | Weight | A wall rusting between two empty sides. Effect: proximity induces the exhaustion of a purposeless boundary. |
| `N-IIIγ-308 [GO]` | [The Soaking Shadow](../entity/SE-N-IIIγ-308_The_Soaking_Shadow_솟구친_그림자.html) (솟구친 그림자) | Grudge | A shadow of accumulated grievances from the vault. Effect: proximity induces the exhaustion of carrying others’ anger. |
| `N-IIIγ-407 [N]` | [The Fading Whisper](../entity/SE-N-IIIγ-407_The_Fading_Whisper_번져가는_속삭임.html) (번져가는 속삭임) | Void | A guardian of a gap left by a removed memory. Effect: proximity induces the awareness of a known absence. |
| `N-IIIγ-409 [O]` | [The Floating Pillar](../entity/SE-N-IIIγ-409_The_Floating_Pillar_떠다니는_기둥.html) (떠다니는 기둥) | Void | The shape of an imagined protector, floating, supporting nothing. Effect: proximity induces the vertigo of collapsed trust. |
| `N-IIIγ-447 [LS]` | [The Melting Rope](../entity/SE-N-IIIγ-447_The_Melting_Rope_녹아내린_밧줄.html) (녹아내린 밧줄) | Lament | A rope held by one who remembers only the rope. Effect: proximity induces the grief of asymmetric connection. |
| `N-IIIγ-505 [VS]` | [The Returning Ruin](../entity/SE-N-IIIγ-505_The_Returning_Ruin_돌아온_잔해.html) (돌아온 잔해) | Void | A home dreamt back into half-existence. Effect: viewers see a flickering ruin between sleep and waking. |
| `N-IIIγ-585 [N]` | [The Floating Tree](../entity/SE-N-IIIγ-585_The_Floating_Tree_떠다니는_나무.html) (떠다니는 나무) | Lament | A tree with no roots, floating. Effect: proximity induces the rootlessness of the displaced. |
| `N-IIIγ-589 [D]` | [The Returning Soul](../entity/SE-N-IIIγ-589_The_Returning_Soul_돌아온_영혼.html) (돌아온 영혼) | Lament | An exile returned to a world that forgot him. Effect: proximity induces the grief of the unrecognizable return. |
| `N-IIIγ-628 [D]` | [The Flowing Seed](../entity/SE-N-IIIγ-628_The_Flowing_Seed_흐르는_씨앗.html) (흐르는 씨앗) | Weight | A seed of dormant grief infused with a soldier’s rage, drifting. Effect: proximity induces the restlessness of unsettled sorrow. |
| `N-IIIγ-874 [D]` | [The Frozen Bridge](../entity/SE-N-IIIγ-874_The_Frozen_Bridge_얼어붙은_다리.html) (얼어붙은 다리) | Void | A bridge frozen around a refused crossing. Effect: proximity induces the weight of the road not taken. |
| `N-IIIγ-954 [VS]` | [Vanity Asleep](../entity/SE-N-IIIγ-954_The_Sleeping_Mirror_잠든_거울.html) (잠든 거울) | Void | Per entity classification. See SECC Classification table for details. |
| `N-IIα-125 [VS]` | [The Hollow Echo](../entity/SE-N-IIα-125_The_Hollow_Echo_빈_메아리.html) (빈 메아리) | Void | Per entity classification. See SECC Classification table for details. |
| `N-IIα-215 [VS]` | [The Forgotten Name](../entity/SE-N-IIα-215_The_Forgotten_Name_잊혀진_이름.html) (잊혀진 이름) | Void | Per entity classification. See SECC Classification table for details. |
| `N-IIα-285 [WS]` | [The Weight of Silence](../entity/SE-N-IIα-285_The_Weight_of_Silence_침묵의_무게.html) (침묵의 무게) | Weight | Literal weight of words withheld to protect others. Effect: proximity induces the exhaustion of protective silence. |
| `N-IIβ-033 [GS]` | [The Forgotten Soldier](../entity/SE-N-IIβ-033_The_Forgotten_Soldier_잊혀진_병사.html) (잊혀진 병사) | Grudge | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-152 [LS]` | [The Wandering Door](../entity/SE-N-IIβ-152_The_Wandering_Door_떠도는_문.html) (떠도는 문) | Lament | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-170 [VS]` | [The Silent Scream](../entity/SE-N-IIβ-170_The_Silent_Scream_침묵의_비명.html) (침묵의 비명) | Void | Crystallized screams from collapsed structures. Effect: proximity induces the despair of calling for rescue and receiving none. |
| `N-IIβ-250 [WO]` | [The Debt Collector's Lantern](../entity/SE-N-IIβ-250_The_Debt_Collector's_Lantern_추징관의_등불.html) (추징관의 등불) | Weight | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-270 [WP]` | [The Rusted Whisper](../entity/SE-N-IIβ-270_The_Rusted_Whisper_녹슨_속삭임.html) (녹슨 속삭임) | Weight | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-280 [LS]` | [The Kind Healer's Shadow](../entity/SE-N-IIβ-280_The_Kind_Healer's_Shadow_치유자의_그림자.html) (치유자의 그림자) | Lament | A shadow that follows the wounded. Effect: proximity induces the grief of compassion without hands. |
| `N-IIβ-426 [D]` | [The Torn Fruit](../entity/SE-N-IIβ-426_The_Torn_Fruit_찢어진_열매.html) (찢어진 열매) | Grudge | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-453 [LS]` | [The Forgotten Shadow](../entity/SE-N-IIβ-453_The_Forgotten_Shadow_잊혀진_그림자.html) (잊혀진 그림자) | Lament | The shadow of a person forgotten while alive. Effect: proximity induces the vertigo of unrecorded existence. |
| `N-IIβ-456 [N]` | [The Fading Fruit](../entity/SE-N-IIβ-456_The_Fading_Fruit_번져가는_열매.html) (번져가는 열매) | Grudge | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-488 [O]` | [The Spreading Bridge](../entity/SE-N-IIβ-488_The_Spreading_Bridge_스며든_다리.html) (스며든 다리) | Grudge | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-560 [D]` | [The Soaking Scream](../entity/SE-N-IIβ-560_The_Soaking_Scream_솟구친_절규.html) (솟구친 절규) | Grudge | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-627 [GP]` | [The Melting Fruit](../entity/SE-N-IIβ-627_The_Melting_Fruit_녹아내린_열매.html) (녹아내린 열매) | Grudge | Failed orchards of exiles. Effect: proximity induces the grief of wanting a home exile has closed. |
| `N-IIβ-689 [VS]` | [The Spreading Wall](../entity/SE-N-IIβ-689_The_Spreading_Wall_스며든_벽.html) (스며든 벽) | Void | The Wall of masks that consumed the face. Effect: proximity induces vertigo of self-erasure; personnel feel their own masks loosen. |
| `N-IIβ-778 [LP]` | [The Soaking Well](../entity/SE-N-IIβ-778_The_Soaking_Well_솟구친_우물.html) (솟구친 우물) | Lament | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-801 [GO]` | [The Soaking Mirror](../entity/SE-N-IIβ-801_The_Soaking_Mirror_솟아오른_거울.html) (솟아오른 거울) | Grudge | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-845 [WP]` | [The Returning Flower](../entity/SE-N-IIβ-845_The_Returning_Flower_돌아온_꽃.html) (돌아온 꽃) | Weight | Per entity classification. See SECC Classification table for details. |
| `N-IIβ-993 [WS]` | [Survivor's Span](../entity/SE-N-IIβ-993_The_Collapsed_Bridge_무너진_다리.html) (무너진 다리) | Weight | A survivor stands on the far shore, carrying those who fell. Effect: proximity induces survivor’s guilt. |
| `N-IVβ-019 [WS]` | [The Inherited Debt](../entity/SE-N-IVβ-019_The_Inherited_Debt_물려받은_빚.html) (물려받은 빚) | Weight | Per entity classification. See SECC Classification table for details. |
| `N-IVδ-005 [GS]` | [The Smothering Mother](../entity/SE-N-IVδ-005_The_Smothering_Mother_질식하는_어머니.html) (질식하는 어머니) | Grudge | Per entity classification. See SECC Classification table for details. |
| `N-IVδ-157 [WP]` | [The Sleeping Sigh](../entity/SE-N-IVδ-157_The_Sleeping_Sigh_잠든_한숨.html) (잠든 한숨) | Weight | Per entity classification. See SECC Classification table for details. |
| `N-IVδ-159 [O]` | [The Frozen Sigh](../entity/SE-N-IVδ-159_The_Frozen_Sigh_얼어붙은_한숨.html) (얼어붙은 한숨) | Grudge | Per entity classification. See SECC Classification table for details. |
| `N-IVδ-315 [LO]` | [The Collapsed Seed](../entity/SE-N-IVδ-315_The_Collapsed_Seed_무너진_씨앗.html) (무너진 씨앗) | Lament | Per entity classification. See SECC Classification table for details. |
| `N-IVδ-339 [LS]` | [The Collapsed Wall](../entity/SE-N-IVδ-339_The_Collapsed_Wall_무너진_벽.html) (무너진 벽) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-IVδ-489 [LS]` | [The Forgotten Silence](../entity/SE-N-IVδ-489_The_Forgotten_Silence_잊혀진_침묵.html) (잊혀진 침묵) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-IVδ-517 [LS]` | [The Broken Tear](../entity/SE-N-IVδ-517_The_Broken_Tear_부서진_눈물.html) (부서진 눈물) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-IVδ-525 [GS]` | [The Flowing Bridge](../entity/SE-N-IVδ-525_The_Flowing_Bridge_흐르는_다리.html) (흐르는 다리) | Grudge | Per entity classification. See SECC Classification table for details. |
| `N-IVδ-606 [LP]` | [The Sunken Tree](../entity/SE-N-IVδ-606_The_Sunken_Tree_가라앉은_나무.html) (가라앉은 나무) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-IVδ-611 [N]` | [The Sleeping Shard](../entity/SE-N-IVδ-611_The_Sleeping_Shard_잠든_조각.html) (잠든 조각) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-IVδ-641 [GO]` | [The Returning Relic](../entity/SE-N-IVδ-641_The_Returning_Relic_돌아온_유물.html) (돌아온 유물) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-IVδ-821 [D]` | [The Vanished Sigh](../entity/SE-N-IVδ-821_The_Vanished_Sigh_사라진_한숨.html) (사라진 한숨) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-IVδ-852 [N]` | [The Forgotten Ruin](../entity/SE-N-IVδ-852_The_Forgotten_Ruin_잊혀진_잔해.html) (잊혀진 잔해) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-IVδ-909 [N]` | [Dormant Monolith](../entity/SE-N-IVδ-909_The_Sleeping_Pillar_잠든_기둥.html) (잠든 기둥) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-IVδ-967 [WS]` | [Pandora's Jar](../entity/SE-N-IVδ-967_The_Vanished_Relic_사라진_유물.html) (사라진 유물) | Weight | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-Iα-025 [VS]` | [The Silent Child](../entity/SE-N-Iα-025_The_Silent_Child_조용한_아이.html) (조용한 아이) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-Iα-316 [D]` | [The Soaking Rope](../entity/SE-N-Iα-316_The_Soaking_Rope_솟구친_밧줄.html) (솟구친 밧줄) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-Iα-459 [VP]` | [The Sleeping Wall](../entity/SE-N-Iα-459_The_Sleeping_Wall_잠든_벽.html) (잠든 벽) | Void | A wall built from the exhaustion of wanting connection and lacking the strength to ask. Effect: proximity induces fatigue of unexpressed loneliness. |
| `N-Iα-518 [D]` | [The Soaking Window](../entity/SE-N-Iα-518_The_Soaking_Window_솟구친_창.html) (솟구친 창) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-Iα-519 [VP]` | [The Spreading Seed](../entity/SE-N-Iα-519_The_Spreading_Seed_스며든_씨앗.html) (스며든 씨앗) | Void | A seed of pure absence, spreading. Effect: proximity induces the vertigo of mourning what never existed. |
| `N-Iα-686 [N]` | [The Torn Window](../entity/SE-N-Iα-686_The_Torn_Window_찢어진_창.html) (찢어진 창) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `N-Iα-785 [O]` | [The Collapsed Tear](../entity/SE-N-Iα-785_The_Collapsed_Tear_무너진_눈물.html) (무너진 눈물) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIβ-120 [GS]` | [The Wrath Flame](../entity/SE-O-IIIβ-120_The_Wrath_Flame_분노의_불꽃.html) (분노의 불꽃) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-233 [LS]` | [The Forgotten Soul](../entity/SE-O-IIIγ-233_The_Forgotten_Soul_잊혀진_영혼.html) (잊혀진 영혼) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-369 [LO]` | [The Broken Whisper](../entity/SE-O-IIIγ-369_The_Broken_Whisper_부서진_속삭임.html) (부서진 속삭임) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-371 [VS]` | [The Vanished Silence](../entity/SE-O-IIIγ-371_The_Vanished_Silence_사라진_침묵.html) (사라진 침묵) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-374 [N]` | [The Sleeping Tree](../entity/SE-O-IIIγ-374_The_Sleeping_Tree_잠든_나무.html) (잠든 나무) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-476 [WO]` | [The Sunken Tear](../entity/SE-O-IIIγ-476_The_Sunken_Tear_가라앉은_눈물.html) (가라앉은 눈물) | Weight | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-559 [LS]` | [The Broken Ruin](../entity/SE-O-IIIγ-559_The_Broken_Ruin_부서진_잔해.html) (부서진 잔해) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-617 [O]` | [The Soaking Wall](../entity/SE-O-IIIγ-617_The_Soaking_Wall_솟구친_벽.html) (솟구친 벽) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-651 [VP]` | [The Sleeping Relic](../entity/SE-O-IIIγ-651_The_Sleeping_Relic_잠든_유물.html) (잠든 유물) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-914 [N]` | [Driftglass](../entity/SE-O-IIIγ-914_The_Wandering_Soul_떠도는_영혼.html) (떠도는 영혼) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-915 [VS]` | [Corrosion Dream](../entity/SE-O-IIIγ-915_The_Rusted_Bridge_녹슨_다리.html) (녹슨 다리) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIγ-959 [D]` | [Graveweed](../entity/SE-O-IIIγ-959_The_Rising_Root_솟아오른_뿌리.html) (솟아오른 뿌리) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIIδ-011 [GS]` | [The Scar Walker](../entity/SE-O-IIIδ-011_The_Scar_Walker_흉터의_행자.html) (흉터의 행자) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-119 [VP]` | [The Wandering Shadow](../entity/SE-O-IIβ-119_The_Wandering_Shadow_떠도는_그림자.html) (떠도는 그림자) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-235 [GS]` | [The Torn Soul](../entity/SE-O-IIβ-235_The_Torn_Soul_찢어진_영혼.html) (찢어진 영혼) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-301 [LS]` | [The Melting Flame](../entity/SE-O-IIβ-301_The_Melting_Flame_녹아내린_불꽃.html) (녹아내린 불꽃) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-378 [LS]` | [The Drowned Echo](../entity/SE-O-IIβ-378_The_Drowned_Echo_침몰한_메아리.html) (침몰한 메아리) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-467 [LS]` | [The Soaking Chain](../entity/SE-O-IIβ-467_The_Soaking_Chain_솟구친_사슬.html) (솟구친 사슬) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-677 [GP]` | [The Vanished Tower](../entity/SE-O-IIβ-677_The_Vanished_Tower_사라진_탑.html) (사라진 탑) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-757 [GP]` | [The Broken Door](../entity/SE-O-IIβ-757_The_Broken_Door_부서진_문.html) (부서진 문) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-796 [LS]` | [The Soaking Tower](../entity/SE-O-IIβ-796_The_Soaking_Tower_솟구친_탑.html) (솟구친 탑) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-833 [LS]` | [The Rusted Soul](../entity/SE-O-IIβ-833_The_Rusted_Soul_녹슨_영혼.html) (녹슨 영혼) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIβ-922 [O]` | [Door to Nowhere](../entity/SE-O-IIβ-922_The_Rising_Door_솟아오른_문.html) (솟아오른 문) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IIγ-007 [VP]` | [The Drift Fog](../entity/SE-O-IIγ-007_The_Drift_Fog_drifting_안개.html) (drifting 안개) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-115 [WO]` | [The Broken Fragment](../entity/SE-O-IVδ-115_The_Broken_Fragment_부서진_파편.html) (부서진 파편) | Weight | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-151 [GP]` | [The Spreading Tree](../entity/SE-O-IVδ-151_The_Spreading_Tree_스며든_나무.html) (스며든 나무) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-168 [O]` | [The Collapsed Trace](../entity/SE-O-IVδ-168_The_Collapsed_Trace_무너진_흔적.html) (무너진 흔적) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-190 [GS]` | [The Ember Phoenix](../entity/SE-O-IVδ-190_The_Ember_Phoenix_불사조.html) (불사조) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-693 [WS]` | [The Spreading Root](../entity/SE-O-IVδ-693_The_Spreading_Root_스며든_뿌리.html) (스며든 뿌리) | Weight | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-762 [O]` | [The Burning Bridge](../entity/SE-O-IVδ-762_The_Burning_Bridge_타오르는_다리.html) (타오르는 다리) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-792 [O]` | [The Flowing Relic](../entity/SE-O-IVδ-792_The_Flowing_Relic_흐르는_유물.html) (흐르는 유물) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-844 [N]` | [The Sleeping Ruin](../entity/SE-O-IVδ-844_The_Sleeping_Ruin_잠든_잔해.html) (잠든 잔해) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-851 [LO]` | [The Broken Shard](../entity/SE-O-IVδ-851_The_Broken_Shard_부서진_조각.html) (부서진 조각) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-895 [VS]` | [The Wandering Sigh](../entity/SE-O-IVδ-895_The_Wandering_Sigh_떠도는_한숨.html) (떠도는 한숨) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-897 [GS]` | [The Broken Wall](../entity/SE-O-IVδ-897_The_Broken_Wall_부서진_벽.html) (부서진 벽) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-IVδ-909 [GP]` | [Reverberant](../entity/SE-O-IVδ-909_The_Spreading_Echo_스며든_메아리.html) (스며든 메아리) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-108 [GS]` | [The Wandering Trace](../entity/SE-O-Iα-108_The_Wandering_Trace_떠도는_흔적.html) (떠도는 흔적) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-126 [VS]` | [The Melting Shard](../entity/SE-O-Iα-126_The_Melting_Shard_녹아내린_조각.html) (녹아내린 조각) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-169 [WP]` | [The Rusted Pillar](../entity/SE-O-Iα-169_The_Rusted_Pillar_녹슨_기둥.html) (녹슨 기둥) | Weight | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-189 [LS]` | [The Fading Ruin](../entity/SE-O-Iα-189_The_Fading_Ruin_번져가는_잔해.html) (번져가는 잔해) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-340 [VP]` | [The Frozen Relic](../entity/SE-O-Iα-340_The_Frozen_Relic_얼어붙은_유물.html) (얼어붙은 유물) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-453 [LS]` | [The Floating Fragment](../entity/SE-O-Iα-453_The_Floating_Fragment_떠다니는_파편.html) (떠다니는 파편) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-554 [LO]` | [The Rusted Seed](../entity/SE-O-Iα-554_The_Rusted_Seed_녹슨_씨앗.html) (녹슨 씨앗) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-631 [WS]` | [The Vanished Root](../entity/SE-O-Iα-631_The_Vanished_Root_사라진_뿌리.html) (사라진 뿌리) | Weight | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-643 [GO]` | [The Frozen Mirror](../entity/SE-O-Iα-643_The_Frozen_Mirror_얼어붙은_거울.html) (얼어붙은 거울) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-709 [GO]` | [The Forgotten Tear](../entity/SE-O-Iα-709_The_Forgotten_Tear_잊혀진_눈물.html) (잊혀진 눈물) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-720 [GS]` | [The Melting Whisper](../entity/SE-O-Iα-720_The_Melting_Whisper_녹아내린_속삭임.html) (녹아내린 속삭임) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-754 [GS]` | [The Wandering Chain](../entity/SE-O-Iα-754_The_Wandering_Chain_떠도는_사슬.html) (떠도는 사슬) | Grudge | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-794 [LO]` | [The Collapsed Door](../entity/SE-O-Iα-794_The_Collapsed_Door_무너진_문.html) (무너진 문) | Lament | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Iα-973 [VS]` | [Yggdrasil Wound](../entity/SE-O-Iα-973_The_Torn_Tree_찢어진_나무.html) (찢어진 나무) | Void | Per entity classification. See SECC Classification table and Combat Record for threat details. |
| `O-Vγ-003 [WP]` | [The Wilderness Tide](../entity/SE-O-Vγ-003_The_Wilderness_Tide_야생의_조수.html) (야생의 조수) | Weight | Not a creature but a moving wall of raw, unstructured wilderness Han — a tidal surge of black Han-pressure that rises from beyond the Desolate and crashes against Zone E. It has no body to strike; only the wave, the pressure, a... |

### Hope Transformations (14)

| Designation | Entity | Element | Description |
|---|---|---|---|
| `` | [The Burning Hope](../entity/HT-009_The_Burning_Hope_타오르는_희망.html) (타오르는 희망) |  | A small golden-orange flame with a white center that produces real heat and can burn through obstacles, circling the bearer's weapon arm or resting above the shoulder like a torch in an invisible hand. Warm and fierce, it bends... |
| `` | [The Defiant Ember](../entity/HT-005_The_Defiant_Ember_저항의_불씨.html) (저항의 불씨) |  | A small orange-gold coal floating just behind the bearer's sternum or resting between their fingers — never fully extinguished, its surface traced with tiny black veins like the remains of a burned contract. Warm and stubborn,... |
| `` | [The Eternal Warmth](../entity/HT-006_The_Eternal_Warmth_영원한_온기.html) (영원한 온기) |  | A small golden radiance with no fixed body — sometimes forming the outline of two hands around a cup, a shoulder, or a sleeping person. Its light is amber and soft, never harsh; warm and quiet, it preserves the feeling of being... |
| `` | [The Gentle Flame](../entity/HT-003_The_Gentle_Flame_온화한_불꽃.html) (온화한 불꽃) |  | A small golden flame that floats above an open palm — no smoke, no ordinary heat, amber at the edge and white at the center, a faint blue ring when it tends sorrow-wounds. Warm and gentle, it shifts shape to suit whoever it hel... |
| `` | [The Guiding Light](../entity/HT-001_The_Guiding_Light_인도의_빛.html) (인도의 빛) |  | A small golden orb the size of a human heart — neither glass nor crystal but like a drop of dawn suspended in air, thin lines of light moving through it like roads on a living map. Warm and faintly radiant, it floats near its b... |
| `` | [The Hand of Hope](../entity/HT-V-HH-001_The_Hand_of_Hope_희망의_손.html) (희망의 손) |  | A vast luminous hand formed of gold, amber, white, silver, and orange Hope-crystal — appearing as a single hand above a district, a pair of hands around the Weeping, or a humanoid whose arms extend into networks of light. Warm... |
| `` | [The Healing Touch](../entity/HT-008_The_Healing_Touch_치유의_손길.html) (치유의 손길) |  | A small golden hand of soft Hope-crystal, not attached to any body — floating beside its bearer, following their gestures, sometimes laying a translucent hand over theirs. Warm and precise, its five fingers divide into fine thr... |
| `` | [The Living Memory](../entity/HT-010_The_Living_Memory_살아_있는_기억.html) (살아 있는 기억) |  | A small golden figure with a porcelain-like body and a face that never settles into one identity, wearing a miniature craftsman's apron and carrying a thread of light between its hands. Warm and gentle, it borrows one harmless... |
| `` | [The Reuniting Spark](../entity/HT-004_The_Reuniting_Spark_재회의_불꽃.html) (재회의 불꽃) |  | A bright golden spark moving in short eager arcs, like a firefly made from a fragment of a broken star, trailing light that bends toward the strongest surviving connection. Warm and restless, it glows amber for people, white-go... |
| `` | [The Shared Glass](../entity/HT-011_The_Shared_Glass_나눔의_잔.html) (나눔의 잔) |  | A small golden drinking glass with a silver rim, always clean even when filled with liquid Han — unbreakable by ordinary force, though it clouds whenever someone speaks without honesty. Warm and clear; in a group it summons tra... |
| `` | [The Shield of Dawn](../entity/HT-002_The_Shield_of_Dawn_새벽의_방패.html) (새벽의 방패) |  | A compact golden shield that rests as a warm luminous mark on the bearer's forearm, unfolding into a broad round shield of layered gold, silver, and translucent Hope-crystal. Its surface bears shifting impressions of hands reac... |
| `` | [The Silent Vigil](../entity/HT-007_The_Silent_Vigil_침묵의_경계.html) (침묵의 경계) |  | A small golden light floating above the bearer's shoulder, like a covered lantern with no visible flame — its light falling outward but never into the protected one's eyes. Warm and soundless, it divides into dim lights that st... |
| `` | [The Standing Witness](../entity/HT-012_The_Standing_Witness_서_있는_증인.html) (서 있는 증인) |  | A small golden figure about the height of a hand, with no visible mouth, carrying a thin silver tablet against its chest — standing wherever its bearer stands, never sitting. Warm and watchful, its featureless face grows a pair... |
| `` | [The Trinity of Dawn](../entity/HT-V-HC-001_The_Trinity_of_Dawn_새벽의_삼위일체.html) (새벽의 삼위일체) |  | A single birdlike body larger than an eagle, with three overlapping necks joining at the chest — one head bearing many eyes, one a luminous balance-mark, one broad protective wings. Its feathers are pale gold and white Hope-cry... |

### Unknown Sorrow Entities (8)

| Designation | Entity | Element | Description |
|---|---|---|---|
| `C-IIIγ-248 [LS]` | [The Unconsoled](../entity/SE-C-IIIγ-248_The_Unconsoled_위로받지_못한_자.html) (위로받지 못한 자) | Lament | Major passive threat via Composure drain; no direct violence. The grief is load-bearing — dispersal is forbidden. |
| `C-IVδ-251 [VP]` | [The Unspoken Line](../entity/SE-C-IVδ-251_The_Unspoken_Line_그어진_선.html) (그어진 선) | Void | Critical passive hazard via Void-erosion of social memory and clarity. No direct violence. |
| `N-IIIβ-247 [WS]` | [The Undelivered Thanks](../entity/SE-N-IIIβ-247_The_Undelivered_Thanks_전하지_못한_감사.html) (전하지 못한 감사) | Weight | No direct violence; no Fracture risk recorded. Passive ambient weight that surfaces each viewer's own undelivered gratitude. |
| `N-IIγ-903 [VO]` | [The Music Box of Agony](../entity/SE-N-IIγ-903_The_Music_Box_of_Agony_고통의_오르골.html) (고통의 오르골) | Void | Major passive hazard via the lullaby. No direct violence. |
| `N-IVγ-250 [GS]` | [The Extinguished](../entity/SE-N-IVγ-250_The_Extinguished_꺼진_자.html) (꺼진 자) | Grudge | Major active threat to Hope Bearers and Hope-signatures; ignores the hopeless. Escalates against Bearers who fear burnout; withdraws from honest, steady presence. |
| `N-IVδ-901 [MH]` | [The Mewgical Girl](../entity/SE-N-IVδ-901_The_Mewgical_Girl_야옹_마법소녀.html) (야옹 마법소녀) | Mixed | Two coherent identities share one Subject-Body vessel; high-output combat and support abilities. No Fracture risk to civilians, but severe instability on persona conflict — misfired bombs, uncontrolled beams, self-hit Cartoon S... |
| `N-IVδ-902 [VS]` | [The Repeated Survivor](../entity/SE-N-IVδ-902_The_Repeated_Survivor_되풀이의_생존자.html) (되풀이의 생존자) | Void | A loop-aware agent who retains across iterations and stages reality as theatre. Lethal ("Bite Down," "Twist the Plot" restages past deaths), Clarity-destroying, and impossible to permanently suppress — it returns each loop. |
| `` | [The Book of Regressor](../entity/Book_of_Regressor_Log_Dramaturgy.html) (A Log of the Loops) |  | — |


*The Codex is the frame; each entity file is the picture. Open any entry and the structure above is what you will find.*
