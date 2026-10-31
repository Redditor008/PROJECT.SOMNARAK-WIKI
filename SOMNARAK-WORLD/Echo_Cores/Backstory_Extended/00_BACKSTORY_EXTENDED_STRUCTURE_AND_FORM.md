# Echo-Core Backstory Extended — Structure and Form Standard

**Status:** 📌 **STRUCTURE FILED — prose not started; no Echo-Core activated**  
**Folder:** [`README.md`](README.md)  
**Parent archive:** [`../README.md`](../README.md)  
**Canonical baseline:** the nine dossiers in `SOMNARAK-WORLD/Echo_Cores/`  
**Filed:** 2026-10-31

> This file defines **how** an Echo-Core Backstory Extended record is built. It does not contain story prose, does not activate a character, and does not amend any canonical dossier. The first character file is created only after the owner names that character.

---

## I. Purpose

`Backstory_Extended/` exists to give the nine Echo-Cores the kind of scene-level history that a personnel dossier cannot hold: formative events, first meetings, failures, private routines, ordinary days that later became load-bearing, and the moment a habit turned into policy.

The functional model is Lobotomy Corporation's named-character story treatment: history unfolds through episodes tied to the character's department and the institution that shaped them. The comparison stops at function. No L Corp plot, scene order, dialogue, character, or imagery is copied into a Somnarak record.

The standard answers four questions before prose begins:

1. **What time is being written?** — PAST, LOOP-PAST, or FLASHBACK.
2. **Through whose eyes?** — FPV, TPV, or SPV.
3. **In what writing style?** — FULL STORY, DIALOGUE, or BOTH.
4. **What does it connect to?** — the featured Echo-Core, the Reverie Directorate, or both.

---

## II. Authority and rule stack

When sources disagree, the higher tier wins:

| Tier | Source | Governs |
|---:|---|---|
| 1 | The featured Echo-Core's canonical dossier and its directly linked records | Facts: identity, chronology, floor, authority, armament, relationships, capabilities, limits |
| 2 | `The_Absolvohan` Parts 1–9 | Exact present-day anchor lines, speakers, day numbers, and scene order |
| 3 | This standard | File arrangement, category, POV, style, appendix, and evidence labels |
| 4 | Owner-supplied Unified Narrative Writing Rules | Prose craft, scene construction, dialogue discipline, banned phrasing |
| 5 | `REFERENCE_SOMNARAK_WIKI/RULES/R-31_CHATROOM_READABILITY.md` | Chat reporting **outside** story files only |

Two delivered rulings are explicit:

- **Chapter Rule — OFF.** No Act, Chapter, or Part labels. No one-Part-per-response delivery. No one-file-one-chapter structure. Length follows filed beats and scene completeness.
- **Chatroom Rule — OFF for story `.md` files.** No chat-first draft requirement, no `.md` versus `.txt` question, and no R-31 report format inside the story body. When a character is activated, write the planned repo `.md` directly, then validate and gate under repo rules.

R-31 Compact Report v2 still governs the chat summary of the work, not the story text.

---

## III. The unit

One Echo-Core, one file, one archival framed mini-story.

- The nine canonical dossiers stay where they are. They are not moved, replaced, merged into the new file, or silently synchronized.
- The extended file is a **new layer**, not a second dossier.
- A file may be long or short. It ends when its filed beats are complete, not at a fixed chapter count.
- A file is complete only when its **Prologue Record**, its **trigger modules**, and its **Present Consequence** form one unbroken Connection String.
- A file may not contradict a canonical fact. If a source conflicts with another source, the conflict is filed as **HOLD**, never averaged into one smooth history.

---

## IV. Time categories

### IV.1 The three categories

| Category | Time covered | Definition |
|---|---|---|
| **PAST** | Before Year 4,232 begins | Human life, formation, construction, recruitment, early R.D. service, first appointment. Direct scene from earlier life. |
| **LOOP-PAST** | Cycles 1–1,777 | A prior iteration of Year 4,232. The same calendar day under different conditions, or an event that no longer exists in the current cycle's record. |
| **FLASHBACK** | Present-day container | A present trigger opens PAST and/or LOOP-PAST, then returns to the present with a changed action. |

**PAST and LOOP-PAST are time layers. FLASHBACK is the doorway between them and the present.**

A flashback may carry one category or both. A file may use one, two, or all three categories. There is no quota and no required order beyond the Prologue.

### IV.1b The Malkuth spine — the owner's model

The owner supplied `Malkuth#Backstory` on the Lobotomy Corporation wiki as the reference for what a good backstory treatment looks like. The functional shape is:

**Pre-break → Break → Post-break**, with the same past shown twice.

| Movement | What it holds |
|---|---|
| **Pre-break** | The wound as it happened, and the present-day behaviour it produced. PAST scenes interleaved with present anchors. |
| **Break** | The in-world event that changes the meaning of the past. Not a chapter marker: a mechanism, a document, a reveal, a suppression, a confession. |
| **Post-break** | The same past memory shown again, re-read. The events do not change. The meaning does. The file ends on a stance, not a cure. |

Three rules follow, and they are mandatory:

1. **One wound, examined twice.** A backstory file is not a life story. It is one formative injury or misreading, followed through everything it caused, and then revisited after the character's understanding of it changes. Choose the wound before choosing the scenes.
2. **The double exposure.** At least one past scene must appear in both movements. The second appearance uses the same place, objects, and words; what changes is what the character notices in them. If the re-exposure has different content, it is not a re-exposure.
3. **The obliquely spoken wound.** The character must at least once describe their own injury in the present, out loud, to someone who was not there — as a question, an anecdote, or a demonstration rather than a confession. The register matters: they do not say *I was hurt.* They ask the other person whether they have ever felt something adjacent. A second witness may supply the counter-memory from outside and admit the failure plainly.

