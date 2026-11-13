#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_command_capture.py — gate 94: a command ends in a file (R-52, O-38).

WHY THIS EXISTS

The archive said it three times in prose — *"a rule that lives only in a conversation will be broken
by whoever reads the file next"*, *"an order that is only in a chat log is not a standard"*, *"no
command lives only in a chat log"* — and never once as a rule or a check. So it happened: the SECC
Refinement was given and was not in the register for four batches, and three gates were written,
tested, indexed, cited and never added to the build.

This gate reads the registers against each other, because a command leaves a mark in at least one of
them or it did not happen.

WHAT FAILS

  * an `R-nn` file on disk that `COMMAND_REGISTER.md` never names;
  * an `O-nn` in `OWNER_DIRECTIVES.md` that is not a row of the register's Part II table;
  * a batch heading in `WORK_IN_PROGRESS.md` that falls outside every era the register declares;
  * a declared batch span that stops short of the highest batch on record.

WHAT IS REPORTED

  * each count on both sides, so a check that matched nothing is visible rather than green.

    python3 tools/auditors/check_command_capture.py
    python3 tools/auditors/check_command_capture.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RULES_DIR = 'REFERENCE_SOMNARAK_WIKI/RULES'
REGISTER = 'REFERENCE_SOMNARAK_WIKI/COMMAND_REGISTER.md'
DIRECTIVES = os.path.join(RULES_DIR, 'OWNER_DIRECTIVES.md')
WIP = 'REFERENCE_SOMNARAK_WIKI/WORK_IN_PROGRESS.md'

RULE_FILE = re.compile(r'^(R-\d+)_.+\.md$')
ORDER_HEAD = re.compile(r'^### (O-\d+)', re.M)
ORDER_ROW = re.compile(r'^\|\s*\*\*(O-\d+)\*\*', re.M)
BATCH_HEAD = re.compile(r'^## Batch (\d+)', re.M)
SPAN = re.compile(r'Batches run 1 to (\d+)')


def read(path):
    with io.open(os.path.join(ROOT, path), encoding='utf-8') as fh:
        return fh.read()


def rule_ids():
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, RULES_DIR, 'R-*.md'))):
        m = RULE_FILE.match(os.path.basename(path))
        if m:
            out.append(m.group(1))
    return out


def part_four(register):
    """Just the era table — Part IV between its heading and Part V."""
    start = register.find('# Part IV')
    end = register.find('# Part V')
    return register[start:end] if start >= 0 else ''


def era_ranges(register):
    """Every `a–b` the era table declares in its batch column."""
    ranges = []
    for cell in re.findall(r'^\|\s*\*\*[^|]+\*\*\s*\|\s*([0-9][0-9–\-, ]*?)\s*\|',
                           part_four(register), re.M):
        for a, b in re.findall(r'(\d+)\s*[–-]\s*(\d+)', cell):
            ranges.append((int(a), int(b)))
        for single in re.findall(r'(?<![–\-\d])(\d{1,3})(?![–\-\d])', cell):
            ranges.append((int(single), int(single)))
    return ranges


def unfiled(rules, orders, batches, table_orders, ranges, span):
    """Everything that ends nowhere. Pure — the tests drive it without disk."""
    issues = []
    reg = span['register']
    for rid in rules:
        if rid not in reg:
            issues.append(('rule', rid, 'on disk, not named in COMMAND_REGISTER.md'))
    for oid in orders:
        if oid not in table_orders:
            issues.append(('order', oid, 'stated, not a row of the register Part II table'))
    for n in batches:
        if not any(a <= n <= b for a, b in ranges):
            issues.append(('batch', str(n), 'no era in the register accounts for it'))
    if batches and span['declared'] and span['declared'] < max(batches):
        issues.append(('span', str(span['declared']),
                       'declared span stops short of batch %d' % max(batches)))
    return issues


def measure():
    register = read(REGISTER)
    orders_text = read(DIRECTIVES)
    wip_text = read(WIP)
    m = SPAN.search(register)
    span = {'register': register, 'declared': int(m.group(1)) if m else None}
    return {
        'rules': rule_ids(),
        'orders': ORDER_HEAD.findall(orders_text),
        'batches': sorted({int(b) for b in BATCH_HEAD.findall(wip_text)}),
        'table_orders': set(ORDER_ROW.findall(register)),
        'ranges': era_ranges(register),
        'span': span,
        'register': register,
    }


def main(argv):
    verbose = '-v' in argv
    d = measure()
    issues = unfiled(d['rules'], d['orders'], d['batches'],
                     d['table_orders'], d['ranges'], d['span'])
    if verbose:
        for kind, ident, why in issues:
            print('%-7s %-10s %s' % (kind, ident, why))
    print('rules on disk %d · named in the register %d'
          % (len(d['rules']), len(d['rules']) - sum(1 for i in issues if i[0] == 'rule')))
    print('orders stated %d · rows in the register table %d'
          % (len(d['orders']), len(d['table_orders'])))
    print('batches in WORK_IN_PROGRESS %d · eras declared %d · declared span 1 to %s'
          % (len(d['batches']), len(d['ranges']), d['span']['declared']))
    print('commands with no entry: %d' % len(issues))
    if issues:
        print('RESULT: FAIL — %d commands ended in no file' % len(issues))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
