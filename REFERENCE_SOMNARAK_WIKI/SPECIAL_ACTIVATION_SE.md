# Special Activation SE — the counter does not decide the reaction

Counted 2026-10-26 over the authoritative 301-dossier ledger corpus (`SE_APPEARANCE_LEDGER.json` `dossiers[].path`), at commit `1d9ab46`.

**Answer: 153 of 301 SEs (50.8%) are Special Activation** — they have **no Breach Behavior section and no breach counter**. How they react is set by a trigger, a channel, an event-in-place, or a standing condition, not by filling a Sorrow Gauge breach counter.

## Method (structural, reproducible)

A dossier counts as Special Activation when its behavior block is one of the following instead of `## Breach Behavior`:

| Structure | Count | Meaning |
|---|---:|---|
| `## Activation Behavior` (no breach section) | 78 | Trigger/channel activation — touch, use, listening, stated conditions |
| `## Containment Event Behavior` (no breach section) | 41 | Event in place — transformation/corruption/expansion where it stands (1 dossier carries both blocks) |
| `## Expansion Behavior` (non-breaching manifestation in place) | 35 | Condition-triggered growth; 34 of 35 state non-breaching / no breach counter in text |
| **Total (union)** | **153** | |

The other **148** dossiers carry `## Breach Behavior` — the counter matters. Borderlines inside that group, **not** counted above: 14 are Transform-type (they transform in place rather than escape, e.g. Kind Healer's Shadow), and 17 carry non-breaching/no-counter wording despite a breach section (internal tension, preserved as found).

Strictest wording subsets across the corpus: **117** files state "no breach counter" in so many words; **113** say non-breaching; **4** state gauge-independence explicitly: `C-IIIγ-904`, `C-IIα-081`, `C-Vδ-111`, `O-IIβ-301` (The Final Door among them: "the order does not depend on the gauge reading").

## The 153 Special Activation designations

**Activation Behavior (78):** `C-IIIβ-015`, `C-IIIβ-016`, `C-IIIβ-036`, `C-IIIβ-072`, `C-IIIβ-275`, `C-IIIγ-044`, `C-IIIγ-088`, `C-IIIγ-102`, `C-IIIγ-115`, `C-IIIγ-120`, `C-IIIγ-195`, `C-IIIγ-300`, `C-IIIγ-373`, `C-IIIγ-609`, `C-IIIγ-891`, `C-IIIγ-902`, `C-IIIγ-948`, `C-IIα-062`, `C-IIα-081`, `C-IIβ-048`, `C-IIβ-051`, `C-IIβ-054`, `C-IIβ-102`, `C-IIβ-135`, `C-IIβ-170`, `C-IIβ-210`, `C-IIβ-280`, `C-IIβ-290`, `C-IIβ-310`, `C-IIβ-340`, `C-IVγ-176`, `C-IVγ-240`, `C-IVγ-946`, `C-IVδ-001`, `C-IVδ-219`, `C-IVδ-222`, `C-IVδ-252`, `C-IVδ-668`, `C-Iα-114`, `C-Iα-236`, `C-Iα-329`, `C-Iα-779`, `C-Iα-884`, `C-Vδ-111`, `C-Vδ-290`, `N-IIIβ-156`, `N-IIIβ-160`, `N-IIIβ-200`, `N-IIIγ-160`, `N-IIIγ-308`, `N-IIIγ-874`, `N-IIβ-250`, `N-IIβ-319`, `N-IIβ-488`, `N-IIβ-560`, `N-IIβ-778`, `N-IIβ-801`, `N-IIγ-903`, `N-IVδ-641`, `N-IVδ-852`, `N-Iα-518`, `N-Iα-686`, `N-Iα-785`, `O-IIIγ-369`, `O-IIIγ-412`, `O-IIIγ-476`, `O-IIIγ-651`, `O-IIβ-757`, `O-IIβ-922`, `O-IVδ-115`, `O-IVδ-168`, `O-IVδ-515`, `O-IVδ-851`, `O-Iα-340`, `O-Iα-643`, `O-Iα-709`, `O-Iα-794` plus the one dual-block dossier listed under Event.

**Containment Event Behavior (41):** `C-IIIγ-021`, `C-IIIγ-190`, `C-IIIγ-248`, `C-IIIγ-448`, `C-IIβ-055`, `C-IIβ-235`, `C-IIβ-565`, `C-IIβ-716`, `C-IIβ-782`, `C-IVγ-073`, `C-IVδ-106`, `C-IVδ-125`, `C-IVδ-200`, `C-IVδ-220`, `C-IVδ-230`, `C-IVδ-249`, `C-IVδ-250`, `C-IVδ-503`, `C-IVδ-823`, `C-IVδ-869`, `C-IVδ-976`, `C-Iα-000`, `C-Iα-300`, `C-Iα-392`, `C-Iα-965`, `C-Vδ-949`, `N-IIIβ-077`, `N-IIIβ-1056`, `N-IIIβ-155`, `N-IIIγ-127`, `N-IIIγ-407`, `N-IIIγ-409`, `N-IIIγ-447`, `N-IIIγ-505`, `N-IIIγ-589`, `N-IIIγ-954`, `N-IIα-125`, `N-IIα-215`, `N-Vω-1055`, `O-IIIγ-1052`, `O-IVγ-1053`

**Expansion Behavior / manifestation in place (35):** `C-IIIγ-140`, `C-IIIγ-180`, `C-IIIγ-649`, `C-IIβ-100`, `C-IIβ-185`, `C-IIβ-240`, `C-IIβ-245`, `C-IIβ-250`, `C-IVγ-180`, `C-IVγ-270`, `C-IVδ-092`, `C-IVδ-193`, `C-IVδ-251`, `C-IVδ-260`, `C-IVδ-763`, `C-IVδ-767`, `C-IVω-001`, `C-Iα-011`, `C-Iα-150`, `C-Iα-175`, `C-Iα-240`, `C-Vγ-225`, `C-Vγ-260`, `C-Vγ-320`, `N-IIβ-270`, `N-IIβ-456`, `N-IIβ-627`, `N-IVδ-157`, `N-IVδ-821`, `N-Iα-459`, `O-IIIγ-617`, `O-IIβ-677`, `O-IIγ-007`, `O-IVδ-909`, `O-Iα-169`

*Scan script and raw table were session artifacts (`/tmp/special_activation_scan.json`); recount any time by scanning ledger paths for the three behavior-block headers above.*
