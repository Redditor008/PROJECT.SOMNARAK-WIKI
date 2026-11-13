# REFERENCE / REGISTRY — The Indexes

**Temporal Anchor:** Year 4,238 · Dawn Initiative · Cycle 1,778

The lookup layer: what exists, what it is called, where it is filed, and what must not be changed. Several tools read from this folder, so a rename here is a tool change too.

| File | Answers | Read by |
|---|---|---|
| [`SORROW_ENTITIES_CATALOG.md`](SORROW_ENTITIES_CATALOG.md) | Which entities exist, by code and category | `tools/label_lint.py` |
| [`ENTITY_DISPOSITION_INDEX.md`](ENTITY_DISPOSITION_INDEX.md) | Where each entity's record sits and how it is disposed | `tools/disp.py`, `tools/ladder.py`, `tools/wikistd.py` |
| [`SOMNARAK_NAME_REGISTRY.md`](SOMNARAK_NAME_REGISTRY.md) | The naming lexicon | Authors |
| [`SOMNARAK_MAIN_ENTITY_PROTECTED_LIST.md`](SOMNARAK_MAIN_ENTITY_PROTECTED_LIST.md) | The entities that may not be rewritten | Everyone |
| [`REGISTRY_MASTER_STATUS.md`](REGISTRY_MASTER_STATUS.md) | Set completion status | Authors |
| [`QUOTE_REGISTER_LEDGER.md`](QUOTE_REGISTER_LEDGER.md) | Which quote belongs to which file | Authors |
| [`SE_APPEARANCE_LEDGER.json`](SE_APPEARANCE_LEDGER.json) | Appearance tracking data | `tools/appearance_progress.py` |
