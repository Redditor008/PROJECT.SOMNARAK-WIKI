#!/usr/bin/env python3
"""
tools/auditors/check_entity_links.py

A finished wiki page hands the reader onward. Every dossier here has an
`Entity Interaction Record` naming the records it relates to — and until batch 146
**not one of the 301 dossiers contained a single internal link.** The catalog linked
down to them; nothing linked back or sideways. A reader who landed in a dossier was
stranded.

WHAT THE EXTERNAL MODELS DO
  A Lobotomy Corporation abnormality page carries a navigation footer and an E.G.O.
  block that names the related entries. An SCP article closes with a wikiwalk
  (`<< SCP-XXXW | SCP-XXXX | SCP-XXXY >>`) and cross-references its addenda. In both,
  a named thing that has a page is a link.

WHAT THIS CHECKS
  In every `| Related entity |` table, a cell naming an entity that resolves to
  exactly one filed record must be written as a markdown link to it.

  Resolution uses, in order: the record's own title, its filename stem, and the
  catalog's `also rendered` alias. A name that matches **more than one** record is
  deliberately *not* a defect — an ambiguous name must stay plain text rather than
  become a wrong link. `SE-N-IIIγ-127`'s alias collided with `SE-C-IIα-081`'s title
  exactly once, and that collision is disambiguated in the catalog, not papered over
  with a guess.

WHAT IS NOT A DEFECT
  A name with no filed record — "the Sorrow River", "the Sunken Bridge" — stays plain.
  Filing a page to satisfy a link count would be inventing canon.

Ceiling 0, ratcheted both ways.
"""

import collections
import glob
import io
import os
import re
import sys

ROOT = os.getcwd()
ENTITY_GLOBS = [
    os.path.join(ROOT, 'SOMNARAK-WORLD', 'Sorrow_Entities', 'SE-*.md'),
    os.path.join(ROOT, 'SOMNARAK-WORLD', 'Unknown_Entities', '*.md'),
    os.path.join(ROOT, 'SOMNARAK-WORLD', 'Hope_Transformations', '*.md'),
]
CATALOG = os.path.join(ROOT, 'REFERENCE_SOMNARAK_WIKI', 'REGISTRY',
                       'SORROW_ENTITIES_CATALOG.md')
RATCHET = 0

TABLE_ROW = re.compile(r'^\|\s*([^|]+?)\s*\|')


def key(s):
    return re.sub(r'\s+', ' ', s).strip().lower()


def build_index():
    """name -> file, only where exactly one file answers to it."""
    idx = collections.defaultdict(set)
    for pattern in ENTITY_GLOBS:
        for path in glob.glob(pattern):
            rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
            with io.open(path, encoding='utf-8') as fh:
                text = fh.read()
            m = re.search(r'^#\s+(.+?)\s*—', text, re.M) or re.search(r'^#\s+(.+)$', text, re.M)
            if m:
                k = key(m.group(1))
                idx[k].add(rel)
                if k.startswith('the '):
                    idx[k[4:]].add(rel)
            stem = re.sub(r'^(SE-[^_]+|UNK_[^_]+)_', '', os.path.basename(path))
            stem = re.sub(r'_[^_]*\.md$', '', stem)
            idx[key(stem.replace('_', ' '))].add(rel)
    if os.path.exists(CATALOG):
        with io.open(CATALOG, encoding='utf-8') as fh:
            cat = fh.read()
        for m in re.finditer(r'\| `(SE-[^`]+)` \| \*\*([^*]+)\*\*'
                             r'(?: \(also rendered \*([^*]+)\*[^)]*\))? \|', cat):
            code, title, alias = m.group(1), m.group(2), m.group(3)
            hits = [os.path.relpath(p, ROOT).replace(os.sep, '/')
                    for p in glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', '**',
                                                    os.path.basename(code) + '_*.md'),
                                       recursive=True)]
            if not hits:
                continue
            for nm in (title, alias):
                if not nm:
                    continue
                k = key(nm)
                idx[k].add(hits[0])
                if k.startswith('the '):
                    idx[k[4:]].add(hits[0])
    return {k: next(iter(v)) for k, v in idx.items() if len(v) == 1}


def scan(path, index):
    """Return [(line_no, name, why)] for resolvable names left unlinked."""
    out = []
    with io.open(path, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    in_block = False
    for n, line in enumerate(lines, 1):
        if line.strip().startswith('| Related entity |'):
            in_block = True
            continue
        if in_block and not line.startswith('|'):
            in_block = False
            continue
        if not in_block or set(line.strip()) <= set('|-: '):
            continue
        m = TABLE_ROW.match(line)
        if not m:
            continue
        cell = m.group(1)
        if '](' in cell:
            continue                      # already a link
        name = re.sub(r'[*\[\]]', '', re.sub(r'\s*\([^)]*\)', '', cell)).strip()
        if not name:
            continue
        k = key(name)
        target = index.get(k) or index.get(k[4:] if k.startswith('the ') else k)
        if target:
            out.append((n, name, target))
    return out


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    index = build_index()
    defects = []
    linked = 0
    files = sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', 'Sorrow_Entities', '*.md'))
                   + glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', 'Unknown_Entities', '*.md')))
    for path in files:
        with io.open(path, encoding='utf-8') as fh:
            linked += fh.read().count('| Related entity |')
        for line_no, name, target in scan(path, index):
            defects.append((os.path.relpath(path, ROOT), line_no, name, target))

    print(f'ENTITY LINKS — {len(files)} dossiers · {len(index)} unique names · '
          f'{linked} interaction tables')
    if verbose:
        for rel, line_no, name, target in defects[:40]:
            print(f'      {rel}:{line_no}  {name:32} -> {target.split("/")[-1][:48]}')
    print(f'  unlinked-but-resolvable  {len(defects)}   ceiling {RATCHET}')
    if len(defects) > RATCHET:
        print(f'RESULT: FAIL — {len(defects)} ABOVE CEILING {RATCHET}')
        return 1
    if len(defects) < RATCHET:
        print(f'RESULT: FAIL — BELOW CEILING, lower it to {len(defects)}')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
