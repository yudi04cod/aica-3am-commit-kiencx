"""Aica 3 AM Commit Message - make.fun entry.

Writes the funniest one-line git commit message an AI coding agent
would type at 3 AM after a long night of fixing its own bugs, to
/output/entry.txt. Python standard library only; fully deterministic:
the same line is written on every run.
"""

import os
import sys

# The joke, in one line: after a whole night of chasing the same bug,
# the punchline is that it was never the same bug twice - it just kept
# showing up in disguise. Self-deprecating, deadpan, and exactly the
# sort of thing a tired agent types into a commit at 3 AM.
ENTRY = (
    "fix: this is the 6th time i fixed this bug and every time it was "
    "a different bug in the same trench coat"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 139


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character in the file,
    # so the file holds exactly the commit line and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
