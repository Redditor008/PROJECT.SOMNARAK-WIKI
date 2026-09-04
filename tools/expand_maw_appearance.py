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

BATCH = ["159", "160", "165", "168", "169", "170", "175", "176", "180", "184", "185", "189"]

WORD_MIN, WORD_MAX = 150, 205

STATS_HEADINGS = [
    "## CORE STATISTICS",
    "## PROTECTION STATISTICS",
    "## GIFT STATISTICS",
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

SLOT_BY_SUFFIX = {"B": "w", "C": "s", "D": "g"}


def find_set_dir(num: str) -> Path:
    hits = [d for d in REG.glob(f"*/{num}_*") if d.is_dir()]
    if len(hits) != 1:
        raise SystemExit(f"set {num}: expected 1 registry dir, found {hits}")
    return hits[0]


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
    report = []
    for num in BATCH:
        set_dir = find_set_dir(num)
        for md_path in sorted(set_dir.glob(f"SE-{num}-[BCD]__MAW-*.md")):
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
    print(f"{verb} {len(report)} Appearance sections across {len(BATCH)} sets")
    for key, words, mdn, htn in report:
        print(f"  {key}: {words} words  {mdn}  ->  {htn}")


if __name__ == "__main__":
    main()
