# Somnarak recovery package — visible in Arena Diff

These two root-level files were deliberately placed in the repository working
tree so they appear in Arena's **Diff** panel. They are recovery artifacts,
not permanent website files.

## Files to save

1. `SOMNARAK_UNPUBLISHED_98c2059.patch`
2. `SOMNARAK_RECOVERY_README.md`

The patch preserves the validated unpublished workspace formerly represented
by local commits `71fddde` and `98c2059`.

## Package identity

- Baseline: `e132c026a675ffd3f0163c185116740ceb8e7472`
- Baseline meaning: public `main` at packaging time
- Changed project paths represented: 210
- Patch SHA-256: `5456894b53d1b3d02435c60ebd9558491e1765552f25ff53559c753f62bf8fc7`
- Patch application check against that baseline: PASS

## Use in a new active Arena session

1. Save both files from this session's Diff panel.
2. Start a new active coding session for the repository.
3. Attach both files to the new session.
4. Ask the agent to inspect current `main` before applying the patch.
5. Run:

   ```bash
   git apply --check SOMNARAK_UNPUBLISHED_98c2059.patch
   git apply --index SOMNARAK_UNPUBLISHED_98c2059.patch
   ```

6. Remove the two recovery artifacts from the new repository working tree
   before committing; they are transfer files, not project content.
7. Run the complete 197-page validation suite and `git diff --check`.
8. Commit and push immediately to the one Arena-assigned branch.
9. Open a pull request into `main`, merge it, and verify GitHub Pages.

## Policy filename correction included

Public `main` contained `RULE TO FOLLOW.md`, while the validated workspace uses
canonical `RULE-TO-FOLLOW.md`. The patch reconciles that mismatch and retains
the hyphenated root policy.

If `main` has advanced and `git apply --check` reports conflicts, do not discard
the patch. Reconcile it deliberately against the baseline listed above.