The model's ending is a stance, usually stated in a short phrase. Majin's is *willingness*; Malkuth's is *the willingness to stand up straight.* The stance is not resolution and must not be written as one.

The model does **not** license copying. Its plot, characters, and imagery stay in Lobotomy Corporation. Only the shape is used.

The full evidence base — thirteen character records read page by page, with the machine taken apart — is filed as [`00A_L_CORP_BACKSTORY_RECORD_RESEARCH.md`](../../../PROJECT_MOON_RESEARCH/CROSS_VERSE/00A_L_CORP_BACKSTORY_RECORD_RESEARCH.md). It lives **outside `SOMNARAK-WORLD/`**, in `PROJECT_MOON_RESEARCH/CROSS_VERSE/`, because it describes another universe's canon and the world bible holds none. Read it with this section; it is the survey, this is the rule.

### IV.1c The six devices the survey added

The source survey found six devices used in every one of the thirteen records. They are mandatory, and they are what separate a record from a chronology.

| Device | Rule | Test |
|---|---|---|
| **The object** | One working object appears before the break and again, identical, after it. It is not a symbol on first appearance and is never explained. | Can the reader name the object, and the two scenes it appears in? |
| **The withheld sentence** | The second pass restores a specific sentence that a specific person chose not to say — not a fact the reader lacked. | Is the missing thing a *decision to stay silent*, and is the person who made it named? |
| **The counter-witness** | A character outside the featured Echo-Core states the failure plainly, in their own voice, with no softening. | Is the witness an existing dossier character, and do they admit it in one unhedged sentence? |
| **The permanent symptom** | One behaviour, unchanged from the first present-day scene to the last, proving the wound still operates in routine rather than in crisis. | Would a colleague describe this character by this behaviour alone? |
| **The oblique speech** | The wound described out loud, in the present, to someone structurally unable to help — as a question, an anecdote, or a demonstration. | Does the listener have any power to act on it? They must not. |
| **The stance line** | The file ends on a named capacity in the record's own vocabulary. Not a resolution, not a lesson, not a summary. | Is it a thing the character can *do* inside a situation that has not changed? |

Two corollaries:

- **The routine-voice check.** After the stance, the character's ordinary professional lines must have shifted by exactly one degree. If the voice after the break is identical to the voice before it, the stance is decoration and the file is not finished.
- **The Ayin failure.** A record whose central figure never takes a posture ends as a case history. Explanation is not a stance. Dissolution is not an ending.

### IV.2 Universal participation, unequal memory

Every Echo-Core lived through the prior 1,777 iterations. **Participation is universal. Memory is not.**

A character who does not retain the loop still experienced it. Their prior-cycle scene is therefore legitimate. What changes is the **access route**:

- direct retained memory;
- archive retrieval;
- data comparison;
- Maw or passenger testimony;
- sensor and transmission records;
- Majin's recollection;
- bodily residue, repetition, or déjà vu;
- reconstruction by an identified in-world compiler.

The knowledge gate is mandatory:

> **How does the featured Echo-Core experience, remember, or access this scene now?**

If the answer is "they remember it," the dossier must grant that memory.

### IV.3 Loop knowledge matrix

| Echo-Core | Loop participation | Canonical access | How LOOP-PAST may be delivered |
|---|---|---|---|
| **Majin** | Yes | Full retained chronology | Direct prior-cycle scenes, or his recollection used as another character's access frame |
| **Seiyon** | Yes | Remembers all 1,778 Cycles | Direct prior-cycle scenes, including exact repeated moments |
| **Ayshuk** | Yes | Full knowledge of the count and mechanics; not Seiyon's exhaustive subjective recall | Data comparison, experiment records, prior-cycle observations |
| **Marjuk** | Yes | Full knowledge; preserves records from every iteration | Archive retrieval — his own prior notes, records, and vault material |
| **Dekan** | Yes | Partial; mediated through the Maw and classified briefings | Maw testimony, pressure, repetition, déjà vu, Majin-frame |
| **Zyrak** | Yes | Partial; inferential | Extraction logs, registry patterns, repeated procedure, Majin-frame |
| **Mellda** | Yes | Partial; embodied through the passenger | Passenger sensation, Desolate change, Majin-frame |
| **Ishall** | Yes | Comparative access through signals and records; not continuous lived memory | Received transmissions, prior-cycle logs, message archives, Majin-frame |
| **Xyan** | Yes | Outside normal suppression; memories not wiped; Gate time unresolved | Direct exile continuity, with a standing time HOLD |

### IV.4 Majin's Footnote

The owner correction that makes non-retaining characters writable:

> **Majin remembers the event. He does not remember why it mattered. The story gives the "why" back to the character.**

The pattern:

1. A present Absolvohan moment makes Majin recall a prior-cycle event.
2. His memory is thin and operational — a timestamp, a name, a logged deviation, a line in a report.
3. To Majin it was minor, routine, or one of 1,778 similar entries.
4. To the featured Echo-Core it was defining.
5. The scene shows the character's experience without letting Majin's indifference set its value.
6. The present returns through a habit, aversion, ritual, or object that carries the consequence.
7. Majin need not learn what it meant. The reader does.

Majin supplies the access. The featured Echo-Core supplies the weight.

### IV.5 The unremembered loop

