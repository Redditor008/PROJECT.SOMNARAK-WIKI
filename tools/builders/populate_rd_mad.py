import re

# Let's read the original file to extract all scenes and lyrics
with open("TRYOUT,SANDBOX/PROJECT.SOMNARAK-Animatic-Text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Visual directions mapped to each scene and lyric
script_data = {
    "SCENE 1": [
        ("It’s quite rambunctious — Bam bii na bam bii na", "Absolver boots marching into Absolvohan as red emergency strobes pulse."),
        ("Stomp your feet", "Heavy iron-plated boots stomping into shallow pools of glowing Han-brine."),
        ("In the indiff-diff-different dance hall", "Floor 04 Acoustic Buffer panning wide; resonators sway like grotesque chandeliers."),
        ("Come over here — Bam bii no bam bii no", "Floor 04 Secretary leaning over an iron balcony, waving with a smiling mask."),
        ("Whose blood was that again?", "Operative wipes crimson Grudge off their visor, glancing at a shredded coat tag.")
    ],
    "SCENE 2": [
        ("Breathe in, breathe out, swallow it up", "Gas mask intake valve hisses as the operative inhales freezing, caustic saline air."),
        ("Where are your eyes peeking at?", "CCTV lenses swivel 180 degrees down; red surveillance glare locks onto their eyes."),
        ("Stick a gun to the peaceful clock’s second hand", "Colossal brass clock counts down the Atmospheric Watch; operative aims rifle at it."),
        ("Here’s a naive song", "Antique gramophone on an ammo crate spins a warped nursery rhyme into the dark.")
    ],
    "SCENE 3": [
        ("Spit out the dead’s message", "Coughing black salt onto an open acoustic ledger; unrecorded wills burn away."),
        ("The closing performance & (and) last page", "Tearing out the final page of the Mnemonic Cycle logbook, scattering gray ashes."),
        ("A drug you can no longer get enough of", "Slamming a mental-stabilizer syringe into the neck; pupils flood with pale light."),
        ("The abandoned goddess’s rampage", "Containment blast doors blow outward; a weeping Rank IV Entity breaches the hall."),
        ("Sentimentality is a mountain of rubbish — You only have one life", "Walking past piles of discarded mourning charms and body bags without pausing.")
    ],
    "SCENE 4": [
        ("Unhappy", "Smash-cut to Floor 02 Archive Secretary laughing while tossing ledgers into air."),
        ("Round round — The party ain’t gonna stop", "360-degree rotational camera spin around 10-node grid; alarms strobe red and cyan."),
        ("Sins, lies, evading the law — fluttered about the space", "Mourning veils and contraband engrams from The Raw flutter like dark confetti."),
        ("Leave love behind — and let’s dance more on delusion’s stage", "Absolver leaps into Pugnahan clash, pirouetting under claws and striking down."),
        ("Slowly mingle our sighs — I want to lose myself in the absurd sounds and rhythm", "Composure drops; acoustic weeping frequencies synchronize with ragged breathing."),
        ("Sink into captivation’s daydream underground", "Sliding backward across grating, boots kicking up glowing bioluminescent salt sludge."),
        (".", "Freeze-frame on the entity's twisted visage grinning from ceiling pipes above."),
        ("Let me forget about it", "Operative closes their eyes with a hollow smile as a shockwave detonates behind.")
    ],
    "SCENE 5": [
        ("You’re rather gloomy — Bam bii naa bam bii na", "Floor 03 Thermal Secretary lights an iron pipe, blowing ash at a rookie."),
        ("Hey hey hey — I can’t hear ya", "Absolver clutches ears as acoustic pressure blasts shatter observation glass."),
        ("Cry for me — Bam bii no bam bii no", "Performing Flerehan: tears stream from behind visor, hardening into salt needles."),
        ("Where did I put your reward again?", "Floor Secretary tosses a handful of salt coins into burning fluid with a chuckle."),
        (".", "Quiet pause: camera tracking slowly down a flooded staircase lined with rusted chains."),
        ("Campanella — The metropolis' night is looking down on us and laughing", "Camera soars up exhaust silo: Somnarak City's cold skyline gleams high above abyss."),
        ("Long ago, everyone wore unsightly masks", "Flashback: citizens in The Raw wearing grotesque animal mourning veils in flood."),
        ("If you nurture love with karma’s tears", "Operative grips the hand of a dying partner as salt crust creeps across skin."),
        ("All that’s left to do is drown", "Tidal surge of Han-brine engulfs the corridor, submerging everything in deep water.")
    ],
    "SCENE 6": [
        ("Unhappy", "The Dekan stands in Council chamber, raising a conductor's baton in the dark."),
        ("Crown crown — a nuisance of a pre-established harmony", "Breaching entity manifests a crown of sharp white salt needles above its skull."),
        ("Philos, agape, and eros swiftly died out", "Rapid three-frame cuts of three operatives falling, tether lines snapping like strings."),
        ("I want to make destiny’s lifespan dissolve even more — but it’s out of arm’s reach", "Absolver lunges with M.A.W. spear, reaching for entity's core but falling short."),
        ("Don’t close your lonely eyes — I want to display your worst expression and the worst scenery", "Macro extreme close-up of operative's eye, reflecting burning containment wing."),
        ("I don’t need any normal mannequin, underground", "Defeated Absolvers stand along walls, petrified into stiff, hollow salt statues."),
        (".", "Single droplet of caustic brine falling in super slow motion toward the ground."),
        ("..", "Drop impacts the salt crust, sending acoustic shock ripples across the frame."),
        ("...", "A lone survivor stands among statues, adjusting their cracked mourning veil.")
    ],
    "SCENE 7": [
        (".", "Black screen. Faint metronomic ticking."),
        ("..", "Dim white spotlight turns on from overhead, illuminating a single steel chair."),
        ("...", "Operative sits on chair, staring at a cracked pocket portrait of their squad."),
        (".", "A match is struck; the flame catches the corner of the photograph."),
        ("Let’s erase happiness so it won’t yield misfortune", "Dropping burning portrait into a tray of chemical ash, watching faces curl black."),
        (".", "Operative stands up, tattered mantle trailing in the falling ash."),
        (".", "Flerehan weeping: sudden violent tremors shake room as sound waves warp walls."),
        ("When we wailed aloud — What were we hoping for?", "Silhouettes of all 10 Floor Secretaries stand on high pillars, faces shadowed."),
        (".", "Operative drops to knees, gloved fists pounding the cold slate floor in despair."),
        (".", "Ghostly hands reach out from Absolvohan walls, offering freezing comfort."),
        ("Even if I hugged you with all my might", "Operative embraces partner's salt statue; statue fractures into white dust."),
        (".", "Salt sand pours through gloved fingers like hourglass grains."),
        (".", "Operative looks up: eyes completely dead, devoid of both fear and hope."),
        ("You only have one life", "Rising to feet, gripping M.A.W. weapon with white-knuckled, grim resolve.")
    ],
    "SCENE 8": [
        ("..", "Fast rising synth pitch; red warning klaxons flash at blinding strobe speed."),
        (".", "Low-angle tracking shot: operative sprints full tilt down containment boulevard."),
        ("Unhappy round round — The party ain’t gonna stop", "Rapid 24fps montage: spinning gears, breaching entities, scrubbers spraying foam."),
        ("Sins,", "Slash attack cleaves entity's arm in a blinding burst of green Han-Energy."),
        ("Lies, Evading the law — fluttered about the space", "Spinning leap over a wave of corrosive brine, trench coat flaring like raven wings."),
        ("Leave love behind — and let’s dance more on delusion’s stage", "Clashing blade-to-blade with Sovereign, sparks lighting up grinning mask."),
        ("Slowly mingle our sighs — I want to lose myself in the absurd sounds and rhythm", "Operative and entity move in grotesque, synchronized choreography of violence."),
        ("Sink into captivation’s daydream underground", "Colossal shockwave shatters floor; both plunge into abyssal depths of Echo-Core."),
        ("Let me forget about it", "Total silence. Operative sits on salt throne in dark, smiling as clock resets to 00:00.")
    ]
}

# Let's format into clean table:
# Column 1 width: 94 chars (inner 92)
# Column 2 width: 90 chars (inner 88)
# Total width: 94 + 90 + 3 = 187 chars

c1_w = 94
c2_w = 90
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
    # scene header
    out_lines.append(top_border)
    sc_clean = f" {sc_name} // REVERIE DIRECTORATE MAD ANIMATIC SCRIPT "
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

print("Generated full R.D. MAD script in TRYOUT,SANDBOX/PROJECT.SOMNARAK-Animatic-Text.txt successfully!")
