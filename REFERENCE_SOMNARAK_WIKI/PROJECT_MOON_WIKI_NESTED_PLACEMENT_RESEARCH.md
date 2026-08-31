# Project Moon wiki nested placement research

**Date:** 2026-08-30  
**Purpose:** Find where Somnarak’s 80%+ source files belong by reading nested pages on six analog wikis — not only homepages.  
**Rule used:** one source chapter → one encyclopedia article (or a hub + list). Never paste a whole manuscript onto a page that is about something else.

Wikis read:

| Game | wiki.gg | Fandom |
|---|---|---|
| Lobotomy Corporation | https://lobotomycorporation.wiki.gg/ | https://lobotomycorp.fandom.com/wiki/ |
| Library of Ruina | https://libraryofruina.wiki.gg/ | https://library-of-ruina.fandom.com/wiki/Library_Of_Ruina_Wiki |
| Limbus Company | https://limbuscompany.wiki.gg/ | https://limbuscompany.fandom.com/wiki/ |

---

## 1. What these wikis never do

They do **not** put the world bible, the facility manual, and the 50-day script on the same URL.

- A **department / floor** page is only that department (layout, functions, missions, research, that Sephirah’s meltdown). Example: [Control Team](https://lobotomycorporation.wiki.gg/wiki/Control_Team) — Overview, Department Functions, Missions, Research, Sephirah Meltdown. It does not contain Yesod’s story, E.G.O manufacturing, or Days 1–50.
- A **character** page is appearance, personality, story cutscenes, backstory, meltdown. Example: [Malkuth](https://lobotomycorporation.wiki.gg/wiki/Malkuth). Missions live on Missions + Control Team, not as the whole facility manual.
- A **story transcript** is its own hub. Example: [Daily Recordings](https://lobotomycorporation.wiki.gg/wiki/Daily_Recordings) — Day 1 … Day 50 on **one** Story page, linked from [Story](https://lobotomycorporation.wiki.gg/wiki/Story). It is not dumped onto Control Team.
- A **city** page describes the city and **links** districts / Wings. Example: [The City](https://libraryofruina.wiki.gg/wiki/The_City), [The City (Limbus)](https://limbuscompany.wiki.gg/wiki/The_City). District 12 is a subsection + link to L Corp, not a paste of Abnormalities + E.G.O + Sephirot.
- An **equipment** hub explains how gear works and **lists** pieces. Full stats live on the Abnormality (or Identity / E.G.O) article. Example: [Equipment](https://lobotomycorporation.wiki.gg/wiki/Equipment), [List of E.G.O](https://limbuscompany.wiki.gg/wiki/List_of_E.G.O).
- An **ordeals** hub explains the mechanic; each color is a child page. Example: [Ordeals](https://lobotomycorporation.wiki.gg/wiki/Ordeals) → Amber / Crimson / Green / …
- A **list** page is a table (Classification, Portrait, Name, Risk, Damage). Example: Fandom [Abnormalities table on Home](https://lobotomycorp.fandom.com/wiki/Home), wiki.gg [Abnormalities](https://lobotomycorporation.wiki.gg/wiki/Abnormalities) + List.

Somnarak analog of the bad pattern: `PROJECT_SOMNARAK.md` or `The_REVERIE_DIRECTORATE.md` pasted onto SECC, Floor 1, The Maw, etc.

---

## 2. Nested map — Lobotomy Corporation (wiki.gg + fandom)

### Homepage tiles (wiki.gg)

Abnormalities · E.G.O Equipment · Ordeals · Meltdowns · Employees · Missions · Characters · Story  
Right column: **ten department buttons** (Control → Architecture), each a nested article.

Fandom home is an **Abnormality list table** (code, portrait, name, damage, risk, e-boxes, Qliphoth) plus a facility diagram.

### Nested gameplay

| Page | What it contains | What it links out |
|---|---|---|
| [Departments](https://lobotomycorporation.wiki.gg/wiki/Departments) | Facility diagram, layer list, **room types** (Main Room, Containment, Hallways, Elevators) | Each Team article |
| [Control Team](https://lobotomycorporation.wiki.gg/wiki/Control_Team) | This floor only: overview, clerk benefits, continued service, **this team’s 4 missions**, this team’s research, this Sephirah’s meltdown | Malkuth, Missions hub, Research, Abnormalities |
| [Employees](https://lobotomycorporation.wiki.gg/wiki/Employees) | Agents vs Clerks, panic, fear, flavor | **Stats**, Hiring, Departments, Works |
| [Equipment](https://lobotomycorporation.wiki.gg/wiki/Equipment) | How E.G.O is obtained; weapons / suits / gifts; default riot stick | Per-Abnormality gear, Risk Level, Damage Type |
| [Ordeals](https://lobotomycorporation.wiki.gg/wiki/Ordeals) | Dawn/Noon/Dusk/Midnight mechanic | Amber, Crimson, Green, Indigo, Violet, White child pages |
| [Missions](https://lobotomycorporation.wiki.gg/wiki/Missions) | **All teams’ missions in one table hub** | Each Department (duplicate of the mission block also sits on the Team page) |
| [Sephirah Meltdown](https://lobotomycorporation.wiki.gg/wiki/Sephirah_Meltdown) | Core Suppression rules + **one section per Sephirah** | Department + character pages |
| [Abnormalities](https://lobotomycorporation.wiki.gg/wiki/Abnormalities) | Encyclopedia of the species | List of Abnormalities; each specimen article |

### Nested story

| Page | Pattern |
|---|---|
| [Story](https://lobotomycorporation.wiki.gg/wiki/Story) | Hub only: Daily Recordings, Seed of Light, then Sephirot **Dialogues** as separate pages |
| [Daily Recordings](https://lobotomycorporation.wiki.gg/wiki/Daily_Recordings) | Full day-by-day transcript (Day 1–50) on **this one URL** |
| [Malkuth](https://lobotomycorporation.wiki.gg/wiki/Malkuth) | Character: Appearance, Personality, Cutscenes 1–4, Meltdown, Backstory. Not the Control Team room list. |
| Seed of Light | Cosmology / ending — not mixed into Equipment |

### Somnarak mapping (LC)

| LC | Somnarak |
|---|---|
| Abnormalities + List | `entities/index.html` + `entities/list.html` + `se-NNN-*.html` |
| Control Team | `departments/floor-1-neutral-command.html` (this floor only) |
| Information / Extraction / Record / … | Floors 2–8 |
| Departments + Room Types | `departments/index.html` + `facility-room-types.html` |
| Employees + Stats | `mechanics/agent-attributes-and-stats.html` |
| Equipment + default kit | `maw/index.html` + `mechanics/maw-equipment-system.html` + `default-standard-equipment.html` |
| Ordeals hub + color pages | `mechanics/ordeals-framework.html` + `the-four-ordeals.html` |
| Missions hub | missions sit **on each floor** (LC also duplicates them on the Team page) |
| Sephirah Meltdown | `departments/core-suppression-guidelines.html` + `facility-meltdown-procedures.html` |
| Characters / Sephirot | `characters/` Echo-Cores |
| Daily Recordings | `lore/the-cycle-and-absolvohan.html` |
| Seed of Light / Cogito | `lore/the-weeping-river.html` + cosmology (Weeping, not Cogito) |
| Risk / Damage / Works | SECC, Han damage, four work types — **separate mechanics articles** |

---

## 3. Nested map — Library of Ruina (wiki.gg + fandom)

### Homepage

Gameplay column: Guests, **Floors**, Librarians, Invitations, Reception, Emotion Level, Status Effects, Stats, Battle Symbols, Books, Combat Pages, Abnormality Pages, Key Pages, Floor Realization, E.G.O Pages.

Story column: Patron Librarians’ Stories, Small Stories, Key Page Stories, Characters, Abnormalities, Distortions, E.G.O, Locations, Factions.

Fandom home: Quick Links (Invitations / Reception / Library / Floors / Characters) plus **The Library** as a floor list (Angela’s room, Floor of History — Malkuth, …).

### Nested

| Page | Pattern |
|---|---|
| [Floors](https://libraryofruina.wiki.gg/wiki/Floors) | **Hub table**: floor button, story #, Patron Librarian, unlock, Abnormalities on that floor. Each floor is its own article (Floor of History, Floor of Language, …). |
| Floor of History | That floor’s librarians, assignments, Abnormality fights, realization. Not the whole Library manual. |
| [The City](https://libraryofruina.wiki.gg/wiki/The_City) | City overview + **short district stubs** that link to Wing articles (L Corp, R Corp, WARP). |
| Reception / Guests | Operation / invitation — analog of SED/UCD **story arcs**, each guest/office its own page |
| Distortions | Separate from Abnormalities (Somnarak: Fracture / Named Fractures, not SE dossiers) |
| Manual | Game systems, not lore dump |

### Somnarak mapping (LoR)

| LoR | Somnarak |
|---|---|
| Floors hub | `departments/index.html` + facility map |
| Floor of X | `departments/floor-N-*.html` |
| Patron Librarian | Echo-Core character page |
| The City | `locations/district-structure-veil-and-raw.html` + zone pages |
| Reception / Guests / Offices | `factions/the-sed-corps.html`, `the-ucd-strike-force.html` (operation books) |
| Key Pages / Combat Pages | M.A.W. weapons / gifts |
| Distortions | `lore/named-fractures.html`, `mechanics/fracture-and-therapy.html` |
| Organizations | `factions/` |

---

## 4. Nested map — Limbus Company (wiki.gg + fandom)

### Homepage tiles

Identities · Abnormalities · Enemies · Season · Mirror Dungeons · Characters · E.G.O · Banners  
Sinner portraits (Yi Sang …) each open a **character hub**, not a world bible.

### Nested

| Page | Pattern |
|---|---|
| [The City](https://limbuscompany.wiki.gg/wiki/The_City) | Overview, Districts (link), Head, Wings/Nests, Backstreets, Culture, Technology/Singularities, Hazards, History (Smoke War, White Nights). **Links** to Districts, Wings, Taboo, Outskirts — does not paste every Canto. |
| Sinner (Yi Sang, Faust, …) | Character + Identities list. Story cutscenes stay on the **Canto** page. |
| Canto / Intervallo | One long story-operation article (cast, chapters, combat). Analog of SED/UCD arcs. |
| List of Abnormalities / List of E.G.O / List of Identities | Tables. Detail is on the child article. |
| Mirror Dungeon | Game mode — not mixed into The City. |

Fandom home: Identities, E.G.O, Status Effects, Enemies, Abnormalities, Season — same split.

### Somnarak mapping (Limbus)

| Limbus | Somnarak |
|---|---|
| The City | Atlas + cosmology + daily life — **separate** articles |
| District / Nest / Backstreets | Zones A–E, Veil/Raw, Desolate |
| Sinners | Echo-Cores |
| Canto / Intervallo | SED, UCD, Absolvohan day batches |
| Identities / E.G.O lists | `entities/list.html`, `maw/index.html` |
| Singularities | Absolvohan / Cycle mechanics on the Cycle page, not on SECC |
| Taboo | `lore/the-seven-absolute-taboos.html` + Giltong |

---

## 5. Where each 80%+ Somnarak **source file** belongs

Transfer % = how much of **that source file** is on the wiki, not how much of the wiki came from the file.

| Source file (07_Reference) | Size | Analog page type | **Place it here** | Do **not** put it here |
|---|---:|---|---|---|
| `PROJECT_SOMNARAK.md` | 262 KB | The City + nested district/faction/mechanic articles | Split: cosmology, SECC, work types, Han, zones, Maw, factions, taboos, history — **one chapter per URL** | SECC, Floor 1, The Maw, any single “codex” URL |
| `The_REVERIE_DIRECTORATE.md` | 144 KB | Departments + Control Team + Employees + Equipment + Daily Cycle | Floor N = that floor’s rooms/layout/missions; RD faction = what the Directorate **is**; stats/kit = mechanics; Echo-Cores = characters | Entire manual inside Floor 1 “layout” or inside SECC |
| `SOMNARAK_ABSOLOVHAN.md` | 236 KB | **Daily Recordings** (LC Story) + Seed of Light notes | `lore/the-cycle-and-absolvohan.html` as the day-log hub (Day 0, batches, final days). Director’s hidden agenda also on Majin. | Floor pages, SECC, entities hub |
| `SOMNARAK_SED.md` | 104 KB | LoR Reception / Limbus Canto | `factions/the-sed-corps.html` (premise, cast, arcs 1–7) | City dump, RD manual |
| `SOMNARAK_UCD.md` | 122 KB | Canto / Syndicate reception | `factions/the-ucd-strike-force.html` (cast, arcs 1–6) | City dump, Maw page |
| `SOMNARAK_MAW_CODEX.md` | 348 KB | Equipment hub + per-specimen E.G.O | `maw/index.html` (rules/grades) + `maw/maw-*-NNN-*.html` per piece. 13 published sets only. | One 348 KB “all 735 pieces” page |
| `SOMNARAK_ENTITY_CODEX.md` / entity MD | 83 KB+ | Abnormalities + List | `entities/index.html`, `list.html`, `se-NNN-*.html`. 13 of ~288. | SECC page body |
| `SOMNARAK_ENTITY_TALES.md` | 1.2 MB | Key Page Stories / Small Stories | `lore/entity-tales.html` (tales only). Do not paste 1.2 MB onto SE dossiers. | Entity hub, SECC |
| `SOMNARAK_CAST.md` | 92 KB | Minor characters list | `lore/somnarak-name-registry.html` + `characters/` for named operatives | Floor dumps |
| `SOMNARAK_DAILY_LIFE.md` | 32 KB | City culture subsection | `lore/daily-life-in-somnarak.html` | Cosmology page |
| `SOMNARAK_NAME_REGISTRY.md` | 32 KB | Names / glossary | `lore/somnarak-name-registry.html` | SECC |
| `SOMNARAK_NAMED_FRACTURES.md` | 31 KB | Distortions | `lore/named-fractures.html` | Abnormalities list |
| `SOMNARAK_UNKNOWN_CITIES.md` | 31 KB | Outskirts / other Nests | `locations/unknown-cities.html` | Zone C dump |
| `SOMNARAK_FACTION_TECH.md` | 29 KB | Wing tech | `factions/faction-technology.html` | Every faction page |
| `SOMNARAK_DAWN_OF_HOPE.md` | 26 KB | Post-cycle / White Nights analog | `lore/the-dawn-of-hope.html` | Absolvohan day log |
| `SOMNARAK_TABOO_RESONANCE.md` | 25 KB | Taboo / Head ethics | `mechanics/taboo-resonance-mechanics.html` + seven taboos lore | SECC |
| `SOMNARAK_THE_WEEPING.md` | 23 KB | Cogito / river analog | `lore/the-weeping-river.html` | SECC origin dump |
| `SOMNARAK_THE_DESOLATE.md` | 22 KB | Outskirts | `locations/the-desolate.html` | Whole city chapter |
| `SOMNARAK_FACTION_RELATIONS.md` | 21 KB | Organizations | `factions/the-high-council.html` + per-guild pages | P.S.md paste |
| `SOMNARAK_THE_DOORSPEECH.md` | 21 KB | Unique lore article | `lore/the-doorspeech.html` | RD manual |
| `SOMNARAK_CHEONGULA.md` | 19 KB | History incident | `lore/the-cheongula-incident.html` + Maw | SECC |
| `SOMNARAK_ORDEALS_FRAMEWORK.md` | 19 KB | Ordeals hub | `mechanics/ordeals-framework.html` | Floor 1 |
| `SOMNARAK_DREAM_REALM.md` | 18 KB | Distortion / dream | `lore/the-dream-realm.html` | Cosmology dump |
| `SOMNARAK_HAN_RELICS.md` | 16 KB | Tool / gift adjacent | `mechanics/han-relics-and-tools.html` | MAW weapon pages |
| `SOMNARAK_BATTLE_SYSTEM.md` | 11 KB | Reception / clash | `mechanics/resonant-clash-mechanics.html` | City page |
| `SOMNARAK_ENEMY_LIST.md` | 10 KB | List of Enemies | `mechanics/enemy-bestiary.html` | Entity list |
| Character wiki `THE_DIRECTOR.md` etc. | 6–16k words | Malkuth-style character | `characters/the-*-*.html` | Floor layout section |
| Absolvohan PART 1/2/6/9 | short | Daily Recordings slices | Cycle hub (already) + floors only if that day is **that floor’s** incident | All floors |

---

## 6. Page recipe (copy LC Control Team)

A Somnarak **floor** article should look like Control Team, not like Daily Recordings:

1. Overview (this floor, this lead)
2. Department functions / rooms of **this** floor
3. Missions of **this** floor
4. Research / extraction notes of **this** floor
5. Link to Echo-Core character (story cutscenes live there)
6. Link to Core Suppression / meltdown
7. Navigation box to other floors

A Somnarak **SECC** article should look like Risk Level + subject-number decoding, not like The City:

1. Code format
2. Origin / Coherence / Potency / Element / Manifestation
3. Examples (including The Maw’s code)
4. Links: entities hub, list, Han, work types

A Somnarak **Absolvohan** article should look like Daily Recordings:

1. What the Cycle is (short)
2. Day 0, then day batches as TOC anchors
3. Epilogue
4. Links to Majin, Seiyon, Dawn of Hope — **not** the city bible

A Somnarak **SED / UCD** article should look like a Canto / Reception:

1. Premise + cast
2. Arc 1…n (chapters stay on this operation page)
3. Links to zones / factions touched — not a paste of those zone bibles

---

## 7. Nested URLs actually opened for this note

**LC wiki.gg:** Main, Abnormalities (prior session), Control Team, Employees, Missions, Sephirah Meltdown, Story, Daily Recordings, Equipment, Ordeals, Characters, Departments, Malkuth.

**LC fandom:** Home (facility diagram + Abnormality list table).

**LoR wiki.gg:** Main, Floors, The City.

**LoR fandom:** Home (Library floor directory + mechanics directory).

**Limbus wiki.gg:** Main, The City.

**Limbus fandom:** Home (Identities / E.G.O / Abnormalities / Enemies tiles).

---

## 8. Status vs this map (after 2026-08-30 splits)

| File | Status |
|---|---|
| `PROJECT_SOMNARAK.md` | Split onto chapter URLs. SECC is classification-only. |
| `The_REVERIE_DIRECTORATE.md` | Floor pages = that floor; RD faction = Directorate identity; stats/kit/ordeals/incidents/cores moved. |
| `SOMNARAK_ABSOLOVHAN.md` | Correct home: Cycle / Absolvohan hub (LC Daily Recordings). Keep days here, not on floors. |
| `SOMNARAK_SED.md` / `SOMNARAK_UCD.md` | Correct home: those faction-operation pages (Canto / Reception). |
| `SOMNARAK_MAW_CODEX.md` | Only 13 published sets on `maw/` — same fraction rule as 13/288 entities. Do not dump 735 rows on one page. |
| Entity corpus | 13/288 dossiers. Hub + list, not the world bible. |
