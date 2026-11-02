# The M.A.W. Stock Ceiling — Five Per Kind, Falling Only Four Ways

**The rule.** A Sorrow Entity supports **up to five M.A.W. pieces of each kind** — five Weapons, five Suits, five Stigmas, fifteen in all. Each record files its own figure in `Maximum Amount`, between one and five, and that figure is the ceiling for that piece.

**Two counts, two questions.** *Three* is how many kinds a set has — a Weapon, a Suit, a Stigma, and no fourth. *Five* is how many copies of one kind the Archive may hold from that source at once. The registry's "up to three pieces" line is a count of kinds. It is not a stock figure and must never be read as one.

**The band word is fixed to the figure.** `1 — Held · 2 — Limited · 3 — Standard · 4 — Stocked · 5 — Abundant`. A record writing *Limited* beside a four has misfiled the word. Correct the word to the figure; never adjust the figure to the word.

**The figure follows the grade, and the filed records say so.** Measured over every record that states both a grade and a figure — **177 of them — the ceiling is the grade's, without a single exception**:

| Grade | α · Minor | β · Moderate | γ · Major | δ · Critical | ω · Catastrophic |
|---|---|---|---|---|---|
| **Ceiling** | **5 — Abundant** | **4 — Stocked** | **3 — Standard** | **2 — Limited** | **1 — Held** |

Read it as *six minus the grade's rank*: a Minor piece is held five at a time, a Catastrophic piece once. The reading is the same one the law already gives — the more potent the piece, the fewer the Archive may hold — and 177 records agree with it independently of each other.

**This is the ceiling, not the count.** The four decrements above still apply, and a piece that has dissolved, gone missing, broken or passed wholly to a holder sits **below** its grade's figure. No record in the archive currently narrates such a loss of its own stock; the two files that carry the words describe the *source entity's* history, not the piece's. Where a loss is later written, the figure drops from the grade ceiling and the band word drops with it.

**The 2026-11-02 fill.** Before that date, **201 of the 852 records filed a figure and 651 did not** — every Stigma among them, because the Stigma records carried `Acquisition Probability` and never the second figure the template asks for. **645 were closed**:

| Source of the figure | Records |
|---|---:|
| **Transcribed** — the number was already printed in the record's own `Maximum / Cost` cell, its inline `**Maximum / Cost:** N / M`, or its compact `max N` | 364 |
| **Derived from the grade** — the record states no figure anywhere, so it takes its grade's ceiling from the table above | 281 |

**Six records filed nothing at the time of the fill**, because they stated neither a grade nor a figure anywhere: `SE-185-D`, `SE-189-D`, `SE-190-D`, `SE-193-D`, `SE-195-D`, `SE-200-D`. They were named here rather than guessed at. **All six were closed on 2026-11-02**, each taking the ceiling its own grade sets, read from its set index — so the field is now **852 of 852**.

**The fill created a divergence, and it has since been closed on evidence rather than by preference.** Measured before the fill, **179 of the 181 records stating both a grade and a figure agreed with the table and two did not**. The fill then transcribed combat-stat cells verbatim, which preserved what each cell said even where it contradicted the record's own grade, leaving **58 records printing a number off their grade's ceiling — 48 above and 10 below**.

Closing them was an editorial judgement this rule declined to make on its own, so the evidence was gathered instead. **Every one of the 58 belongs to an entity whose dossier files a `Potency` line, and that line is Tier-1 canon.** Joined by SECC designation, it confirmed the record's M.A.W. grade in **54 of 58 and contradicted it in none**; the four that could not be joined carried a missing or wrong SECC pointer, and resolved the same way once followed. The grade was therefore the corroborated statement and the figure the derived one, so on 2026-11-02 the figure was corrected to the grade's ceiling with its band word, and 56 set-index `max N` cells moved with it because those indexes repeated the old number.

**This was a correction, not a decrement.** A figure transcribed out of a combat line, against a grade the entity's own dossier attests, was never a filed statement about the Archive's holdings — so moving it destroys no stock on paper, which is the thing this rule exists to prevent. The record's *filed* stock figure, once it is a filing rather than a transcription, is still not to be overwritten.

**Eighty-eight records file a figure but no grade**, and no ceiling can be measured for them; `tools/auditors/check_stock_ceiling.py` reports them by name rather than passing them silently. A record must file a grade for its figure to be checkable, and a new record always does.

Nothing was written above five and nothing at zero.

**The count is stock, not history.** It is not a lifetime total, not a cap on how many have ever existed, and not a running count of extractions. It falls only when a held piece leaves the Archive's hands, and there are exactly four ways that happens:

1. **Dissolution** — the piece loses coherence and returns to its source.
2. **Missing** — the piece is out of the Archive's hands and cannot be accounted for.
3. **Broken** — the piece is destroyed. Damage short of destruction is not breakage.
4. **100% inheritance** — the piece passes wholly to one holder and stops being stock. Two filed forms: *it becomes that agent* (bearer and piece are one object), or *it is Echo-Core bound* (a named Core holds it permanently and it is no longer issuable).

**Fusion is not a fifth event.** A fused piece is still one piece, still counted, still on the record. Fusion is a change of the piece's **state**, not of the Archive's **stock**. Director Majin's *Reaper Hungered* leaves the count because it is **Echo-Core bound**, not because it is fused; the armament table classes it *Fused Singular M.A.W.* A piece fused into an operative who is not an Echo-Core leaves the count under *becomes that agent*. No piece is retired twice and none is retired for being fused alone.

**Everything else leaves the figure standing.** Ordinary issue, a loan between wards, vaulting, a sealed case, ordinary wear, damage short of destruction, corrosion that has not reached takeover, and the bearer's death where the piece survives them — none of it writes the ceiling down. A clerk who lowers a figure because a piece is merely *out* has destroyed stock on paper without destroying a piece.

**Stigmas count the same way and arrive differently.** A Stigma's ceiling is stock like any other's, but it is never manufactured — it is bestowed at random on a successful work, and `Acquisition Probability` governs how often that happens, not how many may exist. Bestowal raises the count toward the ceiling; the same four events lower it. The two figures sit side by side in the record and neither replaces the other: **probability is the rate of arrival, maximum amount is the size of the holding.**

**The figure is required.** A Weapon, Suit or Stigma record that files no `Maximum Amount` is a documentation gap, not an unlimited licence. Where the field is absent the ceiling is still five and the stock is simply unrecorded; the record owes the number.

**Source.** `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md` §I.1 carries the full law and the field table; `TEMPLATES/SE/03`, `04` and `05` carry the row and the short form. Field survey of all 852 `-B/-C/-D` records at the time the rule was written: 199 state a figure (Weapon 98, Suit 101, Stigma 0), 653 do not, and the filed figures run 1 through 5 with no record above five and none at zero — the ceiling holds in the data as well as in the law.
