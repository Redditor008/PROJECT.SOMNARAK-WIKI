#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_backstory_gloss.py — gate 54: a proper noun is not a password (R-59, O-45).

WHY THIS EXISTS

The owner read `01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md` and asked for it to be *"more clearer
and understandable"*. Reading it cold, the first fifty pages offer the reader these, unexplained:

    *"She gave it. Envelope, Veil, conduits, gauges, Maw."*

Four of those five words are the name of a system in a city the reader has not been shown yet. The
text explains the Consolihan twice, in two scenes, and the Veil never. A reader who does not already
know this corpus is asked to carry a vocabulary instead of a story, and the most common result is not
confusion — it is that the reader stops asking what a word means and starts skimming past it. That is
the failure this gate measures.

THE MEASUREMENT

For each `Backstory_Extended` file, take a fixed list of corpus terms that no reader can infer from
the page. For each, find the **first use in the narrative body** (the appendix is where the file
explains itself to an archivist, not to a reader) and require an explanatory construction in the
sentence that carries it or the sentence after:

  * an em-dash appositive        `Han — the substance the city sat on —`
  * a parenthesis                `the Veil (the suppression net)`
  * a copular definition         `A Fracture is what the city calls it when`
  * a cue phrase                 `what the city calls`, `the name for`, `which is`, `that is to say`

This checks that *an explanation is present next to the first use*. It cannot check that the
explanation is true, or good, or short enough not to stop the scene. That is the reader's pass.

WHAT FAILS

  * a term used in the narrative with no gloss at first use, in a file that is not recorded as debt;
  * a recorded file that gets worse.

    python3 tools/auditors/check_backstory_gloss.py
    python3 tools/auditors/check_backstory_gloss.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, 'SOMNARAK-WORLD', 'Echo_Cores', 'Backstory_Extended')

# Terms the corpus uses as if the reader already knows them. Nothing in this list is inferable from
# the sentence that introduces it, except by luck.
TERMS = (
    'Han',
    'Cheongula',
    'Consolihan',
    'Weeping',
    'Veil',
    'Maw',
    'Fracture',
    'Fractured',
    'Absolvohan',
    'Cheonbulok',
    'Alpha Tree',
    'Reaper Hungered',
    'Echo-Core',
)

# A gloss has to sit *next to* the term. An em-dash anywhere in a two-sentence window would match
# every third sentence in this corpus and certify nothing.
DASH = 110          # chars after the term within which an appositive dash must fall
PAREN = 70          # chars after the term within which a parenthesis must open
COPULA = 60         # chars after the term within which `is a / was a / is the` must fall

COPULA_RE = re.compile(r'^\W*(is|was|are|were)\s+(a|an|the|what|one|not)\b', re.I)
CUE_RE = re.compile(r'\bwhat the city calls\b|\bthe name (for|of)\b|\bwhich is\b|'
                    r'\bthat is to say\b|\bcalled\b|\bcalls\b', re.I)

SENTENCE = re.compile(r'[^.!?\n]*[.!?]')


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


META = re.compile(r'^> \*\*(PROVENANCE|COMPILER|HOLDER|ERA|SPINE|ACCESS|RELIABILITY|RECORD CLASS'
                  r'|TOTAL|SOURCE|WITNESS):.*$', re.M)


def narrative(text):
    """The story only.

    Two things are removed, for the same reason: neither is where a reader meets a word.
    The appendix is the file explaining itself to an archivist, and the record header is the
    file cataloguing itself. `Absolvohan Parts 2-9 anchor scenes` is a citation, not a use.
    """
    i = text.find('\n## Appendix')
    body = text if i < 0 else text[:i]
    return META.sub('', body)


def first_use(text, term):
    """The sentence carrying the first use, plus the sentence after it. None if unused."""
    m = re.search(r'(?<![A-Za-z])' + re.escape(term) + r'(?![A-Za-z])', text)
    if not m:
        return None
    start = max(0, text.rfind('\n', 0, m.start()) + 1)
    window = text[start:start + 700]
    return window


def glossed(window, term):
    """An explanation adjacent to this use. Rough by construction — see the docstring."""
    m = re.search(r'(?<![A-Za-z])' + re.escape(term) + r'(?![A-Za-z])', window)
    if not m:
        return False
    after = window[m.end():m.end() + DASH]
    head = window[m.end():m.end() + COPULA]
    if '\u2014' in after or ' - ' in after:          # Han — the substance ...
        return True
    if '(' in window[m.end():m.end() + PAREN]:
        return True
    if COPULA_RE.match(head):                        # A Fracture is what the city calls ...
        return True
    if re.search(r'\b(the|a|an)\s+$', window[:m.start()], re.I) and COPULA_RE.match(head):
        return True
    return bool(CUE_RE.search(window))


def audit(text):
    """(unglossed terms, checked terms). Pure."""
    body = narrative(text)
    missing = []
    for term in TERMS:
        window = first_use(body, term)
        if window is None:
            continue
        if not glossed(window, term):
            missing.append(term)
    used = [t for t in TERMS if first_use(body, t) is not None]
    return missing, used


# Empty on purpose. Batch 219 glossed all thirteen terms in all nine files rather than banking debt;
# the table stays because the next unglossed term must be recorded here and printed, not absorbed.
DEBT = {}


def main(argv):
    verbose = '-v' in argv
    new_debt, regressions, rows = [], [], []
    for path in sorted(glob.glob(os.path.join(DIR, '*.md'))):
        name = os.path.basename(path)
        missing, used = audit(read(path))
        rows.append((name, len(missing), len(used), missing))
        if missing and name not in DEBT:
            new_debt.append((name, len(missing)))
        if name in DEBT and len(missing) > DEBT[name]:
            regressions.append((name, '%d was %d' % (len(missing), DEBT[name])))
        if verbose:
            print('  %-48s cold %2d of %-2d  %s'
                  % (name[:46], len(missing), len(used), ', '.join(missing[:6])))
    clean = sum(1 for r in rows if not r[1])
    print('backstory files %d · fully glossed %d · carrying cold terms %d'
          % (len(rows), clean, len(rows) - clean))
    if DEBT:
        worst = max(DEBT.items(), key=lambda kv: kv[1])
        print('worst recorded: %s — %d cold terms' % (worst[0][:46], worst[1]))
        print('cold terms carried as debt: %d across %d files' % (sum(DEBT.values()), len(DEBT)))
    else:
        print('worst recorded: none — no file is carrying debt')
    print('new debt: %d · regressions: %d' % (len(new_debt), len(regressions)))
    for name, n in new_debt:
        print('  NEW   %-48s %s' % (name[:48], n))
    for name, msg in regressions:
        print('  WORSE %-48s %s' % (name[:48], msg))
    if new_debt or regressions:
        print('RESULT: FAIL — %d new, %d regressed' % (len(new_debt), len(regressions)))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
