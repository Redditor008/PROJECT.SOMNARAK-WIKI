# R-21 — Five Whole-File Cleans Per Prompt

> *"A long turn is cheaper than five short ones. Take the time."*

## The instruction

Each working prompt delivers **five whole-file cleans**, not one. A turn may run long — thirty
minutes of tool work is acceptable and expected. Length is not a reason to cut the batch short.

## What does not change

Everything that made one clean correct still binds on all five:

- `R-04` Bespoke Per Entity. Five files means five *different* mechanisms, five different readings,
  five different grounded inversions. A batch is not a licence to reuse a design.
- `R-02` Growth-Only. Word count rises in every file.
- `R-05` No Threshold Gaming.
- `R-15` Clean Fix, Not Cover-Up — the full per-file verification runs on each file: residual count,
  seam grep, pipe check, duplicate-sentence scan, mirror pass.
- `R-20` One Fixed Denominator. The counter moves by five, to `N / 291`, and by nothing else.

## Batch procedure

1. Re-rank before the batch, and again after each file, so targets two through five are chosen on
   live counts rather than on a list made before any of the work was done.
2. One commit per file, each with its own measured residual in the message. **Not one batch commit** —
   a five-file commit hides which file a defect came from.
3. Gate chain and metrics parity run before each push, as `R-11` requires. No exceptions for batches.
4. Report all five separately: mechanism, reading, residual, and the two numbers. A batch summary
   that averages the five is not a report.

## The failure mode this rule invites

Five files in one turn is exactly the pressure under which boilerplate gets written *back in* —
reaching for a mechanism that worked two files ago because inventing a sixth is harder than reusing
a fifth. The anti-template lists in the working notes exist for this and are checked per file, not
per batch. If a batch cannot produce five distinct designs honestly, it ships four and says so.
