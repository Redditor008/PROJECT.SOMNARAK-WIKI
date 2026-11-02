"""
textbox.py - plain-text table / box generator with merged cells.

A dependency-free local equivalent of tablesgenerator.com/text_tables.
Standard library only (re, textwrap, unicodedata). Python 3.6+.
Drop this one file anywhere and import it.

WHAT IT IS FOR
--------------
Producing ASCII boxes, panels, and system-interface frames that are
GUARANTEED not to be crooked: every row exactly the same width, corners
closed, rules flush, no stray Unicode.

    +-------------+-------+--------+--------+
    |               Results                 |
    +=============+=======+========+========+
    | Competition |        Contestant       |
    |             +-------+--------+--------+
    |             |  John | Andrea | Robert |
    +-------------+-------+--------+--------+
    | Swimming    |  1:30 |   2:05 |   1:15 |
    +-------------+-------+--------+--------+

QUICK START - declarative
-------------------------
    from textbox import grid, L, U
    print(grid([
        ["Results",     L,            L,        L],
        ["Competition", "Contestant", L,        L],
        [U,             "John",       "Andrea", "Robert"],
        ["Swimming",    "1:30",       "2:05",   "1:15"],
    ], align="lrrr"))

    L = MERGE_LEFT  -> this cell joins the one to its LEFT  (colspan)
    U = MERGE_UP    -> this cell joins the one ABOVE it     (rowspan)
    A bare None is accepted and means MERGE_LEFT.

QUICK START - sequential
------------------------
    from textbox import Table
    t = Table(width=72)
    t.cap()                                   # +--------+
    t.head("ABNORMALITY DETAILS")
    t.pair("LEFT LABEL", "RIGHT VALUE")       # both ends of one row
    t.cap("=")
    t.kv("RISK LEVEL", "ZAYIN")               # aligned key / value
    t.wrap("Long prose is word-wrapped automatically.")
    t.bullet("Bullets wrap too.")
    t.cols([46, 19])                          # declare column widths
    t.col_cap()                               # +------+------+
    t.row(["BASIC INFORMATION  8 PE", "L"])
    t.span_right()                            # left rules, right SPANS down
    t.row(["WORK FAVOR    2 PE EACH", "O"])
    t.col_cap("=")
    t.cap()
    print(t.render())

METHOD SUMMARY
--------------
    cap(ch)              full-width cap, '-' or '='
    rule(ch)             interior full-width rule
    text(s, align)       one content row      align: 'l' 'c' 'r'
    head(s)              heading row
    pair(l, r)           label left, value right
    kv(k, v, keyw)       aligned key/value
    wrap(s, indent)      auto-wrapped paragraph
    bullet(s)            wrapped bullet
    blank()              empty row (discouraged)
    cols([w1, w2, ...])  declare column INNER widths
    auto_cols(n, wts)    split remaining space into n columns
    col_cap(ch)          cap with a junction at each column boundary
    row([cells], align)  one multi-column row
    span_left(text)      left cell holds text, columns right of it rule
    span_right()         left column rules, columns right of it span down
    render()             verified string; raises BoxError on any defect
    emit()               fenced in triple backticks, verified, paste-ready

    grid(data, align, width, header_rule)     declarative table
    check(text)          list of problems; [] means clean
    find_boxes(text)     extract ASCII boxes from a document
    verify_file(path)    CLI-style report
    selftest()           built-in test suite; True if all pass

COLUMN ARITHMETIC
-----------------
For a total width W with n columns, the INNER widths must satisfy:

    sum(inner) + (n + 1) rails + 2n padding == W

cols() raises BoxError with the exact required sum if you get it wrong.
Do not compute this by hand; let the error tell you.

HARD RULES ENFORCED
-------------------
  * every row identical width, or BoxError
  * top and bottom caps must be +...+ of equal length
  * only '+' or '|' may open and close a row
  * printable ASCII only inside frames (Unicode auto-substituted)
  * maximum total width 104 (viewport ceiling); wider is refused
  * a rule row is rebuilt, never padded, so it cannot develop a gap
  * spanning rows are legal: a row MAY start '+' and end '|'

CJK / HANGUL - IMPORTANT
------------------------
Do NOT put wide characters (Korean, Chinese, Japanese) inside a box that
will be read in a browser or chat client. dwidth() treats a wide glyph as
exactly 2 columns, which is the terminal convention, but browser fonts
render them at roughly 1.7x-2.1x, so rows drift and the rails will not
line up even though every row 'measures' correct.

By default wide characters are scrubbed to '?'. Calling set_allow_wide(True)
preserves them, and check() will then REFUSE the box and tell you why.
Correct pattern: romanise inside the box and put the original script in the
prose around it, or use a Markdown table (the renderer aligns those).

WHY EVERY OUTPUT IS VERIFIED
----------------------------
Boxes built by hand fail in three ways that are easy to miss:
  1. arithmetic off by one        -> rows disagree by a single character
  2. fill appended to a rule row  -> a hole appears: "| ===   ===|"
  3. the box is RETYPED by hand   -> transcription adds a space
render() catches 1 and 2. emit() exists to prevent 3: print it, then copy
the output verbatim. Never retype a box.
"""

