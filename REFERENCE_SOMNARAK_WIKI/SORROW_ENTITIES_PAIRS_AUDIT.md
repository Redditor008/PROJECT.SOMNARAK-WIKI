# Sorrow Entities Paired Files & Variant Audit

**Audit Scope:** `REFERENCE_SOMNARAK_WIKI/LORE or REFERANCE/01_Sorrow_Entities/`  
**Total Tracked Entity Files:** 529 dossiers  
**Unique Entity Codes:** 287 canonical entities  
**Codes with Multiple File Variants:** 241 codes  

---

## 1. Executive Summary

In `01_Sorrow_Entities/`, 241 entity codes exist as multiple files. This duplication arose from:
1. **Article Prefix Variations (52 pairs):** One file contains a leading `The_` (e.g. `The_Debt_Eater`) while its sibling does not (`Debt_Eater`).
2. **Alternative English Translations (189 pairs):** Independent English renderings of the same Korean concept (e.g. `Crucible` vs `Rage_Forge` for `분노의_용광로`).
3. **Multi-Draft Sets (1 triple):** `SE-N-IIβ-919` contains three iterations (`Ancestral_Bell-Time`, `Ancestral_Hour`, `Passing_Bell`).

### Data Quality Rectifications
- **Regex Collision Fixed:** In `SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md`, line 84 previously contained an automated search-replace artifact (`The The_Debt_Eatered Ledger`). This has been corrected back to the canonical `The Devoured Ledger`.

---

## 2. Canonical Resolution Rule

When determining which variant to cite in codices or armory references:
- **Cross-Reference Authority:** Check `M.A.W. Codex_Set Registry/`. The folder naming used in the M.A.W. registry represents the established editorial canon.
- **Korean Designation is Supreme:** If English codenames differ, the Korean title (e.g. `빚을 먹는 자`, `분노의 용광로`) is the permanent anchor.

---

## 3. Comprehensive Master Pairs Matrix