For characters without retained loop memory, the strongest form is:

1. **Present anchor** — a filed Absolvohan day.
2. **Artifact or testimony** — Majin's recollection, a sealed log, a system playback, a transmission archive.
3. **Embedded loop-past** — rendered in the artifact's POV.
4. **Receipt** — the featured character receives it. The lack of memory is the event.
5. **Trace** — they act on a consequence they cannot explain.

The access route must be legal at that anchor. A sealed record does not open because the plot needs it.

---

## V. Point of view

POV is selectable per scene. A file may use one, two, or all three modes.

| Mode | Person | Use for | Core limit |
|---|---|---|---|
| **FPV** | First — "I", "we" | Confession, testimony, private logs, owned memory, direct interiority | Only what the narrator knows, perceives, or believes |
| **TPV** | Third — "he", "she", "they" | The default archival narrative when the character would not write or speak the scene | Limited to one character per scene; not omniscient |
| **SPV** | Second — "you" | Induction, protocol, debrief, interrogation, memory playback, a letter or transmission to a named holder | "You" must have an in-world addressee and an identifiable speaker |

### V.1 FPV

- The narrator is a named character or a named document author.
- A retrospective "I" must have a defined narrating present — a debrief, a later archive entry, a letter written after the fact.
- A non-retaining character cannot say "I remember that cycle." They may say "I was told," "the record says," or "I have dreamed it." The appendix marks the difference.

### V.2 TPV

- Limited to one character per scene.
- The POV bearer is named in the appendix.
- TPV may be **close** (interior access) or **camera** (external only). If camera, mark it, because interiority is deliberately withheld.
- A TPV loop-past scene still needs an access frame: Majin's memory, a record, testimony, or a reconstruction.

### V.3 SPV

- "You" must have an in-world addressee: the featured Echo-Core, a named character, or a defined role.
- The implied speaker must be identifiable: archivist, system, Director, counselor, successor, the character's recorded voice, the facility. Unknown speaker = **HOLD**.
- **Never the reader.** No fourth-wall address.
- "You remember" requires memory rights. "You are being told" does not grant memory.

SPV is the natural mode for the owner correction:

> **You do not remember this. The record does.**

### V.4 Five POV laws

1. **POV is a lens, not a memory grant.**
2. **One POV bearer per scene.** Switches happen only at a scene break or an in-world artifact boundary.
3. **The featured Echo-Core remains the weight holder.** If a scene becomes about Majin's feelings rather than what the featured character carries, it belongs in Majin's file.
4. **"You" always has an in-world address.** The speaker must be identifiable or marked HOLD.
5. **Reliability is recorded, not smoothed.** Every scene is marked **Canon fact**, **Character belief**, **In-world record claim**, or **HOLD**.

### V.5 Recommended POV palette

Not binding. A starting point, not a prohibition.

| Echo-Core | Strongest fit |
|---|---|
| **Majin** | FPV for his own file; TPV for others observing him |
| **Seiyon** | FPV; SPV when the system addresses her as a system |
| **Dekan** | TPV; SPV for containment protocol; FPV only for owned memory |
| **Zyrak** | FPV extraction log; TPV |
| **Ayshuk** | TPV clinical; SPV research protocol; FPV only for records he owns |
| **Mellda** | FPV for body and passenger; TPV for command scenes |
| **Marjuk** | FPV archive notes; SPV archive instruction |
| **Ishall** | FPV intercept log; TPV |
| **Xyan** | FPV exile log; SPV transmission to a named recipient |

---

## VI. Writing styles

Style is how the scene's language is built. It is not the same thing as **form**, which is what the document is: archival record, transcript, log, letter, oral record, debrief, or notification.

A file declares a **primary style** and may switch style at a module boundary. A module records its actual style. No file must use all three.

### VI.1 FULL STORY

Continuous narrative prose. Dialogue appears when a scene needs it, but the scene is carried by narration, action, sensation, and interiority.

Rules:

- The POV bearer is fixed for the scene.
- Dialogue uses `[Character Name]` speaker-first format when it appears.
- No summary standing in for a scene the character is present for.
- Description is filtered through the POV bearer's attention, not a camera catalogue.
- Best for: embodiment, physical work, isolation, the moment before a report is spoken, aftermath, and any scene where what is **not** said is the subject.

### VI.2 DIALOGUE

The scene is carried by spoken exchange.

Rules:

- Dialogue uses `[Character Name]` speaker-first format.
- Action beats are minimal, physical, and load-bearing: a hand on a rail, a page closed, a gauge tapped, a door held.
- No omniscient narration inside the exchange.
- A DIALOGUE module still has a POV bearer, or is presented as an in-world transcript with a named recorder, channel, or compiler.
- Stage directions may not explain feeling the line already carries.
- Best for: command exchanges, interviews, testimony, debriefs, formal objections, oral records, interrogations, and scenes where two people are deciding something aloud.

The Absolvohan daily `Story — Dialogue` sections are the closest existing model: a short exchange under a day heading, with brief prose stage direction and the decision left visible in what each speaker will and will not say.

### VI.3 BOTH

Prose and dialogue alternate inside a scene or across a module.

Rules:

- Every switch is carried by a physical action, an artifact boundary, or a time break — never by ornament.
- The prose does not repeat what the dialogue just established, and the dialogue does not repeat what the prose just narrated.
- A BOTH module may open in prose, turn on a line, and close in prose, as long as the return changes the action.
- This is the default for long modules where work and speech are inseparable.

### VI.4 Style ledger rules

