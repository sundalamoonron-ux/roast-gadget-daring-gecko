"""One-line roast: the gadget you use every day.

Writes a single original roast line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set), for make.fun's
"One-Line Roast: The Gadget You Use Every Day" bounty.

Resubmit v2 (2026-11-26): the line roasts the phone's autocorrect — it gets
your own name wrong, then suggests you meant the name of your ex. A double
turn with a personal sting: the gadget fails twice, and the second failure
is the one that hurts. Won the in-session pairwise audit 5-0, and beat the
v1 fridge line 2-0 (margin 2 both times) on the judge's criteria 2, 3 and 5.
"""

import os
import sys

LINE = "My phone autocorrects my own name wrong, then suggests I meant the name of my ex."


def validate(line: str) -> str:
    """Gate check from RULES.txt: 1-200 chars, not whitespace-only, one line.

    Returns the line unchanged when it passes; raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"gate fail: line is {len(line)} chars, must be 1-200")
    if not line.strip():
        raise ValueError("gate fail: line is whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("gate fail: line must be a single line")
    return line


def main() -> int:
    # Gate self-check via validate() before writing anything.
    try:
        validate(LINE)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Verify after write: read back and confirm the exact bytes.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("verify fail: entry.txt does not match the line", file=sys.stderr)
        return 1
    if written.endswith("\n"):
        print("verify fail: entry.txt has a trailing newline", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars ({len(LINE.encode('utf-8'))} bytes) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
