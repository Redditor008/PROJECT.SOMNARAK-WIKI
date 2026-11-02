#!/usr/bin/env python3
"""finishedness.py — per-file completeness, measured against filed obligations.

WHAT THIS IS. A percentage computed from obligations this archive already
carries: the sections its templates require, the fields its own files carry in
90%+ of their class, the debts that are on the record (Maximum Amount, the
filename/H1 mismatch), and the defect classes the linters already police. It is
the share of those obligations a file meets.

WHAT THIS IS NOT. It is not a judgement of writing quality. A dossier at 100%
meets every structural obligation we can check; a dossier at 100% is not a good
dossier. Nothing here reads for meaning.

Every obligation is listed with its key, so a file's score can be argued with:
the missing keys are printed beside it.

    python3 tools/finishedness.py                  # summary
    python3 tools/finishedness.py --csv PATH       # per-file rows
    python3 tools/finishedness.py --worst N        # lowest-scoring files
"""
import io
import os
import re
import sys
import glob
import csv
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# ---------------------------------------------------------------- primitives

SPLIT_HYPHEN = re.compile(r'\b([A-Za-z]{2,})- ([A-Za-z]{2,})\b')
# suspended hyphens are correct English: "pre- and post-field", "seven- or ten-unit"
SUSPENDED_NEXT = {'and', 'or', 'nor', 'to'}
AI_TIC = re.compile(r'\b(delve|delving|In conclusion)\b', re.I)
# "a testament to" is the cliché; a monument raised *as* a testament is an object
# testifying, which is the archive's own register. 만들어진 기록 — a record, in stone.
TESTAMENT = re.compile(r'\btestament to\b', re.I)
STONE = re.compile(r'\b(monument|stone|marker|plaque|stele|memorial|grave|tablet|wall|inscription)\b', re.I)
# "tapestry" is banned as an abstraction metaphor, not as an object. The archive
# has a Loom, a Weaver, a Pall that is literally a woven textile, and an ability
# called The Tapestry of Stolen Pasts. Exclude the noun when it is capitalised
# (proper name) or when the same line carries weaving vocabulary.
WEAVE = re.compile(r'\b(loom|woven|weave|weaver|thread|cloth|textile|weft|warp|stitch|dye|dyeing)', re.I)
# A document that has already established the tapestry as a physical textile is
# not using a metaphor when it says so again: the Pall is a woven textile of
# crystallised tears, and the Weaver's tapestry is the thing it weaves.
TAPESTRY_OBJECT = re.compile(r'woven tapestry|tapestry of crystalli[sz]ed tears|hanging tapestry|The Tapestry of Stolen Pasts', re.I)


def ai_tic(text):
    if AI_TIC.search(text):
        return True
    for m in TESTAMENT.finditer(text):
        if STONE.search(text[max(0, m.start() - 120):m.start()]):
            continue
        return True
    if TAPESTRY_OBJECT.search(text):
        return False
    for m in re.finditer(r'\btapestry\b', text, re.I):
        word = m.group(0)
        # look at the sentence around it, not the physical line: a woven pall
        # names its cloth a clause earlier than the word "tapestry"
        lo = max(0, m.start() - 220)
        hi = min(len(text), m.end() + 220)
        window = text[lo:hi]
        if word[0].isupper() or WEAVE.search(window):
            continue
        return True
    return False
SCAFFOLD = re.compile(r'\{\{[^}]{1,80}\}\}')
LADDER = {'0.3': 'Resistant', '0.4': 'Resistant', '0.5': 'Warded', '0.6': 'Warded',
          '0.7': 'Warded', '0.8': 'Warded', '0.9': 'Normal', '1.0': 'Normal',
          '1.1': 'Weak', '1.2': 'Weak', '1.3': 'Weak', '1.4': 'Weak',
          '1.5': 'Weak', '1.6': 'Weak', '1.8': 'Weak'}
DOSSIER_HEADINGS = ['SECC Classification', 'Operational Parameters', 'Appearance',
                    'Origin', 'Behavior', 'M.A.W. Equipment', '관찰 기록',
                    '이야기 보고', '최종 관찰']
