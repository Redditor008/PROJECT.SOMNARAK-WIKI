# Somnarak Wiki — Content Depth and Visual Identity Standards

**Effective:** 2026-08-31  
**Authority:** Direct project-owner instruction  
**Status:** Binding publication gate for every public page and every new or revised visual asset

This document preserves the project-owner rules that were previously given conversationally and could not be found as a durable changelog or specification. These requirements supersede any older instruction that allows a 100-word page, a generic template page, a title-only illustration, a recolored duplicate, or a prohibition against silhouettes.

---

## 1. The 200-word floor

Every public HTML page must contain **at least 200 words of meaningful, page-specific editorial content**. Two hundred words is the floor, never a target and never a ceiling.

The rule applies to every public page type:

- encyclopedia articles;
- category and list hubs;
- character and faction records;
- Sorrow Entity and M.A.W. dossiers;
- Facility, map, mechanics, operation, and story pages;
- project, download, error, and utility pages, including the 404 page.

### What counts

Count the meaningful text in the page’s primary content area. Titles, prose, captions, tables, lists, testimony, and page-specific labels may count when they communicate real information.

Do **not** count shared site chrome or repeated scaffolding:

- global header, side rails, and footer;
- breadcrumbs and article/discussion/source/history tabs;
- table-of-contents labels;
- repeated cross-navigation directories;
- search controls;
- generic status labels copied across the site;
- invisible metadata, alt text, CSS, JavaScript, or comments.

### What is forbidden

- Padding a short page with filler, circular phrasing, or repeated paragraphs.
- Copying unrelated source material merely to cross the threshold.
- Treating 200 words as a reason to truncate a source-rich page.
- Publishing a stub now with a promise to complete it later.
- Counting a large navigation menu as article content.

A page under 200 editorial words fails publication. A page at or above 200 words can still fail if it is generic, repetitive, misplaced, unsupported by source, or visually unfinished. The normal encyclopedia target remains **300+ words whenever the source supports it**, with no upper limit imposed by this rule.

---

## 2. No plain, generic, or swap-template pages

A Somnarak page must never look or read like a generic template whose title, accent color, and nouns were exchanged.

Shared navigation and accessibility behavior may remain consistent across the site, but the page’s editorial composition must be specific to its subject. Page-specific design can come from:

- the subject’s physical structure, material, scale, or movement;
- its Han type, sorrow logic, containment behavior, or environmental effect;
- a canonical event, location, relationship, quote, instrument, or ritual;
- a distinctive diagram, timeline, process, map, evidence plate, or data treatment;
- typography and layout choices that reinforce the written record rather than decorate it arbitrarily.

A consistent wiki shell is not permission to mass-produce identical article bodies. If two pages remain recognizable as the same design after their titles and colors are removed, at least one requires redesign.

---

## 3. Read the text before designing an SVG

Every public page requires an SVG-led visual treatment specific to that page or subject. A shared favicon, site logo, navigation control, or unrelated registry icon does not satisfy this requirement.

No SVG may be designed from the page title alone. The page title and the actual written content are both mandatory design inputs. Before creating, selecting, or revising an SVG for a page, the designer must read the complete destination page and its canonical source material.

The visual brief must identify at least three subject-specific signals from the text, such as:

1. a physical or environmental motif;
2. an emotional, historical, or behavioral motif;
3. a functional, mechanical, or containment motif.

Those signals must influence the composition, silhouette, internal geometry, texture, visual rhythm, or narrative detail. Merely placing the title beside a generic symbol does not satisfy this rule.

When the page text changes the meaning of the title, the text controls the artwork. For example, a “bell” that is fused to a tower, remembers names, and transmits Lament must not be represented as an interchangeable bell pictogram.

---

## 4. SVG means a complete visual language, not only an icon

SVG work may include any page-appropriate combination of:

- navigation or registry icon;
- article banner;
- environmental background;
- profile or dossier plate;
- silhouette, shape study, or non-facial portrait;
- containment schematic;
- equipment drawing;
- map, floor cutaway, timeline, or process diagram;
- decorative frame, signal trace, seal, or page-specific data visualization.

An icon alone is not automatically a complete visual treatment. The required asset set must be chosen from the needs of the written page.

A profile does **not** require a face. It may use a silhouette, posture, object, architecture, negative space, fragmented form, shadow, or another canon-supported shape. A non-facial profile must still communicate the subject’s identity and cannot be a generic human outline.

---

## 5. Every SVG must be stylized and personally identifiable

Plain geometric placeholders and generic clip-art symbols are prohibited. Each SVG must have a visual fingerprint tied to its subject.

The following do not qualify as unique artwork:

- the same paths with a different fill or stroke color;
- the same badge, person, weapon, building, or creature silhouette with a renamed label;
- one generic composition with a different central pictogram;
- a recolored template background;
- a title card that contains no details from the article;
- an asset whose identity disappears when its text label is hidden.

Color may reinforce identity, but color cannot be the only difference. Distinct assets require meaningful differences in silhouette, geometry, composition, proportion, marks, texture, narrative details, or spatial structure.

---

## 6. Shared global-chrome consistency

The top bar, left sidebar, and bottom bar are deliberate shared chrome and must be identical in structure, labels, order, and resolved destinations on every public HTML route, including the 404 page and asset gallery. Relative path prefixes and accurate active states may change with route context; the underlying destinations may not.

