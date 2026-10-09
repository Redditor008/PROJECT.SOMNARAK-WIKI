"""Line-by-line edit applier. Usage: apply.py <spec.json> <file> [--dry]

Each spec entry is {"sub": ..., "repl": ...}. The substring must occur exactly
once in the whole file; otherwise the apply aborts rather than guessing.
"""
import sys, io, json
spec = json.load(io.open(sys.argv[1], encoding='utf-8'))
path = sys.argv[2]
dry  = '--dry' in sys.argv
src  = io.open(path, encoding='utf-8').read()
lines = src.split('\n')
before = len(src.split())
for i, rep in enumerate(spec):
    sub, repl = rep['sub'], rep['repl']
    cnt = sum(L.count(sub) for L in lines)
    if cnt != 1:
        print('rep %d: sub NOT FOUND (%d occurrences)' % (i, cnt))
        sys.exit(1)
    for k, L in enumerate(lines):
        if sub in L:
            lines[k] = L.replace(sub, repl)
            break
out   = '\n'.join(lines)
after = len(out.split())
if dry:
    print('DRY OK  reps=%d  word delta %+d' % (len(spec), after - before))
else:
    io.open(path, 'w', encoding='utf-8').write(out)
    print('APPLIED OK  reps=%d  word delta %+d' % (len(spec), after - before))
