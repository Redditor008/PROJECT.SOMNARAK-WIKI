# R-44 — The Cost of the Session

**Stated by the archive owner, 2026-11-04:** *"The meaning of consequence to all SE is: there will be
a cost on working on them, and what the cost is based on what they are and what they do. Try to
research L Corp stuff — work damage, work interaction, and much more."*

## 1. What L Corp actually files, and what this archive was missing

A Lobotomy Corporation Abnormality page carries, in its basic information, four things that decide
what a work session costs:

| L Corp field | what it is | does this archive have it? |
|---|---|---|
| **Work Damage** | a damage **type** (Red / White / Black / Pale) and an **amount** (`1-3`, `6-8`, `5-10`) taken by the employee *while working* | **no — 0 of 301 dossiers carry it** |
| **Work Preferences** | the four works ranked best to worst — Instinct, Insight, Attachment, Repression | yes — Flerehan / Pugnahan / Viderehan / Ferrehan, matrix-bound by `R-41` |
| **Maximum E-Boxes** and outcome ranges | Good / Normal / Bad thresholds | yes — Han-Energy yield, and the barred cells |
| **Qliphoth Counter** | the number the work can move, and what happens at zero | yes — the Q Counter |
| *work cooldown, work speed* | pacing | partly — `Work difficulty`, R.D. level |

**The missing one is the one the owner named.** The archive could say which work a holding answers
to, and how much energy the session produced, and it could not say what the session **cost the
person doing it**. That is why every holding felt the same to work: the only thing a session ever
produced was a number going up.

## 2. The field

```
| **Work Damage** | 6–9 Grudge — the cost is carried weight: the session is walked, not stood |
```

Three parts, in this order:

1. **An amount**, inside the band for the entity's tier (§3).
2. **A type**, which is the entity's own `Element` row. L Corp has four damage types; this archive
   has four sorrows, and they are the same four. A holding whose element is `All four` cycles
   through them and says so.
3. **A clause saying where the cost comes from** — one sentence, in the entity's own terms, naming
   the mechanism. *Not* a restatement of the element. The Maw's cost is being named by the
   thousand; the Final Door's is hearing the whisper and speaking first; the Ancestral Guilt's is
   genealogical and comes out of the vault with the keeper.

The row sits in the statistics table, directly under `Work difficulty`.

## 3. The bands

Read off the same scale as `R-42`, and deliberately the same shape as L Corp's own spread — a TETH
object that costs `1-3` and an ALEPH that costs `5-10`:

| band | Work Damage |
|---|---|
| **Low** (ZAYIN) | 1–3 |
| **Medium** (TETH) | 1–4 |
| **Common** (HE) | 2–6 |
| **Top** (WAW) | 3–8 |
| **High** (ALEPH) | 5–10 |

**A Special Abnormality has none.** `R-35` says a terminus is never worked; there is no session to
cost, and a `Work Damage` row on one would be the same defect as a work table on one. Their yield
row already opens with `—`.

## 4. What is enforced now, and what is measured

`tools/auditors/check_work_damage.py` (gate 87):

- **fails** any holding whose `Work Damage` amount falls outside its band, or whose type does not
  match its own `Element` row;
- **fails** any holding that carries no work loop (yield opens `—`) and a `Work Damage` row anyway,
  which is how a terminus or a relic gets caught;
- **fails** a High holding that carries a work loop and no `Work Damage` row at all;
- **reports** every lower band that has not been rolled out yet, counted per band.

## 5. Why the rollout is staged

The row has to be written from what each holding is, which is 301 separate readings. This batch
does the **High** band completely — the seven worked ALEPH holdings — and establishes the rule and
the gate. The 288 below it are counted in the gate's report so the remainder is a number, not an
intention.
