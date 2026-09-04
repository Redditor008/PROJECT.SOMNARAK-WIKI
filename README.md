<p align="center">
  <img src="docs/assets/icons/somnarak_icon.svg" width="88" alt="Somnarak emblem">
</p>

<h1 align="center">Somnarak Wiki</h1>

<p align="center">
  Official encyclopedia of <strong>Somnarak</strong> — the City of Unresolved Sorrow<br>
  Year 4,238 · Dawn Initiative
</p>

<p align="center">
  <strong>1.9.0 (Unreleased)</strong> · 1,042 public HTML files · September 2026
</p>

<p align="center">
  <a href="https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/"><strong>Open the wiki →</strong></a>
  &nbsp;·&nbsp;
  <a href="CHANGELOG.md"><strong>Read the changelog →</strong></a>
</p>

---

Static GitHub Pages encyclopedia. No account and no build step are required.

## Current state — 1.9.0 (Unreleased)

The September 2026 expansion grows the archive from 197 to over a thousand pages while preserving Somnarak-native canon terminology.

- **1,042** tracked public HTML files (1,040 indexed pages plus the 404 page and the Search Console verification file)
- **10** principal archive hubs spanning Entities, M.A.W., Characters, Mechanics, Factions, Facility, Atlas, Lore, Locations, and Project
- **876** M.A.W. archive pages — 291 complete item sets (weapon, suit, gift), every item page carrying a source-led Appearance section drawn from the M.A.W. Codex Set Registry
- **246** entity tales collected in the [Entity Tales anthology](https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/lore/entity-tales.html)
- **1,284** local SVG art assets, all page-specific and gate-validated
- Over **1.2 million** words of public page content
- Dedicated Hope Transformation, Unknown Entity, and five-color Ordeal collections

See [`CHANGELOG.md`](CHANGELOG.md) for the full release history, the Unreleased work log, verification details, and known issues.

## Archives

| Hub | What it covers |
| --- | --- |
| [Sorrow Entities](https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/entities/) | Containment registry — published entities, donors, and UNK records |
| [M.A.W.](https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/maw/) | Weapons, suits, gifts — 291 complete registry sets |
| [Characters](https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/characters/) | Nine Echo-Cores and supporting cast |
| [Mechanics](https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/mechanics/) | Han, work types, ordeals, containment |
| [Factions](https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/factions/) | Reverie Directorate, Council, guilds |
| [Facility 01](https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/departments/) | Hand of Change, floors 1–8 |
| [Atlas](https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/locations/) | Zones A–E, the Maw, the Desolate |
| [Lore](https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/lore/) | Cycles, Alpha Tree, taboos, Weeping, the Entity Tales anthology |

## Repository

| Path | Role |
| --- | --- |
| [`docs/`](docs/) | Public wiki (HTML, CSS, art, search) — GitHub Pages root |
| [`REFERENCE_SOMNARAK_WIKI/`](REFERENCE_SOMNARAK_WIKI/) | Canon sources and diagrams, including the M.A.W. Codex Set Registry |
| [`tools/`](tools/) | Publication gates, chrome syncs, and content generators |
| [`RULE-TO-FOLLOW.md`](RULE-TO-FOLLOW.md) | Binding owner rules (v2): push-always doctrine, PR lifecycle, cache-busting |
| [`UNIVERSAL_FOLLOW_RULE.md`](UNIVERSAL_FOLLOW_RULE.md) | Additional binding session rules |
| [`SESSION_BREAK_PRECAUTION.md`](SESSION_BREAK_PRECAUTION.md) | Arena session-break recovery protocol and work ledger |
| [`DEVELOPMENT.md`](DEVELOPMENT.md) | Handoff guide: repo layout, gates, working loop, progress ledger |
| [`REFERENCE_SOMNARAK_WIKI/CONTENT_AND_VISUAL_STANDARDS.md`](REFERENCE_SOMNARAK_WIKI/CONTENT_AND_VISUAL_STANDARDS.md) | Binding 200-word floor and non-generic SVG rules |
| [`REFERENCE_SOMNARAK_WIKI/LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md`](REFERENCE_SOMNARAK_WIKI/LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md) | Binding live-site verification and no-extra-branch rules |
| [`CHANGELOG.md`](CHANGELOG.md) | Verified release history and known issues |

## Run locally

```bash
python3 -m http.server 8000 --bind 0.0.0.0 --directory docs
```

Then open `http://localhost:8000/`.

## Deployment acceptance

The owner verifies every update at **https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/**. Localhost, an Arena preview, a commit, a pushed branch, or an open pull request is not proof that a change is live. After integration into the configured GitHub Pages source, wait for its build and fetch the public URL with a cache-busting query to confirm a distinctive marker from the change.

Do not manually create extra branches. Use the established Pages source directly when the coding environment permits. If Arena assigns an immutable session branch, use only that branch and one direct pull request into the Pages source. See the [binding live-deployment and branch-continuity policy](REFERENCE_SOMNARAK_WIKI/LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md).

## Publication gates

```bash
python3 tools/audit_page_word_floor.py
python3 tools/sync_global_top_bar.py
python3 tools/sync_global_left_sidebar.py
python3 tools/sync_global_bottom_bar.py
python3 tools/audit_site_structure.py
python3 tools/audit_svg_compositions.py
```

After content changes, re-run the derived-artifact builders:

```bash
python3 tools/sync_seo_meta.py
python3 tools/build_search_index.py
python3 tools/build_sitemap.py
```

Use the corresponding sync tool with `--write` after adding or moving a public route. The checks enforce the same ten-link navigation header, homepage-derived left archive sidebar, and identity/resource/release footer across all indexed pages. Any `wiki.css`/`wiki.js` change must bump `ASSET_VERSION` and re-sync, or the fix never shows live.

Every public page must contain at least 200 meaningful editorial words after shared interface chrome is excluded. Pages and SVGs must be source-led, page-specific, and visually distinct—never generic templates or recolored duplicates. The SVG gate validates every vector file as XML and compares curated page-art geometry without relying on color or labels. See the [complete content and visual standards](REFERENCE_SOMNARAK_WIKI/CONTENT_AND_VISUAL_STANDARDS.md).

Canon terms stay Somnarak-native: Sorrow Entities, SECC, M.A.W., Reverie Directorate, Echo-Cores, Han, Absolvohan.
