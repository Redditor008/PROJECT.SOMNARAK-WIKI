#!/usr/bin/env python3
"""
tools/generate_l_corp_transport_guide.py
Generates the definitive guide:
PS_SORROW_ENTITY_IN_L_CORP_CONTAINMENT_GUIDE.md
Covers the transportation of Project Somnarak Sorrow Entities into Lobotomy Corporation via The Well.
"""

import sys
sys.path.insert(0, ".")
from tools.box_formatter import make_box

def add_box(title, rows, width=74):
    box = make_box(title, rows, width=width)
    return f"```text\n{box}\n```\n"

header_box = add_box("LOBOTOMY CORP EXTRACTION DOSSIER // THE WELL ANOMALIES", [
    "DOCUMENT: PS SORROW ENTITY IN L CORP CONTAINMENT MANUAL",
    "CLASSIFICATION: SPECIAL EXTRA-DIMENSIONAL COGITO INTRUSION",
    "ISSUING BODY: EXTRACTION & DISCIPLINARY TEAMS // ANGELA DIRECTIVE",
    "---",
    "PHENOMENON: TRANS-WELL DREDGING OF PLANETARY HAN MATRICES",
    "CONTAINMENT LAWS: WORK TYPE RESTRICTIONS & PLACE-BREACH PROTOCOLS"
])

hud_matrix = add_box("FACILITY WORK PROTOCOLS // COGITO VS HAN CONVERSION", [
    "L CORP WORK TYPE     | PS ANALOG      | SUBJECT SE   | INANIMATE SE [O/P/T]",
    "---------------------+----------------+--------------+---------------------",
    "Instinct Work        | Viderehan (Obs)| Common (PE)  | Safe Extraction",
    "Insight Work         | Ferrehan (End) | High (PE)    | High PE Yield",
    "Attachment Work      | Flerehan (Cath)| Variable PE  | LETHAL BACKFIRE (0 PE)",
    "Repression Work      | Pugnahan (Clsh)| Counter Drop | KINETIC BREACH (0 PE)"
])

breach_box = add_box("PLACE-SE BREACH PHENOMENON // L CORP DEPARTMENT CORRUPTION", [
    "SUBJECT: SE-C-IVw-001 The Maw Transferred to Extraction Department",
    "Normal State: Contained Room | Instinct/Insight ONLY | Qliphoth: 3",
    "Breach Trigger: Counter reaches 0 or Repression Work performed",
    "---",
    "METAMORPHOSIS EVENT: Place-to-Subject Corridor Transformation",
    "1. Containment unit walls liquify into dark whispering asphalt",
    "2. Adjacent department hallways curve inward; elevators disabled",
    "3. Unit coalesces into ALEPH Colossus moving toward Central Command",
    "4. Disciplinary Team (Gebura) mobilization required immediately"
])

checklist_box = add_box("SEPHIRAH CONTAINMENT & EXTRACTION DIRECTIVE CHECKLIST", [
    "01. RISK TIERING    : Map Ranks I-V to ZAYIN, TETH, HE, WAW, ALEPH",
    "02. PE-BOX FORMULA  : Extract Enkephalin while filtering toxic Han brine",
    "03. TWO-WORK RULE   : Strictly block Attachment & Repression on O/P/T",
    "04. SANITY BUFFER   : Assign SP recovery kits for Lament/Weight exposure",
    "05. E.G.O EXTRACTION: Extract Weapon, Suit, Gift with Composure Load",
    "06. CORROSION WATCH : Monitor employees for Acoustic Meltdown symptoms",
    "07. DISCIPLINARY    : Prepare Rabbit Protocol for Place-Metamorphosis"
])

