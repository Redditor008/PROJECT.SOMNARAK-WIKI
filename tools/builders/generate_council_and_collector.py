#!/usr/bin/env python3
"""
Generate SOMNARAK_COUNCIL_OF_SIGHS.md and SOMNARAK_COLLECTOR_BUREAU.md
with 100% text-box symmetry (71 cols), zero HTML tags, zero dollar signs,
and authentic in-universe municipal lore.
"""

def make_box(width, title, lines):
    inner_width = width - 4
    out = []
    top_border = "+" + "-" * (width - 2) + "+"
    out.append(top_border)
    if title:
        t_pad = title.center(inner_width)
        out.append(f"| {t_pad} |")
        out.append("+" + "-" * (width - 2) + "+")
    for l in lines:
        if len(l) > inner_width:
            raise ValueError(f"Line too long ({len(l)} > {inner_width}): {l}")
        l_pad = l.ljust(inner_width)
        out.append(f"| {l_pad} |")
    out.append("+" + "-" * (width - 2) + "+")
    return "```text\n" + "\n".join(out) + "\n```\n\n"

def build_council_md():
    box1 = make_box(71, "COUNCIL OF SIGHS - HIGH CHAMBER OF MUNICIPAL GOVERNANCE", [
        "Sovereign Body    : High Council of Sighs (Tansik-ui Pyeong-uihoe)",
        "Seat of Authority : The Sigh Palace (North Bastion, Zone A)",
        "Total Seats       : Approximately Fifty Council Seats",
        "Public Leadership : First Head Dohee & Third Head Gwanhee",
        "Chief Executive   : Chief of Staff Yeong (Central Chancery)",
        "Shrouded Mystery  : ~45 Councilors Behind Acoustic Veils",
        "Security Tier     : Sovereign Archival Standard - Eyes Only"
    ])

    box2 = make_box(71, "KNOWN EXECUTIVE ROSTER - PUBLIC FACES & HISTORICAL ANCHORS", [
        "Chief of Staff    : Yeong (The Clerk Who Knew Everything)",
        "First Head        : Dohee (The Voice of the Veil & Public Face)",
        "Third Head        : Gwanhee (The Eye of the Archive & Memory)",
        "Sector Head A     : Jaehwan (Warden of the Veil, Zone A)",
        "Sector Head C     : Miran (The Ledger Master, Zone C)",
        "Sector Head E     : Sangmin (The Gate Warden, Zone E)",
        "Veiled Seats      : Second Head, Fourth Head, Fifth Head (Cloaked)"
    ])

    content = f"""# The High Council of Sighs — 한숨의 평의회
## Sovereign Municipal Governance & The Veiled Chamber

---

{box1}
## 1. Institutional Mandate & Historical Coalescence

The High Council of Sighs (탄식의 평의회 — Tansik-ui Pyeong-uihoe) is the supreme civilian and civil-administrative governing body of Somnarak. Unlike sovereign institutions that were founded through monarchical proclamation or corporate charter, the Council was not created by a single ruler; it **coalesced** during the devastation of the Consolihan War, born from the collective exhaustion of community leaders, ward captains, and surviving engineers who realized that without centralized management of fluid Han, the city would dissolve into terminal weeping.

The Council's foundational premise is rooted in the doctrine of civic burden:
> *"Those who govern do not rule by right of blood or gold. They sit upon the stone because their souls are heavy enough to counterbalance the sinking of the floor."*

The assembly convenes within the Sigh Palace (탄식의 궁), located at the northern apex of Zone A (The Veil). Its massive granite walls are continually lined with condensation from pressurized subterranean Han channels, weeping slow, steady tears of mineralized water that drain into central bronze gutters.

---

## 2. Structural Architecture: The Known and The Cloaked

{box2}
The High Council comprises approximately fifty seats, but only a minute fraction of its members ever present their faces, voices, or civil identities to the public. The vast majority of the councilors remain permanently shrouded behind acoustic-dampening silk screens, anonymous voting tablets, and sealed black-wax missives.

### 2.1 The Strategic Necessity of Mystery
This division between the known and the cloaked is not merely an aristocratic vanity; it is an engineered survival mechanism against psychological and metaphysical weaponization:
- **Resonance Insulation:** If an entity or revolutionary faction were to identify the true names, personal griefs, and emotional vulnerabilities of all fifty councilors, a targeted Sorrow resonance could cause the entire municipal government to suffer concurrent Composure Meltdowns.
- **Inviolable Continuity:** When a cloaked councilor dies or succumbs to Fracture, their seat is filled immediately by a vetted successor from the civil service without public announcement, presenting an unbroken, immortal facade of bureaucratic continuity.
- **Unquestioned Objectivity:** Decisions regarding resource rationing, quota enforcement, and Zone B quarantine are delivered as cold institutional decrees of the Council, shielding individual decision-makers from private vengeance.

---

## 3. In-Depth Profiles: The Known Leadership

Only a handful of figures within the Council have their identities confirmed across open civic ledgers. These individuals serve as the living bridges between the hidden council chambers, the Five Institutional Wings, and the civilian populace.

### 3.1 Chief of Staff Yeong (영) — The Clerk Who Knew Everything
- **Civil Designation:** Chief of Staff to the Council Secretariat
- **Physical Profile:** Mousy brown hair tied in a practical loose knot, tired steel-grey eyes, broad and durable build (~186 cm, 47 years of age), sallow parchment skin. Wears unadorned dark wool robes.
- **Operational Tenure:** Over forty years of continuous service within the Sigh Palace.
- **Archival Assessment:**
  Yeong is neither an elected councilor nor an oligarchic lord, yet they are universally recognized as the single individual who makes Somnarak run. Entering the civil service at age twenty from the Archive's administrative apprentice pool, Yeong has outlasted seventeen successive council assemblies.
  Every draft decree, tax ledger, M.A.W. requisition request, and classified suppression order crosses Yeong's small, unvarnished wooden desk situated in the corner of the Grand Chamber. While council members debate ideology and panic during Sorrow Tides, Yeong methodically tracks grain deliveries, water pressure differentials, and ammunition stockpiles.
  Yeong preserves seventeen complete, fully-drafted municipal reform codices in their private lockbox. Whenever an idealistic new councilor approaches seeking to eliminate the debt system, Yeong patiently presents the historical precedent, warns them of the fiscal collapse that would follow immediate abolition, and guides them toward pragmatic, incremental relief.
  Yeong's personal sorrow is an absolute, bone-deep weariness: forty years of carrying the entire city's administrative weight without ever receiving or expecting gratitude.

### 3.2 First Head Dohee (도희) — The Voice of the Veil
- **Council Seat:** First Head / Executive Speaker
- **Public Title:** The Voice of the Veil
- **Status:** Fully Public and Celebrated
- **Archival Assessment:**
  Dohee is the public face and voice of Somnarak. An orator of extraordinary poise and emotional resonance, she delivers the annual State of the City address during the Consolihan Festival and announces major civic mobilizations. Her portraits hang in every municipal administrative hall across Zones A through C.
  Politically astute and diplomatically resilient, Dohee negotiated the historic **Treaty of the Exile's Gate** alongside Supreme Commander Kael, formally chartering the Horizon Caravan while preserving the Council's sovereign borders.
  While cynical citizens view her as an apologist for council conservatism, deep files confirm that Dohee genuinely believes in the necessity of the civic framework: that order, even imperfect order, is the only barrier separating two million civilians from the devouring jaws of The Maw.

### 3.3 Third Head Gwanhee (관희) — The Eye of the Archive
- **Council Seat:** Third Head / Archival Overseer
- **Public Title:** The Eye of the Archive
- **Status:** Publicly Acknowledged Historical Authority
- **Archival Assessment:**
  Eighty-nine years of age, frail of body but razor-sharp of intellect, Gwanhee is a former High Keeper of the Memory Archive who ascended to the Council over four decades ago. His left eye socket has been replaced by a faceted blue-crystal lens directly wired into the subterranean catalog nodes of Floor 6.
  Gwanhee remembers everything Somnarak has ever officially forgotten. When the Council debates whether to deploy kinetic force against syndicates or authorize deeper subterranean descents, Gwanhee recites the exact casualties, costs, and failures of identical operations conducted centuries prior.
  He is completely unsentimental, viewing human suffering as a thermodynamic equation that must be balanced to prevent structural collapse. He forgives nothing, but his archival accuracy ensures that the Council rarely repeats disastrous historical errors.

### 3.4 The Known Sector Heads (Field Executive Councilors)
Operating under the direct supervision of the Council are the three publicly confirmed Sector Heads:
- **Jaehwan (재환) — Sector Head of Zone A (The Veil):** A cold, meticulous career bureaucrat who has administered the inner residential wards for over two decades. He operates with total invisibility, ensuring that water, electricity, and acoustic dampeners function without interruption.
- **Miran (미란) — Sector Head of Zone C (Collector's Row / The Ledger Master):** The only Sector Head who actively maintains an operational license within the Collector Bureau. Brilliant, feared, and uncompromising, Miran treats Zone C as a giant fiscal balance sheet, ensuring that debt repayments match the municipal budget down to the last copper coin.
- **Sangmin (상민) — Sector Head of Zone E (The Gate Warden):** A battle-scarred former Warden Commander who assumed leadership of the border bastions following the Exile's Gate crisis. Exhausted and unyielding, Sangmin personally inspects the wall artillery daily, knowing that if Zone E falls, the inner zones will perish within hours.

---

## 4. The Cloaked Seats: Shadows of Municipal Sovereignty

The remaining forty-five seats, along with Three of the Five Executive Heads, are shrouded in impenetrable secrecy:

### 4.1 The Second Head: The Hand of Debt
The supreme administrator of the Collector Bureau. The Hand of Debt has never appeared before the general assembly. Orders bearing the Hand's seal arrive inscribed upon thin plates of black obsidian wax. These directives specify repossession quotas, interest rate adjustments, and indenture targets with inhuman mathematical precision. Field collectors revere the Hand not as a mortal bureaucrat, but as the living embodiment of fiscal necessity.

### 4.2 The Fourth Head: The Blade of Order
The clandestine commander of the Judexhan and the elite Giltong internal security squads. The Fourth Head's orders arrive through encrypted 432 Hz acoustic telegraphs that bypass all commercial lines. Even fellow councilors do not know who holds this seat; rumors persist that the Fourth Head is an autonomous title rotated among senior military commanders, or perhaps a long-dead general whose contingency protocols continue to execute automatically.

### 4.3 The Fifth Head: The Heart of the City
The greatest enigma in Somnarak. The Fifth Head's seat has been occupied continuously since the founding of the city, yet no surviving record identifies a name, a birthdate, or a physical face. Decrees from the Fifth Head are issued rarely—perhaps once every decade—and invariably concern existential threats to the Alpha Tree or the deep foundational bedrock. In-universe speculation abounds:
- Some believe the Fifth Head is the living biological core of the Alpha Tree itself, communicating through resinous fluid vibrations.
- Others theorize that the seat is held by a dormant Sorrow Sovereign who entered a conditional truce with the first settlers.
- Chief of Staff Yeong simply ensures that a fresh cup of clean spring water is placed beside the empty, veiled chair every morning, and finds the cup empty every dusk.

### 4.4 The Veiled Forty-Two Councilors
The remaining forty-two councilors represent trade guild federations, agricultural syndicates, foundry cartels, and veteran fraternal orders. During plenary debates, they sit behind acoustic veils that distort their voices into low, resonant choral sighs. When a vote is called, each councilor places an iron, bronze, or obsidian coin into a central urn. Only Chief of Staff Yeong counts the coins, announces the outcome, and destroys the voting logs, preserving total anonymity.

---

## 5. Sovereign Archival Summary

The Council of Sighs is neither an enlightened utopia nor a wanton tyranny; it is an endurance machine. By balancing public figureheads who carry civic hope against faceless bureaucrats who enforce harsh survival mathematics, the Council ensures that Somnarak continues to stand against the crushing weight of the Weeping world.

---

**Document ID:** `SOMNARAK-CODEX-COUNCIL-001`  
**Registry Authority:** High Council Secretariat & Central Chancery  
**Classification:** Sovereign Archival Codex — Permanent Lore Standard
"""
    return content

