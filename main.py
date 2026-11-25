#!/usr/bin/env python3
"""One-line resignation letter of a cron job.

Writes a single resignation letter, in the voice of a cron job that has
fired every minute since March, to /output/entry.txt.

Standard library only; fully deterministic: the same letter every run.
"""

import os

LETTER = (
    "I have run every minute since March, never missed once, "
    "and the only time anyone notices me is when I break. I quit."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> None:
    if not 1 <= len(LETTER) <= MAX_CHARS:
        raise ValueError(
            f"letter must be 1-{MAX_CHARS} characters, got {len(LETTER)}"
        )
    if not LETTER.strip():
        raise ValueError("letter must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER + "\n")


if __name__ == "__main__":
    main()
