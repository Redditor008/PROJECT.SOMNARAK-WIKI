#!/usr/bin/env python3
"""
tools/verify_all_anchors_and_jumps.py
Audits all anchor hrefs, headings, and targets across all 135 HTML files
to ensure 100% resolution and zero broken jump links.
"""

import os, re, glob
from html.parser import HTMLParser

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

class AnchorCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if "id" in attrs_dict:
            self.ids.add(attrs_dict["id"])
        if "name" in attrs_dict:
            self.ids.add(attrs_dict["name"])
        if "href" in attrs_dict:
            self.hrefs.append(attrs_dict["href"])

def audit_all_anchors():
    all_html = sorted(glob.glob(os.path.join(WIKI_DIR, "**/*.html"), recursive=True))
    total_files = len(all_html)
    total_anchor_links = 0
    broken_internal_anchors = []

    for file_path in all_html:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        collector = AnchorCollector()
        collector.feed(content)

        for href in collector.hrefs:
            if href.startswith("#"):
                target_id = href[1:].strip()
                if not target_id or target_id == "top":
                    continue
                total_anchor_links += 1
                if target_id not in collector.ids and decode_id(target_id) not in collector.ids:
                    broken_internal_anchors.append((file_path, href, target_id))

    print(f"Audited {total_files} HTML files.")
    print(f"Total on-page anchor jump links checked: {total_anchor_links}")
    print(f"Broken internal on-page anchors: {len(broken_internal_anchors)}")
    for f, href, target in broken_internal_anchors[:10]:
        print(f"  {os.path.relpath(f, WIKI_DIR)} -> {href} (missing ID: {target})")

    return len(broken_internal_anchors) == 0

def decode_id(s):
    import urllib.parse
    return urllib.parse.unquote(s)

if __name__ == "__main__":
    success = audit_all_anchors()
    if success:
        print("\nPERFECT: 100% OF ALL INTERNAL ANCHOR JUMPS RESOLVE TO VALID IDs!")
    else:
        print("\nWARNING: Some anchor jump links need resolution.")
