import sys

# Script data focusing 80% on Sorrow Entities corresponding to lyrics,
# reserving Floor Secretaries for the Meltdown climax at the end!
script_data = {
    "SCENE 1": [
        ("It’s quite rambunctious — Bam bii na bam bii na", "SE-C-IIIγ-102 (The Dancing Chains) violently whips through corridors like a feral dancer."),
        ("Stomp your feet", "SE-C-IIIγ-105 (The Lonely Giant) stomps colossal iron-bound feet, shaking the floor."),
        ("In the indiff-diff-different dance hall", "SE-C-IIIγ-021 (The Hollow Choir) stands on risers in the dark, singing hollow notes."),
        ("Come over here — Bam bii no bam bii no", "SE-C-IIIγ-140 (The Weeping Willow) stretches pale weeping branches to drag an Absolver in."),
        ("Whose blood was that again?", "SE-C-IIIβ-014 (The Debt Eater) tears into a fallen carcass, blood dripping from its jaws.")
    ],
    "SCENE 2": [
        ("Breathe in, breathe out, swallow it up", "SE-C-IVω-001 (The Maw) yawns open its titanic maw in the floor, inhaling whole corridors."),
        ("Where are your eyes peeking at?", "SE-C-IIIγ-031 (The Observing Bird) stares with giant yellow eyes through ceiling grates."),
        ("Stick a gun to the peaceful clock’s second hand", "SE-C-IIIγ-044 (The Broken Clock) spins backward; an operative aims a sidearm at its face."),
        ("Here’s a naive song", "SE-N-IIγ-903 (The Music Box of Agony) spins a childish ceramic dancer leaking black salt.")
    ],
    "SCENE 3": [
        ("Spit out the dead’s message", "SE-N-IIIβ-247 (The Undelivered Thanks) spews burning suicide letters and wills from wall vents."),
        ("The closing performance & (and) last page", "SE-N-IVδ-902 (The Repeated Survivor) tears out the last page of the 1,778 loop ledger."),
        ("A drug you can no longer get enough of", "SE-C-IIIγ-088 (The Sorrow Fountain) gushes luminescent blue brine; operatives drink frantically."),
        ("The abandoned goddess’s rampage", "SE-N-IVδ-901 (The Mewgical Girl) undergoes wrath metamorphosis, roaring in blinding pink-white fury."),
        ("Sentimentality is a mountain of rubbish — You only have one life", "SE-C-IIIγ-081 (The Hollow Saint) floats above a massive heap of discarded corpses and charms.")
    ],
    "SCENE 4": [
        ("Unhappy", "SE-C-IIIβ-275 (Rage Forge) detonates with an explosion of white-hot slag across the screen."),
        ("Round round — The party ain’t gonna stop", "360-degree rotational spin around the 10-node grid as 5 Sorrow Entities breach simultaneously."),
        ("Sins, lies, evading the law — fluttered about the space", "SE-C-IVδ-251 (The Unspoken Line) slices across the room, severing ledgers and veils like confetti."),
        ("Leave love behind — and let’s dance more on delusion’s stage", "An Absolver in Resonant Alloy M.A.W. clashes in a frantic kinetic duel against breaching beasts."),
        ("Slowly mingle our sighs — I want to lose myself in the absurd sounds and rhythm", "SE-C-IIIγ-021 and SE-N-IIγ-903 harmonize into an overpowering acoustic frequency of despair."),
        ("Sink into captivation’s daydream underground", "SE-948 (YANG River Flood) bursts containment, washing operatives into glowing subterranean rapids."),
        (".", "SE-C-IIIγ-032 (The Weighting Bird) tilts its black balance scale downward in absolute silence."),
        ("Let me forget about it", "Operative falls backward with a vacant grin as a massive Grudge shockwave blows out the lights.")
    ],
    "SCENE 5": [
        ("You’re rather gloomy — Bam bii naa bam bii na", "SE-N-IVγ-250 (The Extinguished) sits motionless in a corner, blowing cold ash at passersby."),
        ("Hey hey hey — I can’t hear ya", "SE-C-IIIγ-033 (The Guarding Bird) shrieks an ear-splitting defensive siren, shattering visors."),
        ("Cry for me — Bam bii no bam bii no", "SE-C-IIIγ-019 (The Weeping Weaver) spins threads of crystallized tears, sewing mouths shut."),
        ("Where did I put your reward again?", "SE-C-IIIγ-061 (The Debtor) opens empty palms, dropping counterfeit brass coins into salt brine."),
        (".", "Quiet pause: camera pans down a flooded containment staircase lined with rusted chains."),
        ("Campanella — The metropolis' night is looking down on us and laughing", "SE-O-IIIγ-1052 (The Glass Silt Drifter) gazes up through silos toward Somnarak City's cold lights."),
        ("Long ago, everyone wore unsightly masks", "SE-C-IIIγ-195 (Mirror of Sorrows) reflects distorted faces wearing grotesque animal masks."),
        ("If you nurture love with karma’s tears", "SE-941 (Grieving Love) coils tightly around an operative, weeping translucent blue saline."),
        ("All that’s left to do is drown", "SE-949 (YIN and YANG Sovereign) collides in the corridor, inundating the sector in black-white waves.")
    ],
    "SCENE 6": [
        ("Unhappy", "SE-N-Vω-1055 (The Ancestral Guilt) rises in the deep stratum, radiating crushing Void pressure."),
        ("Crown crown — a nuisance of a pre-established harmony", "The Sovereign Entity manifests an immense crown of jagged white salt crystals over its head."),
        ("Philos, agape, and eros swiftly died out", "Three operatives collapse simultaneously, their M.A.W. resonance links snapping like harp strings."),
        ("I want to make destiny’s lifespan dissolve even more — but it’s out of arm’s reach", "A lone Absolver reaches desperately toward the Echo-Core pedestal, but is thrown back by wind."),
        ("Don’t close your lonely eyes — I want to display your worst expression and the worst scenery", "Macro extreme close-up: operative's pupil reflecting the entire containment facility in flames."),
        ("I don’t need any normal mannequin, underground", "SE-C-IIIγ-190 (The Rage Statue) stands surrounded by defeated Absolvers petrified into white salt statues."),
        (".", "A single droplet of caustic salt brine hangs suspended in mid-air in super slow-motion."),
        ("..", "The droplet impacts the stone, sending acoustic fracture lines spreading across the entire frame."),
        ("...", "SE-N-IVδ-902 (The Repeated Survivor) steps forward among the petrified statues, coat torn.")
    ],
    "SCENE 7": [
        (".", "Dead silence. Black frame with faint mechanical ticking."),
        ("..", "A cold white spotlight snaps on from directly overhead."),
        ("...", "Operative sits alone on a rusted chair, clutching a cracked glass photograph."),
        (".", "A match strikes: the flame consumes the faces of their dead comrades in the photograph."),
        ("Let’s erase happiness so it won’t yield misfortune", "Dropping the burning photo into an ash bin; smoke forms the weeping silhouette of an entity."),
        (".", "The operative rises, their M.A.W. mantle trailing gray ashes across the floor."),
        (".", "Sudden acoustic tremors: the entire room vibrates with subsonic Flerehan wailing."),
        ("When we wailed aloud — What were we hoping for?", "Shadowy apparitions of past cycle casualties emerge from the walls, reaching out in sorrow."),
        (".", "The operative sinks to their knees, gloved fists shattering on the slate floor."),
        (".", "The walls of The Absolvohan weep caustic brine like bleeding wounds."),
        ("Even if I hugged you with all my might", "Operative embraces the petrified salt corpse of their squad partner; the body crumbles to dust."),
        (".", "White salt sand streams through their fingers, blown away by a cold subterranean gale."),
        (".", "Operative raises their head: completely hollow, dead eyes devoid of fear, sorrow, or hope."),
        ("You only have one life", "Standing up slowly, locking their M.A.W. weapon into place with chilling finality.")
    ],
    "SCENE 8": [
        ("..", "Pounding bass buildup; warning klaxons scream in rapid red-and-white strobe rhythm."),
        (".", "FULL MELTDOWN REVEAL: All 10 Floor Secretaries appear in traumatic Echo-Core Realization!"),
        ("Unhappy round round — The party ain’t gonna stop", "Secretaries 01 to 10 in full distorted Core Meltdown, laughing and weeping in chaotic harmony!"),
        ("Sins,", "Floor 07 & 08 Secretaries unleash apocalyptic resonance waves; entities surge through breaches!"),
        ("Lies, Evading the law — fluttered about the space", "The Dekan in Sovereign Meltdown conducts the catastrophe with his baton, surrounded by fire!"),
        ("Leave love behind — and let’s dance more on delusion’s stage", "The operative charges straight into the eye of the storm, slashing through breaching entities!"),
        ("Slowly mingle our sighs — I want to lose myself in the absurd sounds and rhythm", "High-speed 24fps clash: dodging Meltdown attacks, mirroring the madness in a frantic waltz!"),
        ("Sink into captivation’s daydream underground", "A titanic shockwave shatters the bedrock; the entire facility plunges into the glowing Echo-Core!"),
        ("Let me forget about it", "Sudden dead silence. The operative sits alone on a throne of salt in the dark, smiling as the loop resets.")
    ]
}