content = f"""# PS SORROW ENTITY IN L CORP CONTAINMENT GUIDE
## Comprehensive Extraction, Containment & Suppression Manual for Anomalies Transported via The Well
### Central Command & Extraction Department Technical Operations Codex

{header_box}

> *"Manager, we have encountered an unprecedented phenomenological distortion. When the bucket descended into the lowest strata of The Well beneath District 12, it did not draw from the collective unconscious of human minds. It snagged upon an alien fault line—a trans-dimensional siphon dragging liquid sorrow from a world that has wept for six thousand years. These entities do not conform to our standard behavioral matrices. They do not feed on human guilt; they are physical, acoustic condensations of planetary grief. Read this manual carefully before assigning your agents. An error in work selection will not merely cause panic—it will turn your facility floor into living concrete."*  
> — Angela, Briefing to the Manager

---

## Section I: The Well Dredging & Trans-Dimensional Collision

### 1. The Trans-Dimensional Siphon
In standard Lobotomy Corporation operations, Cogito is injected into human test subjects or drawn from The Well to manifest conceptual archetypes from humanity's collective psyche. 

However, when subterranean extraction drills breach below critical operational depths, The Well's resonance can intersect with the subterranean **Weeping** (  비탄   / *Bitan*, located at -2,000 meters beneath planet Mugenhan). Through this siphon, raw **Han** (  한   / *Fluid and Acoustic Grief*) floods into the extraction pumps, materializing Project Somnarak Sorrow Entities directly into L Corp containment units.

### 2. Physical & Environmental Characteristics in Containment
When a Sorrow Entity is manifested inside a containment unit:
- **Chamber Environment:** The sterile white lighting of the unit dims into an indigo-and-crimson twilight. Acoustic monitoring channels pick up a constant 528 Hz or 432 Hz subsonic hum.
- **Han Brine Contamination:** Instead of clean Enkephalin vapors, the chamber floor accumulates a dark, salt-encrusted brine. The Sanitation Department must cycle thermal incinerators after every work turn to prevent structural corrosion.
- **Enkephalin Transmutation:** Energy extracted from a Sorrow Entity produces standard PE-Boxes (Positive Enkephalin), but carries a 15% to 25% "Heavy Han Density". This dense energy yields higher power output per box but increases the global Qliphoth Meltdown rate across the facility.

---

## Section II: Risk Classification Mapping (SECC to Lobotomy Corp Tiers)

The Sephirah Council classifies incoming Sorrow Entities into Lobotomy Corporation's standard five-tier Hebrew risk hierarchy based on their SECC Coherence Rank and Potency Grade:

| Lobotomy Corp Risk Level | Somnarak Coherence & Potency | Standard HP Bar | Attack Value | Max PE-Boxes | Qliphoth Counter | Primary Damage Type |
|---|---|---|---|---|---|---|
| **ZAYIN** | **Rank I (Residue) / Grade α** | 150 – 300 HP | 06 – 14 DMG | 10 – 14 PE | 2 – 3 | RED (Grudge) or WHITE (Lament) |
| **TETH** | **Rank II (Echo) / Grade β** | 300 – 500 HP | 12 – 22 DMG | 14 – 18 PE | 2 – 4 | RED, WHITE, or BLACK (Weight) |
| **HE** | **Rank III (Fragment) / Grade γ** | 500 – 750 HP | 18 – 35 DMG | 18 – 24 PE | 1 – 3 | BLACK (Weight) or PALE (Void) |
| **WAW** | **Rank IV (Entity) / Grade δ** | 750 – 1,000 HP | 30 – 55 DMG | 24 – 32 PE | 1 – 2 | Dual-Element / Multi-Hit |
| **ALEPH** | **Rank V (Sovereign) / Grade ω** | 1,000 – 12,000 HP | 50 – 80+ DMG | 32 – 40 PE | 1 – 3 | All Four Elements Cycled |

---

## Section III: Work Type Mechanics & The Inviolable Two-Work-Type Law

{hud_matrix}

In Lobotomy Corporation, agents are accustomed to performing Instinct, Insight, Attachment, and Repression on almost every Abnormality. **With Sorrow Entities, this standard operating procedure will cause immediate fatalities if applied blindly.**

### 1. Subject Entities (`[S]` — Mobile, Conscious Forms)
For entities classified with a Subject manifestation (e.g., *The Whispering Confessional* `SE-C-Iα-033 [LS]`, *Marksman of the Seventh Watch* `SE-C-IVδ-069 [GS]`):
- **Instinct Work (Viderehan Analog):** Agent monitors the entity's acoustic breathing and posture from within the chamber. Yields common/good results; stabilizes low-potency entities.
- **Insight Work (Ferrehan Analog):** Agent endures the chamber's heavy atmospheric pressure and cold. Yields high PE-Boxes; recommended for high-Resilience agents.
- **Attachment Work (Flerehan Analog):** Agent communicates empathetically, weeping with the entity. Highly polarized: if the agent possesses Level V Prudence and high Composure, it yields massive PE-Boxes; if the agent fails, their SP collapses into immediate suicidal panic.
- **Repression Work (Pugnahan Analog):** Agent deploys suppression batons to strike the entity. High physical risk: temporarily lowers breach agitation, but rapidly degrades the Qliphoth Counter if performed repeatedly.

### 2. Inanimate Entities (`[O]`, `[P]`, `[T]`, `[H]` — Relics, Places, Times, Hazards)
**THE MANAGER MUST ENFORCE THE TWO-WORK-TYPE RULE WITHOUT EXCEPTION:**
- **Instinct & Insight Work:** The ONLY permitted actions. The agent observes energy oscillations (Instinct) or reinforces physical isolation seals (Insight).
- **Attachment Work — LETHAL PSYCHIC COLLAPSE:**  
  * *Reason:* An inanimate relic, an empty flooded district, or a temporal rift possesses no personal psyche to comfort.
  * *Consequence:* The agent attempts to project human empathy into a lifeless void. The void reflects nothing back, instantly draining 100% of the agent's SP. The agent panics immediately, screams in an unknown tongue, and dies of cerebral hemorrhage. Zero PE-Boxes produced.
- **Repression Work — KINETIC CONTAINMENT RUPTURE:**  
  * *Reason:* An inanimate monument or geographic district has no biological anatomy to strike.
  * *Consequence:* The kinetic energy of the agent's weapon deflects off the entity's indestructible bedrock. The reflected shockwave shatters the chamber's containment glass, instantly reducing the Qliphoth Counter to 0 and triggering a catastrophic breach.

---

## Section IV: Damage Type & Elemental Inter-Translation

When Sorrow Entities inflict damage on Lobotomy Corp employees, damage types translate across the elemental spectrum:

| Somnarak Han Element | Lobotomy Corp Damage Type | Target Attribute | Defense & Protection Rule |
|---|---|---|---|
| **Grudge (Crimson /   원한   )** | **RED Damage** | Physical Health (HP) | Protect with high Red-resistant E.G.O suits (e.g., *Red Eyes*, *Mimicry*). Inflicts Laceration bleed. |
| **Lament (Deep Blue /   탄식   )** | **WHITE Damage** | Sanity Points (SP) | Protect with high White-resistant E.G.O suits (e.g., *Smile*, *Sound of a Star*). Drains SP and freezes movement speed. |
| **Weight (Black /   무게   )** | **BLACK Damage** | Dual HP & SP Simultaneously | Protect with balanced hybrid suits (e.g., *Justitia*, *Black Swan*). Inflicts gravitational burden that increases work task duration. |
| **Void (Pale White /   공허   )** | **PALE Damage** | Percentage Max HP (Death Trauma) | Protect strictly with Pale-resistant gear (0.5 or lower, e.g., *Paradise Lost*). Bypasses physical armor. |

---

## Section V: Special Transform Breaches: Place-to-Subject Metamorphosis

{breach_box}

In standard L Corp operations, when an Abnormality breaches, its sprite exits the containment cell and roams the hallways.

When a **Place-Tale Sorrow Entity** breaches in Lobotomy Corporation (most notably *The Maw* `C-IVω-001 [GP]`), the facility faces a catastrophic structural crisis known as **Place-to-Subject Metamorphosis**:

### Phase 1: Departmental Assimilation
- The containment doors do not open; rather, the cell walls dissolve into liquid asphalt and whispering concrete.
- The infection spreads across the host department (e.g., Extraction or Central Command). Elevators lock down, lights extinguish, and the walls begin muttering centuries-old mining ledgers in Korean (  "천 명의 숨소리가 벽 속에 산다..."   / *"A thousand breaths dwell inside the walls..."*).
- Any employee standing on the affected floor suffers continuous 25 Black Damage per second.

### Phase 2: The Walking Maw Metamorphosis (`C-IVω-001-B [GS]`)
- The architecture detaches from the subterranean bedrock. The whispering masonry, pipes, and tar coalesce into an enormous, multi-legged stone colossus.
- Its SECC code shifts from `[GP]` (Place) to `[GS]` (Breaching Subject).
- It enters the main departmental corridors as an **ALEPH-class mobile sovereign**.

### Phase 3: Suppression Doctrine
- **Work Rule Shift:** While mobile, the entity can now be engaged with direct kinetic weaponry (Repression / Pugnahan) and empathetic counter-resonance (Attachment / Flerehan).
- **Suppression Protocol:** Gebura's Disciplinary Team must intercept the colossus before it reaches the Central Command core room. Use long-range PALE and WHITE weaponry to shatter its acoustic resonance before its footsteps crush the Sephirah containment pillars.

---

## Section VI: E.G.O Extraction via Extraction Department (Binah)

When an agent extracts equipment from a Sorrow Entity in the Extraction Department, Binah's machinery extracts unique armaments that synthesize Lobotomy Corporation E.G.O technology with Somnarak's **Materialized Agony Wear (M.A.W.)**:

### 1. Unique E.G.O Trait: Composure Load
Unlike standard E.G.O suits that only have static agent level requirements (e.g., Fortitude III, Prudence II), Sorrow E.G.O imposes **Active Composure Load**:
- While an agent is wearing a Sorrow E.G.O Suit or wielding a Sorrow Weapon, their maximum SP is reduced by a fixed amount (e.g., -15 SP for WAW, -30 SP for ALEPH).
- In exchange, the gear grants **Acoustic Shockwaves**: every 4th strike releases a 528 Hz pulse that staggers all hostiles in the corridor.

### 2. Acoustic Meltdown (Corrosion Dynamic)
If an agent's SP hits 0 while equipped with Sorrow E.G.O:
- They do not panic in standard fashion (running, screaming, or wandering).
- Their body crystallizes into blue-and-black Han salt. They transform into an **Acoustic Echo** of the original Sorrow Entity, attacking both employees and abnormalities with identical damage profiles until put down by suppression teams.

---

## Section VII: Departmental Assignment Roster (Facility Case Studies)

### 1. `SE-C-Iα-000` *The Kind Echo* (  친절한 메아리   / *Chinjeolhan Meari*)
- **Department:** Training Department (Hod)
- **Assigned Risk:** ZAYIN (Residue) · Max PE: 12 · Qliphoth Counter: None
- **Containment Note:** Generates continuous SP restoration aura for the entire Training main room. Highly recommended for onboarding fresh Level I employees.

### 2. `SE-C-IVδ-069` *Marksman of the Seventh Watch* (  칠경의 저격수   / *Chilgyeong-ui Jeogyeoksu*)
- **Department:** Central Command (Tiphereth)
- **Assigned Risk:** WAW (Entity) · Max PE: 28 · Qliphoth Counter: 2
- **Containment Note:** When Qliphoth Meltdown triggers, the entity fires the *Seventh Slate Needle* through three random facility departments, dealing 60 RED damage to every clerk and agent in its straight trajectory. Insight work performed by agents with Temperance V minimizes counter drops.

### 3. `SE-C-IVω-001` *The Maw* (  구라   / *Gura*)
- **Department:** Extraction Department (Binah) / Architecture
- **Assigned Risk:** ALEPH (Sovereign) · Max PE: 36 · Qliphoth Counter: 1
- **Containment Note:** Strictly lock to Instinct and Insight work. Any agent attempting Attachment or Repression work triggers immediate Place-to-Subject breach.

### 4. `SE-N-IIβ-319` *The Magistrate's Strike-Through* (  판관의 취소선   / *Pangwan-ui Chwisoseon*)
- **Department:** Safety Department (Netzach)
- **Assigned Risk:** TETH (O-Relic / Tool Abnormality)
- **Containment Note:** Agents can interact with the black chalk once per day. Grants 45 seconds of complete PALE damage immunity, but reduces the agent's maximum HP by -20% for the remainder of the working day.

---

## Section VIII: Facility Verification Checklist

{checklist_box}
"""

target_path = "SOMNARAK-WORLD/Master_Codices/06_Integrity_Audits_and_Comparative_Studies/PS_SORROW_ENTITY_IN_L_CORP_CONTAINMENT_GUIDE.md"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated: {target_path}")
