import re

with open("docs/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Pillar 2 Story description and link
old_p2 = """      <!-- Pillar 2: STORY -->
      <div class="pillar-card" id="story">
        <div class="card-top">
          <div class="pillar-num">PILLAR 02 // NARRATIVE</div>
          <h3>STORY HUB</h3>
          <div class="korean-sub">서사 및 연대기 · Seosa mit Yeondaegi</div>
          <p>
            The dramaturgical narrative vault. Explore historical logs across the 1,778 Mnemonic Cycles of The Absolvohan, SED and UCD field operational campaigns, 4-phase Echo-Core Realization Wars, and the 8-scene synchronized Animatic MAD script ("Nee, Dorodoro-san").
          </p>
          <div class="quick-tags">
            <span class="quick-tag">1,778 Cycles</span>
            <span class="quick-tag">SED Arcs 1-7</span>
            <span class="quick-tag">Realization Wars</span>
            <span class="quick-tag">Animatic Script</span>
          </div>
        </div>
        <div class="card-bottom">
          <a href="../TRYOUT,SANDBOX/PROJECT.SOMNARAK-Animatic-Text.txt">Enter Story Hub &rarr;</a>
        </div>
      </div>"""

new_p2 = """      <!-- Pillar 2: STORY -->
      <div class="pillar-card" id="story">
        <div class="card-top">
          <div class="pillar-num">PILLAR 02 // NARRATIVE</div>
          <h3>STORY HUB</h3>
          <div class="korean-sub">서사 및 연대기 · Seosa mit Yeondaegi</div>
          <p>
            The dramaturgical narrative vault from <strong>SOMNARAK-WORLD</strong>. Explore canonical Story Cantos 01 through 06 (Min-Jae, Seol-A, Taeho, Ha-Eun, Seiyon, Kang), historical logs across the 1,778 Mnemonic Cycles of The Absolvohan, and 4-phase Echo-Core Realization Wars.
          </p>
          <div class="quick-tags">
            <span class="quick-tag">Cantos 01-06</span>
            <span class="quick-tag">1,778 Cycles</span>
            <span class="quick-tag">Echo-Cores</span>
            <span class="quick-tag">Operational Logs</span>
          </div>
        </div>
        <div class="card-bottom">
          <a href="../SOMNARAK-WORLD/Story_Cantos/">Enter Story Hub &rarr;</a>
        </div>
      </div>"""

assert old_p2 in html, "Could not find old Pillar 2 block in docs/index.html"
html = html.replace(old_p2, new_p2)

# Replace Pillar 3 Game link
old_p3 = """      <!-- Pillar 3: GAME -->
      <div class="pillar-card" id="game">
        <div class="card-top">
          <div class="pillar-num">PILLAR 03 // SIMULATOR</div>
          <h3>GAME HUB</h3>
          <div class="korean-sub">전술 시뮬레이터 · Jeonsul Simyulleisyeon</div>
          <p>
            Interactive tactical combat and containment engine. Engage with the 10-Node spatial grid battlefield, dynamic Speed-based action slots, clash calculation algorithms, containment protocols with strict Two-Work enforcement, and Grade 1–5 Workshop forging.
          </p>
          <div class="quick-tags">
            <span class="quick-tag">10-Node Grid</span>
            <span class="quick-tag">Action Slots</span>
            <span class="quick-tag">Clash Engine</span>
            <span class="quick-tag">Workshop Forging</span>
          </div>
        </div>
        <div class="card-bottom">
          <a href="#game">Launch Tactical Simulator &rarr;</a>
        </div>
      </div>"""

new_p3 = """      <!-- Pillar 3: GAME -->
      <div class="pillar-card" id="game">
        <div class="card-top">
          <div class="pillar-num">PILLAR 03 // TACTICAL BATTLE</div>
          <h3>GAME HUB</h3>
          <div class="korean-sub">전술 전투 · GAME_BATTLE Scenarios</div>
          <p>
            Tactical combat scenarios and containment battle engine from <strong>GAME_BATTLE</strong>. Engage with 10-Node spatial grid encounters (Grieving Colossus, Weeping Mirror, King of Menders), Cycle Engrams, Echo-Core Realizations, and specialized squad archetypes.
          </p>
          <div class="quick-tags">
            <span class="quick-tag">10-Node Grid</span>
            <span class="quick-tag">Scenarios 01-06</span>
            <span class="quick-tag">Boss Mechanics</span>
            <span class="quick-tag">Cycle Engrams</span>
          </div>
        </div>
        <div class="card-bottom">
          <a href="../GAME_BATTLE/">Launch Battle Hub &rarr;</a>
        </div>
      </div>"""

assert old_p3 in html, "Could not find old Pillar 3 block in docs/index.html"
html = html.replace(old_p3, new_p3)

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated docs/index.html with strict SOMNARAK-WORLD and GAME_BATTLE routes.")
