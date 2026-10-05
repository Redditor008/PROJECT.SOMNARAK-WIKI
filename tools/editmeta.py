#!/usr/bin/env python3
"""editmeta.py [dir ...] — candidate R-01 (No Edit-Meta) sentences in the dossiers.

R-01: no file in SOMNARAK-WORLD/ may mention that it was edited. The forbidden shapes are
reconciliation notes about earlier wording ("has been corrected against the Behavior table",
"the earlier entry naming Viderehan primary", "the passage formerly here ... has been
removed", "three previous versions of this file offered one").

This FINDS candidates; it never edits. The test R-01 gives is a human one: is the thing that
changed a fact in the world, or a line in this file? In-world administrative history is
content ("the management condition was rewritten in Year 4231", a withdrawn tale) and is not
matched here on purpose. A flagged line is fixed by converting the correction into cause:
the fact survives, the seam does not. Each conversion is written from the one file and is
at least as long as the sentence it replaces (R-02, R-04).

Usage:
    editmeta.py                         # Sorrow_Entities and Unknown_Entities
    editmeta.py SOMNARAK-WORLD/Katabagil
"""
import collections
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIRS = ['SOMNARAK-WORLD/Sorrow_Entities', 'SOMNARAK-WORLD/Unknown_Entities']

PATTERN = re.compile(
    r"(?:has|have) been corrected (?:against|to match)"
    r"|corrected against the"
    r"|previously carried here|passage formerly|formerly here"
    r"|(?:earlier|previous|older|former) (?:version|entry|draft|account|attribution)s?"
    r" (?:of|naming|offered|said|had|requiring|required|recorded)"
    r"|Every earlier version|Three previous versions"
    r"|(?:was|were|been) withdrawn as intrusive",
    re.I)


def main(dirs):
    by_file = collections.defaultdict(list)
    for d in dirs:
        base = d if os.path.isabs(d) else os.path.join(ROOT, d)
        for path in sorted(glob.glob(os.path.join(base, '**', '*.md'), recursive=True)):
            with io.open(path, encoding='utf-8') as fp:
                for n, line in enumerate(fp, 1):
                    m = PATTERN.search(line)
                    if m:
                        a, b = max(0, m.start() - 70), min(len(line), m.end() + 90)
                        by_file[path].append((n, line.strip()[a:b] if a else line.strip()[:b]))
    for path in sorted(by_file):
        print(os.path.relpath(path, ROOT))
        for n, text in by_file[path]:
            print('  L%-4d %s' % (n, text))
    corrected = sum(1 for v in by_file.values() if any('corrected' in t.lower() for _, t in v))
    print('\n%d dossier(s), %d candidate line(s); %d mention "corrected" (candidates, not verdicts:'
          ' some are in-world, e.g. "neither is corrected against the other")'
          % (len(by_file), sum(len(v) for v in by_file.values()), corrected))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or DEFAULT_DIRS))
