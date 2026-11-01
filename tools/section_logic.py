#!/usr/bin/env python3
"""section_logic.py — whole-file logic audit, section by section.

`breach.py` and `label_lint.py` read the section that carries the claim. This reads
the dossier end to end and asks whether the sections agree with each other: the
classification against the event heading, the two tables against each other, the
resolution row against the sentence the watch is told to close on, the record section
against the rows it is supposed to carry.

Checks that the archive has already settled are honoured here: `tools/review.py`
records that a single heading repeated under *different* parents is by design (the
activation block and the breach block each carrying their own `### Escalation
Notes`), so a repeat is reported only under the same parent, or when two or more
headings repeat together.

  section_logic.py            summary by class
  section_logic.py <path>     one dossier, every finding
  section_logic.py --list C   every dossier in class C
"""
import glob, io, os, re, sys, collections

ELEMS = ('Lament', 'Grudge', 'Void', 'Weight')
EVENT_HEADS = ('## Breach Behavior', '## Activation Behavior', '## Containment Event Behavior',
               '## Expansion Behavior')
CONTACT_CATS = ('Register', 'Exposure', 'Refusal', 'Overload', 'Contagion', 'Attachment',
                'Registering')


def dossiers():
    return sorted(glob.glob('SOMNARAK-WORLD/*/SE-*'))


def split(text):
    """[(heading, level, parent, body)] — body runs to the next heading of the same
    level or higher, so a section is never reported empty because it opens with a
    subheading. parent is the nearest heading above it with a lower level."""
    lines = text.split('\n')
    items = []
    for i, line in enumerate(lines):
        m = re.match(r'^(#{1,6})\s+(\S.*)$', line)
        if m:
            items.append((i, len(m.group(1)), line.strip()))
    out = []
    for k, (i, lvl, head) in enumerate(items):
        end = len(lines)
        for j, lvl2, _ in items[k + 1:]:
            if lvl2 <= lvl:
                end = j
                break
        parent = '(preamble)'
        for i2, lvl2, head2 in reversed(items[:k]):
            if lvl2 < lvl:
                parent = head2
                break
        out.append((head, lvl, parent, '\n'.join(lines[i + 1:end])))
    return out


def h2s(text):
    return [l.strip() for l in text.split('\n') if l.startswith('## ')]


def h3s(text):
    return [l.strip() for l in text.split('\n') if l.startswith('### ')]


def row(text, label):
    m = re.search(r'\|\s*\*{0,2}' + label + r'\*{0,2}\s*\|\s*(.+?)\s*\|', text)
    return m.group(1).strip() if m else None


def rows(text, label):
    return [m.group(1).strip() for m in
            re.finditer(r'\|\s*\*{0,2}' + label + r'\*{0,2}\s*\|\s*(.+?)\s*\|', text)]


def strip_mode(s):
    return re.sub(r'\s+', ' ', re.sub(r'[*`]', '', s or '')).strip().rstrip('.')


