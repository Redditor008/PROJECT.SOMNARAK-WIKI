#!/usr/bin/env python3
"""syncbranch.py - bring this checkout level with origin/<branch> without losing anything.

Two agent sessions can write to the same session branch, and a sandbox can be restored from an
older snapshot of the working tree. gate.sh used to sync with `git reset --mixed FETCH_HEAD`,
which moves HEAD and the index but not the working tree. With the remote ahead, the next
`git add -A` then stages the OLD files and silently reverts the other session's commits (this
nearly happened on 2026-10-05, when three commits, one of them a dossier retirement, had been
pushed to the branch between two turns).

  HEAD == origin tip           nothing to do
  origin ahead of HEAD         if the working tree holds no unpushed work (it is byte-identical to
                               a commit already on the branch) move HEAD and the working tree to
                               the tip; otherwise try a fast-forward merge, which refuses safely
                               if local edits overlap the incoming change
  local commits not on origin  refuse: push or reconcile first

Exit status 0 means the checkout is level with origin and nothing was lost. Anything else prints
why, and nothing has been changed.

  python3 tools/syncbranch.py            sync
  python3 tools/syncbranch.py --check    report only; change nothing
"""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROTECTED = ('', 'main', 'NON-WIKI')


def git(*args, text=True):
    r = subprocess.run(['git', '-c', 'core.quotepath=off'] + list(args), cwd=ROOT,
                       capture_output=True)
    out = r.stdout.decode('utf-8', 'replace') if text else r.stdout
    return r.returncode, out, r.stderr.decode('utf-8', 'replace')


def blob_id(path):
    data = open(os.path.join(ROOT, path), 'rb').read()
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def working_map():
    """path -> blob id for every file git would consider part of the tree: tracked files that
    still exist plus untracked files that are not ignored."""
    paths = set()
    for flag in ([], ['--others', '--exclude-standard']):
        _, out, _ = git('ls-files', '-z', *flag)
        paths.update(p for p in out.split('\0') if p)
    return dict((p, blob_id(p)) for p in paths if os.path.isfile(os.path.join(ROOT, p)))


def tree_map(commit):
    _, out, _ = git('ls-tree', '-r', '-z', commit)
    m = {}
    for rec in out.split('\0'):
        if rec:
            meta, path = rec.split('\t', 1)
            m[path] = meta.split()[2]
    return m


def say(msg):
    sys.stdout.write(msg + '\n')


def main(argv):
    check_only = '--check' in argv
    rc, branch, _ = git('branch', '--show-current')
    branch = branch.strip()
    if branch in PROTECTED:
        say("syncbranch: '%s' is not an assigned session branch; refusing." % (branch or 'detached HEAD'))
        return 1
    if git('ls-remote', '--exit-code', '--heads', 'origin', branch)[0] != 0:
        say('syncbranch: origin has no branch %s yet; nothing to sync.' % branch)
        return 0
    rc, _, err = git('fetch', '-q', 'origin', branch)
    if rc != 0:
        say('syncbranch: fetch failed: %s' % err.strip()[:200])
        return 1
    tip = git('rev-parse', 'FETCH_HEAD')[1].strip()
    head = git('rev-parse', 'HEAD')[1].strip()
    if head == tip:
        say('syncbranch: level with origin/%s at %s.' % (branch, tip[:7]))
        return 0
    if git('merge-base', '--is-ancestor', 'HEAD', tip)[0] != 0:
        say('syncbranch: BLOCKED. HEAD has commits that origin/%s does not, or the two have diverged.' % branch)
        say('             Push or reconcile first; nothing was changed.')
        return 1
    incoming = git('log', '--format=%h %an: %s', 'HEAD..' + tip)[1].strip().split('\n')
    say('syncbranch: origin/%s is %d commit(s) ahead:' % (branch, len([i for i in incoming if i])))
    for line in incoming[:8]:
        say('    ' + line[:150])
    if check_only:
        return 0

    work = working_map()
    matched = None
    if work == tree_map('HEAD'):
        matched = head
    else:
        for c in git('rev-list', '--max-count=300', tip)[1].split():
            if tree_map(c) == work:
                matched = c
                break
    if matched:
        # The working tree is exactly a pushed commit, so nothing unpushed can be lost. Put HEAD
        # and the index on that commit (leaving the files alone), then fast-forward cleanly.
        if matched != head:
            git('reset', '-q', '--mixed', matched)
        rc, _, err = git('merge', '-q', '--ff-only', tip)
        if rc != 0:
            say('syncbranch: BLOCKED. fast-forward failed: %s' % err.strip()[:300])
            return 1
    else:
        rc, _, err = git('merge', '-q', '--ff-only', tip)
        if rc != 0:
            say('syncbranch: BLOCKED. The working tree holds changes that are on no pushed commit,')
            say('             and they overlap what came in, so a fast-forward would overwrite them:')
            say('             ' + err.strip().replace('\n', ' ')[:300])
            say('             Commit them on a separate step after reconciling by hand; nothing was changed.')
            return 1
    now = git('rev-parse', 'HEAD')[1].strip()
    say('syncbranch: now level with origin/%s at %s.' % (branch, now[:7]))
    return 0 if now == tip else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
