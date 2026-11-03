# R-39 — Write It Back, and Chain It

**The owner's instruction, verbatim:**

> *"Also when fixing by writing instead of erasing or cutting used logic for whatever you're fixing, and the logic needs to chain to one another."*

**The rule.** A fix removes nothing that was doing work. When a defect is found in a
statement, the repair **writes a better statement in its place**, and the replacement
must **connect to the record's other statements** — same figures, same terms, same
conclusion — so the reader meets one chain of reasoning and not a patch.

**Why.** `R-02` already forbids shrinking a file. `R-39` says what to do instead of
shrinking: put a real sentence where the bad one stood, and make it agree with
everything around it. A deletion satisfies a checker and leaves a hole. A rewrite
that lands a new number beside an old one in the same file has traded one defect for
another.

**What this forbids.**

- Cutting a sentence because it is boilerplate, without replacing its *function*.
- Repairing a quote by trimming it when the thing it quotes should be rewritten.
- A fix that introduces a figure, band, grade or rank that appears nowhere else in
  the same record or set.
- Two halves of one mechanic stated in two places with no link between them.

**What it requires.**

- The replacement is at least as long as what it replaced, and carries the same
  fact in more grounded form.
- Every number in the new text is traceable to the same record or set.
- If the statement lives on one page of a set, the pages it speaks for must be
  brought into line with it — the chain runs both directions.

**The worked example: batch 142.** Batch 140 had deleted *"The Sorrow Gauge held at
its opening band."* from 76 set pages. It was true that the sentence was a default —
but deleting it left the piece pages with no gauge statement at all, and left the
failure mode truncated. Batch 142 wrote it back:

- Each piece page now files `**Gauge:** 739/739; opens at 45–65%; no hit band is filed.`
- Its failure mode chains the consequence to the same figures: *"…raises the source
  Gauge, so the 739/739 meter moves off its 45–65% opening band before the bearer
  feels the reversal."*
- The set's A-page carries the same reading in prose, and the A-page's
  `Gauge / Pressure` row is the origin of all three.

`tools/auditors/check_gauge_chain.py` enforces the second half of this rule
mechanically: a figure on a piece page that does not appear on its set record fails
the gate.

**The trap.** Chain-checking is not agreement-checking. Four pages can quote one
number and all four can be wrong together. This rule keeps a record *consistent*; it
does not make it *true*, and a consistent record still needs to be read.
