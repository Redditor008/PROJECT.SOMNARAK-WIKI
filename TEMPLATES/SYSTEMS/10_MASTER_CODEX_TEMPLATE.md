# 10 — MASTER CODEX TEMPLATE

**Template ID:** `T-10-CODEX`  
**Generates:** `SOMNARAK-WORLD/Master_Codices/{{06_Subfolders}}/{{CODEX_NAME}}.md`  
**Authority:** `SOMNARAK-WORLD/Master_Codices/README.md` + All 44 Codex standards + Global Primer Laws 4,6,7

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **44 Codices across 6 Subfolders:** 01 Cosmology (7), 02 Institutional (6), 03 Systems/Physics (8), 04 Municipal (9), 05 Entities/Tales (5), 06 Integrity (4). Always place codex in correct subfolder — not root.
- **Codices are in-world monographs, not wiki pages.** Author is a Directorate scholar, Date is Year, Classification is level. Word count target: 300–500 lines for canon codices; do not produce stubs.
- **Geography belongs in `SOMNARAK_GEOLOGY.md`**, not as SE. Companies belong in `SOMNARAK_CORPORATIONS.md`. Workshops belong in `SOMNARAK_WORKSHOPS.md`.

---

## FILE NAMING

```
SOMNARAK-WORLD/Master_Codices/{{SUBFOLDER}}/{{SOMNARAK_TOPIC}}.md
```

Example: `01_Cosmology_and_World_Order/SOMNARAK_THE_DESOLATE.md`

---

## SCAFFOLD

~~~markdown
# Somnarak Codex — {{TITLE_EN}} — {{KOREAN_TITLE}}

> *“{{Epigraph — the thesis of this world law in one line.}}”*

**Document ID:** `CODEX-{{SUBFOLDER}}-{{NUM}}`  
**Author:** {{Archive Lead Marjuk / Research Lead Ayshuk / etc.}}  
**Date:** Year {{4,23x}} — Dawn Initiative  
**Classification:** Level {{3–5}} — {{Access descriptor}}  
**Warden Chapter:** {{01–06 Subfolder Title}}

## I. THESIS & SCOPE

{{1 paragraph: what this codex governs and what it does NOT govern. Explicitly state what belongs in other codices to avoid overlap.}}

## II. CORE SYSTEMS / DOCTRINE

### A. {{System or Doctrine Name}}

{{2–4 paragraphs: the mechanism, physics, or law. Use Somnarak-native terms. Include numbers only as acquisition curves (0.5%/1.0%/5.0% across Grades 1–5), Range Bands (1–5), or Han saturation — never numerical Hz.}}

### B. {{Second System}}

{{Continuation — include tables if needed. Tables must be markdown (outside boxes) — Korean permitted with two-space buffer.}}

| Parameter | Value | Note |
|---|---|---|
| {{Param}} | {{Value}} | {{Note}} |

## III. INSTITUTIONAL FOOTPRINT

{{Which Floors, Companies, Wings, Syndicates, Cadres operate this doctrine — and the Treaty or Corporate matrix that binds them.}}

## IV. FIELD INTEGRATION (10-Node Grid / Battle Engine if applicable)

{{If codex touches combat: define Operative Base Speed Die, Natural Range Bands, M.A.W.-W Speed/Range modifiers, Four P-Framework (Passives, Panic, Parry, Posture), Dual-Threshold Stagger (60% Rupture, 25% Meltdown). Otherwise, note “Non-tactical codex — no grid integration.”}}

## V. HISTORICAL CASE STUDIES

### Case Study — {{TITLE}} (Year {{4,2xx}})

{{2–3 sentences: what happened, what the codex explains about it, what changed after.}}

### Case Study — {{TITLE}} (Year {{4,2xx}})

{{Second case.}}

## VI. CROSS-REFERENCES & READING ORDER

**Prerequisite Codices (read before this one):**
- `{{CODEX_PATH}}` — {{why}}

**Successor Codices (read after):**
- `{{CODEX_PATH}}` — {{why}}

## VII. EDITORIAL CLOSURE

{{1 paragraph archival closure — what remains sealed, what awaits next revision, who holds the key.}}

**Author:** {{Name}}  
**Classification:** Level {{N}}  
**Warden Seal:** {{Floor Seal}}
~~~

---

## VALIDATION CHECKLIST

- [ ] Placed in correct 06 subfolder (01–06) — not root.
- [ ] Length ≥ 300 lines (not a stub); in-world monograph voice.
- [ ] All cross-references use full canonical paths.
- [ ] No PM crossover terms; no numerical Hz; geography not filed as SE.
- [ ] If tactical, includes 10-Node grid + Four P + Dual-Threshold where applicable.
