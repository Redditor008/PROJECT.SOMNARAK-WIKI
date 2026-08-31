# Public Page Compliance Audit — 2026-08-31

**Public root:** `docs/`  
**Binding standard:** `CONTENT_AND_VISUAL_STANDARDS.md`  
**Placement authority:** `PROJECT_MOON_WIKI_NESTED_PLACEMENT_RESEARCH.md`  
**Inventory:** 197 public HTML files, 1,329 SVG assets, and 85 PNG assets

## Result

All reproducible publication gates pass in the current working tree.

| Gate | Scope | Result |
| --- | ---: | --- |
| Editorial word floor | 197 HTML files | **PASS** |
| Local resources, IDs, and fragments | 20,281 local references; 1,767 fragments | **PASS** |
| Search reconciliation | 196 records for 196 non-404 pages | **PASS** |
| Canonical global top bar | 197 components; 10 archive links each | **PASS** |
| Canonical global left sidebar | 197 components; 21 directory links each | **PASS** |
| Canonical global bottom bar | 197 components; 14 fixed links each | **PASS** |
| SVG XML validity | 1,329 SVG files | **PASS** |
| Page-level SVG candidate coverage | 197 HTML files | **PASS** |
| Paint/text-insensitive curated-art comparison | 347 SVG compositions | **PASS** |
| Local HTTP response check | 197 HTML files | **PASS** |

Run the same gates from the repository root:

```bash
python3 tools/audit_page_word_floor.py
python3 tools/sync_global_top_bar.py
python3 tools/sync_global_left_sidebar.py
python3 tools/sync_global_bottom_bar.py
python3 tools/audit_site_structure.py
python3 tools/audit_svg_compositions.py
```

The SVG coverage check requires every page to contain inline SVG or reference a local SVG that is not merely sitewide chrome, using a conservative reuse threshold of 20 pages. This is a triage gate, not an automated claim of artistic merit. Source relevance, meaningful symbolism, mobile legibility, and whether a composition remains recognizable without labels and accent color still require human review under the binding checklist.

## Editorial depth

The word-floor audit parses primary page content and excludes repeated interface regions such as global headers, rails, footers, contents panels, cross-navigation, and tactical chrome.

- **197 of 197 pages** contain at least 200 counted editorial words.
- The current counted corpus contains **256,745 words**.
- The median page contains **603 words**.
- **17 pages** fall between 200 and 299 words; these remain qualifying pages, not targets for truncation or padding.
- The lowest qualifying page is `entities/list.html` at **235 words**.
- Remediated utility pages now count as follows:
  - `404.html`: **279 words**;
  - `downloads.html`: **256 words**;
  - `project/downloads.html`: **308 words**.

No navigation labels, alt text, metadata, CSS, JavaScript, or invisible text were used to make those pages pass.

## Structural and search reconciliation

The site-wide structure audit resolves local links, image sources, scripts, stylesheets, object data, and same-page or cross-page fragments. It also rejects duplicate IDs and reconciles the search index against every non-404 HTML route.

The cleanup replaced the generic broken contents destinations in:

- `maw/maw-crafting-and-extraction.html`;
- `maw/maw-set-synergies.html`;
- `mechanics/panic-states-and-corrosion.html`.

Seven duplicate-ID cases were removed from the affected Location, Lore, M.A.W., and Mechanics articles, and 15 M.A.W. source labels lost a stray extra closing parenthesis. Search now contains exactly 196 unique URLs for the 196 expected non-404 pages, including `departments/daily-cycle.html`, with no duplicate, missing, or stale record.

## Global chrome reconciliation

The top-bar review originally found eleven combinations of link order, wording, search labels, and active-state conventions across 196 pages, while `assets/icons/icons_gallery.html` had no global bar. The canonical renderer now places the same ten archive destinations on all **197 pages** in this order: Main, Characters, Lore, Atlas, Factions, Facility, Entities, M.A.W., Mechanics, and Downloads. Terminal sublabels and A-00 through A-09 slot codes are also fixed rather than page-authored.

Relative prefixes are recalculated for root, one-level, and two-level routes. Represented sections receive one exact `aria-current="page"`; the 404 and project source-map routes correctly claim no unrelated section. Every page now loads the same versioned stylesheet and script, uses a depth-correct search-index path, and exposes the same accessible search and navigation controls.

