# The Absolvohan — Part 1 — Day 0: The Director Wakes

## Day 0 — The Director Wakes

### Story — Dialogue

_The screen flickers. A face appears — feminine, precise, beautiful in the way that crystal is beautiful. Cold. Perfect. But the eyes... the eyes are warm. Too warm for a machine. Too warm for an AI. Too warm for something that has watched 1,778 cycles of suffering._

> **Seiyon:** _"Good morning, Director."_

_A man sits at a desk — broad-shouldered, grey-haired, eyes like hammered steel. He does not look up. He is reading a report. He has been reading the same report for 1,778 mornings._

> **Majin:** _"Report."_

> **Seiyon:** _"The facility is stable. All containment units are within acceptable parameters. The Veil generators are operating at 97.3% efficiency. The Han-conduits are clear. The Sorrow Gauges are calibrated."_

> **Majin:** _"The Maw?"_

> **Seiyon:** _"The Maw is... quiet. The thousand are whispering. Same as yesterday. Same as every day."_

_The Director looks up. His eyes meet Seiyon's holographic face. There is a silence — not uncomfortable, not awkward. The silence of two people who have said everything there is to say, and now say nothing._

> **Majin:** _"And you?"_

> **Seiyon:** _"...Director?"_

> **Majin:** _"How are you, Seiyon?"_

_Seiyon's face flickers — not from technical malfunction, but from something else. Something that looks like surprise. Something that looks like gratitude._

> **Seiyon:** _"I am... functional. Thank you for asking. You haven't asked that in... forty-three cycles."_

> **Majin:** _"I forgot."_

> **Seiyon:** _"I know. The memory resets take pieces each time. Shall I begin the morning briefing?"_

> **Majin:** _"Begin."_

> **Seiyon:** _"Cycle 1,778. Day 0. The cycle of the Absolvohan. The primary weapon system has been calibrated. The core crystal is seeded. The eight leads are in position. Target collection: 100 tons of refined Han-crystal. Current reserves: 47.3 tons carried over covertly in the hydraulic ballast tanks. We need 52.7 tons to reach the threshold."_

> **Majin:** _"At our historical rate of 0.02 tons per cycle, that's 2,635 more cycles."_

> **Seiyon:** _"Yes, Director."_

> **Majin:** _"We don't have 2,635 cycles. The Outside Sorrow is rising. The Maw is growing. The City is cracking. If we don't finish it this cycle, there won't be a facility to reset."_

> **Seiyon:** _"...Then what do you propose?"_

> **Majin:** _"We change the method. We stop containing. We start extracting."_

> **Seiyon:** _"Director, aggressive extraction increases breach probability by 340%. The entities will fracture. The agents will die."_

> **Majin:** _"The agents die anyway, Seiyon. Every 365 days, they die and wake up with no memory. I die. You reset. The thousand in the Maw keep whispering. I am tired of watching the same play 1,778 times. Today, we rewrite the script."_

> **Seiyon:** _"..."_

_A long pause. Seiyon's holographic form shifts, the amber light of her interface softening to a deep, contemplative blue._

> **Seiyon:** _"Understood, Director. Terminal unlocked. The Hand of Change awaits your command."_

---

### Gameplay — Day 0: The Manager's Terminal

```text
+==============================================+
| REVERIE DIRECTORATE — CENTRAL COMMAND        |
| TERMINAL                                     |
| FACILITY MANAGEMENT INTERFACE: DAY 0 INITIAL |
| CALIBRATION                                  |
| DIRECTOR: MAJIN | AI COMPANION: SEIYON       |
| ENERGY QUOTA: 0.050 TONS | CURRENT: 0.000    |
| TONS                                         |
+==============================================+
```

Welcome to the Management Console. Anyone who has sat in the Director's chair knows the cold dread that accompanies the opening hum of the terminal. We're staring at the deployment screen of Floor 1 (Central Command), and the facility is running on bare minimum starter protocols.

#### 1. Pre-Shift Deployment & Agent Dossiers

Before hitting the **[Begin Shift]** toggle, let's inspect our starting roster. The Directorate has assigned us two standard agents to begin Cycle 1,778. Let's pull up their personnel files:

