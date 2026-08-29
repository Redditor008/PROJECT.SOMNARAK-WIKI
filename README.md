# PROJECT.SOMNARAK-WIKI

Official static encyclopedia of **Somnarak** — the City of Unresolved Sorrow.

Open the wiki in a browser:

- Live site folder: [`01_Somnarak_Wiki/index.html`](01_Somnarak_Wiki/index.html)
- Local: `python3 -m http.server 8000 --bind 0.0.0.0 --directory 01_Somnarak_Wiki`

## Contents

| Path | Role |
|---|---|
| `01_Somnarak_Wiki/` | Public wiki (185 HTML articles, CSS, JS, SVG art, search index) |
| `REFERENCE_SOMNARAK_WIKI/` | Canonical lore sources, diagrams, icons, and build tools |

Offline wiki archive (one file, overwritten on every wiki update):

```bash
python3 REFERENCE_SOMNARAK_WIKI/tools/update_wiki_zip.py
```

Output is always `01_Somnarak_Wiki.zip` at the repository root (outside `01_Somnarak_Wiki/` and `REFERENCE_SOMNARAK_WIKI/`) — never a new zip name.

Current era in-canon: **Year 4,238 · Dawn Initiative** (post-1,778 Cycles).

Terminology is Somnarak-native: Sorrow Entities, M.A.W., Reverie Directorate, Echo-Cores, Coherence Counter, Han-Energy / Echoes, Absolvohan.