- Style is recorded per scene in the appendix.
- A file's primary style is declared once, in the seal or the appendix header.
- A file may be entirely DIALOGUE if the record is a transcript, entirely FULL STORY if the record is a narrative history, or BOTH if the evidence requires both.
- Style never changes knowledge, POV, or the connection string.
- A DIALOGUE scene without a POV bearer must identify its recorder or compiler; otherwise it is **HOLD**.

---

## VII. Connection String Rule

No unit exists on its own. Every scene, document, memory, object, or witness account carries at least one tether.

| Code | Tether | Test sentence |
|---|---|---|
| **C** | Character | "This explains why **[Echo-Core]** does, fears, refuses, or carries **[specific thing]**." |
| **R** | Directorate | "This explains why the **R.D.** has **[specific floor, protocol, doctrine, law, ritual, or failure]**." |
| **C/R** | Both | Both sentences can be written without strain. |

If neither sentence can be written, the unit is **orphan lore** and does not belong in the file.

Per unit, one tether is enough. Across a completed file, both should appear, because every Echo-Core is simultaneously a person and an office.

### VII.1 Two audit rules

**No orphan rule.** Every module must pass the C or R test sentence. If it cannot, it is cut or marked HOLD.

**No dead-end rule.** Every module must eventually reach either:

- a present consequence in the featured character's behavior; or
- an institutional consequence in the R.D.'s structure.

A beautiful past scene that changes nothing in the present is not backstory. It is a vignette, and it does not pass.

### VII.2 String format

Each file carries one primary string in the appendix:

```text
PB (C/R)
  → T: trigger
  → M: module [CATEGORY | POV | STYLE]
  → T: trigger
  → M: module [CATEGORY | POV | STYLE]
  → PC (C/R)
```

`PB` = Prologue Record. `PC` = Present Consequence. `T` = trigger. `M` = module.

Worked example, Dekan:

```text
PB (C/R) — the district that could not be contained; his mother's name-anchor during Dream Bleed

→ T (C): the Maw asks, "We want to go home." — Day 101
→ M (LOOP-PAST | Majin FPV | BOTH): a prior cycle where Dekan answered with protocol
     and the log recorded it as a successful containment exchange

→ T (R): the Containment Log is renamed the Sanctuary Log — Day 350
→ M (PAST | Dekan TPV | FULL STORY): the first time he wrote a name where the form asked for a number

→ PC (C/R): in the present he refuses "inmate" language and enters names in the log;
     the floor's containment doctrine now carries his history
```

The reader can trace every jump. Nothing floats.

### VII.3 L Corp parity

In L Corp, a Sephirah's personal history is bound to the department they run and to the Corporation's goal. The story advances the person and the institution at once.

In Somnarak, an Echo-Core's personal history must be bound to their floor's function and to the R.D.'s doctrine — containment, extraction, research, border, archive, intelligence, command.

That gives each file two outputs:

1. **Character output** — why this person behaves as they do.
2. **Directorate output** — why the R.D. is built as it is, and what it cost to build.

---

## VIII. Mandatory Prologue Record

Every Echo-Core file begins with a Prologue Record. It is a record class, used once, before the trigger modules. It is not a chapter label.

Minimum contents:

1. Who they were before the R.D. — or, for constructed characters, the construction and first retained memory.
2. The formative wound, choice, or absence.
3. How they entered the Directorate, were recruited, or were made into an Echo-Core.
4. The first duty that became their floor.
5. One object, phrase, place, or habit that will return later.

The Prologue must establish at least one **C** tether and one **R** tether. It is the only mandatory narrative unit in the file.

The Prologue is always **PAST**. It may use FPV, TPV, or SPV, and FULL STORY, DIALOGUE, or BOTH. It should end at the threshold of the Cycle era, not summarise the whole dossier.

### VIII.1 The Prologue is a doorway, not the past

The Prologue opens the character's history. It does not contain it.

A file whose only PAST material is the Prologue has failed this standard. The owner's ruling is explicit: the past must be **in the story**, as scenes, not compressed into a short introductory glimpse.

Therefore:

- A file must contain **at least one further PAST module** beyond the Prologue, written as a full scene.
- A character with a long, documented history should carry **several** PAST modules — the loss, the fusion, the selection, the founding, the first appointment, the first catastrophe of their office.
- PAST modules may be interleaved with present-day anchors in any order that serves the Connection String. They are not confined to the front of the file.
- A PAST module is not a summary of an era. It is a scene with a place, a time, bodies, objects, speech, and a change.
- Where two PAST modules cover adjacent years, they must be separated by a present-day anchor or a clear time break, so the file does not read as a timeline.
- The Prologue may be short. The past may not be.

Starting points from the canonical dossiers:

| Echo-Core | Prologue spine |
|---|---|
| **Majin** | Early Han research beneath the Alpha Tree; shared work and private life; the Consolihan ends that life |
| **Seiyon** | Construction and inherited memory; the dead researcher whose name she carries; the first morning she greeted him |
| **Dekan** | The district that could not be contained; his mother; the name he was taught to repeat during Dream Bleed |
| **Zyrak** | Debt extraction; the request for a new body; the first extraction performed with manufactured hands |
| **Ayshuk** | The childhood Void; the Inner Sorrow taken; the architect who could not feel what he studied |
| **Mellda** | Ten years as a Warden; the threshold overflow; exile; Efflorescence; the walk back through the Gate |
| **Marjuk** | The Keeper order; the Grand Archive; the Cheongula record; cryogen reconstruction |
| **Ishall** | The Council's hidden specialist; the order to destroy the R.D.; meeting Seiyon; capture and reconstruction |
| **Xyan** | Human life; the forbidden investigation; the Furnace discovery; choosing the Gate |

