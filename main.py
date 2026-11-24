#!/usr/bin/env python3
"""Write one bizarre-but-real startup pitch sentence to entry.txt.

The pitch: renting emotional-support goats to burned-out tech offices.
The sentence names the odd thing sold (goat rentals), who pays
(stressed tech companies), and why it holds together (a live goat
lowers stress better than a wellness app, at a price offices already
pay for perks).
"""

import os

SENTENCE = (
    "We rent emotional-support goats to burned-out tech offices, because "
    "companies happily pay $800 a month for a goat that cuts sick days "
    "better than any wellness app."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
