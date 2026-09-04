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

## 15b. OWNER CORRECTION (2026-09-04) — personalization standard, batch 2 REDONE

Owner review of batches 2–5: **rejected as too same-shape / too template.** Ruling:
- The reference standard is the **approved 001–021 weapons** (other-AI batch 1, commit `019d5e7`): every weapon is an *illustration* — its own composition, its own angle/pose, its own background gradient tuned to the item, and story props from the Appearance text (W-019's flail head swings off-axis with hinged links; W-011's katana sweeps diagonally with a hamon line; W-014's prism floats with an orbit halo and shard moons).
- **NOT allowed:** the vertical centered blade-guard-grip-pommel template, one shared header/palette block, or archetype-only variation. That is generation, not personalization.
- Work in **1 batch of 12 at a time**, then stop for owner review before the next.
- Batch 2 (W-025…054) was REDONE to this standard (`docs/assets/art/maw/maw-w-0{25,31,32,33,36,41,42,43,44,48,51,54}-01.svg`): each has a unique layout (W-025 fist-buckler with dying sound arcs; W-031 full-diagonal estoc with witness iris in the guard; W-032 massive forward-bent cleaver with cho notch; W-033 pane braced in a drawn doorway; W-036 tilted mid-swing with falling sand grains; W-041 tear hanging point-down from the grip; W-042 talon curling across frame with ember specks and fist ring; W-043 loupe with silenced ripple sector; W-044 sabre rising over a dawn horizon; W-048 scimitar with light-filled groove and note-motes; W-051 loupe reading a cracked smiling mask; W-054 dish face turned to the viewer swallowing motes).
- **Batches 3–5 (W-055…159) remain in the rejected template style and must be redone the same way, 12 per review round.**

## 15c. Batch 3 REDONE to the personalization standard (2026-09-04, after owner approved the batch-2 redo)

W-055…099 redrawn as individual illustrations, each staged from its own Appearance text:
- W-055 Tear Requiem — rising diagonal stiletto, teardrop guard wrapping down, sorrow-glow pooled at the tip, dim sheath left behind.
- W-061 Burden Maul — tilted open bowl receiving falling weight-blocks, rim glowing on the target side, burden line arcing out, grey-dot squared pommel.
- W-062 Resentment Fang — falx leaning/straining toward drawn enforcement pillars, obligation chain-links etched along the blade, finger-notch grip, warming pommel block.
- W-063 Denial Lens — hand disc mid-cut severing a branded command mark's tether, thumb-rest notch, tether ring, untouchable voluntary bond below.
- W-071 Gentle Requiem — blunt round-edged glaive, centre seam FORKING into green heal / red harm lines, willing open palm giving a pain wisp, open ring pommel.
- W-073 Duty Fang — squared warbrand planted point-down as a wall between a jagged threat and a small sheltered figure, glowing spine inscription, ring pommel.
- W-077 Shadow Lens — opaque grey disc with opened centre aperture firing the pale strike that knocks a label tag loose; three spoken-fact tally marks + witness profile; wooden rest.
- W-081 Hollow Lens — lens lifted from its open white-lined case, dashed directional seam + pierce line interrupting a hooked identity-pull.
- W-088 Sorrow Requiem — narrow diagonal blade with a low-note wave travelling the flat, blue moisture beads climbing the grip, struck target rings.
- W-091 Crown of Requiem — closed circlet with inward-tucked points + relief-contact inset figure, blade line half-unfurled with floating question-mark motes.
- W-092 Burning Fang — blade launching a crimson pierce line that cracks a gag-bar, page-mark mid-turn grey→black at the guard, closed-book pommel.
- W-099 Dancing Fang — dao mid-step shattering a shackle with sparks, lit notched spine, dance-step arc, lit doorway safe endpoint, ring pommel.

Gates PASS. Batches 4–5 (W-100…159) still in rejected style; next redo round after owner review.

## 15d. Batch 4 REDONE + owner VARIETY ruling (2026-09-04, after owner approved the batch-3 redo)

**New owner ruling:** stop clustering on blade/blunt/spear — vary the weapon *kind* itself, and pick each form from the item's own `Speed / range` stat in its `SE-NNN-B` registry record (consult the M.A.W. codex/creation source). Recorded ranges for this batch: W-100/101/108/119/126 = `2 — Short`; W-102/103/105/106/115/120/125 = `3 — Medium`.

W-100…126 redrawn as varied forms, each staged from its own record:
- W-100 Unsaid Requiem — bladed WAR FAN half-open, ribs holding unfinished script, the lone petal spinning above (Short).
- W-101 Ember Requiem — STILL LIFE: sheathed blade leaning on the empty chair with the written return time; coal mote glowing orange over the guard (Short).
- W-102 Dancing Fang — ROPE DART: fang dart mid-orbit on a full cord loop, open link at the handle end, release partner's mark (Medium).
- W-103 Cold Lens — FROST LENS freezing a pierce line that crystallizes a tangled interference; breath-fog off the glass (Medium).
- W-105 Giant's Maul — SET-DOWN SCENE: head grounded with black pressure rings, load-limit line, open grip cuff released by the supporter's hand, second grip wraps (two-person rule) (Medium).
- W-106 I Alone Crossed Requiem — the blade LAID FLAT AS A BRIDGE over a gap, broken fuller dimming mid-span, lone figure crossing (Medium).
- W-108 Trace Fang — NEEDLE AWL with eye + RED THREAD running through the grip to the context note (one known fact, one unknown line) (Short).
- W-115 Memory Lens — MIRROR LENS: the stranger reflected inside the glass while their dashed outline stands empty beside it; pierce hits the peeled pressure film, not the person (Medium).
- W-119 Shadow Lens — WELL LENS held at the centre of a perspective-drawn room that is swallowing a name off a door plate; return-location note + witness outside (Short).
- W-120 Cage Fang — TRAP-JAW CAGE: two barred jaws held open, ridge line open at the hinge, a small bird-line escaping (release, not revenge) (Medium).
- W-125 Returning Lens — THROWN SHUTTER DISC mid-flight on its dashed return arc with spin ghosts, silver edge, tiny doorway return-image, open waiting hand (Medium).
- W-126 Melting Lens — GLASS MELT BLADE: translucent edge dissolving into beads and reforming lower down, cracked portrait it works against, blank unmarked tag (Short).

Gates PASS. Batch 5 (W-127…159) still in rejected style; next redo round after owner review — apply the same variety + range-stat rule.

## 15i. Batch 7 (2026-09-05, full current standard: shape-variant research + weapon-first detail)

Items: W-193, 195, 200, 205, 210, 215, 219, 220, 222, 225, 230, 233. Ranges from records: Medium = 193/195/200/205/225/233; Short = 210/215/219; Long (10–15) = 220/222/230. All drawn weapon-only (no stickmen/scene props), each a distinct researched shape variant:

- W-193 Wall's Maul — MONOLITH MAUL: unmarked light-swallowing black block (interior pure black, light dying at the rims), the hairline division seam etched down the face, matched witness-notches both sides, TWO wrapped grips on one haft (it will not lift for a single hand's cause).
- W-195 Sorrow Lens — MIRROR-FACED BLADE: broad flat rectangular razor of Void-white glass holding a dusk-dim room reflection (window, low light bar), opacity clouding rolling in from the pry-corner, boundary line etched mid-face.
- W-200 Gatekeeper's Blade — LONG SINGLE-EDGED BOUNDARY BLADE: deep-red flat brightening to a pale true edge, faint gate-arch watermark near the guard, verified-mark rune at the tip third, gate-pillar quillons with the declared passage kept open between them, route tag on the ring pommel.
- W-205 Hollow Staff — SEAM-STAFF (first true staff kind): matte black shaft textured like bark stripped AGAINST the grain, dim lit central seam that illuminates nothing, echo-intake vents mid-staff drinking ambient Han motes, root-shadow etched at the butt ferrule.
- W-210 Laughter Lens — ANGLED HAND-LENS: palm-wide ground disc with radial rim ticks, handle joined at a POINTING angle, the glass showing a mouth a fraction ahead of its face, returned-laugh wave entering from behind the rim.
- W-215 Name Lens — TWO-HANDED WIRE-FRAME LENS: small near-translucent disc in a bent-wire yoke with twin wire-wound grips and hung witness cards; letters materializing at opposite edges, the agreement line joining only matches, mismatches left visible, one warm living-answer spot.
- W-219 Splinter Requiem — ACICULAR NEEDLE-CRYSTAL BLADE (new researched crystal habit): slender needle blade with two companion needles grown alongside, wet luminous edge, authentic droplets running point-to-hilt and vanishing, song lines at the exact remembered pitch, dry residue line at the base.
- W-220 Years Maul — CALENDAR POST-DRIVER: both striking faces stacked with calendar leaves (page edges drawn), one leaf mid-tear showing consequence lines, registration plate the shaft has outgrown, finger-width growth rings down the haft with the newest ring brightest.
- W-222 Patina Fang — RUST-FLAKE-EDGE FANG: warm dark iron fang whose edge is a run of standing orange rust-flake serrations (sharper than polish), flakes shedding, green patina blooms on the flat, motion-ghost quiver at the tip toward the oldest marker.
- W-225 River Maul — FLOW-CHANNEL MAUL: an open tunnel bored clean through the head (no reservoir), dark intake mouth one face and bright outlet mouth the other, channel bore visible through the block, ripple marks worn into the faces, downstream quiver ghosts.
- W-230 Final Lens — SIGHT-STAFF: nearly colorless lens disc fork-mounted atop a long pale frame, heartbeat pulse-line ring, one clear transparency wedge at the exact boundary, three diminishing falloff rings etched down the frame, memory-cost bead counter, planted butt spike.
- W-233 Soul Requiem — BIPYRAMIDAL CRYSTAL BLADE (new researched crystal habit): double-pyramid profile widest at the waist and pointed both ways, warm Lament bead film standing along the edge, walking-line inclusion inside, song notation blurring as it leaves the blade, two tears at the pommel.

