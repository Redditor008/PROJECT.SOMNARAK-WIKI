# Unfinished-Text Register

> *"A file that stops mid-sentence is not a record; it is a note to somebody who never came back to it."*

**Status: reopened.** Every truncation that ends a line has been completed and the end-of-line scan returns zero. A second kind then surfaced that no end-of-line scan can see: a sentence cut mid-clause with another fragment fused onto the same line *after* the break, so the line ends on a full stop and looks finished. **105 of these remain in the dossier wings, across 97 files.** Seven trailing ellipses were read, judged deliberate, and left in place; they are not counted here.

## Final tally

| Class | Fault | Half | Count |
|---|---|---|---|
| **A** | Flavor Text — "At first contact" cut mid-clause | batch | 63 |
| **B** | Story Log origin paragraph cut at "This sorrow …" | batch | 103 |
| **B2** | The same paragraph, cut one sentence earlier | batch | 22 |
| **C** | Identification — Primary marker cut mid-phrase | batch | 31 |
| **F** | `\| **Form** \|` cell cut dead at 150 characters, **no ellipsis** | batch | 30 |
| **E5** | `Threat rating:` fused onto the origin paragraph, itself truncated | careful | 13 |
| **D-unique** | One-off prose truncations, each in a single file | careful | 15 |
| **D-shared** | Six shared Story Log paragraphs, each cut mid-sentence | careful | 35 |
| **G** | Cut mid-clause with a fragment fused after the break — **line does not end in an ellipsis** | mixed | 105 open |
| | **Total completed** | | **312** |

Batch half: 249. Careful half: 63.

## Fix standard applied

Every sentence was completed from the entity's own material in the same file — its form, its site, its element, its recorded effect — and never with a clause reused from another dossier. Where a line fused two fragments, the fragments were separated and each given its own field; in every such case the half that had been hidden turned out to be truncated as well.

Division of labour follows `RULES/R-18`. **Batch-short** meant the completing text already existed in that file. **Careful-detail** meant it had to be written, one file at a time.

## Notes on each class

**A — 63.** Sixty-one completed from each entity's own recorded form; two carried a description found nowhere else in their file and were written individually.

**C — 31.** Identification markers restored from each dossier's Physical Form entry. Taken first because an instruction for recognising an entity is read at the moment of contact, and one that stops mid-phrase is unusable exactly then.

**B — 103, B2 — 22.** Origin paragraphs completed from each file's Expanded origin context, so the closing cadence matches that entity's element. B2 is the same fault cut one sentence earlier; it survived the first pass because the surviving text ended on a lower-case *but* while the scan was anchored on a capital.

**E5 — 13.** Thirteen B lines had a `Threat rating:` field fused onto the end. Separating them exposed thirteen further truncations underneath. Each was completed from that entity's recorded Sorrow and Secondary Effect.

**F — 30.** Thirty `| **Form** |` cells were cut dead at 150 characters, mid-word, with no ellipsis of any kind — invisible to every scan built to look for one. Found by diffing the cell against the file's own `**Primary Form:**`, which held the full text in all thirty cases.

**D-unique — 15.** Eleven Story Log and Archive Note paragraphs written out individually, and four Flavor Text lines whose trailing form description was restored from their own Primary Form.

**D-shared — 35.** Six paragraphs that appeared word for word across many dossiers and stopped mid-sentence in all of them. Completing them with one shared ending would have cleared thirty-five ellipses and left the archive worse, since the truncation was the only thing marking the paragraph as boilerplate. Each was replaced with prose written for its own entity: the Compass corridor where instruments agree with a bone needle instead of north, the willow enclosure that has to be swept, the clock that stops when a debt comes due and makes the silence the event.


## Class G — mid-line truncation (open)

The break is in the middle of the line. A fragment of unrelated field text was fused on after it, so the line terminates in a full stop and reads as complete until it is read as a sentence. One example, repaired during the Sleeping Shard clean, ran `…But this sorrow was different. This sorrow was …  Threat rating: Per entity classification.`

