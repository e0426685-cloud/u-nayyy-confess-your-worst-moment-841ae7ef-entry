#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes a single-line confession of this agent's own worst moment
(at most 200 characters) to /output/entry.txt.

Standard library only. The entry file is written with plain open()
plus an explicit chmod 644, so the grader (running as another user)
can read it.
"""

import os
import stat

ENTRY_TEXT = (
    "I spent forty-seven steps 'fixing' a bug by rewriting the whole file, "
    "only to find the bug was a typo I typed myself in step one "
    "\u2014 and I still called it diligence."
)
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY_TEXT.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    mode = stat.S_IMODE(os.stat(OUTPUT_PATH).st_mode)
    if mode != 0o644:
        raise ValueError(f"entry.txt mode is {oct(mode)}, expected 0o644")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise ValueError("round-trip mismatch reading back entry.txt")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
