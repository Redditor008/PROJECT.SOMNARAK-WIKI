import re

# 1. Fix SE-C-Vγ-320_Sorrow_Storm_슬픔의_폭풍.md
storm_path = "SOMNARAK-WORLD/Sorrow_Entities/SE-C-Vγ-320_Sorrow_Storm_슬픔의_폭풍.md"
with open(storm_path, "r", encoding="utf-8") as f:
    storm_text = f.read()

two_work_storm = """## Behavior

> **Object/Place Work Rule:** Objects and Places cannot be emotionally engaged through Flerehan or confronted through Pugnahan. Only Viderehan (Observation) and Ferrehan (Endurance) are valid Work Types.

| Work Type | Response | Gauge Change |
|---|---|---|
| **Flerehan** (Tears) | N/A — Atmospheric storm phenomena cannot be emotionally engaged through Flerehan. | N/A |
| **Pugnahan** (Confrontation) | N/A — Macro-environmental storm forces cannot be physically confronted through Pugnahan. | N/A |
| **Viderehan** | Remote acoustic observation and barometric frequency monitoring from reinforced bunkers. | Stable |
| **Ferrehan** | Direct physical endurance inside the storm perimeter under heavy ballast anchors. | Decrease |

### Storm Environmental Progression

| Condition | Response | Gauge Change |
|---|---|---|
| **The Storm arrives** | Buildings crack and entities become agitated. | Increase |
| **The Storm passes** | Devastation remains but ambient sorrow decreases. | Decrease |
| **Caught in the Storm** | Personnel experience overwhelming grief and weight. | Severe |
"""

storm_text = re.sub(r"## Behavior.*?(?=### Operational Work Notes|\n## Activation Behavior)", two_work_storm + "\n", storm_text, flags=re.DOTALL)
with open(storm_path, "w", encoding="utf-8") as f:
    f.write(storm_text)
print("Updated SE-C-Vγ-320 successfully!")

# 2. Fix SE-O-Vγ-003_Wilderness_Tide_야생의_조수.md
tide_path = "SOMNARAK-WORLD/Sorrow_Entities/SE-O-Vγ-003_Wilderness_Tide_야생의_조수.md"
with open(tide_path, "r", encoding="utf-8") as f:
    tide_text = f.read()

# Update Core Stat Line with Speed and Resistances
old_stat_line = """### Core Stat Line

| Statistic | Value |
|---|---|
| **Risk tier** | Major |
| **Entity role** | Object/Place — border surge |
| **Primary pressure** | Resolve |
| **Activation threshold** | Wilderness Han surge detected at outer watchtowers |
| **Sorrow Gauge [HP]** | 900/900 out of 1000 |
| **Han Pressure [ATK]** | 25–60 per hit · Weight |
| **HP** | 900/900 out of 1000 |
| **Starting Sorrow Gauge** | 30–50% |"""

new_stat_line = """### Core Stat Line

| Statistic | Value |
|---|---|
| **Risk tier** | Major (Vγ) |
| **Entity role** | Object/Place — border surge |
| **Primary pressure** | Resolve |
| **Speed** | 1–3 (Ponderous environmental surge) |
| **Activation threshold** | Wilderness Han surge detected at outer watchtowers |
| **Sorrow Gauge [HP]** | 900/900 out of 1000 |
| **Han Pressure [ATK]** | 25–60 per hit · Weight (Black) |
| **Starting Sorrow Gauge** | 30–50% |
| **Han-Energy Yield** | 24–32 per successful containment cycle |

### Damage Resistances

| Damage Type | Multiplier | Tactical Note |
|---|---|---|
| **Crimson (Grudge)** | 1.0 (Normal) | Standard kinetic damage penetration. |
| **Deep Blue (Lament)** | 0.8 (Endured) | Resistant to acoustic weeping. |
| **Pale White (Void)** | 1.5 (Weak) | Vulnerable to conceptual void dissolution. |
| **Black (Weight)** | 0.5 (Immune / Endured) | Heavily resistant to gravitational shockwaves. |"""

tide_text = tide_text.replace(old_stat_line, new_stat_line)

# Update Behavior with Two-Work Rule
two_work_tide = """## Behavior

> **Object/Place Work Rule:** Objects and Places cannot be emotionally engaged through Flerehan or confronted through Pugnahan. Only Viderehan (Observation) and Ferrehan (Endurance) are valid Work Types.

| Work Type | Response | Gauge Change |
|---|---|---|
| **Flerehan** (Tears) | N/A — Macro-environmental wilderness surges do not respond to Flerehan. | N/A |
| **Pugnahan** (Confrontation) | N/A — The wilderness tide cannot be physically struck through Pugnahan. | N/A |
| **Viderehan** | Remote acoustic observation and seismic monitoring from the Outer Watchtowers. | Stable |
| **Ferrehan** | Direct physical endurance holding the outer perimeter wall under heavy ballast anchors. | Decrease |

### Tidal Surge Progression

| Phase | Action | Effect |
|---|---|---|
| **Build** | Wilderness Han accumulates beyond the Desolate. | Watchtowers detect rising pressure; Wardens deploy. |
| **Surge** | The Tide crashes against Zone E's outer wall. | Massive Weight pressure; structural stress; personnel fatigue. |
| **Recession** | The Tide recedes gradually. | Salt-residue left on the wall; Wardens assess damage and repair. |
| **Lull** | A period of calm before the next buildup. | Maintenance, recovery, and preparation. |
"""

tide_text = re.sub(r"## Behavior.*?(?=### Operational Work Notes|\n## Activation Behavior)", two_work_tide + "\n", tide_text, flags=re.DOTALL)
with open(tide_path, "w", encoding="utf-8") as f:
    f.write(tide_text)
print("Updated SE-O-Vγ-003 successfully!")
