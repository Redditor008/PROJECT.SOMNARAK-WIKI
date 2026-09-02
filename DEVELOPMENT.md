# DEVELOPMENT.md — Somnarak Wiki Development Handbook

> **Read this file first.** It is the standing handoff for AI/developer sessions
> working on this repository: what the project is, the binding rules, how the
> site is built, how to verify work, what has been shipped, and what is pending.
> Keep it current: when a future session changes any standing convention, update
> the relevant section in the same commit.

## 1. What this is

A static public lore wiki for **Somnarak**, a fictional city in a
Project-Moon-style setting (Han, Sorrow Entities, Facility 01, the Reverie
Directorate). No build step, no framework — plain HTML + one CSS + one JS.

- **Live site:** https://redditor008.github.io/PROJECT.SOMNARAK-WIKI (GitHub Pages serves the session branch tip directly; ~1–2 min rebuild after push)
- **Owner:** Redditor008. Work happens on the Arena session branch
  (e.g. `arena/…`), committed and pushed directly. **Never open a PR** (owner instruction).
- **Canon sources** live in `REFERENCE_SOMNARAK_WIKI/` (read-only input).

## 2. Repository layout

| Path | Contents |
|---|---|
| `docs/` | The public site (root = `index.html`). `assets/{css,js,art,icons,layout,avatars}`, `data/search.json`, one folder per archive (`characters/`, `lore/`, `locations/`, `factions/`, `departments/`, `entities/`, `maw/`, `mechanics/`, `atlas/`, `project/`) |
| `tools/` | All gate/sync/generation scripts. **Standard library only.** See §5–§7 |
| `REFERENCE_SOMNARAK_WIKI/` | Canon source tree. M.A.W. item registry: `LORE or REFERANCE/M.A.W. Codex_Set Registry/` (note the misspelled folder name — it is canonical). SE sources: `LORE or REFERANCE/01_Sorrow_Entities/` |
| `CHANGELOG.md` | Round-by-round history. Add an entry every commit batch |
| `RULE-TO-FOLLOW.md`, `UNIVERSAL_FOLLOW_RULE.md` | Owner's binding rules |
| `BUILD_RECORDS/` | Historical audit artifacts (manifests, QA json) |
| `01_Somnarak_Wiki.zip` / root `index.html` | Owner artifacts — **do not touch** |

## 3. Standing owner rules (binding — do not reverse without the owner)

1. **A0:** Every change is committed **and** pushed in the same turn.
2. **Never open a PR.** Commit + push directly to the session branch.
3. **A5:** Never delete or overwrite owner files without explicit instruction.
   The Google Search Console verification file `docs/google56d75ed58478c406.html`
   must stay **byte-identical** (53 bytes) — every tool skips it via `VERIFY_RE`.
4. **Desktop-only** site. No mobile styling needed (owner policy 2026-09-01).
5. **Source-led content:** page text comes from `REFERENCE_SOMNARAK_WIKI/` or the
   site's own established template language. Missing fields are omitted, never invented.
6. **References/Sources sections: NEVER** (owner rejected; do not propose again).
   Tabs UI and gallery = deferred (may be requested later).
7. Keep Somnarak-native canon terms (Han, SECC, Absolvohan, Echo-Cores, …).
8. **Do not rename HTML files.** URLs are permanent once published (links,
   sitemap, Google index depend on them). New pages use kebab-case slugs
   (`maw-w-016-01-the-lost-lens.html`, `se-001-the-orphaned-bell.html`).

## 4. Page anatomy & chrome

- **Global chrome** = top bar (`header.utility`), left rail (`aside.left-rail`),
  bottom footer (`footer.wiki-footer`). **Never hand-edit chrome** — the three
  sync scripts hold the canonical copy and validate every page.
- `ASSET_VERSION` lives at `tools/sync_global_top_bar.py:18` (format `2026MMDDx`,
  suffix advances x→y→z→aa→ab…). **Bump it whenever `wiki.css`/`wiki.js` change**,
  then re-run the three chrome syncs.
- Per-page SEO meta (description/canonical/OG) is enforced by
  `tools/sync_seo_meta.py` — it derives the description from the first long
  `<p>` inside `<div id="content">`, so give every page a real lead paragraph.
- M.A.W. item page structure (see `docs/maw/maw-w-001-01-*.html`):
  fast-jump pills → tactical directive box → breadcrumbs → `section.item-hero`
  (portrait + h1 + donor line) → optional `blockquote.entity-quote` →
  `section.item-mechanic` (FUNCTION/PRICE) → `div.item-columns` with
  `article.article-body` (overview / appearance / extraction / rejection rule /
  operational statistics / combat|resistance|gift record / signature ability /
  cost / corrosion / maintenance / shutdown / history of use / set resonance /
  source relationship) + `aside.item-infobox` (right) → `nav.article-nav` →
  triad box → cross-reference section.
