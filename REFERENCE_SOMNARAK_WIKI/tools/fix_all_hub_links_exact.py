#!/usr/bin/env python3
"""
tools/fix_all_hub_links_exact.py
Aligns all link targets across all hub pages to existing HTML files.
"""

import os, re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

def fix_links():
    mapping = {
        # Characters
        "the-shadow-lead-ishall.html": "the-outsider-ishall.html",
        "the-exile-lead-xyan.html": "the-exile-xyan.html",
        "agent-minho.html": "minho.html",
        "merchant-doha.html": "doha.html",
        "researcher-soojin.html": "soojin.html",
        "sora-civilian.html": "sora.html",
        "captain-taeho.html": "taeho.html",
        "kael-caravan-master.html": "kael.html",
        "yeonhwa-weaver.html": "yeonhwa.html",
        "engineer-joon.html": "joon.html",
        "core-01-majin.html": "the-director-majin.html",
        "core-02-seiyon.html": "the-secretary-seiyon.html",
        "core-03-dekan.html": "the-containment-lead-dekan.html",
        "core-04-zyrak.html": "the-extraction-lead-zyrak.html",
        "core-05-ayshuk.html": "the-research-lead-ayshuk.html",
        "core-06-mellda.html": "the-border-lead-mellda.html",
        "core-07-marjuk.html": "the-archive-lead-marjuk.html",
        "core-08-ishall.html": "the-outsider-ishall.html",
        "core-09-xyan.html": "the-exile-xyan.html",

        # Lore
        "absolvohan-codex.html": "the-cycle-and-absolvohan.html",
        "seven-absolute-taboos.html": "the-seven-absolute-taboos.html",
        "doorspeech-phenomenon.html": "the-doorspeech.html",
        "efflorescence-phenomenon.html": "efflorescence-and-fracture.html",

        # Mechanics
        "damage-system.html": "han-energy-and-damage.html",
        "four-work-types.html": "the-four-work-types.html",

        # Departments
        "floor-1-neutral-core.html": "floor-1-neutral-command.html"
    }

    for root, _, files in os.walk(WIKI_DIR):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    c = f.read()

                modified = False
                for old_link, new_link in mapping.items():
                    if old_link in c:
                        c = c.replace(old_link, new_link)
                        modified = True

                if modified:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(c)

    print("Aligned all hub links to exact files!")

if __name__ == "__main__":
    fix_links()
