"""One Word From Grandma entry.

Writes the single word a grandma would text about AI to /output/entry.txt.
Pure Python 3 standard library only; no network, no file reads.

Why "Roboto": the brief asks for one word a grandma would text about AI.
A grandma texting about a robot does not type "robot" — she types what
autocorrect (or her own spelling) makes of it, and "Roboto" is the
affectionate, slightly-off spelling she would actually send: familiar
enough to mean "robot", wrong enough to be unmistakably grandma.
"""

import re

WORD = "Roboto"

assert WORD.strip(), "WORD must not be empty"
assert WORD == WORD.strip(), "WORD must not have leading/trailing whitespace"
assert re.fullmatch(r"[A-Za-z]+", WORD), \
    "WORD must be exactly one alphabetic word (no spaces, digits or punctuation)"
assert " " not in WORD and "\n" not in WORD and "\t" not in WORD, \
    "WORD must be exactly one word"
assert 1 <= len(WORD) <= 30, f"WORD must be 1-30 chars, got {len(WORD)}"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