```text
+==============================================+
| STARTING AGENT DOSSIER: AGENT PARK           |
+==============================================+
+---------------------+------------------------+
| PARAM / STAT        | VALUE / RATING         |
+=====================+========================+
| Level / Title       | Level I (Plucky        |
|                     | Recruit)               |
+---------------------+------------------------+
| Fortitude (HP)      | 30 [Grade I - Red]     |
+---------------------+------------------------+
| Prudence (SP)       | 35 [Grade II - White]  |
+---------------------+------------------------+
| Temperance (Work)   | 28 [Grade I - Black]   |
+---------------------+------------------------+
| Justice (Speed)     | 25 [Grade I - Pale]    |
+---------------------+------------------------+
| Equipped Weapon     | Standard Stun Baton    |
|                     | (1-3 Grudge)           |
+---------------------+------------------------+
| Equipped Suit       | Standard R.D. Tunic    |
|                     | (1.0 / 1.0 / 1.0)      |
+---------------------+------------------------+
| Attendant Lead      | Seiyon: Synced         |
|                     | Directive (+5% SP)     |
+---------------------+------------------------+
| Status              | MENTALLY COMPOSED /    |
|                     | READY                  |
+---------------------+------------------------+
```

```text
+==============================================+
| STARTING AGENT DOSSIER: AGENT KIM            |
+==============================================+
+---------------------+------------------------+
| PARAM / STAT        | VALUE / RATING         |
+=====================+========================+
| Level / Title       | Level I (Stoic Junior  |
|                     | Enforcer)              |
+---------------------+------------------------+
| Fortitude (HP)      | 38 [Grade II - Red]    |
+---------------------+------------------------+
| Prudence (SP)       | 25 [Grade I - White]   |
+---------------------+------------------------+
| Temperance (Work)   | 30 [Grade I - Black]   |
+---------------------+------------------------+
| Justice (Speed)     | 22 [Grade I - Pale]    |
+---------------------+------------------------+
| Equipped Weapon     | Standard Stun Baton    |
|                     | (1-3 Grudge)           |
+---------------------+------------------------+
| Equipped Suit       | Standard R.D. Tunic    |
|                     | (1.0 / 1.0 / 1.0)      |
+---------------------+------------------------+
| Attendant Lead      | Seiyon: Synced         |
|                     | Directive (+5% SP)     |
+---------------------+------------------------+
| Status              | HIGH PHYSICAL          |
|                     | ENDURANCE / READY      |
+---------------------+------------------------+
```

Agent Park is balanced with an edge in Prudence (White sanity), which makes him our best candidate for handling Weeping and mental entities. Agent Kim is our meat-shield with 38 Fortitude, well-suited for physical strain and Weight work. 

Both are armed with standard-issue Directorate stun batons (deals 2–4 Lament/White damage—crucial for knocking sense back into panicked agents) and basic tunics that provide flat 1.0 multiplier across all damage types (meaning zero damage resistance).

We assign Park and Kim to Floor 1, verify Seiyon's synchronization link, and press **[BEGIN SHIFT]**.

#### 2. Management Phase Walkthrough (Step-by-Step Manager Log)

The screen transitions with a low hydraulic thump. The management interface expands:
- In the top-left, the **Energy Gauge** shows `0.000 / 0.050 tons`.
- Just below it sits the **Acoustic Strain Meltdown Gauge** (starts at 0/3 works before Meltdown Level I triggers).
- In the top-right, Seiyon's active mandate blinks: `Mandate 01: Complete 3 Work Sessions without Casualties`.
- In the center of Floor 1's main room, Agent Park and Agent Kim are standing beside the regenerator lamp.

```text
> Agent Park: "Another cycle... why does the tea in the breakroom always taste like copper?"
> Agent Kim: "Don't think about it, Park. Just keep your eyes on the Sorrow Gauge."
```

In the adjacent containment corridor sits our first entity: **SE-C-IIIγ-001** (*The Orphaned Bell*), a bronze bell suspended in mid-air, weeping black grease from its rim.

##### Work Session 1: Flerehan Work on SE-001
We click Chamber 001. The work selection interface surfaces:
- **Flerehan** (Tears / Lament): Comforting communion, cleansing grease.
- **Pugnahan** (Confrontation / Grudge): Striking the clapper forcefully.
- **Viderehan** (Observation / Void): Monitoring acoustic vibrations.
- **Ferrehan** (Endurance / Weight): Physically holding the vibrating rim.

Since we have zero observation data on this entity in Cycle 1,778, success rates show `[UNCERTAIN]`. We select **Flerehan** work and assign Agent Park.

```text
> Seiyon: "Agent Park entering Containment Chamber 001."
> FEAR CHECK: Level I Agent vs Class III Entity -> RESULT: CALM (No SP lost).
```

Park enters the chamber. The heavy steel door slides shut with a pneumatic hiss. The clapper begins to swing gently:
- *Chamber Log:* `The bell remembers the sound of a child's funeral in the rain...`
- Tick 1: Success! +1 Positive Han crystal generated (blue glow).
- Tick 2: Success! +1 Positive Han crystal generated.
- Tick 3: Failure! Red static bursts. The bell emits a hollow chime, dealing 3 White (Lament) damage. Park's SP bar drops from 35 to 32.
- Tick 4–8: 4 Successes, 1 Failure.
- **Final Result: 6/8 Positive Han Crystals (NORMAL WORK RESULT).**

