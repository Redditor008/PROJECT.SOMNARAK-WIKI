#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_title_register.py — gate 55: a name keeps its costume (R-61, O-46).

WHY THIS EXISTS

The owner read `01_MAJIN` and said:

> *"SOME IN THE STORY NEED HIGHLIGHTING LIKE P.S. SPECIFIC TITLE AND SUCH SO IT ABLE TO BE KNOW BY
> READER THAT IT WAS A TITLE OR ELSE AND NOT JUST NONSENSE"*

He was reading a file that wrote the same designation four different ways:

    **THE ORIGINAL**        (bold caps, at its coinage)
    *the Original*          (italic, three later uses)
    the Original            (roman, in the appendix)
    THE ORIGINAL            (caps, in the appendix)

and that used *the Hand*, *the Absolvohan*, *Reaper Hungered* and *Ω* with no mark at all. A reader
meeting `the Hand` for the first time in a heading has no way to know it is the name of a structure
rather than a body part. That is the "nonsense" he named, and it is not a matter of taste — it is a
name that changes costume, which reads as four unrelated things.

THE REGISTER

Three classes, one mark each, and the mark is decided by what the thing *is*:

| class | mark | example | because |
|---|---|---|---|
| **Designation** | full caps | `THE ORIGINAL` | An institutional label standing where a name should be. Caps say *this is a filing, not a description.* |
| **Named thing** | italic at coinage, roman after | `*Reaper Hungered*` then `Reaper Hungered` | An entity, weapon, account or structure the record has named. Marked once, when the reader needs to know it is a name. |
| **Office** | roman, lower case after *the* | `the Director` | A post, not a person, and never a name. |

WHAT FAILS

  * a designation written in more than one casing inside one file;
  * a declaration in `REGISTER` whose mark does not match the file;
  * a file using a declared designation without declaring it.

WHAT IT DOES NOT DO

It cannot tell whether a name is *good*. `*Reaper Hungered*` passes whether it is evocative or silly.
That is the reader's pass (`O-29`, `R-38`).

    python3 tools/auditors/check_title_register.py
    python3 tools/auditors/check_title_register.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, 'SOMNARAK-WORLD', 'Echo_Cores', 'Backstory_Extended')
CORES = os.path.join(ROOT, 'SOMNARAK-WORLD', 'Echo_Cores')

# designation -> the file it must appear in, and the casings that are WRONG for it.
# A designation is set in full caps, always, wherever it stands in place of a name.
DESIGNATIONS = {
    'THE ORIGINAL': '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md',
}
# The lower-case word `original` is ordinary English ("they were the original") and is not a casing
# of the designation. Only a capitalised spelling is a claim to be the name.
WRONG_CASINGS = {
    'THE ORIGINAL': ('the Original', 'The Original'),
}

# Named things: italic exactly once, at the coinage, then roman. Checked only for "is the coinage
# marked", not for every later use, because after the coinage the capital letter does the work.
NAMED_THINGS = {
    '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md': (
        'Han', 'the Cheongula', 'the Veil', 'the Maw', 'the Weeping', 'the Hand of Change',
        'Reaper Hungered', 'the Absolvohan', 'the Sovereign', 'the Cycle',
    ),
}

# Bodies: a faction, school, order or council. The mark is a CAPITAL ARTICLE — `The Endurers`,
# `The Council of Sighs` — because a capital article is how English says "this is part of the name".
# The mark only works where it can be seen: at the start of a sentence every word is capitalised, so a
# body whose first appearance is sentence-initial has no mark at all. That is the defect this checks.
BODIES = {
    '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md': (
        'The Endurers', 'The Converters', 'The Council of Sighs',
    ),
}

# A short form is legal only after the long form has been coined. The reader was told what the Hand
# was; `the Hand` after that is the reader's own shorthand, not a second unexplained name.
SHORT_FORMS = {
    '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md': {'the Hand': 'the Hand of Change'},
}

# A roman line is never set in caps, but a *record header* and an in-world document title are not
# lines of narration. This is the whitelist of caps that may stand in narration undecorated.
ALLOWED_CAPS = {'R.D.', 'P.S.', 'M.A.W.', 'Ω', 'CH-202', 'GATE', 'ZONE', 'FLOOR'}


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


REGISTER_LINE = re.compile(r'^> \*\*REGISTER:\*\*.*$', re.M)


def narrative(text):
    """The story, plus the record header minus the register legend.

    The legend names a designation as an example, so leaving it in would make every file look like it
    used a designation it never declared.
    """
    i = text.find('\n## Appendix')
    body = text if i < 0 else text[:i]
    return REGISTER_LINE.sub('', body)


def casings(missing_name):
    """Every casing of a designation found in a text, by shape."""
    stem = missing_name.title()
    return (missing_name, stem, missing_name.lower())


def audit_designation(text, name):
    """(bad casings found, uses found). Pure."""
    body = narrative(text)
    bad = []
    for wrong in WRONG_CASINGS.get(name, ()):
        pattern = r'(?<![A-Za-z])' + re.escape(wrong) + r'(?![A-Za-z])'
        if re.search(pattern, body):
            bad.append(wrong)
    uses = len(re.findall(r'(?<![A-Za-z*])' + re.escape(name) + r'(?![A-Za-z*])', body))
    if uses == 0:   # it may be set inside asterisks at every use
        uses = len(re.findall(r'(?<![A-Za-z])' + re.escape(name) + r'(?![A-Za-z])', body))
    return bad, uses


