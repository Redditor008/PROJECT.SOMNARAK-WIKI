# 01 — SORROW ENTITY DOSSIER TEMPLATE

**Template ID:** `T-01-SE-DOSSIER`
**Generates:** `SOMNARAK-WORLD/Sorrow_Entities/SE-{{SECC}}_{{English_Name}}_{{Korean_Name}}.md`
**Authority:** `SOMNARAK-WORLD/Sorrow_Entities/README.md` + `SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/*.md` + `REFERENCE_SOMNARAK_WIKI/RULES/R-23`, `R-24`, `R-28`, `R-36` + Global Primer Laws 1,4,5,7,8,9
**Canonical Count:** 301 dossiers on file — never invent a new code, select from the catalog

---

## DEEP KNOWLEDGE — READ BEFORE WRITING (Entity-Specific Laws)

- **SECC is immutable:** `SE-[Origin]-[Rank][Potency]-[Number]` e.g., `SE-C-IIIβ-014`, `SE-O-IVδ-515`, `SE-N-IIα-077`. Origin: C City (도한 / Dohan), N Inner (내한 / Naehan), O Outside (외한 / Oehan). Rank I–V Residue→Sovereign. Potency α/β/γ/δ/ω.
- **Manifestation Class decides whether there is a work table at all** (`R-40`): a **Subject** gets `## Behavior` with the four Work Types; an **Object, Place, Time, Hazard, Possession or Relic gets no Work Types at all** and carries `## Handling Process` instead — what is done, in what order, by whom, what it costs, and what is never done. Enforced by `tools/auditors/check_relic_work_types.py`.
- **Geography is not an entity.** Never file a mountain, ocean, or district as an SE. That belongs in `SOMNARAK_GEOLOGY.md`.
- **Breach fiction must respect chronology:** If your entity is City Sorrow with a pre-Dawn origin tale, its crystallization date must precede Dawn; post-Dawn encounters use Year 4,238 field logs.
- **No PM slips:** Use `Sorrow Entity`, `SECC`, `M.A.W.`, `Han`, never `Abnormality`/`E.G.O`/`Sephirah`.
- **Element must be one of 4:** Grudge (Crimson) / Lament (Blue) / Void (Pale) / Weight (Black).
- **The classification cell is a claim and the record is the answer.** `**Entity Type**` and the file's own event section say the same thing in the same words' worth of meaning. A cell that states no breach claim at all is a defect twice over: the census cannot see it and neither can a reader.
- **A holding that does not leave containment has no breach section.** It has the section its category earns (see the table below), with that section's field names, and no `| **Breach Type** |` row anywhere.
- **Work Type rows are written per holding, never as a pair.** The retired stock pair — *Permits study; the <x> pressure becomes legible under sustained observation* / *Recognizes patience; the <x> pressure settles gradually under sustained presence* — is a defect. Each row says what this holding actually lets a person do.
- **A cost is what the piece takes, not what it feels like.** No M.A.W. piece may charge a sentence used by another piece, in this file or any other.
- **The file does not keep notes about its own editing.** No *corrected from the earlier entry*, no review dates, no *After contact, the body holds what the mind files away*, no *β across the set and correctly rated against entities*. Each of those is a note about the file; the file is supposed to be about the holding.
- **Where a holding cannot fight, it has no combat record; where it cannot flee, it has no escape.** R-36 decides which, and the file's argument is written above the stat block, not inferred by the reader.

---

## THE CATEGORY DECIDES THE SECTION (R-28)

| What the record actually shows | Section heading | Field names inside it |
|---|---|---|
| It leaves containment and roams | `## Breach Behavior` | `**Breach Type**` · `**Movement**` · `**Effect**` · `**Secondary Effect**` · `**First Target**` · `**Escalation**` |
| It extends, roots, thickens or widens in place | `## Expansion Behavior` | `**Expansion Trigger**` · `**Expansion Rate**` · `**Expansion Effect**` · `**Containment**` |
| It is used, worn or spent rather than contained against | `## Activation Behavior` | Tool Use Profile: `**Tool Class**` · `**Use Mode**` · `**Activation**` · `**Primary Effect**` · `**Duration**` · `**Termination / Return**` |
| It warps its own zone and nothing walks out | `## Containment Event Behavior` | `**Event Type**` · `**Movement**` · `**Effect**` · `**Secondary Effect**` · `**First Target**` |
| It forms where the parts already are and ceases when they part | `## Containment Event Behavior` or `## Formation Behavior` | `**Event Type**` · the same five rows |
| It appears where it appears and does not travel | `## Manifestation Behavior` | `**Event Type**` · `**Movement**` · `**Effect**` · `**First Target**` |

