#!/usr/bin/env python3
"""Retarget links that still advertise old fail pages; redirect deleted URLs."""
from __future__ import annotations

import json
import pathlib
import re

ROOT = pathlib.Path("/home/user/PROJECT.SOMNARAK-WIKI")
DOCS = ROOT / "docs"

# Deleted satellite dumps → real articles (Netlify pretty URLs, with and without .html).
REDIRECTS = [
    ("/entities/se-001-containment-log", "/entities/se-001-the-orphaned-bell"),
    ("/entities/se-002-incident-log", "/entities/se-002-the-grieving-colossus"),
    ("/entities/se-003-field-survey", "/entities/se-003-the-wilderness-tide"),
    ("/entities/se-005-suppression-guide", "/entities/se-005-the-smothering-mother"),
    ("/entities/se-007-observation-log", "/entities/se-007-brume"),
    ("/entities/se-009-memory-extracts", "/entities/se-009-the-memory-weaver"),
    ("/entities/se-010-verdict-records", "/entities/se-010-the-convergence"),
    ("/entities/se-011-acoustic-analysis", "/entities/se-011-the-whispering-walls"),
    ("/entities/se-014-debt-ledger", "/entities/se-014-the-debt-eater"),
    ("/entities/se-015-equilibrium-trials", "/entities/se-015-the-debt-scale"),
    ("/departments/floor-1-sub-protocols", "/departments/floor-1-neutral-command"),
    ("/departments/floor-2-arsenal-vaults", "/departments/floor-2-maws-keep"),
    ("/departments/floor-3-extraction-protocols", "/departments/floor-3-extraction-hall"),
    ("/departments/floor-4-insight-observation-labs", "/departments/floor-4-insight-forge"),
    ("/departments/floor-5-border-containment-cells", "/departments/floor-5-border-watch"),
    ("/departments/floor-6-deep-vault-records", "/departments/floor-6-deep-vault"),
    ("/departments/floor-7-shadow-corps-operations", "/departments/floor-7-shadow-corps"),
    ("/departments/floor-8-gate-watch-perimeter", "/departments/floor-8-gate-watch"),
    ("/locations/zone-a-central-spire", "/locations/zone-a-core-nexus"),
    ("/locations/zone-b-giltong-slums", "/locations/zone-b-west-ward"),
    ("/locations/zone-c-auction-houses", "/locations/zone-c-collectors-row"),
    ("/locations/zone-d-han-refineries", "/locations/zone-d-forge-and-gardens"),
    ("/locations/zone-e-frontier-ramparts", "/locations/zone-e-perimeter-bulwark"),
    ("/factions/secc-classification-system", "/mechanics/secc-classification-system"),
    ("/mechanics/secc-ranks", "/mechanics/secc-classification-system"),
]