def audit(path):
    t = io.open(path, encoding='utf-8').read()
    name = os.path.basename(path)[:52]
    etype = row(t, 'Entity Type') or ''
    nonbreach = 'on-breaching' in etype
    heads2 = h2s(t)
    out = []
    add = lambda c, m: out.append((c, m))

    # ---- 1. classification against the event heading -------------------------
    if nonbreach and '## Breach Behavior' in heads2:
        add('category', 'Entity Type is non-breaching and the file still heads ## Breach Behavior')
    if not nonbreach and 'Can breach' in etype and '## Breach Behavior' not in heads2:
        add('category', 'Entity Type says Can breach; no ## Breach Behavior section, only %s'
            % [h for h in heads2 if h in EVENT_HEADS])

    # ---- 2. rows that only a breach record carries ---------------------------
    if nonbreach:
        for lab in ('| **Breach Type** |', '- **Breach type:**', '**Breach type:**'):
            if lab in t:
                add('breach-row', 'non-breaching dossier still carries %r' % lab.strip())

    # ---- 3. the contact record and what it may carry (R-36) ------------------
    if '## Contact Record' in heads2:
        for bad in ('Han Pressure [ATK]', '### Combat Actions', '### Battle Phases',
                    '**Battle Length**', '**Battlefield**', '**Threat Role**'):
            if bad in t:
                add('contact', 'contact record still carries %r' % bad)
        has_events = any(x in h3s(t) for x in ('### Contact Events', '### Possession Events'))
        if not has_events:
            add('contact', 'contact record carries no event table')
        for need in ('### Watch Sequence', '### Consequences'):
            if need not in h3s(t):
                add('contact', 'contact record is missing %s' % need)
        if '### Contact Events' in h3s(t) and '### Possession Events' in h3s(t):
            add('contact', 'two event tables: both ### Contact Events and ### Possession Events')
        for h, lvl, parent, body in split(t):
            if h in ('### Contact Events', '### Possession Events'):
                for cat in re.findall(r'\[\*\*(\w+)\*\*\]', body):
                    if cat not in CONTACT_CATS:
                        add('contact', 'event table uses the combat category [**%s**]' % cat)
        if re.search(r'\| \*\*Speed\*\* \|', t):
            add('contact', 'contact record keeps a Speed row')

    # ---- 4. references to a section this file does not have ------------------
    for ref, need in (('Combat Record', '## Combat Record'), ('Combat Actions', '### Combat Actions'),
                      ('Battle Phases', '### Battle Phases'), ('Tool Use Profile', '### Tool Use Profile')):
        if need not in t:
            for m in re.finditer(re.escape(ref), t):
                line = t[:m.start()].split('\n')[-1] + t[m.start():].split('\n')[0]
                if re.search(r'\b(no|never|has no|without)\b[^.]{0,24}' + re.escape(ref), line):
                    continue
                if 'no combat' in line.lower() or 'asked for the' in line.lower():
                    continue
                add('dangling', 'refers to %r, which this file does not have' % ref)
                break

    # ---- 5. a heading repeated under the same parent -------------------------
    seen = collections.defaultdict(list)
    for h, lvl, parent, _ in split(t):
        if lvl >= 3:
            seen[h].append(parent)
    for h, parents in seen.items():
        if len(parents) > 1 and len(set(parents)) < len(parents):
            add('dupe', '%s appears %d times under the same parent' % (h, len(parents)))

    # ---- 6. a section with no body at all ------------------------------------
    for h, lvl, parent, body in split(t):
        if lvl == 2 and not body.strip():
            add('empty', '%s is empty' % h)

    # ---- 7. the same fact stated twice --------------------------------------
    def core(label, pat):
        vals = {m.group(1) for v in rows(t, label) for m in [re.search(pat, v)] if m}
        return vals
    for label, pat, human in (
            ('Starting Sorrow Gauge', r'(\d{1,3})\s*[–-]\s*(\d{1,3})', 'opening band'),
            ('Location', r'^([A-Z][\w\- ]+)', 'location'),
            ('Element', r'^(\w+)', 'element'),
            ('Manifestation', r'^(\w+)', 'manifestation')):
        vals = core(label, pat)
        if len(vals) > 1:
            add('row-conflict', '%s stated %d ways: %s' % (label, len(vals), ' ; '.join(sorted(vals))[:160]))
    hp = {m.group(1) for v in rows(t, 'Sorrow Gauge \\[HP\\]')
          for m in [re.match(r'([\d,]+)', v)] if m}
    if len(hp) > 1:
        add('row-conflict', 'Sorrow Gauge [HP] stated as %s' % ' vs '.join(sorted(hp)))

    # ---- 8. the close against the resolution row -----------------------------
    res = row(t, 'Resolution Condition')
    close = re.search(r'\*\*How it closes:\*\*(.+)', t)
    if res and close:
        sent = close.group(1).lower()
        key = re.findall(r'[A-Za-z]{6,}', strip_mode(res))[:6]
        if key and sum(1 for w in key if w.lower() in sent) < max(1, len(key) // 3):
            add('resolve', 'the closing sentence does not carry the Resolution Condition (%r)'
                % strip_mode(res)[:70])

    # ---- 9. activation inside the opening band -------------------------------
    act = row(t, 'Activation threshold') or ''
    start = row(t, 'Starting Sorrow Gauge') or ''
    ma = re.search(r'(\d{1,3})\s*%', act)
    ms = re.match(r'\s*(\d{1,3})\s*[–-]\s*(\d{1,3})\s*%', start)
    if ma and ms and int(ma.group(1)) <= int(ms.group(2)):
        add('activation', 'activation %s%% sits inside the opening band %s' % (ma.group(1), start))

    # ---- 10. pressure element against the Element row ------------------------
    elem = row(t, 'Element') or ''
    atk = row(t, 'Han Pressure \\[ATK\\]') or ''
    if elem and atk:
        e = elem.split('(')[0].strip()
        if e in ELEMS and e not in atk:
            add('element', 'Element %s but pressure reads %r' % (e, atk[:50]))

    # ---- 11. non-breaching prose that still asserts an escape ----------------
    NARRATIVE = ('### Consequences', '### Operational Notes', '### Operational Work Notes',
                 '### Special Behaviors', '## Origin', '## Trivia', '## Warden Record',
                 '## Apex Record', '## Watch Record', '## 기록 (Registrum) — The Record',
                 '### Registry Addendum', '## 감각 묘사 (Flavor Text)')
    ESCAPE = re.compile(r'breaks? (?:out of|containment)|'
                        r'escapes? (?:the|from) (?:vault|cell|bay|containment|facility|chamber|'
                        r'sector|room|wing|walls)|'
                        r'pursues (?:the worker|personnel|the watch)|'
                        r'attacks (?:the worker|personnel)', re.I)
    if nonbreach:
        for h, lvl, parent, body in split(t):
            if h not in NARRATIVE:
                continue
            for line in body.split('\n'):
                if line.strip().startswith('|'):
                    continue
                if 'no combat' in line.lower() or 'has never' in line.lower():
                    continue
                if ESCAPE.search(line):
                    add('prose', '%s: %r' % (h, line.strip()[:110]))
                    break

    # ---- 11b. the detailed activation record restating the manifestation ----
    main_man = row(t, 'Manifestation')
    det = re.search(r'\|\s*\*\*Manifestation\*\* \|\s*([A-Za-z/-]+)', t[t.find('### Detailed Activation Record'):]) \
        if '### Detailed Activation Record' in t else None
    if main_man and det and not main_man.startswith(det.group(1).strip()):
        add('manifestation', 'Detailed Activation Record says %r, classification says %r'
            % (det.group(1).strip(), main_man))

    # ---- 11c. a resolution the Work Type table cannot deliver ---------------
    res2 = res or ''
    if re.search(r'gauge (?:falls|comes in|is brought) (?:below|under)', res2, re.I) or \
            re.search(r'below \d+ per cent', res2, re.I):
        table = ''
        for h, lvl, parent, body in split(t):
            if h == '## Behavior':
                table = body
        if table:
            dec = [w for w in ('Flerehan', 'Pugnahan', 'Viderehan', 'Ferrehan')
                   if re.search(r'\| \*\*' + w + r'\*\*[^\n]*\|[^\n]*Decrease', table)]
            if not dec:
                add('resolve', 'resolution reads the gauge down but no Work Type decreases it')

    # ---- 11d. what a possession record has to carry --------------------------
    if 'possession' in etype.lower() and '## Contact Record' in heads2:
        for need in ('Who it takes', 'Recovery'):
            if row(t, need) is None:
                add('possession', 'possession record is missing the %r row' % need)
        if '### Possession Events' not in h3s(t):
            add('possession', 'possession record carries no ### Possession Events')

    # ---- 11e. a Work Type that moves the gauge but is not valid ------------
    vt = row(t, 'Valid Work Types') or ''
    if vt and 'only' in vt.lower():
        allowed = set(re.findall(r'(Flerehan|Pugnahan|Viderehan|Ferrehan)', vt))
        for h, lvl, parent, body in split(t):
            if h != '## Behavior':
                continue
            for line in body.split('\n'):
                m = re.match(r'\| \*\*(Flerehan|Pugnahan|Viderehan|Ferrehan)\*\*[^|]*\|[^|]*\|[^|]*?Decrease', line)
                if m and m.group(1) not in allowed:
                    add('work-types', '%s moves the gauge here but the Valid Work Types row excludes it'
                        % m.group(1))

    # ---- 11f. a reason line citing a Movement word the row does not carry ---
    why = re.search(r'> \*\*Why this file has no combat actions\.\*\*(.+)', t)
    mov = rows(t, 'Movement')
    if why and mov:
        joined = ' '.join(mov).lower()
        for word in ('stationary', 'fixed', 'mobile', 'recumbent', 'rooted', 'seated', 'motionless'):
            if re.search(r'movement row says[^.]{0,40}\b' + word, why.group(1), re.I) and word not in joined:
                add('contact', 'the reason line cites %r, which the Movement row does not say' % word)

    # ---- 11g. a watch sequence with the wrong number of movements -----------
    for h, lvl, parent, body in split(t):
        if h == '### Watch Sequence':
            n = len(re.findall(r'^\d+\. ', body, re.M))
            if n and n != 3:
                add('watch', 'Watch Sequence has %d steps, not three' % n)

    # ---- 11h. the same sentence twice inside one file -----------------------
    seen_s = {}
    for line in t.split('\n'):
        s2 = line.strip()
        if len(s2) < 90 or s2.startswith(('|', '>', '#', '-')):
            continue
        if s2 in seen_s:
            add('repeat', 'the same sentence appears twice: %r' % s2[:80])
            break
        seen_s[s2] = 1

    # ---- 11i. the identification profile restating a different type --------
    typ = re.match(r'\*\*([^*]+)\*\*', etype)
    for m in re.finditer(r'^- \*\*Entity Type:\*\*\s*(.+)$', t, re.M):
        prof = m.group(1).strip()
        cls = re.sub(r'\s*\(.*?\)', '', typ.group(1) if typ else '').strip()
        if cls and prof.split('/')[0].strip() not in cls and cls.split('/')[0].strip() not in prof:
            add('profile', 'identification profile says Entity Type %r, classification says %r'
                % (prof, cls))

    # ---- 11j. an M.A.W. piece on an element the archive does not have -------
    for m in re.finditer(r'\*\*Type:\*\* (Weapon|Suit|Armor|Stigma) \| \*\*Grade:\*\* [^|]+ \| '
                         r'\*\*Element:\*\* ([A-Za-z]+)', t):
        if m.group(2) == 'Mixed' and re.search(r'cycles all four|all four elements', t):
            continue
        if m.group(2) not in ELEMS + ('Dream', 'Fracture', 'Tale'):
            add('maw', '%s piece declares an unknown element %r' % (m.group(1), m.group(2)))

    # ---- 12. M.A.W. pieces ---------------------------------------------------
    maw = re.findall(r'^### M\.A\.W\. (Weapon|Suit|Stigma)', t, re.M)
    if maw and len(set(maw)) < 3 and 'M.A.W.' in t:
        missing = {'Weapon', 'Suit', 'Stigma'} - set(maw)
        if 'not issued' not in t and 'no Suit' not in t and 'no Stigma' not in t:
            add('maw', 'M.A.W. block is missing %s and says so nowhere' % ', '.join(sorted(missing)))

    # ---- 13. species prefix against manifestation ----------------------------
    typ = re.match(r'\*\*([^*]+)\*\*', etype)
    man = row(t, 'Manifestation') or ''
    if typ and man and '-' in man:
        pre = man.partition('-')[0].strip()
        parts = {re.sub(r'\s*\(.*?\)', '', x).strip() for x in typ.group(1).split('/')}
        if pre in ('Object', 'Place', 'Subject', 'Time', 'Hazard') and pre not in parts:
            add('manifestation', 'Entity Type %r against Manifestation %r' % (typ.group(1), man))
    return name, out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    if '--list' in sys.argv:
        cls = sys.argv[sys.argv.index('--list') + 1]
        for p in dossiers():
            n, res = audit(p)
            for c, m in res:
                if c == cls:
                    print('%-52s %s' % (n, m))
                    break
        return 0
    if args:
        for p in args:
            n, res = audit(p)
            print(n)
            for c, m in res:
                print('  [%s] %s' % (c, m))
        return 0
    tally = collections.Counter()
    byclass = collections.defaultdict(list)
    for p in dossiers():
        n, res = audit(p)
        for c, m in res:
            tally[c] += 1
            byclass[c].append((n, m))
    total = sum(tally.values())
    print('AUDITED %d dossiers · %d findings' % (len(dossiers()), total))
    print('SECTION LOGIC: %s' % ('PASS' if total == 0 else 'REVIEW'))
    for c, k in tally.most_common():
        print('\n%s — %d' % (c, k))
        for n, m in byclass[c][:5]:
            print('   %-52s %s' % (n, m[:120]))
    print('\nSECTION LOGIC: %s' % ('PASS' if total == 0 else 'REVIEW'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
