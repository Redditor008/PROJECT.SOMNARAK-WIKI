"""Wing counter, and per-file recon. Usage: couples.py [BASE] [CODE]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tools
base = sys.argv[1] if len(sys.argv) > 1 else None
code = sys.argv[2] if len(sys.argv) > 2 else None
w, s, per, total = tools.scan(base)
print('COUPLES: %d / %d ; files carrying %d / %d ; section-pairs %d' % (
    len(w), total, len(per), total, sum(len(v) for v in s.values())))
print('  tiers: >=0.70 %d | 0.60-0.69 %d | 0.50-0.59 %d' % (
    sum(1 for v in w.values() if v >= 0.70),
    sum(1 for v in w.values() if 0.60 <= v < 0.70),
    sum(1 for v in w.values() if v < 0.60)))
if code:
    hits = sorted([(v, k, s[k]) for k, v in w.items()
                   if code in os.path.basename(k[0]) or code in os.path.basename(k[1])],
                  reverse=True)
    print('\nTARGET %s -> %d couples' % (code, len(hits)))
    for v, k, sl in hits:
        o = k[1] if code in os.path.basename(k[0]) else k[0]
        print('  %.2f  %-46s %s' % (v, os.path.basename(o)[:46],
              ' | '.join('%s %.2f/%.2f' % x for x in
                         sorted(sl, key=lambda x: -max(x[1], x[2])))))
