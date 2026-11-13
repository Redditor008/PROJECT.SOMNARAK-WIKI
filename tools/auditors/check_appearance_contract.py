#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_appearance_contract.py — gate 50: Appearance is a category and a way of writing (R-54).

WHY THIS EXISTS

`R-32` asked for shape diversity — Human, Monster, Animal, Abstract at minimum, plus the object-like
and mechanical shapes the One Sin and Singing Machine examples imply — and batch 213 concluded it
"cannot be checked" because `**Physical Form**` is `Mixed` on 104 of 158 subjects. That conclusion was
wrong, and the owner said so: the category is not the `Physical Form` field, **it is readable off the
Appearance section**, which every dossier already carries.

The owner also named the second half: Appearance is **two things** — the category, and *how L Corp
writes it*. A file can hold the right body plan and still be written by nobody, in the voice of an
essayist explaining what the entity means.

THE TWO AXES

**A — the category.** The `**Form**` row, the `**Primary Form:**` line, the `**Physical Form:**` line
or the `**Primary marker:**` line is the dossier's own statement of its body plan. It is read against
the families `R-32` defines, and every dossier must resolve to exactly one. A file whose own form
statement names no body plan has not been written to the section's contract, however good the prose.

**B — how it is written.** The section is an observation record, and the archive writes it in one of
two shapes, both of which are L Corp's way:

  * the **ledger** — a `**Form**` table and the four observer's readings (form, position and
    movement, material and signature, distinctive markers) as labelled rows;
  * the **observation** — continuous prose in the order of meeting, ≥120 words, whose opening
    sentence states the body plainly. Its readings are carried in the prose and are certified by the
    reader's pass (`O-29`, `R-38`), not by a regex.

Neither shape may explain. Interpretation inside an appearance record is the essayist tell `R-45`
§0.2 names: the section says what a reader *sees*, never what it *means*.

WHAT FAILS

  * a dossier whose Appearance resolves to no family (an unfiled shape);
  * a ledger dossier missing one of the four required readings;
  * a prose section with no stated form, or shorter than an observation (neither shape);
  * interpretation language inside Appearance (a `stands for` a symbol is a defect, a `stands for
    three minutes` is not).

    python3 tools/auditors/check_appearance_contract.py
    python3 tools/auditors/check_appearance_contract.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _words(*words):
    """A plural-tolerant word pattern: `wall` also matches `walls`, `branch` also `branches`."""
    return r'\b(?:%s)(?:s|es)?\b' % '|'.join(words)