import re
import textwrap
import unicodedata

# ----------------------------------------------------------------------------
# constants
# ----------------------------------------------------------------------------
DEFAULT_WIDTH = 72
HARD_MAX = 104              # viewport ceiling; beyond this the box wraps
ASCII_OK = set(chr(c) for c in range(0x20, 0x7F))

# Unicode -> ASCII, applied automatically so a stray em dash cannot break a box
SUBS = {
    "\u2014": "-", "\u2013": "-", "\u2212": "-",
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    "\u2026": "...", "\u00a0": " ", "\u2022": "*", "\u00d7": "x",
    "\u2192": "->", "\u2190": "<-", "\u2265": ">=", "\u2264": "<=",
}


# ----------------------------------------------------------------------------
# merge markers for grid()
# ----------------------------------------------------------------------------
class _Merge(object):
    def __init__(self, d): self.d = d
    def __repr__(self): return "<MERGE_%s>" % self.d

MERGE_LEFT = _Merge("LEFT")   # this cell joins the one to its LEFT  (colspan)
MERGE_UP   = _Merge("UP")     # this cell joins the one ABOVE it     (rowspan)
L = MERGE_LEFT                # short aliases
U = MERGE_UP


class BoxError(Exception):
    """Raised when a rendered box fails verification."""


#: when True, CJK/Hangul is preserved and measured by DISPLAY width.
#: when False (default) it is scrubbed to '?' so a box can never go crooked.
ALLOW_WIDE = False


def set_allow_wide(flag=True):
    """Permit CJK / Hangul inside boxes. USE WITH CARE - see the warning.

    !! CJK IN A BOX IS NOT SAFE FOR CHAT / BROWSER RENDERING !!

    dwidth() assumes one wide glyph occupies EXACTLY 2 Latin character
    widths. That is the terminal convention (East_Asian_Width=W), and it
    holds in a true monospace terminal.

    It does NOT hold in a browser or chat client. There the code block is
    rendered with whatever font the client picked, and the Hangul advance
    width is typically ~1.7x to ~2.1x the Latin one, not 2.0x. A row with
    5 wide glyphs then drifts by a different amount than a row with 3, so
    the right rail cannot line up. The box measures perfect and still
    looks crooked - which is exactly the failure this library exists to
    prevent.

    RULE: never put wide characters in a box destined for chat.
    Use romanisation in the box and put the Hangul in the prose around it,
    or use a Markdown table (the renderer handles proportional widths).

    Enable this ONLY for output going to a real terminal or a file the
    reader will open in a fixed-width CJK font.
    """
    global ALLOW_WIDE
    ALLOW_WIDE = bool(flag)


def dwidth(s):
    """Display columns a string occupies (CJK/Hangul count as 2)."""
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1
               for c in str(s))


def wide_report(text):
    """Report wide-character risk for a rendered box.

    A box always contains cap rows (+---+) made only of narrow characters.
    Any wide glyph anywhere in the box therefore drifts against those caps
    in any renderer where a wide glyph is not exactly 2.0x a narrow one -
    which is every browser and chat client.

    There is no safe mixed box. The only safe options are:
      * romanise inside the box, put the Hangul in surrounding prose
      * use a Markdown table, which the renderer aligns proportionally
    """
    wide = [c for c in str(text)
            if unicodedata.east_asian_width(c) in "WF"]
    if not wide:
        return []
    sample = "".join(sorted(set(wide))[:8])
    return [
        "WIDE CHARACTERS IN BOX (%d found: %s)." % (len(wide), sample),
        "  Cap rows are pure ASCII, so these drift against them in any",
        "  browser or chat client (wide advance is ~1.7-2.1x, not 2.0x).",
        "  The box will measure perfect and still look crooked.",
        "  Fix: romanise inside the box, or use a Markdown table.",
    ]