- SE (entity) pages: infobox is a **sibling** of `.entity-article` (not inside
  it), on the right at all widths. Category tag strips (`.entity-tags`) sit
  above the h1.

## 5. Publication gates (all must PASS before commit)

```bash
python tools/audit_page_word_floor.py    # ≥200 editorial words/page, chrome excluded
python tools/audit_site_structure.py     # routes, ids, fragments, search 1:1, chrome on every page
python tools/audit_svg_compositions.py   # SVG XML valid; unique compositions; page visual coverage
```

After content or chrome changes, also run:

```bash
python tools/sync_global_top_bar.py --write
python tools/sync_global_bottom_bar.py --write
python tools/sync_global_left_sidebar.py --write
python tools/build_search_index.py       # search.json 1:1 with pages (keeps existing entries, adds missing)
python tools/build_sitemap.py            # sitemap.xml + robots.txt from the tree
python tools/sync_seo_meta.py --write
```

The chrome sync scripts also carry the public counters (page counts, word
corpus, SVG count, release number) — update those constants **before** running
the syncs when totals change (they live in `sync_global_bottom_bar.py` and
`sync_global_left_sidebar.py`).

## 6. Asset rules (SVG audit is strict)

- `docs/assets/art/**` is the **curated page-art** tree. The audit computes a
  *structural signature* (geometry, element order, transforms, text **placement**
  — paint, labels, IDs, and metadata are ignored). Two art files with the same
  composition but different subjects **fail** the audit; recolor-only variants
  are not allowed.
- Per-item art is therefore **generated with seeded geometry** (see
  `tools/generate_maw_items.py::make_svg`) — verify uniqueness by running the
  audit, not by eyeballing.
- Every HTML page must reference ≥1 local SVG used by ≤20 pages (or have inline
  SVG) — chrome-wide assets (icons, layout) don't count.
- CSS/JS are referenced with `?v=ASSET_VERSION`.
- Floor art exists at `assets/art/departments/f{1..8}-banner.svg` +
  `f{1..8}-icon.svg`; core avatars at `assets/avatars/avatar_core_*.svg`.
- The home right sidebar is the **FACILITY 01 console** (`aside.floor-rail` on
  `docs/index.html`): one CSS block at the end of `wiki.css` owns it
  ("HOME RIGHT RAIL — FACILITY 01 CONSOLE"). Older stacked blocks above it are
  legacy — the last block wins; don't re-activate them.

## 7. M.A.W. pipeline (item pages)

- **Registry:** `REFERENCE_SOMNARAK_WIKI/LORE or REFERANCE/M.A.W. Codex_Set Registry/`
  — 287 donors × 3 items (W/S/G) = **861 item records**, all published as of
  release 1.9.0. Record filename: `<DONOR>-<SLOT>__MAW-<W|S|G>_<Name>.md`.
- **Two record formats** (parser handles both):
  - Format A: `## ITEM IDENTITY` table + `### Ability — X` section +
    `### Incident Record`.
  - Format B: `## CANONICAL SOURCE STAT BLOCK` table + `**Incident — Name:**`
    inline + `**Corrosion:**` / `**Maintenance:**` / `**Shutdown:**`.
- **Generator:** `python tools/generate_maw_items.py` (idempotent — skips
  existing pages; `--dry-run`, `--limit N`, `--version`). Writes the page and
  its seeded SVG; keeps previously published filenames when the slug was
  extended earlier (e.g. `maw-g-014-01-the-debt-scale-gift.html`).
- **Retracted stubs:** SE-003/004/006/008 have **no** registry records — the 12
  stub pages stay as retractions (old URLs must keep resolving). The hub keeps
  their rows at the bottom of each registry table.
- Element colors used on item pages: Lament `#3e8bd5`, Grudge `#d64a4a`,
  Void `#8a8f98`, Weight `#c9a86a`, Mixed `#777777`.
- Grade labels (site-established): α — Minor, β — Moderate, γ — Major, δ — Critical.

## 8. Environment quirks (learned the hard way)

- **Shallow clone.** The sandbox can reset the local branch to the old base
  (`11ca85c`) between turns, and the owner can push files mid-turn (e.g. the
  GSC verification file). Before `git add -A`: `git fetch` and diff
  `FETCH_HEAD`; restore owner files your tree lacks. Before push: verify local
  HEAD vs `git ls-remote` (plain push — `--force-with-lease` is stale in a
  shallow clone).