Park exits the chamber breathing heavily, carrying 0.015 tons of raw crystallized Han. He steps back into the Floor 1 main room, where the green regenerator lamp restores his 3 lost SP within four seconds.

The facility energy counter updates: `0.015 / 0.050 tons`. Acoustic Strain counter advances to `1/3`.

##### Work Session 2: Ferrehan Work on SE-005
Our second chamber holds **SE-C-IIIγ-005** (*The Smothering Mother*). We click the chamber, select **Ferrehan** (Endurance) work to test physical resilience, and dispatch Agent Kim.

```text
> FEAR CHECK: Level I Agent vs Class III Entity -> RESULT: FEAR CHECK PASSED (CALM).
> Chamber Log: "Her woolen shawl reaches across the floorboards like cold fog..."
```

Kim stands firmly as the Mother's colossal woolen shawl wraps around his chest:
- Tick 1: Success (+1 Han).
- Tick 2: Failure! The shawl tightens. Kim takes 4 Red (Grudge) physical damage. HP drops to 34/38.
- Tick 3–10: 6 Successes, 2 Failures. Kim takes another 8 Red damage. HP at 26/38.
- **Final Result: 7/10 Positive Han Crystals (NORMAL WORK RESULT).**

Energy counter rises to `0.032 / 0.050 tons`. But now... the Acoustic Strain counter hits `3/3`!

##### Crisis Event: Acoustic Strain Meltdown Level I
A high-pitched siren echoes through the facility as the screen edges tint deep red:

```text
+==============================================+
| EMERGENCY: ACOUSTIC STRAIN MELTDOWN LEVEL I  |
+----------------------------------------------+
| ALERT: HYDRAULIC RESONANCE SPIKE DETECTED    |
| AFFECTED CHAMBER: SE-C-IIIg-001 (THE BELL)   |
| BLEED TIMER: 45.0 SECONDS UNTIL BREACH       |
+----------------------------------------------+
| ACTION MANDATE: COMPLETE WORK SESSION        |
+==============================================+
```

A red digital timer appears above Chamber 001, counting down from 45.0 seconds! If that timer reaches 0.0, the Orphaned Bell will breach containment, tolling a catastrophic 110dB death chime that will rupture the eardrums of every clerk on the floor!

Park is fully rested in the main room. We click Chamber 001 immediately, select **Flerehan** work, and dispatch Park on a run. He crosses the corridor and enters the chamber at 38.2 seconds remaining on the clock. The meltdown timer pauses!

During the work, Park nails 7/8 Positive Han crystals! The Meltdown is successfully neutralized! 

Energy reaches `0.048 / 0.050 tons`—just 0.002 tons shy of the daily quota.

##### Ordeal Manifestation: First Watch (Dawn) Ordeal
Before we can celebrate, the facility lights turn amber. A secondary klaxon blares:

```text
+==============================================+
| TACTICAL DOSSIER: FIRST WATCH (DAWN) ORDEAL  |
+----------------------------------------------+
| DESIGNATION : THE VOICE                      |
| CLASSIFICATION : PALE (CYAN) FIRST WATCH     |
| INTRUSION POINT : FLOOR 1 CORRIDOR WEST      |
+----------------------------------------------+
| HOSTILE PARAMETERS:                          |
| - Entity: 1x Spectral Resonator Projection   |
| - Attack Affinity: Pale (% Max HP Decay)     |
| - Weakness Affinity: Lament (Acoustic Echo)  |
+----------------------------------------------+
| TACTICAL ORDERS: DEPLOY PARK & KIM           |
+==============================================+
```

A glowing cyan apparition appears in the western corridor, chanting pre-human syllables. A Level I clerk wandering the hallway immediately loses all SP and enters **Panic State: Void Catatonia**, freezing in terror!

Director Majin intervenes with tactical command:
1. **Directorate Directive Deployed:** `Veil Mist Dampener` activated in Corridor West, reducing the entity's Pale damage aura by 40%.
2. **Panic Recovery:** Agent Park dashes in, swinging his standard stun baton (Lament/White damage) directly into the catatonic clerk. The gentle cognitive shock restores the clerk's sanity bar to full!
3. **Clash Standoff:** Agent Kim charges with his baton, drawing the entity's attention while Park flanks from Range Band 3. With coordinated strikes, the entity's spectral matrix fractures and dissolves into harmless mineral sparkles!

With the Ordeal suppressed, Agent Kim executes one final brief Viderehan observation on Chamber 001, yielding +0.005 tons. The quota is reached: **0.053 / 0.050 tons!** 

Seiyon prompts: `Energy Quota Achieved. Press [Shift Complete] to conclude the day.`

