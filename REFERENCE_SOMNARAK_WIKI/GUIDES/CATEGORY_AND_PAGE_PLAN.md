# Category and page plan

**Date:** 2026-08-30  
**Updated quality floor:** 2026-08-31

**Rule:** every public article is a real encyclopedia page with at least **200 meaningful editorial words**; this is a floor, not a ceiling, and the normal target remains **300+** wherever source depth permits. Do not invent stub URLs for redundancy. One source chapter → one fitting category page. See `CONTENT_AND_VISUAL_STANDARDS.md` for the binding count and visual-identity rules.

This plan is written **before** HTML, from:

- `LORE or REFERANCE/07_Reference/` (34 source books)
- `01_Sorrow_Entities/` (specimen dossiers)
- `02_Hope_Transformation/` (14 Hope entities)
- `03_Unknown_Entities/` (7 uncatalogued SEs + Book of Regressor dramaturgy)
- `04_Ordeals/` (60 named watches)
- `CHARACTER_WIKI/` (9 Echo-Cores)
- Nested LC / LoR / Limbus wiki map in `PROJECT_MOON_WIKI_NESTED_PLACEMENT_RESEARCH.md`

---

## 1. Categories that fit (LC analog)

LC wiki.gg does not dump the world bible onto Control Team. It uses **category hubs** that list child articles.

