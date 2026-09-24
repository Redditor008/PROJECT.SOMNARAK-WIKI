import textwrap

# Read the script data with exact LRC timestamps and fully individualized Sorrow Entity action directions
scenes = [
    {
        "title": "SCENE 1 (0:00 - 0:31) // INTRO & VERSE 1",
        "rows": [
            ("[0:00 - 0:06] .", "Intro jazz piano hits: black silhouette of The Absolvohan; red indicator bulbs flicker on one by one in the dark."),
            ("[0:06 - 0:12] ..", "Upright bass enters: rapid cuts of containment iris valves locking; warning klaxons spinning in sync with snaps."),
            ("[0:12 - 0:19] ...", "Snare rolls: SE-C-IIIγ-102 (The Dancing Chains) slithers out from subterranean grates, dragging bloody rusted links."),
            ("[0:19] It’s quite rambunctious — Bam bii na bam bii na", "VOCAL ENTRY: SE-C-IIIγ-102 violently whips across the screen, chains lashing in sync with the brass stabs!"),
            ("[0:22] In the indiff-diff-different dance hall", "SE-C-IIIγ-021 (The Hollow Choir) stands on rusted choral risers, singing empty notes into the silent chamber."),
            ("[0:24] Stomp your feet", "SE-C-IIIγ-105 (The Lonely Giant) slams a colossal foot down, splashing Han-brine across the floor on the snare!"),
            ("[0:25] Come over here — Bam bii no bam bii no", "SE-C-IIIγ-140 (The Weeping Willow) whips pale branches forward, dragging an Absolver into the dark shadows."),
            ("[0:28] Whose blood was that again?", "SE-C-IIIβ-014 (The Debt Eater) tears into a fallen carcass, blood dripping from its jaw as it stares at the camera.")
        ]
    },
    {
        "title": "SCENE 2 (0:32 - 0:43) // VERSE 2",
        "rows": [
            ("[0:32] Breathe in, breathe out, swallow it up", "SE-C-IVω-001 (The Maw) splits the floor wide open, inhaling whole corridors of debris in one titanic gulp!"),
            ("[0:34] Where are your eyes peeking at?", "SE-C-IIIγ-031 (The Observing Bird) stares with giant yellow unblinking eyes through ceiling observation grates."),
            ("[0:38] Stick a gun to the peaceful clock’s second hand", "SE-C-IIIγ-044 (The Broken Clock) spins erratically; an operative rams a M.A.W. gun barrel into its brass gear face."),
            ("[0:40] Here’s a naive song", "SE-N-IIγ-903 (The Music Box of Agony) spins a naive ceramic dancer leaking black salt crystals from its dress.")
        ]
    },
    {
        "title": "SCENE 3 (0:44 - 0:58) // PRE-CHORUS",
        "rows": [
            ("[0:44] Spit out the dead’s message", "SE-N-IIIβ-247 (The Undelivered Thanks) spews burning suicide letters and unread wills from wall vents."),
            ("[0:45] The closing performance & (and) last page", "SE-N-IVδ-902 (The Repeated Survivor) tears out the last page of the 1,778 cycle loop record in desperation."),
            ("[0:47] A drug you can no longer get enough of", "SE-C-IIIγ-088 (The Sorrow Fountain) gushes luminescent blue brine; exhausted operatives drink frantically."),
            ("[0:48] The abandoned goddess’s rampage", "SE-N-IVδ-901 (The Mewgical Girl) undergoes wrath metamorphosis, roaring in blinding pink catastrophic fury."),
            ("[0:50] Sentimentality is a mountain of rubbish — You only have one life", "SE-C-IIIγ-081 (The Hollow Saint) floats serenely above a massive heap of corpses and shattered prayer charms.")
        ]
    },
    {
        "title": "SCENE 4 (0:59 - 1:28) // CHORUS 1 (THE DROP)",
        "rows": [
            ("[0:59] Unhappy", "SE-C-IIIβ-275 (Rage Forge) detonates with an explosion of white-hot slag across the containment corridor."),
            ("[1:00] Round round — The party ain’t gonna stop", "THE DROP: 360-degree rotational camera spin on the 10-node grid as 5 Sorrow Entities breach simultaneously!"),
            ("[1:01] Sins, lies, evading the law — fluttered about the space", "SE-C-IVδ-251 (The Unspoken Line) slices across room, severing ledgers, veils, and contracts like black confetti."),
            ("[1:04] Leave love behind — and let’s dance more on delusion’s stage", "Absolver in Resonant Alloy M.A.W. clashes in a frantic kinetic duel against charging breaching entities."),
            ("[1:10] Slowly mingle our sighs — I want to lose myself in the absurd sounds and rhythm", "SE-C-IIIγ-021 and SE-N-IIγ-903 harmonize into an overpowering acoustic frequency of despair and disorientation."),
            ("[1:17] Sink into captivation’s daydream underground", "SE-948 (YANG River Flood) bursts containment, washing operatives into glowing rapids of iridescent Han-energy."),
            ("[1:19] .", "SE-C-IIIγ-032 (The Weighting Bird) tilts its black balance scale downward in absolute silence."),
            ("[1:22] Let me forget about it", "Operative falls backward with a vacant grin as a massive Grudge shockwave blows out the corridor lights.")
        ]
    },
    {
        "title": "SCENE 5 (1:29 - 2:04) // VERSE 3",
        "rows": [
            ("[1:29] You’re rather gloomy — Bam bii naa bam bii na", "SE-N-IVγ-250 (The Extinguished) sits motionless in a corner, blowing cold ash at terrified passersby."),
            ("[1:32] Hey hey hey — I can’t hear ya", "SE-C-IIIγ-033 (The Guarding Bird) shrieks an ear-splitting defensive siren, shattering operative visors."),
            ("[1:35] Cry for me — Bam bii no bam bii no", "SE-C-IIIγ-019 (The Weeping Weaver) spins threads of crystallized tears, sewing fallen operatives' mouths shut."),
            ("[1:38] Where did I put your reward again?", "SE-C-IIIγ-061 (The Debtor) opens empty palms, dropping counterfeit brass coins into stagnant salt brine."),
            ("[1:40] .", "Quiet pause: camera pans down a flooded containment staircase lined with rusted chains and floating masks."),
            ("[1:41] Campanella — The metropolis' night is looking down on us and laughing", "SE-O-IIIγ-1052 (The Glass Silt Drifter) gazes up through silos toward Somnarak City's cold, mocking skyscrapers."),
            ("[1:48] Long ago, everyone wore unsightly masks", "SE-C-IIIγ-195 (Mirror of Sorrows) reflects distorted faces wearing grotesque animal masks and hollow grins."),
            ("[1:53] If you nurture love with karma’s tears", "SE-941 (Grieving Love) coils tightly around an operative, weeping translucent blue saline down their armor."),
            ("[1:59] All that’s left to do is drown", "SE-949 (YIN and YANG Sovereign) collides in corridor, inundating the sector in apocalyptic black-white waves.")
        ]
    },
    {
        "title": "SCENE 6 (2:05 - 2:50) // CHORUS 2",
        "rows": [
            ("[2:05] Unhappy", "SE-N-Vω-1055 (The Ancestral Guilt) rises from the deep stratum, radiating crushing Void pressure."),
            ("[2:07] Crown crown — a nuisance of a pre-established harmony", "The Sovereign Entity manifests an immense crown of jagged white salt crystals floating over its head."),
            ("[2:08] Philos, agape, and eros swiftly died out", "Three operatives collapse simultaneously, their M.A.W. resonance links snapping like brittle glass."),
            ("[2:11] I want to make destiny’s lifespan dissolve even more — but it’s out of arm’s reach", "Absolver lunges forward with M.A.W. spear, reaching for the entity's core but falling inches short."),
            ("[2:17] Don’t close your lonely eyes — I want to display your worst expression and the worst scenery", "Macro extreme close-up: operative's pupil reflecting the entire containment facility burning in white flames."),
            ("[2:23] I don’t need any normal mannequin, underground", "SE-C-IIIγ-190 (The Rage Statue) stands surrounded by defeated Absolvers petrified into white salt statues."),
            ("[2:27] .", "A single droplet of caustic salt brine hangs suspended in mid-air in super slow-motion."),
            ("[2:35] ..", "The droplet impacts stone, sending acoustic fracture lines spreading across the entire screen."),
            ("[2:45] ...", "SE-N-IVδ-902 (The Repeated Survivor) steps forward among the petrified statues, coat torn and smoking.")
        ]
    },
    {
        "title": "SCENE 7 (2:51 - 3:17) // BRIDGE",
        "rows": [
            ("[2:51] .", "Dead silence. Black frame with faint mechanical ticking echoing in the darkness."),
            ("[2:52] ..", "A cold white spotlight snaps on from directly overhead, cutting through swirling dust."),
            ("[2:53] ...", "Operative sits alone on a rusted chair, clutching a cracked glass photograph with trembling hands."),
            ("[2:54] .", "A match strikes: the flame slowly consumes the faces of their dead comrades in the photograph."),
            ("[2:55] Let’s erase happiness so it won’t yield misfortune", "Dropping the burning photo into an ash bin; smoke forms the weeping silhouette of a Sorrow Entity."),
            ("[2:57] .", "The operative rises, their M.A.W. mantle trailing gray ashes across the cold slate floor."),
            ("[2:58] .", "Flerehan weeping: sudden violent tremors shake room as sound waves warp containment walls."),
            ("[2:59] When we wailed aloud — What were we hoping for?", "Shadowy apparitions of past cycle casualties emerge from the walls, reaching out in desperate sorrow."),
            ("[3:03] .", "The operative sinks to knees, gloved fists shattering on the slate floor as tears spill."),
            ("[3:05] .", "The walls of The Absolvohan weep caustic brine like bleeding open wounds."),
            ("[3:06] Even if I hugged you with all my might", "Operative embraces partner's salt statue; the body crumbles into loose white dust in their arms."),
            ("[3:09] .", "White salt sand streams through their fingers, blown away by a cold subterranean gale."),
            ("[3:12] .", "Operative raises head: completely hollow, dead eyes devoid of fear, sorrow, or hope."),
            ("[3:15] You only have one life", "Standing up slowly, locking their M.A.W. weapon into place with chilling, resolute finality.")
        ]
    },
    {
        "title": "SCENE 8 (3:18 - 4:16) // GRAND FINALE (MELTDOWN CLIMAX)",
        "rows": [
            ("[3:18] ..", "Pounding bass buildup; warning klaxons scream in rapid red-and-white strobe rhythm."),
            ("[3:19] .", "FULL MELTDOWN REVEAL: All 10 Floor Secretaries appear in traumatic Echo-Core Realization!"),
            ("[3:20] Unhappy round round — The party ain’t gonna stop", "Secretaries 01 to 10 in full distorted Core Meltdown, laughing and weeping in chaotic harmony!"),
            ("[3:21] Sins,", "Floor 07 & 08 Secretaries unleash apocalyptic resonance waves; entities surge through breaches!"),
            ("[3:23] Lies, Evading the law — fluttered about the space", "The Dekan in Sovereign Meltdown conducts the catastrophe with his baton, surrounded by fire!"),
            ("[3:24] Leave love behind — and let’s dance more on delusion’s stage", "The operative charges straight into the eye of the storm, slashing through breaching entities!"),
            ("[3:30] Slowly mingle our sighs — I want to lose myself in the absurd sounds and rhythm", "High-speed 24fps clash: dodging Meltdown attacks, mirroring the madness in a frantic waltz!"),
            ("[3:36] Sink into captivation’s daydream underground", "A titanic shockwave shatters the bedrock; the entire facility plunges into the glowing Echo-Core!"),
            ("[3:41] Let me forget about it", "Sudden dead silence. The operative sits alone on a throne of salt in the dark, smiling as the loop resets.")
        ]
    }
]