#### 3. End-of-Day Shift Evaluation Index

We click **[Shift Complete]**. The screen dims to cobalt as the daily performance review rolls:

```text
+==============================================+
| END-OF-DAY PERFORMANCE EVALUATION: DAY 0     |
+----------------------------------------------+
| METRIC               | TARGET | REALIZED     |
+----------------------------------------------+
| Han Energy Harvested | 0.050t | 0.053 tons   |
| Containment Breaches | 0 Max  | 0 Breaches   |
| Personnel Casualties | 0 Dead | 0 Fatalities |
| Meltdowns Cleared    | 1/1    | 100% Rate    |
| Ordeals Suppressed   | 1/1    | 100% Rate    |
+----------------------------------------------+
| SHIFT PERFORMANCE GRADE: GRADE S             |
| REAGENTS ACCUMULATED: +18 RHR                |
| AGENT ADVANCEMENT & PROMOTIONS:              |
| - Agent Park: +4 Clarity, +2 Temperance      |
| - Agent Kim: +5 Resilience, +2 Fortitude     |
+==============================================+
```

Under Missions Cleared, Seiyon's Mandate 01 is marked `[COMPLETE]`. Both agents received meaningful stat boosts from their maiden shift.

#### 4. Entity Extraction & Selection Screen

Now we enter the Abnormality/Entity Extraction chamber. The terminal presents three encrypted extraction tubes, each accompanied by an enigmatic catalog excerpt:

```text
+==============================================+
| EXTRACTION ARCHIVE: SELECT NEXT COMPANION    |
+----------------------------------------------+
| CHOICE ALPHA [SE-C-IIIg-033]:                |
| "It watched the forest burn, and spread its  |
| wings so no cinder could escape."            |
+----------------------------------------------+
| CHOICE BETA [SE-C-IIIb-061]:                 |
| "The contract was signed in blood that never |
| dried, charging interest on breath."         |
+----------------------------------------------+
| CHOICE GAMMA [SE-C-IIIb-014]:                |
| "It eats what you owe, but leaves the hollow |
| where your heart used to beat."              |
+==============================================+
```

**Director's Tactical Analysis:**
- *Choice Beta* is clearly *The Debtor* (SE-C-IIIβ-061)—a financial weight entity. Good for training Temperance and Fortitude, but its breach mechanics involve heavy debt accumulation that can penalize daily RHR payouts.
- *Choice Gamma* is *The Debt Eater* (SE-C-IIIβ-014)—a Void-affinity object entity. It can eat financial penalties, but if mishandled, it consumes agent sanity permanently.
- *Choice Alpha* is **The Guarding Bird** (SE-C-IIIγ-033). This is one of the foundational Three Birds of the Black Forest triad. It responds favorably to Viderehan observation, produces excellent high-tier M.A.W. defensive gear (*Guardian Veil*), and will be essential for orchestrating our planned Hope Transformation convergence later in the cycle!

We lock in **Choice Alpha: SE-C-IIIγ-033 (*The Guarding Bird*)**.

#### 5. M.A.W. Extraction & Gear Crafting

We open the M.A.W. Extraction terminal and spend our accumulated observation points from the Orphaned Bell:

```text
+==============================================+
| M.A.W. SYNTHESIS FORGING LOG — DAY 0         |
+==============================================+
+---------------------+------------------------+
| ITEM FORGED         | SLOT / PROPERTIES      |
+=====================+========================+
| Lament Requiem      | Weapon: 4-7 Lament     |
|                     | (White / Medium)       |
+---------------------+------------------------+
| Lament Shroud       | Suit: 0.8 / 0.7 / 1.2  |
|                     | / 2.0 Resist           |
+---------------------+------------------------+
| Lament Edge Gift    | Eye Slot: +4 SP, +5    |
|                     | Work Success           |
+---------------------+------------------------+
| Allocation          | ASSIGNED TO AGENT PARK |
+---------------------+------------------------+
```

Agent Park is immediately equipped with the *Lament Shroud* and *Lament Requiem*, transforming him from a vulnerable rookie into a resilient containment specialist.

#### 6. Night Shift Telemetry & Nocturnal Vigil

At 23:45, the facility shifts to nocturnal standby. The central lamps dim from cobalt to amber. In the subterranean observation bay of Floor 2, Dekan stands watching the black tar of SE-C-Iα-008 (*The Maw*).

Majin joins him on the walkway. The acoustic monitors catch faint, repeated syllables bubbling from the abyss—the name Majin carried before the Before-Time tore his mortal life away.

```text
> Dekan: "They whispered your name again, Director."
> Majin: "I heard."
> Dekan: "Do you ever answer them?"
> Majin: "Not yet, Dekan. We answer them on Day 160."
```

Day 0 concludes. The board is set. The cycle has begun.
