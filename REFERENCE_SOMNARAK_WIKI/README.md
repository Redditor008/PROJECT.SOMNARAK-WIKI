# REFERENCE_SOMNARAK_WIKI — The Editorial Layer

**Temporal Anchor:** Year 4,238 · Dawn Initiative · Cycle 1,778

Everything in this directory is out-of-world. It governs, measures, indexes or audits the canon in [`SOMNARAK-WORLD/`](../SOMNARAK-WORLD/README.md); none of it is narrated from inside the universe.

The folder is branched by **purpose**, so a search starts from the kind of question being asked.

| Branch | Answers | Files |
|---|---|---|
| [`RULES/`](RULES/README.md) | *What is forbidden?* Binding rule documents R-06 through R-36 | 37 |
| [`GUIDES/`](GUIDES/README.md) | *How is it written?* Structure, standards, quoting, activation, M.A.W. design | 16 |
| [`REGISTRY/`](REGISTRY/README.md) | *What exists and what is it called?* Catalogs, disposition index, naming lexicon, ledgers | 7 |
| [`AUDITS/`](AUDITS/README.md) | *What was checked, and what did it find?* Audit records and progress ledgers | 10 |
| [`RESEARCH/`](RESEARCH/README.md) | *What was compared?* Comparative studies and Project Moon research | 9 |
| `SE_APPEARANCE_REVIEWS/` | *What does each file look like, line by line?* Per-file appearance reviews | 692 |

## Where To Start

1. **Writing a file:** [`GUIDES/SE_DOC_STRUCTURES.md`](GUIDES/SE_DOC_STRUCTURES.md), then the matching template in [`TEMPLATES/`](../TEMPLATES/README.md).
2. **Checking a file:** [`RULES/`](RULES/README.md) for the binding rule, then `bash tools/gate.sh` for the mechanical ones.
3. **Finding a file:** [`REGISTRY/SORROW_ENTITIES_CATALOG.md`](REGISTRY/SORROW_ENTITIES_CATALOG.md) and [`REGISTRY/ENTITY_DISPOSITION_INDEX.md`](REGISTRY/ENTITY_DISPOSITION_INDEX.md).
4. **Understanding why a rule exists:** the audit or comparative study in [`AUDITS/`](AUDITS/README.md) or [`RESEARCH/`](RESEARCH/README.md) that produced it.

## Note On Historical Figures

Some documents in `AUDITS/` and `RESEARCH/` record counts from earlier phases — 284 entities, 529 dossiers, 1,196 M.A.W. records. They are dated evidence and are not updated. For current figures read [`CANONICAL_METRICS.md`](../CANONICAL_METRICS.md), which is generated from the tree.