SECC_FIELDS = ['Designation', 'Entity Type', 'Coherence', 'Potency', 'Element',
               'Manifestation', 'Physical Form', 'Location']
OP_FIELDS = ['Risk tier', 'Sorrow Gauge [HP]', 'Vessel-Destructible', 'Valid Work Types']


def words(t):
    return len(re.findall(r'[A-Za-z가-힣]{2,}', t))


def section(t, name):
    """Body of the first H2/H3 section of that name, INCLUDING its subsections.

    Records carry Appearance at H3 under ITEM IDENTITY as often as at H2, so
    matching only H2 undercounted the section by roughly two thirds. Stopping at
    the next heading of level 1-3 had the same fault one level down: a section
    that organises itself as `## 관찰 기록` + `### Surge Catalogue` +
    `### Observation Progression` reads as one section to a reader, but scored
    only its two-line intro. The section ends at the next heading of the SAME OR
    HIGHER level, so its own subsections stay inside it.
    """
    m = re.search(r'^(#{2,3})\s+' + re.escape(name) + r'\b', t, re.M)
    if not m:
        return ''
    level = len(m.group(1))
    stop = re.compile(r'^#{1,%d}\s' % level, re.M)
    n = stop.search(t, m.end())
    return t[m.end():n.start()] if n else t[m.end():]


def field(t, label):
    m = re.search(r'^\|\s*\*{0,2}' + re.escape(label) + r'\*{0,2}\s*\|\s*([^|\n]*)\|', t, re.M)
    return m.group(1).strip() if m else None


def filled(v):
    return v is not None and v.strip() not in ('', '—', '-', 'N/A')


def has_split_hyphen(t):
    for m in SPLIT_HYPHEN.finditer(t):
        if m.group(2).lower() not in SUSPENDED_NEXT:
            return True
    return False


def corrosion_openers(t):
    """True when the file carries corrosion prose that is NOT the stock sentence."""
    if 'Corrosion' not in t:
        return False
    for m in re.finditer(r'Corrosion (?:runs|begins|starts|opens)', t):
        tail = t[m.start():m.start() + 160]
        if 'first-person description of the event' not in tail:
            return True
    return False


def resistance_off_ladder(t):
    for blk in re.findall(r'\*\*Resistances:\*\*(.{0,300})', t, re.S):
        for m in re.finditer(r'-\s*(Lament|Grudge|Void|Weight|Hope)\s*:\s*([0-9.]+)\s*\(([^)]+)\)', blk):
            if LADDER.get(f'{float(m.group(2)):.1f}') != m.group(3):
                return True
    return False


def h1(t):
    m = re.search(r'^#\s+(.+)$', t, re.M)
    return m.group(1).strip() if m else ''


def _norm(ws):
    out = set()
    for w in ws:
        w = w.lower().replace('\u2019', '').replace("'", '')
        if w.endswith('s') and len(w) > 3:
            w = w[:-1]
        if w not in ('the', 'and', 'of', 'a'):
            out.add(w)
    return out


def stem_tokens(path):
    base = os.path.basename(path)[:-3]
    base = re.sub(r'^SE-\d+-[A-Z]__MAW-[WSG]_', '', base)
    base = re.sub(r'^SE-\d+-[A-Z]__SIDE_CODEX_', '', base)
    return _norm(re.findall(r'[A-Za-z]{3,}', base))


def h1_matches(path, t):
    toks = stem_tokens(path)
    if not toks:
        return True
    return toks.issubset(_norm(re.findall(r'[A-Za-z]{2,}', h1(t))))


# ---------------------------------------------------------------- rubric


