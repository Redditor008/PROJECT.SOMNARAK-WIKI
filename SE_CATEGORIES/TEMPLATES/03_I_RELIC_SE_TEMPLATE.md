# I-RELIC SE TEMPLATE — INDUMENTUM (EQUIPPABLE)

**Template ID:** `T-SECAT-03` · **Version:** 2026 overhaul (2026-10-25) — supersedes the corresponding use of `TEMPLATES/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md` (T-01) for this category. T-01 remains in place as the historical single scaffold; this file is the extended, category-correct one.
**Category guide (read first):** [03_I_RELIC_SE_INDUMENTUM.md](../03_I_RELIC_SE_INDUMENTUM.md)
**Worked example to study, not to copy:** The Debt Scale `C-IIIβ-015`
**Generates:** `SOMNARAK-WORLD/Sorrow_Entities/SE-{{ORIGIN}}-{{COHERENCE}}{{POTENCY}}-{{NUMBER}}_{{English_Name_With_Underscores}}_{{Korean_Name}}.md`

## HOW TO USE THIS TEMPLATE

1. Confirm the category **before** writing, using the ten-second test in [../README.md](../README.md#how-to-tell-which-category-a-dossier-is-ten-seconds). If the test sends you to a different template, stop and switch — structure is decided first, prose second.
2. Copy **only the SCAFFOLD** below into the new dossier file. Everything outside the scaffold fence is instruction and stays behind.
3. Replace every `{{PLACEHOLDER}}`. Placeholders written as instructions ("write the X that…") are prompts, not text: the finished dossier contains **zero** `{{` sequences (the checklist greps for them).
4. The 301-dossier corpus is a closed catalog. A designation is selected from `REFERENCE_SOMNARAK_WIKI/SORROW_ENTITIES_CATALOG.md` on owner instruction, never invented; absent that instruction, use this template to rewrite or repair an existing dossier **in its own category**, preserving its numbers.
5. Write every cell from the entity's own facts. Numbers are tuned across the file as one system (starting gauge, thresholds, HP, pressure, echo costs, counts in the Tale and Registrum must agree), never pasted from the example dossier.
6. Run the VALIDATION CHECKLIST at the end of this file, then ship with `tools/gate.sh` as its own single-unit push.

## CATEGORY LAWS — READ BEFORE WRITING

- **The original never leaves containment.** A "relic session" is an authorised in-chamber operative interaction. M.A.W. pieces are archetype derivations — different objects with their own appearances and costs — never the relic carried into the field.
- **Work is Viderehan + Ferrehan only; Flerehan and Pugnahan are prohibited**, and the `Object/Place Work Rule` banner is printed at the head of `## Behavior`, verbatim as in this scaffold. The Tool Use Profile's Operational Rule repeats that a session cannot replace a scheduled cycle.
- **Failure is activation, not breach.** The failure section is `## Activation Behavior`; escalation is a threshold/cascade story told in measurements.
- **The toll is unavoidable and specific.** Every profile prices residue in the operator (memory, aging, detachment, weight) in this instrument's own terms — never "use with caution".
- **The triad is the classification.** Tool Use Profile + Log and Method + Detailed Activation Record, in that neighbourhood and order, with Escalation Notes between Log and Method and the Detailed Activation Record (the measured order in modern dossiers). If the role row or grade row disagrees with the heading, fix the rows — the heading governs.
- **Attachment is the whole mechanism.** Nothing happens at a distance, nothing continues after correct detachment — and nothing switches itself off. If the effect needs sustained attention rather than attachment, it is an O-Relic; if once is all it gets, an A-Relic.

Shared laws (all five templates): SECC designation is `Origin–Coherence+Potency–Number` (C City 도한 / N Inner 내한 / O Outside 외한; I–V; α/β/γ/δ/ω) and is immutable once filed. Element is exactly one of Grudge / Lament / Void / Weight unless a canon source itself records otherwise. Geography is not an entity. In-world dates use the Year 4,2xx frame. Vocabulary is `Sorrow Entity`, `SECC`, `M.A.W.`, `Han` — never imported terms from other franchises. A contradiction between two sources **inside** the dossier (Tale vs Origin, local equipment vs Side Codex) is recorded as standing evidence, never silently averaged away.

## SCAFFOLD — FILL EVERY PLACEHOLDER IN ORDER

~~~markdown
# {{ENGLISH_NAME}} — {{KOREAN_NAME}}

> *“{{EPIGRAPH — one line, in the entity's own register; it states the wound or the rule, never a summary of the file}}”*

## SECC Classification

| Field | Value |
|---|---|
| **Designation** | `{{ORIGIN C/N/O}}-{{COHERENCE I–V}}{{POTENCY α/β/γ/δ/ω}}-{{NUMBER}} [{{FACTION/RECORD CODE}}]` |
| **Entity Type** | **{{Object/Place / Object / Place / Time / Hazard}}** — {{Can breach via Transform / Non-breaching: manifestation in place; activates on {{condition}} — note: the relic STRUCTURE (triad below), not this row, fixes the category}} |
| **Coherence** | {{Residue (I) / Echo (II) / Fragment (III) / Entity (IV) / Sovereign (V)}} — {{behavior descriptor in this entity's terms}} |
| **Potency** | {{Minor (α) / Moderate (β) / Major (γ) / Critical (δ) / Catastrophic (ω)}} — {{handling descriptor}} |
| **Sorrow Category** | {{City Sorrow (도한) / Inner Sorrow (내한) / Outside Sorrow (외한) — must match the designation's first letter}} |
| **Element** | {{Grudge / Lament / Void / Weight — exactly one, unless the canon source itself records otherwise}} |
| **Manifestation** | {{Object-… / Place-… / Time-… form recorded in the source}} |
| **Physical Form** | {{Mixed / Organic / Inorganic / Acoustic / Phenomenological}} — {{the body in 2–4 sentences: what is seen, what moves, what it is made of, what the instruments read. This row is load-bearing; Appearance below must agree with it word for word in substance}} |
| **Movement** | {{the instrument's own stillness, creep, or in-chamber relocation — it is carried, channelled, or kept; it does not travel to its work}} |
| **Location** | {{registered location — district, zone, named place; the same string recurs across the file}} |
| **R.D. Comprehension Level** | {{1 — Trace / 2 — Basic / 3 — Advanced / 4 — Deep / 5 — Sovereign}} |

## Operational Parameters

> **Mechanics Reference:** Suggested operational values for field simulation and balancing. These parameters support structured play without replacing the canonical SECC classification.

| Statistic | Value |
|---|---|
| **Risk tier** | {{written potency}} ({{Greek letter}}) |
| **Entity role** | {{Object/Place / Object / Place / Time / Hazard}} |
| **Primary pressure** | {{what it presses on — Resilience (resilience/will) / Composure (composure and willpower) / Clarity (identity and memory), or physical/structural; name the register the costs land in}} |
| **Starting Sorrow Gauge** | {{range fitted to potency, e.g. 35–50% at β; must match the Combat Record below}} |
| **Han-Energy yield** | {{range}} Han-Energy per successful work cycle |
| **Work difficulty** | {{written difficulty}} · R.D. Comprehension Level {{n}} — {{level name}} |
| **Activation threshold** | {{count of ignored conditions, if the file uses one; state its scope so it is not confused with the gauge thresholds below}} |
| **Tool / M.A.W. grade** | I-Relic (Indumentum) · {{M.A.W. grade letter}} — {{Weapon name, Suit name, Stigma name}} |
| **Vessel-Destructible** | {{Yes / No — and be able to defend it from the Physical Form row}} |
| **Han Dust Drop (Vessel Destruction)** | {{range fitted to potency}} ({{Greek letter}}) |
| **Recommended response** | {{the one correct first move, in this file's own terms; must agree with Behavior and with the Resolution Condition below}} |

### Operational Notes

- {{the cycle: what a worked cycle does and does not change}}
- {{the escalation tell operators actually read — a number, a posture, a boundary, a sound}}
- {{what yield and risk vary with, if not seniority or equipment, say so}}
- {{extraction: separate authorisation, its scheduling limits}}

## Combat Record
### Core Stat Line

> **R.D. Field Parameters:** Normalized combat values for quick encounter reference. These values support field use and do not replace the full entity record.

| Stat | Value |
|---|---|
| **Speed** | {{m/s if it travels; if it does not travel, say what this number can honestly mean or record the file's own convention}} |
| **Resistance** | {{x}}% against {{own element}} pressure; {{y}}% against other pressure types |
| **Activation threshold** | Sorrow Gauge ≥ {{60% typical}} |
| **Sorrow Gauge [HP]** | {{max}}/{{max}} |
| **Han Pressure [ATK]** | {{low–high}} per hit · {{Element}} |
| **Coherence modifier** | {{I–V}} — affects behavior complexity and response speed |
| **Potency modifier** | {{Greek letter}} — affects pressure, durability, and escalation severity |


> **R.D. Operational Record:** The following parameters are used to prepare personnel for contact with this entity. They describe field behavior and response conditions; the SECC classification and recorded history remain authoritative.

| Field | Value |
|---|---|
| **Battle Length** | {{Short / Medium / Long}} — {{turns}} turns |
| **Threat Role** | {{Standard / Elite / Sovereign encounter}} |
| **Coherence** | {{same as classification}} |
| **Primary Pressure** | {{Resilience / Composure / Clarity — the register its actions drain}} |
| **Starting Sorrow Gauge** | {{same range as Operational Parameters}} |
| **Difficulty** | {{same as Work difficulty}} |
| **Valid Work Types** | Viderehan and Ferrehan {{only — at the {{plinth / stand / chamber position}}, under certified Tool protocol; a relic session is not a Work Type and never replaces a scheduled cycle}} |
| **Battlefield** | {{registered location}} |
| **Resolution Condition** | {{the specific act that ends an encounter — a condition personnel perform, never "kill it", never a damage total}} |

### Combat Actions

| Name / Category | Flavor Text | Combat Move | Combat Effect/Stat | Trigger |
|---|---|---|---|---|
| { *{{Action 1 name}}* [**Debuff**] } | "{{flavor — what it feels like, present tense}}" | [{{what the entity visibly does}}] | *{{register effect in prose}}* **[{{n}} {{Element}} DMG [{{Element}}]]** | {{observable trigger}} |
| { *{{Action 2 name}}* [**Debuff**] } | "{{flavor}}" | [{{move}}] | *{{effect}}* **[{{n}} {{Element}} DMG [{{Element}}]]** | {{trigger}} |
| { *{{Action 3 name}}* [**Attack**] } | "{{flavor}}" | [{{move}}] | *{{effect}}* **[{{low–high}} {{Element}} DMG [{{Element}}]]** | {{trigger}} |
| { *{{Action 4 name}}* [**Attack**] } | "{{flavor}}" | [{{move}}] | *{{effect, including any gauge surge}}* **[{{low–high}} {{Element}} DMG [{{Element}}]]** | {{trigger}} |
| { *{{Action 5 name}}* [**Ultimate**] } | "{{flavor}}" | [{{move}}] | *{{effect, area and duration}}* **[{{low–high}} {{Element}} DMG [{{Element}}] (AoE, x3 turns)]** | When the Sorrow Gauge reaches {{65% typical — keep distinct from the activation threshold or join them explicitly}} |

### Battle Phases

1. **Tension:** {{identification first — the two or three checks that prove this is the right entity before anyone works: marker, position, instrument}}
2. **Clash:** {{how the work is actually done here — ground, cover or its absence, which Work Types carry it, what the gauge answers to}}
3. **Resolution:** The watch closes under management on the recorded condition — **{{Resolution Condition, repeated verbatim}}** — with the instrument {{returned / closed / still unspent}} and the session record complete.

### Consequences

- {{failed resistance: where the pressure goes — into the worker, named by register; never a generic "psychological matrix"}}
- {{extended exposure: the identity course over time, and what relief/second workers are briefed to screen for afterwards}}
- {{extraction and equipment: what the M.A.W. takes, and that the price is paid by the person, itemised in the equipment section}}
- {{the unresolved ending: if the Resolution Condition is not performed, what simply continues}}

## Appearance
**Primary Form:** {{repeat the Physical Form substance in prose — body, parts, motion}}

**Notable Features:** {{the behaviours inseparable from looking at it: what it does while being seen}}

**Identification Profile**

- **Entity Type:** {{Object/Place / Object / Place / Time / Hazard}}
- **Manifestation:** {{same as classification}}
- **Primary marker:** {{the one visible fact that identifies it in a crowd}}
- **Position / movement:** {{where it is met and how it is moving; what to log}}
- **Element signature:** {{Element}}
- **Registered location:** {{registered location}}

### Detailed Appearance Profile

| Field | Detail |
|---|---|
| **Form** | {{body again, for the watcher's eye: proportions, surfaces, what is absent}} |
| **Position / movement** | {{posture and movement as safety information: which state is safe, which is the warning}} |
| **Material / signature** | {{Element}} — {{materials, colours at core and edge, sound, smell, what instruments read versus what skin reads}} |
| **Distinctive markers** | {{the short list a watcher confirms before work}} |
| **Identification** | {{the check: designation, element, manifestation, registered location — and the fastest field confirmation unique to this entity}} |

**Appearance protocol:** {{what to record, in what order, at every contact — counts, postures, colours, distances, separate tallies where two phenomena run independently}}

{{OPTIONAL but recommended — **Reading the {{sight-picture name}}:** one digit-free paragraph separating the sight-pictures a watcher must not merge (figure vs source vs remnant vs telling detail), each grounded in a fact already recorded in this file. Delete this instruction line; keep the paragraph only if the file's own facts support every sentence.}}

## Origin
- **Formation:** {{what the sorrow was before it was this}}
- **The Sorrow:** {{the specific grief, named plainly}}
- **The Event:** {{the incident or process that produced the entity}}
- **The People:** {{who suffered, who acted, who is absent}}
- **Expanded origin context:** {{the documentary layer — records, amendments, applications, refusals — with its disagreements left standing; a contradiction between two in-file sources is recorded, never silently settled}}

## Behavior
> **Object/Place Work Rule:** Objects and Places cannot be emotionally engaged through Flerehan or confronted through Pugnahan. Only Viderehan (Observation) and Ferrehan (Endurance) are valid Work Types.

| Work Type | Response | Gauge Change |
|---|---|---|
| **Flerehan** | N/A — emotional engagement requires a subject; there is nothing here to grieve with. | N/A |
| **Pugnahan** | N/A — confrontation requires a subject; there is nothing here to fight. Force applied is recorded as {{what force actually does here, if the record says — damage, feeding, nothing}} and is not Work. | N/A |
| **Viderehan** | {{what observation recovers — the event, the count, the line as it stood}} | {{Stable typical; Decrease only if the record supports it}} |
| **Ferrehan** | {{what enduring its presence consists of, and how it is timed or scored}} | Decrease |



### Operational Work Notes

{{How to read the table: it is a diagnostic, not a procedure. Restate the classification once in prose, name the two cautions a worker needs (nothing carries over from a similarly named holding; a flat gauge is not a free watch), each grounded in this file.}}

**Reading the response:** {{what a falling, stable, and rising gauge each look like here, in observable terms — and which instrument outranks the room's mood}}
## Activation Behavior

> **This Relic can Benefit the Facility**
> **This Relic is Capable of Operative Alteration**
> **This Relic Extracts Personal {{register — Resilience / Composure / Clarity, matching Primary Pressure}} upon Extended Use**

**Activation Trigger:** {{taking-up contact — hand placed, mask worn, item mounted; name the body contact exactly}}

**Effect:** {{primary effect in one sentence — identical in substance to Primary Effect below}}

**Duration:** {{Until removed / until the hand is lifted / while worn — attachment is the duration}}

**Risk:** {{the class risk in this instrument's terms}}

### Tool Use Profile — I-Relic

| Field | Record |
|---|---|
| **Tool Class** | **I-Relic** |
| **Use Mode** | **Equippable / mounting use** |
| **Activation** | {{taking-up contact — hand placed, mask worn, item mounted; name the body contact exactly}} |
| **Primary Effect** | {{what it does, one sentence}} |
| **Duration** | {{Until removed / until the hand is lifted / while worn — attachment is the duration}} |
| **Termination / Return** | {{the deliberate unequip, step by step, under the named detachment protocol; what premature return or exceeding the threshold leaves behind in the operator after the instrument resets}} |
| **Risk** | {{the residue that remains in the operator, and when}} |

**Operational Rule:** {{who may use it, the discipline of a session, the second person's exact role where one is required, the hard limit * brief requires; end with the standing sentence in this file's words: a relic session cannot replace a scheduled cycle; containment remains Viderehan and Ferrehan.}}

### Log and Method

| Interaction Amount | **Log** | **Method** |
|---|---|---|
| {{shortest amount}} | {{what is observed at this amount — the instrument and the operator, separately}} | {{what it means — effect onset, the register moved, what the second worker watches for}} |
| {{next amount}} | {{…}} | {{…}} |
| {{next amount}} | {{…}} | {{…}} |
| {{limit amount}} | {{the state at the limit, named plainly}} | {{the stop, the forced-ending consequence, and what remains afterwards}} |

{{Amounts are contact durations (seconds to minutes is the measured habit). Each row must be writable from observation: the instrument's behaviour and the bearer's, logged separately.}}

### Escalation Notes

{{Escalation as measurement: trigger, first mark exceeded, new boundary or state, who newly stands inside it, the aggregate consequence. Emotional indicators are logged but are not the instrument.}}

**Response sequence:** {{mark first, clear second, confirm activation-versus-expansion third, apply the recorded protocol last. Two Work Types are valid and no improvisation is available here.}}

### Detailed Activation Record

| Activation field | R.D. operational detail |
|---|---|
| **Trigger** | {{taking-up contact — hand placed, mask worn, item mounted; name the body contact exactly}} |
| **Manifestation** | {{Manifestation, exactly as classified}} |
| **Primary effect** | {{one sentence, agreeing with the profile}} |
| **Duration / rate** | {{Until removed / until the hand is lifted / while worn — attachment is the duration}} |
| **Risk** | {{written potency}} ({{letter}}) {{Manifestation}} producing {{Element}} pressure; {{specific harm in one sentence}} |
| **Management** | {{Viderehan and Ferrehan only, certified Tool protocol, the marking/boundary duty, and the absolute prohibitions}} |

**Activation reporting order:** {{first measurable}} → {{instrument reading}} → {{boundary/count}} → {{who newly affected}} → {{aggregate consequence}} → {{management condition}}. Objects and Places are worked with Viderehan and Ferrehan only.

## M.A.W. Equipment

> **Materialized Agony Wear (M.A.W.):** the entity's archetype drawn into equipment form and split into three M.A.W. pieces — Weapon, Suit, and Stigma.

### M.A.W. Weapon — {{Weapon name}}

**Type:** Weapon | **Grade:** {{potency letter}} | **Element:** {{Element}}

**Appearance:** {{the object as seen and handled — material, moving parts, resting state; the appearance must be drawable from this paragraph alone}}

{{how it strikes, in two or three sentences}}

**Damage:** {{Element}} {{low–high}}
**Speed:** {{n}} ({{Slow / Normal / Fast}})
**Range:** {{n}} ({{Short / Medium / Long}})
**Max Amount:** {{n}}
**Cost:** {{n}} Sorrow Echoes

**Attack Pattern:** {{Single / Skewer / other named pattern}}
**Target Coverage:** {{how many, chosen how}}
**Falloff Rule:** {{how damage changes across targets or distance — write the rule the pattern implies; if the Side source carries the pattern and this file does not, say so rather than inventing one}}
**Damage Application:** {{which register it wounds — Body / Mind / Soul — and how to log it}}

**Ability:** {{what it does beyond damage, in the entity's own logic}}

**Cost:** {{the wielder's price — this piece only, never the set's blended toll}}

### M.A.W. Suit — {{Suit name}}

**Type:** Armor (Suit) | **Grade:** {{potency letter}} | **Element:** {{Element}}

**Appearance:** {{the garment as seen on the rack and as worn}}

**Resistances:**
- Lament: {{multiplier}} ({{Resistant / Warded / Normal / Weak}})
- Grudge: {{multiplier}} ({{…}})
- Void: {{multiplier}} ({{…}})
- Weight: {{multiplier}} ({{…}})
**Max Amount:** {{n}}
**Cost:** {{n}} Sorrow Echoes

**Ability:** {{which pressure it answers, and against what it is worse than nothing}}

**Cost:** {{the wearer's price — this piece only}}

### M.A.W. Stigma — {{Stigma name}}

**Type:** Accessory (Stigma) | **Grade:** {{potency letter}} | **Element:** {{Element}}

**Appearance:** {{the small object as held and worn}}

**Slot:** {{Tail / other named slot — the slot is a fact, keep it identical everywhere it appears}}
**Acquisition Probability:** {{n}}%
**Effect:** {{+n to {{named stat or work}} — name the stat; an unnamed "+2" is an unfinished file}}

**Ability:** {{what it does}}

**Cost:** {{the bearer's price — this piece only}}

{{OPTIONAL italic provenance line: how this piece comes to exist — bestowed, extracted, cut, found — only if a source in this file supports it.}}

### M.A.W. Use Notes

{{The set as one condition: what using as intended looks like, what using against the pattern costs, and which piece is handled differently from the others and why.}}

### Field Use Record

| Stage | Required record |
|---|---|
| **Before use** | {{wielder, piece, the day's reading, and the piece-specific baseline lodged with a second worker}} |
| **During use** | {{the first sign, named per piece — Weapon, Suit, and Stigma announce themselves differently; the hour first seen, entered by the second worker}} |
| **At limit** | {{the stop, named per piece, plus any shared stop across the set; whose call stands against the bearer's}} |
| **After use** | {{return, re-assessment interval, and the separate per-piece finding that the toll has lifted before any reissue}} |

**Stat interpretation:** {{what the grade does and does not tell the reader — the cheap half and the expensive half of the reading}}

## 관찰 기록 (Observation Log)

**R.D. Comprehension Level:** {{n}} — {{level name}}

- {{observation with its count or series attached}}
- {{the most reliable index this file has}}
- {{the exposure course the counsellors screen for}}

**Personnel Note:** *“{{first-person, specific, one watcher's voice}}”* — {{role, R.D.}}



### Observation Progression

| Observation stage | R.D. record |
|---|---|
| **Initial exposure** | {{first sign, first check, what the first person present must do or not do}} |
| **Sustained observation** | {{the standing measurements, taken the same way every time}} |
| **Activation or escalation** | {{the warning, stated as an observable}} |
| **Post-contact review** | {{what is tallied, what is asked, and what the review may not be used for}} |

**Observation method:** {{the instruments and counts, the fixed positions, the separate tallies}}
## 이야기 보고 (Story Log) — Observation Entries

> Progressive declassified records. Each entry unlocks at a higher Comprehension Level.

**Entry 1 — Containment Description**
{{designation, manifestation, element, formation in one breath, and the one behavioural fact a stranger needs}}

**Entry 2 — <{{field or watch record, with its in-world date}}>**
{{what was seen doing, where, with the count or measurement}}

**Entry 3 — <{{marginal, office, or testimony record}}>**
{{the sorrow stated by somebody inside the record}}

**Entry 4 — <Containment Notice>**
{{management in one sentence, then the four Work responses compressed with their gauge directions, agreeing with the Behavior table}}

**Entry 5 — <Archive Note>**
{{the institutional reading — what the office says this case proves, and what it leaves out}}

## 최종 관찰 (Final Observation)

> {{the choice the watch is actually making at the close of contact, stated in one sentence}}

| {{the correct performance of the Resolution Condition, plainly}} | {{the kinder improvisation the file records as failure}} |
|---|---|
| {{the entity's recorded answer; the sorrow is witnessed and {{NAME}} is fully recorded}} | {{the recorded failure course; the gauge climbs}} |
| **OBSERVATION SUCCESS** | **OBSERVATION FAIL** |

## 감각 묘사 (Flavor Text)

{{one short sensory paragraph — this entity only: light, sound, temperature as actually recorded, the urge it produces}}



**At first contact:** {{the first impression, ending on the Primary Form sentence}}

**With continued exposure:** {{the second hour — the working post, the routine, what stops frightening and what starts mattering; write the actual room or ground, never a generic cell}}

**When the entity activates:** {{the observable tell — the same warning the Observation Progression names}}

**After departure:** {{how a watch actually ends here — the door, the route, the reopened hall — and what goes home with the watch}}

### Interaction Pattern

{{the neighbouring holdings in working range, and the axis each pairing is a question about — sound, movement, temperature, memory, gauge, stability}}

**Interaction method:** {{baseline alone first, then the pairing, from the same positions, with the same instruments}}

### Entity Interaction Record

{{one paragraph distinguishing this holding from the neighbours it is confused with}}

| {{Nearby holding / Holding paired}} | {{How the two have stood / The contact, as observed}} | {{What the watch logged / What was measured}} | {{What the entry carries / What the file still lacks}} |
|---|---|---|---|
| **{{Neighbour 1}}** | {{the standing relation}} | {{measured result, including honest nulls}} | {{what to keep recording}} |
| **{{Neighbour 2}}** | {{…}} | {{…}} | {{…}} |
| **{{Neighbour 3}}** | {{…}} | {{…}} | {{…}} |

**Interaction procedure:** {{baseline, distance of first change, duration, and the test that separates a passing interaction from a lasting one}}

## 이야기 (Narratio) — The Tale

{{Paragraph 1 — the whole origin in three sentences: what happened, what was not done about it, what it became.}}

{{Paragraph 2 — the world before: the people, the institution or place, the ordinary arrangement that made the wound possible.}}

{{Paragraph 3 — the event and its immediate human cost, told from the record's strongest source.}}

{{Paragraph 4 — the mechanism: how the unprocessed sorrow sank, condensed, ignited, froze, or otherwise took the form the Physical Form row describes. The Tale's imagery must be reconcilable with that row — if the Tale remembers it larger, older, or stiller, the dossier must say which picture is the working one.}}

{{Paragraph 5 — the present tense: what approaching it now delivers, undiluted.}}

{{Closing paragraph — "Some sorrows are about X. {{NAME}} is about Y" — the distinction this entity exists to carry.}}
## 증언 (Testimonium) — The Testimony

> *“{{the keeper's sentence}}”* — Keeper, Archive

> *“{{the researcher's sentence}}”* — Researcher, R.D.

> *“{{the containment lead's sentence}}”* — Containment Lead, R.D.

> *“{{a citizen or local voice}}”* — Citizen, {{place}}

> *“{{the longest-view voice}}”* — {{Elder / Former Soldier / other named standing}}, {{place}}
## 기록 (Registrum) — The Record

**Classification:** Sorrow Entity — `{{DESIGNATION}} [{{CODE}}]` · {{origin}} origin · {{Coherence}} coherence · {{Potency}} potency · {{Element}} · {{Manifestation}} manifestation
**Common Name:** {{ENGLISH_NAME}}
**Containment Status:** Contained — {{registered location}}
**Comprehension Level:** {{n}} — {{level name}}
**Threat Assessment:** {{written potency}} ({{letter}}). {{the one-sentence operational truth, with its best count attached}}
**Containment & Handling Procedures:**
- {{permitted works and the prohibited one, with the reason}}
- {{the conduct, position, or instrument rule}}
- {{what never to do first}}
**Observation Notes:**
- {{origin fact, compressed}}
- {{the standing count or series}}
- {{extraction or scheduling standing instruction}}
**Cross-References:** {{documents, applications, maps, neighbour files — separated by · }}
**Faction Involvement:** {{factions with their parenthetical remits}}
**Originator:** {{who or what the record holds responsible, in the record's own terms}}

### Registry Addendum

**Operational interpretation:** {{what kind of file this is — which of its numbers are instruments and which are documentary; what every figure assumes about personnel}}

**Review requirement:** {{when this file must be re-verified, what is re-measured first, and what a review may not be used for}}
## {{Warden Record / Watch Record}}

### {{First aspect — a concrete noun phrase from this entity's life}}

{{Two to four paragraphs across the whole Warden/Watch Record should carry the documentary argument of the file: the counts and what they measure, the institutional limit (what the facility may not do and why the rule is defensible), the devices invented to work within that limit, and the named refusals with their in-world dates. Every number here must agree with the Registrum and the Tale.}}

### {{Second aspect}}

{{…}}

### {{Third aspect}}

{{…}}

### {{The counting section — what the standing number is measuring}}

{{…}}

## Trivia

- {{a true, checkable oddity of the record}}
- {{a second, different in kind}}



### Registry Trivia

- **Classification detail:** {{class restated with its operational consequence}}
- **Field detail:** {{element and registered location, with what follows from the pairing}}
- **Recognition detail:** {{the fastest correct identification, and the nearest false one}}
- **Record detail:** {{the state of the paperwork — corrections, stale copies, unreconciled returns — stated plainly}}
- **Containment detail:** {{what containment actually consists of here}}
## Document Information

**Document ID:** SE-{{DESIGNATION}}
**Author:** {{in-world author with role}}
**Date:** Year {{4,2xx}}
**Classification:** Restricted
~~~

## VALIDATION CHECKLIST (must PASS before commit)

- [ ] Category test re-run on the finished file gives THIS category (triad heading / role row), and `Entity Type`, `Entity role`, `Valid Work Types`, `Recommended response`, `Behavior`, and Registrum all tell the same category story.
- [ ] `grep -c '{'` on the finished dossier returns **0** (no placeholder survived).
- [ ] Every number agrees across Operational Parameters, Core Stat Line, Operational Record, Combat Actions, escalation, equipment costs, Observation counts, Tale, Registrum, and Trivia. Thresholds with different scopes (condition count vs gauge % vs ultimate %) are labelled with their scopes or joined explicitly.
- [ ] Physical Form row, Appearance, Movement, Combat Actions, failure section, and Tale describe one reconcilable body/state — or the file explicitly separates the pictures and says which one personnel meet.
- [ ] M.A.W. names, grades, damages, resistances, slots, percentages, and echo costs are internally identical everywhere, and the Stigma bonus names its stat. Field Use Record costs are piece-specific (no blended set toll).
- [ ] Five Story Log entries, Final Observation SUCCESS/FAIL pair, four-part Flavor quartet, five Testimonium voices, Warden/Watch Record, and Registry Trivia all present and written from this entity's facts (the similarity tools compare against all 301 dossiers — borrowed sentences fail the gate).
- [ ] Use Mode reads exactly `Equippable / mounting use`; Duration is attachment-bounded; Termination is a manual unequip with a named protocol and a stated premature-return residue.
- [ ] Nothing in the file lets the relic act while unattended, at range, or after correct detachment.
- [ ] `python3 tools/verify.py <file>` → `RESIDUAL 0`, `seam []`, `pipe True`, `dupes []`.
- [ ] `python3 tools/tpl.py <file>` → `RESIDUE 0`.
- [ ] `python3 tools/sectfile.py <file>` → 0 sections over 0.05.
- [ ] `python3 tools/wikistd.py <file>` → `meets True` (parity/condition/series/disposition clean).
- [ ] `python3 tools/sect.py <file>` → GENERIC at template-furniture level only; no prose line shared with another dossier beyond standard headings/blockquotes.
- [ ] File name matches `SE-{CODE}_{English_Name}_{Korean_Name}.md` exactly, then ship via `bash tools/gate.sh "<message>"` and confirm PUSH VERIFIED.