No kind changes vs the records — Appearance parity intact. Gates PASS (SVG, structure, word floor). Next: batch 8 = next 12 W numbers >233 and <1000.

## 15h. Batches 5 + 6 SHAPE-VARIANT UPGRADE (2026-09-05, owner ruling: research real shape variants, minimum 4 per weapon shape)

Owner directive: research online the different real shapes of each weapon type (minimum 4 variants per shape family) and make each item a DIFFERENT researched variant — e.g. a crystal blade must look like actual crystal (jagged / blunt / sharp / natural edge), not a generic sword recolored. Research sources: splitting-maul subtypes (wedge-poll, post maul, spike maul, drum/cylinder, octagonal sledge), natural quartz formations (terminated prism, double-terminated, bladed/platy aggregate, fenster/skeleton windows, phantom growth, faden thread, druse crust), knife/sword edge types (sharp V, serrated, blunt wedge, natural crystal edge), bow rest-shapes (straight D, recurve, reflex, deflex), javelin types (socketed pilum, barbed angon with weighted joint).

MAUL/HAMMER FAMILY (6 variants across the set): W-127 wedge-poll splitting maul (flat riveted poll + tapering wedge bit carrying the mirrored break); W-130 carved stone orb post-maul (saint-niches, kintsugi); W-155 octagonal sledge (chamfer band on all 8 facets); W-156 cylindrical drum sledge (barrel hoops + clock on the drum END face); W-157 timber post-maul (growth rings on the end face, iron hoops); W-160 double-faced rectangular sledge (chain-link stamp bands, forged open link); W-169 cross-peen hammer (flat bright face + wedge peen); W-180 ledger-brick ram block.

