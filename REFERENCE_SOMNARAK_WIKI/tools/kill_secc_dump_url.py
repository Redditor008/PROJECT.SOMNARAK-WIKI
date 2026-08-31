#!/usr/bin/env python3
"""Stop every click from landing on /mechanics/secc-classification-system.

That URL is the live PROJECT_SOMNARAK.md dump. Codes already live on
entities/index.html#classification. Delete the fail page and 301 the old path.
"""
from __future__ import annotations

import json
import pathlib
import re

ROOT = pathlib.Path("/home/user/PROJECT.SOMNARAK-WIKI")
DOCS = ROOT / "docs"
FAIL = DOCS / "mechanics" / "secc-classification-system.html"
HREF_RE = re.compile(
    r'(?:(?:\.\./)+)?(?:mechanics/)?secc-classification-system\.html'
)


def dest_for(path: pathlib.Path) -> str:
    rel = path.relative_to(DOCS).as_posix()
    if rel == "entities/index.html":
        return "#classification"
    depth = len(path.relative_to(DOCS).parts) - 1
    return ("../" * depth) + "entities/index.html#classification"


def patch_html() -> int:
    n = 0
    for p in DOCS.rglob("*.html"):
        if "assets" in p.parts:
            continue
        t = p.read_text(encoding="utf-8")
        dest = dest_for(p)

        def repl(m: re.Match) -> str:
            return dest

        t2 = HREF_RE.sub(repl, t)
        if t2 != t:
            p.write_text(t2, encoding="utf-8")
            n += 1
            print("href", p.relative_to(DOCS), "->", dest)
    return n


def patch_entities_hub():
    p = DOCS / "entities" / "index.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        '<a href="../mechanics/secc-classification-system.html">Sorrow Entity Classification Code (SECC)</a>',
        '<a href="#classification">Sorrow Entity Classification Code (SECC)</a>',
    )
    t = t.replace(
        '<a href="#classification">Sorrow Entity Classification Code (SECC)</a>',
        '<a href="#classification">Sorrow Entity Classification Code (SECC)</a>',
    )
    old = (
        "        <p>Full tables live on the <a href=\"#classification\">SECC classification</a> record. "
        "Tool-type specimens (SE-001, SE-015) can be worked as relics; Place-type specimens occupy the room itself.</p>"
    )
    new = """        <p>Tool-type specimens (SE-001, SE-015) can be worked as relics; Place-type specimens occupy the room itself. Published codes:</p>
        <div class="table-wrap">
          <table class="wiki-table hub-compact-table">
            <thead><tr><th>Code</th><th>Name</th></tr></thead>
            <tbody>
              <tr><td><code>C-IVδ-001 [LO]</code></td><td><a href="se-001-the-orphaned-bell.html">The Orphaned Bell</a></td></tr>
              <tr><td><code>C-Vδ-002 [WS]</code></td><td><a href="se-002-the-grieving-colossus.html">The Grieving Colossus</a></td></tr>
              <tr><td><code>O-Vγ-003 [WP]</code></td><td><a href="se-003-the-wilderness-tide.html">The Wilderness Tide</a></td></tr>
              <tr><td><code>N-IVδ-005 [GS]</code></td><td><a href="se-005-the-smothering-mother.html">The Smothering Mother</a></td></tr>
              <tr><td><code>O-IIγ-007 [VP]</code></td><td><a href="se-007-brume.html">Brume</a></td></tr>
              <tr><td><code>C-IVγ-009 [VS]</code></td><td><a href="se-009-the-memory-weaver.html">The Memory Weaver</a></td></tr>
              <tr><td><code>C-Vδ-010 [WS]</code></td><td><a href="se-010-the-convergence.html">The Convergence</a></td></tr>
              <tr><td><code>C-Iα-011 [LP]</code></td><td><a href="se-011-the-whispering-walls.html">The Whispering Walls</a></td></tr>
              <tr><td><code>C-IIIβ-014 [VS]</code></td><td><a href="se-014-the-debt-eater.html">The Debt Eater</a></td></tr>
              <tr><td><code>C-IIIβ-015 [VO]</code></td><td><a href="se-015-the-debt-scale.html">The Debt Scale</a></td></tr>
              <tr><td><code>C-IVω-001 [GP]</code></td><td><a href="../locations/the-maw.html">The Maw</a> (uncontained)</td></tr>
            </tbody>
          </table>
        </div>"""
    if old in t:
        t = t.replace(old, new)
        print("hub classification: dropped dump-page pointer, inlined codes")
    else:
        # after href rewrite the sentence may still mention the dump
        t2 = re.sub(
            r"<p>Full tables live on the <a href=\"[^\"]+\">SECC classification</a> record\.[^<]*</p>",
            new,
            t,
            count=1,
        )
        if t2 != t:
            t = t2
            print("hub classification: regex-replaced dump pointer")
        else:
            print("WARN: classification dump sentence not found")
    p.write_text(t, encoding="utf-8")
    assert 'secc-classification-system' not in p.read_text(encoding="utf-8")
    assert 'href="#classification">Sorrow Entity Classification Code (SECC)</a>' in p.read_text(encoding="utf-8")
    print("entities hub SECC intro now #classification")


