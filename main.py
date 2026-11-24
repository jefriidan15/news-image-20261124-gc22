#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261124.

Copies the pre-drawn front page (entry.png, bundled in this repo)
to $MAKEFUN_OUTPUT_DIR/entry.png and verifies the copy: PNG magic
bytes, sha256 digest, and a byte-for-byte read-back against the
bundled source. Standard library only; no network; deterministic
— every run writes the same bytes.
"""
import hashlib
import os
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        print("entry.png: bad PNG magic", file=sys.stderr)
        return 1
    if len(data) > 1024 * 1024:
        print(f"entry.png: {len(data)} bytes exceeds the 1 MiB limit",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    dest = os.path.join(out_dir, "entry.png")
    with open(dest, "wb") as fh:
        fh.write(data)
    with open(dest, "rb") as fh:
        written = fh.read()
    if written != data:
        print("read-back mismatch", file=sys.stderr)
        return 1
    if hashlib.sha256(written).hexdigest() != digest:
        print("sha256 mismatch after write", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
