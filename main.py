"""One-line roast: the gadget you use every day.

Writes a single original roast line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set), for make.fun's
"One-Line Roast: The Gadget You Use Every Day" bounty.

The line roasts the smart fridge: a "smart" gadget that texts you
you're out of milk while you're standing right in front of it
holding the carton. Specific, fresh, and the punch lands on the
last image.
"""

import os
import sys

LINE = "My smart fridge texts me we're out of milk while I'm standing in front of it holding the carton."


def main() -> int:
    # Gate self-check: 1-200 characters, not whitespace-only, one line.
    if not 1 <= len(LINE) <= 200:
        print(f"gate fail: line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("gate fail: line is whitespace-only", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("gate fail: line must be a single line", file=sys.stderr)
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
