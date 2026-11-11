#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_backstory_appearance.py — gate 53: the extended file is built on the dossier (R-57, O-43).

WHY THIS EXISTS

The owner read `01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md` and said it *"doesnt make sense"* and
*"not at all make logical sense"*, and gave the instruction that produced this gate:

> *"YOU SHOULD HAVE READ THE DOSSIER FIRST THAN MAKE THE BACKSTORY EXTENDED VERSION AND IF YOU
> ALREADY FORGET WE USED L CORP STYLE OF WHAT IT LOOK IT LOOK LIKE AND THE GUIDE STYLE HOW ITS READ"*

The Extended file ran to 14,700 words and never once showed the man. The fusion — the single most
visual event in his life — was written as *"he remembers heat, and the smell of the lamp, and the
ceiling"*. His dossier devotes a whole `## Appearance` section to black veins running from the inner
upper arm across the elbow to a scythe-shaped mark at the wrist, three hooked scars on the upper
left of his face, deep blue eyes, silver at the temples, and a coat cut open along the left sleeve
so the mark can be checked. None of it was in the Extended. Not one word.

So this gate asks the one question that fault answers: **was the dossier read first?**

THE MEASUREMENT

For each `Backstory_Extended` file it finds the matching dossier, takes the **physical descriptors**
from that dossier's `## Appearance` section — body parts, colours, materials, garments, marks — and
counts how many of them the Extended file actually uses.

`01_MAJIN` scored **8 of 22** before this batch and **18 of 22** after it. The measurement is taken
over the narrative body only, never the appendix: the old file named *three hooked scars* and
*scythe mark* in its own HOLD table while never showing either in a scene, and a check that counted
the appendix would have scored that as describing him when it never did once.

WHAT FAILS

  * a file below the floor whose reading is not recorded in `DEBT` (new debt);
  * a recorded file that gets worse.

A file may pass below the floor only by being listed, so the remainder is always printed. What this
cannot check is whether the words are used to *show* the character or merely named in passing. That
is the reader's pass (`O-29`, `R-38`).

    python3 tools/auditors/check_backstory_appearance.py
    python3 tools/auditors/check_backstory_appearance.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, 'SOMNARAK-WORLD', 'Echo_Cores', 'Backstory_Extended')
CORES = os.path.join(ROOT, 'SOMNARAK-WORLD', 'Echo_Cores')

# What an Appearance section can be expected to name: the body, what it is wearing, what it is made
# of, and the marks on it. Deliberately narrow — this is not a vocabulary test.
PHYSICAL = set("""
eyes eye hair temple temples scar scars arm arms wrist hand hands palm face cheek cheeks jaw neck
shoulder shoulders chest skin vein veins finger fingers knuckle knuckles nail nails sleeve sleeves
coat collar shirt uniform armour armor boot boots glove gloves mask helm helmet visor blade lens
cable cables alloy silver grey gray black white blue red gold green brown pale porcelain glass iron
steel brass copper stone bone cloth leather silk wool scythe mark hook hooked freckle tattoo chain
ring thread stitch rib ribs tooth teeth throat brow lip lips mouth ear ears skull
""".split())

FLOOR = 0.5          # half of the dossier's physical vocabulary must reach the Extended file
WORD = re.compile(r"[A-Za-z][A-Za-z'-]+")

# Measured 2026-10-25, batch 217. Ratio, used, available. Majin is fixed and not listed.
DEBT = {
    '02_SEIYON_THE_SECRETARY_BACKSTORY_EXTENDED.md': (4, 14),
    '03_DEKAN_THE_CONTAINMENT_LEAD_BACKSTORY_EXTENDED.md': (10, 24),
    '04_ZYRAK_THE_EXTRACTION_LEAD_BACKSTORY_EXTENDED.md': (13, 28),
    '05_AYSHUK_THE_RESEARCH_LEAD_BACKSTORY_EXTENDED.md': (9, 27),
    '07_MARJUK_THE_ARCHIVE_LEAD_BACKSTORY_EXTENDED.md': (6, 24),
    '08_ISHALL_THE_OUTSIDER_BACKSTORY_EXTENDED.md': (10, 23),
    '09_XYAN_THE_EXILE_BACKSTORY_EXTENDED.md': (8, 25),
}


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


