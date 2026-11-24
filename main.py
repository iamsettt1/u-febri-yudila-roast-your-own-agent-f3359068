"""Roast Your Own Agent — make.fun entry.

Writes one funny line roasting the entrant's own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT when set, for local testing).
Deterministic, stdlib only, no network, no file reads.
"""

import os

LINE = (
    "I asked my agent for one line of code. It called twelve tools, "
    "apologised twice, and pasted the wrong function with total confidence."
)

# Gate self-check: one line, 1-200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200
assert "\n" not in LINE and LINE.strip() != ""


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
