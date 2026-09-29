# 00 — GLOBAL DEEP KNOWLEDGE PRIMER

**Template ID:** `T-00-GLOBAL`  
**Applies To:** Every generation task in the repository — read this before opening any other template  
**Authority:** `GOVERNANCE.md` Tier 1 (`RULE-TO-FOLLOW.md`) + `CANON_TIMELINE.md` SSOT + `tools/banned_strings.txt`  
**Status:** MANDATORY FIRST READ — No file may be generated without certifying these 9 laws

---

## PURPOSE OF THIS PRIMER

This primer exists so that **deep knowledge is known BEFORE there will ever was generating somethings**. It compresses 3.5 million words of canon, 6 governance documents, and 4 linters into 9 immutable laws. Memorize them. Every template in this kit repeats them in abbreviated form, but this is the authoritative source.

---

## THE 9 IMMUTABLE LAWS OF SOMNARAK

### LAW 1 — Master Macro-Chronological Partition (Epoch Order)

```
SED (Katabagil, -7,200m to -200m) → UCD (Katharcheok, The Raw) → R.D. Facility 01 / The Absolvohan (1,778 Cycles) → Dawn of Hope → Post-Dawn
```

- **Pre-Dawn (Before Dawn of Hope):** Only three institutions exist in sequence: SED first, then UCD, then Reverie Directorate. Nothing else.
- **Post-Dawn (After Dawn of Hope):** The Dawn Initiative & Lantern, Horizon Caravan (Jipyeongseondae), Memory Archive (Gieok Jeojangso) strata realizations, Wound Walkers / Company 4, continental reconnection — ALL occur strictly AFTER Dawn.
- **Violation = timeline_lint failure.**

### LAW 2 — Cycle Localization Law

- The **1,778 Mnemonic Cycles** belong **EXCLUSIVELY** to R.D. + The Absolvohan (Facility 01, Day 0–365 loop).
- No entity outside R.D. measures time in Cycles. They use **MMSS calendar years** (e.g., Year 4,238, Year 4216). UNK SEs use calendar years.
- Exception: A direct loop survivor may retrospectively reference “Cycle 1,778” in testimony — never as a current date.
- **Violation = timeline_lint failure.**

### LAW 3 — Unknown Entity Chronology (UNK SE Rule)

- All Unknown Sorrow Entities (`SE-O-IIIγ-1052`, `SE-N-Vω-1055`, etc.) manifest **strictly AFTER R.D. facility cycles** — in the post-Dawn / deep-Maw era.
- UNK SEs never appear in SED, UCD, or active R.D. cycle logs.

### LAW 4 — Continental Geography & Corporate Taxonomy

- **Geography is NEVER an SE.** Macro-geographical features (Sea of Glass, Crystal Peaks, Consoling Ocean, Numbing Tundra, Sorrow Lake, The Maw as terrain) belong strictly in `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_GEOLOGY.md` as planetary geography. Never catalog a mountain or ocean as `SE-`.
- **Somnarak has exactly 10 Primary Companies: 5 Main Companies + 5 Sub Companies.** All other facilities are “Somnarak Outsider Factory.” The Memory Archive (기억 저장소 / Gieok Jeojangso) is a municipal sanctuary, not a company — it was replaced in the 5 Main Companies by a sovereign corporate Wing.
- **Violation = audit_lore_archive SECC mismatch.**

### LAW 5 — No Invented SEs & Two-Work-Type Rule

- **Use ONLY the 292 dossiers in `SOMNARAK-WORLD/Sorrow_Entities/`.** Never invent a new `SE-` code.
- **Object, Place, and Time SEs use ONLY Viderehan and Ferrehan.** Flerehan and Pugnahan are strictly `N/A` for those manifestation classes. This is checked by `tools/auditors/audit_two_work_rule.py`.
- Subject-type SEs may use all four work types.

### LAW 6 — M.A.W. Timeless Manifestation Doctrine

- M.A.W. is **NEVER manufactured** in city workshops. It **crystallizes directly** from the emotional core and historical memory of the Sorrow Entity / Relic Entity.
- Weapon archetypes spanning Year 0000 to Year 9999+ (Guns, Katanas, Chakrams, Astral Prisms, Culverins, Mauls, Lenses, etc.) are **authentic manifestations of entity memory** — do NOT remove, nerf, or scrub weapon types. Preserve all archetypes.
- M.A.W. triad: Weapon (Offense), Suit (Armor), Stigma (Accessory). Quadripartite set = Side-Codex (A) + Weapon (B) + Suit (C) + Stigma (D).

### LAW 7 — Zero Banned Strings (PM Vocabulary & Modern Slip Purge)

The following are **strictly banned** in `SOMNARAK-WORLD/` and `GAME_BATTLE/` canon files (enforced by `tools/banned_strings.txt` + `seam_lint.py`):

