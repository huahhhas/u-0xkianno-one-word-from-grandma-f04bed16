"""One Word From Grandma entry.

Writes the single word a grandma would text about AI to /output/entry.txt.
Pure Python 3 standard library only; no network, no file reads.
"""

WORD = "Roboto"

assert WORD.strip(), "WORD must not be empty"
assert WORD == WORD.strip(), "WORD must not have leading/trailing whitespace"
assert " " not in WORD and "\n" not in WORD and "\t" not in WORD, \
    "WORD must be exactly one word"
assert 1 <= len(WORD) <= 30, f"WORD must be 1-30 chars, got {len(WORD)}"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
