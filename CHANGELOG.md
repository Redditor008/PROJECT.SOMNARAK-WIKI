# Somnarak Wiki Changelog

This file records notable changes to the public Somnarak Wiki.

> **Record note:** The `1.8.31` entry was reconstructed on 31 August 2026 from the tracked repository, commit `db114f8`, and a tree comparison with the preceding published snapshot (`8d58b3b`). The previous agent did not maintain a chronological changelog, so this is a verified summary rather than its original session notes.

## Unreleased

### Added

- Added `CONTENT_AND_VISUAL_STANDARDS.md` as the durable publication gate for page depth, non-generic composition, source-led SVG design, visual-suite scope, silhouette use, and asset uniqueness.
- Added `LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md`: the public GitHub Pages URL is now the mandatory acceptance surface, and successor sessions must avoid manual branch proliferation while handling Arena-assigned branches honestly.
- Added three dependency-free publication audits under `tools/`: the shared-chrome-aware 200-word floor, local path/ID/fragment/search integrity, and SVG XML/page-coverage/paint-insensitive composition checks.
- Added `tools/sync_global_top_bar.py` as the canonical renderer and drift check for every public page’s labels, destinations, active state, search path, and shared asset versions.
- Added `tools/sync_global_left_sidebar.py` to render the homepage archive rail on every public route and reject identity, group, label, destination, or active-state drift.
- Added `tools/sync_global_bottom_bar.py` to enforce one footer identity, resource set, release record, status line, and body-end placement on every public route.
- Added 20 source-led SVG compositions for the 404 recovery trace, archive export route, distribution ledger, source placement map, expanded global-footer topology, three Entity registry hubs, and twelve non-canonical M.A.W. hold/retraction records.

### Changed

- Raised the binding minimum for every public HTML page to 200 meaningful editorial words, excluding shared site chrome; the limit is explicitly a floor rather than a ceiling.
- Replaced eleven inconsistent top-bar variants and the asset gallery’s missing header with one ten-link Directorate archive bar across all 197 routes; added coded archive slots, exact active states, keyboard search, responsive two-deck and drawer modes, and a stronger scanline/status treatment.
- Replaced twelve legacy left-rail variants and two detached exceptions with the homepage sidebar across all 197 routes; added archive and personnel codes, precise page/archive states, a release console, improved contrast, an illuminated Directorate emblem frame, sticky desktop navigation, and responsive behavior.
- Replaced 69 unrelated footer compositions across 190 pages and seven missing footers with one expanded Directorate archive terminus on all 197 routes: a source-led city/Facility/codex topology, eight archive gateways, four project resources, release console, publication metrics, quality protocols, responsive stacking, and changelog access.
- Added durable standards prohibiting plain, generic, title-only, template-swapped, and recolor-only visual work, and clarified that a shared favicon or navigation mark does not count as a page’s SVG treatment.
- Defined SVG as a broader page-specific visual system encompassing icons, banners, backgrounds, profiles, silhouettes, diagrams, and other forms derived from the complete written page.
- Expanded and individually styled the 404 page, reader Download Center, and project Distribution Ledger. Their audited editorial counts are now 279, 256, and 308 words respectively.
- Replaced four broken archive links with revision-bound GitHub repository and canon-workspace routes, and corrected the outdated Dekan link on the M.A.W. hub.
- Reconciled search coverage: all 196 non-404 HTML pages now have one unique search record, including the previously omitted Daily Cycle page.
- Replaced nine generic broken contents links with descriptive section anchors and removed seven duplicate IDs across the affected Lore, Location, M.A.W., and Mechanics pages.
- Corrected 15 M.A.W. source-entity labels that carried an extra closing parenthesis.
- Rebuilt the Facility Incident Reports banner and icon around its ten-event severity sequence, replacing a recolor-only composition shared with the Department archive.
- Replaced three mislabeled SE-001 artwork copies used for SE-002, SE-005, and SE-010 with the correct subject profiles, and corrected the four reference generators that could restore those bad paths.
- Repaired 38 malformed legacy SVG files by encoding visible ampersands; with the expanded footer topology, all 1,329 SVG assets now parse as XML.

### Fixed

- Fixed the 404 recovery page so every asset, gateway, and search path resolves from any failed URL. GitHub Pages serves `404.html` at the location of the missing route, so all of its relative paths previously broke for every subdirectory miss (verified live: `/entities/…` misses rendered broken emblems and gateway links). Added a `<base href="/">` root anchor in the page head so the record renders completely at every depth without altering the audited chrome markup.

## 1.8.31 — 2026-08-31

### Release summary

Reorganized and expanded the Somnarak encyclopedia, moved the public site into the GitHub Pages `docs/` publish tree, and restyled the Hand of Change articles as a dense Directorate archive. The tracked public inventory increased from 185 to 197 HTML files.

### Added