def has_stock_ceiling(t):
    """The archive's own standard (MAW codex §I.1): the label must be the FIRST
    cell of its own row. The same strings appear as column headers in the combat
    stat tables, and the codex counts those as filing nothing."""
    for line in t.split('\n'):
        s = line.strip()
        if not s.startswith('|'):
            continue
        cells = s.split('|')
        if len(cells) > 2:
            first = cells[1].strip().strip('*').strip()
            if re.match(r'(?:Maximum|Max)\s*(?:Amount|/\s*(?:Echo\s*)?[Cc]ost)', first, re.I):
                return True
    return bool(re.search(r'\*\*(?:Maximum|Max)\s*(?:Amount|/\s*(?:Echo\s*)?[Cc]ost):\*\*\s*\d', t, re.I)) or \
        bool(re.search(r'\*\*Maximum\s*/\s*(?:Echo\s*)?[Cc]ost:?\*{0,2}\s*[1-5]\s*/', t))


def score_dossier(path, t):
    req = {}
    req['nine_headings'] = all(re.search(r'^#+\s*' + re.escape(h), t, re.M) for h in DOSSIER_HEADINGS)
    req['secc_fields'] = all(filled(field(t, f)) for f in SECC_FIELDS)
    req['operational_fields'] = all(filled(field(t, f)) for f in OP_FIELDS)
    req['story_log'] = len(re.findall(r'^\*\*Entry\s*\d', t, re.M)) >= 1
    req['observation_log'] = words(section(t, '관찰 기록')) >= 40
    req['final_observation'] = words(section(t, '최종 관찰')) >= 40
    req['appearance'] = words(section(t, 'Appearance')) >= 40
    req['maw_named'] = bool(re.search(r'^#{2,4}\s*M\.A\.W\.\s*(Weapon|Suit|Stigma)', t, re.M)) or \
        bool(re.search(r'no M\.A\.W\.|no extraction|extraction (?:is )?impossible', t, re.I))
    req['corrosion_stock'] = not corrosion_openers(t)
    req['ladder'] = not resistance_off_ladder(t)
    req['grade_token'] = not re.search(r'Risk tier\*{0,2}\s*\|\s*[A-Za-z]+\s*\([IVX]+[αβγδω]\)', t)
    req['substance'] = words(t) >= 3000
    return req


def score_maw(path, t):
    """Obligations grounded in what the 852 records already carry.

    Baseline fields (Document ID, Linked Entity, Item Registry Code, Codex Set
    Completion, an H1) sit in 100% of the class, so they anchor "this is a
    record" without discriminating. The rest discriminate, and each one is a
    gap the archive itself names: the Maximum Amount debt, the filename/H1
    mismatch, the corrosion-form debt.
    """
    req = {}
    req['record_header'] = all(re.search(p_, t, re.M) for p_ in
                               (r'\*\*Document ID:\*\*', r'\*\*Linked Entity:\*\*',
                                r'\*\*Item Registry Code:\*\*'))
    # Reader test, not a word count: does the record tell a reader what the piece
    # looks like? 12 words is the floor for "describes the object"; the archive's
    # own transcribed lines run 13–19 and are terse by design.
    app = section(t, 'Appearance')
    req['appearance'] = (words(app) >= 12
                         or bool(re.search(r'\*\*Appearance:\*\*', t))
                         or bool(re.search(r'^\|\s*Appearance\s*\|\s*\S', t, re.M)))
    # Statistics are type-specific: a weapon files damage/speed/range, a suit files
    # a resistance table, a stigma files slot/chance/bonus. Asking every record for
    # damage was penalising every suit and stigma in the archive.
    if '__MAW-S_' in path:
        # three notations are in use: a four-column resistance table, the
        # parenthesised band form, and the compact "L/G/V/W: 1.0/0.4/1.8/1.2"
        req['statistics'] = (bool(re.search(r'\b[0-3]\.\d\b', t)) and
                             len(set(re.findall(r'\b(Lament|Grudge|Void|Weight)\b', t))) >= 3) \
            or bool(re.search(r'L/G/V/W\*{0,2}\s*:?\*{0,2}\s*[\d.]+\s*/\s*[\d.]+', t))
    elif '__MAW-G_' in path:
        # a stigma files a slot, a bestowal rate and a stat bonus; the words vary,
        # so accept the shape: a percentage plus a signed stat bonus
        req['statistics'] = (bool(re.search(r'\b(Slot|Chance|Bonus|Acquisition)\b', t, re.I))
                             or (bool(re.search(r'\d+\s*%', t))
                                 and bool(re.search(r'[+-]\s*\d', t))))
    else:
        req['statistics'] = bool(re.search(r'\b(Damage|Speed|Range)\b', t)) or \
            bool(re.search(r'L/G/V/W\s*[\d.]+/|\bmax\s*\d|\b\d+\s+Echoes\b', t))
    if '__MAW-G_' in path:
        # the arrival rate is a percentage however it is worded: "Acquisition
        # Probability 4%", "bestowal probability is 5%", "occurs in roughly 5%"
        req['cost_line'] = bool(re.search(r'\d+\s*%', t))
    else:
        req['cost_line'] = bool(re.search(r'Echo Cost|Sorrow Echoes|\b\d+\s+Echoes\b', t))
    req['max_amount'] = has_stock_ceiling(t)
    req['set_link'] = bool(re.search(r'SET RELATIONSHIP|SET RESONANCE|[Ss]ource-?[Tt]race|Linked Entity', t))
    req['h1_match'] = h1_matches(path, t)
    req['substance'] = words(t) >= 200
    return req


