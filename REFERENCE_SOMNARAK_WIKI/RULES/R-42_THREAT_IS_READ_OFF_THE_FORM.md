# R-42 — Threat Is Read Off the Form

**Stated by the archive owner, 2026-11-04:** *"I think the Convergence feel lack luster compare to
the Maw — can you make sure ALL Special Case SE will be HIGH THREAT in forms and not just in
designation. This work for all TOP up to HIGH threat. [Low, Medium, Common, Top, High, SPECIAL —
all threat tier based of combat sense.]"*

## 1. The ladder, in the words the owner uses

The archive already had the scale. `R-41` sets the Threat Score as **Coherence rank + Potency
grade**, and `tools/check_stat_bands.py` reads it. The owner's names sit on that scale in order:

| band | code | Threat Score | guide tier | what it means in a room |
|---|---|---|---|---|
| **Low** | ZAYIN | 2–3 | one body, one worker, handled by procedure | it can hurt the person in front of it |
| **Medium** | TETH | 4–5 | a team, contained by the standard session | it can hurt the team |
| **Common** | HE | 6 | a wing, requiring a plan before entry | it can end a shift |
| **Top** | WAW | 7–8 | a facility, requiring an order above the wing | it can end a wing |
| **High** | ALEPH | 9–10 | the city, requiring a posture | it can end a district |
| **SPECIAL** | — | 9–10, and never held | the archive has no containment for it at all | it is a terminus; there is nothing on the other side to handle |

**SPECIAL is not a sixth rung of the same ladder — it is the top of it, and it is a class rather
than a grade.** A Special Abnormality is the terminus of a transformation line: it is never
acquired, never worked, never extracted (`R-35`). Measured on the Threat Score, all three declared
termini land on High, and that is deliberate: the class sits *above* High, and a terminus that
scored Lower than a well-handled Top would be a contradiction in the code itself.

## 2. What "in form, not in designation" means

A code is a filing decision. **A form is what the file says the thing does.** A dossier whose code
reads Top while its stat line prints a Fragment's blow, or whose combat text keeps saying that
nothing happened, carries its tier only in the designation — and the owner named the failure:

> The Convergence read lacklustre beside The Maw. Both are filed at the same score. The Maw's file
> describes a district that takes the ground out from under a person and a thousand voices that
> know their name. The Convergence's described three teams failing slowly and then said, five times
> in one table, that nothing had been measured.

The band has to be visible in four places, and the gate measures the first:

1. **The stat line.** `Han Pressure [ATK]` opens at or above the band's floor. A Top entity's
   lightest blow cannot be a Common entity's blow.
2. **The actions.** What the five moves actually do to a person, in the file's own idiom. A cell
   that says *projected, never measured* is honest once; repeated in every cell it is an excuse
   for having nothing to say.
3. **The appearance.** Scale, sound, what a person sees before they understand what they are
   looking at.
4. **The consequences.** What it costs the station, not what the file wishes it knew.

## 3. The floor rule, and the tolerance it withdraws

`check_stat_bands.py` has always treated a range that starts under the floor as a **note**, not a
failure, on the owner's earlier one-directional ruling: *nothing is to sit under its risk level*,
and a body whose escalation crosses a seam was allowed to straddle.

**At Top and above, that tolerance is withdrawn.** A straddling range at WAW or ALEPH means the
entity's weakest blow is a tier below its own code, which is exactly the *in designation, not in
form* defect this rule exists to stop. Below Top the note stands: a TETH entity that sometimes
hits like a ZAYIN is variance, not a contradiction.

Measured on 2026-11-04, before this batch: **47 of the 55 Top-and-above records that carry an ATK
row opened below their own band** — one High record opened at 25 against a floor of 50, and a Top
record opened at 14 against a floor of 30. All 47 were shifted up until the floor was met. Each
range kept its own width, so the population still varies; no ceiling was invented where the range
was already inside the band.

## 4. What the gate does

`tools/auditors/check_threat_form.py` (gate 39):

- every **Top or High** dossier that carries a `Han Pressure [ATK]` row must open at or above the
  band floor;
- every **Top or High** dossier that carries a `## Contact Record` instead must state why it has no
  combat actions — the `R-36` reason line — so that its tier is argued in words rather than
  implied by the code;
- every **Special Abnormality** must be banded at High, and, if it carries an ATK row, must open at
  or above the High floor.

**What the gate does not police.** It cannot read whether a paragraph is frightening. It measures
the two things that can be measured — the floor, and whether a non-fighting Top entity has said
why it is Top. The prose half of this rule is a reading, done by hand, which is why the Convergence
was rewritten rather than rescaled.

## 5. Precedents

- **The Maw `C-IVω-001 [GP]`** — the benchmark the owner measured against. An entity with no hands,
  no eyes and no reach, filed at the top of the ladder, and the file never once apologises for it.
- **The Convergence `C-Vδ-010 [WS]`** — rewritten under this rule: ATK 25–53 → 50–80, five actions
  given real effects, the four apologetic consequences replaced with what the station actually
  carries, and the appearance given a span wider than the chamber it forms in.
- **The chain idiom (Forgotten God, Stormscale, Dawn)** — three files whose action values sat an
  order below their own ATK rows. All three now read the Grudge tick as the ATK figure, so a reader
  can add the cycle up and land on the number the stat line promised.
