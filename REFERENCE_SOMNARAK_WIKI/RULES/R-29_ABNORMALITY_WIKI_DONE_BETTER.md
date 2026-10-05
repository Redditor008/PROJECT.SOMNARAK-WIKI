# R-29 — The Standard Is An Abnormality Wiki, Done Better

**Stated by the archive owner, 2026-10-05:** *"What You Do Is Just Basically Do What An Abnormality
Wiki Do But Better For SE"*.

This names the thing the whole project has been aiming at, so it is written down as the standard
every dossier is measured against.

## Part one — parity

A good Abnormality wiki page carries nine things. Every Sorrow Entity dossier must carry the
equivalent, and the archive's section names are fixed to them:

| An abnormality page has | A dossier carries | Present in |
|---|---|---|
| Code, risk level, containment location | `## SECC Classification` | 302 / 302 |
| Stats and work results by work type | `## Combat Record`, `## Behavior` | 302 / 298 |
| Escalation and breach behaviour | one of `Breach` / `Activation` / `Expansion` / `Containment Event Behavior` | 302 / 302 |
| E.G.O equipment with its cost | `## M.A.W. Equipment` | 298 |
| Flavour text | `## 감각 묘사 (Flavor Text)` | 298 |
| Observation / story log | `## 이야기 보고 (Story Log)`, `## 관찰 기록 (Observation Log)` | 298 |
| Management tips | the management condition, stated as one obeyable sentence (`R-24`) | — |
| Trivia | `## Trivia` | 298 |
| Related abnormalities | `### Entity Interaction Record` | 297 |

Parity alone is not the standard. It is the floor.

## Part two — better

Six things a wiki page does not do, which this archive does. These are the real content of "better"
and they are already rules; `R-29` is where they are collected as one test.

1. **Every figure is traceable to that dossier's own record.** No number appears in a dossier that
   is not grounded in its own series, log or register. A wiki quotes the game's numbers; this
   archive has to have measured its own.
2. **No line is shared with ten other entries** (`R-23`, `R-24`, `R-27`). A wiki is full of template
   furniture and nobody minds. Here it is the defect being removed.
3. **Every holding has one instrument of its own** — a measurement that belongs to it and to nothing
   else: a tear count, a transit time, a settle rate, a shard count, a words-per-hour figure. No
   instrument is reused between dossiers.
4. **The institutional cost is stated.** What the facility pays, refuses, defers or quietly declines
   to fix. A wiki describes the monster; this archive also describes the organisation that keeps it.
5. **Projections are labelled as projections.** Where nothing has been observed, the dossier says so
   rather than inventing confident mechanics (`C-Vω-001`, `C-Vδ-010`).
6. **Every entity is classified by what it does to the facility** (`R-19`), evidenced by a quoted
   line, and the classification is not a threat rating.

## The test

`tools/wikistd.py` reports parity and the four testable "better" clauses per dossier, and the
archive totals. A dossier **meets `R-29`** when it has every parity section, a specific management
condition, at least one numeric series of its own, a disposition row, and is section-clean under
`R-27`.

## Part three — the ladder (added after Comparative Study 02)

Parts one and two were collected from a single comparison. `COMPARATIVE_STUDY_02_TWENTY_PAGES_FIVE_LEVELS.md`
read twenty pages at all five risk levels, three of them on both wiki hosts, and set ten dossiers against
them. **The test above is unchanged, and so is its denominator (`R-20`).** What the wider reading adds is
guidance for whoever writes a dossier, and one correction to Part one.

**The correction.** The wiki's management tips are a list of two to five guidelines that decay from
statements of effect at ZAYIN into incident reports at HE. One obeyable sentence is our floor above the wiki,
not parity with it. What every standard page above ZAYIN does state, nearly always with figures, is its
trigger rule.

**The frame does not vary with rank.** The wiki's frame is the same at ZAYIN and at ALEPH, so the nine parity
sections are a presence test at every rank.

**What varies is how tightly the entity is coupled to the facility.**

| Rank | Reach of the effect, as the wiki's pages show it | What the file should state |
|---|---|---|
| I | the unit; leaving it is the exception | what was looked for, where no catch is claimed |
| II | one target or one room | the event figures and the cost of the remedy |
| III | a department, or another entity's counter | a price per event |
| IV | the facility's own numbers (casualties, alert state); families and cures | the trigger rule with its figures; the named relations |
| V | modes, formulas, several exits | the exits and what each costs, labelled as models where nothing was observed |

Four habits follow, none of them a pass or fail test:

1. State the trigger rule with its figures, in one place.
2. Let the price of use or of the remedy climb with rank. A Rank IV relic that costs what a Rank I relic costs
   has not been priced.
3. Let a relation change a figure or an outcome, and record the pairings that did nothing.
4. Where an event table gives a figure for an event the file calls practically impossible, say which it is.

`python3 tools/ladder.py` reports the by-rank figures the study used. Rules the study puts in question (`R-06`,
`R-19`, `R-28`) are listed with their evidence in its section 8.3 and are left to the owner.