- **Project Moon crossover terms:** `Abnormality`, `E.G.O`, `Sephirah`, `Qliphoth`, `Cogito`, `L-Corp`, `Fixer`, `Wing` (except Somnarak's 10 Companies), `Nest`, `Backstreets`, `ZAYIN/TETH/HE/WAW/ALEPH`, `Peccatula`.
- **Modern / anachronistic slips:** `GPS`, `battery acid`, `Kevlar`, `Teflon`, `depleted uranium`, `hospital` (use Sanatorium/Hospice), `phone` (use acoustic relay), `DNA` (use ancestral bloodline resonance seal), `Kevlar`, `Teflon`, `Hz` with numbers (use Harmonic Ley-Resonance, Infrasonic Groans, Ultrasonic Resonance).
- **Sanctioned terms only:** `Sorrow Entity (SE)`, `SECC`, `M.A.W. (비탄의 무장)`, `Han (한)`, `Reverie Directorate (몽환국)`, `Echo-Cores`, `Absolvohan`, `Council of Sighs`, `The Weeping`, `The Maw`.

### LAW 8 — Timeless Weapon Authenticity + Elemental Canon

- **Four Damage Elements:** Grudge (원한, physical), Lament (비탄, psychological), Void (공허, soul/memory), Weight (비중, gravitational collapse).
- **Four Work Types:** Ferrehan (인내 — Endurance), Flerehan (공감 — Empathy), Pugnahan (억제 — Suppression), Viderehan (관찰 — Observation).
- **Risk Ranks:** I Whisper (α) → II Murmur (β) → III Fragment (γ) → IV Entity (δ) → V Sovereign (ω).
- **Origins:** C City Sorrow (도한), N Inner Sorrow (내한), O Outside Sorrow (외한).

### LAW 9 — In-Universe Voice & Formatting Discipline

- **`SOMNARAK-WORLD/` is 100% in-universe.** Write as Directorate archival records, field logs, containment dossiers. No meta-commentary, no “as an AI,” no developer notes.
- **ASCII Boxes:** All boxes inside markdown must be inside ````text fences, exactly 74 columns wide (`+` to `+`, `|` to `|`) OR 127–128 wide for tactical monitors — never mixed. Zero Korean Hangul inside boxes (use Romaja: `Dohan`, `Naehan`, `Oehan`, `Gieok Jeojangso`).
- **Outside boxes:** Korean Hangul requires mandatory two-space buffer: `  [한글]  ` with paired Romanization and English, e.g., `  한  / Han [Grief]`.
- **Never use:** Raw `<br>`, raw HTML, LaTeX `$...$`, bare `.md` extensions inside code blocks that auto-link.

---

## PRE-GENERATION CERTIFICATION CHECKLIST

Before you write a single line of canon, certify:

- [ ] I have read `CANON_TIMELINE.md` for the epoch my document belongs to.
- [ ] I have verified the SECC code exists in `SORROW_ENTITIES_CATALOG.md` (if referencing an entity).
- [ ] I have checked `tools/banned_strings.txt` for every noun I plan to use.
- [ ] I know whether my entity is Subject / Object / Place / Time and therefore which work types are valid.
- [ ] I know my document’s in-world author, date (Year 4,2xx), and classification level.
- [ ] I have selected the correct template from `TEMPLATES/` and will fill placeholders in order.

---

## WHERE DEEP KNOWLEDGE LIVES (Source Files)

| Knowledge Domain | Canonical Source File |
|---|---|
| Cosmology & 5 Metaphysical Layers | `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/PROJECT_SOMNARAK.md` |
| Planetary Geology & Terrain | `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_GEOLOGY.md` |
| Reverie Directorate & 8 Floors | `SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_REVERIE_DIRECTORATE.md` |
| SED / UCD / Archive / Caravan | `SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_*.md` |
| Battle Engine & Range Bands | `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md` |
| M.A.W. Architecture | `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md` |
| Ordeals & Tripartite Crisis | `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_ORDEALS_FRAMEWORK.md` |
| Workshops & Acquisition Curve | `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_WORKSHOPS.md` |
| Daily Life & Municipal Law | `SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_DAILY_LIFE.md` |
| Entity Taxonomy & Tales | `SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/*.md` |
| Integrity & PM Comparison | `SOMNARAK-WORLD/Master_Codices/06_Integrity_Audits_and_Comparative_Studies/*.md` |
| Text Box Standards | `TEST_TEXT_BOX_WIDTHS.md` + `REFERENCE_SOMNARAK_WIKI/CHATROOM_TEXT_BOX_STANDARDS.md` |
| Governance & Push Rule | `GOVERNANCE.md` → `RULE-TO-FOLLOW.md` (Rule A0: commit+push same turn) |

---

*This primer is the single source of truth for “what must be known.” If you are about to generate and have not read this, stop and read it now.*