def clean(s):
    """Force a string to safe single-byte ASCII (or wide-safe if enabled)."""
    s = str(s)
    for k, v in SUBS.items():
        s = s.replace(k, v)
    if ALLOW_WIDE:
        # keep printable ASCII plus anything with a defined east-asian width
        return "".join(
            c if (c in ASCII_OK or unicodedata.east_asian_width(c) in "WFNa")
            else "?" for c in s)
    return "".join(c if c in ASCII_OK else "?" for c in s)


def _pad(text, width, align="l"):
    t = clean(text)
    w = dwidth(t)
    if w > width:
        raise BoxError("cell %r needs %d display cols, has %d" % (t, w, width))
    gap = width - w
    if align == "r":
        return " " * gap + t
    if align == "c":
        lo = gap // 2
        return " " * lo + t + " " * (gap - lo)
    return t + " " * gap


# ----------------------------------------------------------------------------
# Table — sequential builder
# ----------------------------------------------------------------------------
class Table(object):
    """Build a box line by line. Geometry is computed, never typed."""

    def __init__(self, width=DEFAULT_WIDTH):
        if width > HARD_MAX:
            raise BoxError("width %d exceeds viewport max %d" % (width, HARD_MAX))
        self.w = width
        self.lines = []
        self._cols = None
        self._open = False          # True once a top cap has been written

    # -- geometry helpers ----------------------------------------------------
    def _inner(self):
        return self.w - 4

    def cols(self, widths):
        """Declare column inner widths for the multi-column section.

        Total check:  '|' + sum(1+w+1) + '|' per boundary  == width
        i.e.  len(widths)+1 rails + sum(w)+2*len(widths) padding == width
        """
        total = len(widths) + 1 + sum(widths) + 2 * len(widths)
        if total != self.w:
            need = self.w - (len(widths) + 1 + 2 * len(widths))
            raise BoxError(
                "columns %s total %d, need %d. Inner widths must sum to %d "
                "(width %d - %d rails - %d padding)"
                % (widths, total, self.w, need, self.w,
                   len(widths) + 1, 2 * len(widths)))
        self._cols = list(widths)
        return self

    def auto_cols(self, n, weights=None):
        """Split the available space into n columns automatically."""
        avail = self.w - (n + 1) - 2 * n
        if weights:
            tot = float(sum(weights))
            ws = [max(1, int(avail * x / tot)) for x in weights]
        else:
            ws = [avail // n] * n
        ws[-1] += avail - sum(ws)
        return self.cols(ws)

    # -- full-width elements -------------------------------------------------
    def cap(self, ch="-"):
        """Top or bottom cap: +------+"""
        self.lines.append("+" + ch * (self.w - 2) + "+")
        self._open = True
        return self

    def rule(self, ch="-"):
        """Interior full-width rule, flush to the right rail."""
        self.lines.append("| " + ch * (self.w - 3) + "|")
        return self

    def text(self, s="", align="l"):
        self.lines.append("| " + _pad(s, self._inner(), align) + " |")
        return self

    def head(self, s, align="l"):
        return self.text(s, align)

    def pair(self, left, right):
        """Left-aligned label, right-aligned value, same row."""
        l, r = clean(left), clean(right)
        gap = self._inner() - dwidth(l) - dwidth(r)
        if gap < 1:
            raise BoxError(
                "pair needs >=1 space between halves: %r + %r = %d cols, "
                "inner width %d" % (l, r, dwidth(l) + dwidth(r), self._inner()))
        self.lines.append("| " + l + " " * gap + r + " |")
        return self

    def kv(self, key, value, keyw=18):
        return self.text(clean(key).ljust(keyw) + clean(value))

    def wrap(self, s, indent=0, align="l"):
        """Word-wrap a paragraph across as many rows as needed."""
        width = self._inner() - indent
        for line in textwrap.wrap(clean(s), width) or [""]:
            self.text(" " * indent + line, align)
        return self

    def bullet(self, s, marker="-", indent=2):
        width = self._inner() - indent - len(marker) - 1
        parts = textwrap.wrap(clean(s), width) or [""]
        pad = " " * indent
        self.text("%s%s %s" % (pad, marker, parts[0]))
        for p in parts[1:]:
            self.text("%s%s %s" % (pad, " " * len(marker), p))
        return self

    def blank(self):
        """Deliberate empty row. Discouraged: spacer bands look hollow."""
        self.lines.append("|" + " " * (self.w - 2) + "|")
        return self

    # -- multi-column elements ----------------------------------------------
    def col_cap(self, ch="-"):
        """Cap with a junction at every column boundary: +----+----+"""
        self._need_cols()
        self.lines.append(
            "+" + "+".join(ch * (c + 2) for c in self._cols) + "+")
        return self

    def row(self, cells, align=None):
        """One row of the declared columns."""
        self._need_cols()
        if len(cells) != len(self._cols):
            raise BoxError("got %d cells, expected %d"
                           % (len(cells), len(self._cols)))
        al = align or "l" * len(self._cols)
        out = "|"
        for cell, cw, a in zip(cells, self._cols, al):
            out += " " + _pad(cell, cw, a) + " |"
        self.lines.append(out)
        return self

    def span_left(self, text, align="l", ch="-"):
        """LEFT cell holds text and continues; the columns to its right rule.

        Mirrors tablesgenerator's canonical shape:
            | Competition +-------+--------+
        """
        self._need_cols()
        out = "| " + _pad(text, self._cols[0], align) + " +"
        out += "+".join(ch * (c + 2) for c in self._cols[1:]) + "+"
        self.lines.append(out)
        return self

    def span_right(self, ch="-"):
        """LEFT column rules; every column to its right spans downward.

            +------------+            |
        """
        self._need_cols()
        out = "+" + ch * (self._cols[0] + 2) + "+"
        for c in self._cols[1:]:
            out += " " * (c + 2) + "|"
        self.lines.append(out)
        return self

    def vspan(self, left_rows, right_cells, align=None):
        """Left column advances row by row while right columns hold one value.

        left_rows    list of strings, one per physical row
        right_cells  values for the spanning columns, vertically distributed
        """
        self._need_cols()
        n = len(left_rows)
        right = list(right_cells) + [""] * (n - len(right_cells))
        for i, lt in enumerate(left_rows):
            self.row([lt] + [right[i]] if len(self._cols) == 2
                     else [lt] + list(right[i]), align)
            if i < n - 1:
                self.span_right()
        return self

    def _need_cols(self):
        if not self._cols:
            raise BoxError("call cols() or auto_cols() first")

    # -- output --------------------------------------------------------------
    def render(self, verify=True):
        out = "\n".join(self.lines)
        if verify:
            problems = check(out)
            if problems:
                raise BoxError("render failed verification:\n  "
                               + "\n  ".join(problems))
        return out

    def emit(self):
        """Fenced and verified — safe to paste into a message verbatim."""
        return "```\n" + self.render() + "\n```"

    def __str__(self):
        return self.render()


# ----------------------------------------------------------------------------
# grid() — declarative, auto-width, merged cells
# ----------------------------------------------------------------------------
def grid(data, align=None, width=None, pad=1, header_rule=True,
         min_col=3, style="-"):
    """Render a 2-D list as a bordered table with merged cells.

    data   list of rows; each cell is a string, or None to merge with the
           cell above (rowspan) or to the left (colspan)
    align  per-column string of l/c/r, e.g. "lrr"
    width  total target width; omit to size to content
    """
    if not data:
        raise BoxError("grid() got no rows. Pass a list of rows, "
                       "e.g. grid([['a','b'],['c','d']])")
    for i, r in enumerate(data):
        if r is None:
            raise BoxError("grid() row %d is None. Use a list of cells, "
                           "e.g. ['a','b']" % i)
        if not hasattr(r, "__iter__") or isinstance(r, str):
            raise BoxError("grid() row %d must be a list of cells, got %r"
                           % (i, type(r).__name__))
        if len(r) == 0:
            raise BoxError("grid() row %d is empty. Every row needs at "
                           "least one cell." % i)

    def _norm(c):
        if c is MERGE_LEFT or c is MERGE_UP:
            return c
        if c is None:
            return MERGE_LEFT          # back-compat: bare None means merge-left
        return clean(c)
    rows = [[_norm(c) for c in r] for r in data]
    # A merge marker in column 0 cannot mean "join the cell to my left" -
    # there is none. It can only mean "join the cell above". Promote it so
    # bare None keeps working in rowspan position.
    for r in rows:
        if r and r[0] is MERGE_LEFT:
            r[0] = MERGE_UP
    ncol = max(len(r) for r in rows)
    for r in rows:
        r.extend([""] * (ncol - len(r)))

    # resolve horizontal merges: a None takes the span of the cell left of it
    span = [[1] * ncol for _ in rows]
    for ri, r in enumerate(rows):
        ci = 0
        while ci < ncol:
            if r[ci] is not None:
                j = ci + 1
                while j < ncol and r[j] is None and ri == 0:
                    j += 1
                ci += 1
            else:
                ci += 1

    # column widths from content that does not span
    def _is_m(x): return isinstance(x, _Merge)
    cw = [min_col] * ncol
    for ri, r in enumerate(rows):
        for ci, cell in enumerate(r):
            if cell and not _is_m(cell):
                nxt = ci + 1
                spans = 1
                while nxt < ncol and r[nxt] is MERGE_LEFT:
                    spans += 1
                    nxt += 1
                if spans == 1:
                    cw[ci] = max(cw[ci], dwidth(cell))
    for ri, r in enumerate(rows):
        for ci, cell in enumerate(r):
            if cell and not _is_m(cell):
                spans = 1
                nxt = ci + 1
                while nxt < ncol and r[nxt] is MERGE_LEFT:
                    spans += 1
                    nxt += 1
                if spans > 1:
                    have = sum(cw[ci:ci + spans]) + (spans - 1) * (2 * pad + 1)
                    if dwidth(cell) > have:
                        cw[ci + spans - 1] += dwidth(cell) - have

    if width:
        cur = sum(cw) + (ncol + 1) + 2 * pad * ncol
        if cur < width:
            cw[-1] += width - cur
        elif cur > width:
            raise BoxError("content needs %d cols, width %d given" % (cur, width))

    al = (align or "l" * ncol)
    al = (al + "l" * ncol)[:ncol]

    def cap_line(ch, mask=None):
        s = "+"
        for ci in range(ncol):
            joint = True if mask is None else mask[ci]
            s += (ch if joint else " ") * (cw[ci] + 2 * pad)
            s += "+" if (ci == ncol - 1 or mask is None or mask[ci] or mask[ci + 1]
                         if mask else True) else "|"
        return s

    out = ["+" + "+".join(ch_ * (c + 2 * pad) for ch_, c
                          in zip([style] * ncol, cw)) + "+"]
    for ri, r in enumerate(rows):
        line = "|"
        ci = 0
        while ci < ncol:
            cell = r[ci]
            if cell is MERGE_UP:
                # vertical merge: blank, no rule above handled by cap logic
                line += " " * (cw[ci] + 2 * pad) + "|"
                ci += 1
                continue
            spans = 1
            nxt = ci + 1
            while nxt < ncol and r[nxt] is MERGE_LEFT:
                spans += 1
                nxt += 1
            total = sum(cw[ci:ci + spans]) + (spans - 1) * (2 * pad + 1)
            # a horizontally-merged cell centres over its span, as the site does
            a = "c" if spans > 1 else al[ci]
            line += " " * pad + _pad(cell, total, a) + " " * pad + "|"
            ci += spans
        out.append(line)
        last = (ri == len(rows) - 1)
        if last:
            out.append("+" + "+".join(style * (c + 2 * pad) for c in cw) + "+")
        else:
            nxt_row = rows[ri + 1]
            seg = ""
            # left edge: '|' if the first column continues downward, else '+'
            seg += "|" if nxt_row[0] is MERGE_UP else "+"
            for ci in range(ncol):
                merged_down = nxt_row[ci] is MERGE_UP
                seg += (" " if merged_down else style) * (cw[ci] + 2 * pad)
                nxt_merged = (ci + 1 < ncol and nxt_row[ci + 1] is MERGE_UP)
                if merged_down and nxt_merged:
                    seg += " "
                elif merged_down or nxt_merged:
                    seg += "|" if (merged_down and nxt_merged) else "+"
                else:
                    seg += "+"
            out.append(seg)
            if header_rule and ri == 0:
                out[-1] = "+" + "+".join("=" * (c + 2 * pad) for c in cw) + "+"

    res = "\n".join(out)
    probs = check(res)
    if probs:
        raise BoxError("grid failed verification:\n  " + "\n  ".join(probs))
    return res


# ----------------------------------------------------------------------------
# verification
# ----------------------------------------------------------------------------
def check(text, max_width=HARD_MAX):
    """Return a list of problems. Empty list means the box is safe."""
    lines = [l for l in text.split("\n") if l.startswith(("+", "|"))]
    p = []
    if not lines:
        return ["no box rows found"]

    p.extend(wide_report(text))

    widths = {dwidth(l) for l in lines}
    if len(widths) > 1:
        widest = max(widths)
        p.append("CROOKED: display widths %s" % sorted(widths))
        for i, l in enumerate(lines):
            if dwidth(l) != widest:
                p.append("row %d: width %d (%+d) | %s"
                         % (i + 1, dwidth(l), dwidth(l) - widest, l[:48]))

    if not (lines[0].startswith("+") and lines[0].endswith("+")):
        p.append("top cap must be +...+")
    if not (lines[-1].startswith("+") and lines[-1].endswith("+")):
        p.append("bottom cap must be +...+")
    if dwidth(lines[0]) != dwidth(lines[-1]):
        p.append("cap widths differ: %d vs %d"
                 % (dwidth(lines[0]), dwidth(lines[-1])))

    for i, l in enumerate(lines):
        if l[0] not in "+|" or l[-1] not in "+|":
            p.append("row %d: must open and close with + or |" % (i + 1))
        bad = sorted({c for c in l if c not in ASCII_OK}) if not ALLOW_WIDE else []
        if bad:
            p.append("row %d: non-ASCII %s"
                     % (i + 1, " ".join("%r" % c for c in bad[:4])))
        if dwidth(l) > max_width:
            p.append("row %d: %d cols exceeds %d" % (i + 1, dwidth(l), max_width))
        # ragged interior rule: fill stops before the right rail
        st = l.strip()
        if (set(st) <= set("+-=| ") and ("-" in st or "=" in st)
                and st.startswith("|") and st.endswith("|")):
            inner = st[1:-1]
            if inner.strip() and inner.endswith(" "):
                p.append("row %d: rule stops %d short of the rail"
                         % (i + 1, len(inner) - len(inner.rstrip())))
    return p


def find_boxes(text):
    """Extract ASCII boxes from a document.

    Only runs that OPEN with a '+' cap count. A Markdown table starts with '|'
    and uses |---|---| delimiters; it is a different construct whose alignment
    the renderer handles, and scanning it as a box produces pure noise.
    """
    lines = text.split("\n")
    blocks, cur = [], []
    for l in lines:
        st = l.strip()
        starts_cap = st.startswith("+") and set(st) <= set("+-=| ")
        if not cur:
            if starts_cap:
                cur = [l]
        elif l.startswith(("+", "|")):
            cur.append(l)
        else:
            blocks.append("\n".join(cur)); cur = []
    if cur:
        blocks.append("\n".join(cur))
    # keep only runs that both open and close on a '+' cap
    out = []
    for b in blocks:
        rows = b.split("\n")
        if len(rows) >= 2 and rows[0].startswith("+") and rows[-1].startswith("+"):
            out.append(b)
    return out


def verify_file(path):
    txt = open(path, encoding="utf-8").read()
    blocks = find_boxes(txt)
    bad = 0
    for i, b in enumerate(blocks, 1):
        pr = check(b)
        if pr:
            bad += 1
            print("BOX %d:" % i)
            for x in pr:
                print("   " + x)
    print("%s: %d box(es), %d with defects" % (path, len(blocks), bad))
    return bad




# ----------------------------------------------------------------------------
# emit — the anti-transcription guard
# ----------------------------------------------------------------------------
def emit(*boxes):
    """Verify boxes and return them fenced, ready to paste VERBATIM.

    Never retype a box into a message. Print this and copy the output.
    A box that fails verification is not emitted at all.
    """
    out = []
    for i, b in enumerate(boxes, 1):
        s = b.render() if hasattr(b, "render") else str(b)
        pr = check(s)
        if pr:
            raise BoxError("box %d unsafe to paste:\n  %s" % (i, "\n  ".join(pr)))
        out.append("```\n" + s + "\n```")
    return "\n\n".join(out)


def selftest():
    """Run the built-in suite. Returns True if everything passes."""
    ok = True

    # canonical tablesgenerator example
    g = grid([["Results", None, None, None],
              ["Competition", "Contestant", None, None],
              [None, "John", "Andrea", "Robert"],
              ["Swimming", "1:30", "2:05", "1:15"]], align="lrrr")
    if len({len(l) for l in g.split("\n")}) != 1:
        print("FAIL: grid widths differ"); ok = False

    # builder with spanning column
    t = Table(72)
    t.cap().head("X").cap("=")
    t.cols([46, 19]).col_cap()
    t.row(["a", "L"]).span_right().row(["b", "O"])
    t.col_cap().cap()
    if len({len(l) for l in t.render().split("\n")}) != 1:
        print("FAIL: table widths differ"); ok = False

    # refusals
    for fn in (lambda: Table(30).cap().text("x" * 40).cap().render(),
               lambda: Table(72).cols([10, 10]),
               lambda: Table(200)):
        try:
            fn(); print("FAIL: bad input accepted"); ok = False
        except BoxError:
            pass

    # unicode scrub
    v = Table(40); v.cap().text("a\u2014b\u201cc\u201d").cap()
    if any(ord(c) > 126 for c in v.render()):
        print("FAIL: unicode survived"); ok = False

    # detector still bites
    if not check("+----+\n| ab |\n| a |\n+----+"):
        print("FAIL: crooked box passed"); ok = False

    # MERGE_LEFT must NOT blank the rule above its row (2026-08-25 bug)
    g2 = grid([["A", "B", "C"],
               ["FOOTER", MERGE_LEFT, "end"]])
    seg = g2.split("\n")[-3]
    if " " in seg.strip("+-="):
        print("FAIL: merge-left blanked the rule above it"); ok = False

    # MERGE_UP must still carry the rail downward
    g3 = grid([["grp", "a"], [MERGE_UP, "b"]])
    if "|" not in g3.split("\n")[3]:
        print("FAIL: merge-up lost its rail"); ok = False

    # any wide glyph in a box must be refused, even with ALLOW_WIDE on:
    # cap rows are pure ASCII so drift is unavoidable in a browser
    set_allow_wide(True)
    try:
        try:
            grid([["\ud55c\uae00", "x"], ["ab", "y"]])
            print("FAIL: wide-char box accepted"); ok = False
        except BoxError:
            pass
    finally:
        set_allow_wide(False)

    # default mode must still scrub wide glyphs
    gs = grid([["\ud55c\uae00", "x"]])
    if any(ord(c) > 126 for c in gs):
        print("FAIL: wide glyph survived default mode"); ok = False

    print("selftest: %s" % ("ALL PASS" if ok else "FAILURES"))
    return ok


# ----------------------------------------------------------------------------
# command line
# ----------------------------------------------------------------------------
def _cli(argv):
    args = [a for a in argv[1:]]

    if not args or args[0] in ("-h", "--help", "help"):
        print(__doc__)
        print("COMMAND LINE")
        print("------------")
        print("  python3 textbox.py FILE [FILE...]   verify boxes in files")
        print("  python3 textbox.py --selftest       run the built-in suite")
        print("  python3 textbox.py --demo           print example output")
        print("  python3 textbox.py --help           this message")
        return 0

    if args[0] in ("--selftest", "-t", "selftest"):
        return 0 if selftest() else 1

    if args[0] in ("--demo", "-d", "demo"):
        print(grid([
            ["Results",     L,            L,        L],
            ["Competition", "Contestant", L,        L],
            [U,             "John",       "Andrea", "Robert"],
            ["Swimming",    "1:30",       "2:05",   "1:15"],
        ], align="lrrr"))
        print()
        t = Table(56)
        t.cap().head("SYSTEM PANEL").pair("STATUS", "NOMINAL").cap("=")
        t.cols([34, 15]).col_cap()
        t.row(["SUBSYSTEM", "STATE"]).col_cap("=")
        rows = [("POWER GRID", "O"), ("COOLANT LOOP", "K")]
        for i, (a, b) in enumerate(rows):
            t.row([a, b])
            if i < len(rows) - 1:
                t.span_right()
        t.col_cap("=").cap()
        print(t.render())
        return 0

    bad = 0
    for path in args:
        if path.startswith("-"):
            print("unknown option %r - try --help" % path)
            return 2
        try:
            bad += verify_file(path)
        except IOError:
            print("cannot read %r" % path)
            return 2
    return 1 if bad else 0


if __name__ == "__main__":
    import sys
    sys.exit(_cli(sys.argv))