These are spines, not scripts. Each must be checked against the whole dossier before drafting.

---

## IX. Trigger modules

After the Prologue, the file is not a fixed sequence. Each further unit is a module opened by a trigger, and different triggers produce different kinds of module.

| Trigger | Module it opens | Usual tether |
|---|---|---|
| **Object** — token, tool, page, armband, key | Object-history scene | C |
| **Document** — journal, log, order, registry | Record scene | R, often C/R |
| **Place** — Maw catwalk, Gate 05, archive vault, observation glass | Floor-origin scene | R |
| **Person** — Lost Prince, Specialist Park, Shin, the envoy | Relationship scene | C |
| **Ritual** — blessing count, reading weeks, extraction procedure | Doctrine-in-practice scene | C/R |
| **Body or entity signal** — passenger stirring, marks, pulse | Bond scene | C |
| **Transmission** — Exile message, sensor intercept | Receipt scene | C/R |
| **Institutional event** — threshold, transmutation, revelation | Policy scene | R |
| **Cycle event** — prior iteration, repeated day | Loop-past scene | C |

The Prologue is fixed. The modules are not. A Marjuk file may be mostly document triggers. A Mellda file may be mostly place and body triggers. A Zyrak file may be mostly object and ritual triggers. They should not share an identical module order.

A file needs at least one trigger module beyond the Prologue. It does not need one of every type.

### IX.0 Placement against the spine

Every module is assigned to one of the three movements before drafting:

| Movement | Placement |
|---|---|
| Pre-break | The wound, its first consequences, and the present-day behaviour it explains |
| Break | The single event that changes the meaning; usually one or two modules, never more |
| Post-break | The re-exposure, the changed action, and the stance |

A module that belongs to none of the three is not part of this file.

### IX.1 Scene, not collection

Every module in the body is a **scene**.

A module is not:

- a list of facts about the character;
- a summary of an era with dates attached;
- a montage of moments without a perceiver;
- a dossier section rewritten in prose;
- a sequence of quotations with no body around them;
- a "collections" heading that gathers several unconnected incidents under one title.

A module is a scene when the reader can answer all five:

1. **Where** is this happening?
2. **When**, relative to the other modules?
3. **Who** is present, and through whose perception is it given?
4. **What changes** between the first line and the last?
5. **What is said out loud**, and what is refused?

If a module cannot answer all five, it is a collection and must be broken into scenes or cut. The only permitted non-scene units are the archival seal and the appendix.

---

## X. File architecture

Every file has three parts, in this order.

### X.1 Archival seal

Short institutional metadata in archive voice. It states the record, not its meaning.

Suggested fields:

- **Record class**
- **Holder or collection**
- **Compiler or narrator**
- **Era or cycle**
- **Anchor date or dates**
- **Access condition**
- **Provenance**
- **Reliability**

The seal is not a POV scene. It must not reveal what the body withholds.

### X.2 Narrative body

- Begins with the **Prologue Record**.
- Continues through **trigger modules**, including at least one further **PAST** scene beyond the Prologue.
- Interleaves PAST, LOOP-PAST, and present-day anchors as the Connection String requires; older material may sit beside Day anchors rather than in a block at the front.
- Ends with the **Present Consequence**.
- Uses PAST, LOOP-PAST, and FLASHBACK as the file requires.
- Uses FPV, TPV, and SPV as the file requires.
- Uses FULL STORY, DIALOGUE, or BOTH as each module requires.
- Has no Act, Chapter, or Part labels.

Scene changes are carried by space breaks, dated headings, or in-world artifact headers. An artifact header is a document boundary, not a chapter label.

### X.3 Source and continuity appendix

Required sections:

1. **Scene ledger** — category, POV, style, trigger, tether, access route, weight holder, status.
2. **Source ledger** — each fact tied to the dossier section, Absolvohan part and day, or linked record that files it.
3. **Knowledge boundaries** — what the POV bearer knows, what they do not, and what the narration withholds.
4. **Connection string** — the primary string, written out.
5. **HOLDs** — incompatible accounts preserved side by side.
6. **Promotion Check** — any new canonical claim, kept separate until the owner approves synchronization.
7. **Validation record** — what was checked before gate.

### X.4 Scene ledger columns

| # | Scene | Category | POV | POV bearer | Addressee | Style | Trigger | Tether | Access route | Weight holder | Present trace | Status |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|

Every row ends with a pipe. Status is one of **Canon-anchored**, **Connective scene**, **HOLD**, or **Promotion Check**.

---

## XI. Evidence and invention

### XI.1 Status labels

| Label | Meaning |
|---|---|
| **Canon-anchored** | The event, line, date, or fact is filed in a dossier, a linked record, or an Absolvohan Part |
| **Connective scene** | Invented staging between filed facts; adds no new canonical event, capability, relationship, or outcome |
| **HOLD** | Sources conflict, or the record is insufficient; no harmonisation is attempted |
| **Promotion Check** | A new fact is proposed for canon; it stays out of the story body until approved |

### XI.2 Invention limits

A connective scene may:

- give filed facts scene form;
- stage an unwritten conversation between people who are already connected;
- fill ordinary time between filed events;
- give a filed object, room, or phrase a history consistent with its filed role.

A connective scene may not:

- add an Echo-Core, floor, doctrine, capability, or relationship that no record files;
- change a death, appointment, injury, promotion, or chronology;
- give a character knowledge their dossier denies;
- solve a contradiction by choosing one side silently;
- overwrite a canonical dossier.

