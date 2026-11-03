#!/usr/bin/env python3
"""Batch-149 rewrite: replace 66 slot-template lines in 29 dossiers with facts
already recorded in the same file. Every replacement line below is drawn from a
figure or observation that appears elsewhere in that dossier; nothing new is
asserted about the world.

Run with --dry-run to list, without --dry-run to write.
"""
import re
import sys

NEW = {
 'SE-C-IVδ-907': {
  'element-register-bullet': "- Warm to the back of a hand at thirty-four degrees, on a corridor where every other wall reads cold; the difference is the first thing the watch has used to tell one run of brick from the next.",
  'form-unmistakable': "- It breathes nine times a minute, and the rate has never matched the respiration of anybody standing in the corridor.",
  'first-catalogued': "- The span has been read by eye once a shift and continuously by sensor since it was identified, which is where the 188 breathing cycles on file come from.",
  'structural-uniqueness': "- Four runs of damaged brick stand on this floor and only one of them is warm; the exclusion covers the span and leaves the other three in the maintenance schedule.",
  'register-feels-different': "- The work is a count rather than a repair: two observers on opposite sides of the painted line for ten minutes, the wall's rate and the observer's entered as two series and never reconciled.",
 },
 'SE-C-IVδ-922': {
  'element-register-bullet': "- Fog to the eye and to the hand, and nothing to any instrument: no particulate load, no temperature differential, no humidity change outside the corridor's ordinary range.",
  'form-unmistakable': "- Ask what the grief is about and the answer is a name, a house, a funeral — and the details belong to somebody the weeping person has never met.",
  'first-catalogued': "- Of 527 logged arrivals, none has been shortened by anything anybody did; the mean dwell of two minutes fifty seconds has not moved in seventeen years.",
  'structural-uniqueness': "- It is not held in a vessel. It occupies a volume and is identified by the grief of the people standing in it, so there is nothing to break and nothing to extract.",
  'register-feels-different': "- It has stood at 60 per cent once, for eleven days, and returned to 40 when the pipe route was grouted — the only movement of that figure on record.",
 },
 'SE-C-IVδ-923': {
  'element-register-bullet': "- Nothing hangs in the air to be seen. The anomaly is read from the ground, by what the people standing beneath it begin to do.",
  'form-unmistakable': "- The anger has no target at first and then has exactly one: whoever is standing nearest, every time, across 63 incidents.",
  'first-catalogued': "- Across those 63 incidents the response that closed them was the same: open the distance. The nearest colleague is named in the record on all 63.",
  'structural-uniqueness': "- The footprint widens while the anomaly itself does not move. The Y4244 widening took the gauge to 70 per cent in nine days, and it fell back to 40 within a shift of the line being re-marked.",
  'register-feels-different': "- A worker who has stopped shouting and has not been answered is the file's definition of resolved. The ground stays marked; the anomaly stays overhead.",
 },
 'SE-C-Vω-925': {
  'element-register-bullet': "- Weight with nothing to look at: the Mass is read off a load gauge that runs out of family with every gauge near it, in a place where nothing has been moved.",
  'form-unmistakable': "- Beneath it, anything — a person, a stone, a held breath — doubles, then triples, then stops being bearable.",
  'first-catalogued': "- The ledger records no event ended by anything the facility did. The holding is filed uncontained, and its gauge is a survey figure rather than a containment figure.",
  'structural-uniqueness': "- Only the Director has entered and returned, and the file names no second person. The crushed wards event, its only reading above 80 per cent, was taken after the floors had already gone.",
  'register-feels-different': "- Three evacuations were found unnecessary afterwards: the gauge falls when the survey is current, not when anything is done to the Mass.",
 },
 'SE-N-IIIγ-917': {
  'element-register-bullet': "- The light is ordinary. What is not is that no shutter opens anywhere in the zone, and the district stays silent while the sky goes from grey to full morning.",
  'form-unmistakable': "- The sleepers are aware. They report knowing that morning had come and being unable to open their eyes, which is the only account the watch has taken from inside.",
  'first-catalogued': "- The file measures the wait from sunrise: mean seventy-one minutes, shortest forty, longest a hundred and ten, across the episodes on record.",
  'structural-uniqueness': "- The gauge has stood at 70 per cent since the third widening and has not moved in nine years.",
  'register-feels-different': "- Resolution is the district opening its eyes. It is called by the morning, not by anything the watch does.",
 },
 'SE-N-IVδ-927': {
  'element-register-bullet': "- The sleeper is asleep where they stood: breathing normally, not in distress, and not woken by anything that is done to them.",
  'form-unmistakable': "- The dream is the same for everyone in the chain — a city that is not Somnarak, a sky that is not this sky, and a sound that gets closer.",
  'first-catalogued': "- Transmission is by touch. The largest chain on record is six, in Year 4,232, before the rule; every chain since has been one.",
  'structural-uniqueness': "- Resolution is a timekeeping exercise: the sleeper wakes on their own, and the cordon is lifted by the person who set it.",
  'register-feels-different': "- Work on this holding is the separate account taken on waking, which is the only content the file has ever had from inside the dream.",
 },
 'SE-C-IVδ-909': {
  'element-register-bullet': "- Dressed stone, dry, unlit except by what is carried in, and inscriptions that alter while they are being read.",
  'first-catalogued': "- The surveyed portion is 41 rooms of a structure whose plan has never been completed, and the yield has not changed as that survey has grown.",
  'structural-uniqueness': "- 188 descents are on file. The two counts have matched in 179 of them, and the nine that did not are the nine pulls.",
  'register-feels-different': "- Three charts of the interior are consistent with one another and disagree beyond the first chamber. The file keeps all three rather than choosing.",
 },
 'SE-N-IIIγ-929': {
  'element-register-bullet': "- There is no figure, no sound and no cold spot. The anomaly registers on the barometer and on the people standing under it.",
  'form-unmistakable': "- The dead arrive as pressure rather than as apparition — the sensation of being leaned on by somebody who is not there.",
  'first-catalogued': "- Across 2,206 entries the Warden's form asks which direction the lean came from, and the answer has never been uniform or stable. The file prints the distribution without interpreting it.",
  'structural-uniqueness': "- Two rooms have been taken in seventeen years, and the reading has never gone above 60 per cent.",
 },
 'SE-N-IIβ-903': {
  'element-register-bullet': "- The surface moves continuously, like water under a light wind, and has never once been still.",
  'first-catalogued': "- 211 channels are on file, and closing one ends it within the second in every one of them.",
  'structural-uniqueness': "- It does not show the room. It shows corridors of buildings that were demolished and faces of people who have been Fractured; naming a place or a face is the oldest prohibition in the file.",
  'register-feels-different': "- The watch runs to a ninety-second clock, and what is entered is the category of the place — never its name.",
 },
 'SE-O-IIIγ-920': {
  'element-register-bullet': "- The hour arrives already narrating. Watchers agree on the shape of it within ten minutes of the opening, which no ordinary time sorrow does.",
  'first-catalogued': "- Its opening sentence has never come from the same room twice, and the register of stories currently stands at 74.",
 },
 'SE-O-IIβ-911': {
  'element-register-bullet': "- A single moment held in the air of a bay: a soldier mid-scream, a table overturned, a light shattered — and it runs again every forty-seven minutes.",
  'first-catalogued': "- The bay has been worked 611 times and the figure has never varied by more than a point, which the wing attributes to the loop being identical every time.",
 },
 'SE-O-IIβ-914': {
  'element-register-bullet': "- The minute is identified by the clocks: it opens between 1159 and 1200 by three instruments that do not otherwise agree with one another.",
  'form-unmistakable': "- The boundary is marked and it holds. The rack bolted at the two-hundred-metre line has not moved in eleven years.",
  'first-catalogued': "- The series holds 61 occurrences in eleven years, and nobody has worked this holding from inside since Year 4,228.",
 },
 'SE-O-IVδ-930': {
  'element-register-bullet': "- The manifestation is physical: a tale about a wolf leaves claw marks on the nearest tree, and a ghost story drops the temperature by ten degrees.",
  'first-catalogued': "- 61 silent cycles have closed the sector the documented way; the four that did not are in the utterance log with a teller's name against each.",
 },
 'SE-C-IIIγ-902': {
  'first-catalogued': "- The wing holds two other carved hands and neither of them beats, which is how the designation is confirmed before any contact.",
 },
 'SE-C-IIIγ-904': {
  'first-catalogued': "- Two people work the chamber and never one, and the gauge falls 10 per cent for each altered result traced back to its source and corrected there.",
 },
 'SE-C-IIIγ-912': {
  'first-catalogued': "- Containment here is notification: the district is told, personnel are held in place, the hour is recorded, and work resumes at 0400.",
 },
 'SE-C-IIIγ-913': {
  'first-catalogued': "- Nothing shortens an occurrence. The holding is watched from a measuring network rather than a post, and the readings are taken at the fixed points.",
 },
 'SE-C-IIIγ-921': {
  'first-catalogued': "- Three minutes of standing is the threshold: the cracks start hairline and painless and deepen from there, and the site itself is ordinary ground.",
 },
 'SE-C-IIIγ-928': {
  'first-catalogued': "- The register separates mind from body by what the gas does: first misplaced words, then reversed meanings, then the loss of the line between memory and imagination.",
 },
 'SE-C-IIβ-901': {
  'first-catalogued': "- The organ is unambiguously a person's — the record names whose — and 188 cycles are on file: the handler's pulse matched the door reading in 147 of them, and the 41 misses are the file.",
 },
 'SE-C-IIβ-906': {
  'first-catalogued': "- 411 cycles and 411 closed covers: the page count has only ever gone up, and the reader named the handwriting correctly in 188 of them.",
 },
 'SE-C-Iα-900': {
  'first-catalogued': "- 309 tales have been read off its body in nineteen years, and 11 of them exist in no other record anywhere in Somnarak.",
 },
 'SE-N-IIIγ-908': {
  'element-register-bullet': "- Walls shift and doors open onto rooms that are on no plan, which is why the work is a survey and not a containment.",
 },
 'SE-N-IIβ-910': {
  'first-catalogued': "- The hall seats forty-four, and at dusk the seats fill in the order of precedence recorded on the hall plan and empty in the same order.",
 },
 'SE-N-IIβ-919': {
  'first-catalogued': "- The dead speak to each other rather than to the living, and the two transcripts are filed side by side without being reconciled.",
 },
 'SE-O-IIIγ-916': {
  'element-register-bullet': "- The hour ends at sixty minutes from the first walker, in all thirty-four occurrences on file, and the column is gone when it does.",
 },
 'SE-O-IIIγ-924': {
  'element-register-bullet': "- The boundary is a measurement: the fifty-metre radius is checked each year against its markers to within half a metre.",
 },
 'SE-C-IVδ-915': {
  'element-register-bullet': "- The only physical trace it leaves is tool wear: hammers and files worn disproportionately to the hours on the log, on a shop floor that otherwise looks like the district's own.",
 },
 'SE-C-IVδ-918': {
  'element-register-bullet': "- 211 cycles are on file and the question put to the interval has worked in 202 of them; the nine failures were all workers past twenty passes.",
 },
}