def record_shaped(t):
    """A record is judged as a record however its path is named.

    Side Codices and the UNK_ registry pieces carry the same front matter and
    field tables as an SE-xxx record, but their paths do not match the
    `SE-\\d+-[BCD]` shape, so they were being held to the prose-page floor.
    Framing, not word count, decides which floor applies.
    """
    return bool(re.search(r'\*\*Document ID:\*\*', t)) and bool(
        re.search(r'\*\*(?:Item Registry Code|Related Entity(?: ID)?|Linked Entity):\*\*', t))


def registry_listing(path, t):
    """A registry index README is a listing: its substance is the rows.

    Registry_716_to_757/README.md is five entity rows plus a tally and reads as
    complete at 65 words. Scoring it against a prose floor measured the wrong
    thing. It must still show a heading and at least four rows.
    """
    if not path.endswith('/README.md') or 'MAW_Codex_Sets' not in path:
        return False
    rows = len(re.findall(r'^\s*(?:[-|])\s*\S', t, re.M))
    return bool(h1(t)) and rows >= 4


def score_generic(path, t, floor):
    req = {}
    req['h1'] = bool(h1(t))
    # "Structured": can a reader find their way around it? A short rule file or a
    # batch-close record legitimately runs as bold-lead paragraphs under one H1 —
    # that is navigable. Requiring an H2 was penalising documents that read fine.
    # Four ways a document can give a reader a spine. The bold-lead form accepts a
    # numeral: R-14 and R-15 are built entirely of "**1. ...**", which the old
    # [A-Z] class could not see at all. The list form is how the batch-close
    # records are written: five entries, each opening with its subject in bold.
    req['sections'] = (len(re.findall(r'^##\s', t, re.M)) >= 1
                       or bool(re.search(r'^\|', t, re.M))
                       or len(re.findall(r'^\*\*[A-Z0-9][^*]{2,80}\*\*', t, re.M)) >= 3
                       or len(re.findall(r'^\s*[-*]\s+\*\*[^*]{2,60}\*\*', t, re.M)) >= 3)
    req['substance'] = (words(t) >= floor or record_shaped(t)
                        or registry_listing(path, t))
    return req


def classify(path):
    if path.startswith('SOMNARAK-WORLD/Sorrow_Entities/SE-'):
        return 'se-dossier'
    if re.search(r'MAW_Codex_Sets/.+SE-\d+-[BCD]__MAW-', path):
        return 'maw-record'
    if path.startswith('TEMPLATES/'):
        return 'template'
    if path.startswith('REFERENCE_SOMNARAK_WIKI/'):
        return 'reference'
    if path.startswith('SOMNARAK-WORLD/Master_Codices/'):
        return 'codex'
    if path.startswith('SOMNARAK-WORLD/'):
        return 'world-other'
    return 'root-doc'


