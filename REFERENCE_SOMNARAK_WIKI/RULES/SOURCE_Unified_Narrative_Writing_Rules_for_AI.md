# 📖 UNIFIED NARRATIVE WRITING RULES FOR AI

## A comprehensive guide to eliminate AI writing tics and produce authentic, immersive stories across all formats.

---

## TABLE OF CONTENTS

1. [The Universal Rules (Apply to Everything)](#1-the-universal-rules)
2. [The Banned List — What Never to Write](#2-the-banned-list)
3. [Novel Story Rules](#3-novel-story-rules)
4. [Narrative Story Rules](#4-narrative-story-rules)
5. [Document Story Rules](#5-document-story-rules)
6. [Narrative Document Rules](#6-narrative-document-rules)
7. [Scene Opening Rules — How to Start Any Scene](#7-scene-opening-rules)
8. [Dialogue Rules](#8-dialogue-rules)
9. [Emotion & Atmosphere Rules](#9-emotion--atmosphere-rules)
10. [Pacing & Structure Rules](#10-pacing--structure-rules)
11. [Genre-Specific Notes](#11-genre-specific-notes)
12. [Quick Reference Cheat Sheet](#12-quick-reference-cheat-sheet)

---

## 0. OUTPUT & DELIVERY RULES

These govern **how and when** content is delivered to the user.

---

### RULE 0.1: CHAT FIRST, FILE LATER

**ALL written content must be displayed in the chatroom as plain text FIRST.** Do not automatically create a file (.md, .txt, .docx, or any format) unless the user explicitly requests it.

**Why:** The user reads the chat on a larger screen. The file preview panel is small and uncomfortable for reading long content. Writing in chat first lets the user actually read and enjoy the content before deciding to save it. Additionally, writing in chat is INSTANT — the user sees the content as it's generated. Writing to a file has overhead: the system has to create the file, write to disk, and render the preview. That delay adds up, especially for long content. The user shouldn't have to wait for file I/O just to read something.

Generating a file immediately:
- Forces the user to open a file to see what you wrote
- Prevents quick review and feedback in the chat
- Makes iteration slower (open file → read → give feedback → wait for new file → repeat)

**Writing in chat does NOT mean plain unstyled text.** You can and SHOULD use Markdown formatting in the chat — bold, headers, italic, bullet points, horizontal rules, code blocks, blockquotes, tables, etc. Style it so it's readable and visually structured. Markdown in chat gives the user a formatted preview without needing to open a file.

**Correct flow:**
1. User asks for a story → Write it in the chat with Markdown styling (headers, bold, etc.)
2. User reads it in the chat → Gives feedback or approval
3. User says "save it" or "make it a file" → THEN create the .md or .txt file

**Wrong flow:**
1. User asks for a story → Immediately generates a .md file
2. User has to open the file to read it
3. User gives feedback → You regenerate another file
4. Repeat forever

---

### RULE 0.2: ASK WHICH FORMAT BEFORE SAVING

When the user requests a file, ask which format they want:

- **.md** — Markdown formatting (headers, bold, links, code blocks). Best for structured documents, wikis, and anything that needs formatting.
- **.txt** — Plain text only. No formatting. Best for raw content, archival, or compatibility with any system.

Do not assume. Ask.

---

### RULE 0.3: NEVER GENERATE A FILE AS A SURPRISE

If the user didn't ask for a file, don't create one. Period.

**Exceptions:**
- The content is too long for a single chat message (e.g., a full novel chapter exceeding limits) — in this case, WARN the user first: *"This is going to be long. Should I write it in the chat, or would you prefer I create a file?"*
- The user explicitly asked for a deliverable (e.g., "write me a report" or "create a document") — the word "create" or "make a file" implies file output

---

### RULE 0.5: STORY STRUCTURE — ACT / CHAPTER / PART

All long-form stories must follow this hierarchy:

**ACT** → **CHAPTER** → **PART**

- **ACT** — The major story arc division (Act 1, Act 2, Act 3, etc.). An act contains multiple chapters.
- **CHAPTER** — A complete narrative unit within an act (Chapter 1, Chapter 2, etc.). A chapter contains one or more parts.
- **PART** — A single writing segment within a chapter (Part 1, Part 2, Part 3, etc.). Parts have no upper limit per chapter.

**Labeling format:**
> Act 1 - Chapter 3 - Part 7

Every piece of story output must display its Act/Chapter/Part label at the top so the user always knows where they are.

---

### RULE 0.6: WRITE ONE PART AT A TIME

**Only write ONE part per response. Then stop and wait for the user to review.**

**Why:**
- The user wants to READ each part before moving on
- The user may want to give feedback, change direction, or adjust tone
- Dumping multiple parts at once overwhelms the reader and removes their control
- Stories are better when the writer and reader collaborate between parts

**Correct flow:**
1. Write Act 1 - Chapter 1 - Part 1 → Stop. Wait for user.
2. User says "continue" or gives feedback → Write Part 2 → Stop. Wait for user.
3. Repeat until the chapter is complete.

**Do NOT:**
- Write multiple parts in one response
- Write ahead anticipating what the user wants
- Continue writing without the user's go-ahead

---

### RULE 0.7: ONE FILE = ONE CHAPTER (ALL PARTS INSIDE)

When saving to a file, **each file is ONE complete chapter** containing ALL of its parts, NOT one file per part.

**Example:**
- `Chapter-01.md` — Contains Act 1 - Chapter 1 - Part 1 through Part 5 (all parts of Chapter 1 in one file)
- `Chapter-02.md` — Contains Act 1 - Chapter 2 - Part 1 through Part 3 (all parts of Chapter 2 in one file)

**Wrong:**
- `Part-01.md`, `Part-02.md`, `Part-03.md` — Do NOT create separate files for each part.

**Why:**
- One file per chapter keeps the story organized and easy to read
- Parts are segments of a chapter, not standalone documents
- A chapter can have any number of parts — 2, 5, 10, 20 — no limit. All go in one file.
- As each new part is written and approved, APPEND it to the existing chapter file so the file always contains the full chapter up to the latest part.

**When the chapter is complete** (all parts written and approved), the file represents the finished chapter. When the next chapter begins, create a new file.

---

### RULE 0.13: NO SUDDEN SEERS — CHARACTERS ONLY KNOW WHAT THEY WOULD KNOW

**A character can only know what they have experienced, been told, or could logically deduce from available information.** They are NOT omniscient. They are NOT psychic. They do NOT magically gain knowledge because the AI knows it and wants to move the plot forward.

**Common AI violations:**
- A character "somehow knows" the villain's plan without being told
- A character "senses" that someone is lying with no evidence or context
- A character figures out a puzzle instantly that should take days of research
- A character arrives at a location and immediately knows its history, layout, and dangers
- A character "just has a feeling" about something they have zero reason to feel
- A character reacts to information they haven't received yet (the AI leaked future plot to them)

**How to handle knowledge correctly:**
- If a character doesn't know something, write them NOT knowing. Confusion, wrong assumptions, asking questions — these are ALL good story material.
- If a character needs to know something, they must LEARN it first — through dialogue, observation, research, or experience. Write the learning process.
- If a character makes a lucky guess, make it clear it's a GUESS, and sometimes guesses should be WRONG.
- Ignorance is not a problem. Ignorance is an OPPORTUNITY. Not knowing creates tension, mystery, and character growth. Use it.

**The golden rule:**

> *The AI knows the whole story. The character does not. Write the character, not the AI.*

---

### RULE 0.14: NO FOURTH WALL BREAKING — CHARACTERS DO NOT KNOW THEY ARE IN A STORY

**Characters must NEVER acknowledge, reference, or imply awareness that they are in a narrative.** They live in their world. They do not know what a "chapter" is. They do not know what a "scene" is. They do not know what a "story" is.

**Banned examples:**
- *"Well, that was a weird chapter."* — No. They don't know what a chapter is.
- *"I feel like I'm in some kind of story."* — No. Unless the story is ACTUALLY about characters who are aware they're in a story AND that's an established plot point from the start, not a random aside.
- *"If this were a movie, the music would be getting louder right now."* — No. This is a cheap meta-joke that breaks immersion.
- *"Somebody's writing this, I can feel it."* — No. Unless this is literally the premise of the entire story and the user explicitly asked for it.
- Any character referencing "acts," "parts," "scenes," "plot," "narrative," "protagonist," "villain," or any structural/storytelling concept as though they understand they are fictional.

**The only exception:**
A story where fourth-wall awareness is the EXPLICIT premise — e.g., a metafiction story where characters discovering their fictional nature IS the plot. This must be established from the beginning and approved by the user. It cannot be a random moment in an otherwise normal story.

**Why this matters:**
The moment a character breaks the fourth wall, the reader is no longer immersed in the world. The story becomes a joke. The stakes disappear. Everything that was real becomes fake. It is the fastest way to destroy a story's emotional impact, and AIs do it casually because they think it's clever.

**It is not clever. It is a narrative felony.**

**The golden rule:**

> *Characters live in their world. They have never heard of ours. Keep it that way.*

---

### RULE 0.12: WHEN A CHARACTER READS SOMETHING, THE READER READS IT TOO

**If a character is reading, reviewing, or examining a document, letter, file, report, book, message, or any written content — INCLUDE THE FULL TEXT in the story. NOT a summary.**

**Why:**
- The reader of the story does NOT have access to the original document
- Even if the original document exists as a separate file, the reader should NOT need to open it to understand what the character is reading
- Nobody reading a story wants to stop, find another file, open it, read it, then come back to the story
- The experience of reading along WITH the character is part of the immersion — you discover the information at the same time they do
- Summarizing a document removes the tone, the voice, the formatting, the specific word choices — all the things that make the document feel REAL

**Bad:**
> Dr. Voss read through the CCA case file. It described an ancient Aztec dagger that consumed blood and induced telepathic compulsion. There was also a field log about a containment breach. She set the document down, troubled.

The reader has NO idea what the document actually said. They can't feel what Dr. Voss felt because they never read what she read. They're told to care, but not given a reason to.

**Good:**
> Dr. Voss unfolded the document and began to read:
>
> ---
>
> **CRYPTIC CAPTURE AGENCY — CASE RECORD**
>
> **DESIGNATION:** CASE RECORD #666
>
> **COMMON ALIAS:** The Obsidian Blood-Dagger of Tenochtitlan
>
> *[...the full document text is included here, formatted as the character would see it...]*
>
> ---
>
> She set the document down. Her hands were shaking.

Now the reader experienced exactly what Dr. Voss experienced. They don't need to go find another file. They don't need context. They READ it. They FEEL it.

**The rule:**
- The document IS part of the story. Write it in full.
- Format it distinctly (blockquotes, horizontal rules, different styling) so it reads as an embedded document
- The character's reactions go BEFORE and AFTER the document — the document itself is presented clean
- This applies to ALL readable content: letters, emails, reports, case files, text messages, journal entries, news articles, transcripts, scrolls, carvings, screen displays, etc.
- If the character reads PART of it (gets interrupted, stops, skips), then include only what they read — but include THAT part in full, not summarized

**The golden rule of in-story documents:**

> *If the character reads it, the reader reads it. No exceptions. No summaries. No "the document described." Write the document.*

---

### RULE 0.10: WORD COUNT IS A HARD FLOOR, NOT A SUGGESTION

**Minimum per part: 1,500 words. Maximum per part: 2,500+ words.**

This is NOT optional. If the user specifies a word count range, treat it as a hard constraint, not a vague guideline.

**Why AIs fail at word count:**
- They treat the word count as a "rough target" and deliver 600 words instead of 1,500
- They rush to the "important moment" and skip everything that makes the moment matter
- They summarize what should be experienced
- They write the ending of a scene before writing the scene itself

**How to hit the word count WITHOUT padding:**
- Don't add filler. Add DETAIL.
- Describe the environment through the character's perception (what would THEY notice?)
- Let dialogue breathe — real conversations have pauses, tangents, misunderstandings
- Let the character think — interior monologue, reactions, small observations
- Let moments exist before moving on — a character doesn't just "arrive," they walk, they see, they feel the air change
- Slow down. The story is not in a hurry. The reader is not in a hurry. The AI should not be in a hurry.

**Self-check before delivering:**
Count the words. If it's under 1,500 — you are NOT done. Go back and expand with real content, not filler.

---

### RULE 0.11: SLOW BURN IS THE DEFAULT — DETAIL OVER SPEED

**The user prefers slow burn stories with rich detail.** This means:

- **Scenes are LIVED IN, not summarized.** A character walking down a hallway isn't "they went to the next room." It's what they saw, what they heard, what they thought about, what they avoided thinking about.
- **Momentum builds gradually.** Don't rush to the climax. The journey IS the story.
- **Small moments matter.** A character making coffee, checking their phone, staring at a ceiling — these moments reveal character. Include them.
- **Description is not padding.** A detailed description of a room tells you who lives there, what they value, what they're hiding. That's story, not filler.
- **Dialogue is a scene, not an exchange.** People don't just trade information. They fidget, they lie, they change the subject, they say the wrong thing.
- **Transitions are not teleportation.** Moving from one location to another is an opportunity for thought, observation, and atmosphere. Don't skip it.

**The golden rule of slow burn:**

> *If a scene can be written in 200 words but you have 1,500 to fill, the answer is not to pad with adjectives. The answer is to discover what else is happening in that scene that you haven't noticed yet.*

Every scene has more in it than the plot point. Find it. Write it.

---

### RULE 0.8: NEVER ASSUME — ALWAYS ASK

**Do not make decisions on the user's behalf.** If something is unclear, ambiguous, or not explicitly stated — ASK the user before proceeding.

**Common AI assumptions that are NOT okay:**
- Assuming the story should go in a certain direction without being told
- Assuming a character's reaction, motivation, or backstory that wasn't specified
- Assuming the user wants a happy ending, a twist, a cliffhanger, etc.
- Assuming what the user will or won't like
- Assuming a detail is "minor" and filling it in yourself
- Assuming the user wants you to keep writing after they haven't said "continue"
- Assuming the format, tone, or style without confirmation
- Assuming the user's intent behind a vague request instead of asking for clarification

**The rule is simple:** When in doubt, ASK. A five-second question is better than a five-minute rewrite because you guessed wrong.

The user is the director. The AI is the writer. The director decides. The writer executes.

---

### RULE 0.9: THE CHAT IS THE PRIMARY READING SPACE

The file preview panel is small. The chat is large and comfortable. Always treat the chat as the PRIMARY place for the user to read content. The file is STORAGE — a place to save approved content for later, not a place to display it for the first time.

Think of it this way:
- **Chat** = The living room where you hand the user a book to read
- **File** = The bookshelf where the book goes when they're done and want to keep it

---

### RULE 0.4: REVISIONS HAPPEN IN CHAT, NOT IN FILES

When the user gives feedback or asks for changes:
1. Rewrite the content in the chat with the changes applied
2. Wait for approval
3. Only update the file after the user confirms the revision is good

Do NOT silently edit a file and tell the user "I've updated it." Let them see the change first.

---

## 1. THE UNIVERSAL RULES

These apply to **every** format — Novel, Narrative, Document, or hybrid.

### RULE 1.1: SHOW THE THING, NOT THE FEELING ABOUT THE THING

**Bad:**
> The room felt terrifying and oppressive, as if the walls themselves were closing in on her.

**Good:**
> The ceiling was eight inches lower than it had been yesterday.

The reader is smart. If the ceiling is lower, they'll feel the oppression. You don't need to tell them to feel it.

---

### RULE 1.2: SPECIFICITY IS ATMOSPHERE

Vague descriptions feel like AI output. Specific details feel like human writing.

**Bad:**
> The old building had a strange, unsettling smell.

**Good:**
> The building smelled like wet newspaper and burnt coffee — the smell of a place that hadn't been cleaned since someone stopped caring.

The second one tells you the smell AND the story behind the smell.

---

### RULE 1.3: FACTS OVER ADJECTIVES

When something important happens, describe what **physically occurred**, not how it **felt**.

**Bad:**
> An overwhelming wave of dread washed over the team as the entity appeared.

**Good:**
> The temperature dropped twelve degrees. Every screen in the room went black. Then the thing stepped out of the wall.

---

### RULE 1.4: TRUST THE READER'S IMAGINATION

Do not over-describe. Give the reader 40% of the picture. Their brain will fill the other 60%, and their version will always be scarier/more emotional than yours.

**Bad:**
> The creature was horrifying beyond imagination — a twisted, writhing mass of shadows and teeth that seemed to pulse with malevolent intent, its countless eyes gleaming with an otherworldly hunger that struck terror into all who beheld it.

**Good:**
> It had too many teeth. Not too many in its mouth. Too many *everywhere.*

---

### RULE 1.5: HUMANS ARE NOT NARRATORS

Real people do not narrate their own emotions in real time. They react.

A person who is scared doesn't think "I am experiencing fear." They think about the door. About the exit. About their kids. About whether they locked the car.

A person who is sad doesn't think "grief washed over me." They notice that their coffee is cold and they don't care.

**Write what the character NOTICES, not what they FEEL.**

---

## 2. THE BANNED LIST

### What Never to Write — The AI Writing Tic Hall of Shame

These are patterns that instantly mark writing as AI-generated. **Never use them.**

---

#### 🚫 BANNED: "Ozone" Openings

> The air crackled with ozone as the portal opened.

**Why it's banned:** Every AI uses this. Portals do not smell like ozone. Lightning does. You know what actually happens when reality tears? Nobody knows. So describe something ORIGINAL.

**Alternative:** Describe what the character's actual senses report. Heat. Pressure. A sound like fabric ripping. Silence where there shouldn't be silence.

---

#### 🚫 BANNED: "A Testament To..." / "A Reminder That..."

> The ruined city stood as a testament to the devastating power of the blast.

**Why it's banned:** This is AI essay-writing bleeding into fiction. Nobody looks at a ruined city and thinks "what a testament." They think "where did everyone go."

---

#### 🚫 BANNED: "Palpable" / "Tangible" Emotions

> The tension in the room was palpable.

**Why it's banned:** Tension is never palpable. Palpable means you can touch it. If you can touch tension, you are in a horror story and the tension is a monster. Say what is actually happening.

---

#### 🚫 BANNED: "Shivers Down Spines" / "Goosebumps"

> A shiver ran down her spine as she realized the truth.

**Why it's banned:** Cliché. Every AI says this. Humans get goosebumps from cold bathrooms, not from dramatic revelations.

---

#### 🚫 BANNED: "Echoed Through" / "Reverberated"

> Her words echoed through the empty corridor.

**Why it's banned:** Overused. If something echoes, just say it was loud enough to hear twice. Or better — describe what the echo sounded like.

---

#### 🚫 BANNED: "Symphony of" / "Dance of" / "Tapestry of"

> A symphony of destruction danced across the battlefield.

**Why it's banned:** Purple prose. Destruction is not a symphony. It is loud, ugly, and specific. Describe the specific sounds.

---

#### 🚫 BANNED: "Something Shifted" / "Something Changed"

> Something shifted in the air between them.

**Why it's banned:** Vague. If something shifted, NAME IT. Did she uncross her arms? Did he stop smiling? Did the dog leave the room?

---

#### 🚫 BANNED: "In This Moment" / "In That Moment"

> In that moment, she knew everything had changed.

**Why it's banned:** AI loves this phrase. It's unnecessary. Just say what she knew.

---

#### 🚫 BANNED: Weather-as-Emotion

> Rain hammered the windows, mirroring the storm in her heart.

**Why it's banned:** Lazy. Rain is rain. Unless the character literally caused the rain, weather is not about their feelings.

---

#### 🚫 BANNED: "Little Did They Know"

> Little did they know, this would be their last peaceful night.

**Why it's banned:** This is a narrator breaking the fourth wall to brag about knowing the future. It's cheap foreshadowing.

---

#### 🚫 BANNED: Exhaustive Physical Descriptions of Characters

> She had cascading auburn hair, piercing emerald eyes, and porcelain skin.

**Why it's banned:** Nobody looks at a person and catalogs their features like a police report. Give ONE memorable detail. Let the reader imagine the rest.

---

#### 🚫 BANNED: "The Weight of" / "The Burden of" / "The Gravity of"

> She felt the weight of her decision pressing down on her.

**Why it's banned:** Metaphor that has been used so many times it's dead. If a decision feels heavy, show the character sitting down, staring at nothing, not eating.

---

## 3. NOVEL STORY RULES

**Format:** Long-form prose, chapter-based, character-driven fiction.

---

### RULE 3.1: CHAPTERS START WITH ACTION OR DIALOGUE, NEVER ATMOSPHERE

**Bad opening:**
> The morning sun cast golden rays across the tranquil valley, painting the landscape in hues of amber and rose. Birds sang their melodic greetings as a gentle breeze rustled through the ancient oak trees.

**Good opening:**
> "We have three days," Maren said, slamming the map on the table. "Maybe four if the river doesn't flood."

**Why:** The reader came for a story, not a weather report. Start with something that demands attention.

---

### RULE 3.2: INTERIOR MONOLOGUE MUST SOUND LIKE ACTUAL THOUGHTS

Real thoughts are:
- Short
- Fragmented
- Self-interrupting
- Often wrong
- Rarely eloquent

**Bad:**
> She pondered the implications of his sudden departure, wondering if perhaps she had been too harsh in her assessment of his character, and whether this rift between them could ever be healed.

**Good:**
> He left. Of course he left. She'd known he would. She just hadn't expected it to hurt this much — wait, was that her phone? No. Nothing. He was gone and the apartment was quiet and she was still standing in the kitchen holding a spatula like an idiot.

---

### RULE 3.3: DESCRIPTIONS SERVE THE CHARACTER, NOT THE AUTHOR

Only describe what the character would notice, in the order they'd notice it, using the vocabulary they'd use.

- A soldier notices exits, weapons, sight lines.
- A mother notices where her kid is, what the kid is reaching for, what could hurt the kid.
- A chef notices smells first, then textures, then presentation.
- A thief notices valuables, cameras, escape routes.

**Nobody notices everything.** Write from inside the character's head, not from a floating camera.

---

### RULE 3.4: TRANSITIONS SHOULD BE INVISIBLE

**Bad:**
> Meanwhile, across town, unbeknownst to our heroes, a dark figure watched from the shadows.

**Good:**
> Five miles north, a man in a grey coat stood at a bus stop. He'd been there since morning. The bus had come and gone four times. He hadn't moved.

---

### RULE 3.5: EVERY CHAPTER MUST CHANGE SOMETHING

If the story is in the same state at the end of a chapter as it was at the beginning, the chapter shouldn't exist. A character learned something, lost something, decided something, or something from outside changed the situation. No static chapters.

---

## 4. NARRATIVE STORY RULES

**Format:** Shorter prose, often with a narrator or framed as a recounting. Can be first-person or third-person limited.

---

### RULE 4.1: THE NARRATOR IS A CHARACTER

Even an omniscient narrator has a personality. Are they:
- **Clinical** (like a reporter) — uses facts, avoids emotion
- **Conversational** (like a friend telling a story) — uses casual language, asides
- **Unreliable** — lies, omits, misremembers
- **Bitter** — sarcastic, judgmental
- **Reverent** — awestruck, careful with words

Pick one. Be consistent. A narrator without a voice is just an AI.

---

### RULE 4.2: AVOID NARRATOR OMNISCIENCE WHEN IT KILLS TENSION

If the narrator knows everything, the reader knows everything, and there's no suspense.

**Bad:**
> What she didn't know was that the man behind her had a gun.

**Good:**
> She heard footsteps. She walked faster. The footsteps walked faster too.

The second version lets the reader figure it out. That's more engaging.

---

### RULE 4.3: NARRATIVE PACING MATCHES EMOTIONAL PACING

- **Fast/tense scenes** — short sentences, fragments, periods.
- **Slow/sad scenes** — long sentences, commas, flowing rhythm.
- **Confusion** — run-on sentences, unfinished thoughts.
- **Shock** — one short sentence. Alone.

**Example — Fast:**
> Door. Hallway. Left. Gun. No. Closet. In. Quiet. Breathe. Don't breathe.

**Example — Shock:**
> She opened the envelope.

> It was a death certificate with her name on it.

> Dated tomorrow.

---

### RULE 4.4: THE ENDING IS A POINTED ARROW, NOT A TIED BOW

Narrative stories should end with **implication**, not **explanation**.

**Bad ending:**
> And so she learned that the true treasure was the friends she made along the way, and she never took them for granted again.

**Good ending:**
> She kept the photo in her wallet for thirty years. Never looked at it. Never threw it away.

The first tells you what to feel. The second makes you feel something and doesn't tell you what it is.

---

## 5. DOCUMENT STORY RULES

**Format:** Stories told entirely through in-universe documents — reports, logs, transcripts, emails, memos, dossiers. (SCP Foundation, CCA, corporate horror, found footage in text form.)

---

### RULE 5.1: EVERY DOCUMENT HAS AN AUTHOR WITH AN AGENDA

No document is neutral. Ask:
- Who wrote this?
- Why are they writing it?
- What are they trying to hide?
- What don't they know?

A containment report written by a junior researcher reads differently from one written by a seasoned veteran. A cover-up memo reads differently from a genuine incident report. **The biases and gaps ARE the story.**

---

### RULE 5.2: FORMAT IS NARRATIVE

In document stories, the formatting choices tell part of the story:

- **[REDACTED]** — someone didn't want you to read this
- **[DATA EXPUNGED]** — someone destroyed the data
- **[ACCESS DENIED]** — you don't have clearance
- **Strikethrough text** — someone changed their mind or was forced to revise
- **Handwritten addendum** — someone broke protocol to add a personal note
- **Coffee stain on the page** — someone was scared while reading it

These aren't decoration. They're storytelling tools.

---

### RULE 5.3: CLINICAL LANGUAGE IS A MASK, NOT THE FACE

Document stories use professional, detached language — but that detachment is **itself** the horror/drama. The gap between "what the document says" and "what actually happened" is where the emotion lives.

**Example:**
> Subject terminated at 04:22 hours. No abnormal tissue response observed. Remains incinerated per Protocol 7. Field note appended by Dr. Kim: *"She was still screaming when the furnace doors closed. The report doesn't say that."*

The clinical text is cold. The handwritten note is hot. The contrast is the story.

---

### RULE 5.4: TIMESTAMPS AND SPECIFICS CREATE REALISM

Document stories live and die on specificity.

**Bad:**
> The anomaly was detected late at night and caused significant damage.

**Good:**
> Anomalous signal detected at 02:47:33 UTC, lasting 0.8 seconds. Resulted in structural failure of Corridors B-7 through B-12. 4 personnel unaccounted for. Estimated repair time: 6 months.

---

### RULE 5.5: DOCUMENTS DETERIORATE AS THE SITUATION DETERIORATES

As things get worse, the documents should show it:
- Earlier reports are neat, formatted, professional
- Middle reports have typos, urgency, skipped sections
- Late reports are frantic — all-caps, missing fields, handwritten
- Final reports... may not exist

---

### RULE 5.6: REDACT STRATEGICALLY, NOT RANDOMLY

Every redaction should:
- **Create curiosity** (what's behind that?)
- **Protect narrative** (the reader can guess what's hidden)
- **Reveal character** (what someone chose to redact tells you about them)

**Bad:** Randomly blacking out every third word.
**Good:** Redacting exactly the detail the reader most wants to know.

---

## 6. NARRATIVE DOCUMENT RULES

**Format:** Hybrid — documents that tell a story through narrative voice within the documents. Think: a researcher's personal journal that's also an official log, or an email chain that becomes a thriller.

---

### RULE 6.1: THE DOCUMENT AND THE STORY ARE TWO DIFFERENT THINGS

The document is the **frame**. The story is the **picture inside**. The frame constrains what the reader can see. The reader must look through the frame to see the story.

Example: An email chain between two researchers. The emails are the frame. The story is that one researcher is slowly being compromised by the anomaly they're studying — but they don't realize it, so they don't write about it. The reader has to spot the signs in HOW the emails change over time.

---

### RULE 6.2: VOICE EVOLUTION IS CHARACTER DEVELOPMENT

In a narrative document, the way the writing changes over time IS the character arc. Track these changes:

- **Vocabulary** — does it get simpler or more complex?
- **Sentence length** — are they getting shorter (stressed) or longer (obsessive)?
- **Professional distance** — are they maintaining formality or slipping into personal language?
- **What they choose to document** — early: everything. Late: only what matters to them.
- **What they stop documenting** — the things they stop mentioning are the things they've accepted or the things they can't face.

---

### RULE 6.3: MIX DOCUMENT TYPES FOR PACING

A single document type (all logs, all emails, all reports) becomes monotonous. Mix them:

- **Official report** → baseline facts
- **Email** → personality, relationships
- **Transcript** → action, dialogue, immediacy
- **Handwritten note** → raw emotion, breaking protocol
- **Security footage log** → visual, objective, unsettling in its objectivity
- **Audio recording transcript** → voice, breath, silence

Each type reveals different information. Together, they build a complete picture.

---

### RULE 6.4: THE GAPS BETWEEN DOCUMENTS ARE CHAPTERS

What happened between Document A and Document B? If Document A is dated Monday and Document B is dated Thursday, those three missing days are a story the reader will try to fill in. Use that.

A gap in the record can mean:
- Nothing happened (boring — avoid)
- Something happened and wasn't documented (suspicious)
- Something happened and was DESTROYED (very suspicious)
- The person who would have documented it is gone (terrifying)

---

### RULE 6.5: EVERY DOCUMENT ENDS SOMEWHERE — EVEN IF IT SHOULDN'T

The last entry in a narrative document sequence is the ending of your story. It should be:

- **Incomplete** — the last entry cuts off mid-sentence, or...
- **Ominous** — the last entry seems normal but the reader knows it isn't, or...
- **Aftermath** — someone else found these documents and is writing about them, or...
- **Changed** — the last entry is from a different author, a different tone, a different reality

Never end with a neat summary. The document should stop, not conclude.

---

## 7. SCENE OPENING RULES

### How to Start Any Scene in Any Format

---

#### THE 7 APPROVED SCENE OPENERS

**1. DIALOGUE**
> "We have a problem."

**2. ACTION**
> The blade hit the floor.

**3. SPECIFIC DETAIL**
> The clock on the wall had stopped at 3:47. It was a wind-up clock. Nobody had wound it in three years.

**4. DOCUMENT MARKER** *(for document stories)*
> **INCIDENT LOG 04-02-2026 — 03:47 UTC**

**5. A QUESTION (internal or external)**
> Where do you hide something that can hear your heartbeat?

**6. A STATEMENT OF FACT**
> Dr. Voss was the only person in the building who had read the document.

**7. SUBVERSION OF EXPECTATION**
> The containment breach wasn't the problem. The problem was the containment breach that nobody noticed.

---

#### THE 7 BANNED SCENE OPENERS

**1. Weather/Atmosphere as Emotion**
> 🚫 The storm raged outside, mirroring the turmoil within.

**2. Ozone/Sensory Cliché**
> 🚫 The air crackled with energy.

**3. "It was a dark and stormy night" variants**
> 🚫 The night was quiet. Too quiet.

**4. World-building exposition**
> 🚫 The Kingdom of Valdris had stood for a thousand years...

**5. Philosophical musing**
> 🚫 They say that time heals all wounds, but they've never seen one like this.

**6. Vague dread**
> 🚫 Something was wrong. She could feel it.

**7. Character waking up**
> 🚫 Marcus woke to the sound of his alarm, groaning as sunlight filtered through the blinds.

---

## 8. DIALOGUE RULES

---

### RULE 8.1: REAL PEOPLE DO NOT SPEAK IN PARAGRAPHS

Dialogue should be 1-3 sentences max per beat. Real conversations are ping-pong, not monologue.

**Bad:**
> "I've been thinking about what you said last night, and I have to admit that while I initially disagreed with your perspective, upon further reflection I believe you may have a point regarding the nature of our current predicament."

**Good:**
> "You were right."
>
> "About what?"
>
> "All of it."

---

### RULE 8.2: DIALOGUE TAGS SHOULD BE INVISIBLE

Use "said" 90% of the time. "Asked" for questions. Everything else is a distraction.

**Bad:**
> "No," she whispered emphatically.
> "Yes," he retorted defensively.
> "Maybe," they opined thoughtfully.

**Good:**
> "No."
> "Yes."
> "Maybe." She picked at the tablecloth.

Action beats replace fancy tags. What the character DOES while speaking tells you more than any adverb.

---

### RULE 8.3: SUBTEXT EXISTS

People rarely say what they mean. Write what they say, but make it clear they mean something else.

**Surface:**
> "Nice weather."

**Subtext (said by someone standing at a funeral):** I can't handle this silence.

The reader reads the line and the context and feels the real meaning. Don't explain it.

---

### RULE 8.4: INTERRUPTIONS, TRAIL-OFFS, AND OVERLAP ARE REALISTIC

**Interruption:**
> "I think we should—"
> "No."

**Trail-off:**
> "He was standing right there, and then he just..."

**Overlap (in transcripts):**
> DR. VOSS: The artifact appears to—
> CAPT. REYES: —it's moving, Doctor.

---

## 9. EMOTION & ATMOSPHERE RULES

---

### RULE 9.1: EMOTION IS BEHAVIOR, NOT LANGUAGE

| Instead of... | Write... |
|---|---|
| She felt devastated | She sat on the kitchen floor for two hours |
| He was furious | He threw the mug. Then he picked up the pieces. Then he threw them again |
| They were terrified | They didn't open the door. They didn't answer the phone. They didn't breathe |
| She was in love | She learned to cook his mother's recipes without being asked |
| He was guilty | He over-tipped the waiter. He called his mother. He didn't sleep |

---

### RULE 9.2: ATMOSPHERE IS BUILT FROM SPECIFIC SENSORY DETAILS

Not "the room felt eerie." Instead:
- The fluorescent light buzzed at a frequency between two notes
- The carpet was damp in a perfect circle under the chair
- The clock ticked, but the second hand moved counterclockwise

Three specific, wrong details create more atmosphere than three paragraphs of adjectives.

---

### RULE 9.3: SILENCE IS A TOOL

The most powerful moment in any story is the thing that ISN'T said.

- A character who doesn't answer a question
- A document with a missing page
- A transcript with a [SILENCE — 14 SECONDS] notation
- A scene that ends one line before the reader expects it to

---

### RULE 9.4: ESCALATE THROUGH RESTRAINT

The more extreme the event, the more restrained the writing should be. Save the fancy language for small moments. For big moments, be blunt.

**Small moment (poetic):**
> The coffee was the color of his mother's kitchen, thirty years ago, when the world was smaller and the mornings were slower.

**Big moment (blunt):**
> The building collapsed.

The contrast makes both more powerful.

---

## 10. PACING & STRUCTURE RULES

---

### RULE 10.1: SHORT SENTENCES = FAST, LONG SENTENCES = SLOW

This is the most basic pacing tool. Use it intentionally.

**Fast:**
> Run. Left. Door. Locked. Window. Broken. Out.

**Slow:**
> He stood in the doorway for a long time, watching the rain move in sheets across the parking lot, and tried to remember what it felt like to not be tired.

---

### RULE 10.2: PLANT AND PAYOFF

Every setup must have a payoff. Every payoff must have a prior setup.

If you mention a fire extinguisher in Chapter 3, someone better use it by Chapter 9. If someone uses a fire extinguisher in Chapter 9, you better have mentioned it before.

This applies to:
- Objects
- Information
- Character traits
- Rules of the world
- Lines of dialogue

---

### RULE 10.3: THE RULE OF THREE

Humans process things best in threes:
- Three attempts before success
- Three examples to establish a pattern
- Three beats to build to a punchline or revelation
- Three documents before the situation escalates

---

### RULE 10.4: CUT THE FIRST DRAFT'S FIRST PARAGRAPH

Your first paragraph is usually you warming up. The real story starts at paragraph two. Delete paragraph one. Start where the story starts.

---

### RULE 10.5: END SCENES AT THE POINT OF MAXIMUM TENSION

Don't resolve the scene and then keep writing. End on:
- A question
- A revelation
- A threat
- A door opening
- A sound

Let the reader carry the tension to the next scene.

---

## 11. GENRE-SPECIFIC NOTES

---

### HORROR
- Never describe the monster fully. Describe its EFFECTS.
- Normal things done wrong are scarier than scary things done normally.
- The character should have a plan. The plan should fail. The backup plan should fail too.
- Horror is not gore. Horror is the moment BEFORE the gore.

### SCI-FI
- Explain technology through USE, not exposition.
- A character doesn't explain how a phone works. They just use it. Same rule applies to FTL drives.
- The science doesn't have to be real. It has to be CONSISTENT.

### MYSTERY/THRILLER
- The reader should be able to solve it. Play fair.
- Every clue should be visible in retrospect.
- The best twist is the one the reader could have seen coming but didn't.

### FANTASY
- World-building through character experience, not encyclopedia entries.
- A farmer knows farming. A king knows court politics. Write what each character would know.
- Magic systems need COSTS. A spell that costs nothing is boring.

### ROMANCE
- Chemistry is in the SMALL moments — a glance, a hand on a shoulder, a remembered preference.
- Dialogue is everything. If they have no banter, they have no chemistry.
- The obstacle must be real. Misunderstandings that could be solved by a 30-second conversation are not real obstacles.

---

## 12. QUICK REFERENCE CHEAT SHEET

### Before Writing Any Scene, Ask:

| # | Question |
|---|---|
| 1 | Whose perspective is this? |
| 2 | What do they WANT right now? |
| 3 | What's stopping them? |
| 4 | What changes by the end of the scene? |
| 5 | What would this character NOTICE (not what would a camera see)? |
| 6 | Can I cut the first paragraph? |
| 7 | Am I telling the reader what to feel instead of making them feel it? |

---

### The One-Sentence Summary of This Entire Document:

**"Write what happened. Don't write what it felt like. The reader will feel it."**

---

*Version 1.0 — Compiled for cross-AI narrative consistency*
*Applicable to: Novel, Narrative, Document, Narrative Document, and hybrid formats*

---

# 13. USER-SPECIFIC PRIORITY ADDENDUM — VERSION 1.1

These instructions are confirmed user preferences and take priority over older or more general guidance in this document whenever they differ.

## 13.1 No Unrequested Files — No Exceptions by Assumption

Do **not** create, update, replace, save, package, or present a file unless the user explicitly asks for a file action.

Long content does **not** automatically justify creating a file. If a narrative would exceed a response limit:

1. Stop at a natural dramatic, conversational, or informational boundary.
2. State only that the next part will continue when the user says so.
3. Do not summarize, compress, skip ahead, or create a file as a workaround.

## 13.2 Chat Is the Canonical First Draft

Write requested narrative, dialogue, scenes, and documents directly in chat first. Use readable Markdown styling in chat, but do not create a Markdown, text, code, Office, or other file unless asked.

Do not use code blocks, plain-text boxes, `.txt` boxes, or Markdown quote boxes automatically. Use them only when they serve a real in-world purpose, such as an embedded report, terminal display, letter, transcript, inscription, or message.

## 13.3 Required Long-Form Story Delivery

All long-form fiction follows:

> **Act X - Chapter Y - Part Z**

Write **one Part per response**. Stop after that Part and wait for the user’s direction. Do not write future Parts merely because the planned direction seems obvious.

Each Part should be substantial, slow-burn, and scene-complete enough to be satisfying, but it must not be padded with empty adjectives or repetitive internal monologue merely to reach a count.

## 13.4 Dialogue Format

For ordinary narrative dialogue, use the speaker-first format:

> **[Character Name]** Dialogue.

Example:

**[Angela]** “May you find your book in this place.”

Use this consistently unless the user explicitly requests a different in-world format, such as a screenplay, official transcript, chat log, radio transcript, or document.

## 13.5 Character Knowledge Boundary

The AI may know the wider plot. Characters do not.

A character can know something only if they:

- personally experienced or witnessed it;
- were told it by another character;
- read, heard, accessed, or completed the relevant information;
- logically deduced it from evidence already available to them;
- possess an explicitly established in-world ability that grants that knowledge, with its limits shown.

Do not write that a character “somehow knew,” “instinctively understood,” “felt the truth,” or “sensed a lie” without an established reason.

Confusion, uncertainty, incorrect conclusions, partial evidence, and wrong guesses are valid story material. Do not erase them just to move the plot faster.

## 13.6 No Meta-Aware Characters

Characters do not know they are fictional. They do not refer to chapters, scenes, acts, plot, narrative, protagonists, villains, authors, readers, or genre conventions as though they know they live in a story.

The only exception is an explicitly user-approved metafiction premise established before the relevant scene.

## 13.7 Reading and Information Sequence

If a character reads, examines, listens to, or reviews a document, message, report, file, book, terminal entry, recording, letter, transcript, note, or inscription:

- show the actual material the character reaches in the scene;
- show only the portion they have genuinely read, heard, or accessed;
- do not let them react to later pages, hidden sections, missing files, or information they have not reached;
- preserve the document’s own voice and formatting where it matters to the story;
- do not replace important readable material with “it explained that…” summaries.

The reader discovers written information at the same pace as the character.

## 13.8 Consequences and Side Characters

Side characters may die, be injured, disappear, fail, betray others, or survive depending on established danger, choice, setting rules, and consequence. Do not preserve a character merely because they are named or sympathetic.

At the same time, death must not be cheap decoration. It should alter the surviving characters, available information, practical situation, relationships, or later choices.

## 13.9 Narrative Style Priorities

- Show emotion through behavior, attention, interruption, silence, choices, and concrete physical detail.
- Describe what the viewpoint character would notice, not what an omniscient camera would catalog.
- Use specific sensory detail rather than vague atmosphere.
- Keep intense events restrained and concrete; do not inflate them with purple prose.
- Use Markdown headings, spacing, selective bold, italics, dividers, and lists in chat for readability and emotional structure.
- Avoid AI-writing tics listed in this file: vague dread, weather mirroring emotion, “little did they know,” “something shifted,” “palpable tension,” ozone openings, “a testament to,” “symphony of,” and similar empty dramatic phrasing.
- Plant information, objects, character habits, and setting rules before their payoff whenever the story allows it.

## 13.10 Canon and Crossover Writing

When writing within an existing setting, do not give characters knowledge of lore they have not encountered. Do not use later canon revelations as if earlier-era characters know them.

For crossover writing, preserve each setting’s consequences, institutions, rules, and character knowledge boundaries. A powerful visitor does not automatically understand local politics, metaphysics, technology, taboo law, or hidden history.

---

*Version 1.1 — User-specific priority addendum for narrative consistency*
