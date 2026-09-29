# 04 — M.A.W. SUIT TEMPLATE (C-File)

**Template ID:** `T-04-MAW-C`  
**Generates:** `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_{{RANGE}}/{{ID}}_{{Folder}}/SE-{{ID}}-C__MAW-S_{{Suit_Name}}.md`  
**Authority:** `SOMNARAK_MAW_CODEX.md` + `SOMNARAK_BATTLE_SYSTEM.md` (Resistances) + Laws 6,8

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Suit (C) is woven from resonance, not sewn.** Language: “woven from Han-gossamer,” “crystallized veil,” “weight of debt pressed into armor.”
- **Resistances are multipliers:** `0.3–0.5` Resistant (strong), `0.8` Withstood, `1.0` Neutral, `1.2–1.6` Weak, `2.0` Vulnerable. Every suit must list all 4 elements. Typical pattern: strong against donor element, weak against its opposite.
- **No “defense points” — use multipliers.** Example: `Void: 0.3 (Resistant)` not `+30 armor`.
- **Wielder cost for suits is ambient** — wearer feels absent, cold, hollow, tethered, not acute memory loss per swing (that’s Weapon). Suits erode identity slowly.

---

## FILE NAMING

```
SE-{{ID}}-C__MAW-S_{{Suit_Name}}.md
```

Registry Code: `MAW-S-{{NUM}}-01`

---

## SCAFFOLD

~~~markdown
# M.A.W. SUIT — {{SUIT_NAME_EN}} — {{KOREAN_NAME}}

> *“{{Epigraph — what it feels like to wear the sorrow.}}”*

**Document ID:** `SE-{{ID}}-C`  
**Linked Entity:** `SE-{{ID}}` — {{Entity Name}}  
**Item Registry Code:** `MAW-S-{{NUM}}-01`  
**Author:** Extraction Lead Zyrak  
**Date:** Year 4,238 — Dawn Initiative  
**Classification:** Classified  
**Codex Set Completion:** `4/4`

## ITEM IDENTITY

| Field | Record |
|---|---|
| **Type** | Armor — {{veil / mantle / shroud / plate / bulwark / skin}} |
| **Category** | {{Light / Medium / Heavy / Resonant}} |
| **Grade** | {{α / β / γ / δ / ω}} |
| **Element** | {{Grudge / Lament / Void / Weight}} |
| **Maximum Amount** | {{2–4 — Limited}} |
| **Echo Cost** | {{20–60 Sorrow Echoes}} |
| **Bearer Requirement** | {{Same vigil as Side Codex — e.g., “Must have completed Bell vigil.”}} |
| **Status** | {{Active / Vaulted}} |

### Appearance

{{2–3 sentences woven imagery. E.g., “A flowing veil of Void Han-gossamer, near-translucent and almost colourless, that shifts and breathes with the wearer. Threads tighten when Void pressure nears.” Material, movement, light.}}

## EXTRACTION HISTORY

{{1–2 sentences: veil woven from same thread as Weapon. Same vigil, same hardening — tailored to body, not hand.}}

### Rejection Rule

{{Suit-specific misuse → punishment. E.g., “Wearer who uses veil to hide from Witnessing finds veil tightening until breathing is audible to the entity.”}}

## COMBAT RECORD — RESISTANCES

| Element | Multiplier | Verdict |
|---|---|---|
| **Grudge (원한)** | {{0.8 / 1.0 / 1.2}} | {{Withstood / Neutral / Weak}} |
| **Lament (비탄)** | {{same}} | {{...}} |
| **Void (공허)** | {{0.3 for Void donor typical}} | {{Resistant}} |
| **Weight (비중)** | {{same}} | {{...}} |

Resistance math: Damage Taken = Incoming × Multiplier. `0.3 = 70% reduction`. `1.5 = 50% extra`.

### Defensive Trait — {{TRAIT_NAME}}

**Trigger:** {{When it activates — e.g., “Void pressure exceeds 60% Gauge.”}}

**Effect:** {{What it grants — e.g., “Grants Soul shielding, prevents identity dissolution for 2 turns.”}}

**Limit:** {{Cooldown or cost — e.g., “After 3 triggers, wearer feels absent to self until removed and recorded.”}}

### Wielder Cost (Ambient)

{{Slow erosion sentence. E.g., “Wearer feels faintly absent to themselves; extended wear thins recognition of own reflection. Thins after removal with spoken naming ritual.”}}

## HISTORY OF USE

### Incident — {{TITLE}}

**Date:** Year {{4,2xx}}  
**Bearer:** {{Rank + Name}}  
**Result:** {{Where suit held, what pressure it endured, who survived because of it.}}

**Aftermath:** {{Ambient cost — what wearer lost/felt, how recovered.}}

## SET RESONANCE

{{Full-set bonus — same as Weapon file, must match.}}
~~~

---

## VALIDATION CHECKLIST

- [ ] All 4 resistances listed as multipliers with verdict labels.
- [ ] Strongest resistance aligns with donor element (or justified opposite).
- [ ] Defensive Trait has Trigger + Effect + Limit.
- [ ] Ambient Wielder Cost is slow/identity-based, not per-swing.
- [ ] Appearance is woven/crystallized language, not “factory sewn.”
- [ ] History has Date/Bearer/Result/Aftermath.
