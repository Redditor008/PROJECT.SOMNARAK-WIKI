# Somnarak recovery — two copyable parts

Arena only displays the first 10,000 lines of a file. The original recovery
patch had 26,495 lines, so two raw halves would still be too long. It was
therefore compressed with gzip and encoded as URL-safe Base64, then divided
into exactly two short text files. Decoding reproduces the original patch
byte-for-byte; no project change was altered.

## Copy these two files from Arena Diff

1. `SOMNARAK_UNPUBLISHED_98c2059_PART_1.txt`
2. `SOMNARAK_UNPUBLISHED_98c2059_PART_2.txt`

Part 1 has 467 lines. Part 2 has 466 lines. Both are safely below
the 10,000-line display limit.

## Reconstruct the original patch

Save the copied text under the two filenames above, preserving the order, and
run this in a new active Arena session:

```python
from pathlib import Path
import base64
import gzip

names = [
    "SOMNARAK_UNPUBLISHED_98c2059_PART_1.txt",
    "SOMNARAK_UNPUBLISHED_98c2059_PART_2.txt",
]
payload = "".join(
    "".join(Path(name).read_text().split())
    for name in names
)
patch = gzip.decompress(base64.urlsafe_b64decode(payload))
Path("SOMNARAK_UNPUBLISHED_98c2059.patch").write_bytes(patch)
```

Then verify the reconstructed file:

```bash
sha256sum SOMNARAK_UNPUBLISHED_98c2059.patch
```

Required SHA-256:

```text
5456894b53d1b3d02435c60ebd9558491e1765552f25ff53559c753f62bf8fc7
```

The reconstructed patch represents 210 changed project paths relative to
public `main` commit `e132c026a675ffd3f0163c185116740ceb8e7472` and previously
passed `git apply --check` against that baseline.

After reconstruction, the new session should inspect current `main`, run
`git apply --check`, apply and validate the patch, remove these transfer files,
commit and push to its assigned branch, open a PR into `main`, merge it, and
verify GitHub Pages.
