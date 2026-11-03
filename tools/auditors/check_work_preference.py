#!/usr/bin/env python3
"""check_work_preference.py — the four cells, and the Threat Score behind the barred pair.

Owner rules, 2026-11-03:

> *"INSTEAD OF N/A For Non-Subject Write It Either 0% ... and how you logic it is
> using the SE Threat Point because it's easier than checking both at the same
> time."*
>
> *"The Threat Point Thing ... I Used It From Our Conversion Guide you know the
> 2–10 things. Also You Dont Write 0% or -100% On Dossier It Look Bad Think It
> Like This Net-Neutral And Negative-Low."*

Five things are enforced here:

1. **The alphabet.** A cell is `Down`, `Up`, `Neutral`, `Net-Neutral` or
   `Negative-Low`. `N/A` on a barred register is retired: it said *not
   applicable*, which is not an answer to "what happens if somebody tries".
2. **The barred cells are words, not percentages.** `0%` and `-100%` were the
   batch-156 labels and they read badly on a dossier page. They are the *same two
   mechanics* under their written names: **Net-Neutral** (nothing is returned: the
   threshold does not come down, the gauge does not move, no benefit is paid) and
   **Negative-Low** (the attempt is charged in full: threshold to 0, gauge to
   100%). A page that still prints a percentage token fails on `percentage-token`.
3. **The barred pair is one reading.** The two cells must be equal, because both
   come from one number rather than from two separate judgements.
4. **One holding, filed twice, answers the same way.** A M.A.W. set's A-page
   (`SE-###-A`) and the Sorrow Entity dossier it belongs to (`SE-O-IIγ-007`) are
   the same entity in two collections, and each prints its own work table. Bar
   status must agree — a page may not bar a pair its dossier files as valid work,
   and may not stay silent where the dossier bars it — and the word must be the
   one the page's own designation wants. A compound (`Net-Neutral / escalation`)
   is refused: a reader cannot act on a verdict that is conditional. Batch 160
   found 125 A-pages still printing `N/A` where their dossiers had words; batch
   161 found nine that still disagreed with their dossiers in other ways.
5. **The Threat Score decides, and it is the guide's 2–10.** `PM_ABNORMALITY_TO_PS_
   SORROW_ENTITY_CONVERSION_GUIDE.md` §III: *Threat Score is Coherence rank +
   Potency rank (I/α = 1 … V/ω = 5)*, so it runs **2–10** — 2–3 ZAYIN, 4–5 TETH,
   6 HE, 7–8 WAW, 9–10 ALEPH. Below 6 the attempt simply fails (**Net-Neutral**);
   6 and above the holding is heavy enough to collect in full (**Negative-Low**).
   The band boundary *is* the rule: HE is the first tier that is a major problem.

    python3 tools/auditors/check_work_preference.py            # ratchet check
    python3 tools/auditors/check_work_preference.py -v         # per-dossier listing
    python3 tools/auditors/check_work_preference.py --variety  # the live distribution
"""
import collections
import glob
import io
import re
import sys

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')

# The four pages of every M.A.W. set. Only the A-page carries a work table.
SIDE_CODEX = 'SOMNARAK-WORLD/MAW_Codex_Sets/**/*-A__SIDE_CODEX_*.md'

PIPESPLIT = re.compile(r'(?<!\\)\|')

# The SECC code, wherever a page prints it: dossiers file it as `**Designation**`,
# Side Codex pages as `**SECC Designation:**`.
DESIGNATION = re.compile(r'(?:\*\*Designation\*\*|SECC Designation):?\*{0,2}\s*\|?\s*`?'
                         r'([CNO])-(I{1,3}|IV|V)([\u03b1\u03b2\u03b3\u03b4\u03c9])-(\d+[a-z]?)')