FLOOR = {'codex': 400, 'template': 100, 'reference': 100, 'world-other': 250,
         'root-doc': 100}


def score_file(path):
    t = io.open(path, encoding='utf-8', errors='ignore').read()
    cls = classify(path)
    if cls == 'se-dossier':
        req = score_dossier(path, t)
    elif cls == 'maw-record':
        req = score_maw(path, t)
    else:
        req = score_generic(path, t, FLOOR.get(cls, 100))
    content = cls in ('se-dossier', 'maw-record', 'codex', 'world-other')
    req['no_scaffold'] = (not content) or not SCAFFOLD.search(t)
    req['no_split_hyphen'] = (not content) or not has_split_hyphen(t)
    req['no_ai_tic'] = (not content) or not ai_tic(t)
    met = sum(1 for v in req.values() if v)
    return cls, met, len(req), [k for k, v in req.items() if not v]


def collect():
    rows = []
    SKIP = ('REFERENCE_SOMNARAK_WIKI/AUDITS/FILE_FINISHEDNESS_2026-11-02.md',)
    for path in sorted(glob.glob('**/*.md', recursive=True)):
        if path.startswith(('.git/', 'ARCHIVE/', 'tools/tests/fixtures/')) or path in SKIP:
            continue
        cls, met, tot, missing = score_file(path)
        rows.append({'path': path, 'class': cls, 'met': met, 'total': tot,
                     'pct': round(100.0 * met / tot, 1), 'missing': ' '.join(missing)})
    return rows


def band(p):
    if p >= 95:
        return 'complete'
    if p >= 85:
        return 'near-complete'
    if p >= 70:
        return 'substantial'
    if p >= 50:
        return 'partial'
    return 'thin'


def main():
    rows = collect()
    by_class = {}
    for r in rows:
        by_class.setdefault(r['class'], []).append(r)

    print(f'FILES MEASURED: {len(rows)}')
    print(f'{"class":<14}{"files":>6}{"mean %":>9}{"median %":>10}   bands')
    for cls in sorted(by_class, key=lambda c: -len(by_class[c])):
        g = by_class[cls]
        pcts = [r['pct'] for r in g]
        b = {}
        for r in g:
            b[band(r['pct'])] = b.get(band(r['pct']), 0) + 1
        bs = ' '.join(f'{k[:4]}={v}' for k, v in sorted(b.items(), key=lambda x: -x[1]))
        print(f'{cls:<14}{len(g):>6}{statistics.mean(pcts):>9.1f}{statistics.median(pcts):>10.1f}   {bs}')

    allp = [r['pct'] for r in rows]
    print(f'\nOVERALL mean {statistics.mean(allp):.1f}%  median {statistics.median(allp):.1f}%')

    tally = {}
    for r in rows:
        for k in r['missing'].split():
            tally[k] = tally.get(k, 0) + 1
    print('\nMOST-MISSED OBLIGATIONS (files):')
    for k, v in sorted(tally.items(), key=lambda x: -x[1])[:12]:
        print(f'  {v:>4}  {k}')

    if '--worst' in sys.argv:
        n = int(sys.argv[sys.argv.index('--worst') + 1]) if len(sys.argv) > sys.argv.index('--worst') + 1 else 20
        print(f'\nLOWEST {n}:')
        for r in sorted(rows, key=lambda x: x['pct'])[:n]:
            print(f"  {r['pct']:>5.1f}%  {r['path']}\n         missing: {r['missing']}")

    if '--report' in sys.argv:
        out = sys.argv[sys.argv.index('--report') + 1]
        write_report(out, rows)
        print(f'wrote {out}')

    if '--csv' in sys.argv:
        out = sys.argv[sys.argv.index('--csv') + 1]
        with io.open(out, 'w', encoding='utf-8', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=['path', 'class', 'met', 'total', 'pct', 'missing'])
            w.writeheader()
            w.writerows(sorted(rows, key=lambda r: (r['pct'], r['path'])))
        print(f'\nwrote {out}')
    return 0