CRYSTAL BLADE FAMILY (6 natural-formation variants): W-135 terminated prism (six-sided prism, pyramid termination facets, growth striations); W-140 bladed/platy aggregate (overlapping crystal plates, each tip catching light); W-150 fenster/skeleton quartz (etched triangular windows that ring); W-152 phantom crystal (nested ghost-blade outlines = the doors it wandered); W-168 double-terminated crystal (pyramid facets BOTH ends, points nowhere by default); W-175 faden quartz (milky white thread running the full length, gas-inclusion beads); W-189 compacted dust-echo (solid edge, dissolving spine).

EDGE VARIANTS: W-145 serrated inner edge + barbed outer spine; W-159 frost DRUSE crust (clusters of tiny terminated points on the spine); W-185 diamond-point offset trowel (four straight edges to a point, stepped crank tang); W-190 barbed angon-style javelin (backward barbs, long iron shank, spherical pilum weight at the joint). OTHER FAMILIES: W-165 candle-staff (melt lips, frozen drips, singing edge-fin); W-170 translucent glass mallet (bell hollow + unrung clapper inside); W-176 RECURVE loom bow (tips curve away, warp-strand window, anchor knots); W-184 sectioned futuristic sighting frame (four connected segments, join couplings, energy conduit, fogged lens muzzle).

Weapon KINDS unchanged — Appearance text still accurate, parity intact. Gates PASS (SVG, structure, word floor).

## 15g. Batches 5 + 6 DETAIL UPGRADE (2026-09-05, owner correction)