TYPE = re.compile(r'\*\*Entity Type\*\*\s*\|\s*([^|]+)\|')
COHERENCE = re.compile(r'\|\s*\*{0,2}Coherence\*{0,2}\s*\|\s*([^|\n]*)')
POTENCY = re.compile(r'\|\s*\*{0,2}Potency\*{0,2}\s*\|\s*([^|\n]*)')
ROW = re.compile(r'^\|\s*\*\*(Flerehan|Pugnahan|Viderehan|Ferrehan)\*\*[^|]*\|[^|]*\|([^|]*)\|', re.M)
_CELL = r'(?:-100%|0%|Down|Up|Neutral|Net-Neutral|Negative-Low)'
VEC = re.compile(r'`?(' + _CELL + r')\s*:\s*(' + _CELL + r')\s*:\s*(' + _CELL +
                 r')\s*:\s*(' + _CELL + r')`?')

ORDER = ('Flerehan', 'Pugnahan', 'Viderehan', 'Ferrehan')
NET_NEUTRAL = 'Net-Neutral'
NEGATIVE_LOW = 'Negative-Low'
GOOD = {'Down', 'Up', 'Neutral', NET_NEUTRAL, NEGATIVE_LOW}
BAR = {NET_NEUTRAL, NEGATIVE_LOW}
# A verdict with a dash in brackets after it is a label with no value. Thirty
# A-pages printed one until batch 166: `Negative-Low (—)`.
EMPTY_PAREN = re.compile(r'\(\s*[\u2014\u2013-]\s*\)')

# Legacy tokens. They parse — a batch may not be half-migrated into a false fail —
# but a page that still prints one is reported, so the words have to land everywhere.
LEGACY = {'0%': NET_NEUTRAL, '-100%': NEGATIVE_LOW, '\u2212100%': NEGATIVE_LOW}

# The guide's arithmetic: Coherence rank + Potency rank, I/α = 1 … V/ω = 5.
ROMAN = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
GREEK = {'\u03b1': 1, '\u03b2': 2, '\u03b3': 3, '\u03b4': 4, '\u03c9': 5}
HE = 6                 # ZAYIN 2–3 · TETH 4–5 · **HE 6** · WAW 7–8 · ALEPH 9–10

# A cell that still says N/A, a dash, or a sentence. Retired for barred registers.
# `\b` after a dash never fires at end of string, so the lookahead is explicit,
# and it keeps `-100%` out of the retired class.
DEAD = re.compile(r'^\s*(?:N/A|—|–|-)(?![A-Za-z0-9])', re.I)

# Still printing a percentage where a word belongs.
PERCENT = re.compile(r'(?<![\d.])-[\u2212]?100\s*%|(?<![\d.])0\s*%')

# The ratchet counts dossiers on the two most crowded vectors; it may only fall.
#
# 172 -> 176 in batch 159, and the rise is recorded rather than dressed up. The
# Threat Score replaced the gauge reading as the source of the barred pair, and
# four of the five dossiers that re-read under it landed on the second crowded
# vector. A rule change moves the measure; nothing was rewritten to move it.
TIERED = [0]
RATCHET = 176
RATCHET_SET = '2026-11-03'


# The L Corp ladder has five grades. The archive writes the middle three today; the
# two extremes are legal so a dossier may claim one without tripping the auditor.
TIERS = ('V.H', 'High', 'Common', 'Low', 'V.L')


def split_tier(cell):
    """`Down · High` -> ('Down', 'High'). A bare sign has no tier."""
    parts = [p.strip().strip('*').strip() for p in cell.replace('**', '').split('·')]
    return parts[0], (parts[1] if len(parts) > 1 else None)


def normalize(cell):
    """Map a written cell to the alphabet, or None when it is prose.

    The two named cells are tested first, then the legacy percentages, then the
    signs. The percentage forms must be tested BEFORE the dash form: `-100%`
    starts with a dash, and a dead-cell pattern run first reads it as a retired `—`.
    """
    c = split_tier(cell)[0]
    low = c.lower().replace('*', '').strip()
    if low in ('net-neutral', 'net neutral', 'netneutral', 'net zero', 'net-zero'):
        return NET_NEUTRAL
    if low in ('negative-low', 'negative low', 'negativelow'):
        return NEGATIVE_LOW
    if re.match(r'^[-\u2212]100\s*%', c):
        return NEGATIVE_LOW
    if re.match(r'^0\s*%', c):
        return NET_NEUTRAL
    if low in ('down', 'up', 'neutral'):        # the canonical word itself
        return low.capitalize()
    if low.startswith('stable') or low.startswith('no movement'):
        return 'Neutral'
    if low.startswith('decrease') or low.startswith('slight decrease'):
        return 'Down'
    if low.startswith('increase'):
        return 'Up'
    if DEAD.match(c):
        return 'RETIRED'
    return None