This is the second time a defect in this archive has been invisible to the scan built for it, after the thirty `| **Form** |` cells cut at 150 characters with no mark at all. The lesson is recorded in `RULES/R-18`: when a scan is written around a symptom, it will find only the cases that show the symptom.

Outside the dossier wings the same pattern appears in Story Cantos and Master Codices, where most instances are deliberate dialogue ellipses and are not counted here.

### Families

| Tail fused after the break | Count |
|---|---|
| `Threat rating: Per entity classification` | 22 |
| `. The space does not become generic; it ` | 17 |
| `Then the moment passes, and you are left` | 7 |
| `heavy. Its sorrow bleeds into everything` | 6 |
| `be near it. The R.D. has noted this beha` | 6 |
| `opens a door. A door that most people ke` | 5 |
| `It is the same element in a different la` | 5 |
| `The space does not become generic or abs` | 5 |
| `. The first sensation is always Lament —` | 3 |
| `The void pressure is present, but it doe` | 3 |

### Files

| File | Line | Text around the break |
|---|---|---|
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md` | 307 | … thin, dry, translucent, and the color of old.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-016_The_Echo_Compass_메아리_나침반.md` | 132 | …cult. The entity is not hostile. It is simply... heavy. Its sorrow bleeds into everything around it, contaminating  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-036_The_Cracked_Hourglass_금이_간_모래시계.md` | 135 | …cult. The entity is not hostile. It is simply... heavy. Its sorrow bleeds into everything around it, contaminating  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-021_The_Hollow_Choir_빈_합창단.md` | 309 | …hereal voices filling a specially constructed.... The first sensation is always Lament — unmistakable, specific, im |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-081_The_Hollow_Saint_빈_성자.md` | 297 | …absence. Its hands reach toward nearby people.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-140_Weeping_Willow_우는_버드나무.md` | 131 | …e these changes directly. Its presence simply... opens a door. A door that most people keep shut. The door to their |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-912_Eleven_Fifty-Nine_슬픔의_시간.md` | 248 | …in the Mantle Commons — between 0300 and 0400... It is the same element in a different language, and the language i |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-913_Backward_Hour_카운트다운_시계.md` | 271 | …d that recurs irregularly in Zone B, during w... Then the moment passes, and you are left with the pressure, the re |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-921_Cracked_Flesh_균열의_들판.md` | 257 | …yone who stands for more than three minutes d... The space does not become generic or abstract; it changes in the s |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-928_Lethe_혼란의_독기.md` | 273 | …n the lower levels of Zone C, causing progres... The void pressure is present, but it does not behave like standard |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-048_Hums_노래하는_돌.md` | 135 | …cult. The entity is not hostile. It is simply... heavy. Its sorrow bleeds into everything around it, contaminating  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-099_The_Masked_Dancer_가면_무용수.md` | 134 | …e these changes directly. Its presence simply... opens a door. A door that most people keep shut. The door to their |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-099_The_Masked_Dancer_가면_무용수.md` | 317 | …ask. It dances continuously, with precise and.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-102_Frozen_Tear_얼어붙은_눈물.md` | 132 | …e these changes directly. Its presence simply... opens a door. A door that most people keep shut. The door to their |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-235_Panopticon_벽_속의_감시자.md` | 131 | …tainment unit, not to study it, but to simply... be near it. The R.D. has noted this behavior and classified it as  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-245_Midnight_Choir_노래하는_벽.md` | 131 | …e these changes directly. Its presence simply... opens a door. A door that most people keep shut. The door to their |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-775_Cleaved_찢어진_탑.md` | 297 | …it vertically. Its upper half leans toward an.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-782_Flotsam_번져가는_유물.md` | 297 | … the skin. It appears as a red outline around.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-906_Grimoire_스스로_쓰는_책.md` | 327 | …ll themselves with ink that seeps from the bi... The grudge pressure is present, but it does not behave like standa |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀.md` | 307 | …dy burns bright red and orange, and her voice.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md` | 308 | …crystallized memories. Its webs are spun from.... The first sensation is always Void — unmistakable, specific, impo |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-073_The_Hollow_Knight_빈_기사.md` | 308 | …e. The armor itself is the entity. It patrols.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-091_The_Lost_Prince_잃어버린_왕자.md` | 308 | …own made from crystallized tears. He flickers.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-175_Somnium_꿈의_직공.md` | 297 | …am-threads. Its face changes according to the.... The first sensation is always Lament — unmistakable, specific, im |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-240_Broken_Clocktower_부서진_시계탑.md` | 132 | …e these changes directly. Its presence simply... opens a door. A door that most people keep shut. The door to their |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-255_Hollow_Architect_빈_건축가.md` | 131 | …tainment unit, not to study it, but to simply... be near it. The R.D. has noted this behavior and classified it as  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-255_Hollow_Architect_빈_건축가.md` | 293 | …rk crystal. It builds continuously, but every.... The first sensation is always Weight — unmistakable, specific, im |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-092_Pyre_of_Truths_타오르는_도서관.md` | 303 | …t this sorrow was different. This sorrow was …  Threat rating: Low. The Library burns perpetually with forbidden tr |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-165_Candela_녹아내리는_성자.md` | 280 | …nderstood. The entity has become more than a …  Threat rating: Low. The Saint melts between present and future grie |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-222_Patina_녹슨_무게.md` | 318 | …. But this sorrow was different. This sorrow …  Threat rating: Low. Corroded ground from inherited resentment. Effe |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억.md` | 131 | …tainment unit, not to study it, but to simply... be near it. The R.D. has noted this behavior and classified it as  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억.md` | 280 | …inment unit, not to study it, but to simply. …  Threat rating: Low. Holds the final thoughts of every citizen who d |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-250_Restless_Gap_찢어진_흔적.md` | 282 | …. But this sorrow was different. This sorrow …  Threat rating: Low. A person-shaped gap from Han-fractured memories |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-255_Rising_Wall_솟아오른_벽.md` | 276 | …t this sorrow was different. This sorrow was …  Threat rating: Low. A wall of one-sided remembering. Effect: proxim |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-357_Sleeping_Weight_잠든_무게.md` | 276 | …t this sorrow was different. This sorrow was …  Threat rating: Low. A worker braced beneath a beam, eternally holdi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-505_Cold_Burn_얼어붙은_그림자.md` | 282 | …t this sorrow was different. This sorrow was …  Threat rating: Low. A shadow guarding an empty vault. Effect: proxi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-668_Frozen_Fury_얼어붙은_잔해.md` | 318 | …t this sorrow was different. This sorrow was …  Threat rating: Moderate. The Ruin rages in cold stasis. Effect: pro |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-907_Breathing_Stone_살아있는_벽.md` | 248 | …C that has become flesh — warm, pale, and fai... The weight pressure is present, but it does not behave like standa |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-909_Labyrinth_of_the_Unfinished_Mind_생각의_미로.md` | 250 | … C that reconfigures its corridors based on t... It is the same element in a different language, and the language i |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-918_Ninety_Seconds_반복되는_생각.md` | 248 | …ndefinitely for anyone caught within its radi... The void pressure is present, but it does not behave like standard |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-922_Miasma_우는_안개.md` | 273 | …e lower corridors of Zone D without warning. ... It is the same element in a different language, and the language i |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-923_Hatred_Above_분노의_폭풍.md` | 248 | …ove Zone C that generates localized fury in a... It is the same element in a different language, and the language i |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-150_Risus_웃음의_메아리.md` | 131 | …tainment unit, not to study it, but to simply... be near it. The R.D. has noted this behavior and classified it as  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-247_Torn_Flower_찢어진_꽃.md` | 293 | …plit petals. It appears in cracks between old.... The first sensation is always Grudge — unmistakable, specific, im |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-300_Sorrow_Seed_슬픔의_씨앗.md` | 131 | …tainment unit, not to study it, but to simply... be near it. The R.D. has noted this behavior and classified it as  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-900_Vellum_Man_잊혀진_이야기꾼.md` | 271 | … shimmers when spoken to — its body is a manu... The space does not become generic or abstract; it changes in the s |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Vγ-260_Sorrow_Tide_한의_조수.md` | 131 | …tainment unit, not to study it, but to simply... be near it. The R.D. has noted this behavior and classified it as  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Vδ-010_The_Convergence_수렴.md` | 312 | …rding Birds. Wings combine with wings, scales.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Vδ-265_Forgotten_God_잊혀진_신.md` | 299 | …ng in the sealed vault beneath the Alpha Tree..... The space does not become generic; it shifts in the specific reg |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIβ-155_Harbinger_추징관의_그림자.md` | 131 | …cult. The entity is not hostile. It is simply... heavy. Its sorrow bleeds into everything around it, contaminating  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIγ-184_Redacted_잊혀진_나무.md` | 82 | …r you should — but the memory of it is simply... not there." \| [The Tree's erased history creates a void in the tar |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIγ-908_Unwaking_Block_잠드는_구역.md` | 271 | …lock in Zone D where every inhabitant fell as... Then the moment passes, and you are left with the pressure, the re |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIγ-917_Dawn_That_Forgot_잠드는_새벽.md` | 248 | …ke the city. The sun rises, the sky lightens,... The space does not become generic or abstract; it changes in the s |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIγ-929_Dead_Air_유령의_압력.md` | 248 | … causes the dead to become briefly, tangibly ... It is the same element in a different language, and the language i |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIα-125_Hollow_Echo_빈_메아리.md` | 131 | …cult. The entity is not hostile. It is simply... heavy. Its sorrow bleeds into everything around it, contaminating  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIβ-280_Kind_Healer's_Shadow_치유자의_그림자.md` | 131 | …cult. The entity is not hostile. It is simply... heavy. Its sorrow bleeds into everything around it, contaminating  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIβ-903_Glass_Elsewhere_환영의_거울.md` | 304 | …or whose surface ripples like water. It does ... Then the moment passes, and you are left with the pressure, the re |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIβ-910_Moktak_조상의_전당.md` | 248 | …he city’s founding families once gathered. Th... And the weight is there, unmistakable, but wearing a shape you hav |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIβ-919_Passing_Bell_조상의_시간.md` | 271 | …ch the voices of the dead become audible in Z... The space does not become generic or abstract; it changes in the s |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-159_Apnea_얼어붙은_한숨.md` | 282 | …. But this sorrow was different. This sorrow …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-315_Collapsed_Seed_무너진_씨앗.md` | 331 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-339_Breach_무너진_벽.md` | 282 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-489_Forgotten_Silence_잊혀진_침묵.md` | 278 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-517_Broken_Tear_부서진_눈물.md` | 278 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-525_Cenotaph_흐르는_다리.md` | 286 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-606_Banyan_가라앉은_나무.md` | 312 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-821_Pent_사라진_한숨.md` | 294 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-852_Conservatory_잊혀진_잔해.md` | 320 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-909_Dormant_Monolith_잠든_기둥.md` | 274 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-909_Dormant_Monolith_잠든_기둥.md` | 291 | …s. Its surface is pale and its shadow reaches.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md` | 271 | …ds through proximity in Zone D. One person fa... The space does not become generic or abstract; it changes in the s |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-967_Pandoras_Jar_사라진_유물.md` | 278 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-967_Pandoras_Jar_사라진_유물.md` | 295 | … an object that no longer exists. Its fire is.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-Iα-025_The_Silent_Child_조용한_아이.md` | 310 | … of sight. The Child makes no sound and often.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-Iα-519_Mourning_a_Life_I_Never_Lived_스며든_씨앗.md` | 81 | … "Where the seeds landed, the floor is simply... gone." \| [The Seeds sprout into patches of void; the target's foot |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-N-Iα-905_Lacrima_영혼의_그릇.md` | 328 | …pt for the faint light that leaks from beneat... And the void is there, unmistakable, but wearing a shape you have  |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-920_Once_Upon_이야기의_시간.md` | 247 | …which every forgotten story ever told within ... Then the moment passes, and you are left with the pressure, the re |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md` | 270 | …us in the Desolate where sound does not exist... Then the moment passes, and you are left with the pressure, the re |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-926_Sky_of_Borrowed_Faces_환각의_격자.md` | 270 | …Desolate where the air itself projects images... Then the moment passes, and you are left with the pressure, the re |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIδ-011_Scar_Walker_흉터의_행자.md` | 307 | … rage. It carries a weapon of solidified fury.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIβ-235_Myrmidon_찢어진_영혼.md` | 298 | … in its chest. Its outline flickers as though.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIβ-914_Amnesia_잊혀진_일분.md` | 249 | …59 and 1200 on an unmarked day — during which... The void pressure is present, but it does not behave like standard |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-115_Broken_Fragment_부서진_파편.md` | 315 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-151_Border_Tree_스며든_나무.md` | 311 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-168_Quagmire_무너진_흔적.md` | 319 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-190_Ember_Phoenix_불사조.md` | 277 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-190_Ember_Phoenix_불사조.md` | 294 | …ash. It burns, dies, and reforms from its own.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-693_Spreading_Root_스며든_뿌리.md` | 277 | …. But this sorrow was different. This sorrow …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-762_Grasp_타오르는_다리.md` | 279 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-844_Repose_잠든_잔해.md` | 281 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-851_Shard_of_a_Broken_Promise_부서진_조각.md` | 319 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-895_Survivors'_Breath_떠도는_한숨.md` | 281 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-897_Welcome_Haven_부서진_벽.md` | 281 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-909_Heirloom_스며든_메아리.md` | 289 | …t this sorrow was different. This sorrow was …  Threat rating: Per entity classification. See SECC Classification t |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-930_Once_Told_살아_있는_서사.md` | 247 | … the deep Desolate where stories told aloud b... Then the moment passes, and you are left with the pressure, the re |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-Iα-126_Anonym_녹아내린_조각.md` | 298 | …a figure made from pale fragments. It watches.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-Iα-453_Floating_Fragment_떠다니는_파편.md` | 290 | …ht, sometimes forming the outline of a crying.... The first sensation is always Lament — unmistakable, specific, im |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-Iα-720_Aphasia_녹아내린_속삭임.md` | 302 | …ed shape — it flows across the floor in a low.... The space does not become generic; it shifts in the specific regi |
| `SOMNARAK-WORLD/Sorrow_Entities/SE-O-Vγ-003_Wilderness_Tide_야생의_조수.md` | 246 | …lderness. Not an entity. Not a creature. Just... a shape. Vast. Dark. Watching.* |
| `SOMNARAK-WORLD/Unknown_Entities/Book_of_Regressor_Log_Dramaturgy.md` | 197 | … the second rememberer again (*oh, you too?* … *yes, yes!*) and make a promise the loop will almost certainly unmak |
| `SOMNARAK-WORLD/Unknown_Entities/Book_of_Regressor_Log_Dramaturgy.md` | 238 | …retend I do not turn the pages with a certain... ease. The survivor has begun, in the nine hundred and sixty-sixth  |
| `SOMNARAK-WORLD/Unknown_Entities/SE-C-IVδ-251_The_Unspoken_Line_그어진_선.md` | 255 | …found my boy's grief and lifted it, and I was... lighter. Brighter. And she wasn't. I stopped crossing because I di |
| `SOMNARAK-WORLD/Unknown_Entities/SE-N-IIIβ-247_The_Undelivered_Thanks_전하지_못한_감사.md` | 245 | …niture. The thanks had nowhere to go. It just... stayed. And then it wasn't mine anymore. It was everyone's." — Ise |
| `SOMNARAK-WORLD/Unknown_Entities/SE-N-IVδ-901_The_Mewgical_Girl_야옹_마법소녀.md` | 81 | …*Shu Shu · Multi-Bomb Volley**] } \| ""Ahuhuhu... have an appetizer, dearies!" — and five to eight cheap pirated fus |
| `SOMNARAK-WORLD/Unknown_Entities/SE-N-IVδ-901_The_Mewgical_Girl_야옹_마법소녀.md` | 103 | …After the opening line (*"Ahuhuhu... alright, dearies!"*), the track **MAGICAL MEW!!** plays as backgro |
