#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes one warning label for a time machine (61 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no input, no randomness.
"""

import os

# Label dibangun dari bagian-bagiannya: kepala peringatan + setup + punchline.
# Setup: "You are 12th in the queue." — punchline: "The other eleven are you."
BAGIAN_1 = "WARNING: You are 12th in the queue."
BAGIAN_2 = "The other eleven are you."

LABEL = " ".join([BAGIAN_1, BAGIAN_2])


def main():
    os.makedirs("/output", exist_ok=True)
    # Exact bytes, no trailing newline: the gate counts characters,
    # and the tie-break favours the smaller text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
