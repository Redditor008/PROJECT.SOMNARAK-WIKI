# R-39 — Write It Back, and Chain It

**The owner's instruction, verbatim:**

> *"Also when fixing by writing instead of erasing or cutting used logic for whatever you're fixing, and the logic needs to chain to one another."*

**The rule.** A fix removes nothing that was doing work. When a defect is found in a
statement, the repair **writes a better statement in its place**, and the replacement
must **connect to the record's other statements** — same figures, same terms, same
conclusion — so the reader meets one chain of reasoning and not a patch.

**The two-sided test — expansion is conditional, not compulsory.** The owner put the
limit on the rule himself: *expand instead of shortening or erasing — but if
expanding makes the thing illogical, do the opposite.*

So the decision is made by the result, not by the preference:

1. **Can the statement be expanded into something true?** If the record already holds
   the material — a figure, a condition, a mechanism, a consequence — write it out.
   Expanding is the default because it keeps what was there and adds what was missing.
2. **Would the expansion be illogical?** Then cut, and cut hard. Padding a defect to
   keep a word count is worse than the defect: it buries it under prose that sounds
   considered. A tautology does not become a statement by being lengthened; a
   duplicated list does not become a description by gaining adjectives.
3. **The test is truth, not length.** Expansion is justified only when every added
   clause is traceable to the record. If the only way to lengthen a sentence is to
   invent, or to restate its own label in more words, the answer is the opposite one.

**The inflation test — and how to tell a fix from stuffing.** The owner put the
sharpest limit on it yet: *"before the fix it was 200 words long, but after the fix it
suddenly grew another 100 — that's just inflation, not a fix. You could tell if things
is really a fix or just stuffing to cover the test."*

Length is not evidence. Growth is earned only where the added words carry a datum the
record already holds — a figure, a code, a named condition, a procedure. The test is
mechanical enough to run:

1. **Delete the added clause and ask what fact disappeared.** If a figure or condition
   goes with it, the clause was a fix. If the paragraph still says the same thing, it
   was stuffing — remove it, whatever the word count then reads.
2. **Count what went in.** `tools/auditors/check_fix_density.py <from> <to>` diffs at
   **word** level (a line diff reports whole paragraphs as added and lies), separates
   content words from grammar, and reports what fraction of the inserted content
   carries a datum. It reports; it does not gate, because "opens at 45–65%" needs the
   word *opens* to say anything.
3. **Rhetoric is the tell.** A clause about how the bearer *feels*, what a reader
   *senses*, or how the meter *seems* to move is stuffing even when the surrounding
   figures are true. Batch 144 removed exactly that from a clause it had written two
   batches earlier.

**Worked example of the opposite.** The `activation-echo` cell read
`| **Activation threshold** | Activation / expansion trigger — no breach counter |`.
It could have been expanded into a longer sentence about triggers. That would have
been illogical: the defect was that the cell answered its own label, and a longer
non-answer is still a non-answer. It was replaced by the record's own answer —
`No breach counter; activates on direct gaze.` — which happens to be shorter than a
padded version and is the only version that is true.

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