Two consequences that are checked by `tools/section_logic.py`:

1. A dossier whose `**Entity Type**` says *non-breaching* may not head `## Breach Behavior` and may not carry `| **Breach Type** |`.
2. A dossier whose event section names a category must state that category in `**Entity Type**` — *Can breach via Expansion*, or *Non-breaching: expansion only; {{the file's own evidence}}*.

The gauge label follows the section: `**Sorrow Gauge on breach:**` · `**Sorrow Gauge on expansion:**` · `**Sorrow Gauge on formation:**` · `**Sorrow Gauge in the event:**` · `**Sorrow Gauge on activation:**`. It is never `on breach` on a file that has no breach, and it is never the placeholder `Starts at 40%, rises 10%/turn` — that sentence is retired archive-wide.

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
| **Entity Type** | **{{Subject / Object / Place / Time / Hazard}}** — {{Can breach via {{Escape / Transform / Corrupt / Expansion}} / Non-breaching: {{Activation / Corruption / Possession / Expansion / Manifestation}} only; {{the evidence this file itself gives}}}} |
| **Coherence** | {{Rank Written}} ({{I-V}}) — {{Behaviour descriptor}} |
| **Potency** | {{Potency Written}} ({{α/β/γ/δ/ω}}) — {{Threat descriptor}} |
| **Sorrow Category** | {{City Sorrow (도한) / Inner Sorrow (내한) / Outside Sorrow (외한)}} |
| **Element** | {{Grudge / Lament / Void / Weight}} ({{Crimson / Blue / Pale White / Black}}) |
| **Manifestation** | {{Subject-Body / Object / Place / Time}} |
| **Physical Form** | {{Organic / Inorganic / Acoustic / Phenomenological — 2 sentences}} |
| **Movement** | {{Mobile / Stationary / Recumbent / Rooted — and, if it has never moved or never pursued, say so here in this file's own words}} |
| **Location** | {{SECTOR-X-##, Zone [A-E] — containment status}} |
| **R.D. Comprehension Level** | {{1–5 — 1 Minimal, 5 Sovereign}} |

## Operational Parameters

| Statistic | Value |
|---|---|
| **Risk tier** | {{α/β/γ/δ/ω}} |
| **Entity role** | {{Subject/Object/Place/Time}} |
| **Primary pressure** | {{Identity / memory / composure / structural pressure}} |
| **Starting Sorrow Gauge** | {{15–30% for α up to 70–85% for ω}} |
| **Han-Energy yield** | {{6–12 for α up to 40–60 for ω}} Han-Energy {{Subject: per successful work cycle · Relic: per completed handling, named against the stage that produced it}} |
| **Work difficulty** | {{Minimal / Low / Moderate / High / Catastrophic}} · R.D. Comprehension Level {{1–5}} |
| **Work Damage** | {{The verdict is one of three (`R-49`). **Damage** — a band inside the grade, the holding's own `Element`, and one clause naming the mechanism: `3–6 Grudge — the cost is …`. **Neutral** — `None — {what it does with the cost instead}; it is the room that pays it, not the worker.` **Gift** — `None` here, plus the `**Work Gift**` row below}} |
| **Work Gift** | {{Gift verdict only, and delete the row otherwise: `+5–10 {Composure or Resilience} for the rest of the cycle — {the price, in the holding's own element}`. A loan, not a line on the worker's sheet — `R-49` §5}} |
| **SE Effect** | {{Only on the 45 % that have one (`R-50`), and delete the row otherwise: `**On {the breach | the counter | the wall | the contact | the completion | the refusal}** — {the law, in this holding's own words}.` The occasion comes from this file's own `**Activation threshold**` and `**Entity Type**`; the law is what this one does that no other one does}} |
| **Activation threshold** | {{Gauge % or turn count — or `no counter` / `no gauge` / both, per Special Activation}} |
| **Tool / M.A.W. grade** | {{— · α/β/γ/δ/ω}} |
| **Vessel-Destructible** | {{Yes / No}} |
| **Han Dust Drop** | {{~5kg for α up to ~500kg for ω}} ({{potency}}) |
| **Recommended response** | {{Subject: the one Work Type that settles it, named. Relic: the first stage of the handling procedure below, named — a relic is not worked and has no Work Type to recommend}} |

## {{Combat Record / Contact Record}}

{{R-36 decides the heading and the note under it. One of the two lines below is mandatory, and both say why in the file's own terms — never as a label.}}

> **Why this file has no combat actions.** {{What the file says instead: that the body has never moved, that nothing here pursues or aims, that the damage is the room's rather than a blow's — and what a watch survives in its place.}}

> **Why this file keeps combat actions.** {{The one thing in this file that can be met, struck, held or withstood, and why dropping the rows would leave a warden without an account of it.}}

### Core Stat Line

| Stat | Value |
|---|---|
| **Speed** | {{1.45 / 1.95 / 2.45 m/s by rank; `0 m/s` and the reason if fixed}} |
| **Resistance** | {{30% against primary element; 20% other}} |
| **Activation threshold** | Sorrow Gauge ≥ {{60% typical}} |
| **Sorrow Gauge [HP]** | {{150–12,000 by grade}}/{{max}} — **subjects, possessions and breaching relics only.** A non-breaching relic files a charge instead: `**000 of {{wall}}** · ready · six doses · limit {{60 / 90 / 120 / 180 by how it is met}} s · recharge 10 min`, named for its Element, with a `## The Charge` section under the table (`R-48`) |
| **Han Pressure [ATK]** | {{6–12 for α up to 50–80 for ω}} per hit · {{Element}} |

| Field | Value |
|---|---|
| **Battle Length** | {{Short 8 / Medium 16 / Long 24 turns}} |
| **Threat Role** | {{Standard / Elite / Sovereign encounter}} |
| **Valid Work Types** | {{Subject only: the four-row table in `## Behavior` says which answer this holding. **A relic has none** — the row reads `**Handling**` and points at `## Handling Process`}} |
| **Battlefield** | {{Sector, Zone — containment detail}} |
| **Resolution Condition** | {{The specific thing that ends it — never “kill it”, and for a Contact Record the one act that closes the watch}} |

### Combat Actions / Contact Events

| Name / Category | Flavor Text | Combat Move | Combat Effect | Trigger |
|---|---|---|---|---|
| { *{{Action 1}}* [**{{Debuff/Attack/Ultimate}}**] } | "{{Flavor}}" | [{{Move}}] | {{Effect}} | {{Trigger}} |

### Consequences

- {{Composure/identity degradation on failed resistance.}}
- {{What the file records after the event rather than during it.}}
- {{Every M.A.W. activation takes something from the wielder — named, and specific to the piece.}}
- {{Without resolution, the file's own documented event behaviour.}}

## Appearance

**Primary Form:** {{2–3 sentences, physical + elemental signature.}}

### Detailed Appearance Profile

- **Silhouette / scale:** {{…}}
- **Surface and colour:** {{…}}
- **Distinguishing feature:** {{the one thing a witness would describe}}
- **Position / movement:** {{the same claim as the `**Movement**` row in the classification table — if the body has never moved, this bullet says so too}}

## Origin

- **Formation:** {{What collective grief crystallized it}}
- **The Sorrow:** {{The human wound — 2 sentences.}}
- **The Event:** {{The specific incident that tipped Han into entity}}
- **The People:** {{Who suffered}}

## Behavior

*Subject only. A relic carries `## Handling Process` in this slot instead — see `R-40`.*

| Work Type | Response | Gauge Change |
|---|---|---|
| **Flerehan** (Tears) | {{What it does when the worker weeps alongside it}} | {{Down / Neutral / Up · High / Common / Low}} |
| **Pugnahan** (Confrontation) | {{What it does when it is faced and forced}} | {{…}} |
| **Viderehan** (Observation) | {{What this holding actually lets an observer get — the specific reading only this file gives, in this holding's own terms}} | {{…}} |
| **Ferrehan** (Endurance) | {{What a party actually does for a full cycle here, and what the endurance is spent on. If it would read “wait”, check the `**Movement**` and `**Effect**` rows first: standing still may be precisely what this holding works on.}} | {{…}} |

**Two judgements per cell, not one.** `state · preference` — the **state** is what the holding does to the gauge (`Down` / `Up` / `Neutral`, or the two barred words **Net-Neutral** and **Negative-Low**), the **preference** is what the work gives back (`High` / `Common` / `Low`, with `V.H` and `V.L` legal at the ends), on the five-grade ladder L Corp uses. They are allowed to disagree: `Neutral · High` is a good reading that settles nothing, `Up · Low` is a work that is bad for the worker *and* pays little. **At most one `High` per dossier.** A barred cell is **Net-Neutral** or **Negative-Low**, carries no preference, and never prints a percentage — the percentage was the batch-156 form and it reads badly on a dossier page (`R-41`). Which of the two it is comes from the **Threat Score** (Coherence rank + Potency rank, 2–10; under 6 Net-Neutral, 6 or more Negative-Low). See `REFERENCE_SOMNARAK_WIKI/GUIDES/WORK_PREFERENCE_VARIETY.md`.

**The four signs follow the `**Element**` row**, not the file next door — Strong = Decrease, Partial = Stable, Weak = Increase, per the Work Type Effectiveness matrix in `PROJECT_SOMNARAK.md` and `REFERENCE_SOMNARAK_WIKI/GUIDES/WORK_RESPONSE_LAW.md`. Every holding has exactly one work type that settles it, one that worsens it, and two that hold it. Checked by `tools/auditors/check_work_response.py`.

## Handling Process

*Relic only — Object, Place, Time, Hazard, Possession. A subject carries `## Behavior` in this slot instead.*

> **This holding is not worked.** {{One line: what it is instead — a thing approached, a ground walked, a tool carried — in this file's own terms.}}

| Stage | What is done | Who holds it | What it costs |
|---|---|---|---|
| **Approach** | {{the posting, the distance, the covering, the instrument carried in}} | {{post, rank, number of people}} | {{what the approach spends}} |
| **Handling** | {{the act itself: what is touched, read, moved, said, or refused}} | {{who may do it, and the condition on them}} | {{the cost of doing it}} |
| **Withdrawal** | {{how it ends: the order of leaving, what is sealed, what is written down}} | {{who confirms it}} | {{what is carried out and what is left}} |
| **Refusal** | {{the thing never done here, and the incident that set the prohibition}} | {{who may authorise the exception — usually nobody}} | {{what happened the last time it was tried}} |

### Operational Work Notes

{{Read the four rows together and say what they add up to for this holding. One sentence of the archive's own argument, not a restatement of the table.}}

## {{Breach Behavior / Expansion Behavior / Activation Behavior / Containment Event Behavior / Manifestation Behavior}}

> *“{{Warden or Directorate call, in the voice of the announcement — this entry is not a summary of the section}}”*

| Field | Detail |
|---|---|
| {{the field names the category table above prescribes, filled from this file's record}} | {{…}} |
| **Escalation** | {{the per-turn figure this file actually uses, and what it is counted against}} |

### Escalation Notes

- **{{Event type / Breach type / Activation type}}:** {{…}}
- **Containment priority:** {{what the wing actually does, and what has already been tried and failed}}
- **Sorrow Gauge {{on breach / on expansion / on formation / in the event / on activation}}:** {{the figure this file uses, derived from its own escalation row — never the retired placeholder}}

### Detailed Activation Record

{{Only where the file records use rather than containment.}}

## M.A.W. Equipment

> **Materialized Agony Wear (M.A.W.):** the entity's archetype drawn into equipment form and split into three M.A.W. pieces — Weapon, Suit, and Stigma.

> **Two labels, one price each.** `**Cost:**` is what the piece costs in Sorrow Echoes — a figure, on the stats line. `**Bearer cost:**` is what it takes from the person carrying it, and it sits under the Ability it is derived from. A block with two `**Cost:**` rows makes the reader guess which is which, and a block with no `**Bearer cost:**` has not said what the piece costs its bearer at all.

### M.A.W. Weapon — {{Name}}

**Type:** Weapon | **Grade:** {{α–ω}} | **Element:** {{…}}

**Appearance:** {{source-led, 2 sentences}}

**Damage:** {{Element}} {{low–high}} **Speed:** {{1–6}} ({{…}}) **Range:** {{1–5}} ({{…}}) **Max Amount:** {{n}} **Cost:** {{Sorrow Echoes}}

**Attack Pattern:** {{Single / Line / Arc / Skewer}}
**Target Coverage:** {{n targets}}
**Falloff Rule:** {{…}}
**Damage Application:** {{…}}

**Ability:** {{What this piece does that no other piece does, from the entity's own nature.}}
**Bearer cost:** {{What it takes from the wielder, derived from the Ability in the line above. Never a sentence another piece uses; never “with each use” filler.}}

{{Optional: custody note, one paragraph, in-world.}}

### M.A.W. Suit — {{Name}}

{{same fields as the Weapon; Suit abilities are protective and their costs are what protection costs}}

### M.A.W. Stigma — {{Name}}

**Category:** Stigma ({{…}}) | **Grade:** {{…}} | **Element:** {{…}}

**Appearance:** {{small, wearable, resonant}}

**Slot:** {{Head / Face / Chest / Hand / Tail / Feet}}
**Acquisition Probability:** {{2–5%}}
**Effect:** {{the passive figure and what it is measured against here}}
**Ability:** {{the specific boon — what it lets the bearer do}}
**Bearer cost:** {{what it takes, derived from the Ability. The four retired stock families — *moves a little slower*, *temper shortens*, *weeps in their sleep*, *forgets a word* — are defects in any file.}}

{{Optional: charm custody / responsibility note, in-world.}}

### M.A.W. Use Notes

{{How the three pieces are issued, carried, returned and reviewed.}}

### Field Use Record

| Stage | Required record |
|---|---|
| **During use** | {{…}} |
| **After use** | {{…}} |

## 관찰 기록 (Observation Log)

**R.D. Comprehension Level:** {{1–5}}

**Key Observations:**
- {{Observation 1}}
- {{Observation 2}}

### Observation Progression

| Cycle | What changed |
|---|---|
| {{…}} | {{…}} |

## 이야기 보고 (Story Log) — Observation Entries

**Entry 1 — Containment Description**
{{SECC + manifestation + element + one-line origin.}}

**Entry 2 — <Excerpt from Field Log, Year {{4,2xx}}>**
{{What the watch actually saw.}}

**Entry 3 — <Excerpt from Counseling Log>**
{{The sorrow, in the words of somebody carrying it.}}

**Entry 4 — <Containment Notice>**
{{Management: the specific figure, the standing instruction.}}

**Entry 5 — <Archive Note>**
{{What the file has concluded, and what it has stopped asking.}}

## 최종 관찰 (Final Observation)

| Endure it — bear the weight without flinching. | Struggle free — try to throw it off. |
|---|---|
| {{Predicted response — sorrow seen clearly; fully recorded.}} | {{Resists wrong approach; gauge climbs.}} |
| **OBSERVATION SUCCESS** | **OBSERVATION FAIL** |

## 감각 묘사 (Flavor Text)

{{What the room is like. Sensory, present tense, no mechanics.}}

### Interaction Pattern

{{What happens when a person and this holding are in the same place.}}

### Entity Interaction Record

{{Pairings with other holdings, each stating whether anything changed.}}

## 이야기 (Narratio) — The Tale

> *“{{The tale as it was told.}}”*

## 증언 (Testimonium) — The Testimony

> *“{{A witness, named by role, in their own words.}}”*

## 기록 (Registrum) — The Record

{{The institutional record: what was filed, what was not, and the minuted objection.}}

**The objection, in the minute's own words:** {{one sentence — this file's own register, its own body raising it, its own finding. Never the same sentence as another dossier.}}

### Registry Addendum

{{What a later reader would find appended, in-world.}}

## Apex Record

{{Where this is a Rank IV–V record: the series, the limit, the standing arrangement.}}

## Trivia

### Registry Trivia

{{What the registry keeps that nobody asked it to keep.}}

## Document Information

| Field | Value |
|---|---|
| **Document ID** | `{{CODE}}` |
| **Date** | Year {{4,2xx}} |
| **Classification** | {{Restricted / Classified}} |
| **Reviewed by** | {{…}} |
~~~

---

## VALIDATION CHECKLIST (Must PASS before commit)

- [ ] SECC code exists in `REFERENCE_SOMNARAK_WIKI/REGISTRY/SORROW_ENTITIES_CATALOG.md` (not invented).
- [ ] A Subject carries the four-row `## Behavior` table; **a relic carries `## Handling Process` and no Work Type table at all** (check `tools/auditors/check_relic_work_types.py`).
- [ ] No banned strings (`Abnormality`, `E.G.O`, `GPS`, `Hz` with numbers, etc.).
- [ ] `**Entity Type**` states a breach claim or a non-breaching category, and it equals the file's own event section (`tools/section_logic.py`).
- [ ] The event section heading matches the category table above — no `## Breach Behavior` on a non-breaching file, no `**Breach Type**` row anywhere on one.
- [ ] The four work signs follow the `**Element**` row — one Decrease, one Increase, two Stable for a Subject — and the Handling Process stages name a cost and a refusal for a relic.
- [ ] The gauge label matches the event section and the figure comes from this file's own escalation row.
- [ ] `**Movement**` row and the `- **Position / movement:**` bullet are the same claim.
- [ ] Combat Record or Contact Record, with its `Why this file …` line, and the note is a reason rather than a label.
- [ ] Every M.A.W. `**Cost:**` is derived from the `**Ability:**` above it and appears in no other dossier.
- [ ] No filing notes: no *corrected from*, no review dates, no *After contact, the body holds what the mind files away*, no *β across the set and correctly rated against entities*.
- [ ] Consequences section has 4 bullet consequences.
- [ ] All 5 Story Log entries present and unlock progressively.
- [ ] Final Observation has 2-column choice with SUCCESS/FAIL labels.
- [ ] File name matches `SE-{{CODE}}_{{English}}_{{Korean}}.md` exactly.