def dossier_for(backstory):
    """`01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md` -> `THE_DIRECTOR.md`."""
    name = os.path.basename(backstory)
    stem = re.sub(r'^0\d_[A-Z]+_', '', name).replace('_BACKSTORY_EXTENDED.md', '')
    return os.path.join(CORES, (stem if stem.startswith('THE_') else 'THE_' + stem) + '.md')


def narrative(text):
    """The story only. The appendix is the file talking *about* the story.

    This is the measurement that matters: the old Majin file named 'three hooked scars' and
    'scythe mark' in its own HOLD table while never showing either in a scene. Counting the
    appendix would have scored that file as describing him. It never did once.
    """
    i = text.find('\n## Appendix')
    return text if i < 0 else text[:i]


def appearance_vocabulary(dossier_text):
    """The physical descriptors the dossier's Appearance section names. Pure."""
    # `\Z` as well as the next heading: a section that ends the file is still a section.
    m = re.search(r'^## Appearance[ \t]*$(.*?)(?=^## |\Z)', dossier_text, re.M | re.S)
    if not m:
        return set()
    return {w.lower() for w in WORD.findall(m.group(1))} & PHYSICAL


def audit(backstory_text, dossier_text):
    """(used, available, missing) for one pair, over the narrative body only. Pure."""
    vocab = appearance_vocabulary(dossier_text)
    body = {w.lower() for w in WORD.findall(narrative(backstory_text))}
    used = vocab & body
    return len(used), len(vocab), sorted(vocab - body)


def main(argv):
    verbose = '-v' in argv
    rows, new_debt, regressions = [], [], []
    for path in sorted(glob.glob(os.path.join(DIR, '*.md'))):
        name = os.path.basename(path)
        dossier = dossier_for(path)
        if not os.path.exists(dossier):
            rows.append((name, 0, 0, 0.0, 'no dossier'))
            new_debt.append((name, 'no dossier'))
            continue
        used, avail, missing = audit(read(path), read(dossier))
        ratio = (used / avail) if avail else 0.0
        rows.append((name, used, avail, ratio, ''))
        below = ratio < FLOOR
        if below and name not in DEBT:
            new_debt.append((name, '%d of %d' % (used, avail)))
        if name in DEBT and used < DEBT[name][0]:
            regressions.append((name, '%d was %d' % (used, DEBT[name][0])))
        if verbose:
            print('  %-48s %2d/%-2d  %.0f%%%s%s'
                  % (name[:46], used, avail, ratio * 100,
                     '  DEBT' if name in DEBT else '',
                     ('  missing: ' + ', '.join(missing[:6])) if missing and ratio < FLOOR else ''))
    fixed = [r for r in rows if r[3] >= FLOOR]
    print('backstory files %d · at or above the floor %d · carried as debt %d'
          % (len(rows), len(fixed), len(DEBT)))
    if DEBT:
        worst = min(DEBT.items(), key=lambda kv: kv[1][0] / kv[1][1])
        print('worst recorded: %s — %d of %d physical descriptors'
              % (worst[0][:44], worst[1][0], worst[1][1]))
    print('new debt: %d · regressions: %d' % (len(new_debt), len(regressions)))
    for name, why in new_debt:
        print('  NEW  %-46s %s' % (name[:44], why))
    for name, why in regressions:
        print('  WORSE %-45s %s' % (name[:44], why))
    if new_debt or regressions:
        print('RESULT: FAIL — %d new, %d regressed' % (len(new_debt), len(regressions)))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
