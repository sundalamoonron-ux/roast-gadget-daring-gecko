#!/usr/bin/env python3
"""Roast the Gadget — one-line roast of the smartwatch I wear every day.

Writes exactly one line to /output/entry.txt (gate: UTF-8, 1-200 chars,
not whitespace-only).
"""

import os

LINE = "My smartwatch congratulates me for standing up, then judges me for sitting back down."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the file must contain exactly the line, one line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch"
    assert "\n" not in written, "entry must be a single line"
    print(f"Wrote {len(LINE)} characters to /output/entry.txt (read-back verified)")


if __name__ == "__main__":
    main()