### XI.3 Promotion Check

Any proposed new canonical fact is listed in the appendix with:

- the claim;
- the scene that carries it;
- the reason it is needed;
- the dossier or linked record it would amend;
- the owner decision.

Until approved, the story body may present it only as belief, rumour, or an in-world claim by a named source.

---

## XII. Voice, documents, and knowledge

### XII.1 Dialogue format

Ordinary dialogue uses speaker-first format:

```text
[Dekan] The Maw asked for a name today.
[Majin] Whose?
[Dekan] Yours.
```

In-world transcripts, logs, terminal output, and forms may use their native document format instead. A transcript should identify its channel, recorder, or compiler; otherwise it is HOLD.

### XII.1a Unnamed speakers

A speaker who has no personal name in the record is **not labelled with a job title.** A title reads like a name on the page, and it implies a personnel entry the record does not contain. Use the pronoun instead:

```text
[she] He read the directive before he signed it. I want that in the record.
[him] He said "noted."
[unknown] The line went quiet at 04:12.
```

- **`[she]` and `[him]`** — the speaker's gender is fixed by the scene or by the record. Fix it once and do not switch mid-file.
- **`[unknown]`** — the record never establishes the speaker's gender, and the scene does not need one.
- **`[???]`** — the speaker has a name the record knows but withholds. **One question mark per character of that name**, so the length is a readable clue and nothing else leaks: `[?????]` is a five-character name, `[??????]` is six.

Four consequences follow:

1. **No two identical labels in one exchange.** If two unnamed speakers are both `[she]`, attribute in prose or the exchange becomes unreadable.
2. **A title the record uses as a title stays a title.** `[The Original]` is the record's own designation for a figure whose name is unknown everywhere in canon; `[???]` would require a name length that no source supplies, so inventing the count invents evidence.
3. **Reproduced documents keep their own conventions,** but the preamble must say which unnamed speaker is which — e.g. *"Three members present. The senior medic speaks first; the second medic is the younger voice."*
4. **Retroactive.** Files 01 and 02 were conformed to this rule when it was filed; files 03–09 obey it from the first draft.


### XII.2 Documents

If a character reads, hears, or accesses a document, write the exact portion reached — not a summary. Stop at the point where the character stops. Do not supply text the record does not contain.

This applies to:

- the Founder's journal;
- the Final Door's fragments;
- the Furnace record;
- the Cheongula account;
- registry entries;
- containment logs;
- extraction authorisations;
- Exile transmissions.

Where Absolvohan quotes only a fragment, the fragment is the limit. Expanding it into a full invented page requires a HOLD or Promotion Check.

### XII.3 Knowledge boundaries

- A character may not know what the dossier denies them.
- A character may not recognise a symbol, language, or person the record says they have never encountered.
- A narrator may not explain an institution's secret to a character who has not learned it.
- A system may not report data it has no sensor for.
- Majin does not become omniscient in another character's file.

### XII.4 Prose rules

- No fourth-wall awareness. No character knows they are in a record, story, or wiki.
- No editorial gloss inside the body. Explanation belongs in the appendix.
- Open on an active scene, not on a summary of the character's significance.
- Plant what pays off; do not announce the plant.
- Keep literal canon terms legal: **Weight**, **Echo-Core**, **Echoes**, **Han**, **Sorrow**, **Lumen**, **M.A.W.**, **E.G.O.**, and **Fracture** may appear as themselves.
- Adapt the banned-phrase list so it removes cliché, not canon vocabulary.
- Avoid summary where the character is present, and avoid dramatisation where only a record exists.

The owner-supplied Unified Narrative Writing Rules govern sentence-level craft where this file does not.

### XII.5 R-31 boundary

R-31 Compact Report v2 governs the chat report of what was written, validated, and gated. It does not govern the story body. Do not paste report scaffolding, status blocks, or checklists into the narrative.

---

## XIII. Absolvohan anchor map

### XIII.1 What the survey found

Parts 1–9 contain **50 day-opening dialogue sections** and **439 quoted dialogue lines**.

| Speaker | Quoted lines | Share |
|---|---:|---:|
| Majin | 207 | 47.2% |
| Dekan | 42 | 9.6% |
| Seiyon | 38 | 8.7% |
| Ayshuk | 37 | 8.4% |
| Zyrak | 33 | 7.5% |
| Mellda | 30 | 6.8% |
| Marjuk | 25 | 5.7% |
| Ishall | 22 | 5.0% |
| Xyan | 5 | 1.1% |

Thirty-seven sections are Majin plus one other speaker. Thirteen are multi-speaker: Days 1, 5, 7, 12, 17, 21, 25, 45, 69, 108, 117, 160, and 177. Day 160 is the only broad ensemble check-in.

The dominant form is:

> **[Floor] report.** → Majin asks one narrowing question → the anomaly is specified → the Echo-Core's crack appears as an ellipsis, question, or short admission → Majin interprets and orders → "Understood."

The backstory is already hiding in the crack. Majin usually closes the meaning. Backstory Extended branches at that crack, before the report, or immediately after acceptance.

### XIII.2 Where a glimpse can branch

1. **Before the report** — the Echo-Core alone with the instrument, chamber, page, gate, or sensor. Nothing filed changes.
2. **At the ellipsis or broken report form** — the pause is the doorway. Enter through perception, object handling, or one remembered practice, not a biography dump.
3. **At Majin's silence** — "…", "…Noted.", "…I see.", "…Good." Do not fill Majin's mind. Show what the other person does with no answer.
4. **After the order** — follow the Echo-Core back to their floor and let the order become physical work.
5. **In the night vigil** — Parts 2–9 use "Nocturnal Sub-Vault Telemetry & Director's Vigil" or "Night Shift Telemetry & Nocturnal Vigil", timestamped roughly 23:45–03:30. Keep the time and place; move the POV to the Echo-Core after Majin leaves.

