#!/usr/bin/env python3
"""One Line of Earned Pride — entry program.

Writes a single line of text to /output/entry.txt: a quiet, earned
moment of pride for one small person in a concrete scene. The line is
fixed; the program exists so the text is produced deterministically
and checked against the gate (1-240 characters, not only whitespace)
before it is written.
"""

import os
import sys

# The line. Elias has mended other people's shoes for forty-one years;
# today he finally puts his own name in a pair, and wears them out.
# The pride is in the stitching and the wearing, never stated.
# Revision: cut the "After ..." setup so the scene happens today and
# the pride lands by the last word, in one read.
LINE = (
    "Elias mended other people's shoes for forty-one years; "
    "today he stitched his own name into a pair \u2014 "
    "and wore them to church."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check the line against the gate: 1-240 characters, not blank."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if not 1 <= len(line) <= 240:
        raise ValueError(
            "entry line must be 1-240 characters, got %d" % len(line)
        )
    return line


def main():
    line = validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Read back and confirm the file holds exactly the validated line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise ValueError("written entry does not match the validated line")
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