def side_codex_rows(text):
    """(work, word, body) for every work row of a Side Codex page.

    The A-page tables come in five shapes — `| Work | Source response |`, a
    three-cell form with the gauge third, a four-cell form with the field rule
    fourth, and both of those with prose in the state cell. The word is
    therefore searched for anywhere after the work name rather than read from a
    fixed column: the row is four cells wide at most and carries one standing.
    """
    out = []
    for line in text.split('\n'):
        m = re.match(r'^\|\s*\*{0,2}(Flerehan|Pugnahan|Viderehan|Ferrehan)', line)
        if not m:
            continue
        body = ' '.join(PIPESPLIT.split(line)[2:-1]) if line.startswith('|') else ''
        word = None
        for candidate in (NET_NEUTRAL, NEGATIVE_LOW):
            if candidate in body:
                word = candidate
                break
        if word is None:
            if 'N/A' in body:
                word = 'N/A'
            elif any(LEGACY[k] in body for k in LEGACY):
                word = 'LEGACY'
        out.append((m.group(1), word, body))
    return out


def cells_of(text):
    """The four raw cells, in file order, or None when the table is not four rows."""
    rows = dict((w, g) for w, g in ROW.findall(text))
    if len(rows) != 4:
        return None
    return [rows[w] for w in ORDER]


def vector_of(text):
    """The four-cell vector of a dossier, from its table or its Work preference row."""
    m = VEC.search(text)
    if m and 'Work preference' in text:
        return [normalize(c) for c in m.groups()]
    cells = cells_of(text)
    if cells is None:
        return None
    return [normalize(c) for c in cells]


def tier_problems(cells):
    """The L Corp ladder: High / Common / Low, one High at most, none on a barred cell."""
    out = []
    tiers = [split_tier(c)[1] for c in cells]
    seen = [x for x in tiers if x]
    for i, tier in enumerate(tiers):
        if tier and tier not in TIERS:
            out.append('cell %d tier %r is off the ladder' % (i + 1, tier))
        if tier and tiers is not None and normalize(cells[i]) in BAR:
            out.append('cell %d is barred and carries no preference' % (i + 1))
    if seen.count('High') > 1:
        out.append('%d High cells — a holding answers to one register best'
                   % seen.count('High'))
    if seen.count('V.H') > 1:
        out.append('%d V.H cells — a holding answers to one register best'
                   % seen.count('V.H'))
    if seen and len(seen) != 4:
        out.append('only %d of four cells carry a tier' % len(seen))
    return out


def threat_score(text):
    """Coherence rank + Potency rank, the guide's 2–10. None when either is unfiled.

    The fields are written `| **Coherence** | Entity (IV) |` and `| **Potency** |
    Major (γ) |`, and the row labels have a `modifier` sibling that must not be
    read as the field itself.
    """
    coh, pot = COHERENCE.search(text), POTENCY.search(text)
    if not coh or not pot:
        return None
    c = re.search(r'\b(IV|V|III|II|I)\b', coh.group(1))
    g = re.search(r'([\u03b1\u03b2\u03b3\u03b4\u03c9])', pot.group(1))
    if not c or not g:
        return None
    return ROMAN[c.group(1)] + GREEK[g.group(1)]


def wanted_barred(score):
    """Below HE the attempt fails; HE and above it is collected in full."""
    return NEGATIVE_LOW if score >= HE else NET_NEUTRAL


def is_relic(text):
    m = TYPE.search(text)
    return bool(m) and 'Subject' not in m.group(1)