def patch_search():
    sp = DOCS / "data" / "search.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    out = []
    for e in data:
        url = e.get("url") or ""
        if "secc-classification-system" in url:
            e["url"] = "entities/index.html"
            e["title"] = "Sorrow Entities — SECC codes"
            e["description"] = "Origin, coherence, potency, element, manifestation codes on the Sorrow Entities hub."
            e["category"] = "Sorrow Entities"
            print("search.json retargeted SECC entry")
        out.append(e)
    sp.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def patch_redirects():
    extra = [
        "/mechanics/secc-classification-system /entities/#classification 301",
        "/mechanics/secc-classification-system.html /entities/#classification 301",
        "/mechanics/secc-classification-system/ /entities/#classification 301",
    ]
    rp = DOCS / "_redirects"
    lines = rp.read_text(encoding="utf-8").splitlines()
    body = []
    for line in lines:
        if "/mechanics/secc-classification-system" in line and "secc-ranks" not in line:
            # factions/secc used to point at the dump
            line = line.replace(
                "/mechanics/secc-classification-system",
                "/entities/#classification",
            )
        if line.startswith("/mechanics/secc-ranks"):
            line = line.replace(
                "/mechanics/secc-classification-system",
                "/entities/#classification",
            )
        body.append(line)
    text = "\n".join(extra + body) + "\n"
    # de-dupe extra if re-run
    seen = set()
    keep = []
    for line in text.splitlines():
        if line in seen and line.startswith("/mechanics/secc-classification-system"):
            continue
        seen.add(line)
        keep.append(line)
    rp.write_text("\n".join(keep) + "\n", encoding="utf-8")
    print("patched docs/_redirects")

    toml = (ROOT / "netlify.toml").read_text(encoding="utf-8")
    toml = toml.replace(
        'to = "/mechanics/secc-classification-system"',
        'to = "/entities/#classification"',
    )
    block = """[[redirects]]
  from = "/mechanics/secc-classification-system"
  to = "/entities/#classification"
  status = 301
  force = true

[[redirects]]
  from = "/mechanics/secc-classification-system.html"
  to = "/entities/#classification"
  status = 301
  force = true

[[redirects]]
  from = "/mechanics/secc-classification-system/"
  to = "/entities/#classification"
  status = 301
  force = true

"""
    if 'from = "/mechanics/secc-classification-system"' not in toml:
        toml = toml.replace(
            '[[redirects]]\n  from = "/*"\n  to = "/404.html"\n  status = 404\n',
            block + '[[redirects]]\n  from = "/*"\n  to = "/404.html"\n  status = 404\n',
        )
    else:
        # ensure force = true on dump URL
        toml = toml.replace(
            'from = "/mechanics/secc-classification-system"\n  to = "/entities/#classification"\n  status = 301\n',
            'from = "/mechanics/secc-classification-system"\n  to = "/entities/#classification"\n  status = 301\n  force = true\n',
        )
        toml = toml.replace(
            'from = "/mechanics/secc-classification-system.html"\n  to = "/entities/#classification"\n  status = 301\n',
            'from = "/mechanics/secc-classification-system.html"\n  to = "/entities/#classification"\n  status = 301\n  force = true\n',
        )
        toml = toml.replace(
            'from = "/mechanics/secc-classification-system/"\n  to = "/entities/#classification"\n  status = 301\n',
            'from = "/mechanics/secc-classification-system/"\n  to = "/entities/#classification"\n  status = 301\n  force = true\n',
        )
    (ROOT / "netlify.toml").write_text(toml, encoding="utf-8")
    print("patched netlify.toml")


def delete_fail_page():
    if FAIL.exists():
        FAIL.unlink()
        print("DELETED", FAIL.relative_to(ROOT))
    else:
        print("already gone", FAIL)


def patch_chrome_tool():
    p = ROOT / "REFERENCE_SOMNARAK_WIKI/tools/restore_article_chrome.py"
    t = p.read_text(encoding="utf-8")
    t2 = t.replace(
        '("secc-classification-system.html", "SECC"),',
        '("../entities/index.html#classification", "SECC"),',
    )
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("chrome pills: SECC -> entities hub")


def verify():
    leftovers = []
    for p in DOCS.rglob("*"):
        if p.suffix.lower() not in {".html", ".json", ".js"}:
            continue
        if "assets" in p.parts and p.suffix != ".js":
            continue
        t = p.read_text(encoding="utf-8")
        if "secc-classification-system" in t:
            leftovers.append(str(p.relative_to(DOCS)))
    print("leftover secc-classification-system refs", leftovers or "none")
    print("fail file exists", FAIL.exists())
    hub = (DOCS / "entities/index.html").read_text(encoding="utf-8")
    assert 'href="#classification">Sorrow Entity Classification Code (SECC)</a>' in hub
    assert "../mechanics/secc-classification-system" not in hub


def main():
    patch_html()
    patch_entities_hub()
    patch_search()
    patch_redirects()
    patch_chrome_tool()
    delete_fail_page()
    verify()


if __name__ == "__main__":
    main()
