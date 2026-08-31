# PROJECT_SOMNARAK_WIKI

Static encyclopedia of Somnarak — open `index.html` in a browser, or serve this folder:

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

This `docs/` folder is the GitHub Pages publish root.

197 tracked HTML files · Year 4,238 Dawn Initiative · every page at or above the 200-word editorial floor.

Binding quality rules live in `../REFERENCE_SOMNARAK_WIKI/CONTENT_AND_VISUAL_STANDARDS.md`; deployment and branch rules live in `../REFERENCE_SOMNARAK_WIKI/LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md`; the current results are recorded in `../REFERENCE_SOMNARAK_WIKI/PUBLIC_PAGE_COMPLIANCE_AUDIT_2026-08-31.md`. The live GitHub Pages URL—not localhost, a pushed branch, or an open pull request—is the final acceptance surface. Run the dependency-free publication checks from the repository root:

```bash
python3 tools/audit_page_word_floor.py
python3 tools/sync_global_top_bar.py
python3 tools/sync_global_left_sidebar.py
python3 tools/sync_global_bottom_bar.py
python3 tools/audit_site_structure.py
python3 tools/audit_svg_compositions.py
```

All three global-chrome checks cover all 197 routes. Use a sync tool with `--write` to regenerate the ten-link header, homepage-derived left sidebar, or canonical identity/resource/status footer after route changes.