def prose_only(text):
    """Narration only: no appendix, no record header, no headings, no table rows.

    A movement heading is a title of a section, not the place a term is coined, and a table row is
    apparatus. What a reader walks through is the prose.
    """
    body = narrative(text)
    lines = [l for l in body.split('\n')
             if not l.startswith('#') and not l.lstrip().startswith('|')]
    return '\n'.join(lines)


def _pattern(name):
    """A name whose first word is `the` may be capitalised when it opens a sentence."""
    if name.startswith('the '):
        return '(?:the|The) ' + re.escape(name[4:])
    return re.escape(name)


def sentence_start(body, pos):
    """True if `pos` opens a sentence or a paragraph."""
    line_start = body.rfind('\n', 0, pos) + 1
    if body[line_start:pos].strip() == '':
        return True
    return bool(re.search(r'[.!?]\s+$', body[max(0, pos - 4):pos]))


def audit_body(text, name):
    """(visible, reason) for a body's coining. Pure."""
    body = prose_only(text)
    core = name[4:] if name.startswith('The ') else name
    m = re.search(r'(?<![A-Za-z])' + re.escape(core) + r'(?![A-Za-z])', body)
    if not m:
        return None, 'never used'
    article = body[max(0, m.start() - 4):m.start()]
    if article.lower().endswith('the '):
        capital = article[-4:] == 'The '
    else:
        capital = True          # no article: nothing to mark, nothing to fail
    if not capital:
        return False, 'written with a lower-case article'
    if sentence_start(body, m.start() - (4 if article.lower().endswith('the ') else 0)):
        return False, 'first use is sentence-initial, where capitalisation is not a mark'
    return True, ''


def audit_named_thing(text, name):
    """True if the first use carries the italic coinage mark. Pure."""
    body = prose_only(text)
    m = re.search(r'(?<![A-Za-z])' + _pattern(name) + r'(?![A-Za-z])', body)
    if not m:
        return None
    before = body[max(0, m.start() - 1):m.start()]
    after = body[m.end():m.end() + 1]
    return before == '*' and after == '*'


def main(argv):
    verbose = '-v' in argv
    issues = []
    for name, where in DESIGNATIONS.items():
        path = os.path.join(DIR, where)
        if not os.path.exists(path):
            issues.append('%s: declared but no such file' % where)
            continue
        bad, uses = audit_designation(read(path), name)
        if uses == 0:
            issues.append('%s: declared designation %r never appears' % (where, name))
        for wrong in bad:
            issues.append('%s: %r is a designation and is written %r' % (where, name, wrong))
        if verbose:
            print('  %-46s %-14s caps %d · bad casings %d'
                  % (where[:44], name, uses, len(bad)))

    for where, names in NAMED_THINGS.items():
        path = os.path.join(DIR, where)
        if not os.path.exists(path):
            issues.append('%s: declared but no such file' % where)
            continue
        text = read(path)
        for n in names:
            got = audit_named_thing(text, n)
            if got is None:
                issues.append('%s: %r is never used' % (where, n))
            elif not got:
                issues.append('%s: %r is not marked at its coinage' % (where, n))
            elif verbose:
                print('  %-46s %-22s coinage marked' % (where[:44], n))

    for where, pairs in SHORT_FORMS.items():
        path = os.path.join(DIR, where)
        if not os.path.exists(path):
            continue
        body = prose_only(read(path))
        for short, long_name in pairs.items():
            m_long = re.search(r'(?<![A-Za-z])' + _pattern(long_name) + r'(?![A-Za-z])', body)
            m_short = re.search(r'(?<![A-Za-z])' + _pattern(short) + r'(?![A-Za-z]| of )', body)
            if m_short and (not m_long or m_short.start() < m_long.start()):
                issues.append('%s: %r is used before %r is coined'
                              % (where, short, long_name))
            elif verbose and m_short:
                print('  %-46s %-22s short form after coinage' % (where[:44], short))
                m_used = re.search(r'(?<![A-Za-z])' + _pattern(short) + r'(?![A-Za-z]| of )', body)

    # a declared designation that appears in a file which did not declare it
    for path in sorted(glob.glob(os.path.join(DIR, '*.md'))):
        base = os.path.basename(path)
        if base in DESIGNATIONS.values():
            continue
        body = narrative(read(path))
        for name in DESIGNATIONS:
            if re.search(r'(?<![A-Za-z*])' + re.escape(name) + r'(?![A-Za-z*])', body):
                issues.append('%s: uses %r without declaring it' % (base, name))

    for where, names in BODIES.items():
        path = os.path.join(DIR, where)
        if not os.path.exists(path):
            continue
        text = read(path)
        for n in names:
            ok, why = audit_body(text, n)
            if ok is None:
                issues.append('%s: body %r is never used' % (where, n))
            elif not ok:
                issues.append('%s: body %r — %s' % (where, n, why))
            elif verbose:
                print('  %-46s %-24s body, mark visible' % (where[:44], n))

    # every file must tell its own reader what the marks mean
    for path in sorted(glob.glob(os.path.join(DIR, '*.md'))):
        base = os.path.basename(path)
        head = read(path)[:2500]
        if '**REGISTER:**' not in head:
            issues.append('%s: carries no REGISTER line, so its marks are unexplained' % base)
        elif verbose:
            print('  %-46s register line present' % base[:44])

    print('designations declared %d · named things declared %d across %d files'
          % (len(DESIGNATIONS), sum(len(v) for v in NAMED_THINGS.values()), len(NAMED_THINGS)))
    print('register defects: %d' % len(issues))
    for i in issues:
        print('  ' + i)
    if issues:
        print('RESULT: FAIL — %d register defects' % len(issues))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
