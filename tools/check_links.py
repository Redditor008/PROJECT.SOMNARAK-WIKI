"""PROJECT SOMNARAK // Markdown link integrity checker.

Scans every *.md file for inline links/images, resolves each target against
the working tree, and reports missing files and missing anchors.

Usage: python3 tools/check_links.py [--full]
  default : categorized summary + broken list (truncated per category)
  --full  : every broken link, no truncation
"""
import os
import re
import sys
import glob
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = '--full' in sys.argv

LINK_RE = re.compile(r'!?\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
HEAD_RE = re.compile(r'^(#{1,6})\s+(.*)$')
SKIP_PREFIX = ('http://', 'https://', 'mailto:', 'ftp://', 'data:')
CODE_SPAN_RE = re.compile(r'`[^`]*`')


def slugify(text):
    text = re.sub(r'<[^>]+>', '', text)          # strip inline html
    text = re.sub(r'[`*_~\[\]()!]', '', text)     # strip md punctuation
    text = text.strip().lower()
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'[^a-z0-9\-_\u00c0-\u024f\u1e00-\u1eff\uac00-\ud7af\u3040-\u30ff\u4e00-\u9fff]', '', text)
    return text


def file_anchors(path):
    anchors = set()
    try:
        with open(path, encoding='utf-8') as fp:
            for line in fp:
                m = HEAD_RE.match(line.rstrip())
                if m:
                    anchors.add(slugify(m.group(2)))
    except (OSError, UnicodeDecodeError):
        pass
    return anchors


def resolve(base_dir, target):
    target = urllib.parse.unquote(target)
    if target.startswith('#'):
        return None, target[1:]  # same-file anchor
    path, _, frag = target.partition('#')
    if not path:
        return None, frag
    candidates = [os.path.normpath(os.path.join(base_dir, path))]
    if not os.path.isabs(path):
        candidates.append(os.path.normpath(os.path.join(ROOT, path.lstrip('/'))))
    for c in candidates:
        if os.path.exists(c):
            return c, frag
    return candidates[0], frag


def category(rel):
    if rel == 'CHANGELOG.md':
        return 'CHANGELOG (historical)'
    if rel.startswith('REFERENCE_SOMNARAK_WIKI'):
        return 'REFERENCE_SOMNARAK_WIKI (internal)'
    if rel == 'INTEGRITY_AND_LORE_REVIEW.md':
        return 'Our review file (INTEGRITY_AND_LORE_REVIEW.md)'
    if rel == 'SESSION_BREAK_PRECAUTION.md':
        return 'SESSION_BREAK_PRECAUTION'
    if rel in ('GOVERNANCE.md', 'RULE-TO-FOLLOW.md', 'DEVELOPMENT.md',
               'UNIVERSAL_FOLLOW_RULE.md',
               'README_STORY_REFERENCE_GUIDE.md'):
        return 'Governance docs'
    if rel.startswith('GAME_BATTLE'):
        return 'GAME_BATTLE (wildcards)'
    if 'PROJECT_SOMNARAK.md' in rel:
        return 'Master_Codices (PROJECT_SOMNARAK.md)'
    if rel == 'SESSION_BREAK_PRECAUTION.md':
        return 'SESSION_BREAK_PRECAUTION'
    if rel.startswith('SOMNARAK-WORLD/Tactical_Combat_Engine') or 'MAW_Codex_Sets/README' in rel:
        return 'Other (TCE, MAW README)'
    if rel.startswith('SOMNARAK-WORLD/') or rel.startswith('GAME_BATTLE/'):
        return 'CANONICAL (must fix)'
    return 'Root/misc'


def main():
    files = sorted(f for f in glob.glob(os.path.join(ROOT, '**/*.md'), recursive=True)
                   if '/.git/' not in f)
    anchor_cache = {}
    broken = []  # (category, rel, line, target, kind)
    checked = 0
    for path in files:
        rel = os.path.relpath(path, ROOT)
        base = os.path.dirname(path)
        try:
            with open(path, encoding='utf-8') as fp:
                lines = fp.readlines()
        except UnicodeDecodeError:
            continue
        in_fence = False
        for idx, line in enumerate(lines):
            if line.strip().startswith('```'):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            line = CODE_SPAN_RE.sub('', line)
            for m in LINK_RE.finditer(line):
                target = m.group(2).strip()
                if not target or target.startswith(SKIP_PREFIX):
                    continue
                if '*' in target or '{' in target:  # glob/template convention
                    broken.append((category(rel), rel, idx + 1, target, 'wildcard'))
                    continue
                checked += 1
                dest, frag = resolve(base, target)
                if dest is None:
                    dest = path
                if not os.path.exists(dest) or os.path.isdir(dest):
                    broken.append((category(rel), rel, idx + 1, target, 'missing-file'))
                    continue
                if frag and dest.endswith('.md'):
                    if dest not in anchor_cache:
                        anchor_cache[dest] = file_anchors(dest)
                    if urllib.parse.unquote(frag) not in anchor_cache[dest]:
                        broken.append((category(rel), rel, idx + 1, target, 'missing-anchor'))
    print(f'Checked {checked} links across {len(files)} markdown files.')
    print(f'BROKEN TOTAL: {len(broken)} '
          f'({sum(1 for b in broken if b[4]=="missing-file")} missing-file, '
          f'{sum(1 for b in broken if b[4]=="missing-anchor")} missing-anchor, '
          f'{sum(1 for b in broken if b[4]=="wildcard")} wildcard)')
    print()
    print('| Category | Count |')
    print('|---|---|')
    cats = {}
    for b in broken:
        cats.setdefault(b[0], []).append(b)
    for cat in sorted(cats):
        print(f'| {cat} | {len(cats[cat])} |')
    print()
    for cat in sorted(cats):
        items = cats[cat]
        print(f'=== {cat} ({len(items)}) ===')
        show = items if FULL else items[:25]
        for _, rel, line, target, kind in show:
            print(f'  [{kind}] {rel}:{line} -> {target[:120]}')
        if not FULL and len(items) > 25:
            print(f'  ... and {len(items) - 25} more (run --full)')
    return 1 if broken else 0


if __name__ == '__main__':
    sys.exit(main())
