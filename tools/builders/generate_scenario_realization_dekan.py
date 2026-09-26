#!/usr/bin/env python3
"""
Generate GAME_BATTLE/SCENARIO_REALIZATION_FLOOR_02_DEKAN.md.
Strict Compliance:
- In Text Box: NO Korean Hangul/Hanja characters; ONLY the Korean Alphabet (Romanization/Romaja) and standard ASCII.
- Outside Text Box: Two-space buffer around all Korean characters: '  [korean]  ' paired with Alphabet Romanization and English translation.
- Zero P.M. vocabulary (No ZAYIN/TETH/HE/WAW/ALEPH, No E.G.O, No Abnormality, No Enkephalin, No Distortion).
- Native Somnarak terms: Han-Energy, Composure, Posture, Ranks I-V, Grades a-w, M.A.W. equipment, Echo-Cores.
- 71-col ASCII text boxes via tools.box_formatter, zero raw <br>, zero raw HTML, zero LaTeX math dollar signs.
- 10-node spatial engine combat resolution.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tools.box_formatter as bf

OUTPUT_PATH = "GAME_BATTLE/SCENARIO_REALIZATION_FLOOR_02_DEKAN.md"

def wrap_box(box_text):
    return "```text\n" + box_text + "\n```\n\n"

def build_scenario_dekan():
    lines = []
    
    # Master Header
    lines.append("# SCENARIO: FLOOR 02 RESONANT REALIZATION — DEKAN (  감금 책임자의 공명 각성전  / Gamgeum Chaegimja-ui Gongmyeong Gak-seongjeon [Floor 02 Containment Realization])")
    lines.append("## Canonical Boss Encounter: The Maw's Keep & Awakening of the Sovereign Warden")
    lines.append("### Tactical Realization Battle Specification — SOP-GB-REALIZATION-002\n")
    
    # Master HUD Box (Strictly English / Romanized Alphabet only - zero Hangul characters!)
    hud_rows = [
        "TACTICAL REALIZATION RECORD: REALIZATION-002-DEKAN",
        "SUPERVISING WING : Reverie Directorate Floor 01 Central Command",
        "OPERATIONAL AREA : Floor 02 — The Maw's Keep (Simyeon-ui Yosae)",
        "DEPTH COORDINATE : -1,200m Deep Containment Strata Nexus",
        "CHALLENGER UNIT  : Strike Team Alpha (The Iron Quad)",
        "SOVEREIGN BOSS   : Dekan (The Containment Lead / Echo-Core 3)",
        "CRISIS TRIGGER   : Sorrow Inversion Meltdown (Han-ui Yeokjeon)",
        "ENGAGEMENT MODE  : 4-Phase Resonant Realization War (Gongmyeong)",
        "PRIMARY GOAL     : Shatter Trauma Vessel / Resonant Awakening"
    ]
    lines.append(wrap_box(bf.make_box("REVERIE DIRECTORATE TACTICAL REALIZATION PROTOCOL", hud_rows, width=71)))
    
    # Section 1
    lines.append("## 1. Tactical Overview & Operational Parameters\n")
    sec1_text = """- **Topological Coordinate:** Subterranean Containment Amphitheater, Floor 02: The Maw's Keep (  심연의 요새  / Simyeon-ui Yosae [The Maw's Keep]), Facility 01 (-1,200m Sub-Basalt Strata).
- **Ambient Han Saturation:** 340 to 380 mMb (Pressurized Liquid Sorrow-Vapor at 14.8 Hz).
- **Environmental Hazard Modifiers:**
  * **Seismic Hydraulic Backpressure:** Floor 02 houses the primary containment hydraulic dampeners for the Raw. At Phase-End of each combat phase, all active combatants must spend 1 Movement AP to brace against subterranean shockwaves or suffer 15 Weight (  무게  / Muge [Weight]) damage.
  * **Acoustic Vault Echo:** Containment bulkheads amplify low-frequency groans. Units failing a clash suffer +10% Composure strain for two combat turns.
  * **Maw-Tether Restraint:** Hostile tendrils rising from Node `[N08]` through `[N10]` inflict *Maw Suture* (reduces movement range by 1 node per stack).
- **Mission Briefing:**
  For one thousand seven hundred and seventy-eight cycles, Echo-Core 3 Lead Dekan (  데칸  / Dekan [The Containment Lead]) has stood guard over the deepest containment vaults of Facility 01. He has evaluated thousands of entity disturbances that ordinary instruments could not classify, holding the line between municipal civilization and the yawning Maw (  심연의 입  / Simyeon-ui Ip [The Maw]). But the cumulative psychological weight of sealing comrades into quarantine cells has triggered a **Sorrow Inversion Meltdown** (  한의 역전 붕괴  / Han-ui Yeokjeon Bunggoe [Sorrow Inversion Meltdown]). Dekan's repressed terror—the belief that the fortress is not a shield, but an inescapable tomb—has detached Floor 02 from reality, initiating a **Resonant Realization War** (  공명 자각전  / Gongmyeong Jagakjeon [Resonant Realization War]). Strike Team Alpha must confront Dekan across four escalating psychological phases, break his trauma vessel with non-lethal precision, and awaken his true Sovereign Authority.