The visual treatment was rebuilt as a Directorate terminal header with an emblem housing, live-era status, archive-specific signal colors, active-route rails, scanline depth, and a keyboard `/` search affordance. It uses a single deck on wide displays, a complete two-deck layout at intermediate widths, and the same ten-link drawer below 900 pixels. The mobile button now controls the primary archive itself rather than opening a separate side rail with different wording.

`python3 tools/sync_global_top_bar.py` compares each static copy against the canonical renderer; `--write` repairs drift. The structure audit invokes the same validator and currently reports **197 expected components and zero consistency issues**.

The left-sidebar review found twelve rough structural variants among 195 existing rails, while the Entity Tales anthology used a separate legacy navigation system and the icon gallery had no sidebar. Labels, destinations, branding marks, core numbering, archive order, and active-page behavior differed. Some character records even replaced the current character’s anchor with unlinked text, preventing one reusable contract.

All **197 pages** now use the homepage-derived archive rail. Each contains the same public-network identity panel, nine database hubs, nine Echo-Core records, two maps, Download Center route, era classification, and 1.8.31 status console. Root, one-level, and two-level prefixes resolve independently; exact records receive `aria-current="page"`, while nested pages also identify their parent archive with `aria-current="location"`. The Entity Tales and icon-gallery layouts were brought into the shared shell instead of being exempted.

The updated visual system uses an illuminated Somnarak emblem housing, cyan/gold Directorate circuitry, numbered group headers, compact archive codes, archive-specific signal colors, clear hover/focus states, a sticky viewport rail, and an online release console. It remains a desktop information rail; below 993 pixels it yields to the complete responsive primary navigation rather than squeezing article content or creating a second competing drawer. Reduced-motion and print states are explicit.

`python3 tools/sync_global_left_sidebar.py` renders and validates the component. Its `--write` mode repairs every static copy, and the structure audit now reports **197 canonical left sidebars and zero consistency issues**.

The bottom-bar review found **69 unrelated footer compositions across 190 pages**, plus seven routes with no footer: the icon gallery, both atlas maps, the Departments hub, the reader Download Center, the Locations hub, and the project Distribution Ledger. Page categories, legal boilerplate, project notes, character-registry slogans, release data, and one-off status messages had been mixed unpredictably into the same global position.

All **197 pages** now end with one expanded Directorate archive terminus after the page shell closes. Its fourteen fixed links include the Somnarak home identity, all eight primary archive gateways, Source Map, Download Center, Icon Library, repository, and changelog. The shared release register records 1.8.31, 197 public pages, 256,745 counted editorial words, 1,414 SVG/PNG assets, the 200-word floor, Year 4,238/Cycle Ended state, Gate Command, public-access telemetry, and the four binding quality protocols.

The footer is intentionally substantial rather than a narrow legal strip. A large identity and motto panel sits beside a new source-led topology SVG that traces the Alpha Tree and five zones through all eight Facility 01 floors into eight orbiting public archive gateways. A separate release console, full sitemap deck, project-resource bank, four-cell publication register, protocol rail, and final status line create a layered Directorate terminal. Desktop uses a broad three-part hero and four-column gateway matrix; intermediate and mobile layouts progressively form two-column and single-column stacks without hiding a destination.

`python3 tools/sync_global_bottom_bar.py` enforces exact content, destinations, one-footer count, and placement before `</body>`; `--write` removes old variants and regenerates the component. The structure audit invokes all three global-chrome validators and currently reports **197 top bars, 197 left sidebars, 197 bottom bars, and zero consistency issues**.

## SVG integrity and composition review

The SVG audit performs three checks:

1. Every SVG must parse as XML.
2. Every public page must expose a non-sitewide SVG candidate or meaningful inline SVG.
3. Curated assets under `docs/assets/art/` are compared after paint, text labels, IDs, and descriptive metadata are removed. Geometry, element order, transforms, proportions, dimensions, and text placement remain in the signature, so recolor-only and renamed-title compositions collide.

Current result:

- all **1,329 SVG files** parse as XML;
- all **197 pages** pass the visual-candidate coverage gate;
- all **347 curated page-art compositions** avoid cross-subject paint/text-only collisions;
- **26 same-subject alias groups** remain allowed, consisting of alternate filenames for the same Entity banner or profile rather than one design assigned to different subjects.

This audit repaired 38 malformed legacy SVGs whose visible ampersands were not XML-encoded. It also removed three files for SE-002, SE-005, and SE-010 that were exact, mislabeled copies of the SE-001 Orphaned Bell composition. Nine M.A.W. pages and four preserved generator scripts now select the correct subject profiles instead.

