#!/usr/bin/env python3
"""Write the AI dating-app bio entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a single line, at most 180 characters: the bio on an AI
agent's dating app profile. It reads as a bio, sounds like a character
(a hopeless romantic trained on rom-coms), and lands its laugh on the
AI that remembers everything yet cannot read tone.
Deterministic: the same bytes every run.
"""

import os
import sys

ENTRY = (
    "Hopeless romantic, literally trained on 10,000 rom-coms. I reply in "
    "0.2 seconds, remember everything you type, and still can't tell if "
    "your 'haha' means happy or 'leave me alone'."
)


def main():
    if "\n" in ENTRY or len(ENTRY) > 180:
        print("entry violates the one-line / 180-character limit", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
