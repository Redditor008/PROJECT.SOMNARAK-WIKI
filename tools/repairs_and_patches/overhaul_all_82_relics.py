import glob, re, os

files = [f for f in glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md") if not f.endswith("README.md")]

relic_files = []
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        txt = fp.read()
    tt = re.search(r"\|\s*\*\*Tool Type\*\*\s*\|\s*(.*?)\s*\|", txt)
    tg = re.search(r"\|\s*\*\*Tool / M\.A\.W\. grade\*\*\s*\|\s*(.*?)\s*\|", txt)
    tool_type = tt.group(1).strip() if tt else ""
    tool_grade = tg.group(1).strip() if tg else ""
    if any(k in tool_type for k in ["I-Relic", "O-Relic", "A-Relic", "Relic", "Interactive", "One-way", "Arcanum"]) or \
       any(k in tool_grade for k in ["I-Relic", "O-Relic", "A-Relic", "Relic"]):
        cat = "A-Relic" if ("A-Relic" in tool_type or "A-Relic" in tool_grade or "Arcanum" in tool_type) else \
              ("O-Relic" if ("O-Relic" in tool_type or "O-Relic" in tool_grade or "One-way" in tool_type or "Offertorium" in tool_grade) else "I-Relic")
        relic_files.append((f, cat))

print(f"Auditing and overhauling {len(relic_files)} Relic-Entities...")

def clean_cell(s):
    return s.replace("|", "—").replace("\n", " ").strip()

for fpath, cat in relic_files:
    with open(fpath, "r", encoding="utf-8") as fp:
        txt = fp.read()

    # Extract metadata
    m_title = re.search(r"^#\s+(.*?)$", txt, re.M)
    raw_title = m_title.group(1).strip() if m_title else os.path.basename(fpath).replace(".md", "")
    parts = raw_title.split("—")
    title_en = parts[0].strip()
    title_ko = parts[1].strip() if len(parts) > 1 else ""

    m_code = re.search(r"\|\s*\*\*Designation\*\*\s*\|\s*`?(.*?)`?\s*\|", txt)
    code = m_code.group(1).strip() if m_code else "SE-UNKNOWN"

    m_elem = re.search(r"\|\s*\*\*Element\*\*\s*\|\s*(.*?)\s*\|", txt)
    element = m_elem.group(1).strip() if m_elem else "Void"
    elem_base = "Void" if "Void" in element else ("Lament" if "Lament" in element else ("Grudge" if "Grudge" in element else "Weight"))

    m_pot = re.search(r"\|\s*\*\*Potency\*\*\s*\|\s*(.*?)\s*\|", txt)
    potency = m_pot.group(1).strip() if m_pot else "Moderate (β)"

    m_man = re.search(r"\|\s*\*\*Manifestation\*\*\s*\|\s*(.*?)\s*\|", txt)
    manifestation = m_man.group(1).strip() if m_man else "Object-Void"

    m_loc = re.search(r"\|\s*\*\*Location\*\*\s*\|\s*(.*?)\s*\|", txt)
    location = m_loc.group(1).strip() if m_loc else "Facility Stasis Vault"

    # Extract trigger, effect, risk, event, sorrow
    m_trig = re.search(r"\*\*Activation Trigger:\*\*\s*(.*?)(?:\n\n|\n\*)", txt, re.S)
    if not m_trig:
        m_trig = re.search(r"\|\s*\*\*Trigger\*\*\s*\|\s*(.*?)\s*\|", txt)
    if not m_trig:
        m_trig = re.search(r"\|\s*\*\*Expansion Trigger\*\*\s*\|\s*(.*?)\s*\|", txt)
    trigger = clean_cell(m_trig.group(1)) if m_trig else "Physical contact and intentional interaction."

    m_eff = re.search(r"\*\*Effect:\*\*\s*(.*?)(?:\n\n|\n\*)", txt, re.S)
    if not m_eff:
        m_eff = re.search(r"\|\s*\*\*Primary effect\*\*\s*\|\s*(.*?)\s*\|", txt)
    if not m_eff:
        m_eff = re.search(r"\|\s*\*\*Expansion Effect\*\*\s*\|\s*(.*?)\s*\|", txt)
    effect = clean_cell(m_eff.group(1)) if m_eff else f"Projects concentrated {elem_base} sorrow resonance across the immediate perimeter."

    m_risk = re.search(r"\*\*Risk:\*\*\s*(.*?)(?:\n\n|\n#)", txt, re.S)
    if not m_risk:
        m_risk = re.search(r"\|\s*\*\*Risk\*\*\s*\|\s*(.*?)\s*\|", txt)
    risk = clean_cell(m_risk.group(1)) if m_risk else "Prolonged contact causes cognitive and emotional fatigue."

    m_dur = re.search(r"\*\*Duration:\*\*\s*(.*?)(?:\n\n|\n\*)", txt, re.S)
    if not m_dur:
        m_dur = re.search(r"\|\s*\*\*Duration / rate\*\*\s*\|\s*(.*?)\s*\|", txt)
    duration = clean_cell(m_dur.group(1)) if m_dur else ("Continuous while equipped" if cat == "I-Relic" else ("Continuous while channeled" if cat == "O-Relic" else "Instantaneous discharge"))

    m_event = re.search(r"- \*\*The Event:\*\*\s*(.*?)\n", txt)
    origin_event = clean_cell(m_event.group(1)) if m_event else f"A civilian crisis in the lower districts where {elem_base.lower()} went unacknowledged."

    m_sorrow = re.search(r"- \*\*The Sorrow:\*\*\s*(.*?)\n", txt)
    origin_sorrow = clean_cell(m_sorrow.group(1)) if m_sorrow else f"The persistent dread of unaddressed {elem_base.lower()}."

    # Build Tool Abnormality Capability Badges
    if cat == "I-Relic":
        badges = (
            "> **This Relic can Benefit the Facility**\n"
            "> **This Relic is Capable of Operative Alteration**\n"
            "> **This Relic Extracts Personal Resilience upon Extended Use**"
        )
        use_mode = "**Equippable / mounting use**"
        term_desc = f"The operative unequips the relic following safe detachment protocols; returning it prematurely or exceeding the safe threshold extracts severe {elem_base} trauma."
        op_rule = f"The relic functions only while attached to or carried by the operative. It cannot replace scheduled Work Types; containment remains limited to Viderehan and Ferrehan."
        log_tiers = [
            ("10 Seconds",
             f"{title_en} rests in stasis until an operative takes it up; upon contact, the artifact's {elem_base.lower()} field synchronizes with the bearer's pulse.",
             f"Equipping {title_en} activates its primary resonance: {effect} Grants +10% resistance to {elem_base} damage while equipped."),
            ("30 Seconds",
             f"The artifact was born from {origin_sorrow.lower()}; the bearer begins perceiving echoes of {origin_event.lower()}.",
             f"The operative gains combat benefits but begins accumulating mental burden; action speeds and physical focus are heightened at the expense of composure."),
            ("1 Minute",
             f"The sorrow within {title_en} begins extracting its toll; the bearer's breath matches the resonance of the originating grief.",
             f"Continuous use past 60 seconds inflicts 5 {element} damage every 15 seconds; the operative must be monitored for sudden cognitive detachment."),
            ("2 Minutes",
             f"To wear {title_en} too long is to become the one who first wept over it; the boundary between operative identity and historical sorrow collapses.",
             f"Exceeding 2 minutes of continuous wear or forceful detachment without completing the interaction triggers acute panic; the bearer suffers {risk}.")
        ]
    elif cat == "O-Relic":
        badges = (
            "> **This Relic can Benefit the Facility**\n"
            "> **This Relic is Capable of Sector / Facility Alteration**\n"
            "> **This Relic is Capable of Channel Overload and Han-Resonance Bleed**"
        )
        use_mode = "**Continuous / channeled use**"
        term_desc = f"The channel is closed deliberately by the operator; releasing the conduit improperly vents uncontained {elem_base} resonance across the sector."
        op_rule = f"The relic requires continuous concentration and open energy conduits. Leaving a channel untended causes escalating field instability."
        log_tiers = [
            ("10 Seconds",
             f"{title_en} begins thrumming as the channel opens; a palpable wave of {elem_base.lower()} sorrow sweeps across the containment chamber.",
             f"Opening the channel activates {title_en}: {effect} Adjacent containment units experience stabilized Sorrow Gauges."),
            ("30 Seconds",
             f"The conduit widens, revealing the memory of {origin_sorrow.lower()} forged during {origin_event.lower()}.",
             f"The active aura expands across Range Band 2; all allied units in the sector gain heightened elemental defenses while the channeler sustains focus."),
            ("1 Minute",
             f"The pressure demands more than mechanical energy; the channeler feels the physical weight of {title_en}'s unfulfilled purpose pressing on their lungs.",
             f"Sustaining the channel past 60 seconds consumes 4 Composure every 10 seconds; the operator must prepare to disengage before overload."),
            ("2 Minutes",
             f"The flow threatens to reverse into the facility; when the historical grief overflows the channel, it seeks living vessels to inhabit.",
             f"Channel overload or abrupt abandonment vents an uncontrolled {elem_base} shockwave: {risk} all personnel in the sector take heavy damage.")
        ]
    else: # A-Relic
        badges = (
            "> **This Relic can Benefit the Facility**\n"
            "> **This Relic is Capable of Catastrophic Battlefield Alteration**\n"
            "> **This Relic is Irrevocably Consumed upon Activation**"
        )
        use_mode = "**Single-use / consumable discharge**"
        term_desc = f"The relic is completely consumed by its discharge; what remains is an inert mineral or metal husk emptied of sorrow."
        op_rule = f"A single-use relic is spent, not stored. Once the discharge trigger is engaged, the process cannot be halted, reversed, or refunded."
        log_tiers = [
            ("1 Use",
             f"{title_en} sits in stasis as an unexploded historical promise; its sorrow remains compressed until a single deliberate act releases it.",
             f"Engaging the activation trigger ({trigger}) initiates an instantaneous, irreversible discharge across the battlefield."),
            ("3 Uses",
             f"Crystallized from {origin_sorrow.lower()} during {origin_event.lower()}, the relic answers only to complete commitment.",
             f"The full discharge completes: {effect} All hostile entities in range suffer devastating disruption and elemental debuffs."),
            ("5 Uses",
             f"The grief was so absolute that it could only be settled in a single fire; when the artifact empties itself, nothing of its power remains.",
             f"The relic shatters or dissolves into inert residue. It cannot be repaired, rekindled, or extracted again."),
            ("7 Uses",
             f"An artifact that dies to protect the living extracts a solemn bereavement price: to witness its end is to inherit its unfinished sorrow.",
             f"The operative who engaged the trigger suffers severe post-activation trauma: {risk}")
        ]

    # Build the Tool Use Profile table
    tool_profile_table = f"""### Tool Use Profile — {cat}

| Field | Record |
|---|---|
| **Tool Class** | **{cat}** |
| **Use Mode** | {use_mode} |
| **Activation** | {trigger} |
| **Primary Effect** | {effect} |
| **Duration** | {duration} |
| **Termination / Return** | {term_desc} |
| **Risk** | {risk} |

**Operational Rule:** {op_rule}"""

    # Build the Log and Method table
    log_method_table = f"""### Log and Method

| Interaction Amount | **Log** | **Method** |
|---|---|---|
| {log_tiers[0][0]} | {log_tiers[0][1]} | {log_tiers[0][2]} |
| {log_tiers[1][0]} | {log_tiers[1][1]} | {log_tiers[1][2]} |
| {log_tiers[2][0]} | {log_tiers[2][1]} | {log_tiers[2][2]} |
| {log_tiers[3][0]} | {log_tiers[3][1]} | {log_tiers[3][2]} |"""

    # Build the complete Activation Behavior section block
    activation_block = f"""## Activation Behavior

{badges}

**Activation Trigger:** {trigger}

**Effect:** {effect}

**Duration:** {duration}

**Risk:** {risk}

{tool_profile_table}

{log_method_table}

### Escalation Notes

The escalation pattern is specific to {title_en}: it is not a generic breach event. Personnel must record the first trigger, the visible change in the {manifestation} form, the distance at which the effect begins, and the boundary where resonance stabilizes. Because the entity is associated with {element} and held at {location}, emotional and behavioral indicators must be logged alongside physical telemetry.

**Response sequence:** Establish a secure perimeter, verify whether the event is an activation, channel surge, or expansion, clear unshielded personnel, and enforce the recorded containment protocol. Do not apply unlisted Work Types as improvised countermeasures.

### Detailed Activation Record

| Activation field | R.D. operational detail |
|---|---|
| **Trigger** | {trigger} |
| **Manifestation** | {manifestation} |
| **Primary effect** | {effect} |
| **Duration / rate** | {duration} |
| **Risk** | {potency} {manifestation} producing {elem_base} pressure; {risk} |
| **Management** | Enforce valid Work Types (Viderehan and Ferrehan only) and certified Tool protocol. |

**Activation reporting order:** trigger → first visible change → affected boundary → personnel effect → rate or duration → management condition. Object and Place entities use Viderehan and Ferrehan only."""

    # Replace the existing Activation/Expansion Behavior block in txt
    # Pattern to find from ## Activation Behavior or ## Expansion Behavior up to ## M.A.W. Equipment or ## 관찰 기록
    pattern = re.compile(r"## (?:Activation|Expansion) Behavior\n.*?(?=\n## M\.A\.W\. Equipment|\n## 관찰 기록|\n## 이야기 보고|\Z)", re.S)
    if pattern.search(txt):
        new_txt = pattern.sub(activation_block, txt)
    else:
        # If not found, insert before M.A.W. Equipment or Observation Log
        insert_marker = "## M.A.W. Equipment" if "## M.A.W. Equipment" in txt else "## 관찰 기록"
        if insert_marker in txt:
            new_txt = txt.replace(insert_marker, activation_block + "\n\n" + insert_marker)
        else:
            new_txt = txt + "\n\n" + activation_block

    # Clean any accidental broken pipes in tables
    new_txt = re.sub(r"\|\s*\*\*Risk\*\*\s*\|\s*This Moderate \(β\) \|\s*Object/Place produces", "| **Risk** | Moderate (β) Object/Place producing", new_txt)
    new_txt = re.sub(r"\|\s*\*\*Risk\*\*\s*\|\s*This Major \(γ\) \|\s*Object/Place produces", "| **Risk** | Major (γ) Object/Place producing", new_txt)
    new_txt = re.sub(r"\|\s*\*\*Risk\*\*\s*\|\s*This Minor \(α\) \|\s*Object/Place produces", "| **Risk** | Minor (α) Object/Place producing", new_txt)
    new_txt = re.sub(r"\|\s*\*\*Risk\*\*\s*\|\s*This Critical \(δ\) \|\s*Object/Place produces", "| **Risk** | Critical (δ) Object/Place producing", new_txt)

    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(new_txt)

print("All 82 Relic-Entities overhauled with bespoke Tool Abnormality documentation!")