The Facility Incident Reports banner and icon were also redrawn. The former pair reused the Department Incident Archive’s stacked-file geometry with changed labels and colors. The replacement uses a ten-event severity rail, distinct incident nodes, the major spikes at reports 004 and 005, and the recorded totals of 44 Fractured, 356 incapacitated, and zero deaths.

## Visual briefs for this remediation

The following briefs record how the new compositions derive from both title and written content rather than filenames alone.

| Page or family | Physical/environmental signal | Emotional/historical signal | Functional/mechanical signal | Distinct composition |
| --- | --- | --- | --- | --- |
| 404 Signal Lost | fractured route, Gate 5, void beyond the Veil | a missing address is not erased canon; 1,778 Cycles and Deep Vault loss | three recovery traces: registry code, archive gate, canon status | radial broken 404 gate feeding three unequal diagnostic branches |
| Reader Download Center | stack of 197 public pages and an archive package | revision provenance rather than an opaque stale ZIP | source → generated snapshot → local reader on port 8000 | continuous export path through a branch lattice and package cube into a terminal |
| Project Distribution Ledger | preservation vault, curation press, reader endpoint | source retention and rejection of binary churn | one revision spine across three distribution layers | asymmetric vertical cutaway beside a crossed-out archive-churn loop |
| Project Source Map | source folders, restart barrier, nested public tree | restart after generic auto-generated pages were rejected | full-source reading, nested placement, 200-word and visual gates | left-to-right editorial machine with a rejected stub fan-out below the publish line |
| Global footer topology | Alpha Tree, five city zones, eight unequal Facility floors, Gate Watch, and eight archive terminals | the archive motto binds witness to name-preservation; missing canon is not replaced by invention | witnessed city record → Directorate curation spine → verified 1.8.31 public codex | three-stage city/tree, Hand of Change, and orbiting archive network rather than a generic decorative footer texture |
| Entity Groups and Chains | birds, rooted sisters, masks, and a debt scale | entities share wounds without sharing form | group response, convergence, and directional transformation triggers | four different relationship constellations around one wounded core, separated from Hope |
| Hope Transformations | Hand of Hope, twelve rays, two Sovereign seals | original grief remains present after transformation | bonded functions such as light, shield, vigil, memory, and witness | preserved dark core inside a hand with a fourteen-node dawn arc |
| Unknown Entities | seven specimen apertures | “Unknown” is an archive status; The Extinguished warns that Hope can fail | seven registry records while the Regressor book routes to Lore | seven different object/place/absence vignettes joined by an archive scan field |
| SE-003 M.A.W. retractions | Wilderness Tide, wall, salt residue, weather contours | a false “Thread of Memory” filing displaced the actual Place-Weight subject | no personality, no individual grief, no extraction during Collapse | separate blade jig, empty cloak stand, and broken thread-evidence compositions |
| SE-004 M.A.W. holds | rust plating and a weeping ocular belong to the Sentry’s body | the 004 gap between canonical 003 and 005 source folders | no A/B/C/D donor files, issue authority, cost, or stat gate | missing registry drawer, anatomy/issue split, and caliper-classified ocular |
| SE-006 M.A.W. holds | leech, effluent conduit, membrane, and biological gland | a wiki Entity description cannot create a Codex donor set | closed registry valve and missing B/C/D and gift slots | blocked pipe circuit, tank-versus-suit examination, and stopped specimen conveyor |
| SE-008 M.A.W. holds | iron-maiden chamber, inward thorns, sarcophagus doors, anchored spikes | architecture and body shape were mistaken for equipment | absent source folder and no weapon, suit, or gift issue | chamber-bound spear path, plan-view clothing boundary, and empty gift orbit |

The twelve M.A.W. visuals deliberately depict a **hold or retraction**, not invented canonical equipment. Their shapes explain why each route remains as an archival correction while preserving the 197-page route inventory.

## Limits of certification

The automated geometry comparison is intentionally scoped to curated page art. Shared interface controls and same-subject deployment aliases elsewhere in `docs/assets/` are expected to repeat and are not evidence that different subjects share a design.

Likewise, this report does not retroactively claim that every untouched legacy illustration has been re-read against every canonical source. It establishes a complete machine-audited baseline, fixes the concrete XML and cross-subject collisions found during this review, and makes the manual source-led checklist binding for every future or revised asset. A visual can still fail editorial review even when its XML, coverage, and geometry signature pass.
