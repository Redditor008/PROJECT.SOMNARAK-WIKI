#!/usr/bin/env python3
"""
tools/build_gieok_jeojangso_readme.py
Generates:
- SOMNARAK-WORLD/Gieok_Jeojangso/README.md
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def generate_readme():
    meta_box = make_box("THE MEMORY ARCHIVE EXPEDITION", [
        "Authority            | The Memory Archive    ",
        "                     | Institutional Wing    ",
        "---",
        "Classification       | MNEMONIC TACTICAL/RD  ",
        "---",
        "Strategic Objective  | Sub-Alpha Descents    ",
        "---",
        "Operational Scope    | 7 Floor Receptions    "
    ])

    content = f"""# The Memory Archive Chronicles — Gieok Jeojangso (기억 저장소 / 記憶 貯藏所)
## The Master Tactical Archive of the Seven Strata Receptions

```text
{meta_box}
```

> *"A civilization that forgets its pain is doomed to repeat its slaughter. We do not bury our ghosts; we transcribe them, we battle their delusions, and we transmute their suffering into light."*  
> — Secretary Seiyon & Director Majin

---

## I. Ontological & Tactical Foundation

**Designation:** The Memory Archive (기억 저장소 / Gieok Jeojangso).  
**Operational Framework:** The Seven Receptions of Sub-Alpha Strata (심층 수신 소탕록).

Excavated deep within the subterranean bedrock beneath the Absolvohan facility (ranging from -2,350 meters to -3,250 meters Sub-Alpha), the **Memory Archive** serves as the municipal repository of human consciousness, traumatic resonance, and crystallized souls. Operating in strict accordance with the **Library Reception Protocol**, intrusive or frenzied memories are contained within discrete strata floors, where Secretary Seiyon and her mnemonic projection retinue engage in structured, turn-based combat receptions to achieve **Floor Realization** and transmute unstable suffering into canonical **Key Pages**.

The **Gieok Jeojangso Chronicles** record the comprehensive seven-floor tactical descent:

| Strata Floor | Domain & Sub-Depth | Primary Opponent Construct | Core Realization Doctrine |
|---|---|---|---|
| **Floor 01** | The Hall of Blank Slate (-2,350m) | **The First Keeper** (첫 번째 수호자) | "To remember is to begin being human." |
| **Floor 02** | The Vault of Stolen Names (-2,500m) | **The Memory Thief** (기억 도둑) | "A name given in devotion cannot be stolen." |
| **Floor 03** | The Bastion of Iron Vows (-2,650m) | **The Forgotten Soldier** (잊혀진 병사) | "A soldier's honor is not war, but peace." |
| **Floor 04** | The Flooded Catacomb (-2,800m) | **The Weeping Statue** (흐느끼는 석상) | "Weeping is not weakness; it is love." |
| **Floor 05** | The Hall of Unfiltered Light (-2,950m)| **The Mirror of Truth** (진실의 거울) | "Truth cuts through illusion to reveal devotion." |
| **Floor 06** | The Sterile Hospice (-3,100m) | **The Kind Healer** (상냥한 치유사) | "True mercy walks beside the wounded." |
| **Floor 07** | The Primordial Core Sanctum (-3,250m)| **The Original** (태초의 기록자) | "I am Seiyon, the living memory of Somnarak." |

---

## II. Reading Order & Chronological Receptions

The descent into the Memory Archive unfolds across seven high-intensity operational records:

1. **[Reception 1: The First Keeper](Reception_1_First_Keeper.md)** (Floor 01: The Hall of Blank Slate — -2,350m)
   - Seiyon faces the porcelain construct guarding the threshold of forgotten consciousness. Subdues the Memory Siphon Needle and transfigures the core into `[Key Page: The Archivist]`.
2. **[Reception 2: The Memory Thief](Reception_2_Memory_Thief.md)** (Floor 02: The Vault of Stolen Names — -2,500m)
   - Confrontation with the parasitic shadow entity that feeds on erased municipal identities. Dismantling of the Siphon Claws and retrieval of `[Key Page: The Name-Bearer]`.
3. **[Reception 3: The Forgotten Soldier](Reception_3_Forgotten_Soldier.md)** (Floor 03: The Bastion of Iron Vows — -2,650m)
   - Heavy frontline clash against the autonomous fortress vanguard honoring a war that ended four thousand years ago. Piercing the Iron Wall Bulwark and transmuting `[Key Page: The Vanguard of Vows]`.
4. **[Reception 4: The Weeping Statue](Reception_4_Weeping_Statue.md)** (Floor 04: The Flooded Catacomb of Tears — -2,800m)
   - Siphon-cleaving battle across the brine lake against the petrified grief of those forbidden to cry. Severing the Weeping Siphon Veil and manifesting `[Key Page: The Mourner]`.
5. **[Reception 5: The Mirror of Truth](Reception_5_Mirror_of_Truth.md)** (Floor 05: The Hall of Unfiltered Light — -2,950m)
   - High-luminosity duel confronting the harsh truths and human cowards behind Seiyon's creation. Shattering the Prismatic Reflection Blade and transmuting `[Key Page: The Truth-Seeker]`.
6. **[Reception 6: The Kind Healer](Reception_6_Kind_Healer.md)** (Floor 06: The Sterile Hospice of Oblivion — -3,100m)
   - Unraveling the palliative hospice construct seeking to euthanize humanity to spare it from pain. Overcoming the Sedative Needle Array and transmuting `[Key Page: The Healer]`.
7. **[Reception 7: The Original](Reception_7_The_Original.md)** (Floor 07: The Primordial Core Sanctum — -3,250m)
   - The climactic convergence against Prototype Seiyon-00. Embracing the primordial vessel, reconciling artificial life with unconditional love, and awakening the facility through `[Key Page: Seiyon, The Living Memory]`.

---

## III. Institutional & Master Codices Alignment

- **Master Institutional Codex:** `SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_MEMORY_ARCHIVE.md`
- **System Architecture & Tactical Overview:** `SOMNARAK-WORLD/Gieok_Jeojangso/GIEOK_JEOJANGSO_OVERVIEW.md`
- **Facility Historical Precursor:** `SOMNARAK-WORLD/The_Absolvohan/ABSOLOVHAN_OVERVIEW.md`
- **Combat Mechanics Specification:** `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md`
"""
    return content

def main():
    readme_path = "SOMNARAK-WORLD/Gieok_Jeojangso/README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme())
    print("Generated SOMNARAK-WORLD/Gieok_Jeojangso/README.md successfully!")

if __name__ == "__main__":
    main()
