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
| 2–3 | 2 AP | Stationary barriers, siege engines, the Final Door (Speed 2, stationary) |
| 4–5 | 3 AP | Vault wardens (Speed 5), Archive Lead Marjuk (Speed 4) |
| 6–7 | 4 AP | Echo-Core field operative Xyan (Speed 7), the Frozen Veil (Speed 6) |

Speed Band effects (for example, −1 Speed Band from time-slip) shift the operative one row
down this table for the stated duration; AP already spent is not refunded.

> **Sovereign Speeds — honest accounting:** no mobile Sovereign has ever been encountered in a tactical log. The only Sovereign with an attested tactical Speed is the stationary Final Door (Speed 2). The Stormscale’s dossier-14 rating is a meters-per-second pursuit scale, not a tactical Speed, and must never be read into this table.

### Dossier pursuit speeds vs tactical Speed

Dossier pursuit ratings in meters per second describe overland chase pace, not grid bandwidth: they never convert into tactical Speed and never award AP. The Stormscale’s dossier-14 rating is the standing example — a 14 m/s pursuit scale, unrelated to the Speed 2–7 tactical bands above.

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

Dossier HP converts 1:1 into tactical HP: no scaling, no rank multiplier. Attested anchors: Rank IV dossiers run 390–1,000 by role (median ~824); Rank V spans from the low hundreds (lowest attested peer 521) through four-digit multi-part totals (the Colossus’s 2,600), with Dawn-002’s 12,000 standing as a documented outlier. Multi-part bosses split their total into per-part pools (the Colossus: 600 / 500 / 500 / 1,000); each part ruptures at 60% depletion per the dual-threshold stagger engine, and parts — never the pooled total — are the damageable unit. Objectives logged with HP N/A cannot be damaged at all: resolve them only through their stated suppression or Resolve condition.

### 5.2 Mind (Composure / SP)

Psychic integrity on the compressed 0-50 field gauge standard to SED, UCD, HORIZON, and
descent operations. Canto dossiers record the same stat as full attribute baselines
(105–120); both scales break at thirty percent.

| Gauge Mark | Meaning |
|---|---|
| 50 (full) | Fresh; no effects |
| 30 | Doctrine caution: no lone nodes, no point positions |
| 20 | Second caution: buddy pairs mandatory, shields shared |
| **At or below 15 — the Transform line** | Onset begins: the member counts as separated for isolation effects, cannot hold a lone node, and any breach vector in play may trigger through them |
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

| Difficulty | Target | Typical cause |
|---|---|---|
| Routine | 10 | Standard dread aura, minor entrapment |
| Hard | 14 | Entity-grade dread, active transformation pressure |
| Extreme | 18 | Sovereign dread (God Dread), deep entrapment |
| Mythic | 22 | Direct witness of a Rank V manifestation |

> **Provisional:** no Resolve target numbers appear in any engagement log; this table is authored doctrine until logs attest values.

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
- Speed attestations (Final Door 2, Marjuk 4, wardens 5, Frozen Veil 6, Xyan 7): Nareumhan descent logs and Canto dossiers.
- Colossus part pools (600 / 500 / 500 / 1,000) and 60% rupture: BOSS_MECHANICS pools record.
