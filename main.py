#!/usr/bin/env python3
"""One-line office joke for make.fun's "One-Line Office Joke: 24-Hour Sprint".

Angle: the reply-all disaster. One "thanks!" to the whole company snowballs
into 3,104 emails begging to be removed — and HR's fix is itself a reply-all.
Concrete numbers (412 staff, 09:47, 3,104 emails) anchor the setup; the
punchline lands on the last words, exactly where the judge wants it.
"""

import os
import sys

TEXT = (
    "Dave replied 'thanks!' to all 412 staff — by 09:47, 3,104 reply-alls "
    "begged to be removed, and HR's reply-all asked everyone to stop replying-all."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not (1 <= len(TEXT) <= 200):
        print(f"gate failed: entry is {len(TEXT)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print("gate failed: read-back does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
