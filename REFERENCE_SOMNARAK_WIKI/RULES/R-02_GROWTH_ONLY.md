# Growth-Only

**The rule.** No edit may make a dossier shorter. Every rewrite ends at equal or greater length than it began.

**Why.** Deletion is the cheapest way to make a quality metric move and it destroys material that cannot be recovered. A boilerplate paragraph is a *bad* paragraph, not a *surplus* one; the fix is a better paragraph of at least the same size.

**What this forbids.**

- Deleting a repetitive section instead of rewriting it.
- Replacing prose with a link to a shared reference page.
- Trimming a file to hit a word target. Reviewer-proposed word-count reductions have been declined on this ground.

**Verification.** Every cleaner script asserts `after >= before` on word count before it is allowed to write. A failed assert aborts the run with no file touched, which makes the run safely repeatable.

**The trap.** Bespoke rewrites silently shrink files, because a tight sentence replacing a bloated one is shorter. Author at genuine length instead: more grounded detail, not padding. Never relax the assert.
