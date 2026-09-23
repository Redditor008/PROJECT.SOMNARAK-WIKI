#!/usr/bin/env python3
"""
tools/build_jipyeongseondae_readme.py
Generates:
- SOMNARAK-WORLD/Jipyeongseondae/README.md
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def generate_readme():
    meta_box = make_box("THE HORIZON CARAVAN EXPEDITION", [
        "Authority            | The Horizon Caravan   ",
        "                     | Institutional Wing    ",
        "---",
        "Classification       | PLANETARY EXPEDITION  ",
        "---",
        "Strategic Objective  | Trans-Desolate Transit",
        "---",
        "Operational Scope    | 6 Overland Arcs       "
    ])

    content = f"""# The Horizon Caravan Chronicles — Jipyeongseondae (지평선대 / 地平線隊)
## The Master Tactical Archive of the Six Trans-Desolate Expeditions

```text
{meta_box}
```

> *"The city thinks it is the entire world. It builds walls of black iron and locks its gates against the dust. But the earth remembers paths between the stars, and someone must have the courage to cross the burning sand."*  
> — Kael, The Drift King, Year 4238

---

## I. Ontological & Tactical Foundation

**Designation:** The Horizon Caravan (지평선대 / Jipyeongseon Dae).  
**Operational Framework:** The Six Trans-Desolate Expeditions (대황야 횡단록 / 大荒野 橫斷錄).

For forty-two centuries following the great planetary fracture, humanity's remnants believed their home city was the solitary survivor of the apocalypse. Operating aboard the 140-meter mobile sand fortress **The Drift Throne (표류옥좌)**, former Warden Commander Kael and his nomadic coalition established the first trans-continental overland bridge across **The Desolate (황야)**, reconnecting the sister cities of Somnarak and Cheonbulok while charting the outer perimeter of Mugeukji.

The **Jipyeongseondae Chronicles** record the comprehensive six-arc planetary journey:

| Expedition Arc | Setting & Region | Primary Adversary Construct | Strategic Expedition Milestone |
|---|---|---|---|
| **Arc 1** | Somnarak Zone E: The Exile's Gate | **Warden Commander Vane** | Council charter ratified; Blast Gate V opened. |
| **Arc 2** | The Desolate: The Sea of Glass | **The Glass-Dune Colossus** | Category-5 storm traversed; Colossus pacified. |
| **Arc 3** | Cheonbulok: The Volcanic Caldera | **Slag Champion Barok** | Battle Pits trial won; furnace entrance granted. |
| **Arc 4** | Cheonbulok: Sacred Great Furnace | **The Blazing Heart of Sorrow** | Magma core cooled; 400 Ash refugees rescued. |
| **Arc 5** | The Desolate: Northern Corridor | **Sand-Corsair Warlord Garek** | Marauder ambush routed; trade route secured. |
| **Arc 6** | Mugeukji: Absolute Silence Border| **The Archon of the Void** | Sensory void charted; heroic retreat executed. |

---

## II. Reading Order & Chronological Arcs

The expedition of the Horizon Caravan unfolds across six high-intensity operational records:

1. **[Arc 1: Departure](Arc_1_Departure.md)** (Somnarak Zone E: The Exile's Gate — Year 4238, Month 1)
   - Kael brings the Drift Throne to Somnarak's gates. Clashes with the Warden Border Battery to force the Council of Sighs to ratify the Overland Expedition Charter.
2. **[Arc 2: The Desolate Crossing](Arc_2_The_Desolate_Crossing.md)** (The Desolate: The Sea of Glass — Year 4238, Months 2-3)
   - The Caravan braves the deep Sea of Glass, confronting a 200-meter Glass-Dune Colossus during a category-5 Han-storm, navigating by subterranean ley-frequencies.
3. **[Arc 3: Arrival at Cheonbulok](Arc_3_Arrival_at_Cheonbulok.md)** (Cheonbulok: The Volcanic Caldera — Year 4238, Month 4)
   - Entering the volcanic caldera of Cheonbulok, Kael fights in the gladiatorial Grand Battle Pit against Slag Champion Barok to win the respect of the city and its Furnace Keepers.
4. **[Arc 4: The Furnace's Secret](Arc_4_The_Furnaces_Secret.md)** (Cheonbulok: The Sacred Great Furnace Core — Year 4238, Month 5)
   - Entering the cracking core of the Great Furnace, Kael and Hwaran confront the agonizing grief of a dying city, stabilize the thermal core, and evacuate 400 Ash Walker refugees.
5. **[Arc 5: The Return](Arc_5_The_Return.md)** (The Desolate: Northern Sand Corridor — Year 4238, Months 6-7)
   - Escorting the massive refugee convoy back toward Somnarak, the Caravan repels a coordinated ambush by Warlord Garek's Sand-Corsairs, cementing the permanent trade highway.
6. **[Arc 6: The Mugeukji Attempt](Arc_6_The_Mugeukji_Attempt.md)** (Mugeukji: Perimeter of Absolute Silence — Year 4238, Month 8)
   - The Caravan ventures north to contact Mugeukji, confronting the horrifying sensory null field of the Archon of the Void before executing a strategic withdrawal to preserve the crew's sanity, leaving an acoustic beacon at the frontier.

---

## III. Institutional & Master Codices Alignment

- **Master Institutional Codex:** `SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_HORIZON_CARAVAN.md`
- **System Architecture & Tactical Overview:** `SOMNARAK-WORLD/Jipyeongseondae/JIPYEONGSEONDAE_OVERVIEW.md`
- **Geopolitical & Planetary Context:**
  * `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_THE_DESOLATE.md`
  * `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_UNKNOWN_CITIES.md`
- **Combat Mechanics Specification:** `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md`
"""
    return content

def main():
    readme_path = "SOMNARAK-WORLD/Jipyeongseondae/README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme())
    print("Generated SOMNARAK-WORLD/Jipyeongseondae/README.md successfully!")

if __name__ == "__main__":
    main()
