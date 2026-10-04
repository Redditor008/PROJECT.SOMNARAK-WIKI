# 01 — SORROW ENTITY DOSSIER TEMPLATE

**Template ID:** `T-01-SE-DOSSIER`  
**Generates:** `SOMNARAK-WORLD/Sorrow_Entities/SE-{{SECC}}_ {{English_Name}}_{{Korean_Name}}.md`  
**Authority:** `SOMNARAK-WORLD/Sorrow_Entities/README.md` + `SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/*.md` + Global Primer Laws 1,4,5,7,8,9  
**Canonical Count:** 291 unique SECC dossiers (never invent a new code — select from catalog)

---

## DEEP KNOWLEDGE — READ BEFORE WRITING (Entity-Specific Laws)

- **SECC is immutable:** `SE-[Origin]-[Rank][Potency]-[Number]` e.g., `SE-C-IIIβ-014`, `SE-O-IVδ-515`, `SE-N-IIα-077`. Origin: C City (도한 / Dohan), N Inner (내한 / Naehan), O Outside (외한 / Oehan). Rank I–V Residue→Sovereign. Potency α/β/γ/δ/ω.
- **Manifestation Class determines work types:** Subject may use all 4 works. **Object, Place, Time → ONLY Viderehan + Ferrehan** (Flerehan/Pugnahan = N/A). Enforced by `audit_two_work_rule.py`.
- **Geography is not an entity.** Never file a mountain, ocean, or district as an SE. That belongs in `SOMNARAK_GEOLOGY.md`.
- **Breach fiction must respect chronology:** If your entity is City Sorrow with a pre-Dawn origin tale, its crystallization date must precede Dawn; post-Dawn encounters use Year 4,238 field logs.
- **No PM slips:** Use `Sorrow Entity`, `SECC`, `M.A.W.`, `Han`, never `Abnormality`/`E.G.O`/`Sephirah`.
- **Element must be one of 4:** Grudge (Crimson) / Lament (Blue) / Void (Pale) / Weight (Black).

---

## FILE NAMING CONVENTION

```
SOMNARAK-WORLD/Sorrow_Entities/SE-{{ORIGIN}}-{{RANK}}{{POTENCY}}-{{NUMBER}}_{{English_Name_With_Underscores}}_{{Korean_Name}}.md
```

Example: `SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md`

---

## SCAFFOLD — FILL EVERY PLACEHOLDER IN ORDER

~~~markdown
# {{ENGLISH_NAME}} — {{KOREAN_NAME}}

> *“{{EVOCATIVE_EPIGRAPH_ONE_LINE}}”*

## SECC Classification

