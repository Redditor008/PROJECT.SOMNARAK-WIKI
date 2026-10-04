#!/usr/bin/env python3
"""
tools/repairs_and_patches/upgrade_consequences_vocab.py
================================================================================
PROJECT SOMNARAK — CONSEQUENCES VOCABULARY UPGRADE & SPLICE CLEANSE
================================================================================
Replaces generic template splices in the '### Consequences' sections of
all 244 affected Sorrow Entity dossiers with high-density, grammatically sound,
and lore-rich canonical prose.
================================================================================
"""

import glob
import re
import os

def upgrade_file_content(txt):
    orig = txt
    
    # --- BULLET 1 UPGRADES ---
    txt = re.sub(
        r"- A worker who cannot hold against the entity['’]s sorrow becomes a conduit — pressure flows through them and back into the gauge\.\s+\*\*([A-Za-z]+)\*\*\s+and\s+may\s+increase\s+the\s+Sorrow\s+Gauge\.",
        r"- A worker who cannot hold against the entity’s sorrow becomes a conduit: raw pressure severely erodes their **\1**, funneling cognitive instability back into the Sorrow Gauge.",
        txt
    )
    txt = re.sub(
        r"- Personnel who fail to resist the entity['’]s pressure take damage to their composure and identity — and the gauge rises in response\.\s+\*\*([A-Za-z]+)\*\*\s+and\s+may\s+increase\s+the\s+Sorrow\s+Gauge\.",
        r"- Personnel who fail to resist the entity’s pressure suffer severe degradation of their **\1** and identity cohesion, accelerating Sorrow Gauge escalation.",
        txt
    )
    txt = re.sub(
        r"- Failed resistance is a double loss: the worker takes the sorrow['’]s full weight, and the entity absorbs their destabilisation\.\s+\*\*([A-Za-z]+)\*\*\s+and\s+may\s+increase\s+the\s+Sorrow\s+Gauge\.",
        r"- Failed resistance is a double loss: the worker absorbs raw sorrow pressure that breaks their **\1**, while the entity feeds on their psychological destabilization to escalate the Sorrow Gauge.",
        txt
    )
    txt = re.sub(
        r"- If resistance fails, the entity['’]s pressure transfers to the worker['’]s composure and the gauge reflects the exchange\.\s+\*\*([A-Za-z]+)\*\*\s+and\s+may\s+increase\s+the\s+Sorrow\s+Gauge\.",
        r"- If resistance fails, the entity’s pressure transfers directly into the worker’s psychological matrix, depleting **\1** and accelerating Sorrow Gauge escalation.",
        txt
    )
    txt = re.sub(
        r"- Resistance failure channels the entity['’]s sorrow directly into the worker, damaging stability and feeding the gauge\.\s+\*\*([A-Za-z]+)\*\*\s+and\s+may\s+increase\s+the\s+Sorrow\s+Gauge\.",
        r"- Resistance failure channels the entity’s sorrow directly into the worker, destroying their **\1** and feeding the Sorrow Gauge.",
        txt
    )
    txt = re.sub(
        r"- When a worker breaks under the entity['’]s pressure, the gauge climbs and the worker Fractures — two failures for the price of one\.\s+\*\*([A-Za-z]+)\*\*\s+and\s+may\s+increase\s+the\s+Sorrow\s+Gauge\.",
        r"- When a worker breaks under the entity’s pressure, the Sorrow Gauge climbs while their **\1** shatters into a psychological Fracture—a catastrophic dual failure.",
        txt
    )
    
    # --- BULLET 2 UPGRADES ---
    txt = re.sub(
        r"- The entity['’]s documented effects intensify with duration\. What is manageable in a five-minute cycle becomes dangerous in fifteen\.\s+the entity[’']s documented emotional, physical, identity, or environmental effect\.",
        "- The entity’s documented effects intensify with duration: what is manageable in a brief cycle becomes lethal over prolonged exposure, manifesting severe emotional, physical, identity, or environmental dissolution.",
        txt
    )
    txt = re.sub(
        r"- Extended contact risks the entity['’]s full documented effect — emotional erosion, physical damage, identity dissolution, or environmental corruption\.\s+the entity[’']s documented emotional, physical, identity, or environmental effect\.",
        "- Extended contact risks the entity’s full documented manifestation—inducing acute emotional erosion, somatic trauma, identity dissolution, or permanent environmental corruption.",
        txt
    )
    txt = re.sub(
        r"- Time is the entity['’]s ally\. Prolonged exposure allows the sorrow to accumulate in the worker, producing the effects the classification was written to prevent\.\s+the entity[’']s documented emotional, physical, identity, or environmental effect\.",
        "- Time is the entity’s ally: prolonged exposure allows sorrow saturation to accumulate within the operative, triggering the catastrophic psychological, somatic, or environmental collapse the classification was codified to prevent.",
        txt
    )
    txt = re.sub(
        r"- Extended exposure carries cumulative risk: each minute past the recommended cycle increases the probability of Fracture, identity drift, or environmental destabilisation\.\s+the entity[’']s documented emotional, physical, identity, or environmental effect\.",
        "- Extended exposure carries cumulative risk: each minute past the recommended cycle accelerates identity drift, cognitive Fracture, and acute environmental destabilization.",
        txt
    )
    txt = re.sub(
        r"- The longer the exposure, the deeper the effect: the entity['’]s sorrow seeps past protocol and into the worker['’]s own psychology\.\s+the entity[’']s documented emotional, physical, identity, or environmental effect\.",
        "- The longer the exposure, the deeper the wound: the entity’s sorrow seeps past containment protocol and permeates the operative’s cognition, inducing irreversible emotional, somatic, and identity breakdown.",
        txt
    )
    txt = re.sub(
        r"- Sustained proximity activates the entity['’]s secondary effects — the ones the short-cycle file warns about but the field rarely sees until too late\.\s+the entity[’']s documented emotional, physical, identity, or environmental effect\.",
        "- Sustained proximity triggers the entity’s latent secondary effects—the subtle hazards that short-cycle briefings warn against, resulting in severe cognitive erosion, somatic distortion, and environmental taint.",
        txt
    )

    # --- BULLET 3 UPGRADES ---
    txt = re.sub(
        r"- Each M\.A\.W\. use debits the wielder — in composure, in memory, in something the grade does not measure\.\s+recorded in the equipment section\.",
        "- Each M.A.W. activation exacts a personal debit from the wielder—eroding composure, personal memories, and somatic vitality beyond what standard grade ledgers can record.",
        txt
    )
    txt = re.sub(
        r"- Every M\.A\.W\. activation extracts a price from the wielder — memories, sensation, years — listed in the equipment section but felt in the field\.\s+recorded in the equipment section\.",
        "- Every M.A.W. activation extracts a profound price from the wielder—intimate memories, physical sensation, and years of life—documented in equipment specifications and paid in the field.",
        txt
    )
    txt = re.sub(
        r"- M\.A\.W\. activation is an exchange: power for price\. The cost is recorded; the payment is personal\.\s+recorded in the equipment section\.",
        "- M.A.W. activation is an unyielding exchange: power for price. While parameters are formally cataloged in the equipment registry, the payment is extracted directly from the bearer’s soul and flesh.",
        txt
    )
    txt = re.sub(
        r"- The equipment section lists what the M\.A\.W\. takes\. The field confirms it\. There is no free extraction\.\s+recorded in the equipment section\.",
        "- The equipment section documents what the M.A.W. extracts; field combat confirms it without exception. There is no costless extraction in Somnarak.",
        txt
    )
    txt = re.sub(
        r"- The M\.A\.W\. is not free\. Its cost — physical, psychological, or temporal — is documented but unavoidable\.\s+recorded in the equipment section\.",
        "- The M.A.W. is never costless: its somatic, psychological, and mnemonic toll is formally codified in equipment records and exacted with every swing.",
        txt
    )
    txt = re.sub(
        r"- Wielding a M\.A\.W\. means accepting the toll: the entity['’]s sorrow flows backward through the equipment into the user\.\s+recorded in the equipment section\.",
        "- Wielding a M.A.W. requires accepting its resonance toll: the entity’s crystallized sorrow flows backward through the weapon into the bearer, extracting the price documented in the armory ledger.",
        txt
    )

    # --- BULLET 4 UPGRADES ---
    txt = re.sub(
        r"- Without resolution the sorrow does not dissipate; it breaches\. The entity follows the escalation recorded in its file;\s+the entity follows its breach, activation, or expansion behavior\.",
        "- Without containment resolution the sorrow never dissipates; it ruptures outward, initiating the escalation and breach behaviors recorded in its dossier.",
        txt
    )
    txt = re.sub(
        r"- Without resolution, the entity defaults to its documented breach, activation, or expansion behavior — the sorrow finds its own outlet;\s+the entity follows its breach, activation, or expansion behavior\.",
        "- Without timely resolution, the entity defaults to its documented breach, activation, or expansion behavior—denied containment, the unchanneled grief carves its own catastrophic outlet.",
        txt
    )
    txt = re.sub(
        r"- An unresolved encounter does not end; it transforms\. The entity follows its breach pattern, and the sorrow finds the exit the work could not provide;\s+the entity follows its breach, activation, or expansion behavior\.",
        "- An unresolved encounter never simply ends; it transforms. The entity executes its documented breach pattern, and the unpacified sorrow forces the violent exit that containment work failed to provide.",
        txt
    )
    txt = re.sub(
        r"- If the condition is not met, the entity reverts to its activation behavior — the sorrow, denied its resolution, seeks its own;\s+the entity follows its breach, activation, or expansion behavior\.",
        "- If the resolution condition is not fulfilled, the entity reverts to its destructive activation protocol—denied peace, the sorrow aggressively seeks its own release.",
        txt
    )
    txt = re.sub(
        r"- Failure to resolve means the entity follows its breach protocol: the gauge climbs, the protocols engage, and the sorrow acts;\s+the entity follows its breach, activation, or expansion behavior\.",
        "- Failure to achieve resolution triggers the entity’s breach protocol: the Sorrow Gauge peaks, containment fail-safes collapse, and the sorrow breaches outward into facility corridors.",
        txt
    )
    txt = re.sub(
        r"- When resolution fails, the entity['’]s containment story continues on its own terms — through breach, expansion, or the documented escalation;\s+the entity follows its breach, activation, or expansion behavior\.",
        "- When resolution fails, the entity’s narrative continues on its own catastrophic terms—manifesting through containment breach, territorial expansion, and rapid escalation.",
        txt
    )

    return txt, txt != orig

def main():
    files = sorted(glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True))
    modified_count = 0
    
    for f in files:
        if f.endswith("README.md"):
            continue
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        
        new_content, changed = upgrade_file_content(content)
        if changed:
            with open(f, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            modified_count += 1

    print(f"Successfully upgraded Consequences vocabulary in {modified_count} files!")

if __name__ == "__main__":
    main()
