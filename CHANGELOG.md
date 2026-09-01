# Somnarak Wiki Changelog

This file records notable changes to the public Somnarak Wiki.

> **Record note:** The `1.8.31` entry was reconstructed on 31 August 2026 from the tracked repository, commit `db114f8`, and a tree comparison with the preceding published snapshot (`8d58b3b`). The previous agent did not maintain a chronological changelog, so this is a verified summary rather than its original session notes.

## Unreleased

### Added

- Added three archive mechanics to the shared footer on all 197 routes: a per-page FILED UNDER filing strip (archive gateway, registry code, source-reference designation/item ID, and Korean name — auto-joined from `REFERENCE_SOMNARAK_WIKI` by the extended `tools/sync_global_bottom_bar.py`, with set-number hard constraints to prevent false provenance joins), a Random Archive action (196-route list generated into `wiki.js` by the new `tools/sync_random_archive.py`), and a last-verified stamp in the publication register.
- Added the CSS redaction component (`<details class="redaction">`, sealed/unseal labels) with a live redaction-protocol demonstration on the 404 recovery page.

- Added `INSTALL_PERCENTAGE_REPORT.md`: a per-file transfer audit measuring what percentage of each of the 1,861 `REFERENCE_SOMNARAK_WIKI/` source files made it into the published 197-page wiki (unique word 4-gram coverage against the published corpus), with overall and per-group breakdowns.

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

