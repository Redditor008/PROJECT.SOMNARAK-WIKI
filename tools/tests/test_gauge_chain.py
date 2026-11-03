#!/usr/bin/env python3
"""
tools/tests/test_gauge_chain.py

Proves the chain check can fail. A guard that always passes is decoration.

The fixtures are built in a temporary directory, never in the archive: a test that
writes fixtures into `SOMNARAK-WORLD/` would be a test that damages the thing it
is meant to protect.

What must fail
  * a piece quoting a meter its set record does not file
  * a piece whose failure mode cites a different meter than its own field
  * an A-page prose clause that disagrees with the A-page's own row
What must pass
  * the shipped shape: piece figures and A-row figures identical
  * a set that files no `**Gauge:**` field at all (older schema), which is skipped
"""

import io
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_gauge_chain as chain  # noqa: E402

A_PAGE = """# Set

| Field | Detail |
|---|---|
| Gauge / Pressure | {row} |

The Stigma identifies the source condition and the Weapon contains only the
immediate manifestation. {clause} The set cannot heal the originating event.
"""

PIECE = """# Piece

**Binding rule:** the bearer names the event and accepts this limit: keep the
series unbroken.

**Gauge:** {mx}; opens at {band}; no hit band is filed.

**Failure mode:** violating “keep the series unbroken” reverses the item’s benefit and raises the source Gauge, so the {fmx} meter moves off its {fband} opening band before the bearer feels the reversal.
"""


class Fixture:
    def __init__(self, tmp, row='739/739; starts 45–65% / no hit band',
                 clause='The gauge opens at 45–65% of its 739/739 meter, and no '
                        'hit band is filed.',
                 mx='739/739', band='45–65%', fmx='739/739', fband='45–65%'):
        self.dir = tmp
        io.open(os.path.join(tmp, 'SE-000-A__SIDE_CODEX_Test.md'), 'w',
                encoding='utf-8').write(A_PAGE.format(row=row, clause=clause))
        io.open(os.path.join(tmp, 'SE-000-B__MAW-W_Test.md'), 'w',
                encoding='utf-8').write(
            PIECE.format(mx=mx, band=band, fmx=fmx, fband=fband))


class TestChainFails(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: [os.remove(os.path.join(self.tmp, f))
                                 for f in os.listdir(self.tmp)])

    def test_piece_inventing_a_meter_fails(self):
        Fixture(self.tmp, mx='999/999')
        defects, n = chain.verify_set(self.tmp)
        self.assertEqual(n, 1)
        self.assertTrue(any('999/999' in d[1] for d in defects))

    def test_piece_with_a_different_band_fails(self):
        Fixture(self.tmp, band='10–20%')
        defects, _ = chain.verify_set(self.tmp)
        self.assertTrue(any('10–20%' in d[1] for d in defects))

    def test_failure_mode_on_another_meter_fails(self):
        Fixture(self.tmp, fmx='120/120')
        defects, _ = chain.verify_set(self.tmp)
        self.assertTrue(any('120/120' in d[1] for d in defects))

    def test_a_page_clause_disagreeing_with_its_row_fails(self):
        Fixture(self.tmp, clause='The gauge opens at 25–40% of its 739/739 meter, '
                                 'and no hit band is filed.')
        defects, _ = chain.verify_set(self.tmp)
        self.assertTrue(any('25–40%' in d[1] for d in defects))


class TestChainPasses(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: [os.remove(os.path.join(self.tmp, f))
                                 for f in os.listdir(self.tmp)])

    def test_shipped_shape_passes(self):
        Fixture(self.tmp)
        defects, n = chain.verify_set(self.tmp)
        self.assertEqual(n, 1)
        self.assertEqual(defects, [])

    def test_set_without_a_gauge_field_is_skipped(self):
        io.open(os.path.join(self.tmp, 'SE-000-A__SIDE_CODEX_Test.md'), 'w',
                encoding='utf-8').write('# Set\n\n| Gauge / pressure | 45–65% / Lament |\n')
        io.open(os.path.join(self.tmp, 'SE-000-B__MAW-W_Test.md'), 'w',
                encoding='utf-8').write('# Piece\n\nNo field here.\n')
        defects, n = chain.verify_set(self.tmp)
        self.assertEqual(n, 0)
        self.assertEqual(defects, [])


if __name__ == '__main__':
    unittest.main()
