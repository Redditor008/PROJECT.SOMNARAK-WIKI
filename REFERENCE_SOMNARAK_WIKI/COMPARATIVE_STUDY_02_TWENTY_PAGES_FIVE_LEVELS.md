# Comparative Study 02 — Twenty Pages, Five Levels, Ten Pairings

**Subjects:** ten dossiers, chosen by a rule fixed before reading (§1.5), and all 302 dossiers by rank (`tools/ladder.py`)
**Benchmarks:** twenty pages of the Lobotomy Corporation Wiki (wiki.gg), four at each risk level from ZAYIN to ALEPH; three of them re-read on the Fandom host; the five level pages and the Risk Level page
**Written:** Year 4,237 / 2026-10-05 · **Status:** reference, not canon · **Rules in play:** `R-06`, `R-19`, `R-23`, `R-24`, `R-27`, `R-28`, `R-29`
**Tests:** `COMPARATIVE_STUDY_01_VELLUM_MAN_AND_BROKEN_DOOR.md` and the standard `R-29` collected from it

---

## 0. Why this study exists

Study 01 set two of our dossiers against two benchmark pages, one WAW and one ZAYIN. Five findings came out of it, and `R-29` collected them into the standard every
dossier is now measured against. The weakness was pointed out by the archive owner: one comparison cannot
show what changes *between* levels, and a whole standard rests on it. Five to ten comparisons are worth far
more than one.

So nothing here is concluded from fewer than twenty pages. The order of work was: read the pages first, find
what the wiki does at each level, measure the same things across every dossier, and only then set our
dossiers against the pages, ten times. Study 01's conclusions are tested at the end (§8), not assumed.

---

## 1. Method, and what it cannot show

### 1.1 The sample

Twenty pages, four per level, taken from the wiki's own level lists. Standard pages vary by origin letter
(F, T, O) and by whether a Qliphoth counter exists; one tool page sits at each of the four levels that
carry tools in the sample. No ALEPH tool page was sampled.

| Level | Pages |
|---|---|
| ZAYIN | One Sin and Hundreds of Good Deeds · Fairy Festival · Plague Doctor · Old Faith and Promise (tool) |
| TETH | Scorched Girl · Fragment of the Universe · Grave of Cherry Blossoms · Behavior Adjustment (tool) |
| HE | Happy Teddy Bear · Nameless Fetus · Der Freischütz · Notes from a Crazed Researcher (tool) |
| WAW | The Burrowing Heaven · The Queen of Hatred · Big Bird · Express Train to Hell (tool) |
| ALEPH | Nothing There · WhiteNight · Blue Star · Mountain of Smiling Bodies |

### 1.2 How far each page was read

The fetch tool returns a page in chunks of about seven thousand characters. For every page the first chunk was
read: contents list, lead sentence, Appearance, Ability, Details, the observation-level box, basic info and
work preferences. Tool pages fit in one to two chunks and were read whole. A second chunk was read for five
standard pages (One Sin, Fairy Festival, Plague Doctor, Scorched Girl, Mountain of Smiling Bodies), which
brought their management tips, escape box, equipment and Story into view. **Statements about the Story,
Flavor Text and Trivia sections of the other fifteen pages rest on the contents list alone.** Where a figure
below is marked "(list)" it comes from the level page, not the article.

### 1.3 Two hosts

The five level pages and the Risk Level page are wiki.gg; they are the wiki's own statement of what a level
means, and they are used throughout. Scorched Girl, One Sin and Nameless Fetus were re-read on the Fandom
host. Library of Ruina and Limbus Company pages were not sampled: their abnormality pages describe different
mechanics (Realisation fights, identities), so "the Abnormality wiki" is read here as both hosts of the
Lobotomy Corporation wiki, the one the repository already cites as primary.

### 1.4 Limits

Both wikis are volunteer-written and uneven: one of twenty pages carries a Strategy section, and the same
number is quoted as 2.0 on one page and 20 on another. Page size is measured in fetch chunks, which include a
navigation template, so it is a proxy. Nothing here was checked in play.

### 1.5 Our side

The ten dossiers were chosen by a rule fixed before any was opened. For the tool pairings: the lowest-numbered
single-use relic (A-Relic) at the level, and the lowest-numbered equippable relic (I-Relic) at the level.
For the standard pairings: the lowest-numbered Subject at each rank, two at Rank V because that is where the
wiki's pages are largest and the archive's holdings fewest. Rank I to V is read against ZAYIN to ALEPH, the
mapping the conversion guide already uses. Every figure about the archive as a whole comes from
`python3 tools/ladder.py`, which regenerates §6.

---

## 2. The twenty

"Leaves the cell" is whether the page says the entity can get out. "Figures" are the numbers the page gives
for what happens when the trigger fires.

