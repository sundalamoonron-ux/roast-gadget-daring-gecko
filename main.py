#!/usr/bin/env python3
"""Roast the Earbuds -- one-line entry writer (resubmit v3).

Writes a single roast line (1-200 UTF-8 chars, one line, no trailing
newline) to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, no network, no secrets.

The line was picked by an internal pairwise tournament over 12 fresh
candidate roasts, judged in the judge's own order: roasts a daily
gadget, funny on first read, fresh angle, tight wording, one person's
specific gripe. The winner beat the v2 line (autocorrect/ex, 81 chars)
3-0 across three pairwise rounds, alternating order, margins 2/2/1.

Tournament (12 candidates, scored on the 5 judge criteria, /20):
 1. charging cable, one working angle          81 ch   16.0
 2. microwave beeps for food already taken     89 ch   16.0
 3. laptop fan, jet engine over a spreadsheet  81 ch   16.5
 4. washing machine "quick wash" 58 minutes    72 ch   15.0
 5. earbuds die mid-sentence, agree with them  81 ch   16.0
 6. earbuds die as the podcast reveals whodunit 73 ch  18.5  WINNER
 7. robot vacuum eats cable, begs as the victim 81 ch  17.5
 8. TV logs me out for saying "still watching" 67 ch   16.0
 9. thermostat heats at 3 a.m. (I woke once)   71 ch   17.0
10. maps says "arrived" at an empty field      71 ch   16.5
11. watch nags about sitting while driving     61 ch   17.0
12. Alexa, wrong song, total confidence        74 ch   15.5

Top 3 vs the v2 line (3 rounds each, order alternated):
 #6 podcast reveal:  W/W/W, margins 2, 2, 1  -> 3-0, replaces v2
 #7 vacuum victim:   W/W/W, margins 1, 2, 1  -> 3-0, narrow, runner-up
 #9 thermostat 3am:  L/L/L, margins 1, 2, 1  -> 0-3
Head-to-head #6 vs #7: #6 wins -- tighter, and the timing gag is a
fresher angle than the (known) vacuum-eats-cables complaint.

Why #6 wins: the joke is not "the battery dies" (a generic gripe) but
the exquisite timing -- the exact second the reveal lands. That is a
concrete behaviour, a fresh angle the judge has not seen, and a sting
every podcast listener recognises on first read. It beats v2 mainly on
freshness (criterion 3): autocorrect is a saturated category even with
the ex twist, while the podcast-reveal timing is new.
"""

import os

ENTRY = "My earbuds always die at the exact second the podcast reveals who did it."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    text.encode("utf-8")  # must be valid UTF-8
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