- **`/tmp` is wiped between turns.** Rebuild the jsdom sandbox:
  `mkdir -p /tmp/jsdom-test && cd /tmp/jsdom-test && npm i jsdom@30.0.1`.
- **No headless browser.** jsdom is the DOM check (no layout). **jsdom OOMs
  past ~150 pages per process** — chunk validation loops (~150 pages/process,
  null the DOM each iteration).
- `fetch_page` fails on most external URLs (`SignatureDoesNotMatch`). For a
  live self-check, read the branch tip via
  `https://raw.githubusercontent.com/Redditor008/PROJECT.SOMNARAK-WIKI/<branch>/<path>`.
- Commit messages: **no backticks** (they execute) — use single quotes.
- Registry filenames: use `os.walk` + string matching; `fnmatch` is unreliable
  here.
- `grep -c` counts lines, not occurrences.
- The canonical source folder is spelled `LORE or REFERANCE` (owner's spelling —
  do not "fix" it).

## 9. Verification recipes

```bash
# DOM: no duplicate ids, all local links + assets resolve, word floor
# (run chunked; see /tmp/jsdom-test/chunk.js pattern from release 1.9.0)
node --max-old-space-size=2048 chunk.js <offset> <count>

# gates + syncs
python tools/audit_page_word_floor.py && python tools/audit_site_structure.py && python tools/audit_svg_compositions.py
```

jsdom gotchas: `Element.indexOf` doesn't exist (use
`compareDocumentPosition(a,b) & 4` for DOM order); `runScripts:'outside-only'`
needs assertions after `setTimeout`; `file://` localStorage throws.

## 10. Progress & open items

**Shipped (release 1.9.0, 2026-09-02):**
- M.A.W. full arsenal: all **861 registry items** (287 donors × W/S/G)
  published — 27 pre-existing sheets + 834 generated (pages, seeded source-led
  SVG art, set-diagram/triad cross-links, fast-jump, prev/next, infoboxes).
- M.A.W. hub: three full registry tables (287 rows each + 4 retracted rows),
  coverage text/bar updated.
- New tools: `tools/generate_maw_items.py`, `tools/build_search_index.py`.
- Site totals: 1,041 chrome pages, 1,040 search routes + sitemap URLs,
  728,439 editorial words, 1,282 SVGs.
- Prior rounds: SE field-record subpages, SE category tag strips, M.A.W.
  chapter publication (combat/resistance/gift records), Google indexing
  (sitemap/robots/SEO meta + GSC verification), home right sidebar rebuilt as
  the FACILITY 01 console, float-TOC, infobox/grid geometry fixes.
  Full history: `CHANGELOG.md`.

**Queued (round 26, 2026-09-02 — owner-ordered sequence):**
1. Reverie Directorate full record — **done** (this round, see CHANGELOG).
2. Nine Echo-Core character page expansions — **done** (round 26, same day):
   all nine `characters/the-*.html` rebuilt in full from `CHARACTER_WIKI/`
   (6.6k–16.3k words each; Director's Story sealed; core cross-links;
   Related Records nav; static + float TOCs regenerated).
3. Faction tech / relations / dream realm / memory archive / corporations —
   `factions/faction-technology.html`, `factions/index.html` (relations),
   `lore/the-dream-realm.html`, `locations/the-library-of-stolen-pasts.html`,
   `factions/the-founding-corporations.html` vs their 07_Reference sources.
4. `SOMNARAK_ENTITY_TALES.md` publication — **verified against the real
   entity files first** (owner gate): 246/246 tales match a real entity file
   by Korean name; SECC codes present in all 246 stems; all 55 main-protected
   entities covered (file = 55 main + 190 non-main); 88 tales use narrative
   names differing from the entity-file codenames (Korean is authority —
   publish under codename, keep tale epithet as alias); 242/246 tale entities
   are M.A.W. donors; 81 donor IDs (SE-1001+ series) have no tale.

**Deferred (owner decisions, not forgotten):**
- Tabs UI on item pages (later). Gallery (later). References: **never**.
- Entity pages for donors beyond the 10 published (SE-016…SE-997, UNK-247…903)
  have no dedicated pages yet; item pages link them to `entities/list.html`
  where needed.

## 11. Working loop for a session

1. Read this file + `CHANGELOG.md` (latest entries) + the owner's message.
2. Check branch state: `git status`, `git rev-parse HEAD`, `git ls-remote`.
3. Make the change. If CSS/JS changed → bump `ASSET_VERSION`. If totals
   changed → update chrome counters in the sync scripts.
4. Run syncs → gates → jsdom spot check (§9).
5. Add a `CHANGELOG.md` entry.
6. Commit (single quotes, no backticks) and push to the session branch.
7. Report to the owner: what shipped, what was deferred, any decision needed.