| Entity Code | Number of Variants | Variant Files & File Sizes | Recommended Canonical Variant |
|---|:---:|---|---|
| `SE-C-Iα-000` | **2** | `SE-C-Iα-000_Kind_Echo_친절한_메아리.md` (31,743 bytes)<br>`SE-C-Iα-000_The_Kind_Echo_친절한_메아리.md` (32,081 bytes) | `SE-C-Iα-000_Kind_Echo_친절한_메아리.md` |
| `SE-C-IVδ-001` | **2** | `SE-C-IVδ-001_Orphaned_Bell_고아의_종.md` (37,954 bytes)<br>`SE-C-IVδ-001_The_Orphaned_Bell_고아의_종.md` (38,294 bytes) | `SE-C-IVδ-001_The_Orphaned_Bell_고아의_종.md` |
| `SE-C-Vδ-002` | **2** | `SE-C-Vδ-002_Grieving_Colossus_슬픔의_거인.md` (31,460 bytes)<br>`SE-C-Vδ-002_The_Grieving_Colossus_슬픔의_거인.md` (31,794 bytes) | `SE-C-Vδ-002_The_Grieving_Colossus_슬픔의_거인.md` |
| `SE-O-Vγ-003` | **2** | `SE-O-Vγ-003_The_Wilderness_Tide_야생의_조수.md` (19,943 bytes)<br>`SE-O-Vγ-003_Wilderness_Tide_야생의_조수.md` (19,859 bytes) | `SE-O-Vγ-003_Wilderness_Tide_야생의_조수.md` |
| `SE-N-IVδ-005` | **2** | `SE-N-IVδ-005_Smothering_Mother_질식하는_어머니.md` (32,248 bytes)<br>`SE-N-IVδ-005_The_Smothering_Mother_질식하는_어머니.md` (32,588 bytes) | `SE-N-IVδ-005_The_Smothering_Mother_질식하는_어머니.md` |
| `SE-O-IIγ-007` | **2** | `SE-O-IIγ-007_Brume_안개.md` (33,044 bytes)<br>`SE-O-IIγ-007_Drift_Fog_drifting_안개.md` (32,850 bytes) | `SE-O-IIγ-007_Brume_안개.md` |
| `SE-C-IVγ-009` | **2** | `SE-C-IVγ-009_Memory_Weaver_기억의_직공.md` (32,328 bytes)<br>`SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md` (32,674 bytes) | `SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md` |
| `SE-C-Iα-011` | **2** | `SE-C-Iα-011_The_Whispering_Walls_속삭이는_벽.md` (32,394 bytes)<br>`SE-C-Iα-011_Whispering_Walls_속삭이는_벽.md` (32,094 bytes) | `SE-C-Iα-011_Whispering_Walls_속삭이는_벽.md` |
| `SE-O-IIIδ-011` | **2** | `SE-O-IIIδ-011_Scar_Walker_흉터의_행자.md` (31,095 bytes)<br>`SE-O-IIIδ-011_The_Scar_Walker_흉터의_행자.md` (31,431 bytes) | `SE-O-IIIδ-011_Scar_Walker_흉터의_행자.md` |
| `SE-C-IIIβ-014` | **2** | `SE-C-IIIβ-014_Debt_Eater_빚을_먹는_자.md` (31,343 bytes)<br>`SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md` (31,653 bytes) | `SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md` |
| `SE-C-IIIβ-015` | **2** | `SE-C-IIIβ-015_Debt_Scale_빚의_저울.md` (33,262 bytes)<br>`SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md` (33,564 bytes) | `SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md` |
| `SE-C-IIIβ-016` | **2** | `SE-C-IIIβ-016_Echo_Compass_메아리_나침반.md` (33,607 bytes)<br>`SE-C-IIIβ-016_The_Echo_Compass_메아리_나침반.md` (33,905 bytes) | `SE-C-IIIβ-016_The_Echo_Compass_메아리_나침반.md` |
| `SE-N-IVβ-019` | **2** | `SE-N-IVβ-019_Inherited_Debt_물려받은_빚.md` (31,211 bytes)<br>`SE-N-IVβ-019_The_Inherited_Debt_물려받은_빚.md` (31,517 bytes) | `SE-N-IVβ-019_The_Inherited_Debt_물려받은_빚.md` |
| `SE-C-IIIγ-021` | **2** | `SE-C-IIIγ-021_Hollow_Choir_빈_합창단.md` (32,353 bytes)<br>`SE-C-IIIγ-021_The_Hollow_Choir_빈_합창단.md` (32,701 bytes) | `SE-C-IIIγ-021_The_Hollow_Choir_빈_합창단.md` |
| `SE-N-Iα-025` | **2** | `SE-N-Iα-025_Silent_Child_조용한_아이.md` (31,039 bytes)<br>`SE-N-Iα-025_The_Silent_Child_조용한_아이.md` (31,345 bytes) | `SE-N-Iα-025_The_Silent_Child_조용한_아이.md` |
| `SE-C-IIIγ-031` | **2** | `SE-C-IIIγ-031_Observing_Bird_지켜보는_새.md` (30,954 bytes)<br>`SE-C-IIIγ-031_The_Observing_Bird_지켜보는_새.md` (31,298 bytes) | `SE-C-IIIγ-031_The_Observing_Bird_지켜보는_새.md` |
| `SE-C-IIIγ-032` | **2** | `SE-C-IIIγ-032_The_Weighting_Bird_재는_새.md` (30,837 bytes)<br>`SE-C-IIIγ-032_Weighting_Bird_재는_새.md` (30,481 bytes) | `SE-C-IIIγ-032_Weighting_Bird_재는_새.md` |
| `SE-C-IIIγ-033` | **2** | `SE-C-IIIγ-033_Guarding_Bird_지키는_새.md` (30,807 bytes)<br>`SE-C-IIIγ-033_The_Guarding_Bird_지키는_새.md` (31,157 bytes) | `SE-C-IIIγ-033_The_Guarding_Bird_지키는_새.md` |
| `SE-N-IIβ-033` | **2** | `SE-N-IIβ-033_Forgotten_Soldier_잊혀진_병사.md` (32,196 bytes)<br>`SE-N-IIβ-033_The_Forgotten_Soldier_잊혀진_병사.md` (32,496 bytes) | `SE-N-IIβ-033_Forgotten_Soldier_잊혀진_병사.md` |
| `SE-C-IIIβ-036` | **2** | `SE-C-IIIβ-036_Cracked_Hourglass_금이_간_모래시계.md` (34,757 bytes)<br>`SE-C-IIIβ-036_The_Cracked_Hourglass_금이_간_모래시계.md` (35,055 bytes) | `SE-C-IIIβ-036_The_Cracked_Hourglass_금이_간_모래시계.md` |
| `SE-C-IVβ-041` | **2** | `SE-C-IVβ-041_Grieving_Maiden_슬픔의_처녀.md` (30,549 bytes)<br>`SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀.md` (30,857 bytes) | `SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀.md` |
| `SE-C-IVβ-042` | **2** | `SE-C-IVβ-042_Angry_Maiden_분노의_처녀.md` (31,444 bytes)<br>`SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀.md` (31,756 bytes) | `SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀.md` |
| `SE-C-IVβ-043` | **2** | `SE-C-IVβ-043_Silent_Maiden_침묵의_처녀.md` (31,019 bytes)<br>`SE-C-IVβ-043_The_Silent_Maiden_침묵의_처녀.md` (31,341 bytes) | `SE-C-IVβ-043_The_Silent_Maiden_침묵의_처녀.md` |
| `SE-C-IIIγ-044` | **2** | `SE-C-IIIγ-044_Broken_Clock_부서진_시계.md` (35,466 bytes)<br>`SE-C-IIIγ-044_The_Broken_Clock_부서진_시계.md` (35,808 bytes) | `SE-C-IIIγ-044_Broken_Clock_부서진_시계.md` |
| `SE-C-IIβ-048` | **2** | `SE-C-IIβ-048_Hums_노래하는_돌.md` (34,767 bytes)<br>`SE-C-IIβ-048_Singing_Stone_노래하는_돌.md` (34,692 bytes) | `SE-C-IIβ-048_Hums_노래하는_돌.md` |
| `SE-C-IIβ-051` | **2** | `SE-C-IIβ-051_Happy_Mask_행복한_가면.md` (33,969 bytes)<br>`SE-C-IIβ-051_The_Happy_Mask_행복한_가면.md` (34,271 bytes) | `SE-C-IIβ-051_The_Happy_Mask_행복한_가면.md` |
| `SE-C-IIβ-054` | **2** | `SE-C-IIβ-054_Empty_Mask_빈_가면.md` (34,290 bytes)<br>`SE-C-IIβ-054_The_Empty_Mask_빈_가면.md` (34,592 bytes) | `SE-C-IIβ-054_The_Empty_Mask_빈_가면.md` |
| `SE-C-IIβ-055` | **2** | `SE-C-IIβ-055_The_Weeping_Statue_우는_조상.md` (30,236 bytes)<br>`SE-C-IIβ-055_Weeping_Statue_우는_조상.md` (29,936 bytes) | `SE-C-IIβ-055_Weeping_Statue_우는_조상.md` |
| `SE-C-IIα-062` | **2** | `SE-C-IIα-062_Forgotten_Market_Stall_잊혀진_가게.md` (34,964 bytes)<br>`SE-C-IIα-062_Night_Peddler_잊혀진_가게.md` (35,041 bytes) | `SE-C-IIα-062_Forgotten_Market_Stall_잊혀진_가게.md` |
| `SE-C-Iα-071` | **2** | `SE-C-Iα-071_Kind_Healer_친절한_치유자.md` (32,172 bytes)<br>`SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md` (32,480 bytes) | `SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md` |
| `SE-C-IVγ-073` | **2** | `SE-C-IVγ-073_Hollow_Knight_빈_기사.md` (31,220 bytes)<br>`SE-C-IVγ-073_The_Hollow_Knight_빈_기사.md` (31,564 bytes) | `SE-C-IVγ-073_The_Hollow_Knight_빈_기사.md` |
| `SE-N-IIIβ-077` | **2** | `SE-N-IIIβ-077_Memory_Thief_기록_도둑.md` (30,847 bytes)<br>`SE-N-IIIβ-077_The_Memory_Thief_기록_도둑.md` (31,149 bytes) | `SE-N-IIIβ-077_The_Memory_Thief_기록_도둑.md` |
| `SE-C-IIIγ-081` | **2** | `SE-C-IIIγ-081_Hollow_Saint_빈_성자.md` (29,763 bytes)<br>`SE-C-IIIγ-081_The_Hollow_Saint_빈_성자.md` (30,105 bytes) | `SE-C-IIIγ-081_The_Hollow_Saint_빈_성자.md` |
| `SE-C-IIα-081` | **2** | `SE-C-IIα-081_Broken_Mirror_거울의_조각.md` (34,880 bytes)<br>`SE-C-IIα-081_Honest_Reflection_거울의_조각.md` (35,182 bytes) | `SE-C-IIα-081_Broken_Mirror_거울의_조각.md` |
| `SE-C-IIIγ-088` | **2** | `SE-C-IIIγ-088_Sorrow_Fountain_슬픔의_분수.md` (30,935 bytes)<br>`SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수.md` (31,267 bytes) | `SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수.md` |
| `SE-C-IVγ-091` | **2** | `SE-C-IVγ-091_Lost_Prince_잃어버린_왕자.md` (31,693 bytes)<br>`SE-C-IVγ-091_The_Lost_Prince_잃어버린_왕자.md` (32,033 bytes) | `SE-C-IVγ-091_The_Lost_Prince_잃어버린_왕자.md` |
| `SE-C-IVδ-092` | **2** | `SE-C-IVδ-092_Burning_Library_타오르는_도서관.md` (32,789 bytes)<br>`SE-C-IVδ-092_Pyre_of_Truths_타오르는_도서관.md` (33,017 bytes) | `SE-C-IVδ-092_Pyre_of_Truths_타오르는_도서관.md` |
| `SE-C-IIβ-099` | **2** | `SE-C-IIβ-099_Masked_Dancer_가면_무용수.md` (31,136 bytes)<br>`SE-C-IIβ-099_The_Masked_Dancer_가면_무용수.md` (31,440 bytes) | `SE-C-IIβ-099_The_Masked_Dancer_가면_무용수.md` |
| `SE-C-IIβ-100` | **2** | `SE-C-IIβ-100_Grave_of_Cherry_Blossoms_벚꽃의_무덤.md` (30,553 bytes)<br>`SE-C-IIβ-100_Unsaid_Blossoms_벚꽃의_무덤.md` (30,646 bytes) | `SE-C-IIβ-100_Unsaid_Blossoms_벚꽃의_무덤.md` |
| `SE-C-IIβ-101` | **2** | `SE-C-IIβ-101_Ember_Child_embers_의_아이.md` (30,264 bytes)<br>`SE-C-IIβ-101_Emberling_embers_의_아이.md` (30,452 bytes) | `SE-C-IIβ-101_Emberling_embers_의_아이.md` |
| `SE-C-IIIγ-102` | **2** | `SE-C-IIIγ-102_Dancing_Chains_춤추는_사슬.md` (35,369 bytes)<br>`SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬.md` (35,709 bytes) | `SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬.md` |
| `SE-C-IIβ-102` | **2** | `SE-C-IIβ-102_Frozen_Tear_얼어붙은_눈물.md` (33,084 bytes)<br>`SE-C-IIβ-102_Icedrop_얼어붙은_눈물.md` (33,238 bytes) | `SE-C-IIβ-102_Frozen_Tear_얼어붙은_눈물.md` |
| `SE-C-IVδ-103` | **2** | `SE-C-IVδ-103_Frozen_Veil_얼어붙은_베일.md` (31,327 bytes)<br>`SE-C-IVδ-103_The_Frozen_Veil_얼어붙은_베일.md` (31,651 bytes) | `SE-C-IVδ-103_The_Frozen_Veil_얼어붙은_베일.md` |
| `SE-C-IIIγ-105` | **2** | `SE-C-IIIγ-105_Lonely_Giant_외로운_거인.md` (30,197 bytes)<br>`SE-C-IIIγ-105_The_Lonely_Giant_외로운_거인.md` (30,547 bytes) | `SE-C-IIIγ-105_The_Lonely_Giant_외로운_거인.md` |
| `SE-C-IVδ-106` | **2** | `SE-C-IVδ-106_Broken_Bridge_부서진_다리.md` (30,075 bytes)<br>`SE-C-IVδ-106_I_Alone_Crossed_부서진_다리.md` (30,387 bytes) | `SE-C-IVδ-106_I_Alone_Crossed_부서진_다리.md` |
| `SE-O-Iα-108` | **2** | `SE-O-Iα-108_Animus_떠도는_흔적.md` (29,689 bytes)<br>`SE-O-Iα-108_Wandering_Trace_떠도는_흔적.md` (29,623 bytes) | `SE-O-Iα-108_Animus_떠도는_흔적.md` |
| `SE-C-Vδ-111` | **2** | `SE-C-Vδ-111_Final_Door_마지막_문.md` (34,781 bytes)<br>`SE-C-Vδ-111_The_Final_Door_마지막_문.md` (35,105 bytes) | `SE-C-Vδ-111_The_Final_Door_마지막_문.md` |
| `SE-C-IIIγ-115` | **2** | `SE-C-IIIγ-115_Memory_Well_기억의_우물.md` (30,834 bytes)<br>`SE-C-IIIγ-115_Remembrance_기억의_우물.md` (31,112 bytes) | `SE-C-IIIγ-115_Remembrance_기억의_우물.md` |
| `SE-O-IVδ-115` | **2** | `SE-O-IVδ-115_Broken_Fragment_부서진_파편.md` (33,220 bytes)<br>`SE-O-IVδ-115_Weight_of_All_Owed_부서진_파편.md` (33,540 bytes) | `SE-O-IVδ-115_Broken_Fragment_부서진_파편.md` |
| `SE-O-IIβ-119` | **2** | `SE-O-IIβ-119_Homeless_Sorrow_떠도는_그림자.md` (31,922 bytes)<br>`SE-O-IIβ-119_Wandering_Shadow_떠도는_그림자.md` (31,711 bytes) | `SE-O-IIβ-119_Homeless_Sorrow_떠도는_그림자.md` |
| `SE-C-IIIγ-120` | **2** | `SE-C-IIIγ-120_Rage_Cage_분노의_감옥.md` (32,811 bytes)<br>`SE-C-IIIγ-120_Redcage_분노의_감옥.md` (33,045 bytes) | `SE-C-IIIγ-120_Redcage_분노의_감옥.md` |
| `SE-O-IIIβ-120` | **2** | `SE-O-IIIβ-120_The_Wrath_Flame_분노의_불꽃.md` (29,399 bytes)<br>`SE-O-IIIβ-120_Wrath_Flame_분노의_불꽃.md` (29,099 bytes) | `SE-O-IIIβ-120_The_Wrath_Flame_분노의_불꽃.md` |
| `SE-C-IVδ-125` | **2** | `SE-C-IVδ-125_Dejà_Vu_돌아온_열매.md` (30,044 bytes)<br>`SE-C-IVδ-125_Returning_Fruit_돌아온_열매.md` (29,882 bytes) | `SE-C-IVδ-125_Dejà_Vu_돌아온_열매.md` |
| `SE-N-IIα-125` | **2** | `SE-N-IIα-125_Hollow_Echo_빈_메아리.md` (29,827 bytes)<br>`SE-N-IIα-125_Undersong_빈_메아리.md` (30,001 bytes) | `SE-N-IIα-125_Hollow_Echo_빈_메아리.md` |
| `SE-O-Iα-126` | **2** | `SE-O-Iα-126_Anonym_녹아내린_조각.md` (30,127 bytes)<br>`SE-O-Iα-126_Melting_Shard_녹아내린_조각.md` (30,029 bytes) | `SE-O-Iα-126_Anonym_녹아내린_조각.md` |
| `SE-N-IIIγ-127` | **2** | `SE-N-IIIγ-127_Broken_Mirror_부서진_거울.md` (29,285 bytes)<br>`SE-N-IIIγ-127_Mirror_of_Broken_부서진_거울.md` (29,602 bytes) | `SE-N-IIIγ-127_Mirror_of_Broken_부서진_거울.md` |
| `SE-C-IVγ-130` | **2** | `SE-C-IVγ-130_Crumbling_Saint_무너지는_성자.md` (29,463 bytes)<br>`SE-C-IVγ-130_Deteriorata_무너지는_성자.md` (29,657 bytes) | `SE-C-IVγ-130_Deteriorata_무너지는_성자.md` |
| `SE-C-IIβ-135` | **2** | `SE-C-IIβ-135_Dream_Fragment_꿈의_조각.md` (31,397 bytes)<br>`SE-C-IIβ-135_Rem_꿈의_조각.md` (31,435 bytes) | `SE-C-IIβ-135_Rem_꿈의_조각.md` |
| `SE-C-IIIγ-140` | **2** | `SE-C-IIIγ-140_The_Weeping_Willow_우는_버드나무.md` (31,023 bytes)<br>`SE-C-IIIγ-140_Weeping_Willow_우는_버드나무.md` (30,695 bytes) | `SE-C-IIIγ-140_Weeping_Willow_우는_버드나무.md` |
| `SE-C-IVδ-140` | **2** | `SE-C-IVδ-140_Gavel_철의_판관.md` (29,522 bytes)<br>`SE-C-IVδ-140_Iron_Judge_철의_판관.md` (29,354 bytes) | `SE-C-IVδ-140_Gavel_철의_판관.md` |
| `SE-C-IIIγ-145` | **2** | `SE-C-IIIγ-145_Briar_가시의_정원.md` (32,031 bytes)<br>`SE-C-IIIγ-145_Garden_of_Thorns_가시의_정원.md` (31,961 bytes) | `SE-C-IIIγ-145_Briar_가시의_정원.md` |
| `SE-C-Iα-150` | **2** | `SE-C-Iα-150_Echo_of_Laughter_웃음의_메아리.md` (31,464 bytes)<br>`SE-C-Iα-150_Risus_웃음의_메아리.md` (31,524 bytes) | `SE-C-Iα-150_Risus_웃음의_메아리.md` |
| `SE-O-IVδ-151` | **2** | `SE-O-IVδ-151_Border_Tree_스며든_나무.md` (31,951 bytes)<br>`SE-O-IVδ-151_Spreading_Tree_스며든_나무.md` (31,740 bytes) | `SE-O-IVδ-151_Border_Tree_스며든_나무.md` |
| `SE-N-IIβ-152` | **2** | `SE-N-IIβ-152_Doorway_to_Nowhere_떠도는_문.md` (29,623 bytes)<br>`SE-N-IIβ-152_Wandering_Door_떠도는_문.md` (29,323 bytes) | `SE-N-IIβ-152_Doorway_to_Nowhere_떠도는_문.md` |
| `SE-N-IIIβ-155` | **2** | `SE-N-IIIβ-155_Debt_Collector's_Shadow_추징관의_그림자.md` (29,871 bytes)<br>`SE-N-IIIβ-155_Harbinger_추징관의_그림자.md` (29,873 bytes) | `SE-N-IIIβ-155_Harbinger_추징관의_그림자.md` |
| `SE-N-IIIβ-156` | **2** | `SE-N-IIIβ-156_Deadline_빚의_시계.md` (32,844 bytes)<br>`SE-N-IIIβ-156_Debt_Clock_빚의_시계.md` (32,666 bytes) | `SE-N-IIIβ-156_Deadline_빚의_시계.md` |
| `SE-N-IVδ-157` | **2** | `SE-N-IVδ-157_Sleeping_Sigh_잠든_한숨.md` (30,456 bytes)<br>`SE-N-IVδ-157_Torpor_잠든_한숨.md` (30,603 bytes) | `SE-N-IVδ-157_Torpor_잠든_한숨.md` |
| `SE-N-IVδ-159` | **2** | `SE-N-IVδ-159_Apnea_얼어붙은_한숨.md` (29,506 bytes)<br>`SE-N-IVδ-159_Frozen_Sigh_얼어붙은_한숨.md` (29,340 bytes) | `SE-N-IVδ-159_Apnea_얼어붙은_한숨.md` |
| `SE-N-IIIβ-160` | **2** | `SE-N-IIIβ-160_Debt_Chain_빚의_사슬.md` (32,899 bytes)<br>`SE-N-IIIβ-160_The_Debt_Chain_빚의_사슬.md` (33,197 bytes) | `SE-N-IIIβ-160_The_Debt_Chain_빚의_사슬.md` |
| `SE-N-IIIγ-160` | **2** | `SE-N-IIIγ-160_Broken_Promise_깨진_약속.md` (33,184 bytes)<br>`SE-N-IIIγ-160_Facsimile_깨진_약속.md` (33,362 bytes) | `SE-N-IIIγ-160_Broken_Promise_깨진_약속.md` |
| `SE-C-IVδ-165` | **2** | `SE-C-IVδ-165_Candela_녹아내리는_성자.md` (30,565 bytes)<br>`SE-C-IVδ-165_Melting_Saint_녹아내리는_성자.md` (30,405 bytes) | `SE-C-IVδ-165_Candela_녹아내리는_성자.md` |
| `SE-O-IVδ-168` | **2** | `SE-O-IVδ-168_Collapsed_Trace_무너진_흔적.md` (32,488 bytes)<br>`SE-O-IVδ-168_Quagmire_무너진_흔적.md` (32,590 bytes) | `SE-O-IVδ-168_Quagmire_무너진_흔적.md` |
| `SE-O-Iα-169` | **2** | `SE-O-Iα-169_Atlas_녹슨_기둥.md` (30,703 bytes)<br>`SE-O-Iα-169_Rusted_Pillar_녹슨_기둥.md` (30,613 bytes) | `SE-O-Iα-169_Atlas_녹슨_기둥.md` |
| `SE-C-IIβ-170` | **2** | `SE-C-IIβ-170_Silent_Bell_침묵의_종.md` (32,857 bytes)<br>`SE-C-IIβ-170_Unrung_침묵의_종.md` (32,992 bytes) | `SE-C-IIβ-170_Unrung_침묵의_종.md` |
| `SE-N-IIβ-170` | **2** | `SE-N-IIβ-170_Aphonia_침묵의_비명.md` (28,926 bytes)<br>`SE-N-IIβ-170_Silent_Scream_침묵의_비명.md` (28,810 bytes) | `SE-N-IIβ-170_Aphonia_침묵의_비명.md` |
| `SE-C-IVγ-175` | **2** | `SE-C-IVγ-175_Somnium_꿈의_직공.md` (30,096 bytes)<br>`SE-C-IVγ-175_Weaver_of_Dreams_꿈의_직공.md` (29,990 bytes) | `SE-C-IVγ-175_Somnium_꿈의_직공.md` |
| `SE-C-Iα-175` | **2** | `SE-C-Iα-175_Anger_Underfoot_스며든_흔적.md` (30,643 bytes)<br>`SE-C-Iα-175_Spreading_Trace_스며든_흔적.md` (30,426 bytes) | `SE-C-Iα-175_Anger_Underfoot_스며든_흔적.md` |
| `SE-C-IVγ-176` | **2** | `SE-C-IVγ-176_Dream_Weaver's_Loom_꿈_직공의_베틀.md` (33,486 bytes)<br>`SE-C-IVγ-176_Loom_of_Unlived_Dreams_꿈_직공의_베틀.md` (33,802 bytes) | `SE-C-IVγ-176_Loom_of_Unlived_Dreams_꿈_직공의_베틀.md` |
| `SE-C-IIIγ-180` | **2** | `SE-C-IIIγ-180_Debt_Wall_빚의_벽.md` (31,104 bytes)<br>`SE-C-IIIγ-180_Owed_빚의_벽.md` (31,285 bytes) | `SE-C-IIIγ-180_Owed_빚의_벽.md` |
| `SE-C-IVγ-180` | **2** | `SE-C-IVγ-180_Labyrinth_of_Stolen_Faces_기억의_미로.md` (31,881 bytes)<br>`SE-C-IVγ-180_Memory_Maze_기억의_미로.md` (31,359 bytes) | `SE-C-IVγ-180_Labyrinth_of_Stolen_Faces_기억의_미로.md` |
| `SE-N-IIIγ-184` | **2** | `SE-N-IIIγ-184_Forgotten_Tree_잊혀진_나무.md` (29,826 bytes)<br>`SE-N-IIIγ-184_Redacted_잊혀진_나무.md` (29,950 bytes) | `SE-N-IIIγ-184_Redacted_잊혀진_나무.md` |
| `SE-C-IIβ-185` | **2** | `SE-C-IIβ-185_The_Whispering_Gallery_속삭이는_갤러리.md` (31,055 bytes)<br>`SE-C-IIβ-185_Whispering_Gallery_속삭이는_갤러리.md` (30,763 bytes) | `SE-C-IIβ-185_Whispering_Gallery_속삭이는_갤러리.md` |
| `SE-O-Iα-189` | **2** | `SE-O-Iα-189_Ephemera_번져가는_잔해.md` (29,526 bytes)<br>`SE-O-Iα-189_Fading_Ruin_번져가는_잔해.md` (29,352 bytes) | `SE-O-Iα-189_Ephemera_번져가는_잔해.md` |
| `SE-C-IIIγ-190` | **2** | `SE-C-IIIγ-190_Rage_Statue_분노의_조각상.md` (29,377 bytes)<br>`SE-C-IIIγ-190_The_Rage_Statue_분노의_조각상.md` (29,716 bytes) | `SE-C-IIIγ-190_The_Rage_Statue_분노의_조각상.md` |
| `SE-C-IVδ-193` | **2** | `SE-C-IVδ-193_Rift_사라진_벽.md` (31,007 bytes)<br>`SE-C-IVδ-193_Vanished_Wall_사라진_벽.md` (30,918 bytes) | `SE-C-IVδ-193_Rift_사라진_벽.md` |
| `SE-C-IIIγ-195` | **2** | `SE-C-IIIγ-195_Learned_Your_Face_슬픔의_거울.md` (33,648 bytes)<br>`SE-C-IIIγ-195_Mirror_of_Sorrows_슬픔의_거울.md` (33,378 bytes) | `SE-C-IIIγ-195_Learned_Your_Face_슬픔의_거울.md` |
| `SE-C-IVδ-200` | **2** | `SE-C-IVδ-200_Aegis_문의_수호자.md` (30,283 bytes)<br>`SE-C-IVδ-200_Guardian_of_the_Gate_문의_수호자.md` (30,255 bytes) | `SE-C-IVδ-200_Aegis_문의_수호자.md` |
| `SE-C-IVγ-205` | **2** | `SE-C-IVγ-205_Hollow_Tree_빈_나무.md` (29,128 bytes)<br>`SE-C-IVγ-205_Timber_Maw_빈_나무.md` (29,376 bytes) | `SE-C-IVγ-205_Hollow_Tree_빈_나무.md` |
| `SE-C-IIβ-210` | **2** | `SE-C-IIβ-210_Laughing_Mask_웃는_가면.md` (32,516 bytes)<br>`SE-C-IIβ-210_Levity_웃는_가면.md` (32,590 bytes) | `SE-C-IIβ-210_Laughing_Mask_웃는_가면.md` |
| `SE-N-IIα-215` | **2** | `SE-N-IIα-215_Forgotten_Name_잊혀진_이름.md` (29,801 bytes)<br>`SE-N-IIα-215_Name_No_One_Remembers_잊혀진_이름.md` (30,164 bytes) | `SE-N-IIα-215_Forgotten_Name_잊혀진_이름.md` |
| `SE-C-IVδ-219` | **2** | `SE-C-IVδ-219_Soaking_Shard_솟구친_조각.md` (33,331 bytes)<br>`SE-C-IVδ-219_Splinter_솟구친_조각.md` (33,479 bytes) | `SE-C-IVδ-219_Soaking_Shard_솟구친_조각.md` |
| `SE-C-IVδ-220` | **2** | `SE-C-IVδ-220_Walking_Calendar_세월의_무게.md` (30,347 bytes)<br>`SE-C-IVδ-220_Weight_of_Years_세월의_무게.md` (30,063 bytes) | `SE-C-IVδ-220_Walking_Calendar_세월의_무게.md` |
| `SE-C-IVδ-222` | **2** | `SE-C-IVδ-222_Patina_녹슨_무게.md` (31,390 bytes)<br>`SE-C-IVδ-222_Rusted_Weight_녹슨_무게.md` (31,266 bytes) | `SE-C-IVδ-222_Patina_녹슨_무게.md` |
| `SE-C-Vγ-225` | **2** | `SE-C-Vγ-225_Black_River_슬픔의_강.md` (31,646 bytes)<br>`SE-C-Vγ-225_Sorrow_River_슬픔의_강.md` (31,399 bytes) | `SE-C-Vγ-225_Black_River_슬픔의_강.md` |
| `SE-C-IVδ-230` | **2** | `SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억.md` (31,343 bytes)<br>`SE-C-IVδ-230_Last_Memory_마지막_기억.md` (30,891 bytes) | `SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억.md` |
| `SE-O-IIIγ-233` | **2** | `SE-O-IIIγ-233_Forgotten_Soul_잊혀진_영혼.md` (29,607 bytes)<br>`SE-O-IIIγ-233_Soul_the_Ledgers_Lost_잊혀진_영혼.md` (30,001 bytes) | `SE-O-IIIγ-233_Forgotten_Soul_잊혀진_영혼.md` |
| `SE-C-IIβ-235` | **2** | `SE-C-IIβ-235_Panopticon_벽_속의_감시자.md` (29,484 bytes)<br>`SE-C-IIβ-235_Watcher_in_the_Walls_벽_속의_감시자.md` (29,424 bytes) | `SE-C-IIβ-235_Panopticon_벽_속의_감시자.md` |
| `SE-O-IIβ-235` | **2** | `SE-O-IIβ-235_Myrmidon_찢어진_영혼.md` (30,242 bytes)<br>`SE-O-IIβ-235_Torn_Soul_찢어진_영혼.md` (30,027 bytes) | `SE-O-IIβ-235_Myrmidon_찢어진_영혼.md` |
| `SE-C-Iα-236` | **2** | `SE-C-Iα-236_Unwitnessed_사라진_씨앗.md` (33,049 bytes)<br>`SE-C-Iα-236_Vanished_Seed_사라진_씨앗.md` (32,837 bytes) | `SE-C-Iα-236_Unwitnessed_사라진_씨앗.md` |
| `SE-C-IIβ-240` | **2** | `SE-C-IIβ-240_Holdout_사라진_잔해.md` (31,079 bytes)<br>`SE-C-IIβ-240_Vanished_Ruin_사라진_잔해.md` (30,965 bytes) | `SE-C-IIβ-240_Holdout_사라진_잔해.md` |
| `SE-C-IVγ-240` | **2** | `SE-C-IVγ-240_Broken_Clocktower_부서진_시계탑.md` (30,958 bytes)<br>`SE-C-IVγ-240_Three_Forty-Seven_부서진_시계탑.md` (31,224 bytes) | `SE-C-IVγ-240_Broken_Clocktower_부서진_시계탑.md` |
| `SE-C-Iα-240` | **2** | `SE-C-Iα-240_Echo_of_Kindness_친절의_메아리.md` (31,234 bytes)<br>`SE-C-Iα-240_Solace_친절의_메아리.md` (31,308 bytes) | `SE-C-Iα-240_Echo_of_Kindness_친절의_메아리.md` |
| `SE-C-IIβ-245` | **2** | `SE-C-IIβ-245_Midnight_Choir_노래하는_벽.md` (31,189 bytes)<br>`SE-C-IIβ-245_Singing_Walls_노래하는_벽.md` (30,943 bytes) | `SE-C-IIβ-245_Midnight_Choir_노래하는_벽.md` |
| `SE-C-Iα-247` | **2** | `SE-C-Iα-247_Torn_Flower_찢어진_꽃.md` (28,962 bytes)<br>`SE-C-Iα-247_Unopened_Bloom_찢어진_꽃.md` (29,256 bytes) | `SE-C-Iα-247_Torn_Flower_찢어진_꽃.md` |
| `SE-C-IVδ-249` | **2** | `SE-C-IVδ-249_Collapsed_Whisper_무너진_속삭임.md` (29,813 bytes)<br>`SE-C-IVδ-249_The_Collapsed_Whisper_무너진_속삭임.md` (30,153 bytes) | `SE-C-IVδ-249_Collapsed_Whisper_무너진_속삭임.md` |
| `SE-C-IVδ-250` | **2** | `SE-C-IVδ-250_Restless_Gap_찢어진_흔적.md` (29,914 bytes)<br>`SE-C-IVδ-250_Torn_Trace_찢어진_흔적.md` (29,604 bytes) | `SE-C-IVδ-250_Restless_Gap_찢어진_흔적.md` |
| `SE-N-IIβ-250` | **2** | `SE-N-IIβ-250_Debt-Collector_s-Lantern_추징관의_등불.md` (33,620 bytes)<br>`SE-N-IIβ-250_Debt_Collector's_Lantern_추징관의_등불.md` (33,404 bytes) | `SE-N-IIβ-250_Debt-Collector_s-Lantern_추징관의_등불.md` |
| `SE-C-IVγ-255` | **2** | `SE-C-IVγ-255_Hollow_Architect_빈_건축가.md` (30,054 bytes)<br>`SE-C-IVγ-255_The_Hollow_Architect_빈_건축가.md` (30,368 bytes) | `SE-C-IVγ-255_Hollow_Architect_빈_건축가.md` |
| `SE-C-IVδ-255` | **2** | `SE-C-IVδ-255_Rising_Wall_솟아오른_벽.md` (28,932 bytes)<br>`SE-C-IVδ-255_The_Rising_Wall_솟아오른_벽.md` (29,272 bytes) | `SE-C-IVδ-255_Rising_Wall_솟아오른_벽.md` |
| `SE-C-IVδ-260` | **2** | `SE-C-IVδ-260_Bridge_to_Nowhere_솟아오른_다리.md` (31,568 bytes)<br>`SE-C-IVδ-260_Rising_Bridge_솟아오른_다리.md` (31,266 bytes) | `SE-C-IVδ-260_Bridge_to_Nowhere_솟아오른_다리.md` |
| `SE-C-Vγ-260` | **2** | `SE-C-Vγ-260_Sorrow_Tide_한의_조수.md` (31,311 bytes)<br>`SE-C-Vγ-260_The_Sorrow_Tide_한의_조수.md` (31,657 bytes) | `SE-C-Vγ-260_Sorrow_Tide_한의_조수.md` |
| `SE-C-Vδ-265` | **2** | `SE-C-Vδ-265_Forgotten_God_잊혀진_신.md` (32,655 bytes)<br>`SE-C-Vδ-265_Sornos_잊혀진_신.md` (32,769 bytes) | `SE-C-Vδ-265_Forgotten_God_잊혀진_신.md` |
| `SE-C-IVγ-270` | **2** | `SE-C-IVγ-270_Memory_Lake_기억의_호수.md` (30,688 bytes)<br>`SE-C-IVγ-270_Mnemosyne_기억의_호수.md` (30,924 bytes) | `SE-C-IVγ-270_Memory_Lake_기억의_호수.md` |
| `SE-N-IIβ-270` | **2** | `SE-N-IIβ-270_Neglect_Learned_to_Listen_녹슨_속삭임.md` (31,599 bytes)<br>`SE-N-IIβ-270_Rusted_Whisper_녹슨_속삭임.md` (31,153 bytes) | `SE-N-IIβ-270_Neglect_Learned_to_Listen_녹슨_속삭임.md` |
| `SE-C-IIIβ-275` | **2** | `SE-C-IIIβ-275_Crucible_분노의_용광로.md` (30,740 bytes)<br>`SE-C-IIIβ-275_Rage_Forge_분노의_용광로.md` (30,546 bytes) | `SE-C-IIIβ-275_Crucible_분노의_용광로.md` |
| `SE-C-IIβ-280` | **2** | `SE-C-IIβ-280_Pall_눈물의_베일.md` (33,082 bytes)<br>`SE-C-IIβ-280_Veil_of_Tears_눈물의_베일.md` (33,016 bytes) | `SE-C-IIβ-280_Pall_눈물의_베일.md` |
| `SE-N-IIβ-280` | **2** | `SE-N-IIβ-280_Kind_Healer's_Shadow_치유자의_그림자.md` (29,502 bytes)<br>`SE-N-IIβ-280_The_Kind_Healer's_Shadow_치유자의_그림자.md` (29,794 bytes) | `SE-N-IIβ-280_Kind_Healer's_Shadow_치유자의_그림자.md` |
| `SE-N-IIIγ-283` | **2** | `SE-N-IIIγ-283_Barrier_of_Nothing_녹슨_벽.md` (29,242 bytes)<br>`SE-N-IIIγ-283_Rusted_Wall_녹슨_벽.md` (28,850 bytes) | `SE-N-IIIγ-283_Barrier_of_Nothing_녹슨_벽.md` |
| `SE-C-IIβ-290` | **2** | `SE-C-IIβ-290_Broken_Compass_부서진_나침반.md` (32,520 bytes)<br>`SE-C-IIβ-290_Compass_Without_North_부서진_나침반.md` (32,890 bytes) | `SE-C-IIβ-290_Broken_Compass_부서진_나침반.md` |
| `SE-C-Vδ-290` | **2** | `SE-C-Vδ-290_First_Tear_첫_번째_눈물.md` (33,962 bytes)<br>`SE-C-Vδ-290_The_First_Tear_첫_번째_눈물.md` (34,686 bytes) | `SE-C-Vδ-290_First_Tear_첫_번째_눈물.md` |
| `SE-C-IIIγ-300` | **2** | `SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠.md` (33,463 bytes)<br>`SE-C-IIIγ-300_The_Memory_Lock_기억의_자물쇠.md` (33,818 bytes) | `SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠.md` |
| `SE-C-Iα-300` | **2** | `SE-C-Iα-300_Sorrow_Seed_슬픔의_씨앗.md` (33,461 bytes)<br>`SE-C-Iα-300_The_Sorrow_Seed_슬픔의_씨앗.md` (33,771 bytes) | `SE-C-Iα-300_Sorrow_Seed_슬픔의_씨앗.md` |
| `SE-O-IIβ-301` | **2** | `SE-O-IIβ-301_Feu_Follet_녹아내린_불꽃.md` (29,527 bytes)<br>`SE-O-IIβ-301_Melting_Flame_녹아내린_불꽃.md` (29,362 bytes) | `SE-O-IIβ-301_Feu_Follet_녹아내린_불꽃.md` |
| `SE-N-IIIγ-308` | **2** | `SE-N-IIIγ-308_Soaking_Shadow_솟구친_그림자.md` (32,372 bytes)<br>`SE-N-IIIγ-308_Vault_of_Unspoken_Spite_솟구친_그림자.md` (32,823 bytes) | `SE-N-IIIγ-308_Soaking_Shadow_솟구친_그림자.md` |
| `SE-N-IVδ-315` | **2** | `SE-N-IVδ-315_Collapsed_Seed_무너진_씨앗.md` (33,857 bytes)<br>`SE-N-IVδ-315_Unsprouted_Life_무너진_씨앗.md` (34,148 bytes) | `SE-N-IVδ-315_Collapsed_Seed_무너진_씨앗.md` |
| `SE-N-Iα-316` | **2** | `SE-N-Iα-316_Soaking_Rope_솟구친_밧줄.md` (29,248 bytes)<br>`SE-N-Iα-316_Tether_솟구친_밧줄.md` (29,368 bytes) | `SE-N-Iα-316_Soaking_Rope_솟구친_밧줄.md` |
| `SE-C-Vγ-320` | **2** | `SE-C-Vγ-320_Sorrow_Storm_슬픔의_폭풍.md` (30,459 bytes)<br>`SE-C-Vγ-320_Unwept_Storm_슬픔의_폭풍.md` (30,725 bytes) | `SE-C-Vγ-320_Sorrow_Storm_슬픔의_폭풍.md` |
| `SE-C-Iα-329` | **2** | `SE-C-Iα-329_Folly_녹아내린_탑.md` (32,264 bytes)<br>`SE-C-Iα-329_Melting_Tower_녹아내린_탑.md` (32,178 bytes) | `SE-C-Iα-329_Folly_녹아내린_탑.md` |
| `SE-C-IIβ-330` | **2** | `SE-C-IIβ-330_Frozen_Window_얼어붙은_창.md` (29,510 bytes)<br>`SE-C-IIβ-330_Sitting_Boundary_얼어붙은_창.md` (29,780 bytes) | `SE-C-IIβ-330_Frozen_Window_얼어붙은_창.md` |
| `SE-C-Iα-330` | **2** | `SE-C-Iα-330_Mourner's_Bloom_슬픔의_꽃.md` (33,779 bytes)<br>`SE-C-Iα-330_Sorrow_Flower_슬픔의_꽃.md` (33,511 bytes) | `SE-C-Iα-330_Mourner's_Bloom_슬픔의_꽃.md` |
| `SE-N-IVδ-339` | **2** | `SE-N-IVδ-339_Breach_무너진_벽.md` (29,912 bytes)<br>`SE-N-IVδ-339_Collapsed_Wall_무너진_벽.md` (29,780 bytes) | `SE-N-IVδ-339_Breach_무너진_벽.md` |
| `SE-C-IIβ-340` | **2** | `SE-C-IIβ-340_Clapperless_빈_종.md` (33,107 bytes)<br>`SE-C-IIβ-340_Hollow_Bell_빈_종.md` (32,877 bytes) | `SE-C-IIβ-340_Clapperless_빈_종.md` |
| `SE-O-Iα-340` | **2** | `SE-O-Iα-340_Apocrypha_얼어붙은_유물.md` (30,791 bytes)<br>`SE-O-Iα-340_Frozen_Relic_얼어붙은_유물.md` (30,631 bytes) | `SE-O-Iα-340_Apocrypha_얼어붙은_유물.md` |
| `SE-C-IIβ-357` | **2** | `SE-C-IIβ-357_Carrying_Nothing_사라진_무게.md` (30,086 bytes)<br>`SE-C-IIβ-357_Vanished_Weight_사라진_무게.md` (29,840 bytes) | `SE-C-IIβ-357_Carrying_Nothing_사라진_무게.md` |
| `SE-C-IVδ-357` | **2** | `SE-C-IVδ-357_Sleeping_Weight_잠든_무게.md` (29,651 bytes)<br>`SE-C-IVδ-357_Unreleased_Beam_잠든_무게.md` (29,909 bytes) | `SE-C-IVδ-357_Sleeping_Weight_잠든_무게.md` |
| `SE-O-IIIγ-369` | **2** | `SE-O-IIIγ-369_Broken_Whisper_부서진_속삭임.md` (33,180 bytes)<br>`SE-O-IIIγ-369_Susurrus_부서진_속삭임.md` (33,322 bytes) | `SE-O-IIIγ-369_Broken_Whisper_부서진_속삭임.md` |
| `SE-O-IIIγ-371` | **2** | `SE-O-IIIγ-371_Protest_No_One_Remembers_사라진_침묵.md` (29,952 bytes)<br>`SE-O-IIIγ-371_Vanished_Silence_사라진_침묵.md` (29,514 bytes) | `SE-O-IIIγ-371_Protest_No_One_Remembers_사라진_침묵.md` |
| `SE-C-IIIγ-373` | **2** | `SE-C-IIIγ-373_Spreading_Well_스며든_우물.md` (30,905 bytes)<br>`SE-C-IIIγ-373_Till_Someone_Understands_스며든_우물.md` (31,343 bytes) | `SE-C-IIIγ-373_Spreading_Well_스며든_우물.md` |
| `SE-O-IIIγ-374` | **2** | `SE-O-IIIγ-374_Sleeping_Tree_잠든_나무.md` (33,510 bytes)<br>`SE-O-IIIγ-374_Slept_Because_You_Never_Returned_잠든_나무.md` (34,153 bytes) | `SE-O-IIIγ-374_Sleeping_Tree_잠든_나무.md` |
| `SE-O-IIβ-378` | **2** | `SE-O-IIβ-378_Drowned_Echo_침몰한_메아리.md` (29,385 bytes)<br>`SE-O-IIβ-378_Fathom_침몰한_메아리.md` (29,501 bytes) | `SE-O-IIβ-378_Drowned_Echo_침몰한_메아리.md` |
| `SE-C-Iα-392` | **2** | `SE-C-Iα-392_Mirror_of_Rising_솟아오른_거울.md` (28,919 bytes)<br>`SE-C-Iα-392_Rising_Mirror_솟아오른_거울.md` (28,627 bytes) | `SE-C-Iα-392_Mirror_of_Rising_솟아오른_거울.md` |
| `SE-N-IIIγ-407` | **2** | `SE-N-IIIγ-407_Fading_Whisper_번져가는_속삭임.md` (28,966 bytes)<br>`SE-N-IIIγ-407_Lingering_Place_번져가는_속삭임.md` (29,265 bytes) | `SE-N-IIIγ-407_Fading_Whisper_번져가는_속삭임.md` |
| `SE-N-IIIγ-409` | **2** | `SE-N-IIIγ-409_Floating_Pillar_떠다니는_기둥.md` (29,350 bytes)<br>`SE-N-IIIγ-409_Pillar_Holding_Nothing_떠다니는_기둥.md` (29,746 bytes) | `SE-N-IIIγ-409_Floating_Pillar_떠다니는_기둥.md` |
| `SE-N-IIβ-426` | **2** | `SE-N-IIβ-426_Hollowcast_찢어진_열매.md` (29,579 bytes)<br>`SE-N-IIβ-426_Torn_Fruit_찢어진_열매.md` (29,351 bytes) | `SE-N-IIβ-426_Hollowcast_찢어진_열매.md` |
| `SE-N-IIIγ-447` | **2** | `SE-N-IIIγ-447_Melting_Rope_녹아내린_밧줄.md` (29,662 bytes)<br>`SE-N-IIIγ-447_Rope_Held_Too_Long_녹아내린_밧줄.md` (30,058 bytes) | `SE-N-IIIγ-447_Melting_Rope_녹아내린_밧줄.md` |
| `SE-C-IIIγ-448` | **2** | `SE-C-IIIγ-448_Floating_Well_떠다니는_우물.md` (29,269 bytes)<br>`SE-C-IIIγ-448_Overflow_떠다니는_우물.md` (29,422 bytes) | `SE-C-IIIγ-448_Floating_Well_떠다니는_우물.md` |
| `SE-N-IIβ-453` | **2** | `SE-N-IIβ-453_Forgotten_Shadow_잊혀진_그림자.md` (29,923 bytes)<br>`SE-N-IIβ-453_Spoor_잊혀진_그림자.md` (29,942 bytes) | `SE-N-IIβ-453_Forgotten_Shadow_잊혀진_그림자.md` |
| `SE-O-Iα-453` | **2** | `SE-O-Iα-453_Floating_Fragment_떠다니는_파편.md` (29,523 bytes)<br>`SE-O-Iα-453_Keen_떠다니는_파편.md` (29,503 bytes) | `SE-O-Iα-453_Floating_Fragment_떠다니는_파편.md` |
| `SE-N-IIβ-456` | **2** | `SE-N-IIβ-456_Fading_Fruit_번져가는_열매.md` (30,861 bytes)<br>`SE-N-IIβ-456_Orchard_of_the_Indebted_번져가는_열매.md` (31,309 bytes) | `SE-N-IIβ-456_Fading_Fruit_번져가는_열매.md` |
| `SE-N-Iα-459` | **2** | `SE-N-Iα-459_Bulwark_잠든_벽.md` (30,314 bytes)<br>`SE-N-Iα-459_Sleeping_Wall_잠든_벽.md` (30,231 bytes) | `SE-N-Iα-459_Bulwark_잠든_벽.md` |
| `SE-O-IIβ-467` | **2** | `SE-O-IIβ-467_Memory_Chain_솟구친_사슬.md` (29,719 bytes)<br>`SE-O-IIβ-467_Soaking_Chain_솟구친_사슬.md` (29,539 bytes) | `SE-O-IIβ-467_Memory_Chain_솟구친_사슬.md` |
| `SE-O-IIIγ-476` | **2** | `SE-O-IIIγ-476_Sehnsucht_가라앉은_눈물.md` (32,797 bytes)<br>`SE-O-IIIγ-476_Sunken_Tear_가라앉은_눈물.md` (32,571 bytes) | `SE-O-IIIγ-476_Sehnsucht_가라앉은_눈물.md` |
| `SE-N-IIβ-488` | **2** | `SE-N-IIβ-488_Friendless_Bridge_스며든_다리.md` (33,085 bytes)<br>`SE-N-IIβ-488_Spreading_Bridge_스며든_다리.md` (32,839 bytes) | `SE-N-IIβ-488_Friendless_Bridge_스며든_다리.md` |
| `SE-N-IVδ-489` | **2** | `SE-N-IVδ-489_Forgotten_Silence_잊혀진_침묵.md` (30,113 bytes)<br>`SE-N-IVδ-489_Silence_We_Forgot_We_Made_잊혀진_침묵.md` (30,525 bytes) | `SE-N-IVδ-489_Forgotten_Silence_잊혀진_침묵.md` |
| `SE-C-IVδ-503` | **2** | `SE-C-IVδ-503_Floating_Shard_떠다니는_조각.md` (29,815 bytes)<br>`SE-C-IVδ-503_Hover_떠다니는_조각.md` (29,854 bytes) | `SE-C-IVδ-503_Floating_Shard_떠다니는_조각.md` |
| `SE-C-IVδ-505` | **2** | `SE-C-IVδ-505_Cold_Burn_얼어붙은_그림자.md` (29,369 bytes)<br>`SE-C-IVδ-505_Frozen_Shadow_얼어붙은_그림자.md` (29,227 bytes) | `SE-C-IVδ-505_Cold_Burn_얼어붙은_그림자.md` |
| `SE-N-IIIγ-505` | **2** | `SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해.md` (29,888 bytes)<br>`SE-N-IIIγ-505_Returning_Ruin_돌아온_잔해.md` (29,644 bytes) | `SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해.md` |
| `SE-N-IVδ-517` | **2** | `SE-N-IVδ-517_Broken_Tear_부서진_눈물.md` (29,587 bytes)<br>`SE-N-IVδ-517_Lachrymose_부서진_눈물.md` (29,830 bytes) | `SE-N-IVδ-517_Broken_Tear_부서진_눈물.md` |
| `SE-N-Iα-518` | **2** | `SE-N-Iα-518_Life_Behind_Glass_솟구친_창.md` (33,271 bytes)<br>`SE-N-Iα-518_Soaking_Window_솟구친_창.md` (32,980 bytes) | `SE-N-Iα-518_Life_Behind_Glass_솟구친_창.md` |
| `SE-N-Iα-519` | **2** | `SE-N-Iα-519_Mourning_a_Life_I_Never_Lived_스며든_씨앗.md` (31,482 bytes)<br>`SE-N-Iα-519_Spreading_Seed_스며든_씨앗.md` (30,967 bytes) | `SE-N-Iα-519_Mourning_a_Life_I_Never_Lived_스며든_씨앗.md` |
| `SE-N-IVδ-525` | **2** | `SE-N-IVδ-525_Cenotaph_흐르는_다리.md` (29,856 bytes)<br>`SE-N-IVδ-525_Flowing_Bridge_흐르는_다리.md` (29,754 bytes) | `SE-N-IVδ-525_Cenotaph_흐르는_다리.md` |
| `SE-O-Iα-554` | **2** | `SE-O-Iα-554_Fallow_녹슨_씨앗.md` (34,272 bytes)<br>`SE-O-Iα-554_Rusted_Seed_녹슨_씨앗.md` (34,159 bytes) | `SE-O-Iα-554_Fallow_녹슨_씨앗.md` |
| `SE-C-IIIγ-558` | **2** | `SE-C-IIIγ-558_Burning_Root_타오르는_뿌리.md` (29,319 bytes)<br>`SE-C-IIIγ-558_Emberroot_타오르는_뿌리.md` (29,531 bytes) | `SE-C-IIIγ-558_Burning_Root_타오르는_뿌리.md` |
| `SE-O-IIIγ-559` | **2** | `SE-O-IIIγ-559_Broken_Ruin_부서진_잔해.md` (29,469 bytes)<br>`SE-O-IIIγ-559_Souvenir_부서진_잔해.md` (29,683 bytes) | `SE-O-IIIγ-559_Broken_Ruin_부서진_잔해.md` |
| `SE-N-IIβ-560` | **2** | `SE-N-IIβ-560_Dismissed_Cry_솟구친_절규.md` (32,691 bytes)<br>`SE-N-IIβ-560_Soaking_Scream_솟구친_절규.md` (32,505 bytes) | `SE-N-IIβ-560_Dismissed_Cry_솟구친_절규.md` |
| `SE-C-IIβ-565` | **2** | `SE-C-IIβ-565_Broken_Well_부서진_우물.md` (29,333 bytes)<br>`SE-C-IIβ-565_Upwell_부서진_우물.md` (29,452 bytes) | `SE-C-IIβ-565_Broken_Well_부서진_우물.md` |
| `SE-N-IIIγ-585` | **2** | `SE-N-IIIγ-585_Floating_Tree_떠다니는_나무.md` (31,750 bytes)<br>`SE-N-IIIγ-585_Rootless_떠다니는_나무.md` (31,913 bytes) | `SE-N-IIIγ-585_Floating_Tree_떠다니는_나무.md` |
| `SE-N-IIIγ-589` | **2** | `SE-N-IIIγ-589_Nemo_돌아온_영혼.md` (28,705 bytes)<br>`SE-N-IIIγ-589_Returning_Soul_돌아온_영혼.md` (28,677 bytes) | `SE-N-IIIγ-589_Nemo_돌아온_영혼.md` |
| `SE-N-IVδ-606` | **2** | `SE-N-IVδ-606_Banyan_가라앉은_나무.md` (32,411 bytes)<br>`SE-N-IVδ-606_Sunken_Tree_가라앉은_나무.md` (32,238 bytes) | `SE-N-IVδ-606_Banyan_가라앉은_나무.md` |
| `SE-C-IIIγ-609` | **2** | `SE-C-IIIγ-609_Frozen_Echo_얼어붙은_메아리.md` (32,647 bytes)<br>`SE-C-IIIγ-609_Thousand_Hands_얼어붙은_메아리.md` (32,981 bytes) | `SE-C-IIIγ-609_Frozen_Echo_얼어붙은_메아리.md` |
| `SE-N-IVδ-611` | **2** | `SE-N-IVδ-611_Sleeping_Shard_잠든_조각.md` (29,591 bytes)<br>`SE-N-IVδ-611_Somnalith_잠든_조각.md` (29,712 bytes) | `SE-N-IVδ-611_Sleeping_Shard_잠든_조각.md` |
| `SE-O-IIIγ-617` | **2** | `SE-O-IIIγ-617_Exiles'_Wall_솟구친_벽.md` (31,042 bytes)<br>`SE-O-IIIγ-617_Soaking_Wall_솟구친_벽.md` (30,814 bytes) | `SE-O-IIIγ-617_Exiles'_Wall_솟구친_벽.md` |
| `SE-C-Iα-622` | **2** | `SE-C-Iα-622_Vanished_Tree_사라진_나무.md` (28,572 bytes)<br>`SE-C-Iα-622_Vestige_사라진_나무.md` (28,654 bytes) | `SE-C-Iα-622_Vanished_Tree_사라진_나무.md` |
| `SE-N-IIβ-627` | **2** | `SE-N-IIβ-627_Harvest_Beyond_the_Gate_녹아내린_열매.md` (31,010 bytes)<br>`SE-N-IIβ-627_Melting_Fruit_녹아내린_열매.md` (30,602 bytes) | `SE-N-IIβ-627_Harvest_Beyond_the_Gate_녹아내린_열매.md` |
| `SE-N-IIIγ-628` | **2** | `SE-N-IIIγ-628_Flowing_Seed_흐르는_씨앗.md` (31,225 bytes)<br>`SE-N-IIIγ-628_Patrimoine_흐르는_씨앗.md` (31,407 bytes) | `SE-N-IIIγ-628_Flowing_Seed_흐르는_씨앗.md` |
| `SE-O-Iα-631` | **2** | `SE-O-Iα-631_Errant_사라진_뿌리.md` (29,675 bytes)<br>`SE-O-Iα-631_Vanished_Root_사라진_뿌리.md` (29,600 bytes) | `SE-O-Iα-631_Errant_사라진_뿌리.md` |
| `SE-N-IVδ-641` | **2** | `SE-N-IVδ-641_Home_to_No_One_Who_Knew_Me_돌아온_유물.md` (33,718 bytes)<br>`SE-N-IVδ-641_Returning_Relic_돌아온_유물.md` (33,230 bytes) | `SE-N-IVδ-641_Home_to_No_One_Who_Knew_Me_돌아온_유물.md` |
| `SE-O-Iα-643` | **2** | `SE-O-Iα-643_Frozen_Mirror_얼어붙은_거울.md` (33,115 bytes)<br>`SE-O-Iα-643_Vanity_얼어붙은_거울.md` (33,217 bytes) | `SE-O-Iα-643_Frozen_Mirror_얼어붙은_거울.md` |
| `SE-C-IIIγ-649` | **2** | `SE-C-IIIγ-649_Sunken_Pillar_가라앉은_기둥.md` (30,559 bytes)<br>`SE-C-IIIγ-649_Unborn_Monument_가라앉은_기둥.md` (30,861 bytes) | `SE-C-IIIγ-649_Sunken_Pillar_가라앉은_기둥.md` |
| `SE-O-IIIγ-651` | **2** | `SE-O-IIIγ-651_Relic_Waiting_for_Its_Maker_잠든_유물.md` (31,156 bytes)<br>`SE-O-IIIγ-651_Sleeping_Relic_잠든_유물.md` (30,618 bytes) | `SE-O-IIIγ-651_Relic_Waiting_for_Its_Maker_잠든_유물.md` |
| `SE-C-IVδ-668` | **2** | `SE-C-IVδ-668_Frozen_Fury_얼어붙은_잔해.md` (33,587 bytes)<br>`SE-C-IVδ-668_Frozen_Ruin_얼어붙은_잔해.md` (33,317 bytes) | `SE-C-IVδ-668_Frozen_Fury_얼어붙은_잔해.md` |
| `SE-O-IIβ-677` | **2** | `SE-O-IIβ-677_Tower_Erased_Overnight_사라진_탑.md` (31,390 bytes)<br>`SE-O-IIβ-677_Vanished_Tower_사라진_탑.md` (31,018 bytes) | `SE-O-IIβ-677_Tower_Erased_Overnight_사라진_탑.md` |
| `SE-C-Iα-683` | **2** | `SE-C-Iα-683_Swallowed_Fury_사라진_눈물.md` (29,014 bytes)<br>`SE-C-Iα-683_Vanished_Tear_사라진_눈물.md` (28,774 bytes) | `SE-C-Iα-683_Swallowed_Fury_사라진_눈물.md` |
| `SE-N-Iα-686` | **2** | `SE-N-Iα-686_Torn_Window_찢어진_창.md` (32,533 bytes)<br>`SE-N-Iα-686_Window_of_a_Thousand_Goodbyes_찢어진_창.md` (33,139 bytes) | `SE-N-Iα-686_Torn_Window_찢어진_창.md` |
| `SE-N-IIβ-689` | **2** | `SE-N-IIβ-689_Face_Beneath_Masks_스며든_벽.md` (29,618 bytes)<br>`SE-N-IIβ-689_Spreading_Wall_스며든_벽.md` (29,316 bytes) | `SE-N-IIβ-689_Face_Beneath_Masks_스며든_벽.md` |
| `SE-O-IVδ-693` | **2** | `SE-O-IVδ-693_Spreading_Root_스며든_뿌리.md` (29,599 bytes)<br>`SE-O-IVδ-693_Undercurrent_스며든_뿌리.md` (29,829 bytes) | `SE-O-IVδ-693_Spreading_Root_스며든_뿌리.md` |
| `SE-O-Iα-709` | **2** | `SE-O-Iα-709_Forgotten_Tear_잊혀진_눈물.md` (33,432 bytes)<br>`SE-O-Iα-709_Ungrievingness_잊혀진_눈물.md` (33,660 bytes) | `SE-O-Iα-709_Forgotten_Tear_잊혀진_눈물.md` |
| `SE-C-IIβ-716` | **2** | `SE-C-IIβ-716_Double_Mouth_찢어진_속삭임.md` (29,966 bytes)<br>`SE-C-IIβ-716_Torn_Whisper_찢어진_속삭임.md` (29,738 bytes) | `SE-C-IIβ-716_Double_Mouth_찢어진_속삭임.md` |
| `SE-O-Iα-720` | **2** | `SE-O-Iα-720_Aphasia_녹아내린_속삭임.md` (30,540 bytes)<br>`SE-O-Iα-720_Melting_Whisper_녹아내린_속삭임.md` (30,456 bytes) | `SE-O-Iα-720_Aphasia_녹아내린_속삭임.md` |
| `SE-C-Iα-723` | **2** | `SE-C-Iα-723_The_Vanished_Rope_사라진_밧줄.md` (29,988 bytes)<br>`SE-C-Iα-723_Vanished_Rope_사라진_밧줄.md` (29,690 bytes) | `SE-C-Iα-723_The_Vanished_Rope_사라진_밧줄.md` |
| `SE-O-Iα-754` | **2** | `SE-O-Iα-754_Thralldom_떠도는_사슬.md` (29,532 bytes)<br>`SE-O-Iα-754_Wandering_Chain_떠도는_사슬.md` (29,412 bytes) | `SE-O-Iα-754_Thralldom_떠도는_사슬.md` |
| `SE-O-IIβ-757` | **2** | `SE-O-IIβ-757_Broken_Door_부서진_문.md` (30,916 bytes)<br>`SE-O-IIβ-757_Door_to_No_One_부서진_문.md` (31,165 bytes) | `SE-O-IIβ-757_Broken_Door_부서진_문.md` |
| `SE-O-IVδ-762` | **2** | `SE-O-IVδ-762_Burning_Bridge_타오르는_다리.md` (29,617 bytes)<br>`SE-O-IVδ-762_Grasp_타오르는_다리.md` (29,696 bytes) | `SE-O-IVδ-762_Grasp_타오르는_다리.md` |
| `SE-C-IVδ-763` | **2** | `SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃.md` (31,361 bytes)<br>`SE-C-IVδ-763_Vanished_Flame_사라진_불꽃.md` (30,864 bytes) | `SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃.md` |
| `SE-C-IVδ-767` | **2** | `SE-C-IVδ-767_Fading_Shadow_번져가는_그림자.md` (31,053 bytes)<br>`SE-C-IVδ-767_Swallow_번져가는_그림자.md` (31,219 bytes) | `SE-C-IVδ-767_Swallow_번져가는_그림자.md` |
| `SE-C-IIβ-775` | **2** | `SE-C-IIβ-775_Cleaved_찢어진_탑.md` (30,250 bytes)<br>`SE-C-IIβ-775_Torn_Tower_찢어진_탑.md` (30,074 bytes) | `SE-C-IIβ-775_Cleaved_찢어진_탑.md` |
| `SE-C-IIβ-777` | **2** | `SE-C-IIβ-777_Burning_Fruit_타오르는_열매.md` (30,019 bytes)<br>`SE-C-IIβ-777_Last_Fruit_타오르는_열매.md` (30,190 bytes) | `SE-C-IIβ-777_Last_Fruit_타오르는_열매.md` |
| `SE-N-IIβ-778` | **2** | `SE-N-IIβ-778_Soaking_Well_솟구친_우물.md` (30,556 bytes)<br>`SE-N-IIβ-778_Well_of_Unfinished_Words_솟구친_우물.md` (30,984 bytes) | `SE-N-IIβ-778_Well_of_Unfinished_Words_솟구친_우물.md` |
| `SE-C-Iα-779` | **2** | `SE-C-Iα-779_Miscast_찢어진_유물.md` (32,928 bytes)<br>`SE-C-Iα-779_Torn_Relic_찢어진_유물.md` (32,754 bytes) | `SE-C-Iα-779_Miscast_찢어진_유물.md` |
| `SE-C-IIβ-782` | **2** | `SE-C-IIβ-782_Fading_Relic_번져가는_유물.md` (30,168 bytes)<br>`SE-C-IIβ-782_Flotsam_번져가는_유물.md` (30,301 bytes) | `SE-C-IIβ-782_Flotsam_번져가는_유물.md` |
| `SE-N-Iα-785` | **2** | `SE-N-Iα-785_Collapsed_Tear_무너진_눈물.md` (33,555 bytes)<br>`SE-N-Iα-785_Tear_Too_Small_to_Honor_무너진_눈물.md` (33,981 bytes) | `SE-N-Iα-785_Tear_Too_Small_to_Honor_무너진_눈물.md` |
| `SE-O-IVδ-792` | **2** | `SE-O-IVδ-792_Flowing_Relic_흐르는_유물.md` (29,708 bytes)<br>`SE-O-IVδ-792_Relic_of_a_Thousand_Owners_흐르는_유물.md` (30,197 bytes) | `SE-O-IVδ-792_Relic_of_a_Thousand_Owners_흐르는_유물.md` |
| `SE-O-Iα-794` | **2** | `SE-O-Iα-794_Collapsed_Door_무너진_문.md` (32,532 bytes)<br>`SE-O-Iα-794_Portcullis_무너진_문.md` (32,684 bytes) | `SE-O-Iα-794_Portcullis_무너진_문.md` |
| `SE-O-IIβ-796` | **2** | `SE-O-IIβ-796_Soaking_Tower_솟구친_탑.md` (29,538 bytes)<br>`SE-O-IIβ-796_Spire_of_Unanswered_Prayer_솟구친_탑.md` (30,000 bytes) | `SE-O-IIβ-796_Spire_of_Unanswered_Prayer_솟구친_탑.md` |
| `SE-N-IIβ-801` | **2** | `SE-N-IIβ-801_Mirror_of_Soaking_솟아오른_거울.md` (33,319 bytes)<br>`SE-N-IIβ-801_Soaking_Mirror_솟아오른_거울.md` (33,037 bytes) | `SE-N-IIβ-801_Mirror_of_Soaking_솟아오른_거울.md` |
| `SE-N-IVδ-821` | **2** | `SE-N-IVδ-821_Pent_사라진_한숨.md` (30,560 bytes)<br>`SE-N-IVδ-821_Vanished_Sigh_사라진_한숨.md` (30,454 bytes) | `SE-N-IVδ-821_Pent_사라진_한숨.md` |
| `SE-C-IVδ-823` | **2** | `SE-C-IVδ-823_Stranded_Between_Two_Shores_가라앉은_다리.md` (30,360 bytes)<br>`SE-C-IVδ-823_Sunken_Bridge_가라앉은_다리.md` (29,850 bytes) | `SE-C-IVδ-823_Stranded_Between_Two_Shores_가라앉은_다리.md` |
| `SE-O-IIβ-833` | **2** | `SE-O-IIβ-833_Neverlast_녹슨_영혼.md` (30,068 bytes)<br>`SE-O-IIβ-833_Rusted_Soul_녹슨_영혼.md` (29,882 bytes) | `SE-O-IIβ-833_Neverlast_녹슨_영혼.md` |
| `SE-O-IVδ-844` | **2** | `SE-O-IVδ-844_Repose_잠든_잔해.md` (30,264 bytes)<br>`SE-O-IVδ-844_Sleeping_Ruin_잠든_잔해.md` (30,130 bytes) | `SE-O-IVδ-844_Repose_잠든_잔해.md` |
| `SE-N-IIβ-845` | **2** | `SE-N-IIβ-845_Perennial_돌아온_꽃.md` (31,632 bytes)<br>`SE-N-IIβ-845_Returning_Flower_돌아온_꽃.md` (31,539 bytes) | `SE-N-IIβ-845_Perennial_돌아온_꽃.md` |
| `SE-O-IVδ-851` | **2** | `SE-O-IVδ-851_Broken_Shard_부서진_조각.md` (33,539 bytes)<br>`SE-O-IVδ-851_Shard_of_a_Broken_Promise_부서진_조각.md` (34,041 bytes) | `SE-O-IVδ-851_Shard_of_a_Broken_Promise_부서진_조각.md` |
| `SE-N-IVδ-852` | **2** | `SE-N-IVδ-852_Conservatory_잊혀진_잔해.md` (33,701 bytes)<br>`SE-N-IVδ-852_Forgotten_Ruin_잊혀진_잔해.md` (33,499 bytes) | `SE-N-IVδ-852_Conservatory_잊혀진_잔해.md` |
| `SE-C-Iα-863` | **2** | `SE-C-Iα-863_Absent_Landmark_가라앉은_탑.md` (29,145 bytes)<br>`SE-C-Iα-863_Sunken_Tower_가라앉은_탑.md` (28,885 bytes) | `SE-C-Iα-863_Absent_Landmark_가라앉은_탑.md` |
| `SE-C-IVδ-869` | **2** | `SE-C-IVδ-869_Rising_Well_솟아오른_우물.md` (29,639 bytes)<br>`SE-C-IVδ-869_Well_Within_솟아오른_우물.md` (29,902 bytes) | `SE-C-IVδ-869_Rising_Well_솟아오른_우물.md` |
| `SE-C-Iα-869` | **2** | `SE-C-Iα-869_Homecoming_Tree_돌아온_나무.md` (31,967 bytes)<br>`SE-C-Iα-869_Returning_Tree_돌아온_나무.md` (31,753 bytes) | `SE-C-Iα-869_Homecoming_Tree_돌아온_나무.md` |
| `SE-N-IIIγ-874` | **2** | `SE-N-IIIγ-874_Bridge_of_the_Unchosen_얼어붙은_다리.md` (32,508 bytes)<br>`SE-N-IIIγ-874_Frozen_Bridge_얼어붙은_다리.md` (32,100 bytes) | `SE-N-IIIγ-874_Bridge_of_the_Unchosen_얼어붙은_다리.md` |
| `SE-C-Iα-884` | **2** | `SE-C-Iα-884_Frozen_Shard_얼어붙은_조각.md` (32,577 bytes)<br>`SE-C-Iα-884_Seething_Tundra_얼어붙은_조각.md` (32,861 bytes) | `SE-C-Iα-884_Seething_Tundra_얼어붙은_조각.md` |
| `SE-C-IIIγ-891` | **2** | `SE-C-IIIγ-891_Screaming_Masonry_스며든_절규.md` (32,443 bytes)<br>`SE-C-IIIγ-891_Spreading_Scream_스며든_절규.md` (32,156 bytes) | `SE-C-IIIγ-891_Screaming_Masonry_스며든_절규.md` |
| `SE-O-IVδ-895` | **2** | `SE-O-IVδ-895_Survivors'_Breath_떠도는_한숨.md` (30,097 bytes)<br>`SE-O-IVδ-895_Wandering_Sigh_떠도는_한숨.md` (29,769 bytes) | `SE-O-IVδ-895_Survivors'_Breath_떠도는_한숨.md` |
| `SE-O-IVδ-897` | **2** | `SE-O-IVδ-897_Broken_Wall_부서진_벽.md` (29,160 bytes)<br>`SE-O-IVδ-897_Welcome_Haven_부서진_벽.md` (29,464 bytes) | `SE-O-IVδ-897_Welcome_Haven_부서진_벽.md` |
| `SE-C-Iα-900` | **2** | `SE-C-Iα-900_Forgotten_Storyteller_잊혀진_이야기꾼.md` (17,813 bytes)<br>`SE-C-Iα-900_Vellum_Man_잊혀진_이야기꾼.md` (18,138 bytes) | `SE-C-Iα-900_Vellum_Man_잊혀진_이야기꾼.md` |
| `SE-C-IIβ-901` | **2** | `SE-C-IIβ-901_Duri's_Heart_보존된_심장.md` (18,859 bytes)<br>`SE-C-IIβ-901_Preserved_Heart_보존된_심장.md` (18,456 bytes) | `SE-C-IIβ-901_Duri's_Heart_보존된_심장.md` |
| `SE-C-IIIγ-902` | **2** | `SE-C-IIIγ-902_Beating_Relic_고동치는_유물.md` (18,153 bytes)<br>`SE-C-IIIγ-902_Goru's_Fist_고동치는_유물.md` (18,556 bytes) | `SE-C-IIIγ-902_Beating_Relic_고동치는_유물.md` |
| `SE-N-Iα-905` | **2** | `SE-N-Iα-905_HanKrater_영혼의_그릇.md` (17,741 bytes)<br>`SE-N-Iα-905_Lacrima_영혼의_그릇.md` (18,144 bytes) | `SE-N-Iα-905_Lacrima_영혼의_그릇.md` |
| `SE-C-IIβ-906` | **2** | `SE-C-IIβ-906_Grimoire_스스로_쓰는_책.md` (18,020 bytes)<br>`SE-C-IIβ-906_The_Self-Writing_Book_스스로_쓰는_책.md` (17,757 bytes) | `SE-C-IIβ-906_Grimoire_스스로_쓰는_책.md` |
| `SE-N-IIIγ-908` | **2** | `SE-N-IIIγ-908_Sleeping_Block_잠드는_구역.md` (17,944 bytes)<br>`SE-N-IIIγ-908_Unwaking_Block_잠드는_구역.md` (18,409 bytes) | `SE-N-IIIγ-908_Unwaking_Block_잠드는_구역.md` |
| `SE-O-IVδ-909` | **2** | `SE-O-IVδ-909_Heirloom_스며든_메아리.md` (30,754 bytes)<br>`SE-O-IVδ-909_Reverberant_스며든_메아리.md` (30,534 bytes) | `SE-O-IVδ-909_Heirloom_스며든_메아리.md` |
| `SE-C-IIIγ-913` | **2** | `SE-C-IIIγ-913_Backward_Hour_카운트다운_시계.md` (18,267 bytes)<br>`SE-C-IIIγ-913_Todesstunde_카운트다운_시계.md` (17,824 bytes) | `SE-C-IIIγ-913_Backward_Hour_카운트다운_시계.md` |
| `SE-O-IIIγ-914` | **2** | `SE-O-IIIγ-914_Driftglass_떠도는_영혼.md` (32,955 bytes)<br>`SE-O-IIIγ-914_Wanderer_Without_a_Destination_떠도는_영혼.md` (33,623 bytes) | `SE-O-IIIγ-914_Driftglass_떠도는_영혼.md` |
| `SE-O-IIIγ-916` | **2** | `SE-O-IIIγ-916_Allhallow_유령의_시간.md` (18,105 bytes)<br>`SE-O-IIIγ-916_Hour_the_Dead_Walk_유령의_시간.md` (18,686 bytes) | `SE-O-IIIγ-916_Allhallow_유령의_시간.md` |
| `SE-N-IIβ-919` | **3** | `SE-N-IIβ-919_Ancestral_Bell-Time_조상의_종-시간.md` (7,269 bytes)<br>`SE-N-IIβ-919_Ancestral_Hour_조상의_시간.md` (18,102 bytes)<br>`SE-N-IIβ-919_Passing_Bell_조상의_시간.md` (18,501 bytes) | `SE-N-IIβ-919_Passing_Bell_조상의_시간.md` |
| `SE-C-IVδ-922` | **2** | `SE-C-IVδ-922_Miasma_우는_안개.md` (18,193 bytes)<br>`SE-C-IVδ-922_Weeping_Fog_우는_안개.md` (17,804 bytes) | `SE-C-IVδ-922_Miasma_우는_안개.md` |
| `SE-O-IIIγ-924` | **2** | `SE-O-IIIγ-924_Anechoic_침묵의_구역.md` (17,768 bytes)<br>`SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md` (18,287 bytes) | `SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md` |
| `SE-O-IIIγ-926` | **2** | `SE-O-IIIγ-926_Fearscape_환각의_격자.md` (18,154 bytes)<br>`SE-O-IIIγ-926_Sky_of_Borrowed_Faces_환각의_격자.md` (18,777 bytes) | `SE-O-IIIγ-926_Sky_of_Borrowed_Faces_환각의_격자.md` |
| `SE-N-IVδ-927` | **2** | `SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md` (18,609 bytes)<br>`SE-N-IVδ-927_Somnophage_꿈의_전염병.md` (18,116 bytes) | `SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md` |
| `SE-C-IIIγ-928` | **2** | `SE-C-IIIγ-928_Forgetting_혼란의_독기.md` (17,914 bytes)<br>`SE-C-IIIγ-928_Lethe_혼란의_독기.md` (18,287 bytes) | `SE-C-IIIγ-928_Lethe_혼란의_독기.md` |
| `SE-N-IIIγ-929` | **2** | `SE-N-IIIγ-929_Barometer_of_the_Dead_haunting_압력.md` (7,325 bytes)<br>`SE-N-IIIγ-929_Dead_Air_유령의_압력.md` (17,768 bytes) | `SE-N-IIIγ-929_Dead_Air_유령의_압력.md` |
| `SE-O-IIIγ-959` | **2** | `SE-O-IIIγ-959_Graveweed_솟아오른_뿌리.md` (29,600 bytes)<br>`SE-O-IIIγ-959_Uprooted_솟아오른_뿌리.md` (29,799 bytes) | `SE-O-IIIγ-959_Uprooted_솟아오른_뿌리.md` |
| `SE-C-IVδ-976` | **2** | `SE-C-IVδ-976_Chainwreathed_스며든_사슬.md` (29,224 bytes)<br>`SE-C-IVδ-976_Willing_Chains_스며든_사슬.md` (29,473 bytes) | `SE-C-IVδ-976_Willing_Chains_스며든_사슬.md` |
| `SE-C-Iα-071b` | **2** | `SE-C-Iα-071b_Blessing_Giver_축복_주는_자.md` (21,984 bytes)<br>`SE-C-Iα-071b_Giver_of_Blessing_축복_주는_자.md` (22,795 bytes) | `SE-C-Iα-071b_Blessing_Giver_축복_주는_자.md` |
| `SE-C-Iα-071c` | **2** | `SE-C-Iα-071c_Apostle_Maker_사도_만드는_자.md` (24,463 bytes)<br>`SE-C-Iα-071c_Maker_of_Apostle_사도_만드는_자.md` (25,689 bytes) | `SE-C-Iα-071c_Apostle_Maker_사도_만드는_자.md` |
