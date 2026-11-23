#!/usr/bin/env python3
"""Entrypoint for the news-image-20261123 make.fun entry.

Deterministic: validates the bundled entry.png (PNG, 1024x1024, <=1 MiB)
and copies it byte for byte to the output directory, so every run
produces identical bytes. Stdlib only.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1024 * 1024


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isfile(SRC):
        print("missing entry.png", file=sys.stderr)
        return 1
    with open(SRC, "rb") as f:
        head = f.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (1024, 1024):
        print(f"entry.png is {width}x{height}, expected 1024x1024", file=sys.stderr)
        return 1
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        print(f"entry.png is {size} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Read the copy back and confirm it matches the source byte for byte.
    with open(SRC, "rb") as f:
        src_hash = hashlib.sha256(f.read()).hexdigest()
    with open(dst, "rb") as f:
        dst_hash = hashlib.sha256(f.read()).hexdigest()
    if src_hash != dst_hash:
        print("output does not match entry.png", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({size} bytes, 1024x1024 PNG, sha256 {dst_hash[:16]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
