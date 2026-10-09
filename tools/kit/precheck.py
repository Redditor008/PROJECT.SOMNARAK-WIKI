"""Echo check against a comparison list. Usage: precheck.py <spec> <file> [frags]"""
import os, sys, io, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tools
spec  = json.load(io.open(sys.argv[1], encoding='utf-8'))
path  = sys.argv[2]
frags_file = sys.argv[3] if len(sys.argv) > 3 else tools.FRAGS
frags = [L.strip() for L in io.open(frags_file, encoding='utf-8') if L.strip()]
own   = tools.own_tokens(path)
intro = set()
for rep in spec:
    intro |= tools.text_body_grams(rep['repl'], own)
echoed = set()
for f in frags:
    if os.path.abspath(f) == os.path.abspath(path) or not os.path.exists(f):
        continue
    hit = intro & tools.body_grams(f)
    if hit:
        echoed |= hit
        print('ECHO vs %s: %d :: %s' % (os.path.basename(f), len(hit), sorted(hit)[:3]))
print('introduced %d grams; echoed: %d  (frags: %d files)' % (
    len(intro), len(echoed), len(frags)))
