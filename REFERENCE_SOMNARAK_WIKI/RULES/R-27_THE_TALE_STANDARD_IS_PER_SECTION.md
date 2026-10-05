# R-27 — The Tale Standard Is Per Section, Not Per File

**Stated by the archive owner, 2026-10-05:** *"The Tale Standard Things Is For Any Section That Have
Many Description Example Behavior Section And The Example Meant That An Example Not Just Me Saying
Only That But Other Thing Also The Same"*.

## The rule

`R-24` set the Tale standard: prose must be this entity's own, measured by 8-gram sharing, clean at
≤ 0.05. `R-27` fixes the **unit of measurement**. The standard applies to **every section that
carries description**, separately. Behaviour is one example. It is not the list.

Sections in scope include — and are not limited to — Behavior, Combat Record, M.A.W. Equipment,
감각 묘사 (Flavor Text), 기록 (Registrum), 관찰 기록 (Observation Log), 최종 관찰 (Final Observation),
Trivia, Appearance, Operational Parameters, Breach / Activation / Expansion Behavior, Story Log,
Origin, Apex / Watch / Warden Records. If a section describes something, it is in scope. Tables of
pure classification furniture (`R-23`) are not.

## Why the file-level number was not enough

Measured on the day this rule was written: **81 dossiers counted clean at file level had at least
one section above 0.05**, and in nine of them a section scored **1.000** — entirely generated text —
hidden behind a good file average. The worst offenders archive-wide:

| Dirty in | of | Section |
|---|---|---|
| 248 | 298 | 최종 관찰 (Final Observation) |
| 225 | 297 | M.A.W. Equipment |
| 221 | 302 | Combat Record |
| 185 | 298 | 감각 묘사 (Flavor Text) |
| 156 | 298 | Trivia |
| 145 | 297 | 기록 (Registrum) |
| 132 | 298 | Behavior |

A file average lets a long bespoke section pay for a short generated one. That is exactly the
accounting `R-20` forbids elsewhere, and it was happening here.

## The measure

`tools/sectfile.py <path>` reports every section of one dossier separately and exits non-zero if any
is above 0.05. A dossier is **section-clean** when it reports `0 section(s) over 0.05`.
Sections under twelve shingles are reported THIN and judged by eye.

## The counter changes

The headline counter for Workstream 6 becomes **section-clean dossiers**. The file-level figure is
kept beside it as a secondary, because it is still the right measure of total archive drift. On the
day of this rule: file-clean **121 / 303**, section-clean **40 / 303**. The second number is the
real one and it is smaller, which is the point.