"""
    lines.append(sec1_text.strip() + "\n\n---\n")
    
    # Section 2
    lines.append("## 2. Combatant Rosters & Technical Profiles\n")
    lines.append("### 2.1 Allied Strike Team (The Iron Quad)\n\n")
    
    team_table = """| Operative Callsign | Tactical Role | Base Spd | Max HP | Composure | Posture | Equipped M.A.W. Set | Range Band |
|---|---|---|---|---|---|---|---|
| **Warden Min-Jae** | Citadel Bastion Anchor | 3 | 240 | 115 | 210 | Tectonic Bulwark (Grade δ) | Band 1 (Melee) |
| **Specialist Seol-A** | Siphon Flanker / Point | 6 | 170 | 120 | 160 | Silenced Requiem (Grade γ) | Band 2-3 (Mid) |
| **Vanguard Taeho** | Kinetic Sunder Striker | 4 | 200 | 110 | 195 | Ancestral Signet (Grade β) | Band 1-2 (Short) |
| **Tech Jinho** | Acoustic Sensor Anchor | 4 | 140 | 100 | 120 | Calibrated Dampener (Grade β)| Band 3-4 (Long) |
"""
    lines.append(team_table.strip() + "\n\n")
    
    lines.append("### 2.2 Sovereign Boss: Dekan, The Containment Lead (`ECHO-CORE-03`)\n")
    boss_info = """- **Coherence Rank & Potency:** Rank IV Sovereign (Floor 02 Departmental Lead) • Grade Delta (δ) Potency
- **Total Composure Pool:** 450 Points • Meltdown Inversion Threshold: 0 Points
- **Base Speed:** 5 (Generates 4 Action Points per turn in Phases 1–3; 5 AP in Phase 4)
- **Modular Body Part Anatomy:**

