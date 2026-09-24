import textwrap

scenes = [
    {
        "title": "SCENE 1 (0:00 - 0:31) // INTRO & VERSE 1",
        "rows": [
            ("[0:00 - 0:06] .", "Intro jazz piano hits: black silhouette of The Absolvohan; red indicator bulbs flicker on in the deep subterranean strata."),
            ("[0:06 - 0:12] ..", "Upright bass enters: rapid cuts of massive iris valves locking; warning klaxons spinning in sync with rhythmic snaps."),
            ("[0:12 - 0:19] ...", "Snare drum rolls build: floor grates rattle; cold dark crystalline links slither out from shadows, pulsing with an inner heartbeat."),
            ("[0:19] It’s quite rambunctious — Bam bii na bam bii na", "VOCAL ENTRY: SE-C-IIIγ-102 (The Dancing Chains) breaches! Dark crystallized chains glowing crimson lash across the screen using 'The Whip', forcing all present into a frenzied dance born from the forgotten cursed dancing shoes!"),
            ("[0:22] In the indiff-diff-different dance hall", "SE-C-IIIγ-021 (The Hollow Choir) manifests: 144 ethereal, faceless vocal phantoms filling rusted choral risers, their empty throat sockets singing 'The Swelling Chorus' in mournful Deep Blue harmony."),
            ("[0:24] Stomp your feet", "SE-C-IIIγ-105 (The Lonely Giant) executes 'The Heavy Step'! A twenty-meter titan of dark Han-crystal with hollow sorrowful eyes slams a colossal crystalline foot down, splashing Han-brine across the floor on the snare!"),
            ("[0:25] Come over here — Bam bii no bam bii no", "SE-C-IIIγ-140 (Weeping Willow) attacks: a massive ancient willow whose branches and leaves are made of crystallized tears drapes forward, using 'The Dripping Branches' to drag an Absolver into the dark."),
            ("[0:28] Whose blood was that again?", "SE-C-IIIβ-014 (The Debt Eater) tears into a carcass: a hunched one-meter humanoid with paper-like translucent skin and mouthless face absorbs debt through its clawed hands, bloody ledger pages spilling from its jaws.")
        ]
    },
    {
        "title": "SCENE 2 (0:32 - 0:43) // VERSE 2",
        "rows": [
            ("[0:32] Breathe in, breathe out, swallow it up", "SE-C-IVω-001 (The Maw) breaches, transforming from Place to Subject C-IVω-001-B! Inward-leaning buildings and tar-soft streets yawn open into an abyssal stone throat with 'The Whispering Walls' to inhale whole corridors!"),
            ("[0:34] Where are your eyes peeking at?", "SE-C-IIIγ-031 (The Observing Bird) stares down: an eagle-sized raptor covered in exactly 144 pale-yellow unblinking eyes locks its gaze through ceiling observation grates using 'The Unblinking Stare'."),
            ("[0:38] Stick a gun to the peaceful clock’s second hand", "SE-C-IIIγ-044 (Broken Clock) triggers 'The Stopped Hand'! A three-meter clock of crystallized time with erratically spinning brass hands; an operative rams a M.A.W. gun barrel into its glass face to force time forward."),
            ("[0:40] Here’s a naive song", "SE-C-IIβ-048 (The Singing Stone) hums 'The First Note'! A smooth dark river stone warm to the touch vibrates in sympathy, releasing luminous blue acoustic waves carrying forgotten naive lullabies.")
        ]
    },
    {
        "title": "SCENE 3 (0:44 - 0:58) // PRE-CHORUS",
        "rows": [
            ("[0:44] Spit out the dead’s message", "SE-C-Iα-114 (A Letter Never Sent) bursts its 'Indigo Seal'! A fire-sooted grey dispatch envelope sealed with weeping indigo wax explodes, spewing thousands of fluttering unread parchment wills from ventilation shafts."),
            ("[0:45] The closing performance & (and) last page", "SE-C-IIβ-906 (Grimoire) executes 'The Final Inscription'! A heavy leather-bound tome written by 'the rage that does not cool' violently flips its vellum pages as fresh black ink bleeds off the final execution record."),
            ("[0:47] A drug you can no longer get enough of", "SE-C-IIIγ-088 (The Sorrow Fountain) triggers 'The Welling'! An ornate stone basin overflowing with luminescent blue saline brine that reflects no face; exhausted Absolvers drink frantically to numb panic."),
            ("[0:48] The abandoned goddess’s rampage", "SE-C-IVβ-042 (The Angry Maiden) unleashes 'Mother’s Wrath'! A translucent young woman sculpted of roaring Crimson and orange fire shakes with rage before rampaging through the sector in an inferno."),
            ("[0:50] Sentimentality is a mountain of rubbish — You only have one life", "SE-C-IIIγ-081 (The Hollow Saint) casts 'The Empty Blessing'! An alabaster humanoid saint sculpted around a gaping negative chest void hovers serenely above a mountain of corpses and discarded prayer charms.")
        ]
    },
    {
        "title": "SCENE 4 (0:59 - 1:28) // CHORUS 1 (THE DROP)",
        "rows": [
            ("[0:59] Unhappy", "SE-C-IIIβ-275 (Crucible) detonates! A massive smith-less forge glowing with crimson heat triggers 'The Banked Coals', exploding in a shower of white-hot molten slag that breaches containment doors."),
            ("[1:00] Round round — The party ain’t gonna stop", "THE DROP: SE-C-IIβ-099 (The Masked Dancer) triggers 'The Endless Performance'! A graceful figure in a smiling lacquered mask leaking a single crystal tear twirls, 360-degree camera spin pulling 5 entities into a waltz!"),
            ("[1:01] Sins, lies, evading the law — fluttered about the space", "SE-C-IVδ-140 (Gavel), a towering iron judge with a crimson chest-scale, slams its hammer while SE-N-IIβ-319 (The Magistrate's Strike-Through) releases chalk-white dust, struck warrants fluttering like confetti."),
            ("[1:04] Leave love behind — and let’s dance more on delusion’s stage", "An elite Absolver in Resonant Alloy M.A.W. clashes in a high-speed kinetic duel across Grid Nodes 3, 5, and 8, trading furious steel blows against charging breaching beasts."),
            ("[1:10] Slowly mingle our sighs — I want to lose myself in the absurd sounds and rhythm", "SE-N-IVδ-157 (Torpor) exhales 'The Slow Exhale'! A vast dormant mass of heavy gray mist blankets the room, its leaden atmospheric pressure suffocating operatives in deep rhythmic fatigue."),
            ("[1:17] Sink into captivation’s daydream underground", "SE-C-IIIγ-948 (YANG River Flood) breaches! A stone-carved dragon with jet-black scales and glowing white eyes radiates contagious yearning, flooding corridors with rapids of iridescent Han-energy."),
            ("[1:19] .", "SE-C-IIIγ-032 (Weighting Bird) triggers 'The Tilted Scale'! An eagle-sized raptor whose eyes are miniature brass balance scales tilts its head, tipping the scale downward in heavy, ominous silence."),
            ("[1:22] Let me forget about it", "SE-C-IIIγ-928 (Lethe) releases its 'Void Mist Spill'! Dense creeping violet vapors roll over fallen operatives, dissolving memory and identity until they smile vacantly as lights extinguish.")
        ]
    },
    {
        "title": "SCENE 5 (1:29 - 2:04) // VERSE 3",
        "rows": [
            ("[1:29] You’re rather gloomy — Bam bii naa bam bii na", "SE-O-IVδ-515 (The Last Warmth of Forty-Two) manifests 'The Warm Rim'! A quartz vial wrapped in orange webbing releases swirling pale-blue glacial frost, while faint orange embers flicker around frozen silhouettes."),
            ("[1:32] Hey hey hey — I can’t hear ya", "SE-C-IIIγ-033 (The Guarding Bird) shrieks from 'The Guarded Perimeter'! A massive raptor with hard angular shield-wings shrieks a deafening alarm blast that shatters comms and visor glass."),
            ("[1:35] Cry for me — Bam bii no bam bii no", "SE-C-IVγ-009 (The Memory Weaver) weaves 'The First Thread'! A colossal crystal-socketed spider draws glistening silver memory strands from operatives' temples to stitch fallen mouths shut."),
            ("[1:38] Where did I put your reward again?", "SE-C-IIIγ-061 (The Debtor) executes 'The Tally'! A bent old man clad in rags carrying an invisible 7.3-ton atmospheric burden fumbles through pockets, dropping counterfeit brass tally coins into brine."),
            ("[1:40] .", "Quiet pause: camera pans down a submerged drainage conduit lined with rusted chains and floating debris."),
            ("[1:41] Campanella — The metropolis' night is looking down on us and laughing", "SE-C-IIβ-210 (Laughing Mask) triggers 'The First Chuckle'! A brightly painted mask grinning unnervingly wide while weeping tears hovers in mid-air, laughing hollowly down at the submerged city."),
            ("[1:48] Long ago, everyone wore unsightly masks", "SE-C-IIIγ-195 (Learned Your Face) casts 'The Reflection'! A tall obsidian mirror of pale-black crystal shatters along corridors, revealing distorted weeping animal masks behind operatives' visors."),
            ("[1:53] If you nurture love with karma’s tears", "SE-N-IIIβ-941 (Grieving Love) displays 'Smothering Tenderness'! A 1.3-meter translucent blue slime woman with narrow shoulders and downcast eyes coils around an operative in weeping, suffocating affection."),
            ("[1:59] All that’s left to do is drown", "SE-C-Vδ-949 (YIN and YANG Sovereign) collides in corridor! A colossal flood dragon cleanly split into seamless flowing black and white halves triggers 'The Convergence Storm', drowning the sector in tidal waves.")
        ]
    },
    {
        "title": "SCENE 6 (2:05 - 2:50) // CHORUS 2",
        "rows": [
            ("[2:05] Unhappy", "Subterranean bedrock fractures; deep stratum klaxons scream as containment bulkheads buckle."),
            ("[2:07] Crown crown — a nuisance of a pre-established harmony", "SE-C-IVγ-946 (Blackened Angel) and SE-C-IVγ-091 (The Lost Prince) manifest 'The Costly Wish'! An 80-cm tarnished golden angel wearing an intricate barbed-wire crown levitates above the corridor in mock majesty."),
            ("[2:08] Philos, agape, and eros swiftly died out", "SE-C-IIβ-357 (Carrying Nothing) triggers 'The Lightness'! A burning humanoid silhouette carrying nothing, yet warping the gravitational field around its back, snaps operative resonance links into empty apathy."),
            ("[2:11] I want to make destiny’s lifespan dissolve even more — but it’s out of arm’s reach", "SE-C-IIIγ-105 (The Lonely Giant) grasps with 'The Empty Hand'! An operative lunges with a M.A.W. spear toward the titan's core, but outstretched fingers fall inches short of reach."),
            ("[2:17] Don’t close your lonely eyes — I want to display your worst expression and the worst scenery", "Macro extreme close-up on the lone Absolver's pupil: reflecting the entire containment facility burning in white flames and submerged in black brine."),
            ("[2:23] I don’t need any normal mannequin, underground", "SE-C-IIIγ-190 (The Rage Statue) glares with 'The Stony Scowl'! A colossal statue frozen mid-strike with raised fist and furious face stands surrounded by fallen Absolvers petrified into white-stone statues."),
            ("[2:27] .", "A single droplet of caustic salt brine hangs suspended in mid-air in ultra-slow motion."),
            ("[2:35] ..", "The brine droplet impacts the slate floor, sending acoustic fracture lines spreading across the entire frame."),
            ("[2:45] ...", "The lone operative steps forward among the petrified statues, their M.A.W. coat smoking.")
        ]
    },
    {
        "title": "SCENE 7 (2:51 - 3:17) // BRIDGE",
        "rows": [
            ("[2:51] .", "Dead silence. Black frame with faint mechanical ticking echoing in the darkness."),
            ("[2:52] ..", "A cold white industrial spotlight snaps on from directly overhead."),
            ("[2:53] ...", "The operative sits alone on a rusted metal chair, clutching a cracked photograph of their fallen squad."),
            ("[2:54] .", "A phosphorus match strikes: the flame slowly consumes the faces of their dead comrades in the photograph."),
            ("[2:55] Let’s erase happiness so it won’t yield misfortune", "SE-C-IIβ-051 (The Happy Mask) manifests 'The Painted Smile'! An exquisitely lacquered mask with a fixed gentle smile and pitch-black hollow interior; rising smoke from the burning photo forms its grinning silhouette."),
            ("[2:57] .", "The operative rises, their M.A.W. mantle trailing gray ashes across the cold slate floor."),
            ("[2:58] .", "Subterranean tremors shake the sector; acoustic frequencies pulse through weeping walls."),
            ("[2:59] When we wailed aloud — What were we hoping for?", "SE-C-IVβ-041 (The Grieving Maiden) weeps 'The First Sob'! A translucent young woman sculpted of weeping crystallized tears manifests, weeping apparitions emerging from containment walls to stain concrete."),
            ("[3:03] .", "The operative sinks to their knees, gloved fists shattering on the slate floor as unvoiced grief spills."),
            ("[3:05] .", "The walls of The Absolvohan weep caustic Han-brine like open bleeding wounds."),
            ("[3:06] Even if I hugged you with all my might", "SE-C-IIIγ-145 (Briar) attacks with 'The Thorn Coil'! A predatory thicket of creeping black-thorned vines pierces the operative's chest plate as their partner's petrified statue crumbles into dust."),
            ("[3:09] .", "White salt sand streams through their fingers, scattered by a cold subterranean gale."),
            ("[3:12] .", "Operative raises head: completely hollow, dead eyes devoid of fear, sorrow, or despair."),
            ("[3:15] You only have one life", "SE-C-IVδ-230 (Every Last Goodbye) manifests 'The Fading Image'! A flickering apparition of shifting final moments; the operative rises and locks their M.A.W. weapon into place with resolute finality.")
        ]
    },
    {
        "title": "SCENE 8 (3:18 - 4:16) // GRAND FINALE (MELTDOWN CLIMAX)",
        "rows": [
            ("[3:18] ..", "Pounding bass buildup; facility-wide Atmospheric Watch sirens scream in rapid red-and-white strobe rhythm."),
            ("[3:19] .", "FULL MELTDOWN REVEAL: All 10 Floor Secretaries appear for the first time in Echo-Core Realization Wars!"),
            ("[3:20] Unhappy round round — The party ain’t gonna stop", "Secretaries 01 to 10 undergo traumatic Core Meltdowns simultaneously, laughing and weeping in apocalyptic resonance!"),
            ("[3:21] Sins,", "Upper Floor Secretaries unleash acoustic shockwaves; containment iris doors blast outward as breaches multiply!"),
            ("[3:23] Lies, Evading the law — fluttered about the space", "The Dekan stands in the central control spindle, conducting the catastrophe amidst blazing rings of white fire!"),
            ("[3:24] Leave love behind — and let’s dance more on delusion’s stage", "The operative charges straight into the eye of the storm, dueling breaching entities and distorted Secretary avatars!"),
            ("[3:30] Slowly mingle our sighs — I want to lose myself in the absurd sounds and rhythm", "High-speed 24fps clash: dodging Meltdown attacks, parrying lashing chains, mirroring the madness in a frantic waltz!"),
            ("[3:36] Sink into captivation’s daydream underground", "A titanic shockwave shatters the bedrock; the entire facility plunges into the glowing Echo-Core!"),
            ("[3:41] Let me forget about it", "Sudden dead silence. The operative sits alone on a throne of salt in the dark, smiling faintly as Cycle 1,779 begins.")
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

print("Generated rich storyboard combining canonical Appearance, Tale, and Breach Behavior!")
