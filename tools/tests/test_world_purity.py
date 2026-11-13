#!/usr/bin/env python3
"""
tools/tests/test_world_purity.py

Locks the folder rule in both directions.

The positive tests are the easy half: each leak pattern must fire on a line that
names our world. The negative tests are the half that matters. Every one of them
is a sentence this archive actually contains, and every one of them was flagged
as a leak by a first draft of the checker:

    "the owner's feelings about the memory"      — an in-world possession
    "the Day 177 record"                         — the world counting its own days
    "12,000 Files expunged"                      — a bank's ledger, not a repo
    "291 dossiers"                               — the Archive counting its holdings
    "PIN AT NODE 02"                             — a tactical order, not a WIP flag
    "the splinter" / "weeping"                   — neither is `linter` or `WIP`

A checker that flags those gets switched off, and a switched-off checker protects
nothing. So the negatives are as load-bearing as the positives.

Nothing here writes into the archive. The archive-wide assertion only reads.
"""

import io
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_world_purity as purity  # noqa: E402

PATTERNS = {kind: re.compile(pat, re.I) for kind, pat, _ in purity.LEAKS}


class TestLeaksFire(unittest.TestCase):
    """Each pattern must catch the defect it was written for."""

    def assertFires(self, kind, sample):
        self.assertTrue(PATTERNS[kind].search(sample),
                        f'{kind} failed to flag: {sample!r}')

    def test_real_world_date(self):
        self.assertFires('real-world-date', 'Filed 2026-10-10 by the registry.')
        self.assertFires('real-world-date', 'Recorded October 2026, unaltered.')

    def test_commit_hash(self):
        self.assertFires('commit-hash', 'Revision `3abe5470` retitled the item.')
        self.assertFires('commit-hash', 'commit 45ea2f5f closed the debt.')

    def test_build_batch(self):
        self.assertFires('build-batch', 'Batch 139 opened this class.')
        self.assertFires('build-batch', 'This repository holds the catalogue.')

    def test_wip_marker(self):
        self.assertFires('wip-marker', '> PIN WIP — reconciliation tracker')
        self.assertFires('wip-marker', 'WIP: finish the roster')

    def test_owner_voice(self):
        self.assertFires('owner-voice', 'The archive owner asked for this edit.')

    def test_outward_link(self):
        self.assertFires('outward-link', 'see https://github.com/Redditor008/x')
        self.assertFires('outward-link', 'see `REFERENCE_SOMNARAK_WIKI/GUIDES/x.md`')
        self.assertFires('outward-link', 'run `tools/timeline_lint.py`')

    def test_meta_count(self):
        self.assertFires('meta-count', 'The 1,196 files are organized across 42 ranges.')
        self.assertFires('meta-count', 'The catalogue indexes 290 of 291.')


class TestInWorldLinesPass(unittest.TestCase):
    """Lines the archive legitimately contains must never be flagged."""

    def assertClean(self, sample):
        for kind, pat in PATTERNS.items():
            self.assertIsNone(pat.search(sample),
                              f'{kind} misfired on in-world line: {sample!r}')

    def test_year_calendar_is_in_world(self):
        self.assertClean('Current_Year == 4238, at the dawn of the Year 4,238 epoch.')

    def test_possession_is_not_owner_voice(self):
        self.assertClean("The owner's feelings about the memory are not recorded.")

    def test_days_and_years_are_counts_of_time(self):
        self.assertClean('The Day 177 record shows what Dekan said.')
        self.assertClean('He did not file it inside the Year 202 record.')

    def test_a_ledger_is_not_a_repository(self):
        self.assertClean('12,000 Files expunged from the banking registry.')

    def test_dossier_counts_are_the_archive_counting_itself(self):
        self.assertClean('291 dossiers carry a unique SECC code.')
        self.assertClean('The Row keeps 44 case files open.')

    def test_pin_in_a_tactical_order(self):
        self.assertClean('PIN AT NODE 02 — hold the line.')

    def test_words_that_resemble_leak_words(self):
        self.assertClean('A splinter of glass in the weeping wall.')
        self.assertClean('Auditor, Keeper and Warden are ranks, not authors.')


class TestArchiveIsPure(unittest.TestCase):
    """The tree itself must measure 0 on every class, at the ratchet's floor."""

    def test_archive_measures_zero(self):
        counts = {kind: 0 for kind, _, _ in purity.LEAKS}
        paths = sorted(glob_paths())
        self.assertGreater(len(paths), 1000, 'archive scan found too few files')
        for path in paths:
            with io.open(path, encoding='utf-8') as fh:
                body = fh.read()
            if os.path.relpath(path, os.getcwd()).replace(os.sep, '/') == purity.CHARTER:
                body = purity.CHARTER_EXEMPT.sub('', body)
            for kind, pat in PATTERNS.items():
                counts[kind] += len(pat.findall(body))
        for kind, ceiling in purity.RATCHET.items():
            self.assertLessEqual(counts[kind], ceiling,
                                 f'{kind}: {counts[kind]} over ceiling {ceiling}')


def glob_paths():
    return [p for p in __import__('glob').glob(
        os.path.join(ROOT, 'SOMNARAK-WORLD', '**', '*.md'), recursive=True)]


if __name__ == '__main__':
    unittest.main()