c1_w = 88
c2_w = 100
tot_w = c1_w + c2_w + 1

top_border = "+" + "-" * (tot_w - 2) + "+"
double_sep = "+" + "=" * (c1_w - 1) + "+" + "=" * (c2_w - 1) + "+"
single_sep = "+" + "-" * (c1_w - 1) + "+" + "-" * (c2_w - 1) + "+"

def pad_c(s, w):
    if len(s) < w:
        return s + " " * (w - len(s))
    return s[:w]

out_lines = []

for sc in scenes:
    out_lines.append(top_border)
    sc_clean = f" {sc['title']} "
    diff = (tot_w - 2) - len(sc_clean)
    l_pad = diff // 2
    r_pad = diff - l_pad
    out_lines.append("|" + " " * l_pad + sc_clean + " " * r_pad + "|")
    out_lines.append(double_sep)
    
    for left, right in sc["rows"]:
        l_wrapped = textwrap.wrap(left, width=c1_w - 3) or [""]
        r_wrapped = textwrap.wrap(right, width=c2_w - 3) or [""]
        n_lines = max(len(l_wrapped), len(r_wrapped))
        
        for i in range(n_lines):
            l_str = l_wrapped[i] if i < len(l_wrapped) else ""
            r_str = r_wrapped[i] if i < len(r_wrapped) else ""
            out_lines.append(f"| {pad_c(l_str, c1_w - 3)} | {pad_c(r_str, c2_w - 3)} |")
        out_lines.append(single_sep)

full_table = "\n".join(out_lines)

target_path = "TRYOUT,SANDBOX/PROJECT.SOMNARAK-Animatic-Text.txt"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(full_table + "\n")

print("Generated clean wrapped table successfully!")