| Level | Page (code) | Kind | What moves it, as the page states it | Leaves the cell | Figures given for the event | Lead-sentence tags |
|---|---|---|---|---|---|---|
| ZAYIN | One Sin and Hundreds of Good Deeds (O-03-03) | standard | no counter | no | heals 4 SP; all of the department at 10 boxes | none |
| ZAYIN | Fairy Festival (F-04-83) | standard | no counter; a worker under its care assigned elsewhere | no | heals 10% max HP a second for 8 s, then death | instadeath; benefit |
| ZAYIN | Plague Doctor (O-01-45) | standard | counter 1: a Good or Bad result; Emergency Level 2 | no | 12 blessings, then it becomes WhiteNight | possession; alterations; benefit |
| ZAYIN | Old Faith and Promise (T-09-97) | tool, single use | none; a bet | no | odds 85% to 25%; cost 2% to 12% of energy | benefit |
| TETH | Scorched Girl (F-01-02) | standard | counter 2: Normal 50%, Bad 70% | yes | 120 HP; 300 RED; 4.5 to 5.5 s | escape |
| TETH | Fragment of the Universe (O-03-60) | standard | counter 2: Normal 50%, Bad 70%, a worker panics | yes | 230 HP; BLACK 2 to 4; sings WHITE 2 to 4 | escape |
| TETH | Grave of Cherry Blossoms (O-04-100) | standard | counter 3: a Good result, a panic | no, it lures about 5 workers | 15 to 18 WHITE to the released | instadeath; possession; benefit |
| TETH | Behavior Adjustment (O-09-96) | tool, equippable | no counter; 30 s; SP at 0 | no | +15 speeds; −10 SP | instadeath; benefit |
| HE | Happy Teddy Bear (T-04-06) | standard | no counter: the same worker twice running | no | one worker; a work is burned | instadeath |
| HE | Nameless Fetus (O-01-15) | standard | counter 1: Normal 30%, Bad 90% | no | 8 to 12 WHITE every 10 s to the department | instadeath; possession; alterations |
| HE | Der Freischütz (F-01-69) | standard | counter 3: a worker under Justice 3; Normal or Bad, 100% | no | BLACK 80 across the screen | benefit |
| HE | Notes from a Crazed Researcher (T-09-78) | tool, equippable | no counter; 30 s; no work; 60 damage | no | +20 success; explosion 30 RED | instadeath; benefit |
| WAW | The Burrowing Heaven (O-04-72) | standard | counter: time off screen; +1 Normal, +2 Good | yes | 800 HP; 150 BLACK | instadeath; escape |
| WAW | The Queen of Hatred (O-01-04) | standard | counter 2: Bad; fewer than 3 deaths per Meltdown | yes, two modes | 1,200 HP in the passive mode | escape; benefit |
| WAW | Big Bird (O-02-40) | standard | counter 5: Good +1, Bad −1, every 5 deaths; Emergency Level 2 | yes | 1,600 HP; marks every ~20 s | instadeath; escape; possession; alteration |
| WAW | Express Train to Hell (T-09-86) | tool, single use | none; four lamps, one per 30 s | the train crosses | 40 / 80 / 50 / 50 healed; 100 BLACK | alteration; healing |
| ALEPH | Nothing There (O-06-20) | standard | counter 1: two skins taken; a worker of Justice 3 or lower | yes, three forms | 2,000 HP in the first form; 10,000 RED answers | instadeath; escape; possession |
| ALEPH | WhiteNight (T-03-46) | standard | counter 0, or the transformation | yes | 12,000 HP; 12 apostles of 1,000 HP | none (second form of Plague Doctor) |
| ALEPH | Blue Star (O-03-93) | standard | counter 2: Prudence under 5; a work past 60 s | yes, immobile | 2,200 HP; 15 to 20 WHITE every 5 to 8 s, facility-wide | instadeath; escape |
| ALEPH | Mountain of Smiling Bodies (T-01-75) | standard | counter 2: an injured entrant; a death in the unit; Bad; 10 deaths in the facility | yes | 500 HP, doubling twice | escape |

---

## 3. What does not change with level

**The frame.** On wiki.gg every standard page has the same ten items: Appearance, Ability, Details, E.G.O
Equipment (Weapon, Suit, Gift), Story, Flavor Text, Gallery, Trivia, External links, Navigation. ZAYIN, TETH,
HE, WAW and ALEPH pages share it. Five pages add a section or subsections of their own (Plague Doctor's
Blessings and Bugs, the Queen of Hatred's Passive and Hostile Breach, Nothing There's three modes,
WhiteNight's Twelve Apostles, Mountain's Strategy) and one drops External links. Tool pages share a shorter one (Appearance, Ability, Log and Method, then
Gallery and Navigation, with Bugs or Trivia on some) and none carries equipment, Story or Flavor Text. The
boxes are identical too: an observation-level ladder (I to IV), basic info with outcome ranges, a work
preference matrix, management tips, escape information. The Fandom host has a different but equally constant
frame: Ability, Origin, Details, Story, Flavour Text, Trivia, Gallery, plus three category tags on every page
read (risk level, shape, origin).

**The connective sentences.** "… responds to the four works in order of best to worst" appears on every
standard page whose Details section was in the text read (12 of 16, one with "work types" for "works"). "… ability will trigger when its
Qliphoth Counter reaches 0. Its Qliphoth Counter can fluctuate in the following ways" opens the Ability on
eight pages. The wiki repeats its furniture and keeps the numbers bespoke. That is the rule `R-23` already
states, and the survey supports it.

**The consequence for parity.** Do not vary the nine `R-29` parity sections by rank. The frame is the one thing
the wiki holds constant.

---

## 4. What does change: the ladder

The wiki says so itself. The level pages and the Risk Level page state, in the wiki's own words, what each
level means, and the figures on the pages follow it.

| | ZAYIN | TETH | HE | WAW | ALEPH |
|---|---|---|---|---|---|
| The Manual (list) | "little to no aggression … may have a positive effect" | "varying degrees of injury … as long as your employees follow the proper managerial guidelines" | "can easily kill a number of employees … twice as much attention" | "high risk and carry devastating force … the death toll could reach into the dozens" | "the most dangerous" |
| Can leave the cell | none can (list) | yes; one target or one room in the sample | some; many act in the cell (sample) | all have a way to breach, summon or possess (list) | all; a Game Over is possible (list) |
| Penalty if breaching at day end (list) | none | −1 LOB point | −3 | −5 | all LOB points |
| Appears from (list) | no limit stated | no limit stated | day 7 | day 13 | a slim chance on day 13; day 18 on |
| Work penalty (list) | none | none | none | −4% a work, to −32% | −6% a work, to −30% |
| Price of basic info, PE boxes | 8 | 12 | 16 | 20 | 30 |
| Max PE boxes a work | 10 | 12 | 15 to 18 | 20 to 24 | 30 to 33 |
| Lead tag naming a benefit | 3 of 4 | 2 of 4 | 2 of 4 | 2 of 4 | 0 of 4 |
| Standard pages with breach figures | 0 of 3 | 2 of 3 | 0 of 3 | 3 of 3 | 4 of 4 |
| Breach HP read | none | 120, 230 | none | 800, 1,200, 1,600 | 500 to 2,000; 2,000; 2,200; 12,000 |
| Page size, fetch chunks, standard pages | 4.7 | 5.0 | 4.7 | 5.7 | 6.5 |