The canonical archive sequence is:

| Slot | Primary label | Terminal sublabel | Destination |
| --- | --- | --- | --- |
| A-00 | Main | Terminal | `index.html` |
| A-01 | Characters | Echo-Cores | `characters/index.html` |
| A-02 | Lore | Cycles | `lore/index.html` |
| A-03 | Atlas | City | `locations/index.html` |
| A-04 | Factions | Orders | `factions/index.html` |
| A-05 | Facility | Floors | `departments/index.html` |
| A-06 | Entities | SECC | `entities/index.html` |
| A-07 | M.A.W. | Arsenal | `maw/index.html` |
| A-08 | Mechanics | Systems | `mechanics/index.html` |
| A-09 | Downloads | Files | `downloads.html` |

Each represented archive marks exactly one link with `aria-current="page"`; project and error routes may correctly have no active archive. Every top bar also uses the same Somnarak brand, Year 4,238 status, search label, search destination, responsive drawer behavior, and shared asset versions.

Every page also uses the homepage-derived canonical left sidebar. It contains the same Somnarak identity, public-network state, nine database hubs, nine Echo-Cores, cartography/download links, release console, labels, order, and resolved destinations. Directory depth and accurate current-page/current-archive states may vary; sidebar content and presentation may not. The asset gallery and Entity Tales anthology are not exceptions.

Every page ends with one canonical bottom bar. It contains the same Somnarak identity and motto, source-led city/Facility/archive topology, eight primary archive gateways, four project resources, release 1.8.31 console, publication metrics, quality protocols, public-access status, and changelog destination. Article-specific categories or previous/next controls belong above this component; they must not turn the global footer into a page-authored variant.

The Directorate-terminal styling of the top bar, left sidebar, and bottom bar is intentionally common navigation and does not count as the page-specific visual treatment required elsewhere in this standard.

Run `python3 tools/sync_global_top_bar.py`, `python3 tools/sync_global_left_sidebar.py`, and `python3 tools/sync_global_bottom_bar.py` to detect drift. Run a corresponding tool with `--write` to regenerate every static copy from its canonical definition. `python3 tools/audit_site_structure.py` enforces all three contracts as publication gates.

---

## 7. Required workflow for pages and visuals

1. **Read the full source and destination page.** Do not design from a filename, heading, or summary alone.
2. **Confirm nested placement.** Follow `PROJECT_MOON_WIKI_NESTED_PLACEMENT_RESEARCH.md`; do not solve a thin page by dumping unrelated canon into it.
3. **Write meaningful editorial content.** Reach at least 200 words without padding; retain greater depth when the source provides it.
4. **Prepare a visual brief.** Record the page-specific physical, emotional/historical, and functional/mechanical signals.
5. **Choose the asset family.** Decide whether the page needs an icon, banner, background, profile, diagram, or a broader suite.
6. **Design for unique form, not recolor.** Compare the new silhouette and composition against related assets; run `python3 tools/audit_svg_compositions.py` to catch malformed XML and paint/text-only duplicates in curated page art.
7. **Integrate the visuals into the page.** Artwork must support reading hierarchy and must not be an unattached gallery ornament.
8. **Perform visual QA.** Check desktop and mobile layout, legibility, overflow, contrast, file paths, and useful alt text.
9. **Run content and chrome QA.** Run `python3 tools/audit_page_word_floor.py`, all three global-chrome synchronizer checks, and `python3 tools/audit_site_structure.py` to confirm the 200-word floor after shared chrome is excluded and to check the canonical header, homepage-derived sidebar, footer, links, resources, IDs, anchors, and search indexing.
10. **Report honestly.** A page or asset that has not passed these checks is incomplete.

---

## 8. Publication checklist

A new or revised public page may be described as complete only when every applicable line passes:

```text
[ ] Primary editorial content contains at least 200 meaningful words.
[ ] The page uses the correct nested category and does not contain an unrelated source dump.
[ ] The prose is page-specific, non-repetitive, and source-supported.
[ ] The page body is not a title/color swap of another article.
[ ] The page has an SVG-led visual treatment beyond shared chrome, tied to its title and written subject.
[ ] The complete page and source were read before visual design began.
[ ] The visual brief uses physical, emotional/historical, and functional/mechanical details from the text.
[ ] The chosen visual suite goes beyond an icon when the page calls for banners, backgrounds, profiles, diagrams, or other forms.
[ ] Profiles use a distinctive canon-supported face, silhouette, object, shape, posture, architecture, or negative-space treatment.
[ ] No SVG is an identical or recolored copy of another asset.
[ ] The artwork remains identifiable when its text label and accent color are removed.
[ ] Desktop and mobile visual QA pass.
[ ] The canonical top bar, homepage-derived left sidebar, and bottom bar labels, destinations, status text, placement, active states, search path, and responsive layouts pass.
[ ] Local links, image paths, IDs, anchors, and search records pass.
```

These standards are a minimum quality gate. Passing them does not cap article length, visual complexity, or the number of meaningful page-specific assets.

The current reproducible baseline and its manual-review limits are recorded in `PUBLIC_PAGE_COMPLIANCE_AUDIT_2026-08-31.md`.
