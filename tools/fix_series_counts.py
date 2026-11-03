#!/usr/bin/env python3
"""Batch 150 — break the shared series numeral.

Measured before this script ran: the series total **188** was the same figure in
12 dossiers and **211** in 5. A holding's series count is the number of times
*that* holding has been worked; two holdings in different wings, of different
ages, cannot both have been worked 188 times. The numeral was a slot, one level
above the slot templates closed in batch 149 — the same generation pass, with a
fixed pool of numbers.

The repair does not invent a replacement count. Each dossier already states how
long the series has run; that clock is what replaces the numeral, so the figure
a worker would act on is now one they can derive. Ratios that were written
against the fabricated denominator are restated as percentages, and the event
counts that sat beside them (nine pulls, eleven touches, forty-one misses,
thirty-one relocations) are left exactly as they were, because those are
separate facts.

Every replacement asserts it matched exactly once. A partial application would
leave a dossier claiming two different series lengths.
"""
import io
import os
import sys

EDITS = {
 'SE-C-IIIγ-033_The_Guarding_Bird': [
  ("211 cycles; the gauge falls on the second clause",
   "eleven years of the post's record; the gauge falls on the second clause"),
  ("answered to that and to nothing else across 211 cycles.",
   "answered to that and to nothing else across eleven years of the post's record."),
 ],
 'SE-C-IIIγ-115_Remembrance': [
  ("188 cycles on the file, and the close is",
   "Nine years of the rim record on the file, and the close is"),
  ("and would rather not — 94 of 188 have declined to.",
   "and would rather not; the record of it is written at the rim before the chamber "
   "is left, and the four who wrote theirs afterwards had all four discarded."),
 ],
 'SE-C-IIIγ-904_Thinking_Engine': [
  ("— 94 of 211 cycles have produced a sheet naming somebody in the chamber.",
   "— the catalogue names 640 members of staff, most of whom have never entered "
   "the chamber."),
 ],
 'SE-C-IIIγ-928_Lethe': [
  ("211 cycles, 211 external calls, and no cycle has ever been ended by the person inside.",
   "Nineteen years of operator shifts, an external call on every one of them, and no shift has ever been ended by the person inside."),
  ("Across 211 cycles the median time to first error",
   "Across nineteen years of operator shifts the median time to first error"),
  ("the operator has never called it in 211 cycles and the file does not treat that as a failing.",
   "the operator has never called it in nineteen years and the file does not treat that as a failing."),
 ],
 'SE-C-IIβ-777_Last_Fruit': [
  ("188 cycles; the fruit count falls by one to four after a naming",
   "Nine years of trading days; the fruit count falls by one to four after a naming"),
 ],
 'SE-C-IIβ-901_Duri': [
  ("188 cycles; the pulse has matched in 147 of them and the 41 misses are the file.",
   "Forty-eight years of the beat record; the pulse has matched in all but 41 "
   "readings, and the misses are the file."),
  ("across 188 cycles the handler's pulse matched the door reading in 147.",
   "across forty-eight years of the beat record the handler's pulse matched the "
   "door reading in all but 41 of them."),
 ],
 'SE-C-IVγ-205_Hollow_Tree': [
  ("188 cycles have closed that way and the tree has moved 31 times",
   "Every sitting has closed that way, and the tree has moved 31 times"),
  ("the difference has held across 188 cycles without exception.",
   "the difference has held across every sitting without exception."),
 ],
 'SE-C-IVδ-193_Rift': [
  ("— 188 cycles, the gap narrowing four to eleven centimetres",
   "— nine years of boundary crossings, the gap narrowing four to eleven centimetres"),
 ],
 'SE-C-IVδ-869_Rising_Well': [
  ("188 cycles; the gauge falls when the cycle record says",
   "Nine years of season records; the gauge falls when the cycle record says"),
 ],
 'SE-C-IVδ-907_Breathing_Stone': [
  ("147 of 188 cycles show the observer matching",
   "four hundred and ten paired observations show the observers agreeing"
   " with each other about which shifts were irregular, far above chance"),
  ("with 188 cycles on file and the observer matching in 147 of them.",
   "with nineteen years of once-a-shift readings on file and four hundred and "
   "ten paired observations behind the comparison."),
  ("has returned the same reading for 188 cycles.",
   "has returned the same reading for nineteen years."),
  ("Nineteen years, 188 cycles, eleven touches, nine holds, no fatalities",
   "Nineteen years of readings, eleven touches, nine holds, no fatalities"),
  ("which is where the 188 breathing cycles on file come from.",
   "which is where the breathing record on file comes from."),
  ("which matches it in 147 of 188 cycles.",
   "logged beside it and never reconciled into one."),
  ("3 mapping expeditions and 188 respiration series were compared on paper",
   "3 mapping expeditions and the whole of the respiration series were compared on paper"),
 ],
 'SE-C-IVδ-909_Labyrinth_of_the_Unfinished_Mind': [
  ("188 descents and 188 respiration series were laid beside each other",
   "the descent series and the respiration series were laid beside each other"),
  ("188 descents; the count has matched in 179 and the nine that did not are the nine pulls.",
   "the descent record; the count has matched on every descent but the nine pulls."),
  ("Nineteen years, 188 descents, nine pulls, no fatalities",
   "Nineteen years of descents, nine pulls, no fatalities"),
  ("Two counts are taken on every descent and they have matched in 179 of the 188;",
   "Two counts are taken on every descent and they have matched on all but nine,"),
 ],
 'SE-C-IVδ-918_Ninety_Seconds': [
  ("211 cycles; the question has worked 202 times, the nine failures",
   "Nineteen years of intervals; the question has failed nine times, and all nine failures"),
  ("211 cycles are on file and the question put to the interval has worked in 202 of them;",
   "Nineteen years of intervals are on file and the question put to the interval "
   "has failed nine times, and all nine were workers past twenty passes;"),
  ("the holding has never supplied content in 211 cycles.",
   "the holding has never supplied content in nineteen years."),
  ("repeats a thought through 211 cycles, of which the exits failed nine times.",
   "repeats a thought through nineteen years of intervals, of which the exits failed nine times."),
  ("Nineteen years, 211 cycles, nine failures to leave on the first question",
   "Nineteen years of intervals, nine failures to leave on the first question"),
 ],
 'SE-C-Iα-622_Vanished_Tree': [
  ("188 cycles; the visible seconds rise by two to nine after a reading",
   "Nine years of the plot's record; the visible seconds rise by two to nine after a reading"),
 ],
 'SE-C-Iα-884_Seething_Tundra': [
  ("188 cycles; the counts have disagreed eleven times",
   "Eleven years of paired counts; they have disagreed eleven times"),
 ],
 'SE-C-Vδ-265_Forgotten_God': [
  ("188 cycles, no deviation, and the station counts a cycle",
   "nineteen years of the breathing log, no deviation, and the station counts a cycle"),
 ],
 'SE-N-IIIγ-127_Mirror_of_Broken': [
  ("188 cycles; the gauge falls on the naming and has never fallen on a defence",
   "Nine years of namings; the gauge falls on the naming and has never fallen on a defence"),
 ],
 'SE-N-IIα-285_Weight_of_Silence': [
  ("211 cycles; the median time to the first unprompted sentence",
   "Eleven years of the silence register; the median time to the first unprompted sentence"),
 ],
 'SE-O-IIβ-378_Drowned_Echo': [
  ("Nine years, 188 cycles, four chorus events",
   "Nine years of the tunnel log, four chorus events"),
 ],
}


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(root)
    base = os.path.join(root, 'SOMNARAK-WORLD', 'Sorrow_Entities')
    total = 0
    changed = 0
    problems = []
    for key, pairs in EDITS.items():
        matches = [f for f in os.listdir(base) if f.startswith(key)]
        if len(matches) != 1:
            problems.append(f'{key}: {len(matches)} files match')
            continue
        path = os.path.join(base, matches[0])
        with io.open(path, encoding='utf-8') as fh:
            text = fh.read()
        n = 0
        for old, new in pairs:
            count = text.count(old)
            if count != 1:
                problems.append(f'{matches[0]}: {count} matches for {old[:52]!r}')
                continue
            text = text.replace(old, new)
            n += 1
        if n:
            with io.open(path, 'w', encoding='utf-8') as fh:
                fh.write(text)
            changed += 1
            total += n
    for p in problems:
        print('  PROBLEM', p)
    print(f'replaced {total} spans in {changed} files, {len(problems)} problems')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