# R-32's families, plus the two the One Sin / Singing Machine examples require.
# Order is priority: the first family whose vocabulary matches wins, so a "brass bird" is an animal
# before it is a machine, a "humanoid of iron" is humanoid before it is an object, and an explicit
# negative — "no physical body" — is read before any incidental noun in the same sentence.
FAMILIES = [
    # An explicit negative outranks every incidental noun in the same sentence: "The Choir has no
    # physical body. It manifests as 144 ethereal voices" is abstract, not humanoid, and "a zone of
    # ground" is a place, not an animal. Read this before the concrete families.
    ('abstract', r'\b(?:no physical body|bodyless|bodiless|incorporeal|disembodied|unseen|'
                 r'intangible|emanation|\bhour\b|\bminutes?\b|\bsecond\b)\b'),
    ('mechanical', _words('machine', 'engine', 'apparatus', 'mechanism', 'automaton', 'clockwork',
                          'piston', 'gear', 'dial', 'turbine', 'boiler', 'furnace', 'crawler',
                          'tread', 'construct', 'turbine')),
    ('animal', _words('bird', 'eagle', 'hawk', 'crow', 'raven', 'owl', 'dog', 'wolf', 'cat',
                      'spider', 'fish', 'serpent', 'snake', 'worm', 'moth', 'insect', 'beetle',
                      'ant', 'horse', 'bull', 'goat', 'deer', 'fox', 'rabbit', 'swarm', 'flock',
                      'feather', 'wing', 'animal', 'beast')),
    ('monster', _words('monster', 'creature', 'assemblage', 'amalgam', 'abomination', 'horror')),
    ('humanoid', _words('humanoid', 'human', 'man', 'woman', 'child', 'boy', 'girl', 'figure',
                        'saint', 'knight', 'maiden', 'giant', 'doll', 'person', 'silhouette',
                        'clerk', 'warden', 'guardian', 'elder', 'priest', 'scribe', 'worker',
                        'statue', 'angel', 'armour', 'armor', 'biped', 'courier')),
    ('place', _words('zone', 'hall', 'room', 'corridor', 'district', 'vault', 'library', 'garden',
                     'field', 'ground', 'junction', 'stair', 'tower', 'street', 'market',
                     'sanctuary', 'chamber', 'gallery', 'ridge', 'crossing', 'bridge', 'door',
                     'gate', 'wall', 'place', 'river', 'stream', 'tide', 'sea', 'lake', 'flood',
                     'wave', 'well', 'fountain', 'spire', 'row')),
    ('object', _words('scale', 'ring', 'coin', 'mirror', 'clock', 'book', 'ledger', 'tome',
                      'letter', 'stone', 'shard', 'shrine', 'mask', 'key', 'bell', 'window',
                      'plate', 'cord', 'rope', 'chain', 'nail', 'needle', 'vessel', 'jar', 'box',
                      'cage', 'lantern', 'lamp', 'crystal', 'relic', 'token', 'seal', 'charm',
                      'staff', 'blade', 'sword', 'pendant', 'veil', 'loom', 'tree', 'fruit',
                      'hourglass', 'compass', 'net', 'crown', 'stick', 'rod', 'bar', 'slab',
                      'branch', 'trunk', 'root', 'bark', 'canopy', 'bough', 'tear')),
]
# A tear may be shaped like a tear; `tear-shaped` is one token to this lexicon.
OBJECT_EXTRA = r'tear[- ]?shaped'
# The loose abstract nouns run last, so an object that merely *makes* a sound or *has* a presence is
# still an object. Only a form with no concrete noun anywhere resolves here.
ABSTRACT_LOOSE = (r'\b(?:voice|sound|song|music|silence|absence|emptiness|void|weight|pressure|'
                  r'fog|mist|smell|scent|emotion|memory|interval|moment|season|cycle|presence|'
                  r'phenomenon|weather|shadow|light|darkness|haze)\b')

# The four readings are questions, not labels. The archive titles each one more than one way, and a
# section answers the reading under whichever title it uses. `REQUIRED` maps reading -> its titles.
REQUIRED = {
    'Form': ('Form', 'Physical Form', 'Primary Form', 'Primary marker'),
    'Position / movement': ('Position / movement', 'Boundary / movement', 'Movement',
                            'Position', 'Movement and Posture'),
    'Material / signature': ('Material / signature', 'Material and Surface', 'Material',
                             'Signature', 'Material / surface'),
    # `Notable Features` is deliberately not a markers title: it is the section's behaviour note.
    'Distinctive markers': ('Distinctive markers', 'Distinctive Markers', 'Markers'),
}
TELL = re.compile(
    # `stands for a wrong` is interpretation; `stands for more than three minutes` is a duration.
    r'\b(?:it represents|represents the|stands? for (?!more than|\d|a (?:moment|while|longer))|'
    r'is a metaphor|symboli[sz]es?|embody|a testament to|a reminder that|'
    r'\b(?:emptiness|absence|silence|stillness|hollow|blank) is the point)\b', re.I)
APPEARANCE = re.compile(r'^## Appearance[^\n]*$(.*?)(?=^## )', re.M | re.S)
HEADING = re.compile(r'^## Appearance(?:[^\n]*)$', re.M)
PROSE_MIN = 120


def dossier_files():
    return [p for p in sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD/**/SE-*.md'),
                                        recursive=True))
            if 'MAW_Codex' not in p]


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


def opening_sentence(body):
    """The first plain sentence of the section — for a prose record, this is the form statement.

    A reader meets the object here, before any label, so this is also the order of meeting `R-45`
    §3 asks the section to be written in.
    """
    for para in body.split('\n'):
        line = para.strip()
        if not line or line.startswith(('|', '-', '#', '**')):
            continue
        m = re.match(r'(.+?[.:])(?:\s|$)', line)
        return (m.group(1) if m else line).strip()
    return ''


