# M.A.W. Personalize Run — Progress & Recovery Log

> Precaution log for recovering from a session break. Arena patch + this file should be enough to rebuild the state of the M.A.W. personalize run if anything is lost. Timestamps are local (Asia/Bangkok / Jakarta).

---

## 0. What this run is

Task (user directive): expand **every M.A.W. Appearance description** so it is no longer vague. Each `### Appearance` must be **150–200 words minimum** (floor, not ceiling) and must cover **Detail + Shape + Look + Material**. Do the work **per batch, 12 M.A.W. sets at a time**, and update **both the source `.md` record and the generated public `.html` page** so the change is visible on Git even without a live wiki rebuild.

Related standing directive from the same run: every M.A.W. **Weapon (W)** must be a **distinct weapon archetype** — no two W items share a silhouette. Six range bands must be covered: **Close, Short, Medium, Long, Room, Instant**. Catalog: `REFERENCE_SOMNARAK_WIKI/MAW_WEAPON_ARCHETYPES.md`.

---

## 1. Repo / branch to always use

- Repo root: `/home/user/PROJECT.SOMNARAK-WIKI`
- Branch (only branch to work/push on): `arena/01a06714-project-somnarak-wiki`
- **Never merge into `main`.** Push only to `arena/01a06714-project-somnarak-wiki`.
- Do not reset to `main`/`d040588`. Recovery command that is safe:
  `git fetch origin arena/01a06714-project-somnarak-wiki && git reset --hard FETCH_HEAD`

---

## 2. Architecture: there are TWO copies of the Appearance text