def write_redirects():
    lines = ["# Old fail / satellite URLs → real articles"]
    for src, dst in REDIRECTS:
        lines.append(f"{src} {dst} 301")
        lines.append(f"{src}.html {dst} 301")
        lines.append(f"{src}/ {dst} 301")
    (DOCS / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote docs/_redirects", len(REDIRECTS) * 3, "rules")

    toml = (ROOT / "netlify.toml").read_text(encoding="utf-8")
    block = "\n".join(
        f'[[redirects]]\n  from = "{src}{suf}"\n  to = "{dst}"\n  status = 301\n'
        for src, dst in REDIRECTS
        for suf in ("", ".html", "/")
    )
    # keep the catch-all 404 last
    if "Old fail / satellite" not in toml:
        toml = toml.replace(
            "[[redirects]]\n  from = \"/*\"\n  to = \"/404.html\"\n  status = 404\n",
            block + "\n[[redirects]]\n  from = \"/*\"\n  to = \"/404.html\"\n  status = 404\n",
        )
        (ROOT / "netlify.toml").write_text(toml, encoding="utf-8")
        print("patched netlify.toml redirects")


def patch_html():
    nfiles = 0
    for p in DOCS.rglob("*.html"):
        if "assets" in p.parts:
            continue
        t = p.read_text(encoding="utf-8")
        o = t
        t = t.replace(">SECC Ranks</a>", ">SECC</a>")
        t = t.replace("SECC Ranks", "SECC")
        t = t.replace(
            "Threat rating hierarchy from T-01 AETHER up to catastrophic T-05 APOCRYPHA breach tiers.",
            "Origin, coherence, potency, element, and manifestation codes — not LC risk ranks.",
        )
        t = t.replace("VIEW RISK TIERS →", "VIEW SECC CODES →")
        t = t.replace(
            "SECC ranks from CAN to APOCRYPHA, work responses, and M.A.W. yield.",
            "SECC codes, work types, and M.A.W. yield. Registry is a fraction of ~3XX entities.",
        )
        t = t.replace(
            "The five ontological layers of reality separating the Upper C",
            "Dream, Abyss, and Han as structural grief — not five LC layers. Upper C",
        )
        t = t.replace(
            "The Four Work Types (Insight, Attachment, Repression, Extraction)",
            "The Four Work Types (Flerehan, Pugnahan, Viderehan, Ferrehan)",
        )
        t = t.replace(
            "Instinct (Ferrehan), Insight (Viderehan), Attachment (Flerehan), Repression (Pugnahan).",
            "Flerehan (Tears), Pugnahan (Confrontation), Viderehan (Observation), Ferrehan (Endurance).",
        )
        if t != o:
            p.write_text(t, encoding="utf-8")
            nfiles += 1
            print("patched", p.relative_to(DOCS))
    print("html files patched", nfiles)


def patch_rd_secc():
    p = DOCS / "factions" / "the-reverie-directorate.html"
    t = p.read_text(encoding="utf-8")
    t2 = t.replace('href="secc-classification-system.html"', 'href="../mechanics/secc-classification-system.html"')
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("fixed RD SECC href")


def patch_search():
    sp = DOCS / "data" / "search.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    n = 0
    for e in data:
        title = e.get("title") or ""
        if "AETHER" in title or "APOCRYPHA" in title or "SECC Ranks" in title:
            if "secc" in (e.get("url") or ""):
                e["title"] = "SECC Classification System"
                e["description"] = "Origin, coherence, potency, element, manifestation codes."
                n += 1
        desc = e.get("description") or ""
        if "AETHER" in desc or "T-01" in desc:
            e["description"] = desc.replace(
                "Threat rating hierarchy from T-01 AETHER up to catastrophic T-05 APOCRYPHA breach tiers.",
                "Origin, coherence, potency, element, and manifestation codes.",
            )
            n += 1
        kw = e.get("keywords") or ""
        if "AETHER" in kw or "Sujipga" in kw:
            e["keywords"] = kw.replace("AETHER", "").replace("APOCRYPHA", "").replace("Sujipga", "Sugeumga")
            n += 1
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("search patches", n)


def patch_lore_hub():
    p = DOCS / "lore" / "index.html"
    t = p.read_text(encoding="utf-8")
    t2 = t.replace(
        "The five ontological layers of reality separating the Upper City from the Weeping Abyss.",
        "Dream (Somnus), Abyss (Narak), and Han as structural grief. Not five LC layers.",
    )
    # partial earlier replace may have broken a sentence; fix common leftovers
    t2 = t2.replace(
        "Dream, Abyss, and Han as structural grief — not five LC layers. Upper City from the Weeping Abyss.",
        "Dream (Somnus), Abyss (Narak), and Han as structural grief. Not five LC layers.",
    )
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("patched lore hub cosmology blurb")


def verify():
    docs = DOCS
    # RD link
    rd = (docs / "factions/the-reverie-directorate.html").read_text(encoding="utf-8")
    assert "../mechanics/secc-classification-system.html" in rd
    # no SECC Ranks
    left = []
    for p in docs.rglob("*.html"):
        if "assets" in p.parts:
            continue
        t = p.read_text(encoding="utf-8")
        if "SECC Ranks" in t or "T-01 AETHER" in t:
            left.append(str(p.relative_to(docs)))
    print("fail-label leftovers", left or "none")
    # purged files still gone
    gone = docs / "entities/se-001-containment-log.html"
    print("containment-log exists", gone.exists())


def main():
    write_redirects()
    patch_html()
    patch_rd_secc()
    patch_search()
    patch_lore_hub()
    verify()


if __name__ == "__main__":
    main()
