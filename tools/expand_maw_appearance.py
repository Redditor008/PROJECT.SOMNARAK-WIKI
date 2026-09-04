#!/usr/bin/env python3
"""Batch tool: publish 150-205 word Appearance sections on M.A.W. item records.

Continues the owner-ordered appearance-expansion batches (sets 001-157 were
completed by the previous session). For each set in BATCH the tool:

1. composes (or takes from OVERRIDES) a 150-205 word source-led Appearance
   paragraph for the Weapon/Suit/Gift registry records, built exclusively
   from that record's own fields (resting form, active form, recognition
   rule, effect, costs, maintenance, rejection rule, shutdown);
2. inserts `## Appearance` into the registry markdown before the statistics
   heading (same placement as the batch-5 records);
3. inserts `<h2 id="appearance">Appearance</h2><p>...</p>` into the public
   docs/maw page between the Overview paragraph and Extraction or Bestowal
   (same placement as the previous batches);
4. verifies md<->html parity and the word range.

Usage:  python3 tools/expand_maw_appearance.py           # dry-run report
        python3 tools/expand_maw_appearance.py --write   # apply
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "REFERENCE_SOMNARAK_WIKI" / "LORE or REFERANCE" / "M.A.W. Codex_Set Registry"
DOCS_MAW = ROOT / "docs" / "maw"

BATCHES = {
    "6": ["159", "160", "165", "168", "169", "170", "175", "176", "180", "184", "185", "189"],
    "7": ["190", "193", "195", "200", "219", "220", "222", "225", "230", "233", "235", "236"],
    "8": ["240", "245", "247", "249", "250", "252", "255", "260", "270", "275", "280", "283"],
}
DEFAULT_BATCH = "8"

WORD_MIN, WORD_MAX = 150, 205

STATS_HEADINGS = [
    "## CORE STATISTICS",
    "## PROTECTION STATISTICS",
    "## GIFT STATISTICS",
    "## GIFT STATISTICS & FUNCTION",
    "## STATISTICS & FUNCTION",
    "## PROTECTION FILE",
    "## FUNCTION & COST",
    "## FUNCTION & HISTORY",
    "## HISTORY & FUNCTION",
    "## COMBAT FILE",
    "## PROTECTIVE FILE",
    "## EFFECT FILE",
]


def decap(s: str) -> str:
    return s[0].lower() + s[1:] if s else s


def strip_period(s: str) -> str:
    return s.rstrip().rstrip(".")


def ensure_period(s: str) -> str:
    s = s.rstrip()
    return s if s.endswith((".", "!", "?")) else s + "."


def table_field(text: str, label: str) -> str | None:
    m = re.search(r"^\|\s*" + re.escape(label) + r"\s*\|\s*(.+?)\s*\|\s*$", text, re.M)
    return m.group(1).strip() if m else None


def bold_field(text: str, label: str) -> str | None:
    m = re.search(r"\*\*" + re.escape(label) + r":\*\*\s*(.+)", text)
    return m.group(1).strip() if m else None


def effect_sentence(text: str) -> str | None:
    m = re.search(r"\*\*Effect:\*\*\s*(.+)", text)
    return m.group(1).strip() if m else None


def storage_sentence(maintenance: str | None) -> str | None:
    if not maintenance:
        return None
    for sent in re.split(r"(?<=\.)\s+", maintenance):
        if re.search(r"\b(stored|hung|aired|kept|rests|never)\b", sent):
            return sent.strip()
    return None


def op_cost_sentence(cost: str | None) -> str | None:
    if not cost:
        return None
    cost = ensure_period(cost)
    if cost.lower().startswith("no echo expenditure"):
        rest = cost.split(";", 1)
        tail = rest[1].strip() if len(rest) > 1 else ""
        if tail:
            return "It carries no Echo cost, but " + ensure_period(decap(tail))
        return "It carries no Echo cost."
    return cost


def compose(md_text: str) -> str | None:
    """Compose an Appearance paragraph from a full-table registry record."""
    name = table_field(md_text, "Official name")
    resting = table_field(md_text, "Resting form")
    active = table_field(md_text, "Active form")
    recognition = table_field(md_text, "Recognition rule")
    op_cost = table_field(md_text, "Operational cost")
    bind_cost = table_field(md_text, "Binding cost")
    recovery = table_field(md_text, "Recovery")
    binding_req = bold_field(md_text, "Binding requirement")
    rejection = bold_field(md_text, "Rejection rule")
    maintenance = bold_field(md_text, "Maintenance")
    shutdown = bold_field(md_text, "Emergency shutdown")
    effect = effect_sentence(md_text)

    if not (name and resting):
        return None

    sentences: list[tuple[str, int]] = []  # (sentence, priority: lower = keep longer)
    sentences.append((f"{name} is {ensure_period(decap(resting))}", 0))
    if recognition:
        sentences.append((ensure_period(recognition), 2))
    if active:
        sentences.append(("In active use " + ensure_period(decap(active)), 0))
    if effect:
        sentences.append(("At full activation, " + ensure_period(decap(effect)), 1))
    if binding_req:
        sentences.append((ensure_period(binding_req), 1))
    cost_s = op_cost_sentence(op_cost)
    if cost_s:
        sentences.append((cost_s, 1))
    if bind_cost:
        sentences.append((ensure_period(bind_cost), 3))
    if recovery:
        sentences.append((ensure_period(recovery), 3))
    store = storage_sentence(maintenance)
    if store:
        sentences.append((store, 2))
    if rejection:
        sentences.append((ensure_period(rejection), 1))
    if shutdown:
        first = re.split(r"(?<=\.)\s+", shutdown)[0]
        sentences.append((strip_period(first) + " during shutdown.", 1))

    def text_for(kept: list[str]) -> str:
        return " ".join(kept)

    kept = [s for s, _ in sentences]
    words = len(text_for(kept).split())
    # trim lowest-priority sentences while above the ceiling
    for prio in (3, 2):
        i = len(sentences) - 1
        while words > WORD_MAX and i >= 0:
            if sentences[i][1] == prio and sentences[i][0] in kept:
                kept.remove(sentences[i][0])
                words = len(text_for(kept).split())
            i -= 1
    # pad with further record fields while below the floor
    if words < WORD_MIN:
        extras = []
        overload = table_field(md_text, "Overload threshold")
        if overload:
            extras.append("Its overload threshold is reached when " + ensure_period(decap(overload)))
        activation = bold_field(md_text, "Activation rule")
        if activation:
            extras.append("The triggered protection engages once " + ensure_period(decap(activation)))
        stacking = table_field(md_text, "Stacking rule")
        if stacking:
            extras.append(ensure_period(stacking))
        removal = table_field(md_text, "Removal rule")
        if removal:
            extras.append(ensure_period(removal))
        echo = table_field(md_text, "Echo cost")
        if echo:
            extras.append("Registration and binding require " + ensure_period(decap(echo)))
        for extra in extras:
            if words >= WORD_MIN:
                break
            kept.append(extra)
            words = len(text_for(kept).split())
    return text_for(kept)


# Hand-written paragraphs for the compact/prose-format records of this batch
# (source fields quoted or paraphrased from the record itself).
OVERRIDES: dict[str, str] = {
    "w-175": (
        "The Dream Requiem is a blue blade of Han crystal threaded with shifting light, the strands moving "
        "under the surface like a path traced through a sleeping room. In rest the thread-light wanders "
        "without direction and the blade stays silent; it only hums after the bearer states the waking cue "
        "and the dreamer\u2019s consent boundary aloud. Drawn, the threads align into a single luminous line down "
        "the flat, and a Lament Pierce along that line can separate a person from a maze built out of their "
        "own hidden desire without declaring the dream false. The grip is wrapped in pale blue cord and the "
        "guard is a thin oval that frames the thread-light like a doorway. The bearer carries unwept dream "
        "grief after every use and requires a waking orientation check when a full Pierce line has been run. "
        "The blade is never drawn without a waking anchor, and calling a mirrored desire \u201cwhat must happen\u201d "
        "turns the path inward and ends activation. The anchor covers the thread line, gives the cue, and "
        "cases the blade during shutdown."
    ),
    "s-175": (
        "The Dream Shroud is a suit of deep-blue dream-cloth that hangs like slow water, its folds catching "
        "light in the shapes of rooms the wearer has wanted and never lived in. A single waking-anchor thread "
        "runs from the collar down the breast and must remain visible outside the Dream at all times; the "
        "suit is not fastened until that thread is confirmed by the outside observer. Inside a desired Dream "
        "image the fabric steadies the wearer\u2019s emotional stability, diffusing the Lament of the image while "
        "the collar thread keeps one line of the present body legible. When the anchor gives the cue, the "
        "cloth pulls taut along that thread and rejects one Dream escalation, returning attention to the "
        "current body. Minor joys go numb after long immersion, and the anchor may end use over the wearer\u2019s "
        "objection. The fabric begins showing a desired scene on its own when the wearer treats waking as "
        "failure, and a Shroud whose collar thread has faded is sealed immediately. The anchor unfastens the "
        "collar thread and calls the bearer into current light during shutdown."
    ),
    "g-175": (
        "The Dream Thread is a thin band of woven blue thread worn at the tail line, light enough to forget "
        "until a dream is near. At rest the weave lies flat and colorless; where a dreamer has permitted "
        "contact, single strands lift and glow, tracing the boundary of the consented Dream so the bearer can "
        "see exactly where permission ends. During entry the band pays out an almost invisible filament that "
        "trails back to the outside anchor, and the bearer walks another person\u2019s dream holding that one "
        "line. The Thread allows observation, support, or shared navigation, never extraction: it cannot read "
        "secrets as inventory, alter a dreamer\u2019s choice, or remain after the anchor cue. Every dream entered "
        "leaves an emotional fragment lodged in the weave, a feeling that was never the bearer\u2019s, and each "
        "fragment must be named and separated in debrief before the band is worn again. Entering without "
        "consent tangles the Thread around the bearer\u2019s own desire and blocks a safe return until the anchor "
        "intervenes. The anchor unhooks the band after debrief during shutdown; cutting it leaves the bearer "
        "emotionally inside the last dream."
    ),
    "w-176": (
        "The Loom\u2019s Dream Requiem is a long blue blade whose crystal holds a single woven thread down its "
        "center, the weave loosening and re-tightening as nearby dream-cloth shifts. The blade cannot draw "
        "until the released thread inside it is marked with both anchors \u2014 one Dream, one waking \u2014 and the "
        "marks show as two small knots of light at the guard. In use the edge runs a Lament Pierce that "
        "loosens a temporary dream reality where it has begun overwriting a current room, unpicking the "
        "construct a line at a time rather than tearing it. At full activation the weapon dissolves one "
        "escalating woven construct across its Pierce line and returns its emotional material to the Loom\u2019s "
        "custody; it cannot decide which future was worth living. The bearer carries unwept dream grief, and "
        "recovery requires the temporary construct to be fully unmade. Thread knots gather around the hilt "
        "when the bearer wants to preserve a dream, and a black knot means a channel was not closed. Both "
        "anchors close the channel and case the blade during shutdown; breaking it leaves a woven room in the "
        "bearer\u2019s next sleep."
    ),
    "s-176": (
        "This Dream Shroud is cut from pale loom-cloth that shows two textures at once \u2014 the weave of the "
        "current room and, faintly beneath it, the weave of whatever construct the wearer stands inside. Two "
        "anchor knots sit at the collar, one held by a waking witness and one by a Dream witness, and the "
        "suit gives only ordinary resistance unless both knots are tied and held by separate hands. Worn "
        "correctly, the fabric keeps the wearer\u2019s current body and Dream identity distinct from a "
        "Loom-created temporary reality, so a woven room can be entered, worked, and left without the "
        "wearer\u2019s outline joining the cloth. When both witnesses jointly invoke the return cue, the Shroud "
        "breaks one Dream bleed and sets the wearer back into current space. Minor joys go numb after "
        "immersion, and either anchor may end use. One knot tightens when the bearer starts privileging the "
        "dream over waking consent, and a two-knot deadlock puts the suit into Dream Gate custody. Both "
        "witnesses release their knots together during shutdown; cutting either knot leaves the wearer split "
        "between the construct and the current room."
    ),
    "g-176": (
        "The Dream Shuttle is a small charm shaped like a weaver\u2019s shuttle, carved from blue crystal and "
        "wound with a single empty thread channel. It hangs at the tail line and remains completely still \u2014 "
        "no glow, no warmth \u2014 until the bearer voluntarily names a personal memory they are willing to "
        "contribute; only then does the channel fill with a thin line of light drawn from that memory. In use "
        "the Shuttle passes once through the air like a loom stroke and weaves one controlled illusion for "
        "care, training, or safe route visualization, built from the offered memory and nothing else. The "
        "construct cannot replace reality, cannot sustain itself after its emotional source closes, and "
        "cannot take a private memory as material without permission. The contributed memory grows less vivid "
        "with every weaving, a cost the bearer accepts in advance. The Shuttle moves on its own when the "
        "bearer wants an easier reality, and a snapped shuttle stays out of use until Dream Gate review. Both "
        "anchors unthread the illusion during shutdown; breaking the Shuttle leaves the memory lodged in the "
        "bearer\u2019s next dream."
    ),
    "w-180": (
        "The Debt Maul is a broad black maul of Han steel whose head is cut with the flat, layered lines of a "
        "ledger wall, each layer slightly offset like bricks of recorded obligation. The haft is long, "
        "iron-banded, and cold, and the head will not rise from the ground until a custodian has identified a "
        "route beyond the pressure block it is meant to open. In use the weapon drives a Weight Pierce into a "
        "present debt barrier \u2014 never into a person \u2014 and at full activation it holds a Wall-like Weight "
        "surge open long enough for people to reach review, care, or transit. It cannot demolish debt, decide "
        "a claim, or create private passage, and a bearer who swings it for advantage finds it immovable. The "
        "bearer grows progressively heavier and ages slightly with prolonged use, and every deployment ends "
        "in a route review. The head grows heavier still when the bearer calls a person a burden, and a black "
        "line appears along the haft when a route was omitted. The custodian covers the head and confirms the "
        "route during shutdown; breaking the Maul embeds debt pressure in the floor."
    ),
    "s-180": (
        "The Debt Shield is a black harness built around a broad backplate, worn like a bearer\u2019s yoke rather "
        "than armor. The plate\u2019s surface is smooth Han iron that takes marks the way a ledger takes entries: "
        "every Weight impact the suit absorbs appears as a thin engraved line, and the lines remain visible "
        "until they are discharged through review. The straps cross the chest and leave the hands free, and "
        "the plate rides high enough that its marks can be read by a custodian standing behind the wearer. In "
        "the field the Shield endures direct Weight damage by converting impact into stored karmic pressure; "
        "when the custodian confirms a support or review action, one stored mark releases into the "
        "accountable route instead of the bearer\u2019s body. The harness grows heavier with every absorbed "
        "impact, and a plate that is never discharged eventually becomes too heavy to wear. Marks multiply "
        "after unreviewed impacts, and hiding the plate closes it and drops protection to normal. A fully "
        "black plate is sealed immediately. The custodian opens the discharge latch during shutdown; cutting "
        "the harness spills its stored Weight into the bearer\u2019s next route."
    ),
    "g-180": (
        "The Debt Charm is a small black charm cut in the shape of a single wall block, dense for its size "
        "and worn at the head. Its faces are blank until a debt pressure begins closing a current route; then "
        "the block glows along one edge, always toward the block itself and never toward a person who might "
        "be blamed for it. In use, with a custodian present and the affected person\u2019s support, the Charm "
        "reveals the first review or support action that can keep the route open \u2014 an unfiled dispute, a "
        "missed appeal, a case that needs a reader. It cannot forgive debt, set a judgment, or bypass "
        "consent. The bearer moves more slowly under recognized burden, and every ignored reading adds Weight "
        "to their own frame. A glow that persists after action means the review was performative, and a Charm "
        "that points at every debtor at once has caught the bearer\u2019s anger and must be set down. It is "
        "stored beside completed route records, never inside a collection file. The custodian covers the "
        "block face during shutdown; shattering it makes every nearby obligation feel physically immediate."
    ),
    "w-184": (
        "The Redacted Lens is a weapon built around a disc of pale Void glass set in a slender white frame, "
        "held like a short blade with the lens where an edge would be. At rest the glass is fogged and shows "
        "nothing; it opens \u2014 clears to a hard, readable transparency \u2014 only after the bearer states aloud "
        "what is known, what is unknown, and what is merely inferred, as three separate declarations. Through "
        "the cleared glass an erasure field becomes visible as a pale outline, and a Void Pierce along the "
        "sightline separates a target from active erasure pressure. At full activation, under Archive "
        "witness, the Lens stabilizes an absence so fragments can be preserved without fabricating a "
        "restoration; it cannot identify the erased person, restore a deleted life, or prove a desired "
        "explanation. Each use takes a small nameless memory from the bearer, and custody review follows "
        "every draw. The glass reflects a complete face when the bearer wants certainty too badly, and an "
        "opaque Lens is sealed. The witness covers the glass and names the blank during shutdown; breaking it "
        "scatters false history fragments."
    ),
    "s-184": (
        "The Redacted Veil is a full-length suit of pale, half-transparent cloth that blurs the wearer\u2019s "
        "outline without ever fully hiding it \u2014 by rule, an Archive witness must still be able to read the "
        "wearer\u2019s name through the fabric, and the Veil is not worn if the name cannot be read. The weave is "
        "Void-pale and faintly cool, with a collar that holds the wearer\u2019s identity card visible at the "
        "throat. Beside a missing history the Veil protects identity: it keeps the erasure field from "
        "attaching to the wearer while preserving the difference between a blank and an answer. When the "
        "witness calls the bearer by name and names the known record, the Veil rejects one Void surge. The "
        "wearer feels faintly absent to themself while it is active, and the witness may terminate use. The "
        "collar empties when the wearer wants an answer too quickly, and a wearer who supplies unsupported "
        "details finds the veil turn transparent and give nothing. A blank veil goes to Archive custody at "
        "once. The witness unfastens the collar during shutdown; cutting the cloth attaches an absence to the "
        "wearer\u2019s reflection."
    ),
    "g-184": (
        "The Redacted Ring is a plain circle of pale glass, unmarked and slightly cold, worn at the head. "
        "Light passes through it wrong: looking through the Ring at a record, a room, or a person\u2019s account, "
        "the bearer sees one place where something should be and is not \u2014 a missing entry, a gap in a year, "
        "an absent name \u2014 outlined as a faint pale border. The Ring reveals the missing element and the "
        "boundary of the surrounding fragments, and nothing more; it never supplies the missing person\u2019s "
        "whole story, never establishes motive, and never converts an absence into evidence for a preferred "
        "explanation. Every reading takes certainty from one of the bearer\u2019s own remembered events, so that "
        "a bearer who uses the Ring often can no longer swear to the details of their own past. It brightens "
        "when the bearer is reaching for a satisfying story, and a Ring gone dark is sealed as a "
        "false-history hazard. It is worn only under Archive witness and stored with the custody ledger. The "
        "witness covers the Ring and closes custody during shutdown; breaking it fragments a current memory "
        "across everyone watching."
    ),
    "w-185": (
        "The Gallery Requiem is a blue blade with the texture of layered paint rather than polished crystal: "
        "its flat carries fine brush-stroke ridges, and close to the guard the color deepens as if a "
        "portrait\u2019s background had been dragged down the steel. It was formed from a paint echo after a "
        "verified name and an explicit unknown were preserved beside a faceless frame, and the blade "
        "remembers that origin \u2014 it binds only to a bearer working under Archive witness, and it turns "
        "silent in the hand of anyone forcing a portrait to yield a full biography. Drawn before a whispering "
        "frame, the edge steadies the air so one forgotten history becomes emotionally legible, without "
        "compelling a living witness and without inventing a single missing detail. The bearer receives the "
        "Gallery\u2019s unwept grief in exchange, and repeated use brings involuntary weeping. Paint-like blue "
        "marks surface along the flat when the bearer wants an answer too badly, and the blade is maintained "
        "with a known/unknown custody card between uses. The Archive witness cases the blade and names the "
        "unresolved field during shutdown."
    ),
    "s-185": (
        "The Gallery Shroud is a long wrap of blue silk so fine that portrait light passes through it "
        "softened, as if every image behind the wearer had been moved one room away. The silk formed from a "
        "Gallery echo after a listener walked the full corridor without answering each whisper, and the weave "
        "keeps that discipline: worn correctly it muffles a portrait chorus to a single voice\u2019s distance, "
        "quiet enough for one history to be witnessed without emotional overload, but it never silences the "
        "frames entirely. An Archive witness must hold the names under review before the Shroud is fastened, "
        "and it rejects a wearer who uses the silence to avoid the records themselves. Minor joys go numb "
        "after extended voice exposure, and thin whisper lines appear in the hem when the wearer starts "
        "holding names alone; a fully silent hem is the overload sign. It is maintained with a known/unknown "
        "list and a second listener, and the witness removes the collar if the wearer begins treating every "
        "whisper as a personal command."
    ),
    "g-185": (
        "The Gallery Stone is a smooth blue stone the size of a thumb joint, worn at the tail line, with a "
        "surface that feels faintly wet, like paint that never quite dried. Held before a forgotten image "
        "under Archive witness, the Stone warms and returns one verified name attached to that image \u2014 a "
        "surname from a frame, a first name from a corridor plaque \u2014 and nothing else of the life behind "
        "it. It is bestowed only after a listener has restored a name without changing a portrait\u2019s missing "
        "history, and it binds to an Archive custodian; it rejects any bearer who tries to use a recovered "
        "name as a key to private records. The cost arrives at night: the bearer hears every name still "
        "beyond recovery, dozens of incomplete syllables filling their sleep until the recovered name is "
        "properly filed. The Stone grows cold when consulted out of curiosity and hums continuously when the "
        "unrecovered names are treated as a burden to solve alone. It is kept with the name-custody ledger, "
        "and the witness covers it after each reading; breaking it scatters name echoes through every nearby "
        "portrait."
    ),
    "w-189": (
        "The Fading Requiem is a short blue blade that looks permanently on the edge of dispersal: its "
        "surface is made of compacted dust-echo, matte rather than bright, and fine grains lift from the "
        "spine whenever the weapon moves quickly. It condensed from a Desolate survey that documented a "
        "settlement\u2019s last trace and then let Ephemera fade at dusk, and it keeps the manners of that "
        "survey. Raised over a fading site, the edge steadies one memory field \u2014 a street plan, a doorway, "
        "the outline of a well \u2014 long enough for a witness to record it, and no longer; it does not keep the "
        "ruin from fading, and using it to force a place to remain makes the blade itself dissolve into "
        "dust. The bearer feels the unwept grief of the ruin after each use, and blue dust gathers on the "
        "hilt when archival custody is postponed. It binds to a route custodian and refuses any bearer "
        "treating a destroyed place as salvage. The blade is maintained with a route record, and the map "
        "custodian cases it once the recorded memory reaches storage."
    ),
    "s-189": (
        "The Fading Shroud is a survey cloak of pale blue weave that seems half gone even when new: the hem "
        "fades to translucence, and in Desolate light the whole garment reads as an outline rather than a "
        "solid shape. It formed from a fading dust echo when a surveyor stayed to witness a ruin\u2019s last "
        "outline and withdrew before treating the trace as a home, and it protects exactly that kind of "
        "witness. Worn over survey gear it preserves the cartographer\u2019s emotional boundary while a "
        "place-memory fades around them, resisting the Lament of disappearance while the record is made. The "
        "cost accumulates quietly \u2014 minor joys go numb after too many fading-site records, and one scout "
        "could not taste a familiar meal until a surviving witness had received the record. Dust appears on "
        "the hem when the bearer tries to keep every ruin alive alone, and a fully pale shroud means the "
        "witness is becoming another fading record. It is issued with a route custodian and a post-survey "
        "rest requirement, maintained with a named custodian and release plan; cut fabric is a Desolate "
        "dispersal hazard."
    ),
    "g-189": (
        "The Fading Brick is a single blue brick, light as dried clay, its faces worn smooth as if it had "
        "been handled by everyone who ever lived near it. It is bestowed only after a settlement trace has "
        "been recorded without physical collection, and it binds to a map custodian. Within it the Brick can "
        "hold exactly one memory of a destroyed place \u2014 a well\u2019s position, a lane\u2019s turning, the height of "
        "a door \u2014 and it replays that memory only under permitted review. The cost is constant: the bearer "
        "hears the ruin\u2019s final silence, the last sound the place made, carried under every quiet moment "
        "until the map and witness note reach Archive custody. The Brick grows heavy when it is treated as a "
        "souvenir and turns transparent if the place-memory is claimed as private property. It is stored with "
        "its map and custody record, never displayed. The custodian covers it after each permitted replay "
        "during shutdown; breaking the Brick releases the ruin\u2019s silence directly into the bearer\u2019s "
        "hearing."
    ),
}

OVERRIDES.update({
    # ---- batch 7 (compact/prose-format records; all paragraphs source-led) ----
    "w-190": (
        "The Rage Fang is a crimson fang of Han iron condensed from a fissure echo \u2014 the kind that forms "
        "only after the Rage Statue\u2019s fist lowers through acknowledged grief, never through forced impact. "
        "The blade carries that origin in its surface: fine fissure lines run from tip to guard, and they "
        "heat visibly, glowing a deeper red, whenever the bearer\u2019s intent drifts from justice toward "
        "revenge. In use the Fang opens a bounded Grudge path against active injustice pressure \u2014 a coercive "
        "field, a detention line \u2014 and the bounds are literal: the red path ends where the accountability "
        "route begins, and the weapon cannot punish a historical grievance on the bearer\u2019s behalf. Old "
        "wounds ache while it is drawn, and anger becomes physically immediate, heat in the forearms and "
        "jaw. It binds only alongside an accountability witness empowered to stop retaliation-driven use, "
        "and a fissure ridge that closes into a solid red line is the withdrawal sign \u2014 witness shutdown, no "
        "exceptions. It is maintained with the named injustice and the current remedy written beside it, "
        "never with a list of enemies."
    ),
    "s-190": (
        "The Rage Gauntlet is a heavy crimson gauntlet formed from a cooled fissure \u2014 stone-dark metal over "
        "the knuckles, with hairline crack patterns that pulse faintly warm when an old grievance passes "
        "through the wearer\u2019s mind. It came into being when the Statue\u2019s raised fist was witnessed without "
        "being forced down, and the armor keeps that discipline in its fit: the fingers close easily around "
        "present harm and stiffen around remembered harm. Worn in the field it adds accumulated resentment "
        "to a defensive strike, but only while the assigned response witness can name the actual present "
        "harm being answered. The cost is written into the hand \u2014 the wearer cannot easily distinguish "
        "justice from retaliation while the plates are warm. Fist plates pulse at old grievances, and a "
        "gauntlet that clenches by itself is withdrawn from issue immediately. It is maintained by naming "
        "the present harm, the remedy, and the stop point before each wearing, and it rejects any bearer who "
        "calls every anger righteous. The witness opens the palm seam for shutdown; cutting the gauntlet "
        "free releases a Grudge punch through the wearer\u2019s own arm."
    ),
    "g-190": (
        "The Rage Charm is a small crimson tail-charm cut like a clenched fist that has not yet fallen, its "
        "surface crossed with the Statue\u2019s fissure grain. It is bestowed only when a worker acknowledges "
        "the injustice behind the Statue\u2019s pose without treating the Statue as permission to strike, and it "
        "binds to a response witness from the first day of carry. At rest it is warm as held breath; in use "
        "it marks one held anger that needs a present accountability route \u2014 an unaddressed record, an "
        "unopened review \u2014 and points at the route, not at the nearest person. The bearer pays in temper: "
        "carrying the Charm shortens it, and the sharpness does not ease until the marked review is entered "
        "into the action log. It burns outright near revenge fantasies, and a Charm that points at every "
        "person in the room means the bearer arrived already furious and must set it down. It is maintained "
        "with a current remedy and a stop point recorded beside each marking. The witness covers it after "
        "action; breaking it sends a Grudge flare through the closest grievance."
    ),
    "w-193": (
        "The Wall\u2019s Maul is a massive black maul formed from an absence echo \u2014 the black that was left "
        "when former neighbors crossed the old line with witnesses from both histories. Its head is smooth, "
        "unmarked Han material that seems to swallow lamplight, and its weight is the Weight of a division "
        "no one can see anymore but everyone still walks around. The weapon will not lift for a single "
        "hand\u2019s cause: it requires representatives from both sides present, and it may not be wielded to "
        "prove reunion. Swung correctly it breaks an invisible Weight division field long enough for a "
        "current shared route to be established \u2014 an old road reopened for a joint memorial, a crossing "
        "made walkable \u2014 but it cannot erase lived separation, and the route stays open only while both "
        "groups keep the follow-up plan. The bearer grows progressively heavier, and use without mutual "
        "witness turns the Maul\u2019s force back on the one who swung it. Black cracks spread across the head "
        "when the bearer calls the divide solved. It is maintained with both history records side by side, "
        "and shutdown requires witnesses from both sides."
    ),
    "s-193": (
        "The Wall\u2019s Absence is a black veil-suit that reads less as fabric than as a gap given shape \u2014 a "
        "boundary-colored absence draped over the shoulders, formed after a witnessed crossing recognized "
        "that removing a wall had not ended the division. The cloth is matte black, edgeless in low light, "
        "and it binds only with a route observer drawn from each side of the former line. Deployed, it "
        "creates a temporary boundary against hostile force while keeping the negotiated passage visible \u2014 "
        "a wall that admits, openly, where it can be crossed. The wearer pays for the protection in empathy "
        "reversed: they feel every person kept on the other side for as long as the field stands, which is "
        "why the field is ended when the crossing plan begins, not when one group feels safer. The veil "
        "darkens when a passage is closed for convenience and grows heavy when the wearer starts treating a "
        "community as an outside. It is maintained by checking both histories and the passage route before "
        "each use. Both witnesses remove the collar together; cutting it leaves an invisible barrier "
        "standing in the room."
    ),
    "g-193": (
        "The Wall\u2019s Charm is a small black head-charm shaped like a short section of line \u2014 a boundary "
        "reduced to something that fits in a palm. It is bestowed only after a former boundary has been "
        "crossed with both histories named aloud, and it requires two route witnesses; it rejects every "
        "unilateral reading. Held over a district map or carried down a avoided street, the Charm identifies "
        "one invisible inherited barrier \u2014 not a physical obstacle but an old crossing custom, a habit of "
        "avoidance passed down until no one remembers choosing it. The bearer moves slower under its "
        "history, a drag in the legs that eases only when the barrier is addressed jointly. When a bearer "
        "wants simple blame, the Charm points at every line at once and gives nothing usable; the correct "
        "response is a joint visit, not a verdict of irrationality. It is maintained with both sides\u2019 "
        "accounts and a shared follow-up recorded together. The witnesses cover it after each route action; "
        "breaking the Charm hardens an invisible barrier around the bearer themselves."
    ),
    "w-195": (
        "The Sorrow Lens (weapon expression) is a pale reflection-echo blade \u2014 a flat, mirror-faced edge of "
        "Void-white Han glass that formed after a viewer named one grief with a companion and then looked "
        "away by choice. Nothing about it invites a second glance: its face holds the room dimly, the way a "
        "mirror does at dusk, and it clouds to full opacity the moment someone tries to use it to pry. In "
        "use the Lens separates a target from an identity overload caused by reflected grief, opening a "
        "boundary between a person and the mirrored loss that has trapped them, long enough for a companion "
        "to name the person\u2019s present body. It cannot reveal secrets, and it cannot prove that a grief "
        "belongs to anyone. The bearer pays a small nameless memory with each drawing, and a companion "
        "debrief is mandatory afterward. It requires a mirror witness to bind at all, and it refuses any use "
        "aimed at exposing another person\u2019s sorrow. It is maintained with consent records and witness "
        "notes, and the companion shutters the reflecting face to end every use."
    ),
    "s-195": (
        "The Sorrow Veil is a suit of pale, half-reflective weave that formed after a companion sat through "
        "a mirror gaze without interpreting the reflected grief for the viewer. Worn, it reads as a thin "
        "silver-grey film over ordinary clothing, and from certain angles the fabric returns not the room\u2019s "
        "light but a faint image of whoever stands beside the wearer \u2014 the companion thread made visible. "
        "The Veil resists Void reflection pressure near Learned Your Face while preserving that thread: the "
        "wearer can stand in the mirror\u2019s field and remain a person accompanied rather than a person "
        "absorbed. The cost is a faint absence \u2014 the wearer feels slightly missing to themself for the "
        "duration of wear. It binds only to a named witness who can stop the exposure, and the fitting rule "
        "is absolute: the collar fades when the bearer refuses companionship, and a threadless Veil is "
        "sealed. It is maintained with a consented mirror witness and a debrief after every exposure. The "
        "witness unfastens it at the first loss-of-self sign; cutting the fabric leaves a grief reflection "
        "hanging where the wearer stood."
    ),
    "g-195": (
        "The Sorrow Lens gift is a small lens-pendant of pale glass worn at the head, ground so fine that "
        "looking through it feels like looking slightly deeper than the surface of things. It is bestowed "
        "only after a viewer shares one private grief with a companion voluntarily, and it binds only under "
        "an empathy witness; pointed at a person without consent, the pendant simply warms and shows "
        "nothing. Used with consent, it reveals hidden sorrow in another person \u2014 grief they have not "
        "spoken, sometimes grief they cannot speak \u2014 and the cost is exact: the bearer experiences the "
        "observed sorrow as if it were their own, intensely enough that a separate debrief is standard "
        "procedure. The correct outcome of a reading is an offered support option, never a declaration of "
        "understanding. The pendant warms around unconsented curiosity and grows heavy when the bearer is "
        "carrying too many observed sorrows unreturned. It is maintained with consent, purpose, and empathy "
        "debrief recorded together. The witness covers it after each use; breaking it spreads the last "
        "observed grief into the bearer\u2019s own senses."
    ),
    "w-200": (
        "The Gatekeeper\u2019s Blade is a long crimson blade formed from the red echo Aegis left behind after "
        "lowering its weapon for a logged Gate arrival. The steel is deep red along the flat and brightens "
        "toward the edge, and a faint gate-arch watermark sits in the metal near the guard \u2014 visible only "
        "when the blade is raised at a boundary. It does not draw for an exclusion order: the wielder, the "
        "Gate Watch partner, the hostile condition, and the permitted route must all be named before the "
        "grip warms. In action the Blade marks a verified fleeing threat and prevents flight through the "
        "defined boundary, and its restraint is structural \u2014 it cannot mark an authorized returnee or a "
        "civilian using the declared passage. Every time the mark holds, the bearer feels the grief of "
        "historical exiles, the names in the old departure log pressing close. The blade heats when a bearer "
        "calls a person \u201cunauthorized\u201d without a current record, and the crimson edge darkens if the "
        "return lane is blocked. It is maintained with the incident map and route partner; the partner ends "
        "the mark, and breaking the blade creates a one-way Grudge barrier."
    ),
    "s-200": (
        "The Gatekeeper\u2019s Plate is scarred crimson armor \u2014 an echo given weight, its chest piece carrying "
        "an old diagonal scar that no polish removes. The metal stays cold in ordinary wear and becomes warm "
        "only around a current Gate threat, which makes the Plate its own threat gauge: a warm collar means "
        "the danger is real and present, a cold scar means the danger being described is remembered or "
        "invented. The collar will not seal until a passage observer is named, and the armor rejects use "
        "during any unreviewed exclusion. Its central mechanic is worn openly \u2014 the Plate holds a defensive "
        "line against Crimson impact only while the assigned non-hostile route remains open, and if that "
        "route is closed simply to avoid an arrival, the Grudge resistance drains out of the metal at once. "
        "The wearer\u2019s reflexes dull as resentment hardens around the body, the recorded cost of long "
        "carries. Closed-route marks, not impact damage, are its corrosion warning. It is maintained by "
        "reviewing threat, passage, and return rule with Gate Watch; the passage observer unfastens the "
        "collar after incident closure, and cutting it makes a rigid Gate-shaped field."
    ),
    "g-200": (
        "The Gatekeeper\u2019s Charm is a small tail-charm in Gate-red metal, shaped like a latch that never "
        "quite closes. It appears only after Aegis recognizes an arrival and the Gate Watch writes the "
        "response, and it binds to a route officer \u2014 never to a permanent gate owner, a distinction the "
        "Charm enforces by cooling in the hand of anyone who holds a post too long. Consulted at a working "
        "gate, it identifies one missing passage responsibility: an unassigned guard, an unkept return "
        "record, absent arrival support, or unclear closure authority. It points at obligations, never at "
        "people, and it grows heavy the moment it is used to identify a person instead of a duty. The "
        "bearer\u2019s temper shortens whenever they see a route held without accountability \u2014 the Charm\u2019s "
        "recorded cost \u2014 and it burns near a route treated as one-way by habit. It is maintained through "
        "route review, and the Gate Watch partner removes it once the missing duty has been assigned. "
        "Breaking the Charm creates a false passage-denial mark that some gate, somewhere, will honor."
    ),
    "w-219": (
        "Splinter Requiem is a slender deep-blue Han-crystal blade with a wet, luminous edge \u2014 authentic "
        "droplets run from point to hilt and vanish before they reach the hand. The blade sings when drawn, "
        "and the pitch is exact: it is the pitch of the last memory allowed to evaporate beside Splinter. It "
        "forms from a dry residue line after a complete O-Relic channel, and it binds only to a wielder who "
        "can name a grief they have postponed without claiming it is resolved; a bearer who calls "
        "suppression \u201crecovery\u201d finds the grip filling with warm water. In action a thrust carries one "
        "released grief along the wet edge and through up to three targets, cutting at emotional stability "
        "rather than flesh \u2014 though if the channel is held too long the blade can no longer distinguish the "
        "wielder\u2019s tears from Splinter\u2019s. The bearer weeps involuntarily during use, and later tears may "
        "carry memories that belong to the shard rather than to them. It is maintained point-down over a "
        "shallow witness basin outside Splinter\u2019s drip line, and cleared only when its song ends. For "
        "shutdown it is sheathed wet, laid horizontal so runoff can exit both ends."
    ),
    "s-219": (
        "Splinter Shroud is a wrapping suit of deep-blue Han-silk, cool and faintly luminous, in which water "
        "moves visibly between the layers but never drips from the hem. A genuine Shroud shows two faces at "
        "once: the wearer\u2019s current expression on the outer fold and an older grief on the inner one. It "
        "condenses from mist above a memory vision that evaporates with witnesses present, and it binds only "
        "to a wearer who can remain through another person\u2019s grief without turning the account into their "
        "own \u2014 it rejects anyone seeking numbness as the objective. Worn in a Lament surge, the wrapping "
        "lets grief pass between its layers and leave as moisture instead of accumulating in the wearer\u2019s "
        "mind. The cost arrives afterward: minor joys go numb, food keeps its taste but not its pleasure, "
        "and a successful rescue may feel emotionally flat. Dry inner fabric under a wet outer layer is the "
        "first corrosion sign, and a crystal seam over the sternum is the last. It is maintained by "
        "unwrapping every layer over open grating in the Alpha Tree vault, each fold drying at its own rate; "
        "a partner loosens the outermost wet fold for removal."
    ),
    "g-219": (
        "Splinter Pendant is a deep-blue Han-crystal drop worn at the tail slot, cool to the touch until an "
        "emotional attack arrives \u2014 then it fills with a tiny moving scene, a memory image sealed under the "
        "surface. Its weight bears no relation to its size; bearers report it heavy as a held breath on some "
        "days and weightless on others. Splinter bestowed the registered Pendant after a researcher "
        "completed Ferrehan beside an evaporating memory without trying to identify the dead by guesswork; "
        "no extraction procedure can produce one. In function it absorbs one attack against emotional "
        "stability and stores it as the scene it shows: the bearer stays functional through the strike, but "
        "sleep replays the stored moment from the sufferer\u2019s perspective, night after night, until it is "
        "properly released. A second attack taken before release displaces one of the bearer\u2019s own dream "
        "memories. A crystal that dreams while the bearer is awake, or stored figures that begin using the "
        "bearer\u2019s voice, are the corrosion signs. Release is performed over a shallow bowl near Splinter, "
        "the scene draining as warm blue water under both witnesses. It must never be shattered \u2014 the "
        "stored attack would strike every sleeper nearby."
    ),
    "w-220": (
        "The Years Maul is a matte black two-handed maul of Han steel whose striking faces are formed from "
        "calendar leaves \u2014 but each leaf displays consequences rather than days. The shaft lengthens by one "
        "finger-width whenever the weapon records an omitted year, so an old Maul is visibly longer than its "
        "registration entry. It condenses from Weight released after an unabridged archive entry, and "
        "binding requires the wielder to name one institutional harm they benefit from, without pretending "
        "that personal confession completes repair. Before striking, the wielder states the target event and "
        "its surviving consequence; the Maul then sends that Weight through up to three linked structures. A "
        "date without consequence produces no force at all, and an invented date returns the blow through "
        "the bearer\u2019s own joints. The cost is cumulative \u2014 the body grows heavier, ages slightly, and with "
        "repeated use historical time begins to feel more real than the current room. Swinging without a "
        "complete record freezes the head on one repeating year. It is maintained laid across two archive "
        "supports with the last affected file open beneath the head, and the shaft returns to registered "
        "length only when no euphemism remains in the entry."
    ),
    "s-220": (
        "The Years Mantle is a draped black Han-weave garment that smells of dust and wet stone. Its hem "
        "carries tiny date marks that rearrange themselves according to the age of each surface the cloth "
        "touches, and the authentic garment always keeps the current year\u2019s mark nearest the wearer\u2019s "
        "hand. It forms from the shadow of a record-layer that Walking Calendar releases after honest "
        "archival work, and it binds to a wearer who can distinguish responsibility from inherited personal "
        "guilt. Worn under Weight pressure, the cloth separates the pressure into historical layers so that "
        "centuries do not land on the body at once, and the wearer gains the ability to read the age and "
        "repair sequence of any material they touch. The cost follows them out of the archive: every contact "
        "delivers age as sensation, and prolonged wear makes present objects and living people feel like "
        "artifacts already archived. It is maintained by hanging it in the current archive room \u2014 never "
        "deep storage \u2014 and touching each hem mark with an object made this year until the current date "
        "returns to the hand. Removal is by a partner\u2019s three present-tense questions, lifted from the "
        "newest layer outward."
    ),
    "g-220": (
        "The Years Charm is a small black Han-steel calendar weight worn at the head slot \u2014 matte, "
        "disproportionately heavy, and engraved with a single blank square that warms near an omitted date. "
        "Walking Calendar bestowed it after an archivist restored a casualty entry with its consequence and "
        "authorizing office intact; it cannot be scheduled or extracted. In use it points toward a missing "
        "date, an excised consequence, or a chronology that has been made falsely seamless \u2014 and it detects "
        "missing consequence as readily as missing calendar data, holding its bearer motionless beside a "
        "page whose dates are complete but whose footnote names an evacuation without the people denied "
        "passage. It does not determine guilt; it identifies where history has been made falsely light. The "
        "bearer\u2019s movement slows as unresolved omissions accumulate, and blank squares multiplying across "
        "the band are the first corrosion sign. Filling an omission with a convenient explanation cools the "
        "Charm while making it heavier. Care requires comparing the marked interval against original, "
        "edited, and public versions, and the Charm lightens only when uncertainty is recorded rather than "
        "filled. Emergency release is the current date spoken aloud and one defined archival task handed to "
        "another named person."
    ),
    "w-222": (
        "Patina Fang is a fang-curved blade of crimson Han iron \u2014 dark, warm to the touch, and edged with "
        "orange rust flakes that are sharper than polished metal. Drawn, it does not point at the nearest "
        "enemy; it quivers toward the oldest active boundary marker in range, the original site of the "
        "inherited grievance. The Fang forms from rust shed when current representatives of both sides name "
        "the same original loss, and it binds only to a wielder who can state the grievance without naming a "
        "living heir as its rightful target. In action it follows a line of inherited hostility through up "
        "to three markers or structures, cutting the corroded route itself; a living person may be struck "
        "only for present conduct documented independently of ancestry, and Patina pulls the tip downward if "
        "the wielder points at a descendant. Old wounds ache with every draw, and prolonged use paints "
        "bruise-lines matching injuries inherited through family stories the wielder never suffered. It is "
        "maintained set between the two sides of the last crossed boundary, each side stating the same "
        "original loss in its own words, brushing away only the flakes that fall voluntarily. Shutdown is "
        "the point dropped into disputed soil and the grip released."
    ),
    "s-222": (
        "Patina Plate is a crimson Han-iron harness of rust-dark plates that breathe apart under calm "
        "conditions and clamp together near hostility \u2014 the armor\u2019s state is legible across a room. Inside "
        "each plate runs an unassigned border line; names appear along those lines only when the wearer "
        "begins sorting strangers into inherited sides, which makes the interior of the armor its own "
        "warning system. The Plate condenses from Patina\u2019s loosened Weight after Ferrehan, and binding "
        "requires the wearer to name a conflict they inherited and one person they refuse to treat as its "
        "continuation. In the field, directed anger hardens the outer plates into physical resistance \u2014 "
        "hostility tempered into armor \u2014 while Void slips through, because the protection depends on "
        "remembered sides. The cost is intimate: the wearer feels inherited anger toward strangers and "
        "begins mistaking unfamiliarity for allegiance. Plates that stay hard after hostility ends, or "
        "border lines acquiring family names, mean withdrawal. It is maintained opened flat over a current "
        "route map with all family labels removed, two people from different sides identifying present "
        "hazards together. A neutral partner unhooks the plates in the order hostility reached them; forced "
        "front release sends stored anger into the nearest stranger."
    ),
    "g-222": (
        "Patina Charm is a small crimson Han-iron charm worn at the tail, dark and faintly warm, its rust "
        "pattern resembling two boundary lines that never meet. The metal\u2019s behavior is its function in "
        "miniature: it stays cool through a current, documented threat, and heats sharply the moment an old "
        "grievance is assigned to a living stranger by ancestry, district, accent, or inherited role. Patina "
        "granted it after a worker endured Ferrehan while refusing both sides\u2019 demand to identify the "
        "\u201ctrue heirs\u201d of the feud, and it cannot be manufactured. As the audit point of its set, the Charm "
        "distinguishes present hostility from inherited accusation \u2014 it does not decide which history is "
        "correct, only warns when history is being converted into a living person\u2019s essential nature. The "
        "bearer\u2019s temper shortens whenever people ignore the distinction, and persistent heat around all "
        "unfamiliar people is the first corrosion sign. Treating every present grievance as inherited cools "
        "the Charm falsely and leaves current victims unprotected. Care requires recording one present harm "
        "and one inherited accusation from the same incident without collapsing either into the other, the "
        "Charm resting on neutral ground until both boundary lines cool separately."
    ),
    "w-225": (
        "The River Maul is a matte black two-handed maul of Han steel that quivers toward the downstream "
        "route whenever it is lifted. Its head contains no reservoir \u2014 by design, Weight enters one face "
        "and must leave the other \u2014 and an authentic Maul cannot be aimed directly upstream without "
        "rotating in the bearer\u2019s hands. It is shaped only from residue already condensed at the sealed "
        "monitoring sluice, and binding requires a declared discharge path; no bearer may carry it beyond "
        "the mapped return network. In use it drives burden through up to three targets or structures along "
        "the declared flow, attacking Han reserves and karmic load, and the outlet rule is absolute: a "
        "strike without an open outlet stores the entire line inside the wielder. Each use increases bodily "
        "heaviness, and prolonged operation produces slight aging proportional to the burden redirected \u2014 "
        "the first bearer\u2019s hair carries a permanent gray band matching the waterline. Obstructed outlets "
        "send the hit back through the bearer, and striking to collect Han roots the handle into the sluice "
        "floor. It is maintained resting across the open return trench until both faces reach the same "
        "temperature. Shutdown is the grip released while the head faces downstream."
    ),
    "s-225": (
        "The River Mantle is a breathing drape of matte black Han-weave whose hem flows downstream even in "
        "still air \u2014 the cloth always knows the direction of the current. Its inner surface feels like "
        "stone worn smooth by water, and it condenses from vapor above an authorized sluice return; no "
        "thread of it crosses the sealed River boundary. It binds to a wearer who accepts that the task is "
        "passage, not containment, and it rejects any deployment plan that promises to halt Black River. "
        "Worn in moving Weight, the cloth divides the current around the wearer and rejoins it behind them \u2014 "
        "banked passage, not a dam \u2014 and the effect gives no protection if both sides are sealed. The cost "
        "settles in the legs: constant low fatigue that becomes undertow, and rest does not help until all "
        "received burden has passed downstream. Bracing in place makes the cloth rigid and raises local "
        "pressure. It is maintained spread along \u2014 never across \u2014 the return trench until the fabric lifts "
        "downstream at every point. Removal is walking with the flow until the collar loosens; pulling it "
        "off facing upstream transfers the current into the chest."
    ),
    "g-225": (
        "The River Stone is a smooth black Han-steel stone fixed at the head slot. It begins lead-cold and "
        "gains mass without changing size, and its surface holds no reflection at all; a genuine Stone "
        "points its heaviest side toward the sluice return, wherever the bearer stands. It appeared after a "
        "Ferrehan observer completed rotation without attempting direct River contact, and it cannot be "
        "manufactured, requested, or emptied into storage. In function it absorbs sorrow from the immediate "
        "environment \u2014 enough to clear a monitoring room for evacuation \u2014 and every absorbed burden "
        "increases the bearer\u2019s physical and emotional weight, until the Stone pins the head toward the "
        "return trench and demands discharge. Neck strain appears before the Stone feels heavy to the hand, "
        "which is the first corrosion sign; a bearer describing other people\u2019s grief as inventory is the "
        "second. Enclosing the Stone preserves burden and creates a local undertow, and emptying it outside "
        "the sluice seeds a new Weight pool. Release seats the bearer above the return trench, heavy face "
        "downstream, one monitoring gate opened at a time until the Stone cools \u2014 and no one may measure "
        "the released burden as production yield. Shattering it produces a room-wide heavy wave."
    ),
    "w-230": (
        "The Final Lens is a lens-ground disc of nearly colorless Han-glass mounted on a long pale frame, "
        "held like a staff-mounted sight rather than a blade. The disc pulses faintly \u2014 in time with the "
        "last heartbeat it observed \u2014 and goes fully transparent at the exact boundary after a final image "
        "ends. It forms from residue left when a final moment is recorded without alteration, and it binds "
        "only to a wielder who can repeat the difference between ending a harmful Void effect and deleting "
        "the memory that carries it. Once a final frame completes, the Lens focuses the Void immediately "
        "following it through up to three targets, attacking Soul continuity in the blank after the ending; "
        "firing early pierces the memory itself and removes evidence from every witness. Each shot takes a "
        "small unnamed memory from the wielder while leaving indexed facts intact. It is maintained placed "
        "between two sealed witness accounts, cleared only when it shows a transparent interval after both "
        "accounts rather than when one version wins. Shutdown is the frame rotated away from all faces until "
        "its borrowed heartbeat stops; breaking it releases every retained Blank After."
    ),
    "s-230": (
        "The Final Veil is a flowing suit of pale Han-gossamer that shifts like breath after breathing has "
        "stopped. Thousands of indistinct faces cross its outer cloth \u2014 the final moments it has received \u2014 "
        "while the inner surface shows only one thing: the wearer\u2019s own living pulse, kept visible like a "
        "lamp in a corridor. It condenses from a final memory\u2019s receding edge, and it binds when the wearer "
        "names one unfinished living obligation and appoints a partner to confirm it after exposure. In the "
        "field it separates that ongoing pulse from incoming final moments, letting Void pass over the outer "
        "faces without ending the wearer\u2019s personal continuity. The cost is a haunting one \u2014 the wearer "
        "becomes faintly absent and may feel already dead, remembered, and no longer responsible for present "
        "choice. A wearer speaking of current events in past tense is the first warning, one ending adhering "
        "to the inner surface the second. It is maintained hung beside an active clock and "
        "an open task, cleared only when the inner pulse resumes before the outer faces. The partner states "
        "the obligation and waits for a present-tense answer before removal."
    ),
    "g-230": (
        "The Final Hour is a pale Han-glass hour-token worn at the head slot, with no hands and no numerals "
        "\u2014 an empty watch face for a measurement no ordinary clock makes. Near imminent death a thin white "
        "line circles the rim and stops at the instant immediately before the selected target\u2019s ending. "
        "Every Last Goodbye bestowed it after a worker witnessed a peaceful final moment without asking the "
        "entity to change or deliver it, and the current token is unassigned, because every full stop also "
        "shows the bearer their own final moment. The image is not a guaranteed prophecy: intervention can "
        "alter the route, but the Gift does not explain which detail is causal \u2014 in its one supervised "
        "trial, a replaced vault latch un-made two deaths at once. The rim line appearing around healthy "
        "strangers without selection is the first corrosion sign; a bearer planning life around avoiding one "
        "image is the second, and treating the vision as certain narrows choices until it self-fulfills. "
        "Care records the image as sensory data, lists at least three unknowns, and makes one proportionate "
        "safety change without declaring the death prevented. Shattering the token projects every possible "
        "ending stored during the session."
    ),
    "w-233": (
        "The Soul Requiem is a deep-blue Han-crystal blade that sings in a voice no listener can remember "
        "after the note ends \u2014 witnesses agree it sang, and cannot say how. A thin film of warm Lament "
        "beads along the edge whenever an erased record blocks the bearer\u2019s route, the blade weeping at "
        "administrative denial the way other steel rusts at rain. It forms from tears left outside the "
        "Soul\u2019s walking line after two witnesses finish Ferrehan without proposing a name, and it binds "
        "only to a wielder willing to protect an unknown person without converting protection into "
        "ownership. A thrust carries Lament through up to three barriers that deny an observed person\u2019s "
        "presence \u2014 archive seals, closed stairs, doors that no longer recognize a person-shaped figure; "
        "against a living target, authorization requires present conduct, because missing records are not "
        "hostility. The wielder feels the Soul\u2019s unwept grief, weeps involuntarily with extended use, and "
        "may lose certainty about which remembered sorrow is personal. It is maintained "
        "laid parallel to the Soul\u2019s route after it has passed, two witnesses reading only observed "
        "incident facts, the edge left to weep until no letters remain in the liquid. Shutdown is the point "
        "lowered, the path opened, the naming stopped."
    ),
    "s-233": (
        "The Soul Shroud is a wrapping suit of cool deep-blue Han-silk that smells faintly of rain. Its "
        "folds never retain a face \u2014 by nature, not by cleaning \u2014 and what they preserve instead is a "
        "distance: the measured space between the wearer and the person being accompanied. It condenses from "
        "route mist after an honest Ferrehan walk, and its binding words are fixed: the wearer must say "
        "\u201cI do not remember you, and I will remain,\u201d adding no name and no promise of recovery. Worn "
        "beside the fading figure, the cloth distributes Lament across that measured space so the wearer "
        "accompanies grief rather than absorbing it; falling behind or trying to lead collapses the "
        "protection entirely. The cost is joy \u2014 minor pleasures go numb, and prolonged wear makes "
        "accompaniment feel like the only morally permitted life. A lead fold means the wearer has stepped "
        "ahead and begun inventing a destination; a trailing seal means grief has become an object of study. "
        "It is maintained by walking the empty route once at ordinary pace with a living partner, speaking "
        "no source theory. The partner walks level and loosens the side fold for removal; pulling from ahead "
        "or behind tears the measured distance."
    ),
    "g-233": (
        "The Soul Thread is a cool deep-blue Han-crystal thread worn at the tail slot, fine as a hair and "
        "colder than the room. It links the bearer to a fading person as a pulse \u2014 presence reduced to its "
        "honest minimum, with no name, no face, no biography attached \u2014 and false information physically "
        "deforms it: every unsupported detail hardens into a knot along the line. The Soul granted it after "
        "two workers completed an accompanied route while openly admitting they did not remember it; no "
        "procedure can manufacture one. In function the Thread keeps one fading identity connected to living "
        "witnesses \u2014 when every observer forgot the Soul on looking away, the Thread went on pulsing, "
        "letting its bearer say \u201csomeone remains behind us\u201d without supplying a person. The cost enters at "
        "night: the bearer hears that person\u2019s grief during sleep. Knots forming around plausible but "
        "unsupported details are the first corrosion sign, and dream-weeping before sleep the second. Care "
        "is comparative: two note-takers strike every unsupported statement and leave the missing fields "
        "visible, and the Thread unkinks only when \u201cunknown\u201d is accepted as a valid record. Cutting it "
        "abandons both ends to the same erasure."
    ),
    "w-235": (
        "The Watcher\u2019s Lens is a short-handled disc of almost colorless Han-glass. One side shows the "
        "observed scene; the other remains blank until a responder accepts responsibility for acting on it \u2014 "
        "a weapon whose firing condition is printed in its own glass. It forms from an eye that closes after "
        "intervention, and binding requires the wielder to name what action they can perform and what "
        "exceeds their authority; a person who only intends to document sees no target at all. In use the "
        "Lens attacks one documented present danger \u2014 a support crack ignored in seven reports, a hazard "
        "hidden under Void \u2014 and it cannot target a person merely because surveillance marked them. Delay "
        "after designation drains the wielder\u2019s nameless memories without producing a shot. An observed "
        "victim becoming the target instead of the danger is the listed failure, and repeated aiming without "
        "action erases the wielder\u2019s reason for caring. It is maintained pressed against the repaired site \u2014 not the report archive \u2014 and the "
        "blank side clears only after real-world verification. Shutdown transfers responsibility aloud to a "
        "named qualified person."
    ),
    "s-235": (
        "The Watcher\u2019s Veil is a pale Han-gossamer suit patterned with open eyes on the outside and a "
        "single human outline within \u2014 the surveillance state rendered as clothing, with the person "
        "preserved at its center. It condenses after a watcher-route intervention, and the binding term is "
        "plain: the wearer accepts being identifiable while retaining the right to act rather than perform "
        "for the gaze. Worn through a watched corridor, the Veil holds the observations on the outer cloth \u2014 "
        "the whispered private fears, the running commentary of the eyes \u2014 long enough for the wearer to "
        "reach the person who needs them. Protection lasts exactly as long as the declared intervention "
        "does; a wearer who stops to manage their appearance finds the outer eyes turning inward. The cost "
        "is a faint absence, and a subtler risk: confusing continuous observation with continuous consent. "
        "It is maintained hung in a room with no recording devices while the wearer speaks one fact they "
        "choose not to disclose operationally; the eyes close only when privacy is respected. The person "
        "helped \u2014 or an assigned partner \u2014 removes it by addressing the wearer by name rather than role."
    ),
    "g-235": (
        "The Watcher\u2019s Lens gift is a pale Han-glass lens-pendant fixed at the head slot, small enough to "
        "sit unnoticed at the hairline. Touched to a wall, it reveals what that structure witnessed from its "
        "own position \u2014 twelve shifts of a corridor, one alcove\u2019s unblinking record of a citizen "
        "collapsing while people passed. The price is symmetrical with the power: the bearer cannot later "
        "forget the scene, even if the wall\u2019s record is sealed. Panopticon granted it after an observer "
        "acknowledged the gaze and acted on a recorded hazard; no extraction procedure produces it. The Gift "
        "supplies evidence, never verdicts \u2014 a wall\u2019s field of view is not the whole event, and mistaking "
        "perspective for truth is its listed failure. Old scenes intruding over present walls is the first "
        "corrosion sign; a bearer seeking private scenes unrelated to intervention is the last and worst. "
        "Care requires recording exactly where the structure could and could not see, with another witness "
        "identifying the blind areas, and the Lens rests against an unwitnessing surface until the current "
        "room becomes primary again. Emergency release covers the bearer\u2019s sight \u2014 not the Gift \u2014 with "
        "neutral cloth; shattering the lens projects the permanent scene to everyone nearby."
    ),
    "w-236": (
        "The Seedless Requiem is a short singing blade of faint blue Han-crystal whose central groove is "
        "seed-shaped \u2014 and empty. The emptiness is the point: the weapon guards beginnings, not outcomes, "
        "and the groove darkens the moment its bearer supplies a final form for the thing being protected. "
        "It forms from rain residue outside Unwitnessed\u2019s marked boundary, and binding requires the wielder "
        "to name a beginning they will defend while leaving its outcome undescribed. In action it strikes "
        "one immediate threat to a fragile beginning \u2014 a husk surge against a new water-marker, a present "
        "danger to a first attempt \u2014 and it will not attack uncertainty, delay, or failure merely because "
        "the bearer fears them. The cost is anticipatory grief: the wielder feels Unwitnessed\u2019s sorrow and "
        "weeps for futures the protected beginning may never reach. Attacking a possible outcome damages the "
        "beginning itself, and collecting phantom forms fills the blade with unusable husks; suppressed "
        "grief jams the groove outright. It is maintained washed with ordinary rain outside the no-plant "
        "ring, recording only what the protected beginning is now, and the groove clears when no future "
        "image remains in it. Shutdown lowers the edge and strikes every projected outcome from the mission "
        "order."
    ),
    "s-236": (
        "The Seedless Shroud is a cool blue wrapping of Han-silk patterned with roots that end before "
        "reaching a center \u2014 growth interrupted, woven honestly into cloth. It condenses from mist over "
        "Unwitnessed\u2019s boundary after Ferrehan, and it binds only to a wearer prepared to guard potential "
        "without claiming ownership of it. Worn during an expansion event, the fabric becomes a moving "
        "screen: phantom trees, flowers, and crops drift across the outer weave \u2014 every future the ground "
        "never grew \u2014 while the actual survey markers stay visible through it, and none of the imagined "
        "forms take root in the wearer\u2019s mind. The cost follows the protection: minor joys go numb, and the "
        "deeper risk is a wearer who begins valuing hypothetical futures over present life. Fabric reaching toward a beginning the wearer "
        "treats as theirs is the first corrosion sign, and every present pleasure postponed for a possible "
        "later life is the last. It is maintained spread over barren ground away from the source site, one "
        "ordinary current object placed at its center and described without metaphor \u2014 the root pattern "
        "must stop short of it. Removal rolls the cloth inward from the unrealized edges while a partner "
        "keeps the present object visible."
    ),
    "g-236": (
        "The Seedless Pod is a hollow pod of blue Han-crystal worn at the tail slot, and its hollowness is "
        "exact \u2014 it contains no seed, and never will. When it is assigned to a fragile beginning, one dim "
        "point of light appears inside the crystal, a glow that shows that something has started without "
        "ever showing its final form. Unwitnessed bestowed it after a worker marked the absence and waited "
        "through Ferrehan without planting; manufacturing is impossible. In function it preserves one "
        "fragile beginning outside the source boundary \u2014 in its recorded trial, the first line of a "
        "survivor\u2019s account stayed legible through a Han-storm while imagined complete narratives appeared "
        "and vanished around it. The cost is constant "
        "and quiet: the bearer feels every future that did not start. The point of light dividing into "
        "competing futures is the first corrosion sign, and a Pod that treats completion as death and "
        "refuses release is the last. Naming the final form makes the Gift preserve a plan instead of a "
        "beginning, and it goes dark if anyone declares its protected outcome mandatory. Care returns it to "
        "a neutral site until the protected person or project makes one unpredicted choice."
    ),
})

OVERRIDES.update({
    # ---- batch 8 (compact/prose-format records; all paragraphs source-led) ----
    "w-240": (
        "The Ruin Fang is a dark crimson fang of Han iron whose wet edge does something no other blade "
        "does: raised inside a memorial footprint, it outlines absent masonry \u2014 the ghost-lines of walls, "
        "stairs, and banisters that no longer exist \u2014 in a thin red tracing along its edge. It forms from "
        "the overlap between two corroborated survivor maps, and it binds only to a wielder who can "
        "distinguish surviving evidence from reconstruction. In use the blade attacks one present "
        "obstruction crossing a corroborated lost boundary \u2014 a modern brace blocking a phantom evacuation "
        "route \u2014 and it cannot strike the absence itself; unsupported geometry makes the edge cut the "
        "wielder\u2019s own remembered space instead. The cost is written on the body: the first bearer\u2019s old "
        "shoulder wound bruised in the exact shape of a tenement\u2019s missing banister. Imagined detail "
        "hardening into a replica edge is the first corrosion sign. It is maintained with independent room "
        "sketches laid on opposite sides of the blade, cleaning only the edge where both show the same "
        "boundary and leaving disputed sections wet and unusable. Shutdown steps outside the memorial "
        "footprint and lowers the Fang before the phantom room fades."
    ),
    "s-240": (
        "The Ruin Plate is a crimson Han-iron harness that carries the scent of dead timber and plaster "
        "dust, its plates shaped like mismatched fragments from rooms that no longer exist \u2014 no two pieces "
        "matching, because no two surviving memories of the fallen building match either. It condenses "
        "after a stable memorialization cycle, and it binds to a wearer who will absorb shock without "
        "claiming the armor restores what fell. In the field the harness absorbs one sequence of structural "
        "shock and delays it until personnel clear the footprint \u2014 a collapse held in suspension long "
        "enough for evacuation. The cost comes due afterward: the wearer experiences the stored collapse "
        "through their own body, including phantom impact from walls that vanished years ago. Grudge "
        "hardens the plates, Void bypasses the absent joints, and Weight overloads the remembered "
        "foundation. Delayed impacts releasing before evacuation ends is the listed failure, and a wearer "
        "who steps inside the footprint turns the armor into a substitute wall. It is maintained by "
        "releasing stored shock into a test frame built outside the memorial boundary, comparing each "
        "impact to corroborated collapse records. Removal is flat on the ground outside the footprint, a "
        "partner releasing the plates in reverse collapse order."
    ),
    "g-240": (
        "The Ruin Charm is a warm crimson tail-charm of Han iron shaped like a broken door hinge \u2014 an "
        "opening that no longer opens anything, carried at the belt. Near Holdout it points toward one "
        "boundary that appears in at least two independent memories, and it remains completely inert around "
        "a single polished reconstruction; corroboration, not confidence, is its fuel. It appeared after "
        "former residents named the same stair landing without consulting the Council plan, and fabrication "
        "has never succeeded. In use it marks one corroborated absent doorway, wall edge, or structural "
        "load line \u2014 in its recorded case, an exterior doorway omitted from the stabilization report, "
        "whose route led nowhere physically but explained why survivor accounts placed the evacuation "
        "toward a wall. The bearer\u2019s temper shortens whenever destruction is justified without mourning, "
        "and heat rising at the word \u201cnecessary\u201d is the first corrosion sign. Official drawings overriding "
        "lived memory is the listed capture failure. It is maintained placed between two independent "
        "sketches with agreement, conflict, and absence marked in different inks \u2014 it cools only while the "
        "conflict stays visible. Emergency release leaves the disputed room unmarked; forced certainty "
        "triggers ghost collapse."
    ),
    "w-245": (
        "The Wall Requiem is a short deep-blue blade of Han crystal whose edge hums only after an "
        "interrupted phrase \u2014 silence, then the exact pitch of a song that stopped mid-line. It forms from "
        "resonance fallen at the break point of the Midnight Choir\u2019s frescoes; no pigment is ever removed. "
        "Binding is a discipline of the voice: the wielder must repeat the last confirmed lyric and then "
        "keep silence where the verse was lost. In use the Requiem attacks one harmful note continuing "
        "beyond a documented interruption \u2014 surplus resonance spreading as bone-rattling vibration past "
        "the final known word \u2014 and striking an original phrase damages the historical voice instead. The "
        "cost is grief on someone else\u2019s meter: unwept sorrow enters the wielder and produces involuntary "
        "tears paced to the unfinished song. Invented notes becoming false targets is the first corrosion "
        "sign, and force used against the wall itself deletes the audible record. It is maintained held "
        "near \u2014 never against \u2014 the originating fresco at midnight, no recording played, the blade left "
        "to hum the confirmed phrase and stop by itself. Shutdown sheathes it at the break point and keeps "
        "the missing line silent."
    ),
    "s-245": (
        "The Wall Shroud is a wrapping shroud of blue Han-silk that carries faint painted mouths along its "
        "outer fold \u2014 they breathe in time with nearby frescoes but never supply the missing lyric, a "
        "restraint woven into the fabric itself. It condenses from midnight resonance after a complete "
        "Ferrehan watch, and it binds to a wearer who can listen without treating endurance as proof of "
        "understanding. Worn through a long chorus, the cloth distributes resonant Lament across its "
        "painted mouths, preserving the wearer\u2019s breathing and clarity while the walls sing. The cost is "
        "specific and cruel to music-lovers: minor joys go numb, especially pleasure in familiar music \u2014 "
        "the first wearer lost it for two days. A wearer whose breath joins the chorus and cannot stop at "
        "the break is the first failure; a cloth that supplies a comforting ending the source never sang is "
        "the worst. Covering a fresco with the suit counts as silencing and is prohibited. It is maintained "
        "hung in open air at noon, when the walls are quiet, while the wearer listens to one complete "
        "living song chosen by its singer. Removal unwraps during the natural silence after the confirmed "
        "phrase; removing it mid-note transfers the chorus into the chest."
    ),
    "g-245": (
        "The Wall Stone is a small deep-blue tail-stone of Han crystal that vibrates with one confirmed "
        "fragment of an unfinished song \u2014 and becomes silent exactly where the fresco does, refusing on "
        "principle to hum a single note further. The Midnight Choir bestowed it after a listener catalogued "
        "a lullaby without composing its goodnight; no R.D. process can manufacture one. In use it calms "
        "nearby people through the remembered fragment: during a shelter panic it steadied breathing "
        "without promising safety or resolution, and at its missing final line the responders supplied "
        "instructions rather than pretending the song had ended. The cost follows the bearer home \u2014 "
        "unfinished songs become audible whenever they are near walls. Every wall returning the same "
        "fragment is the first corrosion sign; a bearer who cannot tolerate silence after the break point "
        "is the second; and using the song to pacify people whose danger remains active is the listed "
        "misuse. A bearer who completes the phrase overwrites its source. Care is recitation at the "
        "originating wall \u2014 provenance, confirmed words, and the exact interruption \u2014 and the Stone must "
        "stop where the record stops. It is never smashed; every nearby surface would inherit the loop."
    ),
    "w-247": (
        "The Unopened Bloom Sword is a narrow crimson sword of Han iron whose flat resembles an unopened "
        "petal and whose edge follows one permanent split \u2014 the weapon is itself a sealed flower with a "
        "single wound. It forms from residue shed when the Bloom closes around grief without being touched, "
        "and its binding is a renunciation: the wielder identifies someone they love and accepts a "
        "no-contact order, because heat along the edge makes affectionate touch harmful. The weapon\u2019s two "
        "faces do opposite work: the flat heals one minor current wound, while the "
        "edge deals Grudge pressure \u2014 and healing the source tear, a memorial scar, or a wound the bearer "
        "needs hidden makes the blade cut instead. The crueler inversion is the cost: the wielder\u2019s touch "
        "harms loved ones until the weapon is discharged and cleared. Cosmetic cure deepening the "
        "hidden wound is the listed failure, and cutting source petals roots the Sword into the hand. It is "
        "maintained laid beside \u2014 not on \u2014 the damaged memorial, the healed person verifying what was "
        "treated and a witness naming what remains torn; the flat cools before the edge. Shutdown places it "
        "beyond arm\u2019s reach of loved ones, both hands open."
    ),
    "s-247": (
        "The Unopened Bloom Plate is a dark crimson harness of Han iron arranged like overlapping split "
        "petals, and it smells permanently of char and crushed flowers. Each plate carries the pattern of "
        "the Bloom\u2019s tear, and polishing that pattern away causes outright rejection \u2014 the armor insists "
        "on its own damage being visible. It condenses after a no-touch Ferrehan cycle and binds to a "
        "wearer who records damage before attempting repair. In the field the plates harden against "
        "aggression reaching the torn form, holding a Crimson field long enough to clear civilians \u2014 but "
        "protection drops the moment the wearer conceals, replaces, or handles the original damage. The "
        "cost accumulates around good intentions: reflexes dull as resentment armor thickens, worst around "
        "repair tools, and the first wearer froze every time she reached toward the Bloom itself. New "
        "memorial material fusing to the armor is the replacement-shell failure, and erased provenance "
        "passes through the weak seams as Void rot. It is maintained by opening each petal plate and "
        "documenting every new scratch separately from the source tear, removing only loose residue. "
        "Removal requires a witness standing between wearer and memorial while the harness opens from the "
        "outermost undamaged plate."
    ),
    "g-247": (
        "The Unopened Bloom Charm is a warm crimson tail-charm of Han iron shaped like one split petal \u2014 a "
        "single fragment of the flower, carried without ever having been picked. It glows at the original "
        "wound and changes color around later damage, concealment, or attempted replacement, making it a "
        "chronology worn at the belt: first harm, second harm, cover-up, each in its own light. The Bloom "
        "granted it after a worker remained beside the torn form without picking a fallen petal; it cannot "
        "be manufactured. Its registered use is exact \u2014 it distinguishes the original memorial tear from "
        "subsequent harm or repair, and in its recorded case it stopped a maintenance team from sealing the "
        "source split with clear resin, marking the resin as a second event rather than healing. The "
        "bearer\u2019s temper shortens when damage is made cosmetically invisible. Every imperfection glowing "
        "as original harm is the purity error; chronology becoming accusation is the blame flare; and an "
        "attractive repair cooling the Gift while erasing provenance is the worst failure. Care compares it "
        "against first-contact sketches and later maintenance logs, naming original tear, later harm, and "
        "protective work separately. Pulling it free during a repair transfers the split to the bearer\u2019s "
        "skin."
    ),
    "w-249": (
        "The Warning Fang is a fang-curved blade of crimson Han iron that vibrates with interrupted "
        "syllables \u2014 pieces of a message that never finished arriving. It forms from the overlap of two "
        "independent dream reports, and the honesty of that origin is visible on the weapon: where the "
        "reports fall silent, blank gaps remain along the edge, unpolished and unfilled. Binding requires "
        "the wielder to state one confirmed danger vector and one unknown, in the same breath. In use the "
        "Fang pierces up to three interference layers along a verified direction, cutting a path through "
        "red static toward rising pressure without naming what the storm is \u2014 and supplying a missing "
        "target from fear makes the line follow the guess instead of the evidence. The cost is carried in "
        "old injuries: they ache with use, and prolonged operation leaves bruising shaped like broken "
        "signal marks. Inference becoming target is the prophecy-strike failure, and a weapon that repeats "
        "a resolved warning attacks the responder. It is maintained with separate fragment transcripts laid "
        "along opposite edges, cleaning only the matching sounds and leaving the gaps visible. Shutdown "
        "lowers the Fang when confirmed danger ends \u2014 even if the sentence remains incomplete."
    ),
    "s-249": (
        "The Warning Plate is a crimson harness of Han iron whose plates flicker between two images: a "
        "sleeping body and a red-static silhouette, the listener and the interference, never quite settling "
        "on either. It forms after a dream fragment is captured without reconstruction, and it binds only "
        "with an external waking recorder assigned before wear. In the field the harness maintains physical "
        "continuity while Grudge tears dream-space apart \u2014 the wearer\u2019s body stays whole while the dream "
        "floor collapses \u2014 but the protection preserves neither interpretation nor response speed. The "
        "cost is in the joints: reflexes dull as if resentment has armored every one of them, so severely "
        "that the first wearer\u2019s recorder, not she, initiated the evacuation. A threat understood before "
        "the muscles can respond is the delayed-body failure; a guessed message locking one limb is the "
        "static joint; and a recorder\u2019s interpretation replacing the dreamer\u2019s fragment is the "
        "substitution the set forbids. Worn without a waking recorder, it traps the wearer in recursive "
        "warning. It is maintained with the wearer awake while each plate is tapped in fragment order \u2014 "
        "unknown intervals receive silence, not filler tones. The recorder states current location and "
        "confirmed danger before releasing the slowest joint last."
    ),
    "g-249": (
        "The Warning Thread is a warm crimson thread of Han iron worn at the tail, carrying one pulse of "
        "sound through static \u2014 and by nature it never holds a complete sentence. The source granted it "
        "after a dreamer preserved a danger-direction fragment and openly marked the absent words; it "
        "cannot be manufactured. Its function is transmission without embroidery: it preserves one verified "
        "warning fragment through interference, and in its recorded case it carried \u201ceast\u2014ground\u2014\u201d from "
        "a dreamer to an awake patrol, who avoided an eastern subsidence zone without inventing what the "
        "missing words described. The Thread goes physically rigid around speculative words \u2014 guessing "
        "stiffens it like wire. The cost arrives as sound: the bearer hears every warning that arrived too "
        "late, replaying over current safe conditions. A fragment growing fluent despite no new evidence is "
        "the sentence-growth failure, alarm fatigue makes current warnings inaudible, and a bearer treating "
        "a fragment as inevitable future has tied the prophecy knot. Care plays the raw fragment once and "
        "records signal, noise, and silence separately; the Thread clears when it returns only the original "
        "pulse. Emergency release transmits the fragment exactly once to a named responder, then lets the "
        "Thread fall silent."
    ),
    "w-250": (
        "The Memory Requiem is a short singing blade of deep-blue Han crystal with a single clear raindrop "
        "suspended above the guard \u2014 a drop that never falls, the weapon\u2019s origin carried as ornament. It "
        "forms from a catalogued drop that crystallized without entering a collector, and it binds only "
        "when the wielder holds two current identity anchors. Its work is surgical: the blade targets one "
        "invasive memory attached to a person and severs the false ownership bond \u2014 in its recorded case, "
        "separating an unknown wedding from a patrol agent who had begun answering to the groom\u2019s name \u2014 "
        "and aimed at the person\u2019s own memory it damages Mind stability instead. The wielder pays in "
        "someone else\u2019s tears: they experience the fragment\u2019s unwept grief and cry involuntarily, weeping "
        "through vows they never heard. A true personal memory misclassified as foreign is the self-cut "
        "failure, and a wielder who keeps the severed memory loses one identity anchor. It is maintained "
        "suspended beneath an empty Umbrella, reading the crystal\u2019s catalog number \u2014 never its story \u2014 "
        "until the drop above the guard turns clear without dissolving. Shutdown sheathes after one "
        "separation and rechecks both identity anchors before reuse."
    ),
    "s-250": (
        "The Memory Umbrella is a wearable canopy of blue Han-silk with clear channels running from rim to "
        "sealed processing pockets \u2014 rain equipment for a rain no forecast covers. It condenses from mist "
        "around successfully catalogued drops, and it binds to a wearer who carries two identity anchors "
        "and accepts post-use processing duty, because the canopy\u2019s protection is a debt: memory droplets "
        "enter the labeled channels instead of the wearer\u2019s mind, but the Umbrella does not destroy or "
        "anonymize what it catches. Every stored memory must later be processed \u2014 the first wearer crossed "
        "a heavy garden fall and spent three shifts cataloguing the thirty-two stranger memories that "
        "remained above her. Saturation exposes the wearer to all of them simultaneously. Drops losing "
        "provenance when compartments merge is the mixed-channel failure, and Void drying leaves memories "
        "as facts without emotional identity. Closing the canopy before processing turns it into a memory "
        "reservoir, which is why folding a loaded Umbrella is prohibited outright. It is maintained by "
        "opening each channel over a separate Archive tray, a recorder logging sensory content and "
        "uncertainty before the next pocket is released. The canopy stays open until every drop is "
        "transferred."
    ),
    "g-250": (
        "The Memory Charm is a warm blue tail-charm of Han crystal holding one written self-fact that is "
        "visible only to the bearer \u2014 a private line of identity sealed in stone. Memory Rain granted it "
        "after a worker completed Ferrehan beneath a heavy fall without claiming any stranger\u2019s life; it "
        "cannot be manufactured. Its function activates in the worst moment: during memory saturation it "
        "restores one chosen personal identity anchor, returning the bearer to themselves when the rain "
        "supplies a convincing alternate childhood. The recorded case chose well \u2014 the anchor was a "
        "private disagreement, an unrecorded fact no rain could counterfeit. The cost is nocturnal: the "
        "bearer weeps in sleep as unprocessed fragments pass nearby. An anchor becoming a slogan rather "
        "than a lived fact is the rigid-self failure; a stranger\u2019s fact selected and reinforced is the "
        "borrowed anchor; and sleep-tears containing fragments from the Umbrella mark a dream leak. Care "
        "requires the bearer to restate the anchor in current language and name one way they have changed "
        "since choosing it \u2014 continuity without frozen biography. Emergency release moves beyond rainfall, "
        "speaks the anchor once, and transfers all collected drops before sleep."
    ),
    "w-252": (
        "The Unknown Extraction Lens is a pale disc of Han glass held in a long black frame, and its "
        "surface stays blank until a Gate whisper enters the room \u2014 then it fractures the fragment into "
        "center, inner, and outer dissipation zones, a target diagram for what must not be read. The unit "
        "predates current extraction rules. Binding requires the wielder to stand with their back "
        "to the Gate and name the sealed field receiving the discharge. In use it converts one quarantined "
        "whisper fragment into a controlled long-area Void burst aimed away from all persons and the "
        "threshold; it does not reveal, preserve, or validate content \u2014 dissipation is the entire "
        "function. The cost is subtraction: small nameless memories disappear with each discharge, and the "
        "only modern test cost its wielder the memory of why one childhood word had mattered. Aiming at the "
        "Gate creates a false hinge in space, and decoding the burst traps the truth in the "
        "wielder. Maintenance stores it face-down in a sealed dissipation room for thirteen silent "
        "seconds, verified image-free before the case closes. Shutdown rotates the frame away from the "
        "threshold and grounds it in the empty field; an active disc is never covered by hand."
    ),
    "s-252": (
        "The Unknown Extraction Veil is a near-colorless suit of Han gossamer with thirteen pale seams "
        "running from collar to floor \u2014 and the seams are a clock: one darkens for each second of an "
        "active whisper, counting down the only protection the garment offers. The same prohibited "
        "historical event produced it. Binding requires an external timekeeper and a pre-contact "
        "identity statement spoken aloud. Worn in contact, each seam takes one second of identity pressure; "
        "at the final seam, protection ends regardless of content or listener readiness \u2014 the fourteenth "
        "second delivers all stored Void into the wearer. The cost begins earlier: the wearer feels faintly "
        "absent, and may treat the whispered truth as more real than the self hearing it \u2014 at second "
        "eleven of its one test, the wearer experienced her own name as information about an absent "
        "person. Inner heat turning the garment toward the Gate is the warm-side pull; the Veil must never "
        "touch the threshold line. Maintenance counts every seam under neutral light while "
        "a partner repeats the identity statement; any seam that stays dark seals the unit from reuse. The "
        "timekeeper lifts the collar immediately after second thirteen \u2014 the wearer never removes it "
        "alone."
    ),
    "g-252": (
        "The Unknown Extraction Charm is a pale neck-charm of Han glass with thirteen blank notches cut "
        "into its rim \u2014 a counting device for a window no one should hold open. The sole registered Gift "
        "appeared after an undocumented pre-rule whisper event, and the Gate has never bestowed another; "
        "current contact is forbidden outright. Its function is termination: it counts and closes one "
        "thirteen-second whisper window, a cutoff and never a decoder. The cost is lexical \u2014 the bearer "
        "intermittently forgets an ordinary word, and the loss is not random: in the recorded residue test "
        "the Charm removed access to the word \u201chinge\u201d at second thirteen, and that missing word prevented "
        "a spontaneous opening metaphor from becoming an O-Relic command. Forgotten words clustering around "
        "doors, locks, and permission is the first corrosion sign; notches filling before contact begins is "
        "the second; and a bearer who mistakes word loss for buried truth is already failing. A missing "
        "word treated as an opening command is the lexical-key error. Care records lost words as absences "
        "without interpreting them, and the Charm stays isolated until all thirteen notches are blank. "
        "Breaking it releases every forgotten word into the Gate chamber."
    ),
    "w-255": (
        "The Architect\u2019s Maul is a black two-handed maul of Han steel whose striking faces display "
        "incomplete plan sections \u2014 walls that stop mid-line, stairs that reach no landing, drawn in the "
        "metal itself. It forms from blueprint residue after purpose is documented without construction, "
        "and its binding is an act of restraint: the wielder states who the structure was intended to serve "
        "and why finishing it now may repeat the loss. In use it sends Weight through up to three connected "
        "structural targets matching the plan\u2019s present load path \u2014 striking the fracture that exists, "
        "along the line that was intended \u2014 and it cannot create the missing element or make unoccupied "
        "design safe. The cost is age: the wielder grows heavier and older with prolonged operation, the "
        "first bearer\u2019s arms aging visibly through the third blow. A completion strike materializes the "
        "absent element hollow and unstable, and a bearer lost inside future plans suffers blueprint aging. "
        "It is maintained resting its head on a current support outside the phantom plan, reading intended "
        "use and present use separately, and the missing plan face is always left blank. Shutdown grounds "
        "the Maul before the last required strike becomes a completion impulse."
    ),
    "s-255": (
        "The Architect\u2019s Mantle is a matte black garment of Han weave with open seams exactly where "
        "walls, doors, and supports are missing from the source plan \u2014 the suit is an honest copy of an "
        "unfinished building, gaps included. It condenses from construction dust after Ferrehan, and it "
        "binds to a wearer who will enter without supplying the missing element. Worn inside the phantom "
        "structure, Weight follows the open seams around the body instead of landing fully on it \u2014 the "
        "unfinished spans carry the load past the wearer \u2014 and closing a seam with tools, cargo, or "
        "another person removes the protection instantly. The cost is exhaustion for work never "
        "commissioned: constant low fatigue and a growing compulsion to complete every space entered; the "
        "first wearer crossed a hollow tower and emerged as tired as if she had worked a full construction "
        "shift for occupants who never arrived. A wearer bracing an absent element becomes load-bearing \u2014 "
        "the human-support failure \u2014 and a repaired seam creates a hollow structural void. It is "
        "maintained hung on an incomplete frame with each open seam unsupported, dust removed but gaps "
        "never patched. Removal exits the plan boundary and lets the garment fall from the missing side "
        "first."
    ),
    "g-255": (
        "The Architect\u2019s Compass is a black head-compass of Han steel with no cardinal marks at all \u2014 its "
        "needle ignores geography and follows intended circulation instead: door, stair, gathering place, "
        "light. The Architect granted it after a cartographer mapped an unfinished structure by purpose "
        "without adding the missing room; it cannot be manufactured. Held over damaged or incomplete "
        "construction, it reveals the intended structure beneath \u2014 in its recorded case, a planned clinic "
        "entry that was never built, whose intended route located buried utilities without the nonexistent "
        "clinic ever being marked as recovered infrastructure. The cost is grief for the unbuilt: the "
        "bearer feels every future the building failed to hold. A needle pointing toward people who never "
        "arrived is the first corrosion sign, planned use replacing actual current need the second, and a "
        "needle locked on the missing element is the completion pull. Blueprint authority \u2014 intended "
        "structure overriding living users \u2014 is the listed capture failure. Care compares intended plan, "
        "current structure, and current occupants on separate maps, and the Compass clears only while all "
        "three remain distinct. Emergency release leaves the construction zone and orients to a living "
        "person\u2019s stated present destination; forcing north destroys the purpose needle."
    ),
    "w-260": (
        "This Memory Requiem is a singing blade of deep-blue Han crystal whose fuller resembles a worn "
        "path \u2014 the groove polished not by grinding but by the remembered passage of feet that no longer "
        "cross anywhere. It forms from residue after the Bridge settles, and binding requires the wielder "
        "to state their current location and admit aloud that the old route cannot be restored. In use it "
        "pierces up to three unstable lift points along the remembered route, cutting rising memory supports "
        "before the Bridge lifts people into an ascent with no far shore \u2014 and striking a path-stone "
        "damages the memory itself, removing one traveler from the historical crossing. The wielder pays "
        "in departure grief: they feel the route\u2019s unwept sorrow and cry involuntarily, the "
        "first bearer weeping at the final departure of a traveler he never knew. A shore cut costs the "
        "route\u2019s history a traveler; a transport line turns the crossing into current infrastructure and "
        "raises the apex higher. It rests parallel to the settled footprint for maintenance, old route and "
        "current location read as separate entries, the fuller drying with its worn marks unpolished. Shutdown lowers the point when the Bridge returns to flat memory, even if the route "
        "remains visible."
    ),
    "s-260": (
        "This Memory Shroud is a wrapping shroud of blue Han-silk patterned with two absent shores \u2014 one "
        "at each hem \u2014 and a single current-location mark woven over the heart. It condenses from bridge "
        "mist after Ferrehan, and it binds only through a physical anchor taken from the present site: "
        "something real, carried against the cloth. Worn while a remembered crossing tries to overwrite the "
        "present, the heart mark keeps current place and identity accessible \u2014 the wearer stands in the "
        "Gardens even while the Gardens become an erased riverside route. Losing the physical anchor makes "
        "the cloth follow the vanished route, wearer included. The cost is a traveler\u2019s numbness: minor "
        "joys fade, especially pleasure associated with travel or return, buried under the accumulated "
        "farewells of everyone who ever crossed. A wearer left standing on the remembered shore after the "
        "Bridge settles is the anchor-loss failure, and a current home that feels less real than the route "
        "is return numbness. It is maintained wrapped around the present anchor beside the settled "
        "footprint while two people name the current site without describing the old shore. Removal steps "
        "completely off the memory route and unwraps from the heart mark outward."
    ),
    "g-260": (
        "The Memory Span is a warm blue tail-charm of Han crystal shaped like two route stones with empty "
        "space between them \u2014 the crossing itself, carried as an absence between two points. The Bridge "
        "granted it after a cartographer mapped a crossing as memory and allowed it to settle; it cannot be "
        "manufactured. Its function sounds like transport and is not: one remembered distance may be "
        "crossed once \u2014 in its recorded use, carrying its bearer across a missing stair memory to reach "
        "a trapped observer, entry and exit both occurring in the same present room. Only the "
        "remembered effort and the farewells were real. The cost is those farewells: the bearer feels the "
        "final goodbye of everyone attached to the route. The empty gap filling with a desired shore is the "
        "first corrosion sign, and a bearer confusing remembered transit with teleportation is the "
        "destination claim \u2014 the Gift constructing a false shore. A second crossing strands the bearer "
        "inside route memory. Care maps old path and current geometry on separate layers; the Span clears "
        "when they share only the crossing action, never a destination. Emergency release "
        "drops the destination claim, names current ground, and crosses back through the same memory once."
    ),
    "w-270": (
        "The Lake Requiem is a singing blade of deep-blue Han crystal whose edge holds a perfectly still "
        "liquid line \u2014 a waterline that does not tilt when the blade moves, level against every horizon "
        "except the Lake\u2019s own. It forms from a witnessed memory that voluntarily surfaced and returned, "
        "and it binds only to a wielder holding two current identity anchors. Its work is separation "
        "without harvest: the blade pierces up to three overflow connections while preserving the "
        "memory-mass as one record \u2014 in its recorded case, separating one stranger\u2019s early life from "
        "three workers without cutting the memory into fragments \u2014 and striking the remembered figure "
        "splits its identity instead. The wielder pays in unclaimed mourning: they receive the Lake\u2019s "
        "unwept grief and cry involuntarily, the first bearer weeping for a family whose names were absent "
        "from every file. A coherent memory fragmenting across several hosts is the life-cut failure, and a "
        "bearer who adopts the memory loses a self-anchor. It is maintained suspended over still Lake water "
        "without contact, the memory\u2019s provenance record read once, the liquid edge kept unbroken. "
        "Shutdown sheathes after one complete separation and returns all surfaced material."
    ),
    "s-270": (
        "The Lake Shroud is a wrapping of deep-blue Han-silk with a dark reflective outer layer and one "
        "warm pulse line running inside \u2014 a single thread of current life sewn through a surface built to "
        "carry other people\u2019s. It condenses from mist after a witnessed memory returns to the Lake, and it "
        "binds through two personal anchors and a shore partner watching from dry ground. Worn at an "
        "overflow, historical lives reflect across the outer cloth without entering the wearer\u2019s identity \u2014 "
        "hundreds of strangers\u2019 years crossing the fabric while the pulse line keeps the current body "
        "legible. Void can erase the pulse, and deep Weight can submerge it. The cost is scale: minor joys "
        "go numb beside the mass of stored life, small pleasures feeling irrelevant for days. The outer "
        "life replacing the inner pulse is the reflection-merger failure, and a wearer who crosses the "
        "waterline becomes another stored reflection \u2014 the suit is not diving equipment and may not enter "
        "the Lake. It is maintained hung facing ordinary still water while the wearer states two current "
        "anchors and the shore partner confirms the pulse line. Removal steps beyond all memory water and "
        "opens from the warm inner seam."
    ),
    "g-270": (
        "The Lake Flask is a warm tail-flask of deep-blue Han crystal that looks empty until it is held "
        "against witnessed Lake memory \u2014 then its interior moves, one life in liquid form. Mnemosyne "
        "granted it after a worker catalogued one life and returned it without claiming ownership; it "
        "cannot be manufactured. Its function is custody, never collection: it stores one witnessed memory "
        "long enough for the work that requires it \u2014 in its recorded case, one lost street-vendor\u2019s "
        "memory carried long enough to compare an erased market map. The cost is the ending: the user feels "
        "the death or loss attached to the stored life \u2014 the vendor\u2019s final empty stall remained in the "
        "bearer\u2019s body until the Flask returned to the shore. Liquid displaying the bearer\u2019s face instead "
        "of the source life is the ownership stain \u2014 a bearer calling the stored life \u201cmy memory\u201d \u2014 and a "
        "second memory added mixes both identities in the capacity breach. Unwitnessed contents evaporate "
        "and leave grief without record. Care keeps the witness present, reads provenance, and returns the "
        "liquid to its original channel; the Flask clears once the same memory reappears in the Lake. "
        "It opens only at the witnessed shore, never into another archive vessel."
    ),
    "w-275": (
        "The Rage Hammer is a heavy crimson forge-hammer of Han iron that pulses in the hand like "
        "Crucible\u2019s own heart \u2014 a slow beat through the haft that quickens near unnamed anger. It forms "
        "from cooled slag after the Forge produces a named nonviolent tool, and its binding is a "
        "declaration: the wielder states the anger entering the work and the object\u2019s protective purpose "
        "before the first strike. In use, hostile force accelerates Han shaping at one selected target \u2014 "
        "opposition becomes forge-heat, a breach hammering the opposite door speeding the brace being "
        "shaped against it \u2014 but using manufactured opposition or personal resentment as fuel imprints "
        "that anger permanently into the result. The cost is relational: the wielder feels anger toward "
        "every object altered, hating each correction the metal requires. Provoking hostility for speed is "
        "the enemy-manufacture failure, and a protective item developing an aggressive function is weapon "
        "drift. It is maintained by reworking one harmless scrap slowly with no opposition, naming each "
        "error without striking harder \u2014 the pulse clears when the object is allowed to remain imperfect. "
        "Shutdown sets the Hammer on cooled slag and stops work before anger becomes the reason to "
        "continue."
    ),
    "s-275": (
        "The Rage Plate is a dark crimson harness of Han iron that runs warm at every joint and cold "
        "against the skin \u2014 forge-heat held in the armor\u2019s moving parts, never quite reaching the body it "
        "protects. It condenses from controlled-work slag, and its binding has three terms: a named anger, "
        "a shift limit, and an external supervisor with authority to enforce both. Worn at the Forge, the "
        "armor receives directed hostility and furnace heat as structural hardening \u2014 the Crucible\u2019s "
        "Grudge field tempering the plates \u2014 but the protection falls as resentment turns supervision into "
        "combat; the first wearer\u2019s reflexes slowed each time she treated the Forge as an adversary rather "
        "than a worksite. The cost concentrates where the wearer resists help: reflexes dull, especially "
        "when rest or correction is refused. A wearer who cannot stop after the stated limit has hit shift "
        "lock, feedback hardening the joints is correction rage, and exhaustion arriving as absence rather "
        "than anger is Void burnout. It is maintained by opening each joint during a cold Forge period and "
        "logging the emotion present when it stiffened; no plate is reheated while blame remains unnamed. "
        "The supervisor ends the shift aloud before releasing the slowest joint."
    ),
    "g-275": (
        "This Rage Charm is a crimson tail-charm of Han iron shaped like a small cooled coal \u2014 spent fuel, "
        "carried as a reminder of what fuel costs. It warms around acknowledged anger and burns outright "
        "around emotion being treated as free fuel; the distinction is its entire function. Crucible "
        "granted it after a worker named resentment before making a repair tool; it cannot be manufactured. "
        "As the audit point of its set, it distinguishes named emotional input from hidden rage entering "
        "the Forge \u2014 in its recorded case staying warm while workers described their anger, and flaring "
        "only when a supervisor called that rage \u201cuseful output variance.\u201d The bearer\u2019s temper shortens "
        "for as long as they carry it. A Charm burning around all production work is the first corrosion "
        "sign; a bearer mistaking temper for diagnostic truth is the second; and anger treated as resolved "
        "merely because it was logged is the third. Emotional naming becoming another production "
        "requirement is the metric-capture failure. Care records anger, source, requested change, and the "
        "worker\u2019s right to stop \u2014 the Charm cools only when naming changes the work conditions. Removal "
        "waits until production stops; a hot Charm torn free ignites every hidden resentment in the room."
    ),
    "w-280": (
        "The Tear Requiem is a short singing blade of deep-blue Han crystal whose edge beads with tears "
        "drawn from the nearest emotional attack \u2014 the weapon weeps before the wielder does. It forms from "
        "salt residue after a safe external Pall removal, and its binding is an order of operations: the "
        "wielder names their own grief before touching another\u2019s. In use it cuts one overwhelming "
        "emotional attack away from its target while leaving the person\u2019s own grief intact \u2014 in its "
        "recorded case separating a panic wave from a wearer without stopping the person\u2019s crying, because "
        "the crying was theirs and the attack was not. Treating grief itself as hostile wounds the "
        "mourner\u2019s mind. The wielder pays in inherited tears: they feel Pall\u2019s unwept grief and cry "
        "involuntarily, the first bearer weeping through every prior face Pall remembered. Authentic grief "
        "removed as threat is the mourner-cut failure, and suppressed tears return as a Lament strike "
        "through the dry edge. It is maintained resting on a dry stand while the wielder names which tears "
        "were theirs and which arrived through the set \u2014 the edge is never wiped. Shutdown sheathes only "
        "after the separated attack has been witnessed and released."
    ),
    "s-280": (
        "The Tear Veil is a flowing suit of blue Han-silk that breathes with the wearer and releases "
        "received emotional pressure as visible tears \u2014 protection that refuses to be private. It "
        "condenses from salt outside Pall\u2019s source weave, and it binds through an external remover and "
        "one personal grief marker chosen before wear. In the field the Veil absorbs one emotional attack "
        "and expresses it continuously rather than storing it unseen: fear, grief, and anger crossing the "
        "fabric as indistinguishable tears for everyone present to see. That visibility is the cost \u2014 the "
        "wearer displays all grief openly and cannot stop the expression until external removal; it must "
        "never be worn for anonymity. Collective tears erasing the wearer\u2019s identity is the "
        "faceless-mourning failure; continuous tears used as proof that processing is complete is false "
        "composure; and tears stopping because the wearer has disappeared behind them is Void drying. It is "
        "maintained hung where each tear can drain separately, wearer and remover identifying one personal "
        "grief marker before reuse. The assigned remover approaches from behind, names the wearer, and "
        "lifts the Veil only after a responsive answer."
    ),
    "g-280": (
        "The Tear Charm is a cool blue tail-charm of Han crystal holding one moving salt pattern \u2014 a "
        "single grief\u2019s signature, drifting slowly under the surface like sediment that never settles. "
        "Pall granted it after a worker wore the I-Relic, remained identifiable, and accepted external "
        "removal; it cannot be manufactured. Its function is ownership in a place built to dissolve it: the "
        "Charm preserves one personal grief marker within collective mourning \u2014 in its recorded case "
        "keeping a bearer\u2019s grief for a lost plan distinct from the older tears in Pall, letting her share "
        "the field without claiming the historical mourners\u2019 pain. The cost is nocturnal: the bearer weeps "
        "in sleep. A salt pattern that begins matching everyone nearby is the ownership blur; a bearer "
        "treating personal grief as more authentic than shared sorrow is building a grief hierarchy; and "
        "sleep-tears reproducing Pall\u2019s prior wearers mark the dream weave \u2014 a second Pall forming in the "
        "bearer\u2019s bed. Care requires naming the grief without comparing its size or importance; the Charm "
        "clears when the salt pattern remains distinct without becoming isolated. Emergency release wakes "
        "the bearer, identifies current grief, and moves them away from woven tear material before sleep "
        "resumes."
    ),
    "w-283": (
        "The Rust Wall Maul is a black maul of Han steel whose head is built from overlapping rusted faces "
        "with a single passable seam running through it \u2014 a wall rendered as weapon, with the gap "
        "preserved. It forms from dream-rust released after both sides of a separation are named; binding "
        "requires the wielder to identify the current closure and the historic boundary separately. In "
        "use it carries Weight through up to three current closure points \u2014 newly "
        "hardened plates sealing a corridor \u2014 while the historic dream-boundary is left untouched; "
        "striking that older wall erases one side\u2019s departure evidence and transfers it into the wielder. "
        "The cost is the wall\u2019s age: progressive heaviness and slight aging, the first bearer\u2019s arms "
        "gaining the felt age of the abandoned boundary. Both sides flattened into one false account is the "
        "neutral-blow failure; authorized passage treated as intrusion is return denial; and a bearer who "
        "becomes the wall\u2019s new stationary purpose has inherited its rust. It is maintained resting across "
        "an open route while one account from each side is read without combining them, brushing only the "
        "rust shed at the passable seam. Shutdown grounds the Maul after passage reopens \u2014 the remaining "
        "dream image is not demolished."
    ),
    "s-283": (
        "The Rust Wall Plate is a black harness of Han steel assembled from rusted boundary plates \u2014 "
        "sections of a wall that exiled and admitted, refitted to a human frame. It condenses after a "
        "stable dream crossing, and it binds only through a named passage partner from the opposite side of "
        "the old line. Worn in a corridor compression, the Plate resists forced movement and corridor "
        "Weight while the wearer leaves room for crossing: they cannot be pushed from the route, and they "
        "must not become what blocks it. The cost is social and slow: the wearer becomes difficult to "
        "welcome into any group and may appear to belong to neither side \u2014 after its first deployment, "
        "personnel unconsciously addressed everyone except the wearer, because the armor had made "
        "resistance to movement look like refusal to belong. A wearer becoming the obstacle they resisted "
        "is the human-barrier failure, and social absence entering through the weak seams is Void exile. It "
        "is maintained with every plate open while one person from each side includes the wearer in a "
        "current task \u2014 rust clears only after participation, not verbal neutrality. The passage partner "
        "releases the rear plate while the wearer steps toward an explicitly named welcome point."
    ),
    "g-283": (
        "The Rust Wall Charm is a matte black head-charm of Han steel with two rusted faces and one clear "
        "seam between them \u2014 both sides of a separation carried at the temple, with the passage kept "
        "visible. The Subject granted it after an officer named city, exile, departure, and return without "
        "choosing one as the universal viewpoint; it cannot be manufactured. Its function is completion of "
        "the record: it identifies which side of a separation is absent from the current account \u2014 in its "
        "recorded case correcting a Gate review that described \u201coutbound traffic\u201d without naming "
        "involuntary exile, while refusing to classify every departure as forced. The bearer pays in the "
        "stride, moving more slowly under both histories. A Charm inventing two sides where "
        "more exist is the binary-wall failure; a bearer mistaking naming for agreement is the second sign; "
        "and movement stopping under the demand to represent everyone is representation load. A bearer "
        "claiming exemption from both consequences has built the neutral center. Care adds missing "
        "positions without merging them or speaking for them, and the Charm clears while its seam remains "
        "open and no side is labeled neutral. Emergency release transfers the record to multiple named "
        "witnesses and steps out of representative authority."
    ),
})

SLOT_BY_SUFFIX = {"B": "w", "C": "s", "D": "g"}


def find_set_mds(num: str) -> list[Path]:
    """Registry item records for a set: nested set dir or flat registry folder."""
    dirs = [d for d in REG.glob(f"*/{num}_*") if d.is_dir()]
    if len(dirs) == 1:
        hits = sorted(dirs[0].glob(f"SE-{num}-[BCD]__MAW-*.md"))
    else:
        hits = sorted(REG.glob(f"*/SE-{num}-[BCD]__MAW-*.md"))
    if len(hits) != 3:
        raise SystemExit(f"set {num}: expected 3 registry records, found {len(hits)}")
    return hits


def find_html(num: str, slot: str) -> Path:
    hits = sorted(DOCS_MAW.glob(f"maw-{slot}-{num}-01-*.html"))
    if len(hits) != 1:
        raise SystemExit(f"set {num} slot {slot}: expected 1 html page, found {hits}")
    return hits[0]


def insert_md(md_path: Path, paragraph: str, write: bool) -> None:
    text = md_path.read_text(encoding="utf-8")
    if re.search(r"^##+ Appearance\s*$", text, re.M):
        raise SystemExit(f"{md_path.name}: already has an Appearance heading")
    pos = None
    for heading in STATS_HEADINGS:
        i = text.find("\n" + heading)
        if i != -1 and (pos is None or i < pos):
            pos = i
    if pos is None:
        raise SystemExit(f"{md_path.name}: no stats heading found for insertion")
    new = text[: pos + 1] + "## Appearance\n\n" + paragraph + "\n\n" + text[pos + 1 :]
    if write:
        md_path.write_text(new, encoding="utf-8")


def insert_html(html_path: Path, paragraph: str, write: bool) -> None:
    text = html_path.read_text(encoding="utf-8")
    if 'id="appearance"' in text:
        raise SystemExit(f"{html_path.name}: already has an appearance section")
    marker = '<h2 id="extraction-or-bestowal">'
    if text.count(marker) != 1:
        raise SystemExit(f"{html_path.name}: extraction marker count != 1")
    block = f'<h2 id="appearance">Appearance</h2><p>{paragraph}</p>'
    new = text.replace(marker, block + marker)
    if write:
        html_path.write_text(new, encoding="utf-8")


def main() -> None:
    write = "--write" in sys.argv
    batch_id = DEFAULT_BATCH
    for arg in sys.argv[1:]:
        if arg.startswith("--batch="):
            batch_id = arg.split("=", 1)[1]
    batch = BATCHES[batch_id]
    report = []
    for num in batch:
        for md_path in find_set_mds(num):
            suffix = re.search(r"-([BCD])__", md_path.name).group(1)
            slot = SLOT_BY_SUFFIX[suffix]
            key = f"{slot}-{num}"
            md_text = md_path.read_text(encoding="utf-8")
            paragraph = OVERRIDES.get(key) or compose(md_text)
            if not paragraph:
                raise SystemExit(f"{md_path.name}: could not compose Appearance (no override)")
            words = len(paragraph.split())
            if not (WORD_MIN <= words <= WORD_MAX):
                raise SystemExit(f"{md_path.name}: {words} words out of range {WORD_MIN}-{WORD_MAX}")
            html_path = find_html(num, slot)
            insert_md(md_path, paragraph, write)
            insert_html(html_path, paragraph, write)
            report.append((key, words, md_path.name, html_path.name))
    verb = "wrote" if write else "validated (dry-run)"
    print(f"{verb} {len(report)} Appearance sections across {len(batch)} sets (batch {batch_id})")
    for key, words, mdn, htn in report:
        print(f"  {key}: {words} words  {mdn}  ->  {htn}")


if __name__ == "__main__":
    main()