| Field | Value |
|---|---|
| **Designation** | `{{ORIGIN}}-{{RANK}}{{POTENCY}}-{{NUMBER}} [{{ELEMENT_ABBR}}]` |
| **Entity Type** | **{{Subject / Object / Place / Time}}** — {{Can breach / Cannot breach / Relic-class}} |
| **Coherence** | {{Rank Written}} ({{I-V}}) — {{Behavior descriptor}} |
| **Potency** | {{Potency Written}} ({{α/β/γ/δ/ω}}) — {{Threat descriptor}} |
| **Sorrow Category** | {{City Sorrow (도한) / Inner Sorrow (내한) / Outside Sorrow (외한)}} |
| **Element** | {{Grudge / Lament / Void / Weight}} ({{Crimson / Blue / Pale White / Black}}) |
| **Manifestation** | {{Subject-Body / Object / Place / Time}} |
| **Physical Form** | {{Organic / Inorganic / Acoustic / Phenomenological — 2 sentences}} |
| **Movement** | {{Mobile / Stationary / Phase-shifting — and breach capability}} |
| **Location** | {{SECTOR-X-##, Zone [A-E] — containment status}} |
| **R.D. Comprehension Level** | {{1–5 — 1 Minimal, 5 Sovereign}} |

## Operational Parameters

| Statistic | Value |
|---|---|
| **Risk tier** | {{α/β/γ/δ/ω}} |
| **Entity role** | {{Subject/Object/Place/Time}} |
| **Primary pressure** | {{Identity / memory / composure / structural pressure}} |
| **Starting Sorrow Gauge** | {{15–30% for α up to 70–85% for ω}} |
| **Han-Energy yield** | {{6–12 for α up to 40–60 for ω}} Han-Energy per successful work cycle |
| **Work difficulty** | {{Minimal / Low / Moderate / High / Catastrophic}} · R.D. Comprehension Level {{1–5}} |
| **Activation threshold** | {{Gauge % or turn count}} |
| **Tool / M.A.W. grade** | {{— · α/β/γ/δ/ω}} |
| **Vessel-Destructible** | {{Yes / No}} |
| **Han Dust Drop** | {{~5kg for α up to ~500kg for ω}} ({{potency}}) |
| **Recommended response** | {{Reduce Gauge through listed valid Work Types; Object/Place uses Viderehan and Ferrehan only.}} |

## Combat Record
### Core Stat Line

| Stat | Value |
|---|---|
| **Speed** | {{1.20 to 3.50 m/s by rank}} |
| **Resistance** | {{30% against primary element; 20% other}} |
| **Activation threshold** | Sorrow Gauge ≥ {{60% typical}} |
| **Sorrow Gauge [HP]** | {{300–1200 by rank}}/{{max}} |
| **Han Pressure [ATK]** | {{6–12 for α up to 24–48 for ω}} per hit · {{Element}} |

| Field | Value |
|---|---|
| **Battle Length** | {{Short 8 / Medium 16 / Long 24 turns}} |
| **Threat Role** | {{Standard / Elite / Sovereign encounter}} |
| **Valid Work Types** | {{List — remember Object/Place = Viderehan, Ferrehan only}} |
| **Battlefield** | {{Sector, Zone — containment detail}} |
| **Resolution Condition** | {{Specific suppression condition — not “kill it”}} |

### Combat Actions

| Name / Category | Flavor Text | Combat Move | Combat Effect | Trigger |
|---|---|---|---|---|
| { *{{Action 1}}* [**{{Debuff/Attack/Ultimate}}**] } | "{{Flavor}}" | [{{Move}}] | {{Effect}} | {{Trigger}} |
| { *{{Action 2}}* [**Attack**] } | "{{Flavor}}" | [{{Move}}] | {{Effect}} | {{Trigger}} |
| { *{{Action 3}}* [**Ultimate**] } | "{{Flavor}}" | [{{Move}}] | {{Effect}} | Gauge ≥ 80% |

### Consequences
- {{Composure/identity degradation on failed resistance.}}
- {{Extended contact risks full manifestation — erosion, trauma, dissolution, corruption.}}
- {{Every M.A.W. activation extracts price — memory, sensation, years.}}
- {{Without resolution, documented breach/activation behavior triggers.}}

## Appearance
**Primary Form:** {{2–3 sentences, physical + elemental signature.}}

**Notable Features:**
- {{Feature 1}}
- {{Feature 2}}
- {{Feature 3}}

**Identification Profile**
- **Entity Type:** {{Subject/Object/Place/Time}}
- **Manifestation:** {{Subject-Body / Object / Place / Time}}
- **Primary marker:** {{One-line visual identifier}}
- **Element signature:** {{Grudge/Lament/Void/Weight}}

## Origin
- **Formation:** {{What collective grief crystallized it}}
- **The Sorrow:** {{The human wound — 2 sentences.}}
- **The Event:** {{The specific incident that tipped Han into entity}}
- **The People:** {{Who suffered}}

## Behavior

| Work Type | Response | Gauge Change |
|---|---|---|
| **Flerehan** (Tears) | {{Becomes agitated / settles / N/A for Object/Place}} | {{Stable / Decrease / Increase / N/A}} |
| **Pugnahan** (Confrontation) | {{Cowers / Enrages / N/A}} | {{...}} |
| **Viderehan** (Observation) | {{Remains calm / permits study}} | {{Decrease typical for Object/Place}} |
| **Ferrehan** (Endurance) | {{Recognizes patience / settles}} | {{Decrease}} |

## Breach Behavior

| Field | Detail |
|---|---|
| **Breach Type** | {{Escape / Lure / Expansion / Acoustic Leak}} |
| **Movement** | {{How it breaks and pursuit range}} |
| **Signal** | {{First sign — fog, chime, silence, weight}} |
| **Response Protocol** | {{Directorate counter-protocol}} |

## 관찰 기록 (Observation Log)

**R.D. Comprehension Level:** {{1–5}}

**Key Observations:**
- {{Observation 1}}
- {{Observation 2}}

**Personnel Note:**
> *“{{First-person testimony — Citizen, Zone, Year}}”*

## 이야기 보고 (Story Log) — Observation Entries

**Entry 1 — Containment Description**
{{SECC + manifestation + element + one-line origin.}}

**Entry 2 — <Excerpt from Field Log, Year {{4,2xx}} >**
{{White fog / chime / silence — personnel compelled behavior}}

**Entry 3 — <Excerpt from Counseling Log>**
{{The sorrow — denial, exhaustion, debt.}}

**Entry 4 — <Containment Notice>**
{{Management: specific Echo amount, fog dissipates, Tide increase note.}}

**Entry 5 — <Archive Note>**
{{Cross-reference with registered location — structural sorrow, not singular.}}

## 최종 관찰 (Final Observation)

| Endure it — bear the weight without flinching. | Struggle free — try to throw it off. |
|---|---|
| {{Predicted response — sorrow seen clearly; fully recorded.}} | {{Resists wrong approach; gauge climbs.}} |
| **OBSERVATION SUCCESS** | **OBSERVATION FAIL** |
~~~

---

## VALIDATION CHECKLIST (Must PASS before commit)

- [ ] SECC code exists in `REFERENCE_SOMNARAK_WIKI/SORROW_ENTITIES_CATALOG.md` (not invented).
- [ ] Object/Place/Time uses ONLY Viderehan + Ferrehan (check `audit_two_work_rule.py`).
- [ ] No banned strings (`Abnormality`, `E.G.O`, `GPS`, `Hz` with numbers, etc.).
- [ ] Four work responses present; gauge changes are `Decrease`/`Stable`/`Increase`/`N/A` consistent with rank.
- [ ] Consequences section has 4 bullet consequences.
- [ ] All 5 Story Log entries present and unlock progressively.
- [ ] Final Observation has 2-column choice with SUCCESS/FAIL labels.
- [ ] File name matches `SE-{{CODE}}_{{English}}_{{Korean}}.md` exactly.
