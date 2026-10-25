# SE Category Templates — choose by structure, then write

**Created:** 2026-10-25 as the extended overhaul of the single old scaffold `TEMPLATES/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md` (T-01), at the owner's request. The category explanation these templates implement is one folder up: [../README.md](../README.md).

## Which template do I use? (decide in this order)

1. **Is there a mind in it** — something that can notice conduct, choose, refuse, or answer?
   - Yes → [01_SUBJECT_SE_TEMPLATE.md](01_SUBJECT_SE_TEMPLATE.md) (142 dossiers).
   - No → continue.
2. **Is it kept and used as an operational tool** by the facility, with authorised operative sessions?
   - No — it is simply an object, place, time, or hazard that is contained and worked around → [02_NON_SUBJECT_SE_TEMPLATE.md](02_NON_SUBJECT_SE_TEMPLATE.md) (71 dossiers).
   - Yes → it is a relic. Continue.
3. **How is it used?**
   - Worn, held, or mounted; works only while attached; manually unequipped → [03_I_RELIC_SE_TEMPLATE.md](03_I_RELIC_SE_TEMPLATE.md) — Indumentum (53 dossiers).
   - Held open by sustained touch, gaze, or invocation; formally closed → [04_O_RELIC_SE_TEMPLATE.md](04_O_RELIC_SE_TEMPLATE.md) — Offertorium (28 dossiers).
   - Triggered once and consumed → [05_A_RELIC_SE_TEMPLATE.md](05_A_RELIC_SE_TEMPLATE.md) — Arcanum (7 dossiers).

If you are repairing an existing dossier, do not re-decide: run the ten-second test in [../README.md](../README.md), take the template it names, and keep the dossier in its own category.

## What all five templates share (the modern spine)

Title + epigraph → SECC Classification → Operational Parameters + Operational Notes → Combat Record (Core Stat Line, Operational Record, five Combat Actions, Battle Phases, Consequences) → Appearance (Identification, Detailed Appearance Profile, protocol) → Origin → Behavior + Operational Work Notes + Reading the response → failure section (category-specific) → M.A.W. Equipment (Weapon, Suit, Stigma, Use Notes, piece-specific Field Use Record, Stat interpretation) → Observation Log + Progression → Story Log (5 entries) → Final Observation → Flavor Text quartet → Interaction Pattern + Record → Tale → Testimonium (5 voices) → Registrum + Registry Addendum → Warden/Watch Record → Trivia + Registry Trivia → Document Information.

## What is actually different (the whole point of five files)

| Difference | Subject | Non-Subject | I-Relic | O-Relic | A-Relic |
|---|---|---|---|---|---|
| Valid Work Types | all four | Viderehan + Ferrehan | Viderehan + Ferrehan | Viderehan + Ferrehan | Viderehan + Ferrehan |
| Object/Place Work Rule banner | never | yes | yes | yes | yes |
| Failure section | `## Breach Behavior` (it acts, chooses a First Target) | `## Breach Behavior` read as in-place change of state/reach, + Detailed Activation Record | `## Activation Behavior` + relic triad | `## Activation Behavior` + relic triad | `## Activation Behavior` + relic triad |
| Tool Use Profile / Log and Method | forbidden | forbidden | required (equippable) | required (channeled) | required (single-use) |
| Termination story | Resolution Condition performed | recorded condition ends the rise | manual unequip | formal channel closure | consumption — no return |
| First Target | a recorded choice | a selecting condition | threshold/cascade scope | threshold/cascade scope | threshold/cascade scope |
| Movement language | its own locomotion | reach, spread, recurrence | carried/kept; in-chamber only | kept; in-chamber only | kept; in-chamber only |

## What this overhaul changes versus the old T-01 template

- **One scaffold became five.** T-01 had a single `{{Subject / Object / Place / Time}}` fork and no relic structure at all; the relic triad (Tool Use Profile, Log and Method, Detailed Activation Record) existed in 88 dossiers with no template. It has one now, three times — once per use mode.
- **Sections real dossiers have, T-01 lacked, now scaffolded:** Operational Notes, Battle Phases, Detailed Appearance Profile + Appearance protocol, Expanded origin context, Operational Work Notes + Reading the response, the full six-field failure table + Escalation Notes, the complete M.A.W. Equipment set (Weapon/Suit/Stigma/Use Notes/Field Use Record/Stat interpretation), Observation Progression + method, Flavor Text quartet, Interaction Pattern + Record, Tale/Testimonium/Registrum/Registry Addendum, Warden/Watch Record, Trivia + Registry Trivia, Document Information.
- **Combat Actions corrected from 3 rows to the measured 5** (Debuff, Debuff, Attack, Attack, Ultimate) with the archive's effect format.
- **Stale facts retired:** the closed catalog is 301 dossiers (T-01 said 291); R.D. levels are named Trace / Basic / Advanced / Deep / Sovereign; the Han dust row is `Han Dust Drop (Vessel Destruction)`; the old breach `Signal / Response Protocol` rows are replaced by the fields dossiers actually carry; and T-01's cited `audit_two_work_rule.py` no longer exists — the two-work rule is now verified by the template checklists and the standard five tools, which the checklists name with their expected outputs.
- **Hard-won writing rules are now in the scaffold itself:** prohibitions repeated in four places; piece-specific (never blended) equipment tolls; named Stigma stats; pattern/falloff written or honestly sourced; thresholds scoped; Tale-vs-body pictures reconciled or separated; flavor text written for the real room or ground, never a generic cell.

## Conventions inside every template

- Copy only the fenced SCAFFOLD. `{{DOUBLE_BRACE}}` marks a placeholder; instructional placeholders are prompts to replace, and a finished dossier contains zero of them.
- Keep the Korean section headings exactly as scaffolded — the tools and the archive key on them.
- Brackets and braces inside Combat Actions (`[move]`, `{ *Name* [**Attack**] }`) are literal archive style, not placeholders.
- Ship one dossier per validated push through `tools/gate.sh`, after the template's checklist, ending in PUSH VERIFIED.
