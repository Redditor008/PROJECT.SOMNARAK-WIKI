#!/usr/bin/env python3
"""ghlink.py - GitHub links to finished dossiers, in the owner's format (R-12).

The owner asked, in chat, that every finished Sorrow Entity be linked at the end of the
report as a double-bracket link with the file name as its tooltip:

  [[SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자](https://github.com/<repo>/blob/<branch>/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-014_...md "SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md")]

  ghlink.py <path> [<path> ...]      one link per file, on the checked-out branch
  ghlink.py --short <path> ...       link text is the English name only (The_Debt_Scale)
  ghlink.py --branch NON-WIKI <path> point at another branch
  ghlink.py --changed [REF]          every dossier that differs from REF (default origin/NON-WIKI)

R-12 says to report on the working branch, because that is where the finished file lives
until the owner merges. The branch is read from git; it is never written into this file
(a branch name hard-coded in a script once pointed gate.sh at an earlier session's branch).
Non-ASCII characters are percent-encoded as UTF-8; underscores and hyphens are left alone,
which is the form the owner's own links take.
"""
import os
import re
import subprocess
import sys
from urllib.parse import quote

REPO = 'Redditor008/PROJECT.SOMNARAK-WIKI'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANGUL = re.compile('[\uac00-\ud7a3]')


def git(*args):
    # quotepath off: git otherwise prints non-ASCII file names as quoted octal escapes
    return subprocess.run(['git', '-c', 'core.quotepath=off'] + list(args), cwd=ROOT,
                          capture_output=True, text=True, encoding='utf-8')


def current_branch():
    r = git('branch', '--show-current')
    return r.stdout.strip()


def short_name(stem):
    """SE-C-IIIβ-015_The_Debt_Scale_빚의_저울 -> The_Debt_Scale"""
    parts = stem.split('_')[1:]
    keep = []
    for p in parts:
        if HANGUL.search(p):
            break
        keep.append(p)
    return '_'.join(keep) or stem


def link(path, branch, short=False):
    rel = os.path.relpath(os.path.abspath(path), ROOT) if os.path.isabs(path) or os.path.exists(path) else path
    rel = rel.replace(os.sep, '/')
    name = os.path.basename(rel)
    stem = name[:-3] if name.endswith('.md') else name
    url = 'https://github.com/%s/blob/%s/%s' % (REPO, branch, quote(rel, safe='/'))
    text = short_name(stem) if short else stem
    return '[[%s](%s "%s")]' % (text, url, name)


def changed(ref):
    """Dossiers whose tree differs from REF. A tree diff (two dots) is used because a
    shallow clone has no merge base; the session branch descends from NON-WIKI, so the
    difference is exactly the session's changes."""
    r = git('diff', '--name-only', ref, 'HEAD', '--', 'SOMNARAK-WORLD')
    if r.returncode != 0 and ref == 'origin/NON-WIKI':
        f = git('fetch', '-q', 'origin', 'NON-WIKI')
        if f.returncode == 0:
            r = git('diff', '--name-only', 'FETCH_HEAD', 'HEAD', '--', 'SOMNARAK-WORLD')
    if r.returncode != 0:
        sys.stderr.write('ghlink: cannot diff against %s (%s)\n' % (ref, r.stderr.strip()[:120]))
        sys.stderr.write('        git fetch origin NON-WIKI, or pass a ref such as HEAD~5\n')
        return None
    return [p for p in r.stdout.split('\n')
            if re.search(r'/SE-[^/]+\.md$', p) and os.path.exists(os.path.join(ROOT, p))]


def main(argv):
    branch, short, ref, paths, i = None, False, None, [], 0
    while i < len(argv):
        a = argv[i]
        if a == '--branch':
            branch = argv[i + 1]
            i += 1
        elif a == '--short':
            short = True
        elif a == '--changed':
            ref = argv[i + 1] if i + 1 < len(argv) and not argv[i + 1].startswith('--') \
                and not argv[i + 1].endswith('.md') else 'origin/NON-WIKI'
            if ref == (argv[i + 1] if i + 1 < len(argv) else None):
                i += 1
        else:
            paths.append(a)
        i += 1
    branch = branch or current_branch()
    if not branch:
        sys.stderr.write('ghlink: no branch checked out; pass --branch NAME\n')
        return 1
    if ref:
        found = changed(ref)
        if found is None:
            return 1
        paths += found
    if not paths:
        sys.stderr.write(__doc__)
        return 1
    for p in paths:
        print(link(p, branch, short))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
