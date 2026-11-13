#!/usr/bin/env python3
"""Batch 151 — sentence hygiene: fragments that begin mid-sentence.

Found by reading SE-C-IVδ-909 whole, after two batch-150 numerals were replaced
in it. Two of the thirteen lowercase sentence-starts in the corpus were mine:

    ...the room count matching. the descent record; the count has matched...
    ...no longer needs guarding. nine years of the post's record; the gauge...

The repair for three of them was written by the same session that broke them,
which is the point of reading the file whole rather than the two lines changed.

Two families, one defect: text that reads as a fragment.
  * a sentence that opens on a lowercase word (13 in 301 dossiers)
  * a field whose value re-opens with another field's label — `| **Position /
    movement** | Physical Form: A market stall...` — where the field is answered
    by a label instead of by its own content (5 in 4 dossiers)

Every replacement asserts exactly one match.
"""
import io
import os
import sys

EDITS = [
 # --- broken by batch 150, found by reading the whole file -------------------
 ('SE-C-IVδ-909_Labyrinth_of_the_Unfinished_Mind',
  'room count matching. the descent record; the count has matched in nineteen '
  'descents of every twenty and the nine that did not are the nine pulls.',
  'room count matching. The descent record holds the count: it has matched in '
  'nineteen descents of every twenty, and the nine that did not are the nine pulls.'),
 ('SE-C-IIIγ-033_The_Guarding_Bird',
  "no longer needs guarding. nine years of the post's record; the gauge falls",
  "no longer needs guarding. The post's record runs eleven years; the gauge falls"),

 # --- the same defect, older -------------------------------------------------
 ('SE-C-IIIγ-902_Beating_Relic', 'bare-handed grip. gloved contact', 'bare-handed grip. Gloved contact'),
 ('SE-C-IIβ-280_Pall', 'over a face. this has not happened', 'over a face. This has not happened'),
 ('SE-C-IIβ-565_Broken_Well', 'depth where there is none. workers stop trusting',
  'depth where there is none. Workers stop trusting'),
 ('SE-C-IVγ-073_The_Hollow_Knight', 'becomes structural. walls crack along the route',
  'becomes structural. Walls crack along the route'),
 ('SE-N-IIIγ-160_Broken_Promise', 'or event followed. event adds a fracture',
  'or event followed. An event adds a fracture'),
 ('SE-N-IIIγ-308_Soaking_Shadow', 'on purpose. anger merely carried',
  'on purpose. Anger merely carried'),
 ('SE-N-IIα-125_Hollow_Echo', 'names stop being available. not identity wholesale',
  'names stop being available. Not identity wholesale'),
 ('SE-N-IIβ-319_The_Magistrates_Strike-Through',
  'over compliance. during the great directorate purge of year 4,119',
  'over compliance. During the great Directorate purge of Year 4,119'),
 ('SE-O-IVδ-515_The_Last_Warmth_of_Forty-Two',
  'die in silence. during the great freeze of year 4,188 in sector 09',
  'die in silence. During the Great Freeze of Year 4,188 in Sector 09'),
 ('SE-O-Iα-189_Ephemera', 'must align before Work begins. before Work or contact.',
  'must align before Work begins, before Work or contact.'),

 # --- a field answered by another field's label ------------------------------
 ('SE-C-IIα-062_Forgotten_Market_Stall',
  '- **Position / movement:** Physical Form: A market stall that appears overnight '
  'in the abandoned commerce district.',
  '- **Position / movement:** It stands where it appeared and does not move; by '
  'morning only a warm patch and a chalked outline remain, which is what the next '
  'survey measures from.'),
 ('SE-C-IVδ-255_Rising_Wall',
  '- **Position / movement:** Primary Form: A pressure-shaped humanoid that rises '
  'from the ground as a wall of invisible grief.',
  '- **Position / movement:** Mobile in breach on foot with the cold running ahead '
  'of it, toward wherever there is grief to stand beside.'),
 ('SE-C-IVδ-255_Rising_Wall',
  '| **Position / movement** | Primary Form: A pressure-shaped humanoid that rises '
  'from the ground as a wall of invisible grief. |',
  '| **Position / movement** | It walks the corridors on foot with waves of cold '
  'grief running ahead of it, and it goes toward wherever there is grief to stand '
  'beside; it is not looking for anybody in particular. |'),
 ('SE-C-Vγ-260_Sorrow_Tide',
  '- **Position / movement:** Physical Form: A city-wide wave of concentrated Han '
  'that rises after sunset and recedes at dawn.',
  '- **Position / movement:** Stationary \u2014 the wave does not travel; it rises over '
  'the district after sunset and recedes at dawn, and the almanac prints when.'),
 ('SE-C-Vγ-260_Sorrow_Tide',
  '| **Position / movement** | Physical Form: A city-wide wave of concentrated Han '
  'that rises after sunset and recedes at dawn. |',
  '| **Position / movement** | Stationary \u2014 a place or zone; spreads rather than '
  'moves. What is forecast is the night rather than a route: the almanac is '
  'printed in the ninth month and has called the red-marked nights to within '
  'forty minutes. |'),
]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bases = [os.path.join(root, 'SOMNARAK-WORLD', 'Sorrow_Entities'),
             os.path.join(root, 'SOMNARAK-WORLD', 'Unknown_Entities')]
    texts, problems, done = {}, [], 0
    for stem, old, new in EDITS:
        path = None
        for base in bases:
            for name in os.listdir(base):
                if name.startswith(stem):
                    path = os.path.join(base, name)
        if path is None:
            problems.append(f'{stem}: no file')
            continue
        if path not in texts:
            with io.open(path, encoding='utf-8') as handle:
                texts[path] = handle.read()
        count = texts[path].count(old)
        if count != 1:
            problems.append(f'{os.path.basename(path)}: {count} matches for {old[:60]!r}')
            continue
        texts[path] = texts[path].replace(old, new)
        done += 1
    for path, text in texts.items():
        with io.open(path, 'w', encoding='utf-8') as handle:
            handle.write(text)
    for problem in problems:
        print('  PROBLEM', problem)
    print(f'applied {done} of {len(EDITS)} edits across {len(texts)} files, '
          f'{len(problems)} problems')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