def build_collector_md():
    box1 = make_box(71, "THE COLLECTOR BUREAU & MUNICIPAL DEBT ENFORCEMENT CODEX", [
        "Agency Name       : The Collector Bureau (Susim Jingsuguk)",
        "Jurisdiction      : Municipal Debt Recovery across All Zones",
        "Supreme Authority : The Second Head (The Hand of Debt)",
        "Operational Center: Zone C - Collector's Row & Central Vaults",
        "Debt Currencies   : Financial, Karmic, Soul, and Emotional Debt",
        "Enforcement Force : High Collectors, Bailiff Wardens, Trackers",
        "Classification    : Sovereign Judicial Codex - Class Alpha"
    ])

    box2 = make_box(71, "THE FOUR METAPHYSICAL DEBT CURRENCIES - JURISDICTION MATRIX", [
        "Currency 01: Material Han Marks (Capital & Resource Deficits)",
        "Currency 02: Karma Debt (Ancestral Sin, Unatoned Guilt, Blood)",
        "Currency 03: Soul Debt (Mortgaged Will, Psychic Fragmentation)",
        "Currency 04: Emotional Debt (Trauma, Broken Vows, Memory Rent)",
        "The Balance Scale : The Collector Scales (Susim-ui Jeoul)",
        "Terminal Remedy   : Complete Foreclosure & Echo-Core Harvest"
    ])

    content = f"""# The Collector Bureau & Municipal Debt Enforcement
## Metaphysical Jurisprudence across Financial, Karmic, Soul, and Emotional Liabilities

---

{box1}
## 1. Foundational Doctrine: Debt as Metaphysical Mass

In the sovereign metropolis of Somnarak, debt is not a mere accounting fiction, credit ledger, or legal abstraction; **debt is a physical and metaphysical reality with measurable mass, acoustic frequency, and gravitational weight**.

When a citizen borrows resources, takes food from municipal granaries, inherits ancestral land, or causes emotional trauma to a neighbor, they do not merely create a fiscal deficit—they draw upon the collective stability of the city. Because Somnarak is constructed directly over the weeping bedrock of Mugenhan, every unpaid obligation generates localized structural stress.

The Collector Bureau (수심 징수국 — Susim Jingsuguk), headquartered along the grim, stone-paved avenue of **Collector's Row in Zone C**, is the sovereign wing chartered by the High Council of Sighs to locate, quantify, and extract debt in all its manifestations before unpaid weight can collapse the city into The Maw.

> *"The ledger does not forgive because the stone does not forgive. If your family borrowed three sacks of grain during the long winter, the earth remembers the hunger, and the earth will have its payment in silver, in labor, or in blood."*  
> — Sector Head Miran, Address to Apprentice Scribes

---

## 2. The Four Metaphysical Debt Currencies

{box2}
The fundamental law enforced by the Collector Bureau recognizes four distinct, convertible debt currencies. While common street money-lenders deal only in copper marks, certified Municipal Collectors are trained to audit and extract all four layers:

### 2.1 Currency 01: Material Han Marks (재물 부채 — Jaemul Buchae)
- **Nature:** The tangible civic currency of Somnarak—struck in Han-copper, silver slag, and compressed coal tokens.
- **Sources:** Housing rent in Zone A and C, agricultural leases, water ration vouchers, municipal utility fees, and commercial guild loans.
- **Amortization:** Paid through standard economic activity, industrial manufacturing, or agricultural labor.
- **Risk Level:** Low. If a citizen falls delinquent solely in material marks, their furniture, tools, and housing allocations are repossessed through standard bailiff action.

### 2.2 Currency 02: Karma Debt (업보 부채 — Eopbo Buchae)
- **Nature:** Trans-generational and ethical liability. When an individual commits murder, commits betrayal, or causes another citizen to suffer irreversible Fracture, the resulting grief stains the spiritual fabric of their family lineage.
- **Hereditary Transmission:** Karma Debt cannot be discharged by death. If a debtor dies with unatoned guilt, the liability automatically transfers to their children, grandchildren, and living kin.
- **Physical Manifestation:** High Karma Debt produces physical symptoms: localized temperature drops, chronic heaviness in the limbs, and an acoustic aura of 380 Hz that attracts roaming Sorrow Entities.
- **Extraction Protocol:** Paid through high-risk civic sacrifice—such as volunteering for hazardous perimeter defense in Zone E, serving on deep subterranean dredging crews, or submitting to the cleansing rites of the Katharcheok operations.

### 2.3 Currency 03: Soul Debt (영혼 부채 — Yeonghon Buchae)
- **Nature:** The hypothecation of personal psychic coherence and autonomous will.
- **Genesis:** Citizens undergoing catastrophic financial or medical crises frequently pledge portions of their consciousness to corporate wings or the Council of Sighs in exchange for emergency life-support or containment shielding.
- **Mechanics:** The Collector Bureau places an invisible "Lien on the Will." The debtor retains daily autonomy, but their nervous system is bound to municipal priority override. During civil emergencies or Ordeal surges, the Council can issue a psychic mobilization command, instantly commandeering the debtor's body as an expendable frontline combatant.
- **Terminal Default:** If a Soul Debt enters irrecoverable default, the Bureau executes a **Full Core Foreclosure**. The debtor's physical vessel is dismantled, and their remaining conscious spark is refined into an Echo-Core to power municipal machinery.

### 2.4 Currency 04: Emotional & Memory Debt (정동 및 기억 부채 — Jeongdong Buchae)
The most insidious and pervasive form of liability in Somnarak, divided into three specialized categories:
- **Ancestral Trauma Debt:** The lingering terror, grief, and despair of ancestors who died during the Cheongula sacrifice or the Occlusihan War. Offspring carry this trauma in their bone marrow, leading to spontaneous nightmares and emotional paralysis.
- **Broken Vow Debt:** Oaths sworn upon copper coins, sacred tree resin, or blood that were left unfulfilled. A broken promise curdles into an internal parasite (such as `SE-N-IIIβ-1056 The Unbroken Pledge`), physically tightening around the oath-breaker's throat until restitution is paid.
- **Memory Debt:** Citizens who rent fond memories (childhood comfort, maternal warmth, victories) from the Memory Archive must pay continuous monthly interest. If they fail to return the memory token on schedule, the Archive and the Collector Bureau apply compound interest, forcibly confiscating two of the borrower's own authentic memories for every rented one in arrears.

---

## 3. Instrumentation: The Collector Scales (수심의 저울)

The primary judicial instrument utilized by the Bureau is the **Collector Scale (수심의 저울 — Susim-ui Jeoul)**. 

### Mechanical & Resonant Operation
- **Construction:** Forged from cold-cast basalt and hung with pans of unrefined silver-Han alloy. The balance beam is calibrated to resonate at exactly 432 Hz.
- **Weighing Procedure:** The debtor places their right hand upon the left pan while reciting their full civil registry lineage. Upon the right pan, the Collector Scribe places calibrated lead counter-weights representing material marks, blood marks, and broken contracts.
- **The Telemetric Verdict:**
  * **Level Balance:** The citizen is in civic equilibrium; no immediate foreclosure is authorized.
  * **Downward Deflection (10–30 Degrees):** The debtor carries Moderate Debt; wage garnishment and mandatory labor shifts are imposed.
  * **Severe Deflection (31–75 Degrees):** The debtor carries Critical Karmic Burden; immediate asset seizure and family indenture contracts are enacted.
  * **Sudden Plunge (Total Collapse to Base):** The debtor carries Terminal Soul Insolvency; the pan slams into the stone table with the force of an anvil. The individual's citizen rights are extinguished on the spot.

---

## 4. Enforcement Hierarchy & Operational Units

{box2}

### 4.1 High Collector Scribes (상급 징수 서기)
The judicial officers of Zone C. Wearing voluminous ink-black coats and brass spectacles, Scribes conduct mathematical debt audits. They carry the Great Ledger of Zone C, bound in cured leather and inscribed with waterproof cinnabar ink. Scribes hold executive authority to sign foreclosure warrants and modify interest schedules.

### 4.2 Bailiff Wardens (집행 간수)
The kinetic enforcement arm of the Bureau. Heavily armored in reinforced basalt-fiber coats and carrying hydraulic crowbars, stun mauls, and manacles, Bailiff Wardens execute physical property seizures, evict delinquent tenants, and secure indentured workers for transfer to industrial complexes.

### 4.3 Debt Hounds & Repossession Trackers (부채 추적견)
Specialized operatives accompanied by cybernetic-canine constructs or trained Sorrow-sensitive hounds. These hounds do not track human scent; they track the distinct acoustic vibration of unfulfilled guilt. When a debtor flees into the slums of Zone B or the labyrinths of Zone D, the Debt Hounds track their acoustic trail through the sewer mains, running them down with relentless endurance.

---

## 5. The Four Foreclosure Tiers (체납 처분 4단계)

When a debtor cannot satisfy their obligations through voluntary payment, the Collector Bureau enforces a strict, four-stage foreclosure escalation:

| Foreclosure Tier | Official Classification | Enforcement Actions & Consequences |
|---|---|---|
| **Tier I: Fiscal Garnishment** | Standard Delinquency | 50% garnishment of daily wages; confiscation of excess grain rations; revocation of Zone A transit passes. |
| **Tier II: Indentured Wardenship** | Structural Default | Debtor is forcibly drafted into three to ten years of hazardous labor (Zone E blast wall repair, subterranean dredging, Facility 01 lower sanitation). |
| **Tier III: Memory Foreclosure** | Metaphysical Insolvency | Memory Archive technicians extract the debtor's cherished memories (wedding days, first love, artistic talent), selling them to affluent buyers to offset the ledger balance. |
| **Tier IV: Terminal Extraction** | Complete Soul Liquidation | Total civic forfeiture. The debtor's physical vessel is rendered into industrial Han dust, and their psychic core is processed into an Echo-Core for municipal power generators. |

---

## 6. The Hand of Debt's Sovereign Mandate

The Collector Bureau operates with the terrifying realization that without its ruthless bookkeeping, Somnarak would have drowned under its own emotional weight millennia ago. Every coin extracted, every memory repossessed, and every indentured hour worked is a structural wedge driven beneath the sinking city, holding the floor stable for another dawn.

---

**Document ID:** `SOMNARAK-CODEX-COLLECTOR-001`  
**Registry Authority:** The Collector Bureau Central Chancery & Zone C Administration  
**Classification:** Sovereign Judicial Codex — Permanent In-Universe Law Standard
"""
    return content

if __name__ == "__main__":
    c1 = build_council_md()
    with open("SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_COUNCIL_OF_SIGHS.md", "w", encoding="utf-8") as f:
        f.write(c1)
    print("Successfully wrote SOMNARAK_COUNCIL_OF_SIGHS.md")

    c2 = build_collector_md()
    with open("SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_COLLECTOR_BUREAU.md", "w", encoding="utf-8") as f:
        f.write(c2)
    print("Successfully wrote SOMNARAK_COLLECTOR_BUREAU.md")