def write_report(path, rows):
    import datetime
    by_class = {}
    for r in rows:
        by_class.setdefault(r['class'], []).append(r)
    tally = {}
    for r in rows:
        for k in r['missing'].split():
            tally[k] = tally.get(k, 0) + 1

    maw = by_class.get('maw-record', [])
    sub = {'W': 0, 'S': 0, 'G': 0}
    subn = {'W': 0, 'S': 0, 'G': 0}
    for r in maw:
        for k in 'WSG':
            if f'__MAW-{k}_' in r['path']:
                subn[k] += 1
                if 'max_amount' not in r['missing'].split():
                    sub[k] += 1
    allp = [r['pct'] for r in rows]
    L = []
    A = L.append
    A('# File finishedness — every file, measured')
    A('')
    A(f'**Measured:** {datetime.date.today().isoformat()} · **files:** {len(rows):,} · '
      f'**mean:** {statistics.mean(allp):.1f}% · **median:** {statistics.median(allp):.1f}%')
    A('')
    A('## What this number is')
    A('')
    A("A file's percentage is **the share of its filed obligations it meets**. The obligations are not")
    A('opinions: they are the sections its template requires, the fields its own class carries in')
    A('90%+ of its members, the debts already on the record (the `Maximum Amount` gap, the')
    A('filename/H1 mismatch, the corrosion-prose debt), and the defect classes the linters police')
    A('(scaffold braces, split compounds, banned wording).')
    A('')
    A('**It is not a judgement of writing quality.** A dossier at 100% meets every structural')
    A('obligation that can be checked mechanically; that is all it means. Nothing here reads for')
    A('meaning, and a 100% file is not a good file — it is a file with nothing missing from its')
    A('checklist.')
    A('')
    A("The rubric is in `tools/finishedness.py`; every file's missing obligations are printed in the")
    A('CSV beside it, so any score can be argued with.')
    A('')
    A('## By class')
    A('')
    A('| Class | Files | Mean | Median | Complete ≥95% | Near 85–95% | Substantial 70–85% | Partial 50–70% | Thin <50% |')
    A('|---|---:|---:|---:|---:|---:|---:|---:|---:|')
    for cls in sorted(by_class, key=lambda c: -len(by_class[c])):
        g = by_class[cls]
        pcts = [r['pct'] for r in g]
        b = {}
        for r in g:
            b[band(r['pct'])] = b.get(band(r['pct']), 0) + 1
        A(f'| `{cls}` | {len(g):,} | {statistics.mean(pcts):.1f}% | {statistics.median(pcts):.1f}% | '
          f'{b.get("complete",0)} | {b.get("near-complete",0)} | {b.get("substantial",0)} | '
          f'{b.get("partial",0)} | {b.get("thin",0)} |')
    A('')
    A('## By wing')
    A('')
    wings = {}
    for r in rows:
        w = r['path'].split('/')[0] if '/' in r['path'] else '(root)'
        if r['path'].startswith('SOMNARAK-WORLD/'):
            parts = r['path'].split('/')
            w = 'SOMNARAK-WORLD/' + (parts[1] if len(parts) > 2 else '')
        wings.setdefault(w, []).append(r['pct'])
    A('| Wing | Files | Mean | Median |')
    A('|---|---:|---:|---:|')
    for w in sorted(wings, key=lambda x: -len(wings[x])):
        v = wings[w]
        A(f'| `{w}` | {len(v):,} | {statistics.mean(v):.1f}% | {statistics.median(v):.1f}% |')
    A('')
    A('## Where the missing share actually is')
    A('')

    A('')
    A('| Obligation | Files missing it | What it means |')
    A('|---|---:|---|')
    _order = sorted(tally.items(), key=lambda kv: -kv[1])
    _desc = {
        'max_amount': 'No stock ceiling filed — no `Maximum Amount` row, no `Maximum / Echo Cost` column, no inline `max N`.',
        'appearance': 'No Appearance section and no inline `**Appearance:**`.',
        'cost_line': 'No Echo cost (weapons, suits) or bestowal chance (stigmas).',
        'h1_match': 'The H1 does not carry the subject the filename names.',
        'statistics': 'No damage/speed/range/chance/grade line at all.',
        'sections': 'No second-level section — short index pages and stubs.',
        'substance': 'Below the class word floor.',
        'corrosion_stock': 'Corrosion prose present but not in the stock form.',
        'no_ai_tic': 'Banned wording in a content file.',
        'no_split_hyphen': 'A compound split by a space after its hyphen.',
        'h1': 'No H1 at all.',
        'no_scaffold': 'An unfilled two-brace placeholder in a content file.',
        'nine_headings': 'Missing one of the nine required dossier sections.',
        'secc_fields': 'A SECC classification field is empty.',
        'operational_fields': 'An Operational Parameters field is empty.',
        'story_log': 'No numbered entry under 이야기 보고.',
        'observation_log': 'The 관찰 기록 section is under 40 words.',
        'final_observation': 'The 최종 관찰 section is under 40 words.',
        'maw_named': 'No M.A.W. piece named and no non-extraction statement.',
        'ladder': 'A resistance band word is off the ladder.',
        'grade_token': 'A coherence letter sits in the potency grade.',
        'record_header': 'Missing Document ID, Linked Entity or Item Registry Code.',
        'set_link': 'No set or source relationship.',
    }
    for _k, _v in _order:
        A(f'| `{_k}` | {_v} | {_desc.get(_k, "")} |')
    A('')
    A('## The M.A.W. registry, block by block')
    A('')
    reg = {}
    for r in rows:
        if '/MAW_Codex_Sets/' in r['path']:
            m = re.search(r'Registry_([0-9]+)_to_([0-9]+)', r['path'])
            k = f'Registry {m.group(1)}–{m.group(2)}' if m else 'unfiled'
            reg.setdefault(k, []).append(r['pct'])
    A('| Registry block | Files | Mean | Median |')
    A('|---|---:|---:|---:|')
    for k in sorted(reg, key=lambda x: statistics.mean(reg[x])):
        v = reg[k]
        A(f'| {k} | {len(v):,} | {statistics.mean(v):.1f}% | {statistics.median(v):.1f}% |')
    A('')
    A('## The stock-ceiling debt, stated precisely')

    A('')
    A('The standing figure was *199 filed / 653 blank*. Re-measured with a wider definition — the row,')
    A('the weapon/suit `Maximum / Echo Cost` column, and the compact inline `max N` all count as a')
    A('filing — the number is **' + str(sum(sub.values())) + ' of 852 filed, ' + str(852 - sum(sub.values())) + ' not filed**')
    A('(' + ' · '.join(f'weapons {sub["W"]}/{subn["W"]}, suits {sub["S"]}/{subn["S"]}, stigmas {sub["G"]}/{subn["G"]}' for _ in [0]) + ').')
    A('')
    A('The difference is not a correction of the old figure — it is a correction of what counts. The')
    A('old count read only the explicit `Maximum Amount` label. **The stigma finding stands exactly as')
    A('recorded: ' + str(sub['G']) + ' of ' + str(subn['G']) + ' stigmas file a stock ceiling, because the Stigma schema has the field nowhere.**')
    A('')
    A('## Lowest-scoring files')
    A('')
    A('| File | Score | Missing |')
    A('|---|---:|---|')
    for r in sorted(rows, key=lambda x: x['pct'])[:25]:
        A(f'| `{r["path"]}` | {r["pct"]:.1f}% | {r["missing"]} |')
    A('')
    A('## Reproduce')
    A('')
    A('```bash')
    A('python3 tools/finishedness.py                      # summary')
    A('python3 tools/finishedness.py --worst 25           # lowest files')
    A('python3 tools/finishedness.py --csv out.csv        # every file, every missing key')
    A('```')
    A('')
    io.open(path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    sys.exit(main())
