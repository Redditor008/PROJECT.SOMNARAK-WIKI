# No Label Decoration

**The rule.** Labels are labels. They are never decorated with the entity's identity.

**What this forbids.**

- Appending the entity name to a table or callout label: `**Breach type (Broken Door)**`.
- Appending a code tag to a sentence: `… as recorded [SE-O-IIβ-757].`
- Naming the entity inside a Work Type label or a record-suffix label.

**Why.** Decoration is differentiation theatre. It makes two identical rows look different to a line-comparison metric while the row says exactly the same thing. It is the cheapest form of the gaming this project forbids.

**Enforcement.** `tools/label_lint.py` rules R5 `CALLOUT_SELF_NAME`, R6 `WORKTYPE_SELF_NAME`, R7 `RECORD_SUFFIX_SELF_NAME`. Every cleaner additionally asserts that no replacement text contains `[SE-` or a parenthesised code.

**Known hazard.** `label_lint.py` exits 0 even when it prints violations. Grep for its explicit PASS string; never trust the exit code.
