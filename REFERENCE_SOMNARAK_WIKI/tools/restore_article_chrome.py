#!/usr/bin/env python3
"""Restore LC article chrome (full left-rail + RAPID JUMP + tabs) on skinny wrap pages.

Homepage keeps its own right-rail / floor-buttons. Article analog is Architects:
left-rail (hubs + Echo-Cores + cartography) + RAPID JUMP pills + status HUD + page tabs.
"""
from __future__ import annotations

import pathlib
import re

DOCS = pathlib.Path("/home/user/PROJECT.SOMNARAK-WIKI/docs")

LEFT_NAV = """
      <nav aria-label="Wiki navigation" class="left-links">
        <section>
          <h2>DATABASE HUBS</h2>
          <a href="{p}index.html">Main Overview</a>
          <a href="{p}characters/index.html">Characters Hub</a>
          <a href="{p}lore/index.html">Lore &amp; Cosmology</a>
          <a href="{p}locations/index.html">Locations &amp; Atlas</a>
          <a href="{p}factions/index.html">Factions &amp; Guilds</a>
          <a href="{p}departments/index.html">Facility Floors</a>
          <a href="{p}entities/index.html">Sorrow Entities</a>
          <a href="{p}maw/index.html">M.A.W. Equipment</a>
          <a href="{p}mechanics/index.html">Systems &amp; Mechanics</a>
        </section>
        <section>
          <h2>THE NINE ECHO-CORES</h2>
          <a href="{p}characters/the-director-majin.html">1. Director Majin</a>
          <a href="{p}characters/the-secretary-seiyon.html">2. Seiyon (Secretary)</a>
          <a href="{p}characters/the-containment-lead-dekan.html">3. Dekan (Containment)</a>
          <a href="{p}characters/the-extraction-lead-zyrak.html">4. Zyrak (Extraction)</a>
          <a href="{p}characters/the-research-lead-ayshuk.html">5. Ayshuk (Research)</a>
          <a href="{p}characters/the-border-lead-mellda.html">6. Mellda (Border)</a>
          <a href="{p}characters/the-archive-lead-marjuk.html">7. Marjuk (Archive)</a>
          <a href="{p}characters/the-outsider-ishall.html">8. Ishall (Outsider)</a>
          <a href="{p}characters/the-exile-xyan.html">9. Xyan (Exile)</a>
        </section>
        <section>
          <h2>CARTOGRAPHY &amp; SCHEMATICS</h2>
          <a href="{p}atlas/hand-of-change-map.html">Hand of Change Map</a>
          <a href="{p}atlas/somnarak-city-map.html">Somnarak City Blueprint</a>
          <a href="{p}project/source-map.html">Master Archive Map</a>
        </section>
      </nav>
"""

PILLS = {
    "factions": [
        ("the-reverie-directorate.html", "Directorate"),
        ("the-high-council.html", "High Council"),
        ("the-sed-corps.html", "SED Corps"),
        ("the-ucd-strike-force.html", "UCD Force"),
        ("the-architects.html", "Architects"),
        ("the-weavers.html", "Weavers"),
        ("the-wardens.html", "Wardens"),
        ("the-collectors.html", "Collectors"),
        ("the-horizon-caravan.html", "Caravan"),
        ("the-memory-washers.html", "Washers"),
        ("faction-technology.html", "Faction Tech"),
        ("index.html", "✦ Factions Hub"),
    ],
    "lore": [
        ("the-cycle-and-absolvohan.html", "The Cycle"),
        ("the-alpha-tree.html", "Alpha Tree"),
        ("the-three-sorrows.html", "3 Sorrows"),
        ("the-seven-absolute-taboos.html", "7 Taboos"),
        ("the-cheongula-incident.html", "Cheongula"),
        ("the-dawn-of-hope.html", "Dawn of Hope"),
        ("the-dream-realm.html", "Dream Realm"),
        ("daily-life-in-somnarak.html", "Daily Life"),
        ("efflorescence-and-fracture.html", "Efflorescence"),
        ("the-three-ages-and-history.html", "3 Ages"),
        ("index.html", "✦ Lore Hub"),
    ],
    "departments": [
        ("floor-1-neutral-command.html", "F1: Neutral"),
        ("floor-2-maws-keep.html", "F2: Maw's Keep"),
        ("floor-3-extraction-hall.html", "F3: Extraction"),
        ("floor-4-insight-forge.html", "F4: Insight"),
        ("floor-5-border-watch.html", "F5: Border"),
        ("floor-6-deep-vault.html", "F6: Vault"),
        ("floor-7-shadow-corps.html", "F7: Shadow"),
        ("floor-8-gate-watch.html", "F8: Gate"),
        ("facility-room-types.html", "Room Types"),
        ("incident-reports-archive.html", "Incidents"),
        ("index.html", "✦ Dept Hub"),
    ],
    "mechanics": [
        ("han-energy-and-damage.html", "Damage Matrix"),
        ("the-four-work-types.html", "Work Types"),
        ("secc-classification-system.html", "SECC"),
        ("resonant-clash-mechanics.html", "Clash Rules"),
        ("ordeals-framework.html", "Ordeals"),
        ("the-four-ordeals.html", "Four Watches"),
        ("containment-and-suppression.html", "Containment"),
        ("maw-equipment-system.html", "MAW System"),
        ("taboo-resonance-mechanics.html", "Resonances"),
        ("index.html", "✦ Systems Hub"),
    ],
    "locations": [
        ("zone-a-core-nexus.html", "Zone A: Core"),
        ("zone-b-west-ward.html", "Zone B: West"),
        ("zone-c-collectors-row.html", "Zone C: East"),
        ("zone-d-forge-and-gardens.html", "Zone D: Flanks"),
        ("zone-e-perimeter-bulwark.html", "Zone E: Bulwark"),
        ("the-desolate.html", "The Desolate"),
        ("the-maw.html", "The Maw"),
        ("the-library-of-stolen-pasts.html", "Stolen Pasts"),
        ("district-structure-veil-and-raw.html", "Urban Grid"),
        ("index.html", "✦ Atlas Hub"),
    ],
    "entities": [
        ("se-001-the-orphaned-bell.html", "SE-001"),
        ("se-002-the-grieving-colossus.html", "SE-002"),
        ("se-003-the-wilderness-tide.html", "SE-003"),
        ("se-005-the-smothering-mother.html", "SE-005"),
        ("se-007-brume.html", "SE-007"),
        ("se-009-the-memory-weaver.html", "SE-009"),
        ("se-010-the-convergence.html", "SE-010"),
        ("se-011-the-whispering-walls.html", "SE-011"),
        ("se-014-the-debt-eater.html", "SE-014"),
        ("se-015-the-debt-scale.html", "SE-015"),
        ("index.html", "✦ Full Codex"),
    ],
    "characters": [
        ("the-director-majin.html", "1. Majin"),
        ("the-secretary-seiyon.html", "2. Seiyon"),
        ("the-containment-lead-dekan.html", "3. Dekan"),
        ("the-extraction-lead-zyrak.html", "4. Zyrak"),
        ("the-research-lead-ayshuk.html", "5. Ayshuk"),
        ("the-border-lead-mellda.html", "6. Mellda"),
        ("the-archive-lead-marjuk.html", "7. Marjuk"),
        ("the-outsider-ishall.html", "8. Ishall"),
        ("the-exile-xyan.html", "9. Xyan"),
        ("index.html", "✦ Cast Hub"),
    ],
    "maw": [
        ("index.html", "✦ M.A.W. Hub"),
        ("maw-crafting-and-extraction.html", "Extraction"),
        ("maw-set-synergies.html", "Set synergies"),
        ("../mechanics/maw-equipment-system.html", "MAW System"),
    ],
    "atlas": [
        ("hand-of-change-map.html", "Hand of Change"),
        ("somnarak-city-map.html", "City Blueprint"),
        ("../locations/index.html", "✦ Atlas Hub"),
    ],
    "project": [
        ("source-map.html", "Source map"),
        ("../index.html", "✦ Hub"),
    ],
}

