# -*- coding: utf-8 -*-
"""Gate 93 — every dossier carries the sections its template asks for (R-45 s3)."""
import io
import os
import unittest

from tools.auditors import check_section_registry as gate

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CORE = ['SECC Classification', 'Operational Parameters', 'Appearance', 'Origin',
        'M.A.W. Equipment', '관찰 기록 (Observation Log)', '이야기 보고 (Story Log)',
        '최종 관찰 (Final Observation)', '감각 묘사 (Flavor Text)', '이야기 (Narratio)',
        '증언 (Testimonium)', '기록 (Registrum)', 'Trivia', 'Document Information']


def dossier(rank='III', grade='β', number='014', entity='**Subject** — Can breach',
            combat='Combat Record', behaviour='Behavior', drop=(), apex=False):
    heads = [h for h in CORE if h not in drop]
    if combat:
        heads.insert(2, combat)
    if behaviour:
        heads.insert(5, behaviour)
    if apex:
        heads.append('Apex Record')
    body = '\n'.join('## %s\n\ntext\n' % h for h in heads)
    return ("| **Designation** | `C-%s%s-%s [VS]` |\n| **Entity Type** | %s |\n\n"
            % (rank, grade, number, entity)) + body


class TheRequirements(unittest.TestCase):
    """The pure half — a synthetic dossier, no disk."""

    def test_a_whole_subject_dossier_passes(self):
        missing, code = gate.audit(dossier(rank='V', grade='δ', apex=True))
        self.assertEqual(missing, [], missing)
        self.assertEqual(code, 'C-Vδ-014')

    def test_a_missing_core_section_is_named(self):
        """The four dossiers with no closing tail: 증언 removed."""
        missing, _ = gate.audit(dossier(drop=('증언 (Testimonium)',)))
        self.assertEqual(missing, ['증언 (Testimonium)'])

    def test_the_closing_tail_can_go_missing_together(self):
        tail = ('최종 관찰 (Final Observation)', '증언 (Testimonium)', '기록 (Registrum)',
                'Document Information')
        missing, _ = gate.audit(dossier(drop=tail))
        self.assertEqual(sorted(missing), sorted(tail))

    def test_a_relic_may_carry_contact_record(self):
        """The template's own alternate — no combat actions, so no Combat Record."""
        missing, _ = gate.audit(dossier(entity='**Object** — Not worked', combat='Contact Record',
                                       behaviour='Handling Process'))
        self.assertEqual(missing, [])

    def test_a_subject_must_carry_behavior_not_handling(self):
        missing, _ = gate.audit(dossier(entity='**Subject** — Can breach',
                                        behaviour='Handling Process'))
        self.assertEqual(missing, ['Behavior'])

    def test_a_relic_must_carry_handling_not_behavior(self):
        missing, _ = gate.audit(dossier(entity='**Object** — Not worked',
                                        behaviour='Behavior'))
        self.assertEqual(missing, ['Handling Process'])

    def test_a_rank_v_without_apex_record_fails(self):
        missing, _ = gate.audit(dossier(rank='V', grade='ω', apex=False))
        self.assertEqual(missing, ['Apex Record'])

    def test_apex_record_is_not_required_below_rank_iv(self):
        missing, _ = gate.audit(dossier(rank='III', grade='β', apex=False))
        self.assertEqual(missing, [])

    def test_rank_iv_does_require_apex_record(self):
        missing, _ = gate.audit(dossier(rank='IV', grade='δ', apex=False))
        self.assertEqual(missing, ['Apex Record'])


class TheDebt(unittest.TestCase):
    """A recorded gap passes; an unrecorded one fails. The count may only fall."""

    def test_a_recorded_gap_is_not_new(self):
        new, known = gate.split_debt([('C-Vγ-225', ['Apex Record'])])
        self.assertEqual((new, len(known)), ([], 1))

    def test_an_unrecorded_gap_is_new(self):
        new, known = gate.split_debt([('C-IIIβ-014', ['Apex Record'])])
        self.assertEqual(len(new), 1)
        self.assertEqual(known, [])

    def test_a_second_gap_in_a_recorded_dossier_is_still_new(self):
        """Recorded for Apex only; losing a closing section is a fresh fault."""
        new, known = gate.split_debt([('C-Vγ-225', ['Apex Record', '증언 (Testimonium)'])])
        self.assertEqual([s for _, s in new], ['증언 (Testimonium)'])
        self.assertEqual(len(known), 1)

    def test_the_debt_covers_the_tail_files(self):
        for code in ('N-IIIβ-1056', 'N-Vω-1055', 'O-IIIγ-1052'):
            self.assertIn('Document Information', gate.DEBT[code])


class TheArchive(unittest.TestCase):
    """Against the 301 dossiers on disk."""

    def test_no_dossier_has_an_unrecorded_gap(self):
        gaps = []
        for path in gate.dossier_files():
            missing, code = gate.audit(gate.read(path))
            if missing:
                gaps.append((code or os.path.basename(path), missing))
        new, _ = gate.split_debt(gaps)
        self.assertEqual(new, [], new[:5])

    def test_the_gate_reads_every_dossier(self):
        self.assertEqual(len(gate.dossier_files()), 301)

    def test_the_debt_is_a_snapshot_not_a_policy(self):
        """Every debt key must name a section the gate actually checks."""
        known_sections = set(gate.ALWAYS) | {'Apex Record', 'Behavior', 'Handling Process',
                                              ' / '.join(gate.EITHER)}
        for code, sections in gate.DEBT.items():
            self.assertTrue(sections.issubset(known_sections), (code, sections))


if __name__ == '__main__':
    unittest.main()
