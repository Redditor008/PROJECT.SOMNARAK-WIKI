# The Dossier Points In-World — a record cites a record, never a shelf

**Stated by the archive owner, 2026-10-25:**

> *"Also in the dossier there should never be a `.md` mention used other way to point other file in a dossier that should act as if it was a dossier."*

## 1. What was wrong

The Director's dossier said, in the middle of the Solidification:

> The Memory Archive holds the manner of her death, and holds it plainly: she was the intellectual
> architect of the original containment systems, and when the breach opened she sealed the core with
> her own body, **shielding him from terminal psychic dissolution** (`` `The_MEMORY_ARCHIVE.md` § 3.2 ``).

Every word of it is true. None of it could appear in a document a reader inside the world is holding.
A dossier is a filing that exists **in** Somnarak; a citizen cannot open it and read a filename, a
folder path, or the archive's section numbering — those are facts about the shelf, not about the city.
The sentence had already named its source in its own subject: *the Memory Archive holds it*. The
parenthesis was therefore not carrying the attribution. It was carrying the filing cabinet.

The same class appeared in two other places, both of them story bodies:

- a Sorrow-Entity dossier's own **Archival Note** gave a full folder path — `` `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_1001_to_1043/1001_The_Kind_Echo/` `` — where a registry ID would do;
- three backstory files opened with a **PROVENANCE** line naming `` `THE_ARCHIVE_LEAD.md` ``, `` `THE_EXILE.md` ``, `` `THE_OUTSIDER.md` ``, on the first screen a reader sees, while the other six files in the same set named records in-world.

## 2. The rule

**A dossier addresses the world, not the repository.** A record may point at another record by what
it *is* — a name, an office, a registry number, a floor, a keeper's title. It may not point at another
file by its filename, its folder, or its section number.

**The test is what a reader can see.** A markdown link is legal and always has been:

```
[The Debt Scale](SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md)
```

renders as *The Debt Scale*. The filename lives in the destination and never reaches the page. The
archive needs 2,276 of these to navigate at all, every one of them renders in-world, and none of them
is the defect. The defect is a `.md` **on the page** — in prose, in a code span, in a table cell.

**What to write instead.** Use the in-world handle the corpus already has:

| Not this | This |
|---|---|
| `` `The_MEMORY_ARCHIVE.md` § 3.2 `` | *the Memory Archive*, *the Archive's own register*, *Floor 07* |
| `` `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_1001_to_1043/...` `` | *registry ID `SE-1001`*, *the 1001 set* |
| `` `THE_ARCHIVE_LEAD.md` `` | *the Echo-Core 7 dossier* |
| `§ 4` in a record | *the fourth register*, *the north wall ledger* |

## 3. What this does not forbid

- **Links.** See above: a link is how the shelf is reached without being described.
- **A backstory file's appendix.** The source ledger and the comparison tables exist to tie each claim
  to the file that carries it; the structure standard (`00_BACKSTORY_EXTENDED_STRUCTURE_AND_FORM.md`
  §X.3) requires exactly that, and it is archive apparatus, not story. The **story body above the
  appendix** is held to the rule in full — three files were failing that and are fixed.
- **The word "file" in-world.** *"The first of several silences in this file"* is a classified dossier
  describing itself, which `R-01` explicitly permits. The rule is about filenames, not about the noun.
- **`filed`, `filing`, `case file`, `evidence file`.** The world's own vocabulary.

## 4. Enforcement

`tools/auditors/check_dossier_world_pointer.py` — gate 57. It reads all 310 dossiers and the nine
backstory story bodies, replaces every link destination with its label, and fails on any filename,
folder path, or bare section number left visible. **Ceiling is zero and there is no debt register:**
the four files that carried the class were fixed in the batch that created the rule.

The gate's own first version could not see its own founding example — the negative lookbehind
excluded a backtick, so a filename inside a code span was invisible to it. Caught by feeding it the
exact defect that produced the rule. **A checker is not finished until it has been shown to fail.**

## 5. Scope

`SOMNARAK-WORLD/Echo_Cores/THE_*.md`, `SOMNARAK-WORLD/Sorrow_Entities/SE-*.md`,
`SOMNARAK-WORLD/Unknown_Entities/SE-*.md`, and the story body of every
`SOMNARAK-WORLD/Echo_Cores/Backstory_Extended/*.md`. `SOMNARAK-WORLD/Pages/` is the wiki's own
navigation and contributor manual — it is not a dossier and is outside the rule.
