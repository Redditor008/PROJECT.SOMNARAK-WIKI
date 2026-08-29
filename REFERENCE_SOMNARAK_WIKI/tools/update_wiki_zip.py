#!/usr/bin/env python3
"""Always overwrite the one 01_Somnarak_Wiki.zip after wiki updates.

Canonical output (never a new filename):
  01_Somnarak_Wiki/downloads/01_Somnarak_Wiki.zip

Excludes nested .zip files so the archive does not pack itself.
"""
from __future__ import annotations

import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WIKI = REPO / "01_Somnarak_Wiki"
OUT = WIKI / "downloads" / "01_Somnarak_Wiki.zip"
ZIP_NAME = "01_Somnarak_Wiki.zip"


def format_size(n: int) -> str:
    mb = n / (1024 * 1024)
    if mb >= 10:
        return f"{mb:.1f} MB"
    if mb >= 1:
        return f"{mb:.2f} MB"
    kb = n / 1024
    return f"{kb:.0f} KB"


def build_zip() -> tuple[int, int]:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_suffix(".zip.tmp")
    if tmp.exists():
        tmp.unlink()

    count = 0
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(WIKI.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(WIKI)
            if path.suffix.lower() == ".zip":
                continue
            if path.name in {ZIP_NAME, OUT.with_suffix(".zip.tmp").name}:
                continue
            zf.write(path, Path("01_Somnarak_Wiki") / rel)
            count += 1

    tmp.replace(OUT)
    return count, OUT.stat().st_size


def patch_download_pages(size_label: str, file_count: int) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    pages = [
        WIKI / "downloads.html",
        WIKI / "project" / "downloads.html",
    ]
    for page in pages:
        if not page.exists():
            continue
        text = page.read_text(encoding="utf-8")
        text = re.sub(
            r'(id="wiki-zip-size"[^>]*>)[^<]+',
            lambda m: m.group(1) + f"{size_label} (.ZIP)",
            text,
            count=1,
        )
        text = re.sub(
            r'(id="wiki-zip-size-btn">)[^<]+',
            lambda m: m.group(1) + size_label,
            text,
            count=1,
        )
        page.write_text(text, encoding="utf-8")
        print(f"patched {page.relative_to(REPO)}  ({stamp}, {file_count} files)")


def main() -> None:
    count, nbytes = build_zip()
    label = format_size(nbytes)
    print(f"updated {OUT.relative_to(REPO)}  {label}  {count} files")
    patch_download_pages(label, count)


if __name__ == "__main__":
    main()
