# -*- coding: utf-8 -*-
"""Gate 52 — a backstory is a story (R-56, O-42)."""
import unittest

from tools.auditors import check_echo_backstory as gate

PROSE = ('He was a researcher before he was a title. ' * 130)


def doc(heading='Backstory', words=PROSE, after='## Abilities'):
    return '# Echo-Core\n\n## Profile\n\nstuff\n\n## %s\n\n%s\n\n%s\n\nbody\n' % (
        heading, words, after)


class TheSection(unittest.TestCase):
    """Every Echo-Core dossier carries one, under whichever name it uses."""

    def test_each_heading_is_accepted(self):
        for name in ('Backstory', 'Origins', 'History', 'Origin'):
            words, subs, issue = gate.audit(doc(heading=name))
            self.assertIsNone(issue, name)

    def test_a_missing_section_fails(self):
        words, subs, issue = gate.audit('# Echo-Core\n\n## Profile\n\nstuff\n')
        self.assertEqual(issue, 'no backstory section')

    def test_the_archive_all_carry_one(self):
        missing = [p for p in gate.files() if gate.audit(gate.read(p))[2] == 'no backstory section']
        self.assertEqual(missing, [])


class TheFloor(unittest.TestCase):
    """A summary is not a story, and its length is the one part that can be measured."""

    def test_the_old_majin_section_fails(self):
        """365 words in five stub paragraphs — the section the owner rejected."""
        words, subs, issue = gate.audit(doc(words='He was a researcher. ' * 70))
        self.assertEqual(issue, 'under the floor')

    def test_a_full_section_passes(self):
        self.assertIsNone(gate.audit(doc())[2])

    def test_the_floor_is_not_a_target(self):
        """Explicit: one word over the floor with no subheads still passes the gate, because the
        gate cannot read. O-16 governs the rest."""
        words, subs, issue = gate.audit(
            doc(words=' '.join(['word'] * (gate.FLOOR + 1))))
        self.assertIsNone(issue)
        self.assertEqual(subs, 0)

    def test_the_archive_clears_the_floor(self):
        bad = [(p, gate.audit(gate.read(p))[2]) for p in gate.files()
               if gate.audit(gate.read(p))[2]]
        self.assertEqual(bad, [])

    def test_majin_is_no_longer_the_shortest(self):
        """The defect was relative as well as absolute: the central character had the shortest
        life story in the set."""
        rows = {p: gate.audit(gate.read(p))[0] for p in gate.files()}
        director = [w for p, w in rows.items() if 'THE_DIRECTOR' in p][0]
        self.assertGreater(director, gate.FLOOR)
        self.assertGreater(len([w for w in rows.values() if w < director]), 0)


if __name__ == '__main__':
    unittest.main()
