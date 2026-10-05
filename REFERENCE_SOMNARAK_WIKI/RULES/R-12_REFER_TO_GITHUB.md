# Refer to GitHub, Not the Workspace

**The rule.** Work is reported with GitHub URLs on the working branch, never with local workspace paths, and the branch is kept pushed so the GitHub view is current.

**Pattern.** `https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/<branch>/<path>`, where `<branch>` is the branch the session is working on (`git branch --show-current`). The finished file is not on `NON-WIKI` until the owner merges, and an earlier version of this line named an earlier session's branch, which is the mistake `tools/gate.sh` once made; the branch is read, never copied.

**Encoding.** `δ` → `%CE%B4`, `β` → `%CE%B2`, `γ` → `%CE%B3`, `ω` → `%CF%89`, `α` → `%CE%B1`, and Hangul likewise. Dossier file names are linked in full, Hangul and all (see Format below); the directory link `.../tree/<branch>/SOMNARAK-WORLD/Sorrow_Entities` is the fallback.

**Corollary.** Push after every unit of work. An unpushed commit is invisible to the person reading the result.

**Format (stated by the archive owner, 2026-10-05).** When a unit is finished, link each finished dossier at the
end of the report in this form, with the file name without `.md` as the link text, the percent-encoded path as the
URL and the file name with `.md` as the tooltip:

`[[SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/<branch>/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-014_The_Debt_Eater_%EB%B9%9A%EC%9D%84_%EB%A8%B9%EB%8A%94_%EC%9E%90.md "SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md")]`

The short form, with only the English name as the link text, is equally accepted:
`[[The_Debt_Scale](… "SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md")]`. Underscores and hyphens are not encoded.

**Tool.** `python3 tools/ghlink.py <path> …` prints the links. `--short` gives the short form, `--changed` lists every
dossier that differs from `NON-WIKI`, and `--branch NON-WIKI` reproduces the owner's two examples byte for byte.