SKIP = {
    "index.html",
    "404.html",
    "downloads.html",
    "project/downloads.html",
}

HUD = """
<!-- Tactical Fast-Jump Subpage Bar -->
<div class="fast-jump-nav">
  <span class="fast-jump-title">/// RAPID JUMP:</span>
  <div class="fast-jump-pills">
    {pills}
  </div>
</div>
<!-- Tactical Directive Status HUD -->
<div class="tactical-directive-box">
  <div class="directive-text">
    <span class="led-dot led-green"></span> <b>STATUS:</b> ARCHIVE VERIFIED &nbsp;|&nbsp;
    <b>CLEARANCE:</b> LEVEL-4 OVERSIGHT &nbsp;|&nbsp;
    <b>PROTOCOL:</b> REVERIE DIRECTORATE
  </div>
  <img src="{asset}assets/icons/hud_resonance_wave.svg" alt="Resonance Wave" class="directive-wave">
</div>
<!-- Page Tabs -->
<div class="page-tabs">
<span>ARTICLE</span>
<span>DISCUSSION</span>
<span>SOURCE</span>
<span>HISTORY</span>
<b>YEAR 4,238 · DAWN OF HOPE</b>
</div>
"""


def depth_prefix(rel: str) -> str:
    n = rel.count("/")
    return "../" * n if n else ""


def pill_html(hub: str, filename: str) -> str:
    items = PILLS.get(hub, [("index.html", "✦ Hub")])
    bits = []
    for href, label in items:
        active = " active" if href == filename or href.endswith("/" + filename) else ""
        bits.append(f'<a href="{href}" class="jump-pill{active}">{label}</a>')
    return " ".join(bits)


def restore(path: pathlib.Path) -> str:
    rel = str(path.relative_to(DOCS)).replace("\\", "/")
    if rel in SKIP:
        return "skip"
    t = path.read_text(encoding="utf-8")
    if "left-rail" not in t:
        return "no-rail"
    changed = []
    pfx = depth_prefix(rel)
    hub = rel.split("/")[0] if "/" in rel else ""
    filename = pathlib.PurePosixPath(rel).name

    nav = LEFT_NAV.format(p=pfx)
    t2, n = re.subn(
        r'<nav aria-label="Wiki navigation" class="left-links">.*?</nav>',
        nav.strip(),
        t,
        count=1,
        flags=re.S,
    )
    if n:
        t = t2
        changed.append("left-nav")

    if "RAPID JUMP" not in t and "<main" in t:
        pills = pill_html(hub, filename)
        block = HUD.format(pills=pills, asset=pfx)
        t2, n = re.subn(
            r'(<main[^>]*>)',
            r"\1\n" + block,
            t,
            count=1,
        )
        if n:
            t = t2
            changed.append("rapid-jump")

    if t != path.read_text(encoding="utf-8"):
        path.write_text(t, encoding="utf-8")
        return ",".join(changed) or "ok"
    return "unchanged"


def main():
    counts = {}
    for p in sorted(DOCS.rglob("*.html")):
        if "assets" in p.parts:
            continue
        r = restore(p)
        counts[r] = counts.get(r, 0) + 1
        if r not in ("skip", "no-rail", "unchanged"):
            print(f"{r:20} {p.relative_to(DOCS)}")
    print("counts", counts)


if __name__ == "__main__":
    main()