c1_w = 94
c2_w = 95
tot_w = c1_w + c2_w + 1

top_border = "+" + "-" * (tot_w - 2) + "+"
double_sep = "+" + "=" * (c1_w - 1) + "+" + "=" * (c2_w - 1) + "+"
single_sep = "+" + "-" * (c1_w - 1) + "+" + "-" * (c2_w - 1) + "+"

def pad_c(s, w):
    if len(s) < w:
        return s + " " * (w - len(s))
    return s[:w]

out_lines = []

for sc_name, rows in script_data.items():
    out_lines.append(top_border)
    sc_clean = f" {sc_name} // REVERIE DIRECTORATE MAD ANIMATIC SCRIPT (ENTITY-FIRST) "
    diff = (tot_w - 2) - len(sc_clean)
    l_pad = diff // 2
    r_pad = diff - l_pad
    out_lines.append("|" + " " * l_pad + sc_clean + " " * r_pad + "|")
    out_lines.append(double_sep)
    
    for left, right in rows:
        l_padded = pad_c(left, c1_w - 3)
        r_padded = pad_c(right, c2_w - 3)
        out_lines.append(f"| {l_padded} | {r_padded} |")
        out_lines.append(single_sep)

full_table = "\n".join(out_lines)

target_path = "TRYOUT,SANDBOX/PROJECT.SOMNARAK-Animatic-Text.txt"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(full_table + "\n")

print("Updated PROJECT.SOMNARAK-Animatic-Text.txt with 80% Sorrow Entity showcases & Meltdown finale successfully!")
