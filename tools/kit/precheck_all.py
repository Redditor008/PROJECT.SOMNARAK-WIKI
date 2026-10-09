"""Echo check against all 301 files. Usage: precheck_all.py <spec> <file>"""
import os, sys, io, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tools
spec = json.load(io.open(sys.argv[1], encoding='utf-8'))
path = sys.argv[2]
own  = tools.own_tokens(path)
intro = set()
for rep in spec:
    intro |= tools.text_body_grams(rep['repl'], own)
files = tools.files_under()
owner = collections.Counter()
grams = {}
for f in files:
    g = tools.body_grams(f)
    grams[f] = g
    for x in g:
        owner[x] += 1
n = 0
for f in files:
    if os.path.abspath(f) == os.path.abspath(path):
        continue
    hit = {x for x in (intro & grams[f]) if owner[x] <= tools.DISTINCTIVE_MAX}
    if hit:
        n += 1
        print('ECHO vs %s: %d :: %s' % (os.path.basename(f), len(hit), sorted(hit)[:3]))
print('introduced %d grams; distinctively echoed in %d files (of %d)' % (
    len(intro), n, len(files)))