Owner ruling: too much surrounding detail, not enough weapon detail — the weapons looked simple, and small stickmen are not wanted. All 24 SVGs (batch 5: W-127/130/135/140/145/150/151/152/155/156/157/159; batch 6: W-160/165/168/169/170/175/176/180/184/185/189/190) redrawn WEAPON-FIRST: no stick figures, no scene props; each weapon fills the frame at a dynamic angle with dense material detail (iron straps + rivets, banded hafts, cord wraps loop by loop, facet/grain/vein lines, edge highlights, engraved story marks carried ON the weapon itself — e.g. the Broken Maul's mirrored crack-web with two reflected faces, the Saint's Maul's gold-filled kintsugi cracks and halo, the Deadline Maul's clock face with exposed gears in the crack, the Binding Maul's open chain link forged into the head, the Silence Hammer's bell hollow visible inside the translucent glass head with an unrung clapper, the Loom bow's warp strands crossing the window, the Redacted Lens's fogged rim + cleared core with chequered grip and witness-ring, the Rage Fang's fissure web heating at the tip). Weapon KINDS unchanged from the records — no Appearance text edits required, parity intact. Gates PASS.

## 15f. Batch 6 (2026-09-05, first batch under the NON-MELEE ruling)

Owner directive with the batch-5 approval: for variety, Medium-range items should include gun/cannon/staff/fantasy kinds — not everything a hitting/cutting weapon. Ranges from records: W-160/168/169/170/185/189 = `2 — Short`; W-165/175/176/180/184/190 = `3 — Medium`.

- W-160 Binding Maul — GROUNDED CHAIN-LINK MAUL: maul lying on the ground (it does not rise until the name is spoken), open link in the head, Weight line wrapping a hatched obligation field, name card and obligation card held apart, released person walking to the review door, custodian with the debt file (Short).
- W-165 Melted Requiem — CANDLE-STAFF (new kind): tall planted staff whose wax-soft candle head drips light and carries a singing edge-fin; melted light runs forward and stops at ONE current danger; the future forked possible/never-certain; present-care witness with raised hand (Medium). Appearance text updated in md+html.
- W-168 Trace Requiem — RETURN-ROUTE BLADE: small blade with the broken route line inside, the line turning toward the mapped lit exit and away from the crumbling collapsed trace; map card with custodian mark; dim tally until all return (Short).
- W-169 Rusted Maul — BRACE-STRIKE MAUL: small maul swung level, rust lines on the head, short dark brace line from the cracked column into the prepared A-frame replacement, relief team with the repair plan, green handoff tick (Short).
- W-170 Silence Hammer — BELL-HOLLOW HAMMER: pale glass hammer over the single spreading impact circle that swallows sound marks; external warning arriving OUTSIDE the field; alert partner with the warning log; struck-ear mark for the deaf bearer (Short).
- W-175 Dream Requiem — THREAD-LIGHT BLADE: wandering under-surface threads gathering into one luminous line that runs past the tip into the maze of hidden desire; sleeper led out; lantern waking-anchor; oval doorway guard (Medium).
- W-176 Dream Requiem (Loom) — LOOM-FRAME THREAD-BOW (new kind): two crystal limbs strung with the single released thread, warp strands crossing the window, two anchor knots (Dream/waking) at the grip; the shot unpicks a woven grid construct line by line and spirals the material back to the Loom's custody box (Medium). Appearance text updated in md+html.
- W-180 Debt Maul — LEDGER-WALL RAM MAUL: long iron-banded haft driven horizontally like a ram, ledger-brick head holding the debt wall open, people passing through the held gap to review, custodian pointing the route beyond, route-review card (Medium).
- W-184 Redacted Lens — HAND-CANNON SIGHTING FRAME (new kind): slender white pistol-shaped frame with the Void-glass disc where a muzzle would be — it fires nothing but sight; Pierce along the sightline to the pale erasure outline; three declaration cards (known/unknown/inferred); Archive-witness eye over the fragment tray (Medium). Appearance text updated in md+html.
- W-185 Gallery Requiem — PALETTE-KNIFE BLADE: broad trowel blade with brush-stroke ridges and a dragged-background patch, cranked tang; faceless portrait in its frame, whispers steadied into legible lines; verified-name and explicit-unknown cards; witness eye; involuntary tears (Short).
- W-189 Fading Requiem — DUST-ECHO BLADE: matte blade shedding grains from the spine, steadying cone falling on ONE bright doorway of a fading dashed settlement; witness recording; dusk band; postponed-custody dust on the hilt (Short).
- W-190 Rage Fang — FANG-HEAD JAVELIN (new kind): crimson fang socketed onto a short javelin shaft cocked for the cast; the bounded red path literally ENDS at the gold accountability line; detention grid; accountability witness with the stop-hand; heat marks for revenge-drift (Medium). Appearance text updated in md+html.

Gates PASS (SVG, structure, word floor). PARITY: form-sentences updated in registry md + docs html for the four items whose kind changed (W-165 staff, W-176 bow, W-184 hand-cannon frame, W-190 javelin); ability/limit/ritual text verbatim; md↔html parity 12/12.

## 15e. Batch 5 REDONE (2026-09-05, after owner approved batch 4 + variety rule)

Ranges from records: W-135/150/152/155/156 = `2 — Short`; W-127/130/140/145/151/157/159 = `3 — Medium`. Note: five items in this batch are canonically NAMED "Maul" and W-151 is named a club by its own record, so their weapon KIND is fixed by canon — variety was achieved by giving every maul a completely different head, pose, and scene, and by pushing the non-maul items into non-sword forms where the record allows.

- W-127 Broken Maul — FRACTURE-FACE MAUL: head face to viewer with mirrored cracks reflecting two angles of the bearer's face; multiple black impact paths converge on one chosen endpoint ring (Medium).
- W-130 Saint's Maul — RELIQUARY STONE MAUL: cracked stone orb held high, black pressure lines splitting the named load onto THREE prepared support points; wide case key at the haft base (Medium).
- W-135 Warm Requiem — TEAR-LIGHT BLADE: warm tear-shaped light drifting inside the crystal, dream-line running to a lantern waking-anchor with the wake-cue tag; fading dream spiral being cut (Short).
- W-140 Willow Requiem — WEEPING WILLOW BLADE: the blade droops in a willow arc, shedding slow-falling leaf-light motes; leaf-shaped guard; hum arcs under the bow (Medium).
- W-145 Thorn Fang — THORN HOOK + PERIMETER: inward-curving thorn planted at the crown of its unfurled red thorn ring, marked entrance gap with a safe person entering; hostile arrows stopped outside (Medium).
- W-150 Laughter Requiem — CHIME BLADE: shimmer band fading toward the gripped end, chime hollow releasing a laugh-note that falls as a tear; the one-joy/one-loss pair held together by a cord (Short).
- W-151 Border Root — ROOT CLUB + BOUNDARY FENCE: living green root strand coiling the grip into the ground, raising a red root fence with the negotiated open arch and a traveller passing through (Medium).
- W-152 Wandering Requiem — DOOR-GRAIN BLADE: charred door-grain under the glass; the blade separates a repeating ghost-door loop from the real lit door, threshold line pointing home (Short).
- W-155 Shadow Maul — WRONG-SHADOW MALLET: compact mallet in a lamp-lit room casting its shadow TOWARD the lamp, the shadow darkening as it reaches the hovering Weight block; chalk balance/uncertainty marks (Short).
- W-156 Deadline Maul — CLOCK-FACE MAUL: cracked clock face with off-time hands, weight line running to the framed action field with its green check; case card with due date/action/protected rest (Short).
- W-157 Sleeping Maul — EXHALE MAUL: head held horizontal, black weight line falling like a slow exhale onto the hatched fatigue field; rest/watch/wake-bell rotation drawn below (Medium).
- W-159 Frozen Fang — FROST-FRACTURE FANG: frost fractures opening along the sharp red line, the visible breath escaping the pressure knot at the tip; relief person's raised stop-hand; cold exhale under the guard (Medium).

Gates PASS (SVG, structure, word floor). No Appearance text changes needed: all 12 illustrations depict exactly the forms the records describe (mauls stay mauls, blades stay blades, club stays a club) — parity intact from the batch-appearance install.

**Text-parity follow-up (owner check, 2026-09-04):** when a redo CHANGES an item's physical form, the `### Appearance` text in the `.md` record AND the `.html` page must be updated to describe the new form (physical-form sentences only; abilities, limits, rituals kept verbatim). Applied to the four batch-4 items whose kind changed: W-100 (narrow blade → bladed war fan with script-lined ribs), W-102 (broad blade → rope dart on woven cord + open link), W-108 (narrow blade → tracing needle/awl with eye + red thread), W-120 (broad blade → hinged trap-jaw cage held open). W-101/103/105/106/115/119/125/126 already matched their art (scene/staging changed, form did not). md↔html parity re-verified 12/12; word counts 167–205; word-floor, structure, and SVG gates PASS. **This parity rule applies to every future redo batch.**

## 16. Next weapon batch
Batch 6 = next 12 W SVGs in numeric order after 159 (run `ls docs/assets/art/maw/maw-w-*-01.svg | grep -oE 'maw-w-[0-9]+' | sed 's/maw-w-//' | sort -n | awk '$1>159 && $1<1000' | head -12` for the exact list). Same procedure: read each page's Appearance paragraph → assign an unused archetype/variant (extend the catalog if needed) → hand-write the SVG in the batch-1 format → render + contact-sheet review → gates → update mapping table + this log → commit + push.