The price of basic info is read on three pages at ZAYIN and HE, two at TETH, and one each at WAW (Burrowing
Heaven, 20) and ALEPH (Blue Star, 30). The ranges for max PE boxes include the level page's list.

The HE column has no breacher because the three HE standard pages sampled all act inside the cell. That is a
property of the sample, not of the level: the HE page says its members breach when the counter empties.

**The ladder is how tightly the entity is coupled to the rest of the facility.** At ZAYIN the effect stays in
the unit. At TETH it reaches one target or one room. At HE it reaches a department, or it alters another
entity's counter. At WAW the triggers are the facility's own numbers, its casualty count and its alert level,
and the page names families and cures. At ALEPH the page documents modes, formulas, several exits with a
price on each, and the scoring consequences for the institution.

---

## 5. Twelve things the pages do

Each is a practice, with the pages that show it.

1. **The hazard is a short rule with numbers.** 14 of the 16 standard pages state what triggers the event in the
   Ability section: twelve as a list of two to four conditions, one (Happy Teddy Bear) as a single staffing
   rule, one (WhiteNight) as the counter or the transformation. Nearly all carry a figure: 50% and 70%
   (Scorched Girl, Fragment), 30% and 90% (Nameless Fetus), every 5 deaths (Big Bird), 10 deaths (Mountain), a
   work past 60 s (Blue Star). The two exceptions are ZAYIN pages with no counter.
2. **The triggers are of nine kinds.** A work result (Normal, Bad or Good, sometimes with odds, sometimes
   raising the counter); a worker panicking in the unit; deaths, in the facility or in the cell; a worker's
   stat below a gate (Justice, Prudence, Temperance, Fortitude); a work's length, or time off screen; a staffing
   pattern (the same worker twice running); an alert state (Emergency Level 2); the state of the entrant (an
   injured worker); a use count (the seventh Request). Ten of 16 standard pages use a work result; eleven use
   at least one other kind.
3. **From TETH up, the breach has figures.** Health, speed or timer, damage and the end condition. ZAYIN
   pages have none because nothing leaves.
4. **The remedy has a price, stated.** A sacrificed worker drawn by roulette (Nameless Fetus); 10% of the
   facility's energy per shot (Der Freischütz); a weapon that is not granted if the cure is confession
   (WhiteNight); mission credit denied (Nothing There); a work burned (Happy Teddy Bear). The price rises with
   level: a weapon, a worker, a train through the facility, a scoring penalty.
5. **At WAW the facility's own numbers are triggers.** Casualty counts (Big Bird, Queen of Hatred, Mountain)
   and alert levels (Plague Doctor, Queen of Hatred, Big Bird).
6. **Relations are mechanics.** A family in the lead sentence (the Magical Girls; the birds of the Black
   Forest); cures by name (Big Bird's mark is removed by entering We Can Change Anything or the Shelter from
   the 27th of March; WhiteNight by the twelfth apostle confessing to One Sin); a merge event (three birds
   breaching together on day 21 call Apocalypse Bird). The relation changes a figure or an outcome.
