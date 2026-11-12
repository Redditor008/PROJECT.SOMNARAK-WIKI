# The Gate Register

**What this is.** Every gate `tools/gate.sh` runs, numbered by **the order the build runs them**.
That is the only definition that cannot drift: the number is a position, the file is the identity.

**Why it exists.** Until batch 213 the numbers were assigned ad hoc and never registered, so
`gate 92` was claimed by two different scripts and `gate 93` by two more — in the same folder, cited
by different rules. A number that two gates answer to is not a number.

**How to cite a gate.** Write the script name; add the number only if it matches this table.
`check_gate_numbers.py` (gate 49) fails the build on any citation that disagrees.

**Numbering history.** Numbers used before batch 213 (79–94 in the register) were assigned by hand
and are superseded by this table. Where a rule or an order cites one, it now cites the number below.

| gate | script | passes on |
|---|---|---|
| **1** | `tools/check_box_symmetry.py` | `RESULT: PASSED` |
| **2** | `tools/audit_lore_archive.py` | `OVERALL LORE HEALTH: PASS` |
| **3** | `tools/timeline_lint.py` | `[PASS] 0 timeline contradictions` |
| **4** | `tools/seam_lint.py` | `[PASS] 0 semantic seams` |
| **5** | `tools/check_links.py` | `BROKEN TOTAL: 0` |
| **6** | `tools/label_lint.py` | `[PASS] 0 label or code-tag violations found!` |
| **7** | `tools/check_stat_bands.py` | `OVERALL STAT BANDS: PASS` |
| **8** | `tools/text_box_double_checker.py` | `RESULT: PASSED` |
| **9** | `tools/check_box_geometry.py` | `RESULT: PASS (0 crooked boxes)` |
| **10** | `tools/section_logic.py` | `SECTION LOGIC: PASS` |
| **11** | `tools/auditors/compare_conversion_guide.py` | `RESULT: PASS` |
| **12** | `tools/auditors/check_stock_ceiling.py` | `RESULT: PASS` |
| **13** | `tools/auditors/check_boilerplate.py` | `RESULT: PASS` |
| **14** | `tools/auditors/check_event_claims.py` | `RESULT: PASS` |
| **15** | `tools/auditors/check_dossier_consistency.py` | `RESULT: PASS` |
| **16** | `tools/auditors/check_sourcing.py` | `RESULT: PASS` |
| **17** | `tools/auditors/check_set_agreement.py` | `RESULT: PASS` |
| **18** | `tools/auditors/check_citations.py` | `RESULT: PASS` |
| **19** | `tools/auditors/check_world_purity.py` | `RESULT: PASS` |
| **20** | `tools/auditors/check_gauge_chain.py` | `RESULT: PASS` |
| **21** | `tools/auditors/check_appearance_dupe.py` | `RESULT: PASS` |
| **22** | `tools/auditors/check_form_line.py` | `RESULT: PASS` |
| **23** | `tools/auditors/check_ai_prose.py` | `RESULT: PASS` |
| **24** | `tools/auditors/check_tale_register.py` | `RESULT: PASS` |
| **25** | `tools/auditors/check_entity_links.py` | `RESULT: PASS` |
| **26** | `tools/auditors/check_mutual_interactions.py` | `RESULT: PASS` |
| **27** | `tools/auditors/check_slot_templates.py` | `RESULT: PASS` |
| **28** | `tools/auditors/check_series_counts.py` | `RESULT: PASS` |
| **29** | `tools/auditors/check_sentence_starts.py` | `RESULT: PASS` |
| **30** | `tools/auditors/check_ratio_basis.py` | `RESULT: PASS` |
| **31** | `tools/auditors/check_work_response.py` | `RESULT: PASS` |
| **32** | `tools/auditors/check_relic_work_types.py` | `RESULT: PASS` |
| **33** | `tools/auditors/check_relic_interaction_damage.py` | `RESULT: PASS` |
| **34** | `tools/auditors/check_relic_gauge.py` | `RESULT: PASS` |
| **35** | `tools/auditors/check_work_preference.py` | `RESULT: PASS` |
| **36** | `tools/auditors/check_md_tables.py` | `RESULT: PASS` |
| **37** | `tools/auditors/check_barred_prescriptions.py` | `RESULT: PASS` |
| **38** | `tools/auditors/check_special_abnormality.py` | `RESULT: PASS` |
| **39** | `tools/auditors/check_threat_form.py` | `RESULT: PASS` |
| **40** | `tools/auditors/check_consequence_register.py` | `RESULT: PASS` |
| **41** | `tools/auditors/check_work_damage.py` | `RESULT: PASS` |
| **42** | `tools/auditors/check_work_effect.py` | `RESULT: PASS` |
| **43** | `tools/auditors/check_se_effect.py` | `RESULT: PASS` |
| **44** | `tools/auditors/check_rule_index.py` | `RESULT: PASS` |
| **45** | `tools/auditors/check_secc_shape.py` | `RESULT: PASS` |
| **46** | `tools/auditors/check_gate_wiring.py` | `RESULT: PASS` |
| **47** | `tools/auditors/check_section_registry.py` | `RESULT: PASS` |
| **48** | `tools/auditors/check_command_capture.py` | `RESULT: PASS` |
| **49** | `tools/auditors/check_gate_numbers.py` | `RESULT: PASS` |
| **50** | `tools/auditors/check_appearance_contract.py` | `RESULT: PASS` |
| **51** | `tools/auditors/check_backstory_reader.py` | `RESULT: PASS` |
| **52** | `tools/auditors/check_echo_backstory.py` | `RESULT: PASS` |
| **53** | `tools/auditors/check_backstory_appearance.py` | `RESULT: PASS` |
| **54** | `tools/auditors/check_backstory_gloss.py` | `RESULT: PASS` |
| **55** | `tools/auditors/check_title_register.py` | `RESULT: PASS` |
| **56** | `tools/auditors/check_scene_stamps.py` | `RESULT: PASS` |
