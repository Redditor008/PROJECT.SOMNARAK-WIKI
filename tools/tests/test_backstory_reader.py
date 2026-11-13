# -*- coding: utf-8 -*-
"""Gate 51 — a file is read once, in order (R-55, O-41)."""
import unittest

from tools.auditors import check_backstory_reader as gate

APPENDIX = """
## Appendix

### Scene ledger

| # | Scene |
|---:|---|
| 1 | Day 10 |
| 2 | Day 40 |

### Chronological spine

| When | Scene | What changes |
|---|---|---|
| Day 10 | A | one |
| Day 40 | B | two |
"""


def doc(*headings):
    body = '\n\n'.join('### %s\n\nprose.\n' % h for h in headings)
    return body + APPENDIX


class Order(unittest.TestCase):
    """The body must be read in the order it claims."""

    def test_a_clean_file_passes(self):
        self.assertEqual(gate.audit(doc('Day 10 — A', 'Day 40 — B')), [])

    def test_a_day_anchor_going_backwards_fails(self):
        """The Seiyon defect: Part One ended on Day 108 and Part Two opened on Day 0."""
        issues = gate.audit(doc('Day 0 — A', 'Day 108 — B', 'Day 0 — C', 'Day 17 — D'))
        self.assertTrue(any('backwards' in why for why, _ in issues), issues)

    def test_a_day_anchor_after_a_year_anchor_fails(self):
        """The Marjuk defect: a Year 4,235 scene filed between Day 49 and Day 77."""
        issues = gate.audit(doc('Day 10 — A', 'Year 4,235 — B', 'Day 40 — C'))
        self.assertTrue(any('after a year anchor' in why for why, _ in issues), issues)

    def test_a_year_anchor_after_every_day_is_fine(self):
        self.assertEqual(gate.audit(doc('Day 10 — A', 'Day 40 — B', 'Year 4,238 — C')), [])

    def test_a_day_the_appendix_never_names_fails(self):
        issues = gate.audit(doc('Day 10 — A', 'Day 99 — B'))
        self.assertTrue(any('never accounts for' in why for why, _ in issues), issues)

    def test_a_spine_that_runs_backwards_fails(self):
        bad = APPENDIX.replace('| Day 40 | B | two |', '| Day 40 | B | two |\n| Day 5 | C | three |')
        text = '### Day 10 — A\n\nprose.\n' + bad
        issues = gate.audit(text)
        self.assertTrue(any('spine itself runs backwards' in why for why, _ in issues), issues)


class Reading(unittest.TestCase):
    """The gate must not fire on things that are not anchors."""

    def test_a_grouped_day_row_is_read(self):
        """Files 05 and 06 file their flashbacks as `Days 7, 41, 73` in one row."""
        text = doc('Day 10 — A').replace('| 1 | Day 10 |', '| 1 | Day 10 |\n| 2 | Days 40, 60 |')
        text = text.replace('| Day 10 | A | one |', '| Day 10 | A | one |\n| Days 40, 60 | B | two |')
        self.assertEqual(gate.audit(text), [])

    def test_a_day_named_in_prose_is_not_an_anchor(self):
        """`for 1,778 cycles` and `by Day 157 of the last iteration` are prose, not headings."""
        text = doc('Day 10 — A', 'Day 40 — B').replace('prose.', 'since Day 103 this held, by Day 157.')
        self.assertEqual(gate.audit(text), [])

    def test_a_missing_appendix_fails(self):
        issues = gate.audit('### Day 10 — A\n\nprose.\n')
        self.assertTrue(any('no Appendix' in why for why, _ in issues), issues)

    def test_a_missing_spine_fails(self):
        text = doc('Day 10 — A').replace('### Chronological spine', '### Something else')
        issues = gate.audit(text)
        self.assertTrue(any('Chronological spine' in why for why, _ in issues), issues)


class TheArchive(unittest.TestCase):
    """The measurement, not a fixture."""

    def test_all_nine_read_in_order(self):
        bad = {}
        for path in gate.files():
            issues = gate.audit(gate.read(path))
            if issues:
                bad[path] = issues
        self.assertEqual(bad, {})


if __name__ == '__main__':
    unittest.main()
