# -*- coding: utf-8 -*-
"""Gate 91 — the SECC table answers one question per row (R-51)."""
import io
import os
import unittest

from tools.auditors import check_secc_shape as gate

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

GOOD = """## SECC Classification

| **Designation** | `C-IIIβ-014 [VS]` |
| **Coherence** | Fragment (III) — Personality shaped by origin |
| **Potency** | Moderate (β) — Manageable with standard precautions |

## Operational Parameters
"""

BARE = """## SECC Classification

| **Designation** | `N-Iα-025 [LS]` |
| **Coherence** | Residue (I) |
| **Potency** | Minor (α) |

## Operational Parameters
"""


class TheShape(unittest.TestCase):
    """The pure half — no disk, no dossier path."""

    def test_a_cell_with_a_descriptor_passes(self):
        issues, stats = gate.audit(GOOD)
        self.assertEqual(issues, [])
        self.assertEqual(stats['coherence +desc'], 1)
        self.assertEqual(stats['designation'], 1)

    def test_a_cell_with_no_descriptor_is_correct(self):
        """175 real dossiers carry the value alone; absence is not a fault."""
        issues, stats = gate.audit(BARE)
        self.assertEqual(issues, [])
        self.assertEqual(stats['coherence value'], 1)

    def test_the_pair_written_backwards_fails(self):
        """The seven repaired files read `I — Residue (barely formed)`."""
        bad = GOOD.replace('Fragment (III) — Personality shaped by origin',
                           'III — Fragment (Personality shaped by origin)')
        issues, _ = gate.audit(bad)
        self.assertTrue(any('not "Value (Symbol)"' in why for why, _ in issues), issues)

    def test_a_word_that_disagrees_with_its_symbol_fails(self):
        bad = GOOD.replace('Fragment (III)', 'Fragment (IV)')
        issues, _ = gate.audit(bad)
        self.assertTrue(any('word/symbol disagree' in why for why, _ in issues), issues)

    def test_a_symbol_that_disagrees_with_the_designation_fails(self):
        """`C-IIIβ-014` fixes the rank and the potency; the rows cannot re-decide them."""
        bad = GOOD.replace('`C-IIIβ-014', '`C-IVδ-014')
        issues, _ = gate.audit(bad)
        self.assertEqual(len(issues), 2, issues)
        self.assertTrue(all('disagrees with Designation' in why for why, _ in issues), issues)

    def test_a_descriptor_that_became_a_sentence_fails(self):
        """The five repaired cells — a clause of behaviour with its own verb."""
        bad = GOOD.replace('Personality shaped by origin',
                           'Personality shaped by origin, which it carried from the household '
                           'that made it and has never once been persuaded to leave behind')
        issues, _ = gate.audit(bad)
        self.assertTrue(any('descriptor is a sentence' in why for why, _ in issues), issues)

    def test_a_descriptor_ending_in_a_full_stop_fails(self):
        bad = GOOD.replace('Personality shaped by origin', 'Personality shaped by origin.')
        issues, _ = gate.audit(bad)
        self.assertTrue(any('full stop' in why for why, _ in issues), issues)

    def test_a_missing_row_fails(self):
        bad = GOOD.replace('| **Potency** | Moderate (β) — Manageable with standard precautions |\n', '')
        issues, _ = gate.audit(bad)
        self.assertTrue(any('no Potency row' in why for why, _ in issues), issues)

    def test_a_dossier_with_no_secc_section_fails(self):
        issues, stats = gate.audit('# A file with no table\n')
        self.assertTrue(issues)
        self.assertEqual(stats['files'], 0)

    def test_the_designation_count_is_always_reported(self):
        """A cross-check that matched nothing must be visible, not green."""
        _, stats = gate.audit(GOOD.replace('`C-IIIβ-014 [VS]`', 'no code here'))
        self.assertEqual(stats['designation'], 0)


class TheArchive(unittest.TestCase):
    """Against the 301 dossiers on disk, which is the only place this can be proved."""

    def test_every_dossier_is_on_contract(self):
        bad = []
        for path in gate.dossier_files():
            issues, _ = gate.audit(io.open(path, encoding='utf-8').read())
            bad.extend((os.path.basename(path), why) for why, _ in issues)
        self.assertEqual(bad, [], bad[:5])

    def test_every_dossier_carries_a_designation_code(self):
        """If this ever reads 0 of 301 the cross-check has gone blind."""
        seen = 0
        for path in gate.dossier_files():
            _, stats = gate.audit(io.open(path, encoding='utf-8').read())
            seen += stats['designation']
        self.assertEqual(seen, len(gate.dossier_files()))
        self.assertGreater(seen, 300)


if __name__ == '__main__':
    unittest.main()
