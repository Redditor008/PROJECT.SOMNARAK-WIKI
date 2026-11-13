#!/usr/bin/env python3
"""
tools/auditors/check_set_agreement.py

Do the four pages of one M.A.W. set agree about the entity behind them?

A set is four dossiers — A (Side Codex), B (Weapon), C (Suit), D (Stigma) — all
describing one entity. Each carries the same SECC header fields. If the A page
calls the entity Fragment (III) and the C page calls it Entity (IV), then one of
them is wrong and a reader has no way to choose.

This is the last of the three lenses run over this archive:

  check_dossier_consistency  one dossier against itself
  check_sourcing             one dossier against the other three hundred
  check_set_agreement        four dossiers against their own set

Deliberately narrow. It compares only fields that are properties of the ENTITY
and therefore must be identical across the set. It does not compare `Element`
values naively, because the Suit page files `Multiplier` as a slot scheme rather
than an element, and it does not compare anything about the ITEM, which differs
by design — a weapon and a charm are not supposed to share a potency profile.

A value that merely carries a longer note is not a disagreement: "Weight" and
"Weight — Amber" are the same element, one with a note. The comparison strips to
the leading term before judging.
"""

import collections
import glob
import os
import re
import sys

SETS = 'SOMNARAK-WORLD/MAW_Codex_Sets/**/SE-*.md'

# properties of the entity: identical across all four pages, or one page is wrong
ENTITY_FIELDS = ['Potency', 'Coherence', 'Sorrow Category', 'Risk tier']

# the Suit page files a slot scheme here rather than an element
SUIT_ELEMENT = 'Multiplier'

RATCHET = {
    'sibling-disagreement': 0,
}


def leading(value):
    """'Weight — Amber' and 'Weight; braided …' are both Weight."""
    v = value.strip()
    v = re.split(r'\s*(?:—|–|;|,)\s*', v)[0]
    return v.strip().lower()


def field(text, label):
    m = re.search(r'\|\s*\*{0,2}' + re.escape(label) + r'\*{0,2}\s*\|\s*([^|\n]*)\|', text, re.I)
    return m.group(1).strip() if m else None


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv

    sets = collections.defaultdict(dict)
    for p in glob.glob(SETS, recursive=True):
        m = re.match(r'(SE-[0-9A-Za-zαβγδω\-]+)-([ABCD])__', os.path.basename(p))
        if not m:
            continue
        with open(p, encoding='utf-8') as f:
            sets[m.group(1)][m.group(2)] = (p, f.read())

    defects = []

    for base, pages in sets.items():
        if len(pages) < 2:
            continue

        for label in ENTITY_FIELDS:
            seen = {}
            for let, (p, t) in pages.items():
                v = field(t, label)
                if v is None:
                    continue
                k = leading(v)
                seen.setdefault(k, []).append(let)
            if len(seen) > 1:
                detail = ' · '.join(f'{"/".join(sorted(lets))}={k}' for k, lets in seen.items())
                defects.append((base, f'{label} differs across the set: {detail}'))

        elems = {}
        for let, (p, t) in pages.items():
            v = field(t, 'Element')
            if v is None:
                continue
            k = leading(v)
            if k == SUIT_ELEMENT.lower() and let == 'C':
                continue                      # the Suit files a slot scheme, not an element
            elems.setdefault(k, []).append(let)
        if len(elems) > 1:
            detail = ' · '.join(f'{"/".join(sorted(lets))}={k}' for k, lets in elems.items())
            defects.append((base, f'Element differs across the set: {detail}'))

    n = len(defects)
    ceiling = RATCHET['sibling-disagreement']
    print(f'SET AGREEMENT — {len(sets)} sets, {sum(len(v) for v in sets.values())} pages')
    if n > ceiling:
        print(f'  sibling-disagreement {n}   ABOVE CEILING {ceiling} — a set disagrees with itself')
        for base, why in defects:
            print(f'      {base:14} {why}')
    elif n < ceiling:
        print(f'  sibling-disagreement {n}   BELOW CEILING — lower it to {n}')
    else:
        print(f'  sibling-disagreement {n}   at ceiling')
    if verbose:
        for base, why in defects:
            print(f'      {base:14} {why}')
    ok = n == ceiling
    print('RESULT: ' + ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