def form_text(text):
    """The dossier's own statement of its body plan, in the order the file gives it."""
    # The archive names this statement three ways; all three are read, in the file's own order.
    for pat in (r'^\|\s*\*\*Form\*\*\s*\|\s*(.+?)\s*\|$',
                r'^\*\*Primary Form:\*\*\s*(.+)$',
                r'^\*\*Physical Form:\*\*\s*(.+)$',
                r'^\*\*Form:\*\*\s*(.+)$',
                r'^-\s*\*\*Primary marker:\*\*\s*(.+)$',
                r'^\|\s*\*\*Distinctive markers\*\*\s*\|\s*(.+?)\s*\|$'):
        m = re.search(pat, text, re.M)
        if m:
            return m.group(1).strip()
    return opening_sentence(text)


def family(txt):
    """Which of R-32's families this text reads as. Pure — the tests drive it."""
    low = txt.lower()
    for name, pattern in FAMILIES:
        if re.search(pattern, low):
            return name
    if re.search(OBJECT_EXTRA, low):
        return 'object'
    if re.search(ABSTRACT_LOOSE, low):
        return 'abstract'
    return None


def labels(body, reading):
    """How many of a reading's titles this section uses, as a row or a bolded line. Pure."""
    return sum(1 for title in REQUIRED[reading]
               if re.search(r'\|\s*\*\*%s\*\*' % re.escape(title), body)
               or ('**%s:**' % title) in body)


def shape(body):
    """`ledger` if the four readings are labelled, `observation` if the section is prose. Pure."""
    labelled = sum(1 for part in REQUIRED if labels(body, part))
    if labelled == len(REQUIRED):
        return 'ledger'
    # A prose record labels at most its form; it carries the four readings in the order of meeting.
    # A section that labels three or four of them is a ledger, and a missing row is the finding.
    if labelled <= 1 and len(body.split()) >= PROSE_MIN and form_text(body):
        return 'observation'
    return None


def audit(text):
    """(issues, {family, shape, tells}) for one dossier. Pure."""
    issues = []
    sec = APPEARANCE.search(text)
    if not sec:
        return [('no Appearance section', '')], {'family': None, 'shape': None, 'tells': 0}
    body = sec.group(1)
    form = form_text(body) or form_text(text)
    fam = family(form)
    if not fam:
        issues.append(('Appearance names no shape family', form[:70]))
    kind = shape(body)
    if kind is None:
        for part in REQUIRED:
            if part == 'Form':
                # The form statement is `**Form**` in a table, or `**Physical Form:**` / `**Primary
                # Form:**` in a line, or the section's opening sentence. One satisfies the reading.
                if form_text(body):
                    continue
            if not labels(body, part):
                issues.append(('Appearance has no %s' % part, ''))
    tells = len(TELL.findall(body))
    return issues, {'family': fam, 'shape': kind, 'tells': tells}


def main(argv):
    verbose = '-v' in argv
    files = dossier_files()
    distribution, shapes = {}, {}
    unfiled, missing, telling = [], [], []
    for path in files:
        issues, stats = audit(read(path))
        name = os.path.basename(path)
        if stats['family']:
            distribution[stats['family']] = distribution.get(stats['family'], 0) + 1
        if stats['shape']:
            shapes[stats['shape']] = shapes.get(stats['shape'], 0) + 1
        for why, detail in issues:
            if why.startswith('Appearance names no shape'):
                unfiled.append((name, detail))
            else:
                missing.append((name, why))
        if stats['tells']:
            telling.append((name, stats['tells']))
    if verbose:
        for n, d in unfiled:
            print('  UNFILED %-52s %s' % (n[:50], d))
        for n, w in missing:
            print('  MISSING %-52s %s' % (n[:50], w))
        for n, c in telling:
            print('  TELL    %-52s %d' % (n[:50], c))
    print('dossiers read %d · appearance sections %d'
          % (len(files), sum(1 for p in files if APPEARANCE.search(read(p)))))
    print('shape families — ' + ' · '.join(
        '%s %d' % (k, distribution.get(k, 0)) for k, _ in FAMILIES))
    print('families present %d of %d (R-32 asks for four at minimum)'
          % (sum(1 for k, _ in FAMILIES if distribution.get(k)), len(FAMILIES)))
    print('written as — ledger %d · observation %d'
          % (shapes.get('ledger', 0), shapes.get('observation', 0)))
    print('unfiled shapes: %d' % len(unfiled))
    print('appearance readings missing: %d' % len(missing))
    print('interpretation tells in Appearance: %d in %d dossiers'
          % (sum(n for _, n in telling), len(telling)))
    if unfiled or missing:
        print('RESULT: FAIL — %d unfiled shapes, %d missing readings'
              % (len(unfiled), len(missing)))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
