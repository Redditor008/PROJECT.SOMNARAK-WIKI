# 03 — M.A.W. WEAPON TEMPLATE (B-File)

**Template ID:** `T-03-MAW-B`  
**Generates:** `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_{{RANGE}}/{{ID}}_{{Folder}}/SE-{{ID}}-B__MAW-W_{{Weapon_Name}}.md`  
**Authority:** `SOMNARAK_MAW_CODEX.md` + `SOMNARAK_BATTLE_SYSTEM.md` (Range Bands, Falloff, Speed/AP) + Laws 6,7,8

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Weapon archetype spans Year 0000–9999+** — guns, katanas, chakrams, astral prisms, culverins, mauls, lenses, fangs, daggers, cleavers are ALL valid as timeless manifestations. Do not scrub.
- **Every B-file must have:** ITEM IDENTITY table, Appearance (source-led), Extraction History + Rejection Rule, COMBAT RECORD (Damage/Speed/Range/Falloff), Signature Ability, Wielder Cost, History of Use (incident + aftermath), Set Resonance.
- **Combat math:** Damage element = one of 4 (Grudge/Lament/Void/Weight). Speed 1–6 (1 Very Slow, 6 Very Fast) maps to AP. Range 1–5 (Melee to Line). Falloff: `Primary 100% → first pierced 70% → second pierced 50%` for piercing weapons. Non-piercing uses single-target.
- **Never write workshop manufacturing.** Crystallization language only.

---

## FILE NAMING

```
SE-{{ID}}-B__MAW-W_{{Weapon_Name_With_Underscores}}.md
```

Registry Code: `MAW-W-{{NUM}}-01`

---

## SCAFFOLD

~~~markdown
# M.A.W. WEAPON — {{WEAPON_NAME_EN}} — {{KOREAN_NAME}}

> *“{{Epigraph — what the blade/cannon/lens believes about grief.}}”*

**Document ID:** `SE-{{ID}}-B`  
**Linked Entity:** `SE-{{ID}}` — {{Entity Name}}  
**Item Registry Code:** `MAW-W-{{NUM}}-01`  
**Author:** Extraction Lead Zyrak  
**Date:** Year 4,238 — Dawn Initiative  
**Classification:** Classified  
**Codex Set Completion:** `4/4`

## ITEM IDENTITY

| Field | Record |
|---|---|
| **Type** | Weapon — {{singing blade / maul / lens / fang / culverin / prism / etc.}} |
| **Category** | {{MELEE / RANGED / PIERCE / LINE RESONANCE}} |
| **Grade** | {{α / β / γ / δ / ω}} |
| **Element** | {{Grudge — Crimson / Lament — Deep Blue / Void — Pale White / Weight — Black}} |
| **Maximum Amount** | {{1–4 — Limited}} |
| **Echo Cost** | {{20–80 Sorrow Echoes}} |
| **Bearer Requirement** | {{Vigil/weight/memory condition — must echo Side Codex}} |
| **Status** | {{Active, restricted issue / Vaulted / Field trial}} |

### Appearance

{{2–3 sentences source-led. E.g., “A delicate eight-inch stiletto of gold-tinted celestial alloy, tapering into a needle point with diamond serrations. The blade absorbs darkness and emits a warm twilight luminescence; piercing strikes discharge radiant pulses that blind adjacent hostiles.” Include silhouette, material, light/sound/pressure.}}

## EXTRACTION HISTORY

{{2–3 sentences: approved Named Vigil, thread of light, hardening. See Side Codex for full donor lore — do not duplicate verbatim.}}

### Rejection Rule

{{Specific misuse → specific punishment. E.g., “Bearer who uses blade to erase memory hears Bell without pause; strikes redirect inward as Lament until returned.”}}

## COMBAT RECORD

| Field | Record |
|---|---|
| **Damage** | {{Element}} {{12–18 for γ typical; 24–48 for ω}} |
| **Speed** | {{1 Very Slow — 6 Very Fast}} |
| **Range** | {{1 Melee — 5 Line}} |
| **Attack Pattern** | {{Wide Arc / Line Resonance / Single Pierce / Cone}} |
| **Target Coverage** | {{One corridor line, up to {{N}} targets linked by {{shared grief event}}}} |
| **Falloff Rule** | {{Primary 100% → first pierced 70% → second pierced 50% (or “Single target — no falloff”)}} |
| **Recovery** | {{One breath / Two beats / Instant}} |

### Signature Ability — {{ABILITY_NAME}}

**Trigger:** {{Condition — e.g., “Primary target must be marked by recent loss, spoken name, or active Lament pressure.”}}

**Effect:** {{What it does — toll through target + linked line, damage + status. Include Pierce falloff if applicable.}}

**Limit:** {{When it fails or deals lower value}}

### Wielder Cost

{{Intimate price per swing/shot. Must be personal — memory, voice, warmth, years, sensation. E.g., “Bearer hears fragment of Bell’s search after every swing. Three activations cause one childhood memory to blur until written/spoken aloud.” Specify stacking and recovery.}}

## HISTORY OF USE

### Incident — {{INCIDENT_TITLE}}

**Date:** Year {{4,2xx}}  
**Bearer:** {{Rank + Name}}  
**Result:** {{2–3 sentences: where, who it cut/saved, how Pierce chain worked.}}

**Aftermath:** {{Bearer cost paid — what was forgotten/lost, who restored it.}}

## SET RESONANCE

{{1–2 sentences: what equipping full set (Weapon+Suit+Gift) grants. Must be unique per set, not generic.}}
~~~

---

## VALIDATION CHECKLIST

- [ ] Damage element is one of 4; Grade matches donor potency ±1 tier.
- [ ] Speed 1–6 and Range 1–5 present with correct AP mapping in prose.
- [ ] Falloff rule present where applicable; single-target weapons explicitly say “no falloff.”
- [ ] Signature Ability has Trigger + Effect + Limit (all three).
- [ ] Wielder Cost is personal (memory/voice/warmth/years), not generic “HP loss.”
- [ ] History of Use has Date + Bearer + Result + Aftermath (all four).
- [ ] Rejection Rule is specific (misuse → specific redirection).
- [ ] Zero banned strings; timeless archetype preserved.
