# Action Dice & Clash Resolution — GBS Tactical Rules

## Grid Battle System combat lexicon: dice, AP, clashes, and gauges

---

This file defines every action name, die, and resolution step used in Grid Battle System
engagement logs (Nareumhan descent records, GAME_BATTLE scenarios, SED/UCD after-action
reports). The engine frame — 10-node grid, Range Bands 1–5, Four P-Framework — is defined
in `README.md`; what follows is the resolution layer those logs assume.

---

## 1. Speed & Action Points

Speed is operational bandwidth: higher Speed acts earlier in the turn and receives more
Action Points. One AP purchases one die (attack, defense, or maneuver); unspent AP is lost.

| Speed | AP per Turn | Attested Operatives |
|---|---|---|
| 2–3 | 2 AP | Stationary barriers, siege engines |
| 4–5 | 3 AP | Vault wardens (Speed 5), Archive leads (Speed 4) |
| 6–7 | 4 AP | Echo-Core field operatives (Speed 7), Wail-rank entities (Speed 6) |
| 8+ | 5 AP | Sovereign-rank entities, realized Echo-Cores |

Speed Band effects (for example, −1 Speed Band from time-slip) shift the operative one row
down this table for the stated duration; AP already spent is not refunded.

---

## 2. The Dice Lexicon

Every die is rolled as a flat range (for example, Gash 6-10 rolls 6 to 10). Bands below are
operative-grade as attested in the Nareumhan logs; entity and Sovereign dice run higher.

### 2.1 Offense Dice (P4: Poise — breaking stance)

| Die | Effect | Attested Band |
|---|---|---|
| Gash | Slashing damage; disrupts manifestations and tendrils | 4-7 (detachment), 6-10 (operative) |
| Bludgeon | Crushing damage; clears nodes, bashes barriers | 5-9 |
| Skewer | Piercing damage; defeats armor and carapace | Per issuing M.A.W. |
| Burn | Incendiary damage over sweeps; denies ground | Per issuing M.A.W. |

### 2.2 Defense Dice (P3: Parry / Protection — winning clashes)

| Die | Effect | Attested Band |
|---|---|---|
| Block | Shield and guard dice; negates HP damage on a won clash | 4-8 (operative), 8-12 (shield-wall), 14-18 (bulwark) |
| Evade | Dodge dice; avoids the attack entirely on a won clash | Per issuing M.A.W. |
| Counter | Riposte dice; on a won clash, negates and returns margin damage | 3-6 |

Block is the shield-wall member of the Parry family: wardens Block where unshielded
operatives Parry. The resolution is identical; only the instrument differs.

---

## 3. Clash Resolution

When an attack die and a defense die meet in mutual range, they clash: both roll, higher
roll wins. Ties favor the defender.

- **Defense wins:** HP damage is negated. The defender still suffers block-cost Weight
  strain (the shock through the guard), and the clash margin spills as additional Posture
  strain on the loser.
- **Attack wins:** full damage lands on HP and Composure; the margin spills as Posture
  strain on the defender.
- **Counter wins:** as defense wins, and the margin is returned to the attacker as damage.
- **Unopposed attacks:** no clash is rolled; full damage lands. This is why formations
  never leave a working node uncovered.

Splash is damage that reaches an adjacent node after the primary clash: reduced dice,
no second clash. Interception (throwing a guard across another's node) moves the clash to
the interceptor's dice.

---

## 4. Damage Elements

| Element | Vector | Notes |
|---|---|---|
| Void | Erasure, isolation, cold | Ignores cover at Sovereign grade; severs relays |
| Lament | Grief, water, sound | Wounds weep; suppresses Composure first |
| Grudge | Resentment, iron, verdict | Resisted by its own bearers; heaviest HP pressure |
| Weight | Burden, debt, mass | Strikes HP and Composure together; causes strain |
| Hope | Dawn-grade ordnance | Sovereign-tier only; resets breaking points |

Mixed damage cycles elements in sequence (see Sovereign dossiers). Resistance notation
(0.5x, 1.0x, 1.5x, 2.0x with Exposed markers) multiplies landed damage after the clash.

---

## 5. Health Tracks

### 5.1 Body (HP)

Physical integrity as a percentage. Burns, cuts, splinters, and fractures reduce HP;
field binding stabilizes but does not restore. HP wounds persist between chapters until
treated at a waystation or the surface (see the Nareumhan wound continuity).

### 5.2 Mind (Composure / SP)

Psychic integrity on the compressed 0-50 field gauge standard to SED, UCD, HORIZON, and
descent operations. Canto dossiers record the same stat as full attribute baselines
(105–120); both scales break at thirty percent.

| Gauge Mark | Meaning |
|---|---|
| 50 (full) | Fresh; no effects |
| 30 | Doctrine caution: no lone nodes, no point positions |
| 20 | Second caution: buddy pairs mandatory, shields shared |
| **15 — the Transform line** | Onset begins: the member counts as separated for isolation effects, cannot hold a lone node, and any breach vector in play may trigger through them |
| 0 | Terminal Meltdown (P2: Panic); the member is lost to the field |

Recovery above 15 arrests onset but leaves a Transform scar: a permanent mark (frost-veins,
iron-fleck, glass-cut that never closes) and a permanent Frailty the table agrees — the
body keeps the score the gauge forgives. The Canto-scale equivalent of the line is the
Crisis Threshold band (30–45).

### 5.3 Strain (Weight) and Posture

Weight strain is the shock-load of blocked hits, lost clashes, and vault pressure; it
accumulates separately from Composure and clears at waystations. Posture is stance: when
margin strain collapses Posture, the operative Staggers (loses the next die); entity-grade
targets follow the dual-threshold stagger engine (60% part rupture, 0% meltdown).

### 5.4 Resolve

Resolve checks resist debuffs, dread auras, entrapment, and transformation pressure. Roll
against the stated difficulty with Composure as the anchor: high Composure steadies
Resolve, and Resolve failures cost Composure. Sovereign dread (God Dread) demands a
Resolve check every turn.

---

## 6. Grid, Turns, and Phases

Engagements run on the 10-node linear grid (surface-side Node 10 to depth-side Node 1 in
descent orientation). Six turns constitute one macro environmental phase; descent
gauntlets are scoped as exactly one phase, which is why every Nareumhan chapter runs six
turns. Retreat past the entry node invites one turn of pursuit before seals re-engage.

---

## 7. Source Index

- Dice bands, clash margins, and gauge marks: Nareumhan Descents 2–5 action logs.
- Clash-as-Parry, margin-as-strain: GAME_BATTLE README (P3: Parry / Protection).
- AP 2–5 economy, six-turn macro phase: Tactical Combat Engine README.
- 0-50 field gauge: HORIZON, MEMORY ARCHIVE, SED, UCD, Jipyeongseondae, Gieok codices.
- 105–120 baselines, Crisis Thresholds: Story Cantos 01–06 dossiers.
- Work-type permissions for entity handling: PROJECT_SOMNARAK (Viderehan, Ferrehan).