### XIII.3 Part structure

| Part | Days | Use |
|---|---|---|
| 1 | 0 | The only long daily dialogue scene: Majin and Seiyon, 23 quoted lines |
| 2 | 1–25 | Office-in-operation introductions for every lead |
| 3 | 29–49 | Procedure begins producing a moral problem |
| 4 | 53–73 | Reports become planetary; first direct challenges to Majin |
| 5 | 77–97 | Documents, marks, signs; the Founder's journal |
| 6 | 101–121 | Strongest pre-break pressure; nearly every lead questions the old reading |
| 7 | 125–145 | Threshold layer; Majin increasingly agrees with evidence |
| 8 | 149–177 | Changed-alert territory; Day 160 ensemble; Day 177 revelation |
| 9 | 350–365 | Post-loop coda; only Dekan, Ishall, and Seiyon receive direct dialogue |

Days 178–349 are the intentionally unexpanded **Quiet Season**. Connective or coda scenes may use that interval only where no major new event is invented and the dossier supports the change.

### XIII.4 Anchor chains

| Echo-Core | Anchors |
|---|---|
| **Majin** | Day 0 "And you?"; Day 1 the Maw repeats his old name; Day 29 the Mother's forgiveness; Day 53 the name in the bedrock; Day 149 the cannon becomes a fountain; Day 365 the first real sunrise |
| **Seiyon** | Day 0 treated as a system, answering as a person; Day 17 counting 1,778 unanswered warnings; Day 108 Protocol 14-B overridden; Day 149 "like rain"; Day 157 counting Zone B as people; Days 360–365 the resets stop |
| **Dekan** | Day 1 the Maw says Majin's name; Day 29 Specialist Park; Day 53 "It's not growing. It's listening."; Day 87 "Math doesn't bleed. We do."; Day 101 and Day 151 "We want to go home" and the thousand under clear water; Day 350 the Sanctuary Log |
| **Zyrak** | Day 5 "It fought me."; Day 31 the Birds want to be whole; Day 60 the Lost Prince and the replaced arm; Day 103 the AY-001 vision; Day 132 the Birds watching forgiveness; Day 170 the merged Trinity |
| **Ayshuk** | Day 5 nine blessings; Day 36 the interrupted tenth; Day 65 "You've said that before."; Day 92 Shin's tenth mark; Day 113 and Day 137 the eleventh blessing and the waiting Healer; Day 155 "It was me" |
| **Mellda** | Day 7 storm and passenger; Day 41 the Desolate rearranging; Day 73 the envoy recognises the passenger; Day 82 the Drift King's token; Day 108 Gate 05 opened; Day 141 the refugee smiths; Day 160 "The border is silent." |
| **Marjuk** | Day 12 the Furnace fragment; Day 49 the word for mercy; Day 77 the Founder's journal; Day 121 "Are we the seed?"; Day 145 the hidden Hand of Change entry; a Quiet Season archive coda |
| **Ishall** | Day 17 the unanswered warning; Day 55 the changed warning; Day 69 the Floor 7 emergency; Day 127 the fourth message and the moss; Day 177 Xyan at Gate 05; Day 355 the bells |
| **Xyan** | Day 17 the 1,778th sending, received by Ishall; Day 55 "The Vaults are leaking.", received by Ishall; Day 69 his first direct line in a facility scene; Day 97 his four-line direct telemetry report, "The Silence is breaking."; Day 127 the fourth message and moss image, received by Ishall; Day 177 and Day 355 the return |

### XIII.5 Forms already present in Absolvohan

The Narrative Interludes already authorise non-Majin knowledge forms:

- first-person oral records identified by role;
- an unsigned letter written on Day 12;
- corridor transcripts;
- a formal objection reproduced in full;
- vault and reading-week debriefs;
- composite witness accounts;
- archivists' notes on a page nobody reads aloud;
- objects and practices such as the mess pot, tally board, reading cart, and index cards.

Backstory Extended may inherit these forms. The difference is that the record now belongs to a named Echo-Core, and the featured character remains the primary perceiver rather than dissolving into anonymous facility elegy.

The Overview's fifteen Ending Dialogue Branches may suggest cast configuration — who can confront or support whom without Majin present. Their deaths, rewinds, and dramatised details are not canon and must not become backstory facts.

### XIII.6 Source cautions

- The dossier **Role in Absolvohan** sections sometimes expand or alter the short Part 1–9 dialogues. Parts 1–9 control the exact present-day anchor line and speaker; the dossier history controls the past spine. A conflict goes to HOLD.
- Day 97 in Part 5 is Xyan speaking directly. The Outsider dossier treats that message inside Ishall's chain. Keep the two layers distinct; do not overwrite either.
- The Overview contains stale or conflicting dramatisation details. It is a structural reference, not the factual scene authority.
- Absolvohan quotes only fragments of the Founder's journal, the Final Door's language, and the Furnace record. Do not invent full texts without a HOLD or Promotion Check.
- Day 160 does not give dialogue to Marjuk, Ishall, or Xyan. Their changed-state scenes must come from their own anchors.

---

## XIV. Activation protocol

