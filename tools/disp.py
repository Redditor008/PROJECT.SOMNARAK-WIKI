#!/usr/bin/env python3
"""disp.py — Entity Disposition Index maintenance.

  disp.py "<row>"   append a row to '## Neutral' (Neutral-insert only, by design:
                    the tool has no class awareness, so Positive/Negative rows are
                    hand-spliced into their own section and then --recount is run)
  disp.py --recount recompute the coverage counters from the rows actually present
"""
import io, re, sys

P = "REFERENCE_SOMNARAK_WIKI/ENTITY_DISPOSITION_INDEX.md"
CODE = re.compile(r"`?(?:SE-)?([A-Z]-[IVX]+[\u03b1-\u03c9]-\d{2,4}[a-z]?)`?")
TOTAL = 302  # entity dossiers carrying an SECC code; the 303rd catalogued file is the Regressor log

def classified_codes(index_text):
    """Every entity code carrying a row in Positive / Neutral / Negative."""
    out = set()
    section = None
    for ln in index_text.split("\n"):
        if ln.startswith("## "):
            section = ln[3:].strip()
        if section in ("Positive", "Neutral", "Negative") and ln.startswith("|"):
            m = CODE.search(ln)
            if m:
                out.add(m.group(1))
    return out

def recount(s):
    n = len(classified_codes(s))
    s = re.sub(r"\| \*\*Classified here, with a quoted line of evidence\*\* \| \*\*\d+\*\* \|",
               "| **Classified here, with a quoted line of evidence** | **%d** |" % n, s)
    pend = TOTAL - n
    s = re.sub(r"\| Pending \| \*\*[^|]*\*\* \|",
               "| Pending | **%s** |" % ("0 — the index is complete" if pend == 0 else "%d" % pend), s)
    return s, n

def main(argv):
    s = io.open(P, encoding="utf-8").read()
    if argv[1] == "--recount":
        s, n = recount(s)
        io.open(P, "w", encoding="utf-8").write(s)
        print("recount -> %d classified / %d pending of %d" % (n, TOTAL - n, TOTAL))
        return 0
    row = argv[1].strip()
    if row.count("|") != 4:
        raise SystemExit("row must have exactly 4 pipes (3 columns), got %d" % row.count("|"))
    m = CODE.search(row)
    if not m:
        raise SystemExit("row carries no `SE-...` code")
    lines = s.split("\n")
    start = next(i for i, l in enumerate(lines) if l.strip() == "## Neutral")
    end = next(i for i in range(start + 1, len(lines)) if lines[i].startswith("## "))
    last = max(i for i in range(start, end) if lines[i].startswith("|"))
    lines.insert(last + 1, row)
    s = "\n".join(lines)
    s, n = recount(s)
    io.open(P, "w", encoding="utf-8").write(s)
    print("+%s -> %d classified / %d pending of %d (recomputed, not incremented)"
          % (m.group(1), n, TOTAL - n, TOTAL))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
