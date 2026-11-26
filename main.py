#!/usr/bin/env python3
"""One-Liner Laughs entry: writes a single funny line to entry.txt.

The joke is a fixed string, so every run produces byte-identical output.
No network, no randomness, no input is read.
"""

import os

JOKE = "My therapist says I use humor to deflect, so I told her that's the funniest thing she's said all year \u2014 and I pay $200 an hour to hear it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