This is the key mistake another AI (and this session's first pass) made: only updating one copy.

1. **Source .md record** (the registry / source of truth):
   `REFERENCE_SOMNARAK_WIKI/LORE or REFERANCE/M.A.W. Codex_Set Registry/Registry_XXX_to_YYY/<SET>/SE-<NNN>-<B|C|D>__MAW-<W|S|G>_<Name>.md`
   - `-B` = Weapon (W), `-C` = Suit (S), `-D` = Gift (G)
   - Section: `### Appearance` (some records originally had none; some had a 24–45 word paragraph).
   - The record also carries `Item Registry Code: MAW-W-001-01`.

2. **Public .html page** (what the user counts with a word counter / sees on Git):
   `docs/maw/maw-<w|s|g>-<NNN>-01-<slug>.html`
   - Section: `<h2 id="appearance">Appearance</h2><p>...</p>`
   - Before this session, several pages still showed the **old short text** (e.g. W-001 = 42 words) because they were generated before the `.md` edit.

**The .md must be updated first, then the .html synced from it.** The html page is what the user checks.

---

## 3. How to sync .md → .html (avoid touching SVGs)

`tools/generate_maw_items.py` regenerates pages AND SVGs. Running it with `--force` would clobber the hand-designed weapon SVGs, so DO NOT use it for the batch sync. Instead update the html `Appearance` `<p>` directly, using the `.md` text as the source:

- Match the page by registry code:
  `<dt>Registry code</dt><dd>MAW-<W|S|G>-<NNN>-01</dd>`
- Replace:
  `<h2 id="appearance">Appearance</h2><p>OLD</p>`
  with the escaped `.md` text.
- If the page has NO Appearance section at all (W-019, W-021 previously), insert:
  `<h2 id="appearance">Appearance</h2><p>...</p>`
  immediately before `<h2 id="extraction-or-bestowal">`.
- Escape with `html.escape(text, quote=True)`.

Verification after each batch:
- For all batch items, extract `.md` Appearance text and the `.html` `<p>` text, `unescape` the html, collapse whitespace, and assert they are byte-identical.
- Assert word count is 150–200+ (count with whitespace-split; em dashes may raise the number in some counters, which is safe).

---

## 4. Status of the first completed batch (12 sets)

Sets: **001, 002, 005, 007, 009, 010, 011, 014, 015, 016, 019, 021**
Items: 12 sets × (Weapon + Suit + Gift) = **36 records** and **36 html pages**.

| Item | What happened |
|---|---|
| Source `.md` | 22 records had a 24–45 word Appearance → expanded. 14 records had NO Appearance (009-C, 010-C, 011-C, 014-C, 015-C, 016-B/C/D, 019-B/C/D, 021-B/C/D) → section inserted. All now 150–177 words. |
| Public `.html` | 34 pages were text-replaced with the expanded paragraph; W-019 and W-021 had no Appearance heading → section inserted before Extraction/Bestowal. All 36 pages now 150–177 words. |
| md↔html match | 36 / 36 exact matches. |
| Weapon redesigns | W-001 Greatsword, W-002 Box Maul, W-005 Talon Claw, W-007 Survey Staff, W-009 Shuttle-Razor Lens, W-010 War Sledge, W-011 Katana, W-014 Prism Astral Item, W-015 Balance Cannon, W-016 Compass Chakram, W-019 Chain Flail, W-021 Rapier — distinct silhouettes, six range bands. |

### Commits on the branch
- `019d5e7` — weapon redesign: 12 distinct archetypes across six range bands + `REFERENCE_SOMNARAK_WIKI/MAW_WEAPON_ARCHETYPES.md`
- `5c9e5d0` — expand `.md` Appearance to 150–200 words for the 36 records
- `b93d520` — publish the expanded Appearance into the 36 `docs/maw/*.html` pages

### File paths touched (md)
`Registry_001_to_007/{001_Orphaned_Bell,002_Grieving_Colossus,005_Smothering_Mother,007_Brume}`, `Registry_009_to_015/{009_Memory_Weaver,010_Convergence,011_Whispering_Walls,014_Debt_Eater,015_Debt_Scale}`, `Registry_016_to_031/{016_Echo_Compass,019_Inherited_Debt,021_Hollow_Choir}` → each set's `SE-0NN-B/C/D` records.

### Recovery test that worked
While doing the first pass, an error left the `.html` pages still at 42 words while the `.md` was correct. Fix was: update `.md` first, then sync `.html` (Section 3). The user's check was on the public `.html`, not the `.md`.

---

## 5. Next batch (in progress)

Next 12 sets by registry order, excluding already-done sets. The same procedure applies:
1. Read each set's `-B`/`-C`/`-D` record fully (RULE 0: read page + source first).
2. Write/grow `### Appearance` to 150–200+ words, personalized from that record's element, grade, existing short appearance, ability, limit, cost, history, set resonance. Must cover Detail + Shape + Look + Material.
3. Apply to the `.md` record (replace existing paragraph or insert the section before the first `### Ability`-type heading).
4. Sync to `.html` (Section 3), insert Appearance heading where missing.
5. Verify md↔html match + word floor.
6. Do NOT touch SVGs / do NOT run `generate_maw_items.py --force`.
7. Commit + push only to `arena/01a06714-project-somnarak-wiki`.

If a later batch insert drops the `### ` from the following ability heading, restore it (regex: `\n\n(?!###)(Ability|Protective Ability|Signature Ability|Gift Effect|GIFT EFFECT|Incident Record|History Record|Wearer Cost|Bearer Cost) ` → `\n\n### \1 `). And clean any stray double period from appended sentences (`\.\s*\.\s*` → `. `).

---

## 6. Batch 2 (sets 025, 031, 032, 033, 036, 041, 042, 043, 044, 048, 051, 054)

Status: **done**. Same 36-record + 36-page procedure. All records originally had NO Appearance section, so every `### Appearance` in `.md` was inserted, then synced to `.html` (`22` pages replaced, `14` pages inserted because the Weapon pages had no Appearance heading).

- Word counts after fixes: **150–175** on all 36 (`.md`), identical on `.html`.
- md↔html parity: **36 / 36 exact**.
- Two gotchas hit and fixed in this batch:
  1. Inserting `### Appearance` into records that already had `### Ability`-style headers dropped the `###` from the next header. Fix = regex restore `\n\n(?!###)(Ability|Protective Ability|Signature Ability|Gift Effect|GIFT EFFECT|Incident Record|History Record|Wearer Cost|Bearer Cost) ` → `\n\n### \1 `.
  2. The `SE-044` records use `## IDENTITY & BINDING` / `## CORE STATISTICS` instead of `### Ability`, so insert `### Appearance` before `## CORE STATISTICS`.
  3. A verification pass that stops at the next `###` header revealed true word counts (131–148) after the header fix — the earlier higher counts had swallowed the ability text. Added one lore-consistent closing sentence per record to reach ≥150.

### Files touched (Batch 2)
Registry dirs: `Registry_016_to_031/025_*`, `Registry_043_to_055/{031..044,048,051,054}*` sets (SE-xxx-B/C/D `.md`), plus the matching `docs/maw/maw-<code>-...html` pages.

## 7. Batch 3 (sets 055, 061, 062, 063, 071, 073, 077, 081, 088, 091, 092, 099)

Status: **done**. All 36 records had no Appearance section; inserted `### Appearance` into each `.md` (154–168 words) and synced to `.html` (12 replaced, 24 inserted — the Weapon pages had no Appearance heading). md↔html parity 36/36. No SVGs touched. Same gotchas from batch 2 applied (inserted `###` headers restored; word counts measured correctly after header fix; supplements added to reach 150+).

## 8. Snapshot of this log's creation

- Log created: session while on branch `arena/01a06714-project-somnarak-wiki`, after the first 12-set batch (and its html sync) was committed and pushed.
- Worktree at creation: clean except `_batch_previews/` (scratch, untracked).
- Latest remote commit at creation: `b93d520`.
- Batch 1 commits: `019d5e7` (weapons + archetype catalog), `5c9e5d0` (`.md` appearance), `b93d520` (`.html` appearance sync).
- Batch 2 commits: `cb8a687` (36 `.md` + 36 `.html` for sets 025–054 + this log).
- Batch 3 commits: `7f4c476` (36 `.md` + 36 `.html` for sets 055–099 + this log).

## 9. Batch 4 (sets 100, 101, 102, 103, 105, 106, 108, 115, 119, 120, 125)

Status: **done**. Set 111 is entity-only (`SE-111-A__SIDE_CODEX_The_Final_Door.md`, no W/S/G items), so batch 4 = 11 sets / **33 records** instead of 36.

- All 33 records had **no** `### Appearance` section → inserted into each `.md` (150–177 words), then synced into the matching `docs/maw/maw-*-NNN-01-*.html` page (all inserted after the Overview paragraph, before Extraction or Bestowal).
- md↔html parity: **33 / 33 exact** after normalizing HTML entity encoding (`&#x27;` ↔ `'`, `&amp;` ↔ `&`).
- Word floor: **min 150 / max 177** on both `.md` and `.html`.
- Same batch-3 gotchas applied: inserted `###` headers restored (33/33); short paragraphs supplemented with one lore-consistent closing line to reach ≥150 (32 supplemented, 1 was at 150).
- No SVGs touched.

### File paths touched (Batch 4)
Registry dirs:
- `Registry_099_to_103/{100_Unsaid_Blossoms,101_Emberling,102_Dancing_Chains,103_Frozen_Veil}`
- `Registry_105_to_115/{105_Lonely_Giant,106_I_Alone_Crossed,108_Animus,115_Remembrance}`
- `Registry_119_to_127/{119_Homeless_Sorrow,120_Redcage,125_Deja_Vu}`

Each set's `SE-NNN-B/C/D` `.md` record plus the matching `docs/maw/maw-<w|s|g>-NNN-01-*.html` page.

## 10. Batch 5 (sets 126, 127, 130, 135, 140, 145, 150, 151, 152, 155, 156, 157)

Status: **done**. The registry order does not use every integer (sets 128, 133, 142, 147, 153 do not exist), so batch 5 took the next 12 item-bearing sets in registry order: 126, 127, 130, 135, 140, 145, 150, 151, 152, 155, 156, 157 — **36 records**.

- These records use a **different schema** from batches 1–4: `## ITEM IDENTITY`, `## EXTRACTION & BINDING` / `## ACQUISITION & BINDING`, `## CORE STATISTICS` / `## PROTECTION STATISTICS` / `## GIFT STATISTICS`, and `## COMBAT FILE` / `## PROTECTIVE FILE` / `## EFFECT FILE`.
- Inserted `## Appearance` (top-level `##`, matching the record's own structure) before the first statistics header in each `.md` (36/36). Word counts: **157–205** (floor 150 met; a few slightly exceed 200, which the directive permits).
- Synced into the matching `docs/maw/maw-*-NNN-01-*.html` page (36/36 inserted after Overview, before Extraction or Bestowal). md↔html parity: **36 / 36** after normalizing `&#x27;`/`&amp;`.
- Gotcha hit and fixed in this batch: the insertion helper that removed the `## ` prefix from the following statistics header (e.g. `## CORE STATISTICS` → ` CORE STATISTICS`), which inflated the measured word count and broke the appearance/extraction boundary. Fix = regex restore `(?m)^ (PROTECTION STATISTICS|CORE STATISTICS|GIFT STATISTICS)$` → `## \1` on all 36, then re-sync the `.html` paragraphs.
- No SVGs touched.

### File paths touched (Batch 5)
Registry dirs:
- `Registry_119_to_127/{126_Anonym,127_Mirror_of_Broken}`
- `Registry_130_to_150/{130_Deteriorata,135_Rem,140_Weeping_Willow,145_Briar,150_Risus}`
- `Registry_151_to_157/{151_Border_Tree,152_Doorway_to_Nowhere,155_Harbinger,156_Deadline,157_Torpor}`

Each set's `SE-NNN-B/C/D` `.md` record plus the matching `docs/maw/maw-<w|s|g>-NNN-01-*.html` page.

## 11. Next batch
Batch 6 next 12 item-bearing sets in registry order, continuing after 157: `159, 160, 165, 168, 169, 170, 175, 176, 180, 184, 185, 189` (12 sets; verify each has B/C/D records).

> NOTE (2026-09-04): the Appearance-expansion arm of this run was completed in a later session on branch `arena/01a06ba5-project-somnarak-wiki` (batches 6–20, all 291 in-scope sets; legacy sets cleared and 1000-series deferred by owner ruling — see `SESSION_BREAK_PRECAUTION.md` §6). The weapon-SVG remake arm continues below.

---

## 12. Weapon SVG remake — Batch 2 (W-025, 031, 032, 033, 036, 041, 042, 043, 044, 048, 051, 054)

Session: branch `arena/01a06ba5-project-somnarak-wiki`, 2026-09-04.

Status: **done**. The next 12 W items after the batch-1 dozen (in `docs/assets/art/maw/` numeric order) were redesigned by hand from each page's own Appearance paragraph — each is a distinct silhouette; no `generate_maw_items.py` involvement.

| Item | Archetype | Band |
|---|---|---|
| W-025 The Silence Lens | Lens Buckler | Close |
| W-031 The Witness Requiem | Estoc | Long |
| W-032 The Judgment Fang | Kukri Cleaver | Short |
| W-033 The Guardian Lens | Framed Pavise Lens | Medium |
| W-036 The Hourglass Maul | Hourglass Maul | Room |
| W-041 The Tear Requiem | Tear Dagger | Short |
| W-042 The Fury Fang | Ring Talon | Close |
| W-043 The Silence Lens | Signal Loupe | Instant |
| W-044 The Dawn of Requiem | Sabre | Medium |
| W-048 The Singing Requiem | Song Scimitar | Medium |
| W-051 The Joy Lens | Ray Loupe | Instant |
| W-054 The Void Maul | Dish Maul | Room |

- Catalog extended with archetypes 18–21 (Lens/Loupe, Curved Blade, Hooked Blade, Shield-Weapon) in `MAW_WEAPON_ARCHETYPES.md`; mapping table extended to 24 items.
- Element palettes preserved per item (Void = grey/pale, Lament = blue, Grudge = crimson, Weight = amber/black); frame/badge chrome matches batch-1 format.
- Visual check: all 12 rendered via `tools/render_maw_svg.mjs` (needs `npm install --no-save @resvg/resvg-js` first — not committed) and reviewed as a contact-sheet grid; all silhouettes distinct from each other and from batch 1.
- Gates: `audit_svg_compositions.py` PASS (1284 XML files, cross-subject composition checks), `audit_site_structure.py` PASS.

## 13. Weapon SVG remake — Batch 3 (W-055, 061, 062, 063, 071, 073, 077, 081, 088, 091, 092, 099)

Status: **done** (same session, 2026-09-04). Same procedure as §12; each SVG hand-designed from its page's Appearance paragraph.

| Item | Archetype | Band |
|---|---|---|
| W-055 The Tear Requiem | Tear Stiletto | Short |
| W-061 The Burden Maul | Vessel Maul | Room |
| W-062 The Resentment Fang | Falx | Medium |
| W-063 The Denial Lens | Caliper Lens | Instant |
| W-071 The Gentle Requiem | Round-Edge Glaive | Long |
| W-073 The Duty Fang | Squared Warbrand | Medium |
| W-077 The Shadow Lens | Lens Pistol | Instant |
| W-081 The Hollow Lens | Sceptre Lens | Long |
| W-088 The Sorrow Requiem | Cruciform Longsword | Medium |
| W-091 The Crown of Requiem | Crown Coil Blade | Room |
| W-092 The Burning Fang | Falchion | Medium |
| W-099 The Dancing Fang | Notched Dao | Short |

- Catalog extended with archetypes 22–23 (Glaive/Polearm Blade, Exotic/Transforming) plus family-variant notes; mapping table now 36 items.
- Contact-sheet rendered and reviewed; all distinct. SVG + structure gates PASS.

## 14. Weapon SVG remake — Batch 4 (W-100, 101, 102, 103, 105, 106, 108, 115, 119, 120, 125, 126)

Status: **done** (same session, 2026-09-04). Same procedure; each SVG hand-designed from its page's Appearance paragraph.

| Item | Archetype | Band |
|---|---|---|
| W-100 The Unsaid Requiem | Petal Blade | Short |
| W-101 The Ember Requiem | Ember Sidesword | Medium |
| W-102 The Dancing Fang | Link Cleaver | Short |
| W-103 The Cold Lens | Hex Frost Lens | Instant |
| W-105 The Giant's Maul | Round Grand Maul | Room |
| W-106 I Alone Crossed Requiem | Bridge Greatblade | Long |
| W-108 The Trace Fang | Thread Sai | Close |
| W-115 The Memory Lens | Gimbal Lens | Instant |
| W-119 The Shadow Lens | Lantern Lens | Medium |
| W-120 The Cage Fang | Basket Cutlass | Medium |
| W-125 The Returning Lens | Shutter Lens | Instant |
| W-126 The Melting Lens | Glass Leaf Blade | Short |

- Mapping table now 48 items. Contact sheet reviewed; all silhouettes distinct. SVG + structure gates PASS.

## 15. Weapon SVG remake — Batch 5 (W-127, 130, 135, 140, 145, 150, 151, 152, 155, 156, 157, 159)

Status: **done** (same session, 2026-09-04). Same procedure; each SVG hand-designed from its page's Appearance paragraph.

| Item | Archetype | Band |
|---|---|---|
| W-127 The Broken Maul | Split-Head Maul | Room |
| W-130 The Saint's Maul | Stone Orb Maul | Room |
| W-135 The Warm Requiem | Kris Wave Blade | Short |
| W-140 The Willow Requiem | Willow-Leaf Saber | Medium |
| W-145 The Thorn Fang | Thorn Sickle | Short |
| W-150 The Laughter Requiem | Main-Gauche | Close |
| W-151 The Border Root | Root Cudgel | Short |
| W-152 The Wandering Requiem | Cane Sword | Medium |
| W-155 The Shadow Maul | Wedge Maul | Room |
| W-156 The Deadline Maul | Clock Maul | Room |
| W-157 The Sleeping Maul | Bell Maul | Room |
| W-159 The Frozen Fang | Shard Fang | Short |

- Mapping table now 60 items. Contact sheet reviewed; all silhouettes distinct. SVG + structure gates PASS.

## 16. Next weapon batch
Batch 6 = next 12 W SVGs in numeric order after 159 (run `ls docs/assets/art/maw/maw-w-*-01.svg | grep -oE 'maw-w-[0-9]+' | sed 's/maw-w-//' | sort -n | awk '$1>159 && $1<1000' | head -12` for the exact list). Same procedure: read each page's Appearance paragraph → assign an unused archetype/variant (extend the catalog if needed) → hand-write the SVG in the batch-1 format → render + contact-sheet review → gates → update mapping table + this log → commit + push.