| Category (Somnarak) | LC / LoR / Limbus analog | Hub URL | Child articles |
|---|---|---|---|
| **Sorrow Entities** | Abnormalities | `entities/index.html` + `list.html` | `se-NNN-*.html` (13 of ~288 published) |
| **Hope Transformations** | Unique species (not Abnormalities; closest: Limbus E.G.O / Identities as a **separate tile**) | `entities/hope-transformations.html` | HT-001…012, Trinity of Dawn, Hand of Hope |
| **Unknown Entities** | Unidentified / Distortion-adjacent specimens | `entities/unknown-entities.html` | 7 uncatalogued SEs |
| **Entity groups** | Abnormality groups (Birds, Magical Girls) | `entities/entity-groups-and-chains.html` | one article, not four stubs |
| **Ordeals** | [Ordeals](https://lobotomycorporation.wiki.gg/wiki/Ordeals) → Amber / Crimson / Green… | `mechanics/ordeals-framework.html` | **5 color pages**, not 60 watch stubs |
| **Four Watches** | Dawn / Noon / Dusk / Midnight (time axis) | `mechanics/the-four-ordeals.html` | time axis only; links to colors |
| **SECC** | Risk Level decoding | `mechanics/secc-classification-system.html` | classification codes only |
| **Departments / Floors** | Control Team | `departments/floor-N-*.html` | that floor’s rooms / missions |
| **Characters** | Malkuth | `characters/the-*-*.html` | Echo-Cores + named operatives |
| **Story / Cycle** | Daily Recordings | `lore/the-cycle-and-absolvohan.html` | keep days on this hub |
| **SED / UCD** | Canto / Reception | faction operation pages | keep arcs there |
| **M.A.W.** | Equipment + List of E.G.O | `maw/index.html` | per-piece pages for published sets |
| **The City / Zones** | The City → Districts | `locations/` | zone articles, not cosmology dumps |
| **Book of Regressor** | Small Stories / Key Page Stories | `lore/the-book-of-regressor.html` | dramaturgy, not an SE dossier |

**Do not create:** 60 separate ordeal HTML files, 529 duplicate SE filenames, or 1,196 M.A.W. registry dumps. Those are source files, not wiki categories.

---

## 2. Word-count rule

| Kind of page | Words |
|---|---|
| Reject | **under 200 meaningful editorial words** after shared chrome is excluded |
| Minimum qualifying page | **200–299** only when the subject is complete, distinct, source-supported, and non-generic |
| Default encyclopedia article | **300+** wherever the source supports that depth |
| Operation / transcript hub | may be as long as the source requires (Daily Recordings analog) |

The 200-word requirement applies to every public HTML page, including hubs, lists, maps, downloads, project pages, and the 404 page. It must not be reached with filler, repeated navigation, duplicated prose, or unrelated source material. It is a floor, never a target or ceiling.

Hope Transformation source files are 2,000–2,600 words. Wiki articles take **Appearance + Origin + Function + Bearer** (~300–500 words), not the full tale/testimony/record dump.

---

## 3. Source folder → wiki category

### `01_Sorrow_Entities` (529 md, many name-duplicates)

**Category:** Sorrow Entities.  
**Now:** 13 public dossiers. Do not paste the other ~275 onto SECC or Floor 1.

### `02_Hope_Transformation` (14 md) — **missing category**

| File | Wiki page | Bearer |
|---|---|---|
| HT-001 Guiding Light | `entities/ht-001-the-guiding-light.html` | Yeonhwa |
| HT-002 Shield of Dawn | `entities/ht-002-the-shield-of-dawn.html` | Taeho |
| HT-003 Gentle Flame | `entities/ht-003-the-gentle-flame.html` | Sooah |
| HT-004 Reuniting Spark | `entities/ht-004-the-reuniting-spark.html` | Duri |
| HT-005 Defiant Ember | `entities/ht-005-the-defiant-ember.html` | Sero |
| HT-006 Eternal Warmth | `entities/ht-006-the-eternal-warmth.html` | Sarang |
| HT-007 Silent Vigil | `entities/ht-007-the-silent-vigil.html` | Midnight |
| HT-008 Healing Touch | `entities/ht-008-the-healing-touch.html` | Seol |
| HT-009 Burning Hope | `entities/ht-009-the-burning-hope.html` | Hwaran |
| HT-010 Living Memory | `entities/ht-010-the-living-memory.html` | Mori |
| HT-011 Shared Glass | `entities/ht-011-the-shared-glass.html` | Bong |
| HT-012 Standing Witness | `entities/ht-012-the-standing-witness.html` | Chunhwa |
| HT-V-HC-001 Trinity of Dawn | `entities/ht-v-hc-001-the-trinity-of-dawn.html` | Convergence-class Hope |
| HT-V-HH-001 Hand of Hope | `entities/ht-v-hh-001-the-hand-of-hope.html` | City-scale Hope |

Hub: `entities/hope-transformations.html` (Limbus Identities-style list hub).

### `03_Unknown_Entities` (8 md) — **missing category**

| File | Wiki page |
|---|---|
| SE-N-IIIβ-247 The Undelivered Thanks | `entities/unk-247-the-undelivered-thanks.html` |
| SE-C-IIIγ-248 The Unconsoled | `entities/unk-248-the-unconsoled.html` |
| SE-N-IVγ-250 The Extinguished | `entities/unk-250-the-extinguished.html` |
| SE-C-IVδ-251 The Unspoken Line | `entities/unk-251-the-unspoken-line.html` |
| SE-N-IVδ-901 The Mewgical Girl | `entities/unk-901-the-mewgical-girl.html` |
| SE-N-IVδ-902 The Repeated Survivor | `entities/unk-902-the-repeated-survivor.html` |
| SE-N-IIγ-903 The Music Box of Agony | `entities/unk-903-the-music-box-of-agony.html` |
| Book of Regressor (dramaturgy) | `lore/the-book-of-regressor.html` — **Story**, not an SE |

Hub: `entities/unknown-entities.html`.

### `04_Ordeals` (60 md) — **do not make 60 pages**

LC pattern: one **color** article lists Dawn/Noon/Dusk/Midnight variants.

Canon colors (from `SOMNARAK_ORDEALS_FRAMEWORK.md`):

| Color | Han | Theme | Wiki page |
|---|---|---|---|
| BLUE | Lament | Mourning Host | `mechanics/ordeal-blue.html` |
| BLACK | Weight | Crushing Tide | `mechanics/ordeal-black.html` |
| PALE | Void | The Fading | `mechanics/ordeal-pale.html` |
| GREY | Grudge | Resentful March | `mechanics/ordeal-grey.html` |
| PURPLE | Raw Han | The Corruption | `mechanics/ordeal-purple.html` |

Times (First / Second / Third / Tide Watch) stay on `the-four-ordeals.html` as the **time axis**, with links into the five color pages.

### `07_Reference` (34 md)

Already mapped in the nested-placement research. Keep:

- Absolvohan → Cycle hub (Daily Recordings)
- SED / UCD → those faction pages (Cantos)
- Maw Codex → maw/ (13 published sets)
- Cast → characters + name registry
- Entity groups (`SOMNARAK_ENTITIES.md`) → **new** `entities/entity-groups-and-chains.html`

### `CHARACTER_WIKI` (9 md)

Already on Echo-Core character pages. Do not paste onto floors.

### `M.A.W. Codex_Set Registry` (1,196 md)

Equipment hub + per-piece pages for the **published** 13 sets. Not a 1,196-page dump.

---

## 4. Footer categories (every new article)

Same idea as LC `Categories:` at the bottom of Control Team / Malkuth:

```
Categories: Hope Transformations | Dawn Initiative | Sorrow Entities
Categories: Unknown Entities | Sorrow Entities | SECC
Categories: Ordeals | BLUE | Mechanics
```

---

## 5. What this turn implements

1. This plan file.
2. Hope Transformations hub + 14 real articles (300+ words from source).
3. Unknown Entities hub + 7 real articles.
4. Entity groups article.
5. Five ordeal **color** articles + hub links.
6. Book of Regressor as a Story page.
7. Entity-hub tabs so the new categories are reachable (LC Abnormalities / List pattern).
8. Search index entries + the single wiki zip.

Not this turn: 275 remaining SE dossiers, 1,196 M.A.W. registry files, splitting Absolvohan/SED/UCD (those already sit on the analog hubs).
