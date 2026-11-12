# -*- coding: utf-8 -*-
"""Gate 56 — the stamp (§ IV.6)."""
import io
import os
import tempfile
import unittest

from tools.auditors import check_scene_stamps as gate


def write(text):
    fd, path = tempfile.mkstemp(suffix='.md')
    os.close(fd)
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    return path


GOOD = '''# Echo-Core 9 — Test

## Prologue Record — The Bench

---

> **STAMP — 9 days before [REDACTED] happened · 17:40 · Floor 3, the bench**

There was a lamp.

### The Warm Floor

> **STAMP — 00:00 to 23:41, the day of the Solidification. The redaction lifts here · 23:24 · Floor 3**

The floor warmed.
'''


class TheStamp(unittest.TestCase):
    def test_a_stamped_file_passes(self):
        self.assertEqual(gate.check_file(write(GOOD)), [])

    def test_a_scene_without_a_stamp_fails(self):
        bad = GOOD.replace('> **STAMP — 9 days before [REDACTED] happened · 17:40 · Floor 3, the bench**\n\n', '')
        issues = gate.check_file(write(bad))
        self.assertTrue(any('carries no STAMP' in i for i in issues), issues)

    def test_an_offset_without_a_unit_fails(self):
        bad = GOOD.replace('9 days before [REDACTED] happened', 'before [REDACTED] happened')
        issues = gate.check_file(write(bad))
        self.assertTrue(any('names no unit' in i for i in issues), issues)

    def test_a_stamp_without_a_clock_fails(self):
        bad = GOOD.replace('· 17:40 ·', '· ·')
        issues = gate.check_file(write(bad))
        self.assertTrue(any('no clock' in i for i in issues), issues)

    def test_a_stamp_without_a_place_fails(self):
        bad = GOOD.replace('· Floor 3, the bench**', '**')
        issues = gate.check_file(write(bad))
        self.assertTrue(any('no place' in i or 'offset · clock · place' in i for i in issues), issues)

    def test_the_redaction_may_not_outlive_its_lift(self):
        bad = GOOD + '''
### The Filing

> **STAMP — 14 days before [REDACTED] happened · 09:15 · the register office**

She stamped it.
'''
        issues = gate.check_file(write(bad))
        self.assertTrue(any('still counts toward [REDACTED]' in i for i in issues), issues)

    def test_the_lift_is_stamped_from_midnight(self):
        bad = GOOD.replace('00:00 to 23:41, the day of the Solidification. The redaction lifts here · 23:24',
                           '23:24 to 23:41, the day of the Solidification. The redaction lifts here · 23:24')
        issues = gate.check_file(write(bad))
        self.assertTrue(any('not stamped from 00:00' in i for i in issues), issues)

    def test_years_months_days_hours_and_minutes_are_all_units(self):
        for unit in ('years', 'months', 'days', 'hours', 'minutes'):
            text = GOOD.replace('9 days before', '9 %s before' % unit)
            self.assertEqual(gate.check_file(write(text)), [], unit)


class TheArchive(unittest.TestCase):
    def test_majin_is_stamped(self):
        path = os.path.join(gate.DIR, '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md')
        self.assertEqual(gate.check_file(path), [])

    def test_majin_lifts_the_redaction_once(self):
        path = os.path.join(gate.DIR, '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md')
        text = gate.read(path)
        self.assertEqual(text.count('The redaction lifts here'), 1)

    def test_majin_uses_the_bracket_before_the_lift_only(self):
        path = os.path.join(gate.DIR, '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md')
        text = gate.read(path)
        lift = text.index('The redaction lifts here')
        self.assertIn('[REDACTED]', text[:lift])
        self.assertNotIn('[REDACTED]', text[lift:])


if __name__ == '__main__':
    unittest.main()