7. **Tips stop being instructions above ZAYIN.** ZAYIN tips are statements of effect. At TETH one of three is an
   incident recap (Scorched Girl's third). At HE both of Happy Teddy Bear's are incident reports that the
   reader has to turn into a rule, and they cost 9 PE boxes each against 3 or 4 below. Obeyable management
   arrives, on one ALEPH page of the sample, as a volunteer's Strategy section: stat gates and resistance
   thresholds under Management, stage-by-stage handling under Suppression.
8. **The Story changes the kind of document, and the deepest entry carries the cost.** Scorched Girl's five:
   a description, a rumour, a researcher's log, a staff conversation, a counselling log. Fairy Festival's last:
   the fairies are carnivores and management decided not to tell the staff because the accident rate had
   fallen. One Sin's: a level-3 confession cost a subject six years of memory and the facility two hours of
   power.
9. **The page corrects its own game.** "Unlike what his Managerial Guidelines say, … a 100% chance of lowering
   if the work result isn't Good" (Der Freischütz).
10. **Names arrive with observation.** Happy Teddy Bear is "A Teddy Bear" before level 2; the Queen of Hatred
    is "Magical Girl" before level 3.
11. **Tool pages are small and numeric.** A time- or use-keyed log table beside a method table; three or four
    short conditionals; a probability or dose table; no Story.
12. **The wiki does not own its figures.** Scorched Girl's speed is 2.0 on wiki.gg and 20 on Fandom; Fragment of
    the Universe, which that page calls slow, is 20 on wiki.gg; the explosion delay is 4.5 to 5.5 s on one
    host and 5 s on the other.

The lead sentence deserves one more line. Eighteen of the twenty pages open with "capable of …" and a tag
from a closed set: instadeath, escape, possession, employee, department or facility alteration, benefit
(healing, damage, a named stat). It is a facet, not prose.

---

## 6. Our archive, by rank

`python3 tools/ladder.py`, 302 dossiers.

| Rank | n | Words | Sorrow Gauge [HP] | ATK max | Speed | Yield | Breach-capable | Event section words | Rank record words | Positive / Neutral / Negative | Meet `R-29` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| I | 46 | 6,477 | 198 | 10 | 0.95 | 10–14 | 63% | 341 | none | 2 / 41 / 3 | 8 |
| II | 71 | 6,723 | 415 | 22 | 1.45 | 12–18 | 56% | 346 | 894 | 2 / 68 / 1 | 13 |
| III | 86 | 6,880 | 653 | 34 | 1.95 | 16–22 | 52% | 309 | 1,100 | 4 / 80 / 2 | 10 |
| IV | 85 | 7,194 | 827 | 55 | 2.45 | 20–28 | 61% | 294 | 1,450 | 3 / 74 / 8 | 10 |
| V | 14 | 7,566 | 897 | 48 | 2.80 | 20–28 | 50% | 281 | 2,185 | 0 / 3 / 11 | 2 |

Medians, as of the commit that carries this study, when `R-29` stood at 43. Later dossier units move two cells and
no argument: the Rank V words and the last column (after The Stormscale Sovereign, Sorrow Tide, The Final Door,
Forgotten God, The Convergence, Wilderness Tide and the second Dawn of Mourning, Rank V reads 7,670 words and 9
meeting). "Rank record" is the section each rank adds: Watch Record at II, Warden Record at III, Apex Record at
IV, Sovereign Chronicle at V. Six readings follow from the table and its companions.

1. **Length climbs.** 6,477 to 7,566 words, monotonically. That is the ladder the archive already requires, and
   it is met.
2. **A second ladder exists and no test reads it.** The rank record grows 894, 1,100, 1,450, 2,185 words, and
   it is where the guidance a worker needs sits: the Debt Eater's Warden Record opens with a spatial standing
   order, the Grieving Maiden's Apex Record with the distance to her sisters. The wiki has no counterpart on
   most pages; its Strategy section appeared once in twenty. `R-29` does not test these sections at all.
3. **The stat line follows potency, not rank, and it flattens at the top.** Sorrow Gauge medians by potency
   are 198, 415, 653, 880, 1,200 for α to ω. Four values cover 78 of 301 dossiers (415 ×22, 910 ×20, 653 ×18,
   198 ×18). Rank V's median Sorrow Gauge (897) is barely above Rank IV's (827), its ATK median is lower
   (48 against 55), and its yield equals Rank IV's. Against the conversion guide's Rank V floor of 1,000
   (`PM_ABNORMALITY_TO_PS_SORROW_ENTITY_CONVERSION_GUIDE.md`, Section III), ten of fourteen Rank V dossiers sit
   below it. The guide's own ranges hold at Ranks I and II (40 of 46, 64 of 70) and
   weaken above (59 of 86 at III, 57 of 85 at IV, 4 of 14 at V).
4. **Breach capability does not climb.** 63%, 56%, 52%, 61%, 50% across Rank I to V. The wiki's is zero at the
   bottom and "all" at the top. `R-28` set floors by entity type (RE, SE, OP), not by rank, and the flat result
   follows. Rank I at 63% contradicts the Sorrow Entities README, which defines Rank I as "minimal cell breach
   risk", and the wiki's own ZAYIN statement that none can breach.
5. **The event section is the same size at every rank.** About 300 words, three or four figures, from Rank I
   (341 words) to Rank V (281). The wiki's event content grows with level and is absent at ZAYIN. The
   Escalation row of the event table mentions a drain of five per turn or cycle in 95 of 189 cells (50%), at
   every rank (37%, 56%, 56%, 50%, 33%). That is a shared operative value in the sense of `R-23`'s third shape.
6. **Dispositions climb only at the top.** Positive 11 of 302; Negative 11 of 14 at Rank V against 14 of 288
   below. The wiki's benefit tags fall 3, 2, 2, 2, 0 of four from ZAYIN to ALEPH, so both end at zero benefit
   at the top, and the middle of our ladder is almost entirely Neutral.

The work-response vocabulary is nearly flat as well: Decrease on 37%, 40%, 42%, 43%, 28% of the four work-type
rows from Rank I to V, Increase on 8%, 9%, 11%, 13%, 13%. The template (line 184 of
`TEMPLATES/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md`) asks for gauge changes "consistent with rank", and the wiki's
equivalent is a five-column matrix of ratings by employee level. That divergence is by design and is not
counted as a gap here.

---

## 7. Ten pairings

Each block is the same three things: what the page does, what the dossier does, and a verdict that says who is
ahead and what to take.

### P1 · ZAYIN, single-use tool · `C-Iα-114` A Letter Never Sent against *Old Faith and Promise*

**Theirs.** A seven-item page with no Story and no equipment. The Ability is a bet: a worker stakes a weapon
for a damage boost at odds from 85% down to 25%, paying 2% to 12% of the day's energy. A Bad result loses the
weapon, and "resetting the day … will not return the lost weapon".

**Ours.** 4,248 words, three banners, three M.A.W. pieces. Breaking the seal cures Panic and gives +15
Composure inside Range Band 3 for one combat phase; the cost is the letter, burnt to ash, and "a poignant
ache". There is no management line, no odds and no trial counts in the Interaction rows.

**Verdict.** Theirs ahead on the price: printed odds spend something the player owns, where ours spends the
object and prices it in feeling. Ours is ahead on the story (a father who missed the train and a daughter
waiting at the station entrance). The banner "Capable of Catastrophic Battlefield Alteration" overstates a
+15 Composure effect at Rank I, where the ZAYIN page's own lead says only "increasing the damage of an E.G.O
Weapon".

### P2 · TETH, equippable tool · `C-IIβ-051` The Happy Mask against *Behavior Adjustment*

**Theirs.** The whole page is one chunk. Equipped: +15 attack and movement speed, −10 max SP and Prudence.
Panic, or a return inside 30 seconds, and the wearer tears out their eyes, dies and sits down to laugh once.
SP at 0 while equipped also kills. The log is keyed to seconds of holding: 10, 60, 120, 180.

**Ours.** 7,514 words. Wearing "is prohibited absolutely and without exception", as the first line of the
standing order; the mask "is never equipped", and "every removal in the record was performed by a second
person". The Interaction table counts 22, 19, 29 and 21 pairings, each ending with no movement in either
gauge, and the smile has widened
2.1 mm in sixty years of gauge-card readings and never narrowed. The condition line is a recording list
("tray thermometer logged at both ends of every cycle; the room list recorded in full").

**Verdict.** Ours ahead on measured null results and a sixty-year series; no wiki page in the sample counts a
relation that did nothing. Theirs ahead on obeyability: three numeric conditions a worker can follow, where our
condition line tells the author what to log. At TETH the wiki's tool kills; ours takes expression away.

### P3 · HE, equippable tool · `C-IIIβ-015` The Debt Scale against *Notes from a Crazed Researcher*

**Theirs.** +20 to success and speed; death if returned inside 30 seconds, if no work is done, or at 60
accumulated damage, which also deals 30 RED around the wearer. The log runs from "incomprehensible cursive" to
a researcher's confessions to "Born again."

**Ours.** 7,344 words. "It displays no numerals anywhere. What it gives is weight and feeling, which is why
every figure in this file is the wing's own conversion and is recorded as such." 2,604 readings and never an
empty balance. Three relations (six, four and five co-presences) each tested against a common claim and each
null. The condition is a prohibition a worker can obey: "no measurement of any named person under any
authority".

**Verdict.** Ours ahead on saying where its figures come from, which is `R-29` clause 1 stated more cleanly
than any page of the twenty. Theirs ahead on stakes: an HE tool in the wiki kills its wearer under three stated
conditions; the Scale's risk is a burden that "may remain emotionally", with no figure.

### P4 · WAW, single-use tool · `O-IVδ-515` The Last Warmth of Forty-Two against *Express Train to Hell*

**Theirs.** Four lamps light one per 30 seconds. Use heals 40, 80, 50 to the department, 50 to the facility.
Leave all four lit for 30 seconds and a five-wagon train crosses the facility: 100 BLACK to every entity outside
a cell in its path. The Use Counter rises even at zero lamps. The log and method tables run to ten uses.

**Ours.** 5,080 words. A thrown vial puts every hostile target in Cryogenic Stasis for two combat turns (twelve
rounds), cancels boss attacks and cuts defences by 30%. The cost is the vial, 15 Composure and 72 hours of
weeping. No management line. Three relations; one keeps Cold Burn 120 m away.

**Verdict.** Theirs ahead: the WAW tool has a clock and a facility-wide downside if it is not used. Ours has a
one-off effect with a personal cost of the same kind as Rank I's. The price does not climb with rank. Ours has
the stronger origin (a crawler, forty-two voices in one bottle).

### P5 · ZAYIN, standard · `C-Iα-000` Kind Echo against *One Sin and Hundreds of Good Deeds* and *Fairy Festival*

**Theirs.** Both are harmless as observed and both hide a catch in the Story. Fairy Festival kills a
healed worker who is reassigned, and its Story says management chose not to tell the staff. One Sin's
experiment record gives +12% and +15% energy for two sin levels and, for a third, a flash after 1 minute 48
seconds and six years of memory.

**Ours.** 5,415 words, a Containment Event section ("corruption of its own zone"), a drain of 5 Composure a turn,
and the line that the entity is "docile and forgiving of errors". It is the training baseline: its Trivia says
"more aggressive than 000" is the Directorate's standard phrase for a threat. No `Management:` line.

**Verdict.** A deliberate catch-less baseline is a valid design. The wiki lists the same idea as its Standard
Training-Dummy Rabbit (0-00-00), numbered zero and listed at TETH; that page was not read. The weakness is smaller: the event table gives a drain of 5 a turn for an event the file calls
practically impossible, so the figure describes something the text says never happens. Three of the four ZAYIN
pages carry a concealed catch; a Rank I dossier should decide on purpose whether it does.

### P6 · TETH, standard · `N-IIβ-033` Forgotten Soldier against *Scorched Girl* (and *Fragment of the Universe*)

**Theirs.** The counter moves 1 at 50% on Normal and 70% on Bad; at 0 she walks, 120 HP, speed 2.0, to a
randomly marked worker and explodes after 4.5 to 5.5 seconds for 300 RED in the room; resistances by type; and a
third tip that is an incident recap.

**Ours.** 6,912 words. He walks to the nearest door that faces the abolished boundary and stands in it; four
frames in the last event, no injuries. Suppression "has been authorised twice, worked both times, and cost
eleven frames and a broken arm". The tolerated interval before the gauge crosses has gone from 31 days to 22 to
16. The condition: say "I remember you", and never because you were told to. Five relations, including the
Maw's expansion held at its edge for nine hours and the Kind Healer's null result.

**Verdict.** Ours ahead on the cost of the remedy in figures, on a trend that tells you when the next breach
is due, and on null results. Theirs ahead on a stated rule for every trigger with its odds, and on a
resistance for each damage type. Our Resistance is one percentage.

### P7 · HE, standard · `O-IIIδ-011` Scar Walker against *Nameless Fetus* and *Happy Teddy Bear*

**Theirs.** Nameless Fetus screams 8 to 12 WHITE every 10 seconds at the whole department and drains other
entities' counters; the only remedy is a worker drawn by roulette and devoured. Happy Teddy Bear kills the same
worker on the second consecutive visit, and its two tips (9 PE boxes each) are incident reports.

**Ours.** 5,733 words. The instruction is the strongest in this group: salute on arrival rather than on
departure, a named leader, and a standing order for entry. The Event table still speaks in the older voice
("Rage erupts outward, scorching resilience from all nearby"), two of three Interaction rows carry the same
stock effect sentence, and the Observation Log says it "has never breached" while the section is headed Breach
and opens "has broken free", a projection not labelled as one.

**Verdict.** Theirs ahead on a stated price per event and on cross-entity effect. Ours ahead on the instruction.
The file still fails `R-27` and `R-29`, and the contradiction between "never breached" and a breach table is
the thing to fix first.

### P8 · WAW, standard · `N-IVδ-005` The Smothering Mother against *Big Bird* (and *The Queen of Hatred*)

**Theirs.** The counter moves on Good and Bad results and falls once for every five employee deaths in the
facility; at Emergency Level 2 the department blacks out, a lamp marks the lowest-max-HP worker every 20 seconds,
clerk 40% or agent 60%; yellow marks take 0.5 and red are immune. The mark can be broken by leaving the
department, by entering We Can Change Anything (the worker still dies) or by the Shelter from the 27th of
March. The lead names the birds of the Black Forest, and a merge event can fire from day 21.

**Ours.** 7,969 words. "She holds. She has never squeezed, in four breaches"; the first target is the smallest
person on the floor, "not the nearest, and not the one whose sorrow matches hers; both alternatives have been
tested against the logs". Eleven applications to the Family Office, eleven refusals; the empty-room interval has
shortened 41, 29, 21 minutes. The one reliable suppression, the Orphaned Bell, the wing "has declined to use
routinely on the ground that it is done to her, not for her".

**Verdict.** Ours ahead on institutional cost (a refusal series and a refusal to use a working remedy) and on a
shortening series. Theirs ahead on coupling: nothing in the file ties her trigger or breach to a facility count or
an alert state. Her Escalation row carries the stock drain of five per turn.

### P9 · ALEPH, standard · `C-Vω-001` Dawn of Mourning against *WhiteNight*

**Theirs.** The observed chain. Twelve apostles of about 1,000 HP and speed 30; the player loses control of time
and the menu; a red ring in under a minute re-awakens the fallen; the first breach calls the Third Trumpet
(score 98). **Three exits, each with its price:** end the day on the energy quota; the twelfth apostle confesses
to One Sin (3,330 PALE continuously, 666 after the 0.2 resistance), and the weapon is not granted; or suppress it at
12,000 HP, and the weapon is.

**Ours.** 7,658 words. The same chain modelled: the Kind Healer's twelfth blessing completing in sorrow rather
than hope. 1,200 Sorrow Gauge, where the sibling `C-Vω-002` carries 12,000. The Interaction table has the
columns "What it is to this one" and "What is actually known", and the escalation line says the +10% figure "has
been cited back at itself as corroboration". The condition: a genuine confession before the twelfth blessing,
with "no reliable post-formation method".

*Post-study note, 2026-10-05.* The figures above are as measured on the day. The sibling `C-Vω-002` has since been retired into this file, which now carries the 12,000 Sorrow Gauge (WhiteNight's own figure, and the one the Conversion Guide gives the Dawn), 8,266 words, and a few facts taken from the retired file; the evidence is the addendum in [`SORROW_ENTITIES_PAIRS_AUDIT.md`](SORROW_ENTITIES_PAIRS_AUDIT.md).

**Verdict.** Ours ahead on labelled projection (`R-29` clause 5): no wiki page separates what a relation is from
what is known of it. Theirs ahead on exits and their prices, and on tactical figures for the retinue. A modelled
holding can still model its exits, labelled as models.

### P10 · ALEPH, standard · `C-Vδ-002` The Grieving Colossus against *Mountain of Smiling Bodies* (and *Blue Star*)

**Theirs.** Four counter conditions, including 10 deaths in the facility; growth by eating corpses, each three
adding a part and doubling max HP, with the attacks changing at two and three parts. The Strategy section sets
stat gates and a resistance floor of 0.8 or 0.7 under Management, and under Suppression a stage-by-stage plan
with a minimum of 100 HP and SP and 0.6 resistance at three parts, plus a list of which Ordeals will feed it.

**Ours.** 8,844 words. A design the wiki has no page for: permanently uncontained, a landmark that walks one
route; "Cannot be stopped. It can only be guided". The one figure the doctrine rests on is that the posts have
fifteen minutes from the junction. The only recorded harm along the route "was caused by a barricade". Four
relations with seven, six, five and three co-presences. A Sovereign Chronicle of nine sections.

**Verdict.** Ours ahead on originality, on a single instrument and on institutional cost. Theirs ahead on staged
guidance with thresholds: the Colossus has one stage (clear ahead). Four lines (three in its Registrum, one in its Escalation Notes), such as "Earlier copies
of this line recorded 4 — Mastered … the correction is made here", are `R-01` edit-meta.

### The ten at a glance

| Pair | Ours ahead on | Theirs ahead on |
|---|---|---|
| P1 | story weight | price of use (odds); level fit of the banner |
| P2 | null results; a sixty-year series | obeyable numeric conditions; stakes fitted to the level |
| P3 | disclosing where the figures come from; an obeyable prohibition | stakes fitted to the level |
| P4 | origin story | a clock and a facility-wide downside; a price that climbs |
| P5 | a deliberate baseline | the hidden catch; a log that escalates to it |
| P6 | the cost of the remedy in figures; a declining series; null results | a rule for every trigger with odds; a resistance per type |
| P7 | the instruction | a price per event; cross-entity effects |
| P8 | institutional cost; a shortening series; a declined remedy | triggers that are facility numbers; named cures |
| P9 | labelled projection; "is" against "known" | exits with prices; tactical figures |
| P10 | one doctrine figure; institutional cost; originality | staged guidance with thresholds |

Theirs ahead on the price of use or remedy in seven pairings (P1, P2, P3, P4, P5, P7, P9). Ours ahead on relation
honesty, meaning null results or a labelled projection, in six (P2, P3, P6, P8, P9, P10).

### The ten under `R-29`

`python3 tools/wikistd.py <dossier>`, run on each of the ten after they were chosen.

| Pair | Dossier | Parity | Condition | Own series | Dirty sections | Meets |
|---|---|---|---|---|---|---|
| P1 | `C-Iα-114` A Letter Never Sent | complete | no | yes | 2 | no |
| P2 | `C-IIβ-051` The Happy Mask | complete | yes | no | 4 | no |
| P3 | `C-IIIβ-015` The Debt Scale | complete | yes | yes | 6 | no |
| P4 | `O-IVδ-515` The Last Warmth of Forty-Two | complete | no | yes | 2 | no |
| P5 | `C-Iα-000` Kind Echo | complete | no | yes | 2 | no |
| P6 | `N-IIβ-033` Forgotten Soldier | complete | yes | yes | 8 | no |
| P7 | `O-IIIδ-011` Scar Walker | complete | yes | no | 9 | no |
| P8 | `N-IVδ-005` The Smothering Mother | complete | yes | yes | 7 | no |
| P9 | `C-Vω-001` Dawn of Mourning | complete | yes | yes | 0 | **yes** |
| P10 | `C-Vδ-002` The Grieving Colossus | complete | yes | no | 5 | no |

One of ten meets the standard; the archive's rate is 43 of 302. All ten carry every parity section and a
classified disposition. **The pairings and the test agree on where the work is and disagree on which dossier is
better.** Forgotten Soldier (P6) and the Smothering Mother (P8) are ahead of the wiki on several axes and carry 8
and 7 dirty sections; Scar Walker (P7), behind on most axes, carries 9. The last `R-29` clause measures residue,
not content, as `R-27` intends. That makes it the right binding constraint for the campaign and the wrong ranking
of quality: a pass is necessary for a finished page and is not sufficient for a good one.

---

## 8. Findings

### 8.1 Study 01, tested

1. **One obeyable sentence (Finding 1): stands, but its benchmark was misdescribed.** The wiki's management
   text is a list of two to five guidelines that decays from effect statements at ZAYIN into incident reports at
   HE. A single sentence a worker can obey is our improvement on the wiki, not the wiki's practice. What every
   standard page above ZAYIN does state, nearly always with figures, is its **trigger rule**, in one place and
   as a list. A reader of our dossiers assembles the same thing from the Activation threshold cell, the
   Escalation row and the notes; `R-06` fixes only the uniform part.
2. **Hazard and instrument are one object (Finding 2): stands, with more evidence.** Burrowing Heaven's gaze,
   Express Train's four lamps on a 30-second clock, Big Bird's lamp marks and Blue Star's 60 seconds are all
   instrument and hazard in one. Ours does it in the Colossus (fifteen minutes), Forgotten Soldier (31, 22, 16
   days) and the Mother (41, 29, 21 minutes).
3. **Irreversible loss stated once (Finding 3): stands, and is incomplete.** The wiki states the price of the
   remedy at every level above ZAYIN, and the price rises with level. Ours do not climb: a Rank I relic costs "a
   poignant ache", a Rank IV relic 15 Composure and 72 hours of weeping.
4. **Narrative escalates by kind (Finding 4): stands.** Scorched Girl's five entries are five kinds of document.
   Our Story Logs do the same, but every dossier has exactly five entries; the wiki's number varies from three
   to six.
5. **A finished article may admit the hazard is slight (Finding 5): stands, and needs a rider.** Three of four
   ZAYIN pages in the sample hide a catch in their Story. A Rank I dossier can still be a deliberate baseline
   with no catch (Kind Echo), and it should then say what was looked for.

### 8.2 `R-29` parity, row by row

| Row | Verdict |
|---|---|
| SECC Classification | Holds, level-invariant. |
| Combat Record, Behavior | Holds in name. Ours is categorical; the wiki's is a rating by employee level for each work type. By design (template line 184), not a gap. |
| Breach / Activation / Expansion / Containment Event | Holds from TETH up. **At ZAYIN the wiki has none**, and `R-29` demands one of every dossier. |
| M.A.W. Equipment | Holds for standard pages. The wiki's tool pages have none; our 83 relics carry three pieces each, a superset. |
| Flavor Text | Holds. Fandom keys it to events (dies, panics, breaching); wiki.gg to start and during. |
| Observation and Story Log | Holds. The wiki's count varies; ours is a constant five. |
| Management condition | Corrected: see 8.1.1. |
| Trivia | Holds; the wiki's is development-facing, ours in-world, which is a difference of function and not a gap. |
| Entity Interaction Record | Holds, and should deepen: the wiki's relations change a figure or an outcome. |

### 8.3 Rules the survey puts in question

1. **`R-06` describes one trigger family of nine.** "The count decreases by one on each failed or refused cycle"
   covers the work-result family only, and even there the wiki's counter sometimes rises on a Good result (Big
   Bird) or on Normal and Good (Burrowing Heaven), sometimes falls on a Good result (Cherry Blossoms) and
   sometimes falls by chance (50%, 70%, 30%, 90%). Eleven of sixteen standard pages use at least one trigger `R-06` cannot express.
2. **`R-28` is rank-blind.** The wiki's breach capability is a gradient; ours is flat (63, 56, 52, 61, 50%).
   A gradient would put the largest correction in Rank I, where 29 of 46 claim breach capability.
3. **`R-19` has no rule for a dual-mode entity.** The wiki tags the Queen of Hatred "capable of escape and
   benefitting the facility", and her Passive Breach, which assists suppression, occurs once Emergency Level 2 is reached.
   `R-19` and the Disposition Index use her as the reference point for **Neutral** ("lethal, but her damage is
   her own"), which reads against `R-19`'s own definition of Positive. The wiki's tags are multi-valued; `R-19`'s
   class is single-valued.
4. **The relic banner is a closed vocabulary on both sides.** Eighteen of twenty wiki pages open with a tag from a
   set of about eight; our 82 banner-carrying relics use eight strings. This bears on the open Workstream 6
   question whether the banner is furniture, and it says yes where the string is from the set and the Effect
   line carries the figure that earns it. It says no where the banner overstates the effect (P1).
5. **The Rank V numbers do not separate from Rank IV.** Ten of fourteen are below the conversion guide's own
   floor. The real difference at Rank V is the Sovereign Chronicle, which no test reads.
6. **The `R-01` sweep was undercounted.** `tools/editmeta.py` matched 58 dossiers. Reading these dossiers found a
   second family ("The earlier entry grading it Moderate … is an error and is corrected here", "Earlier copies
   named …") that it did not match. With the pattern extended it reports **88 dossiers, 159 candidate lines**.
7. **Borrowed numbers need a host.** The wiki disagrees with itself on one speed and one delay (§5.12). `R-09`
   already says to verify borrowed mechanics against the source page; the page and the host should be named.

### 8.4 `R-29` as a test

The ten were chosen by a neutral rule and not for their R-29 status, and nine of them fail it. Every failure is
on residue, a missing condition or a missing series, never on a missing section. So the test is reliable on what
it is for: it finds the work. It does not say which of two failing dossiers is the better article, and the survey
gives a way to say it, by the axes above (price, trigger rule, coupling, relation honesty, instrument). The
campaign keeps `R-29` as its counter, because the denominator is fixed (`R-20`) and the owner set it; the axes are
how a dossier is judged once it is clean.

---

## 9. What changes

**Applied with this study.**

- This study, `tools/ladder.py` (report only, not in the gate), and an addendum to Study 01 pointing here.
- `R-29` gains a **Part three**, additive: the ladder as author guidance, not as a test. `wikistd.py` and the
  fixed denominator (`R-20`) are unchanged.
- `tools/editmeta.py` extended with the second family (58 to 88 dossiers).
- The work record and the change log.

**Not applied, because each changes canon or a measure and belongs to the owner.**

| Decision | What the survey shows | What it would touch |
|---|---|---|
| A rank gradient for breach capability | 63% at Rank I against the wiki's 0% | Up to 18 Rank I dossiers to reach 75% non-breaching; reclassification only on each file's own evidence (`R-28`) |
| Rank V Sorrow Gauge against the conversion guide | 10 of 14 below 1,000 | 10 dossiers, or the guide |
| A stated trigger rule with figures as a seventh `R-29` test | present on 14 of 16 wiki pages | a new clause and a new denominator |
| `R-06` broadened to the nine trigger kinds | one rule against nine families | the rule text; no dossier |
| A dual-mode rule for `R-19`, and the Queen of Hatred reference point | one wiki entity is both | the rule text and the index header |
| Sanction the relic banner vocabulary | eight strings, closed | `tpl.py`'s residue list for 18 dossiers |
| A by-employee-level work matrix | the wiki's largest data block | the dossier template; a design change |

**Next targets for the dossier campaign, in the order the survey supports.**

1. The Rank V cohort. It fails `R-29` on the "own series" clause in 9 of 14. The work record called three of them
   projection-only; that was taken from the record and not checked, and it was wrong for two: the Final Door and
   Forgotten God are observed holdings, and only the Convergence carries projections (labelled in its Combat
   Record). Four of the nine were closed after this study, by stating in digits the record each file already
   kept in words; the measurement finding that follows from that is in the work record.
2. The `R-01` sweep on the 88-dossier list, converting each correction to cause.
3. The rank-blind event section: where a Rank I or II dossier's event table gives the stock drain for an event the
   file calls practically impossible (Kind Echo), say so or remove the figure.
4. The remaining targets already on the work record.

---

## 10. Sources

wiki.gg, `https://lobotomycorporation.wiki.gg/wiki/<page>`: One_Sin_and_Hundreds_of_Good_Deeds, Fairy_Festival,
Plague_Doctor, Old_Faith_and_Promise, Scorched_Girl, Fragment_of_the_Universe, Grave_of_Cherry_Blossoms,
Behavior_Adjustment, Happy_Teddy_Bear, Nameless_Fetus, Der_Freisch%C3%BCtz, Notes_from_a_Crazed_Researcher,
The_Burrowing_Heaven, The_Queen_of_Hatred, Big_Bird, Express_Train_to_Hell, Nothing_There, WhiteNight,
Blue_Star, Mountain_of_Smiling_Bodies; and the level pages ZAYIN, TETH, HE, WAW, ALEPH and Risk_Level.
Fandom, `https://lobotomycorp.fandom.com/wiki/<page>`: Scorched_Girl, One_Sin_and_Hundreds_of_Good_Deeds,
Nameless_Fetus.

---

**Counters at time of writing:** pages read 20 / 20 · pairings 10 / 10 · dossiers scanned 302 / 302 · dispositions
302 / 302 · `R-29` **43 / 302** (unchanged by this study) · section-clean 79 / 302 · rules 29.
