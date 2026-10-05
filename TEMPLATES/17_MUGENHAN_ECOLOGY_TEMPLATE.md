# 17 — MUGENHAN ECOLOGY TEMPLATE

**Template ID:** `T-17-MUGEN`  
**Generates:** `SOMNARAK-WORLD/Mugenhan_Ecology/{{FILE}}.md`  
**Authority:** `SOMNARAK-WORLD/Mugenhan_Ecology/README.md` + `MUGENHAN_ECOLOGY_OVERVIEW.md` + Laws 4,7

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Mugenhan (무겐한) is the planet**, not a district. Ecology has 3 tiers: Tier 1 Mundane (15 Canonical Species) / Tier 2 Sorrow-Infused Organisms (6 Sorrow Beasts/Plants) / Tier 3 Mortal Sorrow Creatures (6 MSF, mortal but Han-tainted). Do not file Tier 1/2/3 as SE — SEs are Tier 4 (immortal crystallized sorrow).
- **Geography is terrain** — Crystal Peaks, Sea of Glass, Consoling Ocean, Numbing Tundra, Sorrow Lake, Maw strata all belong in `SOMNARAK_GEOLOGY.md`, not ecology.
- **Ecology codices are encyclopedic, not dossier.** Each file covers multiple species/organisms with morphology, habitat, Han tolerance, and Directorate handling note.

---

## FILE NAMING

```
SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_{{TOPIC}}.md
```

Example: `MUGENHAN_PLANETARY_FLORA_AND_FAUNA.md`

---

## SCAFFOLD

~~~markdown
# Mugenhan Ecology — {{TITLE_EN}} — {{KOREAN_TITLE}}

> *“{{Epigraph — what the land remembers when no one is looking.}}”*

**Codex ID:** `MUGEN-{{TIER}}-{{NUM}}`  
**Tier:** {{1 Mundane / 2 Sorrow-Infused / 3 Mortal Sorrow Creature}}  
**Compiler:** {{Research Lead Ayshuk / Ecology Survey Team}}  
**Date:** Year {{4,23x}} — Dawn Initiative  
**Strata:** {{Surface / Subterranean / Desolate / Deep Abyss}}

## I. TAXONOMY & CANONICAL COUNT

{{State tier and how many species this file covers — e.g., “Tier 1: 15 Canonical Mundane Species (baseline, no Han).” Do not exceed canonical totals without Directorate amendment.}}

## II. SPECIES / ORGANISM ENTRIES

### {{Species 1 English Name}} — {{Korean Name}} (  {{Hangul}}  / {{Romaja}} [{{English}}] )

| Field | Record |
|---|---|
| **Tier** | {{1/2/3}} |
| **Morphology** | {{Size, form, color, distinguishing mark}} |
| **Habitat** | {{Stratum/sector/zone — link geology if terrain-relevant}} |
| **Han Tolerance** | {{None / Low / High / Tainted — mMb range}} |
| **Diet / Behavior** | {{Herbivore / scavenger / burrower / photosynthetic}} |
| **Directorate Note** | {{Handling — edible, quarantine, M.A.W. irrelevant, Veil filter spec}} |

{{1 paragraph natural history — where it lives, what it does when Han rises, what it means to city dwellers.}}

*(Repeat block for each species in file — 3–6 per codex file typical.)*

## III. STRATA DISTRIBUTION & FIELD INTEGRATION

{{Where Tier sits in world: Tier 1 across city strata, Tier 2 near Veil leaks, Tier 3 in Maw periphery / Desolate.}}

## IV. CROSS-REFERENCES

- Geology (terrain): `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_GEOLOGY.md`
- Infection/Grief physics: `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_HAN_RELICS.md`
- Entity taxonomy (Tier 4 SE): `SOMNARAK-WORLD/Sorrow_Entities/README.md` (do not conflate)
~~~

---

## VALIDATION CHECKLIST

- [ ] Tier 1/2/3 species ARE NOT filed as SE (Tier 4 is SE).
- [ ] Canonical totals respected (15 / 6 / 6) — expansion beyond requires note.
- [ ] Terrain references point to geology codex, not duplicated as entity.
- [ ] Han tolerance and Directorate handling per species.
- [ ] Zero banned strings; encyclopedic tone, not dossier.
