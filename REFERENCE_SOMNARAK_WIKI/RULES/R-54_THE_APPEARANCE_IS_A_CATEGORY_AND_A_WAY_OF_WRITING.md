# R-54 — The Appearance Is a Category, and a Way of Writing

**Stated by the archive owner, 2026-10-25:**

> *"On Appearance Things The Things You Mention Mean For You To Check If Every SE Minimum Fall Onto
> That Category and More And Also The Appearance Things Is Two Things The Category Things And The
> Following How L corp Write Them Things"*

## 1. What this overturns

`R-53` §1 records that `O-14` "claimed a partial that no gate can reach", because the four shapes —
Human, Monster, Animal, Abstract — are not a recorded field, and `**Physical Form**` is `Mixed` on
most subjects. That reasoning was wrong, and the owner said so.

It was wrong about **where the category lives**. `Physical Form` is a classification column, and it
was never the description of a body plan. The body plan is already written, in prose, in the
`## Appearance` section of every dossier — the section asks the writer to state the form first, and
almost every file does. 213 looked for the category in the column and concluded the archive had no
category. The archive had 301 of them, in the section the reader meets first.

So `O-14` is reopened. The schema change it asked for was already in the files; what was missing was a
gate that read them.

## 2. The rule

**Appearance is two things, and a dossier must satisfy both.**

**A — the category.** The dossier's own form statement — the `**Form**` row, the `**Physical Form:**`
line, the `**Primary Form:**` line, or the `**Primary marker:**` line — must resolve to one of the
`R-32` families:

| family | what it is | example |
|---|---|---|
| humanoid | a body with a human plan, worn or built | a clerk, a doll, a saint, a statue |
| monster | an assembly that is no single animal | an amalgam, a many-limbed horror |
| animal | a beast, or a body read as one | a raven, a serpent, a swarm |
| abstract | a phenomenon with no body to hold | a voice, an hour, a pressure |
| place | a ground, a structure, a reach of water | a wall, a garden, a river |
| object | a made or found thing | a compass, a tear, a ledger |
| mechanical | a machine, or a body run by one | a clockwork, a boiler, a crawler |

Every one of the 301 dossiers resolves. The archive reads humanoid 117 · place 82 · object 51 ·
abstract 25 · animal 19 · mechanical 4 · monster 3. `R-32` asks for four families at minimum and all
seven are present.

**B — how L Corp writes it.** The section is an observation record, and it is written in one of two
shapes. Both are correct; the file must be one of them, not a draft of neither:

- **the ledger** — a `**Form**` table, and the four observer's readings as labelled rows: form,
  position and movement, material and signature, distinctive markers;
- **the observation** — continuous prose in the order of meeting, at least 120 words, whose opening
  sentence states the body plainly. Its readings are carried in the prose and are certified by the
  reader's pass (`O-29`, `R-38`), not by a pattern match.

288 dossiers are ledgers; 12 are observations. Both counts are reported by the gate, because a check
that silently stopped matching one shape would look like it had nothing to say.

**Neither shape may explain.** `R-45` §0.2 named the essayist defect; `R-45` §3 gives Appearance its
contract — *observation, in the order of meeting* — and bans three things from it: a mechanic, a
consequence, and an interpretation. The tell is a symbolic verb: *a bloom stands for a wrong*, *each
feather represents a grief*. The same content in record register — *corresponds to* — is a fact about
the entity and belongs. The difference is not the claim. It is who is talking.

## 3. What was measured and what it cost

The gate's first run reported 92 dossiers missing a reading and 33 interpretation tells. The second
run, after the reader was fixed, reported 16 unfiled shapes and 7 tells. The third reported 0 shapes,
1 reading, 3 tells. **Most of the first two numbers were the checker's, not the archive's:**

- `\bwall\b` does not match *walls*. The lexicon had no plurals.
- `**Physical Form:**` and `**Primary Form:**` are form statements, and the first version only looked
  for `**Form**`.
- 12 dossiers write Appearance as continuous prose and were being scored for missing table rows.
- `stands for more than three minutes` was being read as a symbolic claim.

The real defects were four, in four files: one missing material reading, and three Interpretation
tells. The tells were fixed with the archive's own wording — `corresponds to`, the register the same
dossiers already use for their indicators — not with a rewrite that invented a meaning.

**A gate's first reading is a measurement of the gate.** The archive numbers came down from 92 to 4
without a single dossier changing until the fourth run, and the four that changed were the four that
were actually wrong.

## 4. Why the prose shape is allowed

`R-45` does not ask for a filled form. It asks for the thing a reader would see standing in the room,
in the order they would see it. A section that reads

> *The red silk and tarnished copper braid is the entity's body; its split bite-marked coin is the
> terminal piece.*

does that better than a table, and `SE-N-IIIβ-1056` carries its category — object — in the first
clause of its first sentence. Requiring a table of it would be requiring the archive to write worse
to satisfy a checker.

What the gate therefore requires of a prose section is not labels but **substance**: a stated form, and
enough of it that a reader has something to read.

## 5. What is checked

`check_appearance_contract.py` (gate 50) reads all 301 dossiers and reports the family distribution,
the count written as ledger and as observation, the unfiled shapes, the missing readings, and the
interpretation tells. It fails on an unfiled shape, a ledger with a missing reading, and a section
that is neither shape. A tell count above zero is reported and is a defect to fix, not a fixture to
accept.

The gate reads the **dossier's own statement**, never a classification column, so the `Physical Form`
argument cannot come back.