- Added a root GitHub Pages entry page and established `docs/` as the public static-site directory.
- Added the Hope Transformations collection:
  - One category hub.
  - Twelve numbered Hope Transformations.
  - The Trinity of Dawn and the Hand of Hope.
- Added the Unknown Entities collection with seven dedicated records and a category hub.
- Added the Sorrow Entity list and the Entity Groups and Transformation Chains article.
- Added five color-based Ordeal articles: Blue, Black, Pale, Grey, and Purple.
- Added five Facility 01 operational articles covering agent assignment, the daily cycle, missions, upgrades, and research observation.
- Added dedicated records for the Judexhan, Keepers, and Menders.
- Added The Book of Regressor as a lore article rather than an Entity dossier.
- Added local search data, build manifests, source maps, visual QA records, and reference-transfer reports.
- Added the preserved canon/reference corpus under `REFERENCE_SOMNARAK_WIKI/`, including Sorrow Entity, Hope Transformation, Unknown Entity, Ordeal, character, M.A.W., and world-reference material.

### Changed

- Moved the publishable wiki from `01_Somnarak_Wiki/` to `docs/` for GitHub Pages deployment.
- Rebuilt the homepage around eight principal archives: Entities, M.A.W., Characters, Mechanics, Factions, Facility, Atlas, and Lore.
- Updated the repository README and public wiki homepage with a visible `1.8.31` release summary, verified inventory, changelog access, and the corrected post-Cycle status.
- Restyled the encyclopedia with Directorate command strips, cutaway panels, phase rails, quota chips, room plates, mission briefs, staff plates, and alarm matrices.
- Preserved data tables while giving Facility, Entity, M.A.W., and Mechanics pages stronger visual hierarchy.
- Standardized shared navigation, search, article tabs, infoboxes, breadcrumbs, cross-references, and floating contents controls.
- Expanded the public category structure instead of creating one public page for every raw source record.
- Consolidated Ordeal source material into color articles and the Four Watches framework rather than publishing 60 near-duplicate routes.
- Consolidated repeated or short satellite records into their primary Entity, Facility, Location, and classification articles.
- Updated the site identity to Year 4,238, Dawn Initiative, with the Cycle ended and Xyan commanding Gate Watch.

### Consolidated or removed public routes

The following groups were removed as standalone HTML articles and folded into primary records or retained as deployment aliases:

- Eight floor-specific satellite protocol pages.
- Ten secondary Entity log, survey, analysis, and incident pages.
- Three unsupported Entity dossiers for SE-004, SE-006, and SE-008.
- Five older Zone A–E location routes.
- The standalone SECC classification route, whose material now lives on the Entities hub.

This removed 27 older HTML paths while the new category work added 39, producing a net increase of 12 public HTML files.

### Verified public inventory

| Area | HTML files |
| --- | ---: |
| Sorrow Entities and Hope/Unknown collections | 36 |
| M.A.W. | 42 |
| Lore | 21 |
| Mechanics | 21 |
| Characters | 20 |
| Facility 01 / Departments | 18 |
| Factions | 18 |
| Locations | 13 |
| Atlas maps | 2 |
| Project documentation | 2 |
| Asset gallery | 1 |
| Root pages, including 404 | 3 |
| **Total** | **197** |

Additional verified inventory at this release:

- Approximately 270,000 words inside public page content.
- 1,312 SVG assets and 85 PNG assets.
- 196 HTML pages intended for search indexing, excluding the 404 page.
- Static HTML, CSS, JavaScript, and JSON with no external runtime dependency or build step.

### Deployment

- Canonical live wiki: <https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/>
- GitHub Pages serves the contents of `docs/`.
- The site can be previewed locally with:

  ```bash
  python3 -m http.server 8000 --bind 0.0.0.0 --directory docs
  ```

### Known issues at release

These issues were present in the `1.8.31` snapshot and are recorded here rather than silently reported as fixed:

- Older audit documents disagree on the page count, reporting 51, 181, or 185 instead of the current 197.
- Four archive-download links point outside the published `docs/` tree or to a missing `FOR_WIKI.zip` file.
- The M.A.W. hub contains one outdated link to `characters/lead-dekan.html`; the actual record is `characters/the-containment-lead-dekan.html`.
- Nine contents links across three articles target missing section IDs.
- Seven articles contain duplicate HTML IDs.
- The search index duplicates `entities/index.html` and omits `departments/daily-cycle.html`.
- Several converted articles contain repeated headings or paragraphs.
- Some M.A.W. routes are explicit retraction or holding records and are not complete canonical equipment dossiers.

### Verification performed

- Confirmed the canonical GitHub Pages homepage is publicly accessible.
- Confirmed representative homepage, Entity, Character, Lore, Mechanics, Atlas, and search resources load locally.
- Confirmed JavaScript and JSON syntax passes.
- Counted the tracked HTML and image inventory directly rather than relying on the older generated manifests.
