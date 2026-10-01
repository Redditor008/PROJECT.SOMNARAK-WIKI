#!/usr/bin/env python3
"""
Shared-line (boilerplate) reporter for the Sorrow Entity dossiers.

V7-5: two good-faith measurements of "how much of a dossier is boilerplate"
disagreed — 13.4% and ~37% — because they counted different lines. This tool
reports every scope side by side so the number is never ambiguous again.

SCOPES
  prose    Narrative sentences only. Excludes table rows, headings, block
           quotes, code fences AND bullet list items. This is the narrowest
           reading and the one that produced 13.4%. It understates the reader's
           experience badly, because most dossier body text is bulleted.
  body     Prose plus bullet list items: everything a reader reads as content,
           excluding only tables, headings and fences. This is the headline
           number and the one to quote.
  all      Every non-heading, non-fence line, including table rows. Table rows
           are largely fixed schema (labels and units), so this scope always
           looks worst and is included only for completeness.

A line counts as shared when its normalised form appears in at least
--threshold distinct dossiers. Normalisation replaces the entity's own name
and code with placeholders, so per-entity name substitution does not disguise
an otherwise identical line (the defect behind the retracted V5-12 figure).
"""

import argparse
import collections
import glob
import os
import re
import sys

ENTITY_DIR = "SOMNARAK-WORLD/Sorrow_Entities"
DEFAULT_THRESHOLD = 30

SCOPES = {
    "prose": lambda s: len(s) > 40 and not s.startswith(("|", "#", ">", "-", "*", "`")),
    "body": lambda s: len(s) > 40 and not s.startswith(("|", "#", ">", "`")),
    "all": lambda s: len(s) > 0 and not s.startswith(("#", "`")),
}


def dossiers(directory=ENTITY_DIR):
    return [f for f in sorted(glob.glob(os.path.join(directory, "*.md")))
            if re.match(r"SE-[^_]+_", os.path.basename(f))]


def identity(path):
    """(english name, SE code) parsed from the filename."""
    base = os.path.basename(path)[:-3]
    m = re.match(r"(SE-[^_]+)_(.*)", base)
    if not m:
        return None, None
    code = m.group(1)
    parts = m.group(2).split("_")
    cut = next((i for i, p in enumerate(parts)
                if re.search(r"[\uac00-\ud7af]", p)), len(parts))
    return " ".join(parts[:cut]), code


def normalise(line, name, code):
    s = re.sub(r"\s+", " ", line.strip())
    if code:
        s = s.replace(code, "«C»")
    if name:
        s = s.replace(name, "«N»")
        bare = re.sub(r"^The\s+", "", name)
        if bare and bare != name:
            s = s.replace(bare, "«N»")
    return s


def collect(files, keep):
    """Returns (ordered lines per file, file-count per normalised line)."""
    per_file = []
    counts = collections.Counter()
    for f in files:
        name, code = identity(f)
        with open(f, "r", encoding="utf-8") as fp:
            lines = [normalise(l, name, code) for l in fp.read().split("\n")
                     if keep(l.strip())]
        per_file.append((f, lines))
        for u in set(lines):
            counts[u] += 1
    return per_file, counts


def measure(files, scope, threshold):
    per_file, counts = collect(files, SCOPES[scope])
    total = sum(len(l) for _, l in per_file)
    shared = sum(1 for _, lines in per_file for u in lines if counts[u] >= threshold)
    return total, shared, counts, per_file


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD,
                    help="a line is 'shared' at this many distinct dossiers (default 30)")
    ap.add_argument("--top", type=int, default=10, help="worst offending lines to list")
    ap.add_argument("--dir", default=ENTITY_DIR)
    args = ap.parse_args()

    print("=== PROJECT SOMNARAK // DOSSIER BOILERPLATE REPORT ===")
    files = dossiers(args.dir)
    if not files:
        print(f"[FAIL] no dossiers found under {args.dir}")
        return 1
    print(f"Corpus: {len(files)} dossiers in {args.dir}")
    print(f"Shared = identical in >= {args.threshold} distinct dossiers "
          f"(entity name and code normalised).\n")

    print(f"{'SCOPE':8} {'LINES':>8} {'SHARED':>8} {'SHARE':>8}   MEANING")
    meaning = {
        "prose": "narrative sentences only (excludes bullets)",
        "body":  "prose + bullets = what a reader reads  <-- headline",
        "all":   "everything incl. table rows (fixed schema)",
    }
    headline = None
    for scope in ("prose", "body", "all"):
        total, shared, _, _ = measure(files, scope, args.threshold)
        pct = (shared / total * 100) if total else 0.0
        if scope == "body":
            headline = pct
        print(f"{scope:8} {total:8} {shared:8} {pct:7.1f}%   {meaning[scope]}")

    # Thresholds, on the headline scope.
    print(f"\nHeadline scope 'body' at other thresholds:")
    for thr in (2, 3, 8, 30):
        total, shared, _, _ = measure(files, "body", thr)
        print(f"  shared by >= {thr:2} dossiers : {shared/total*100:5.1f}%")

    # Worst offenders on the headline scope.
    total, shared, counts, _ = measure(files, "body", args.threshold)
    print(f"\nWorst offending lines (scope 'body'):")
    for text, n in counts.most_common(args.top):
        snippet = text if len(text) <= 88 else text[:85] + "..."
        print(f"  {n:4} files | {snippet}")

    # Per-section breakdown on the headline scope.
    sec = collections.defaultdict(list)
    for f in files:
        name, code = identity(f)
        cur = "(preamble)"
        for raw in open(f, "r", encoding="utf-8").read().split("\n"):
            s = raw.strip()
            if s.startswith("## "):
                cur = s[3:].strip()
                continue
            if SCOPES["body"](s):
                sec[cur].append(normalise(s, name, code))
    print(f"\nMost templated sections (scope 'body', >=200 lines):")
    rows = []
    for title, lines in sec.items():
        if len(lines) < 200:
            continue
        sh = sum(1 for u in lines if counts[u] >= args.threshold)
        rows.append((sh / len(lines) * 100, title, len(lines)))
    for pct, title, n in sorted(rows, reverse=True)[:10]:
        print(f"  {pct:5.1f}%  {title[:44]:44} ({n} lines)")

    print(f"\nHEADLINE: {headline:.1f}% of dossier body lines are shared by "
          f"{args.threshold}+ dossiers.")
    print("This tool reports only. It does not pass or fail a build.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