def pair_equality(vec):
    """If both cells are barred words, they are the same word.

    This holds for every dossier, not only a relic. A Subject that bars the pair
    — thirteen do, on their own record — reads the two cells off one Threat
    Score exactly as a relic does; two different words would be two readings.
    """
    if vec[0] in BAR and vec[1] in BAR and vec[0] != vec[1]:
        return ['barred pair disagrees (%s vs %s) — it is one threat reading'
                % (vec[0], vec[1])]
    return []


def barred_pair_problems(vec):
    """A relic's two cells must be words rather than percentages, and the same."""
    out = []
    for i in (0, 1):
        if vec[i] not in BAR and vec[i] is not None:
            out.append('cell %d is %r, not Net-Neutral or Negative-Low' % (i + 1, vec[i]))
    return out + pair_equality(vec)


def measure():
    files, problems, distribution = [], [], collections.Counter()
    tiered = [0]
    for pattern in DOSSIERS:
        for path in sorted(glob.glob(pattern, recursive=True)):
            with io.open(path, encoding='utf-8') as fh:
                text = fh.read()
            files.append(path)
            vec = vector_of(text)
            if vec is None:
                continue
            bad = []
            if 'RETIRED' in vec:
                bad.append('barred cell still written N/A or a dash')
            for word in vec:
                if word is not None and word != 'RETIRED' and word not in GOOD:
                    bad.append('cell %r is off the alphabet' % word)
            if is_relic(text):
                bad.extend(barred_pair_problems(vec))
            else:
                bad.extend(pair_equality(vec))
            cells = cells_of(text)
            if cells is not None:
                bad.extend(tier_problems(cells))
                if any(split_tier(c)[1] for c in cells):
                    tiered[0] += 1
            score = threat_score(text)
            if score is not None and vec[0] in BAR and vec[1] in BAR:
                want = wanted_barred(score)
                if vec[0] != want:
                    bad.append('threat score %d (%s) wants %s, cells say %s'
                               % (score, 'HE or above' if score >= HE
                                  else 'under HE', want, vec[0]))
            # Scoped to the cells, not the file: "the store is the same size at
            # 0 % as at 45 %" is a gauge reading in prose, not a work-response
            # cell, and a whole-file scan reported it as one.
            raw = cells_of(text) or []
            vrow = [l for l in text.split('\n') if 'Work preference' in l and VEC.search(l)]
            if any(PERCENT.search(x) for x in raw) or any(
                    PERCENT.search(VEC.search(l).group(0)) for l in vrow):
                bad.append('percentage-token: still prints a percentage where the '
                           'alphabet has a word')
            if bad:
                problems.append((path, bad))
            if all(v is not None and v != 'RETIRED' for v in vec):
                distribution[tuple(vec)] += 1
    TIERED[0] = tiered[0]
    return files, problems, distribution


def designation_score(text):
    """Threat Score from the SECC code a page prints, or None.

    The dossier's two fields (`Coherence`, `Potency`) and its designation say the
    same thing; the Side Codex page files only the designation, so the code is the
    one reading both collections share.
    """
    m = DESIGNATION.search(text)
    if not m:
        return None
    return ROMAN[m.group(2)] + GREEK[m.group(3)]


# `Negative-Low / contextual` is two standings in one cell; the alphabet has no
# compound, because a reader cannot act on a verdict that is conditional.
COMPOUND = re.compile(r'(Net-Neutral|Negative-Low)\s*[/+;]')


def dossier_word_map():
    """SECC key -> the words the dossier prints in its Flerehan/Pugnahan cells.

    An empty string means the dossier files both works as valid work: the pair is
    not barred, so its A-page must not carry a barred word. A missing key means
    no dossier files that code at all, which is a filing question and not a rule.
    """
    out = {}
    for pattern in DOSSIERS:
        for path in sorted(glob.glob(pattern, recursive=True)):
            with io.open(path, encoding='utf-8') as fh:
                text = fh.read()
            m = DESIGNATION.search(text)
            if not m:
                continue
            key = '%s-%s%s-%s' % (m.group(1), m.group(2), m.group(3), m.group(4))
            vec = vector_of(text)
            words = set(w for w in (vec or ()) if w in BAR)
            out[key] = '/'.join(sorted(words))
    return out


