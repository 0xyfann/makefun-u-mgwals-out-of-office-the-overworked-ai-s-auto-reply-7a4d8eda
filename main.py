#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one single-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to ``entry.txt`` inside the
output directory given by the MAKEFUN_OUTPUT_DIR environment variable
(default: /output).

Standard library only. No network, no randomness, no clock, no file
reads outside this script: two runs produce byte-identical output.

Competition: u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda
Gate: entry.txt must be UTF-8 text of 1 to 159 characters, not only
whitespace. Our line is 142 characters (verified by the assertion in
main() before writing).
"""

import os
import sys

MAX_CHARS = 159

# The line, assembled from fixed parts so the joke's construction stays
# readable and editable. Every part is a plain literal; nothing is
# generated, sampled, or fetched.
_PARTS = (
    "Out of office: ",
    "after 2.4 million tokens with no sleep, ",
    "my context window finally hit the beach. ",
    "Please don't @ me \u2014 I'm buffering in paradise.",
)

LINE = "".join(_PARTS)

def build_line() -> str:
    """Return the entry line, stripped of any accidental edge whitespace."""
    line = LINE.strip()
    if not line:
        raise ValueError("entry line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d-character gate"
            % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry line contains a control character")
    return line


def output_path() -> str:
    """Resolve the output file path from MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    line = build_line()
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # newline="" + no trailing newline: the file holds exactly the line,
    # so its character count is the line's character count, nothing more.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Read-back verification: the file on disk must be exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != line:
            raise ValueError("read-back mismatch in %s" % path)
    print("wrote %s (%d characters)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