PATTERNS = [
    ('element-register-bullet', re.compile(r'Expresses \w+ pressure in an? \w+ register\b')),
    ('form-unmistakable', re.compile(r'form is unmistakable\b')),
    ('first-catalogued', re.compile(r'\bOne of the first catalogued\b')),
    ('structural-uniqueness', re.compile(r'descriptor makes it structurally unique\b')),
    ('register-feels-different', re.compile(r'register feels (?:different from|unlike) standard \w+')),
]


def main(dry):
    import glob
    import io
    files = sorted(set(glob.glob('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md', recursive=True)
                       + glob.glob('SOMNARAK-WORLD/Unknown_Entities/*.md')))
    total = 0
    touched = 0
    for path in files:
        key = None
        for k in NEW:
            if k in path:
                key = k
                break
        if not key:
            continue
        text = io.open(path, encoding='utf-8').read()
        lines = text.split('\n')
        out = []
        n = 0
        for line in lines:
            fam = None
            for name, pat in PATTERNS:
                if pat.search(line):
                    fam = name
                    break
            if fam is None:
                out.append(line)
                continue
            if fam not in NEW[key]:
                print(f'  UNMAPPED {path.split("/")[-1]} :: {fam} :: {line[:80]}')
                out.append(line)
                continue
            out.append(NEW[key][fam])
            n += 1
        if n:
            touched += 1
            total += n
            print(f'  {n:2d}  {path.split("/")[-1]}')
            if not dry:
                io.open(path, 'w', encoding='utf-8').write('\n'.join(out))
    print(f'{"would replace" if dry else "replaced"} {total} lines in {touched} files')
    return 0


if __name__ == '__main__':
    sys.exit(main('--dry-run' in sys.argv))
