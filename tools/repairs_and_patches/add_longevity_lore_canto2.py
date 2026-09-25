f = "SOMNARAK-WORLD/Story_Cantos/CANTO_02_THE_ACOUSTIC_VOID_SEOL_A.md"
with open(f, "r", encoding="utf-8") as fp:
    c = fp.read()

target = '"Fourteen hundred and twelve times," Min-Jae replied without missing a beat. "And three hundred and eight times I had to drag you out of an acid puddle by your collar."'

lore_para = '''"Fourteen hundred and twelve times," Min-Jae replied without missing a beat. "And three hundred and eight times I had to drag you out of an acid puddle by your collar."

It was an impossible number for mortal men, but none of them were strictly mortal anymore. In the subterranean depths of The Absolvohan, ordinary cellular mortality had long ceased to function under the laws of the surface. Through the phenomenon known as **Mnemonic Cycle Dilation** (  기억 주기 지연  , *Gieok Jugi Jiyeon*) and **Han-Saturation Cellular Stasis** (  한 포화 세포 정체  , *Han Pohwa Sepo Jeongche*), operatives bound to high-grade M.A.W. weaponry ceased to age along ordinary calendar years. Between the violent municipal resets of the 1,778 Cycles, their biological tissues were suspended within the cryo-engrammatic salt-strata of the lower vaults—frozen at the exact somatic hour of their binding oath, re-awakened only when containment ruptured or an atmospheric watch sounded. They had endured through two hundred and sixty-six cycles not by outliving time, but by having time torn away from them, leaving only their weapons, their grudges, and the stubborn weight of living.'''

assert target in c, "Target not found in Canto 2"
c = c.replace(target, lore_para)

with open(f, "w", encoding="utf-8") as fp:
    fp.write(c)

print("Added canonical Cycle Longevity lore paragraph to CANTO_02.")