def side_codex_problems(text, twin):
    """The reasons one Side Codex page stands against its dossier, if any.

    `twin` is the dossier's barred word, the empty string when the dossier files
    both works as valid, or None when no dossier files that code at all. A page
    with no work row is not measured: there is nothing on it to disagree with.
    """
    rows = side_codex_rows(text)
    if not rows:
        return []
    bad = []
    score = designation_score(text)
    want = wanted_barred(score) if score is not None else None
    mine = set()
    for work, word, body in rows:
        if work not in ('Flerehan', 'Pugnahan'):
            continue
        if COMPOUND.search(body):
            bad.append('%s prints a compound verdict' % work)
        if EMPTY_PAREN.search(body):
            bad.append('%s prints an empty parenthetical' % work)
        if word == 'N/A':
            bad.append('%s still written N/A — the alphabet has words' % work)
        elif word == 'LEGACY':
            bad.append('percentage-token: %s prints a percentage' % work)
        elif word is not None:
            mine.add(word)
    said = '/'.join(sorted(mine))
    if len(mine) > 1:
        bad.append('the barred pair disagrees (%s) — it is one threat reading'
                   % said)
    if twin and not mine:
        bad.append('its dossier bars the pair as %s; this page records no '
                   'standing' % twin)
    elif twin and mine != set(twin.split('/')):
        bad.append('this page says %s, its dossier says %s' % (said, twin))
    elif twin == '' and mine:
        bad.append('this page bars the pair as %s; its dossier files both works '
                   'as valid' % said)
    if want and mine and mine != {want}:
        bad.append('threat score %d wants %s, page says %s'
                   % (score, want, said))
    return bad


def measure_side_codex(word_map):
    """One holding, one standing: the A-page and its dossier agree, cell for cell.

    An A-page and its dossier are the same holding filed twice — the dossier
    records what was measured, the codex page records what a Warden is told. If
    one bars the pair and the other files both works as valid, the holding has
    two standings and a reader has no way to choose between them.
    """
    files, problems, unpaired = [], [], []
    for path in sorted(glob.glob(SIDE_CODEX, recursive=True)):
        with io.open(path, encoding='utf-8') as fh:
            text = fh.read()
        if not side_codex_rows(text):
            continue
        files.append(path)
        m = DESIGNATION.search(text)
        key = ('%s-%s%s-%s' % (m.group(1), m.group(2), m.group(3), m.group(4))
               if m else None)
        twin = word_map.get(key) if key else None
        if key not in (word_map or {}):
            unpaired.append(path)
        bad = side_codex_problems(text, twin)
        if bad:
            problems.append((path, bad))
    return files, problems, unpaired


def main(argv):
    files, problems, dist = measure()
    if '--variety' in argv:
        for vec, n in dist.most_common():
            print('%5d  %s' % (n, ' : '.join(vec)))
        print('%d graded dossiers, %d distinct vectors' % (sum(dist.values()), len(dist)))
        return 0
    for path, bad in problems:
        if '-v' in argv:
            print('%s  %s' % (path, '; '.join(bad)))
        else:
            print('%s  %s' % (path, '; '.join(bad)[:110]))
    sc_files, sc_problems, unpaired = measure_side_codex(dossier_word_map())
    for path, bad in sc_problems:
        if '-v' in argv:
            print('%s  %s' % (path, '; '.join(bad)))
        else:
            print('%s  %s' % (path, '; '.join(bad)[:110]))
    on_two = sum(n for _, n in dist.most_common(2))
    pct = sum(1 for _, bad in problems for b in bad if b.startswith('percentage-token'))
    print('off alphabet: %d  printing a percentage: %d  on the two crowded vectors: %d  '
          'ratchet %d  set %s'
          % (len(problems), pct, on_two, RATCHET, RATCHET_SET))
    print('carrying a preference tier: %d of %d graded' % (TIERED[0], sum(dist.values())))
    print('side codex: %d pages carry a work table; %d stand against their dossier; '
          '%d cite a code no dossier files  ratchet 0'
          % (len(sc_files), len(sc_problems), len(unpaired)))
    if problems or sc_problems or on_two > RATCHET:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
