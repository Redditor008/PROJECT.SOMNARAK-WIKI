#!/usr/bin/env python3
"""Validate the independent SE written-appearance ledger; never infer legacy credit."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / 'REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_LEDGER.json'
STATUSES = {'pending', 'blocked', 'held', 'changed', 'retained'}


def validate(data, inventory, root=ROOT):
    """inventory maps full designations to canonical repo-relative paths."""
    rows = data['dossiers']
    assert data['denominator'] == len(inventory) == 301, 'Corpus/denominator drift'
    ids = [r['designation'] for r in rows]
    assert len(ids) == len(set(ids)) == 301, 'Missing or duplicate dossier'
    assert set(ids) == set(inventory), 'Dossier inventory mismatch'
    paths = [r['path'] for r in rows]
    assert len(set(paths)) == 301, 'Duplicate path'
    for row in rows:
        assert row['path'] == inventory[row['designation']], 'Wrong identity/path'
        assert row['status'] in STATUSES, 'Unknown status'
        if row['status'] in {'changed', 'retained'}:
            assert row.get('outcome') in {'source-supported repair', 'owner-authorized redesign', 'retained design'}
            assert (row['status'] == 'retained') == (row['outcome'] == 'retained design')
            assert row.get('evidence') and (root / row['evidence']).is_file(), 'Missing evidence record'
            assert row.get('sources') and all((root / p).is_file() for p in row['sources']), 'Missing source file'
            assert row.get('whole_final_reread') is True, 'Final reread not recorded'
            assert row.get('checks') == dict.fromkeys(('verify', 'tpl', 'sectfile', 'wikistd', 'sect'), 'PASS'), 'Incomplete checks'
    batch = data['active_batch']
    assert batch['status'] in {'OPEN', 'CLOSED'}
    assert batch['required'] in {5, 7, 10}
    queue = batch['queue']
    assert len(queue) == len(set(queue)) == batch['required'] and set(queue) <= set(ids)
    by_id = {r['designation']: r for r in rows}
    done = sum(by_id[c]['status'] in {'changed', 'retained'} for c in queue)
    unchanged = sum(by_id[c]['status'] == 'retained' for c in queue)
    if batch['status'] == 'CLOSED':
        assert done == batch['required'], 'Cannot close below rung'
        assert unchanged < 3 or done == 10, 'No change ladder requires extension'
    counts = Counter(r['status'] for r in rows)
    return counts, done, unchanged


def corpus():
    # Same canonical corpus as the established section/prose tools; exclude the non-SE Book.
    import sect
    import maw_compare
    files, _, _ = sect.build()
    result = {}
    for file in files:
        p = Path(file)
        code = maw_compare.designation_from_primary(p.read_text())
        if code:
            assert code not in result, 'Duplicate primary designation'
            result[code] = p.resolve().relative_to(ROOT).as_posix()
    return result


def main():
    data = json.loads(LEDGER.read_text())
    counts, done, unchanged = validate(data, corpus())
    total = data['denominator']
    completed = counts['changed'] + counts['retained']
    print(f'SE Appearance Fix: {completed} / {total} = {completed / total:.2%}; remaining {total-completed} / {total}')
    print(f"Changed {counts['changed']} / {total}; retained {counts['retained']} / {total}; held {counts['held']} / {total}; blocked {counts['blocked']} / {total}; pending {counts['pending']} / {total}")
    b = data['active_batch']
    print(f"Batch {b['number']}: {b['status']} {done} / {b['required']}; No change {unchanged} / {done}")
    print('PASS: independent appearance ledger; no legacy credits inferred')


if __name__ == '__main__':
    main()