- Fixed the floating PAGE CONTENTS button, which was dead or missing on most routes, and rebuilt its entire float behavior (widget availability, pinning, float range, and sidebar clearance):
  - **Availability:** 57 pages still shipped a legacy static `.float-toc` whose button had no event handler, and `initFloatingToc()` only rebuilt the widget when it found at least two sections inside `.wiki-section` wrappers — entity, lore, M.A.W., department, and faction pages use flat `h2[id]` headings outside those wrappers, so dead legacy chrome (or no widget at all) was left behind. A further 123 pages had no `id` attributes on their section headings at all, so there was nothing for any TOC to link to. The legacy static navs were removed from all 57 pages; `initFloatingToc()` now collects every addressable `h2` in the content area regardless of wrapper; a new `ensureHeadingIds()` step assigns stable MediaWiki-style slug ids (CJK-safe, collision-suffixed, existing ids preserved) before any TOC is built; and the IntersectionObserver call is guarded so it can never truncate the remaining initialization.
  - **Pinning and hard viewport limits:** one canonical CSS block now owns the widget (overriding four conflicting legacy `!important` generations): desktop resting a quarter of the way down the open gap between the top bar and the bottom of the viewport at the content column's left edge (resting pin = top bar + 25% of the remaining gap, guarded to stay at least top-bar height + 14px on very short screens, so a wrapped two-row top bar can never clip it), panel rendered as a static flex item beside the trigger with `max-height: calc(100vh - 110px)` and internal scroll; narrow screens pinned bottom-left with a 55vh panel cap. The widget can no longer float beyond the viewport in either orientation. Tracking is transform-only (wiki.js writes the `--float-toc-xform` custom property, which the stylesheet's `transform: var(…) !important` rule consumes — the position MUST go through the variable, since an inline `style.transform` loses to the !important rule and would freeze the widget at the pre-JS fallback with no rail clearance — on a `will-change`-promoted layer) with the legacy drop-shadow filter disabled, so the widget moves on the compositor without per-frame layout while scrolling. The multi-page test suite now asserts both halves: the var is written and the stylesheet consumes it.
  - **Float range — stops exactly before the lower footer:** the button keeps a fixed transparent hit box (2.3rem × min 9.4rem — its original clickable footprint) while the visible tab (`.float-toc-tab`, compact 0.52rem type, centered inside) is smaller — so the button looks smaller but the hit box never shrinks — and a separate transparent element (`.float-toc-hit-ext`, clickable, up to 220px) carries the long lower hit box. wiki.js sizes that hit zone every frame so its lower edge always stops exactly 2px above the bottom of the page box (the bordered content frame) — a full gap above the top of the lower footer, so the stopper can never land inside the bottom-bar box — or 2px above the viewport bottom while the bottom of the page is off-screen. Only when the page box rises up to that lower hit edge does the tab itself lift, tracking the page-box bottom edge upward and exiting through the top of the viewport: the visible button stops at the bottom of the page box, above the bottom-bar box, and can never cross it, and the button is never hidden.
  - **Sidebar clearance:** the widget's left edge was hardcoded for the legacy 190px left-rail while the modern rail is 220px wide at ≥993px, so the button intruded into the top of the left sidebar where the [PUBLIC NETWORK] / [NODE RD-01] rail-signal chips live; it is now pinned to the actual content column's left edge (+6px inset, ≥8px floor), recomputed on every scroll/resize, with the pre-JS CSS fallback assuming the modern 220px rail. When the left-rail drawer is open on narrow screens the widget slides to the right of the drawer instead of sitting under it.
  - Verified with a stubbed-geometry jsdom sweep (15 scroll-position cases across desktop 1920×1080, short-viewport guard cases, and narrow 390×800, with the invariant that the lower hit edge sits exactly on the stop line whenever the extension is uncapped and never crosses the footer's top edge) and a runtime click suite (trigger click, hit-zone click, outside-click close, re-open, in-page link close, every link target existing; hub and homepage correctly widget-free). `ASSET_VERSION` advanced `20260901c` → `20260901p` across the iteration with all four chrome syncs re-run 197/197 per rule A3.
- Fixed the [PUBLIC NETWORK] / [NODE RD-01] rail-signal at the top of the left sidebar: the network label was a `display:flex` span, where CSS ellipsis cannot apply, so on narrower rails NODE RD-01 rendered on top of the NETWORK text. The label is now a block-level truncating flex item (ellipsis, `min-width:0`, status dot as inline-block), NODE RD-01 is `flex: 0 0 auto` (never shrinks), the container clips, and the signal type steps down below 1180px/1024px — the two labels can no longer overlap at any rail width.
- Fixed the 404 recovery page so every asset, gateway, and search path resolves from any failed URL. GitHub Pages serves `404.html` at the location of the missing route, so all of its relative paths previously broke for every subdirectory miss (verified live: `/entities/…` misses rendered broken emblems and gateway links). Added a `<base href="/">` root anchor in the page head so the record renders completely at every depth without altering the audited chrome markup.
- Restored the 87 legacy satellite URL routes (29 archived Entity, department, floor, zone, and mechanics URLs in three forms each) on the canonical GitHub Pages surface. `_redirects` is a Netlify-only mechanism that GitHub Pages ignores, so those bookmarks previously landed on the 404 record; the 404 page now carries a client-side route-recovery map derived from `_redirects`, verified to redirect all 87 forms to their consolidated records while leaving every other missing path untouched. `_redirects` is retained for Netlify mirrors.
- Removed the repeated-paragraph artifacts recorded as a known issue in 1.8.31: 104 duplicated editorial paragraphs across 29 articles (worst: the daily-cycle log line repeated 17× in the Cycle & Absolvohan article, 24 extra copies each in the Facility Incident Reports archive and the UCD Strike Force article, and tripled bios on most of the nine Echo-Core character pages). Four near-identical pairs where one copy carried wiki cross-links kept the linked copy in the narrative section and dropped the unlinked restatement in the summary block; no content was lost beyond the exact duplicates, and every affected page still clears the 200-word floor.
- Renamed the duplicated closing heading on all 27 M.A.W. Weapon / Suit / Gift sheets. Each sheet's final section repeated the item name as an `<h2>` identical to the page `<h1>` (and its float-TOC entry repeated it again); the section heading the registry fact-grid is now consistently titled **Registry Record** (`#registry-record`) across the nine Lament/Mourning/Embrace/Hope/Forgotten/Absolute/Listening/Debt/Balance donor lines, and every in-page TOC link was updated with the anchor.
- Pruned 966 unreferenced art files (4.58 MB: 881 legacy SVGs and all 85 never-used PNG icon sources, including the 158 Hand and 130 City layout sheets from the 51-page restart build; 777 of the pruned files are byte-identical to another pruned or retained file, 334 of them exact copies of assets still in use). The orphan set was computed with the structure audit's own reference-resolution logic and cross-checked against every HTML, CSS, JavaScript, SVG, and JSON reference in the tree before deletion; the public inventory is now the 448 SVGs (308 curated page-art compositions) that pages actually render. All publication gates pass on the pruned tree.
- Added a visually hidden `<h1 class="sr-only">` to the six routes that had none (the Characters, Factions, Lore, and Mechanics hubs and the two Atlas blueprint pages), which previously opened their content with an h2 or a banner image. The hidden headings reuse the site's existing `.sr-only` treatment, change nothing visually, and leave the dynamic floating TOC untouched (it skips hub pages and tracks only identified h2/h3 sections), so all 197 public pages now carry exactly one primary heading.
- Moved the 51-page restart build records (`WIKI_BUILD_MANIFEST.json`, `WIKI_BUILD_AUDIT.json`, `WIKI_PAGE_MANIFEST.csv`, `VISUAL_QA.json`, `RESTART_SOURCE_MAP.csv`) and the never-loaded icon generation manifest (`icons_manifest.json`) out of the public `docs/` tree into a repository-root `BUILD_RECORDS/` archive with a provenance README. None of the six files was referenced by any page, script, style, or data file; the current source-provenance record (`docs/SOURCE_MANIFEST.csv`, whose destinations are live pages) stays in place.
- Corrected the published inventory figures in every location (README, homepage release stats, and the global footer publication register on all 197 pages, re-rendered through the canonical bottom-bar sync tool) to the measured totals: **253,462** chrome-excluded editorial words and **448** in-use SVG art assets, superseding the 1.8.31 approximations of ~270,000 words and 1,414 assets.
- Rebuilt the home page's right rail (Facility 01 department console) to full L-Corp terminal parity with the canonical left rail, per rule A4: the same layered dark gradient (hairline accent, scanlines, radial glow, vertical depth), mirrored glowing edge strips (gold top / cyan bottom), and a signal header with a cyan monospace console line, gold glow underline, and red hazard rule. The eight floor rows are now coded terminal rows with per-floor accent bars, monospace code column, and the left rail's hover language (accent border, accent gradient, inset bar, glow) with the L-Corp avatar treatment, and the two map links became heavy hazard action buttons (red diagonal stripe, gold frame, arrow) after the reference `build_perfect_rails_and_styles.py` console. CSS-only, appended as the canonical block at the end of `wiki.css`; below 992px the console drops under the article as a full-width two-column grid, honors `prefers-reduced-motion`, and hides in print like the left rail. `ASSET_VERSION` bumped to `20260901b` and re-synced across all 197 pages per rule A3.

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
