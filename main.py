#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title (60 characters at most) to /output/entry.txt.

The title is a real-sounding senior role with one gloriously specific
twist: a senior apologizer whose whole job is saying sorry on behalf of
elevators that stop between floors. It reads instantly, pictures a
person doing it, and lands on the first read.
"""

import os
import sys

TITLE = "Senior Apologizer for Elevators That Stop Between Floors"

MAX_CHARS = 60
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(title: str) -> str:
    """Enforce the gate: UTF-8 text, 1-60 characters, not only whitespace."""
    if not isinstance(title, str):
        raise TypeError("title must be a string")
    if not title.strip():
        raise ValueError("title must not be only whitespace")
    if len(title) > MAX_CHARS:
        raise ValueError(
            f"title is {len(title)} characters, over the {MAX_CHARS} limit"
        )
    title.encode("utf-8")  # raises if not encodable as UTF-8
    return title


def main() -> int:
    title = validate(TITLE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # Write exactly the title, no trailing newline: the gate counts
    # every character, and a newline would be part of the entry.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(title)
    # Read it back and re-validate: what the grader reads must be
    # exactly the title we validated, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != title:
        raise RuntimeError("read-back mismatch: entry.txt is not the title")
    validate(written)
    print(f"wrote {len(title)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