| Modular Part Name | Part Max HP | Rupture Threshold (60%) | Lament Def | Grudge Def | Void Def | Weight Def |
|---|---|---|---|---|---|---|
| **Basalt Ward Helm** | 600 HP | 360 HP | 1.0x | 0.8x | 1.2x | 0.5x |
| **Hydraulic Vault Core**| 1,200 HP | 720 HP | 0.8x | 1.0x | 0.8x | 0.6x |
| **Maw-Chained Gauntlet**| 750 HP | 450 HP | 1.2x | 0.7x | 1.0x | 0.8x |
| **Grounding Anchor Spik**| 500 HP | 300 HP | 0.9x | 1.2x | 1.0x | 0.4x |
"""
    lines.append(boss_info.strip() + "\n\n---\n")
    
    # Section 3
    lines.append("## 3. 10-Node Spatial Combat Grid & Environmental Architecture\n\n")
    lines.append("The spatial battlefield across Floor 02's central containment amphitheater is mapped across ten linear tactical nodes:\n\n")
    
    # 10-node spatial combat grid banner
    grid_lines = [
        bf.make_borderless_banner("10-NODE SPATIAL COMBAT GRID: FLOOR 02 CONTAINMENT AMPHITHEATER", width=71),
        "[NODE 01] [NODE 02] [NODE 03] [NODE 04] [NODE 05] [NODE 06] [NODE 07] [NODE 08] [NODE 09] [NODE 10]",
        "[ Jinho ] [ Baffle] [       ] [Min-Jae] [ Taeho ] [Seol-A ] [       ] [       ] [ DEKAN ] [       ]",
        "[Comms  ] [ Cover ] [ Empty ] [ANCHOR ] [STRIKER] [ FLANK ] [ Empty ] [ Empty ] [BOSS   ] [ Empty ]",
        "-" * 71,
        "Node 01 : Entrance airlock threshold / Jinho acoustic sensor station.",
        "Node 02 : Hydraulic pressure baffle / Kinetic cover barrier.",
        "Node 03 : Mid-gallery conduit ramp / Secondary staging position.",
        "Node 04 : Frontline defensive fulcrum / Min-Jae Bastion Anchor line.",
        "Node 05 : Forward engagement salient / Taeho kinetic disruption point.",
        "Node 06 : Lateral drainage flume / Seol-A high-speed flanking channel.",
        "Node 07 : Outer containment ring / Seismic floor hazard boundary.",
        "Node 08 : The Precipice Threshold / Liquid sorrow trench overflow.",
        "Node 09 : The Maw's Keep Dais / Dekan Sovereign Core locus.",
        "Node 10 : Abyssal Gate 02 / The Deep Maw quarantine threshold.",
        "=" * 71
    ]
    lines.append("```text\n" + "\n".join(grid_lines) + "\n```\n\n---\n")
    
    # Section 4: Phase-by-Phase Breakdown
    lines.append("## 4. Four-Phase Realization Combat Progression\n\n")
    
    phase_box_rows = [
        "THE FOUR REALIZATION ENGAGEMENT PHASES",
        "PHASE 1: DENIAL (100% -> 75% HP) — THE UNBROKEN VAULT",
        "- Dekan manifests heavy basalt bulkheads and immovable parries.",
        "- Trait: Unyielding Lock (Takes 50% reduced kinetic stagger).",
        "-------------------------------------------------------------------",
        "PHASE 2: ANGER (75% -> 50% HP) — THE HYDRAULIC ERUPTION",
        "- Floor plates buckle; boiling coolant floods Nodes 4-7.",
        "- Trait: Pressurized Venting (+3 Clash Power to heavy swings).",
        "-------------------------------------------------------------------",
        "PHASE 3: BARGAINING (50% -> 20% HP) — THE TETHERED SHADOWS",
        "- Spectral chains manifest from the Maw, pulling squad forward.",
        "- Trait: Composure Leech (Drains 12 allied Composure per turn).",
        "-------------------------------------------------------------------",
        "PHASE 4: CATHARSIS (20% -> 0% HP) — THE SOVEREIGN AWAKENING",
        "- Stagger thresholds invert to True Grit; Dekan readies Final Gate.",
        "- Tactical Goal: Synchronized 4-way clash to shatter trauma vessel."
    ]
    lines.append(wrap_box(bf.make_box("ECHO-CORE REALIZATION PHASE ENGINE", phase_box_rows, width=71)))
    
    lines.append("### 4.1 Climax: Phase 4 Battle Turns (Turns 1 Through 6)\n\n")
    lines.append("The decisive confrontation occurs within Phase 4, where the squad must synchronize their Action Points and Speed Bands to break Dekan's despair without dealing lethal trauma:\n\n")
    
    turn_rows = [
        "TURN 1: SPEED INITIATIVE & CONTAINMENT OVERLOAD",
        "- Dekan enters Phase 4 Sovereign Stance (Speed 6 / 5 AP).",
        "- Intention: Charges [Absolute Quarantine Seal] targeting Nodes 4-6.",
        "- Allied Initiative: Seol-A Speed 8, Taeho Speed 5, Min-Jae Speed 3.",
        "- Action: Min-Jae establishes [Citadel Redoubt] at Node 4 (2 AP).",
        "- Posture holds at 190/210. Area deflection aura protects trench.",
        "-------------------------------------------------------------------",
        "TURN 2: BREAKING THE SEISMIC ANCHORS (PILLAR: PRESENCE)",
        "- Dekan unleashes [Tectonic Slam] (Clash Power 26 vs Min-Jae 28).",
        "- Victory Min-Jae! Kinetic shock absorbed into basalt floor plates.",
        "- Taeho uses 3 AP on [Ancestral Sunder] targeting Grounding Spikes.",
        "- Presence Trigger: Dekan witnesses Min-Jae holding the vault door",
        "  open for his squad, realizing a warden never locks comrades out.",
        "- Dekan Composure slips: 180 -> 120/450.",
        "-------------------------------------------------------------------",
        "TURN 3: THE HIGH-VELOCITY ACOUSTIC FLANK",
        "- Seol-A expends 4 AP on [Silenced Siphon Dash]:",
        "  Maneuvers from Node 6 -> Node 8 across liquid sorrow trench.",
        "- Strikes Maw-Chained Gauntlet with [Missing Note Thrust].",
        "- Gauntlet ruptured (60% threshold met)! Disables [Crushing Grip].",
        "-------------------------------------------------------------------",
        "TURN 4: THE PRECIPICE OF THE MAW (PILLAR: PRECIPICE)",
        "- Dekan initiates ultimate skill [The Maw's Eternal Gate] at Node 9.",
        "- Massive 360-degree Weight burst charging; threatens whole floor.",
        "- Precipice reached: Min-Jae steps into Node 7 directly facing Dekan.",
        "- Min-Jae speaks: 'You kept the beasts inside for a thousand years,",
        "  Dekan. But you don't have to lock yourself in with them!'",
        "-------------------------------------------------------------------",
        "TURN 5: SYNCHRONIZED COUNTER-CLASH (PILLAR: PURPOSE)",
        "- Jinho discharges [Harmonic Baffle Surge] from Node 1, disrupting",
        "  Dekan's acoustic focus and reducing Boss Clash Power by 6.",
        "- Taeho and Seol-A launch synchronized cross-strike at Node 8.",
        "- Dekan's trauma vessel cracks! Sapphire Han-light bleeds outward.",
        "-------------------------------------------------------------------",
        "TURN 6: THE RESONANT AWAKENING (PILLAR: PACT)",
        "- Min-Jae charges from Node 7 -> Node 9 with [Citadel Sunder Parry]!",
        "- Final Clash Power: 46 vs 34! CRITICAL CLASH OVERWHELM!",
        "- Min-Jae's shield strikes Dekan's Basalt Ward Helm with perfect precision.",
        "- The blackened trauma shell shatters; Dekan's true Sovereign Core",
        "  ignites with brilliant golden-blue dawn light. Meltdown reversed!"
    ]
    lines.append(wrap_box(bf.make_box("TACTICAL REALIZATION LOG: PHASE 4 (TURNS 1-6)", turn_rows, width=71)))
    
    # Section 5
    lines.append("## 5. The Four Pillars of Psychological Realization\n\n")
    pillars_text = """During the engagement, Dekan's psychological journey mirrors the Four P-Framework established in the Reverie Directorate Realization Codices:

1. **Presence (  실재  / Siljae [Presence]):**
   - In Phase 1 and 2, Dekan perceives his squad not as living comrades, but as future corpses doomed to be swallowed by containment failures.
   - When Min-Jae plants his *Tectonic Bulwark* at Node 4 and refuses to retreat, Dekan is forced to perceive their tangible, breathing reality. The living presence of his peers halts his descent into nihilism.
2. **Precipice (  절벽  / Jeolbyeok [Precipice]):**
   - At the transition to Phase 4, Dekan stands at the edge of Node 10, overlooking the abyssal maw of Floor 02.
   - He confronts the terror that his life's work has been meaningless—that Mugenhan will eventually fall regardless of containment protocols. Standing at this emotional precipice, he must choose between voluntary annihilation and renewed purpose.
3. **Purpose (  목적  / Mokjeok [Purpose]):**
   - Min-Jae, Taeho, and Seol-A reject the premise of eternal containment. They declare that prisons exist to protect the living, not to entomb the guardians.
   - Reclaiming his identity as the sovereign keeper of the threshold, Dekan channels his guilt into unshakeable protective resolve.
4. **Pact (  맹약  / Maeng-yak [Pact]):**
   - The climactic parry-clash shatters the blackened basalt shell of despair without harming Dekan's living vessel.
   - Dekan and Strike Team Alpha swear a mutual covenant: the Maw will be contained, but the wardens will walk out of the dark together at the end of every watch.
"""
    lines.append(pillars_text.strip() + "\n\n---\n")
    
    # Section 6
    lines.append("## 6. After-Action Report & Sovereign Awakening Rewards\n\n")
    sec6_text = """### 6.1 Containment Assessment & Structural Recovery

```text
+=====================================================================+
|              REVERIE DIRECTORATE REALIZATION AFTER-ACTION           |
+---------------------------------------------------------------------+
| OPERATION STATUS  : SUCCESSFUL REALIZATION CATHARSIS                |
| FLOOR STABILITY   : 100% Harmonic Equilibrium Restored (-1,200m)    |
| CASUALTIES        : Zero Fatalities / Composure Fully Restored      |
| RECOVERED ARTIFACT: Key Page: The Containment Sovereign (Dekan)     |
+=====================================================================+
```

### 6.2 Key Page: The Containment Sovereign (Dekan)
- **Equip Requirement:** Assigned Lead Warden (Posture 180+ / Composure 110+)
- **Sovereign Passive 1 — Unyielding Bastion Threshold:**
  All allied operatives occupying defensive nodes (`[N01]` to `[N04]`) gain +2 Clash Power and +15% Weight and Lament damage resistance.
- **Sovereign Passive 2 — Seal the Maw:**
  When an enemy entity initiates a breach action or prepares an area-of-effect skill, Dekan can expend 2 AP to deploy an *Acoustic Hydraulic Ward* across two nodes, canceling the hostile movement and reducing target Clash Power by 4.
- **Awakened Combat Skill — Sovereign Sunder Lock (3 AP • Band 1-2 • Power 38):**
  Dekan slams the awakened *Maw-Keeper's Greatshield* into the ground, sending a shockwave through the bedrock. Deals 65 Weight Blunt damage and inflicts *Containment Lockdown* (target cannot gain Speed Bands above 3 for 2 turns).

---
"""
    lines.append(sec6_text.strip())
    
    content = "\n".join(lines)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {OUTPUT_PATH} ({len(content)} bytes)")

if __name__ == "__main__":
    build_scenario_dekan()
