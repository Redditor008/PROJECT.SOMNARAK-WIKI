# Build records (archived)

These files are **historical build artifacts of the 51-page restart build
(2026-08-28)**, preserved for provenance. They are intentionally **outside
`docs/`** so they are not served by GitHub Pages and cannot be mistaken for
the current public inventory.

| File | What it records |
| --- | --- |
| `WIKI_BUILD_MANIFEST.json` | Build manifest of the 51-page restart build (build date 2026-08-28, `html_pages: 51`). |
| `WIKI_BUILD_AUDIT.json` | Audit result of that same build (51 HTML pages, 8 department pages, 2 map pages, 10 entity pages, 27 M.A.W. pages). |
| `WIKI_PAGE_MANIFEST.csv` | Per-page row inventory of the 51-page build (relative path, title, visible article words, bytes, SHA-256). |
| `VISUAL_QA.json` | Visual QA record of the restart build (navigation restructure, entity home and M.A.W. codex review). |
| `RESTART_SOURCE_MAP.csv` | Source-to-destination map used to transfer canon material into the restart build. |
| `icons_manifest.json` | Icon generation manifest (SVG/PNG icon inventory metadata) from the icon transfer pass; not loaded by any page. |

The current public site is defined by the tracked pages in [`docs/`](../docs/),
the live publication gates in [`tools/`](../tools/), and the verified
inventory in [`CHANGELOG.md`](../CHANGELOG.md). Where these archived counts
disagree with the live site (page totals, asset totals, route lists), the
live site and the changelog win.
