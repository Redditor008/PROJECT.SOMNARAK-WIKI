# 02 — M.A.W. SIDE CODEX TEMPLATE (A-File)

**Template ID:** `T-02-MAW-A`  
**Generates:** `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_{{RANGE}}/{{ID}}_{{Entity_Name}}/SE-{{ID}}-A__SIDE_CODEX_{{Name}}.md`  
**Authority:** `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md` + Global Primer Laws 5,6,7,8,9

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Side Codex (A) is the donor lore + extraction gate.** It does NOT contain weapon stats. It records who the entity was, what sorrow crystallized the M.A.W., and what vigil/extraction condition must be met.
- **M.A.W. is not manufactured.** Never write “forged in Workshop” or “assembled.” Use: “crystallized from,” “hardened from a thread of {{Element}} light,” “fell from the bell’s inner rim and hardened.”
- **Quadripartite set is 4/4:** A Side Codex + B Weapon + C Suit + D Gift share the same `SE-{{ID}}` and must all reference the same Linked Entity. `audit_lore_archive.py` checks `198/198 complete`.
- **Appearance must be source-led:** Describe what the M.A.W. looks like as drawn from entity Description — not generic “sword” filler.
- **Rejection Rule is mandatory:** Every M.A.W. has a condition where it punishes misuse.

---

## FILE NAMING

```
SOMNARAK-WORLD/MAW_Codex_Sets/Registry_{{RANGE}}/{{NUM}}_{{Entity_Folder}}/SE-{{ID}}-A__SIDE_CODEX_{{Codex_Name}}.md
```

Example: `Registry_001_to_007/001_Orphaned_Bell/SE-001-A__SIDE_CODEX_The_Orphaned_Bell.md`

---

## SCAFFOLD

~~~markdown
# SIDE CODEX — {{CODEX_TITLE_EN}} — {{KOREAN_TITLE}}

> *“{{Epigraph — the entity’s sorrow in one line}}”*

**Document ID:** `SE-{{ID}}-A`  
**Linked Entity:** `SE-{{ID}}` — {{Entity_English_Name}}  
**Item Registry Code:** `SE-{{ID}}-A`  
**Author:** Extraction Lead Zyrak (Floor 3) / Archive Lead Marjuk (Floor 6)  
**Date:** Year {{4,23x}} — Dawn Initiative  
**Classification:** Classified  
**Codex Set Completion:** `4/4`

## DONOR IDENTITY

| Field | Record |
|---|---|
| **Donor Entity** | `SE-{{ID}}` — {{English Name}} ({{Korean Name}}  {{Romaja}} ) |
| **SECC** | `{{ORIGIN}}-{{RANK}}{{POTENCY}}-{{NUM}}` |
| **Element** | {{Grudge / Lament / Void / Weight}} |
| **Sorrow Core** | {{One sentence: what grief hardened into matter}} |
| **Crystallization Venue** | {{Where it hardened — e.g., “Beneath the Bell at midnight during Sorrow Tide.”}} |
| **Extraction Authority** | {{Floor 3 Extraction Hall, Chamber {{A/B}}}} |

### Donor Lore (300–500 words)

{{3–5 paragraphs: the entity’s origin wound, the human cost that fed it, why this sorrow could become a thing that can be held. No PM terms. Cite the sector/zone.}}

### Extraction History

{{How the first thread of light fell/hardened/cooled. Who stood vigil. What name or weight was carried.}}

### Rejection Rule

{{The misuse that turns the M.A.W. inward. E.g., “A bearer who uses the thread to erase a name hears the Bell without pause; every strike redirects as Lament pressure until returned to the tower.”}}

## EXTRACTION PARAMETERS

| Field | Record |
|---|---|
| **Bearer Requirement** | {{Vigil, weight, or memory condition}} |
| **Harvest Yield** | {{e.g., “99.2% pure crystal, single thread per toll.”}} |
| **Cooldown** | {{e.g., “One tide cycle between extractions.”}} |
| **Risk Class** | {{Same as donor potency: α–ω}} |
| **Containment Note** | {{Where the Codex is stored — Floor 3, Floor 6 Vault, etc.}} |

## RESONANCE & SET IDENTITY

| Field | Record |
|---|---|
| **Set Members** | `SE-{{ID}}-B` (Weapon) · `SE-{{ID}}-C` (Suit) · `SE-{{ID}}-D` (Gift) |
| **Resonance Theme** | {{One-line theme — e.g., “A debt that can be held, worn, and measured.”}} |
| **Narrative Thread** | {{How the three items echo the same wound differently — cut (Weapon), endure (Suit), weigh (Gift).}} |

### Full-Set Resonance (Unique — Do Not Copy-Paste)

{{2–3 sentences of **unique, set-specific** resonance lore for wearing all three. Never reuse generic phrasing across sets.}}

## FIELD REMARKS

> *“{{One-line field testimony — bearer, zone, year.}}”* — {{Rank, Name, Year}}

{{1 paragraph of after-action reflection: what the Codex taught the Directorate about this sorrow.}}
~~~

---

## VALIDATION CHECKLIST

- [ ] Linked Entity `SE-{{ID}}` exists in `Sorrow_Entities/`.
- [ ] No weapon stats in A-file (stats belong in B/C/D).
- [ ] Appearance is source-led (drawn from entity lore, not generic filler).
- [ ] Rejection Rule present and specific.
- [ ] Full-Set Resonance is unique (not copy-pasted).
- [ ] Zero banned strings; in-universe voice only.