1. Owner names the Echo-Core.
2. Read that character's whole canonical dossier.
3. Read every directly linked record named in that dossier.
4. Read the relevant Absolvohan days and any linked entity, floor, or incident record.
5. Build the Prologue spine and the primary Connection String.
6. Choose the anchor chain and the trigger modules.
7. Choose category, POV, and style per module.
8. Draft the file directly at its planned repo path.
9. Write the appendix before declaring the draft complete.
10. Validate links, tables, labels, and lore audit.
11. Gate and push the unit.
12. Update the planned-record status only for that character.

One Echo-Core at a time. No file begins before the previous one is gated, unless the owner explicitly opens a batch.

### XIV.1 Pre-draft checklist

- [ ] Whole dossier read
- [ ] Linked records read
- [ ] Absolvohan anchors read in the Part, not only in the dossier summary
- [ ] Prologue spine checked against dossier facts
- [ ] At least one further PAST scene beyond the Prologue
- [ ] The wound is named in one sentence before drafting
- [ ] Every module assigned to pre-break, break, or post-break
- [ ] At least one past scene appears in both pre-break and post-break
- [ ] The character speaks the wound obliquely at least once, in the present, to a witness
- [ ] The file ends on a stance, not a resolution
- [ ] One working object appears before and after the break, unchanged
- [ ] The second pass restores a sentence a named person chose not to say
- [ ] A named counter-witness states the failure plainly, unaided
- [ ] One permanent symptom is visible in routine, not only in crisis
- [ ] The professional voice after the stance has shifted by one degree
- [ ] Every module answers where, when, who perceives, what changes, and what is said
- [ ] No module is a list, montage, or collection of incidents
- [ ] At least one C tether and one R tether in the Prologue
- [ ] Every module passes the C or R test sentence
- [ ] Every module reaches a present or institutional consequence
- [ ] Loop access checked against the matrix
- [ ] POV bearer named for every scene
- [ ] SPV addressee and speaker named
- [ ] Style recorded per module
- [ ] Documents quoted only as far as the record reaches
- [ ] Conflicts marked HOLD
- [ ] New facts moved to Promotion Check
- [ ] No Act, Chapter, or Part labels
- [ ] No R-31 scaffolding in the story body

### XIV.2 Validation checklist

- [ ] `python3 tools/check_links.py` — 0 broken
- [ ] `python3 tools/audit_lore_archive.py` — PASS
- [ ] `python3 tools/timeline_lint.py` — PASS
- [ ] `python3 tools/seam_lint.py` — PASS
- [ ] `python3 tools/label_lint.py` — PASS
- [ ] Every table row closes with a pipe
- [ ] Canonical dossiers unchanged
- [ ] README status matches what was written
- [ ] Gate pushed and `dirty: 0`

---

## XV. Folder and naming rules

| File | Purpose |
|---|---|
| `00_BACKSTORY_EXTENDED_STRUCTURE_AND_FORM.md` | This standard |
| `01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md` | Majin |
| `02_SEIYON_THE_SECRETARY_BACKSTORY_EXTENDED.md` | Seiyon |
| `03_DEKAN_THE_CONTAINMENT_LEAD_BACKSTORY_EXTENDED.md` | Dekan |
| `04_ZYRAK_THE_EXTRACTION_LEAD_BACKSTORY_EXTENDED.md` | Zyrak |
| `05_AYSHUK_THE_RESEARCH_LEAD_BACKSTORY_EXTENDED.md` | Ayshuk |
| `06_MELLDA_THE_BORDER_LEAD_BACKSTORY_EXTENDED.md` | Mellda |
| `07_MARJUK_THE_ARCHIVE_LEAD_BACKSTORY_EXTENDED.md` | Marjuk |
| `08_ISHALL_THE_OUTSIDER_BACKSTORY_EXTENDED.md` | Ishall |
| `09_XYAN_THE_EXILE_BACKSTORY_EXTENDED.md` | Xyan |

Rules:

- Do not rename a canonical dossier.
- Do not create a character file before activation.
- Do not use a character file as a dossier replacement.
- Keep the character's Korean name and English title in the H1, matching the dossier.
- One file per Echo-Core.

---

## XVI. Change control

This standard can be amended by owner instruction at any time. An amendment that changes the rule stack, the category set, the POV set, the style set, the Connection String Rule, or the Prologue requirement is recorded in the README and in `CHANGELOG.md` in the same unit.

An amendment that changes a canonical fact belongs in the dossier and its linked surfaces, not in this standard.

No story file may cite this standard as authority for contradicting a dossier. The dossier wins on facts. This standard wins on arrangement.

---

## XVII. Current state

- Structure and form: **filed** (`11cd68a`), amended with the Malkuth spine (`ce95ff4`).
- Source survey: **filed outside the world bible** — [`00A_L_CORP_BACKSTORY_RECORD_RESEARCH.md`](../../../PROJECT_MOON_RESEARCH/CROSS_VERSE/00A_L_CORP_BACKSTORY_RECORD_RESEARCH.md) in `PROJECT_MOON_RESEARCH/CROSS_VERSE/`: thirteen L Corp records read in full for the spine, the doubling, the witness, and the stance.
- Character files: **01 Majin** and **02 Seiyon** filed; Majin rebuilt twice, last on the pre-break/break/post-break spine.
- Activated Echo-Core: **Majin**, closed. Next activation waits on the owner.
- Next step: characters 03–09 in order, one at a time, each read against the dossier before drafting and each validated before the next begins.
- Outstanding owner decision: the Solidification dating conflict held in file 01.
- The nine canonical dossiers remain unchanged and authoritative.
