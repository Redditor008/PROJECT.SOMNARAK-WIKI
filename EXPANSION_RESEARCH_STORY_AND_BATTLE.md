# Expansion Research — Story Arcs & Battle Systems (Tracks 3+4)

> Research date: 2026-09-30. Sources: in-repo `PROJECT_MOON_RESEARCH/` vols 05, 08, 09, 16.
> Method: inventory source models, census current coverage, propose PS-original expansions.
> Standing guardrails: common/real-world words stay; PM-signature terms stay out (47-term battery clean through R14);
> new content uses PS vocab (Grudge/Lament/Void/Weight, Ticks, Composure/SP, Meltdown, Stratum, Glamour, Echo-Cores).

---

## 1. Source models inventoried

| # | Source model | Volume | Our parallel | Status |
|---|---|---|---|---|
| M1 | LoR Ten Floor Realizations (themed boss-rush per floor, 3–5 entities each) | 05 §2C | `ECHO_CORE_REALIZATION_SYSTEM.md` (4-phase engine: Denial/Anger/Bargaining/Catharsis, 6 turns/phase, 10-node grid) | Engine done; content thin (2 scenarios) |
| M2 | Limbus 7 Cantos (`The [epithet]` titles; focus-character + district + climax-anomaly) | 05 §3C, 16 §3 | 5 arcs use day/passage/operation/reading/arc chaptering | No focus-character expedition format |
| M3 | Limbus engine (coins, SP ±45, 7 sins + resonance, 7 status archetypes) | 08 §3 | Dice + SP 0–50 + Light + Ticks; statuses scattered, no codex | Status codex missing |
| M4 | LoR combat (speed dice, clash routing, emotion 0–5, stagger) | 08 §2 | Speed/Spd, clash, Emotion, Stagger/Posture | Mirrored; no work needed |
| M5 | ALEPH gear registry (7 apex gears w/ origin-entity + mechanics; Twilight = fusion-of-3 boss loot) | 09 §2 | `SOMNARAK_MAW_CODEX.md` + 3 boss folios | Folio coverage thin (3 of 13+ apex) |
| M6 | Side-story formats (expedition novella, detective casefiles, episodic lab) | 05 §4 | Single-format arcs | Format variety open (defer) |

---

## 2. Gap analysis (census 2026-09-30)

| Area | Have | Missing |
|---|---|---|
| Story arcs | 5 arcs × 8–11 files (Absolvohan, Katabagil, Katharcheok, Gieok, Jipyeongseondae) | Focus-character expedition arc (M2 format) |
| Realization chapters | Floor 02 Dekan (Containment) + Memory Archive stratum (Archive) | 7+ uncovered leads: Border, Director, Exile, Extraction, Outsider, Research, Secretary |
| Boss folios | 3 (Grieving Colossus C-V, Weeping Mirror, King of Menders) | 12 C-V entities uncovered, incl. The Convergence, Forgotten God, First Tear |
| Status effects | Rupture ×86, Burn ×5, Poise ×3, Bleed ×2, Tremor ×1, Charge ×0 in `GAME_BATTLE/` | Codified status-archetype codex (M3) |
| Scenario↔arc bridges | Katabagil/Katharcheok/Gieok: 1 scenario each | Absolvohan ×0, Jipyeongseondae ×0 |
| Ordeals | 60 files, 12 per color (ASHEN/BLUE/GREY/OBSIDIAN/PURPLE) | Balanced; no work needed |
| SE classes | 292 entities; thinnest N-I (8), O-II (13) | Entity track deferred (not 3/4) |

---

## 3. Proposals

### S1. New Canto-model expedition arc (Track 3, M2)

- **Concept:** focus-lead expedition in 6 chapters + overview, `The [epithet]` chapter titles (common words).
- **Focus candidates:** THE_EXILE (Xyan, field lead) or THE_OUTSIDER (signal/scout lead) — both expedition-natural.
- **Climax candidates (C-V, uncovered):** Forgotten God (C-Vδ-265) or First Tear (C-Vδ-290).
- **File plan:** `SOMNARAK-WORLD/<New_Expedition>/` — `OVERVIEW.md` + 6 chapter files + `README.md` (8 files, matches Katharcheok/Jipyeongseondae scale).
- **De-copy:** no Sinners/Dante/Boughs; expedition party = Specialists/Wardens; chapters titled with plain epithets.

### S2. Realization chapters for uncovered leads (Track 3, M1)

- **Concept:** 4-phase Realization War scenarios per `ECHO_CORE_REALIZATION_SYSTEM.md` (engine already specified).
- **Priority:** Exile + Outsider (pairs with S1 cast); then Border, Extraction, Research, Secretary; Director last (Floor 1 capstone).
- **File plan:** one scenario file each (~28 KB, mirrors `SCENARIO_06_MEMORY_ARCHIVE_STRATUM_REALIZATION.md`).
- **De-copy:** engine terms already PS-native (Sorrow Saturation, Resonant Toll, Sovereign Core); keep them.

### B1. C-V boss folios (Track 4, M5)

- **Concept:** Sovereign Boss Mechanics Folios (~18 KB each, mirrors existing `BOSS_MECHANICS_*`).
- **Priority:** (1) The Convergence (C-Vδ-010, user-mandated fusion; Twilight-model fusion-of-3 mechanics);
  (2) Forgotten God (C-Vδ-265); (3) First Tear (C-Vδ-290).
- **File plan:** `GAME_BATTLE/BOSS_MECHANICS_<NAME>.md` × 3.
- **De-copy:** ALEPH→apex M.A.W. registry; Pale→Void/Weight equivalents; no Apocalypse/Twilight borrowings beyond structural inspiration.

### B2. Status-archetype codex (Track 4, M3)

- **Concept:** single codex defining our battle statuses (potency/count/decay math, interactions with Ticks/SP/Posture).
- **File plan:** `GAME_BATTLE/STATUS_ARCHETYPE_CODEX.md` + retrofit pass tagging existing scattered uses.
- **Open item:** verify Sinking-analog (SP-on-hit) and Charge-analog coverage during drafting (not yet censused).
- **De-copy:** Burn/Bleed/Tremor/Rupture/Poise are common words (keep); Sinking already kept (R7); mechanics re-expressed in PS units.

### B3. Scenario↔arc bridges (Track 4, M4/M6)

- **Concept:** 6-turn scenarios set inside uncovered arcs.
- **SCENARIO_07:** Absolvohan Quiet Season (Days 178–349 bridge — setting already canonized in CHANGELOG).
- **SCENARIO_08:** Jipyeongseondae furnace/Mugeukji expedition defense.
- **File plan:** `GAME_BATTLE/SCENARIO_07_*` + `SCENARIO_08_*` (~16 KB each, mirrors SCENARIO_02–05).

---

## 4. Recommended execution order

1. **B1-Convergence first** — highest-value single file; the user-mandated entity has no folio.
2. **S1 + B1-combo pack** — expedition arc whose climax is staged via the new folio + a B3-style 6-turn scenario (one coherent release: story home + boss + battle).
3. **S2 Exile/Outsider** — Realization chapters for the S1 cast.
4. **B2 codex** — systematizes statuses before further scenario volume.
5. **Remaining B1/S2/B3** — fill in priority order.

---

## 5. Open research items (resolve during drafting, not before)

- Sinking-analog + Charge-analog coverage census (one grep).
- Lead→floor mapping completion (partial: Floor 1 Director/Secretary, Floor 2 Dekan/Containment, Archive/Marjuk; rest open).
- S1 expedition name + setting (new geography must live in `SOMNARAK_GEOLOGY.md`, never as SE — standing rule).
