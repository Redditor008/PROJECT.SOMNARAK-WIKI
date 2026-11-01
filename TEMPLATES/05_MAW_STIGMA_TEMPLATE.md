# 05 — M.A.W. STIGMA TEMPLATE (D-File)

**Template ID:** `T-05-MAW-D`  
**Generates:** `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_{{RANGE}}/{{ID}}_{{Folder}}/SE-{{ID}}-D__MAW-G_{{Stigma_Name}}.md`  
**Authority:** `SOMNARAK_MAW_CODEX.md` + Laws 6,8

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Stigma (D) is NOT crafted — it is granted at random** upon successful work by the entity. Never write “manufactured stigma.” Write: “The entity leaves behind,” “found on the worker’s chest after successful Viderehan,” “bestowal chance.”
- **Stigmas are accessories with slots:** Head, Face, Chest, Hand, Feet, etc. Each has Acquisition Probability (typically 2–5% per work, higher on success) and a passive effect + cosmetic manifestation.
- **Stigma effect is subtle:** +1 stat, +5% resistance, or narrative ability (measure debt, hear Bell fragment, see grief link). Never game-breaking.
- **The item page repeats the cost, and must repeat the same one.** The B/C/D record's own `**Operational / binding cost:**` field states, in two clauses, what one use takes and what continued use does — the same price the embedded block charges, said in the item's own record. The *continued use makes the source sorrow feel autobiographical* tail is retired; a new item page writes its own.
- **Cost is brief but intimate:** Momentary crushing weight, hollow, chill — not permanent loss.
- **The cost is the boon, read backwards, and it belongs to this piece alone.** Forty stigmas in the archive once shared four sentences between them — *moves a little slower* (Weight), *temper shortens* (Grudge), *weeps in their sleep* (Lament), *forgets a word* (Void) — which made four whole elements of the catalogue read as one piece with four labels. Each cost now states what the ability in the line above it implies: the charm that lets a bearer see what somebody else finished by hand takes their own work from them; the charm that keeps a grievance overnight returns it dated. `grep` the finished sentence against `SOMNARAK-WORLD/`: it must return one file.

---

## FILE NAMING

```
SE-{{ID}}-D__MAW-G_{{Stigma_Name}}.md
```

Registry Code: `MAW-G-{{NUM}}-01`

---

## SCAFFOLD

~~~markdown
# M.A.W. STIGMA — {{STIGMA_NAME_EN}} — {{KOREAN_NAME}}

> *“{{Epigraph — what the stigma whispers when held.}}”*

**Document ID:** `SE-{{ID}}-D`  
**Linked Entity:** `SE-{{ID}}` — {{Entity Name}}  
**Item Registry Code:** `MAW-G-{{NUM}}-01`  
**Author:** Extraction Lead Zyrak  
**Date:** Year 4,238 — Dawn Initiative  
**Classification:** Classified  
**Codex Set Completion:** `4/4`

## ITEM IDENTITY

| Field | Record |
|---|---|
| **Type** | Stigma — accessory |
| **Category** | {{Head / Face / Chest / Hand / Feet / Held}} |
| **Grade** | {{α / β / γ / δ / ω}} |
| **Element** | {{Grudge / Lament / Void / Weight}} |
| **Slot** | {{Head / Face / Chest / etc. — where manifestation appears}} |
| **Acquisition Probability** | {{2–5% per successful work cycle}} |
| **Status** | {{Granted at random — not stockpiled}} |

### Appearance

{{2 sentences intimate object. E.g., “A scale-pendant of Void Han-glass, near-translucent and almost colourless, warm to the touch. Catches light only when debt is near.” Must be small, wearable, resonant.}}

## BESTOWAL HISTORY

{{How it is left behind — e.g., “After a Level 3 Viderehan that reduced Gauge to 20%, worker found pendant on chest. No extraction required.” Mention it is not guaranteed; many works yield nothing.}}

### Rejection Rule

{{Stigma misuse → brief punishment. E.g., “User who weighs another’s debt to mock finds scale showing own debt crushing for one breath.”}}

## COMBAT RECORD — PASSIVE

| Field | Record |
|---|---|
| **Passive Effect** | {{E.g., “+1 Composure when working SE-{{ID}}” or “Measure karmic debt weight/type”}} |
| **Activation** | {{Always on while equipped / On successful work / On Gauge threshold}} |
| **Cosmetic Manifestation** | {{What witness sees — e.g., “Pale scale mark on forehead, visible in Veil-light.”}} |
| **Limit** | {{E.g., “No stacking; only one Stigma of this line per person.”}} |

### Wielder Cost (Brief)

Filed as `**Bearer cost:**` in the dossier block. A Stigma has no Echo price — it is found, not bought — so a `**Cost:**` row on a Stigma is a mislabelled bearer cost every time.

{{One sentence, derived from the Passive Effect or Ability directly above it, and used by no other stigma in the archive. “Brief” is a length, not a licence to be vague: it should be short, concrete and checkable.}}

**Retired — do not use:** *The bearer moves a little slower.* · *The bearer's temper shortens.* · *The bearer weeps in their sleep.* · *The bearer occasionally forgets a word.* · *The wielder experiences a persistent low-grade headache with each use.* · any sentence already charged by another piece.

## HISTORY OF USE

### Incident — {{TITLE}}

**Date:** Year {{4,2xx}}  
**Bearer:** {{Name}}  
**Result:** {{Stigma revealed hidden debt / saved through +1 / warned of Tide.}}

**Aftermath:** {{Brief cost — what bearer felt, quick recovery.}}

## SET RESONANCE

{{Full-set bonus — must match B/C files.}}
~~~

---

## VALIDATION CHECKLIST

- [ ] Acquisition Probability present (2–5% typical).
- [ ] Slot specified; Appearance is small/wearable.
- [ ] Bestowal history says “at random / after successful work,” not manufactured.
- [ ] Passive effect is subtle (+1 or narrative), not sovereign-tier.
- [ ] Brief Wielder Cost present (one breath/one moment), derived from the Passive Effect, and appearing in exactly one file archive-wide.
- [ ] Zero banned strings.
