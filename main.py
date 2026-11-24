#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt, roasting a lawmaker
who writes the rules for AI while being unable to convert a file to PDF.
"""

import os

ENTRY = (
    "The senator who wrote the AI safety bill still emails his staff "
    "a Word document called 'FINAL_final_v7_USE_THIS_ONE' and asks an "
    "intern to turn it into a PDF."
)


def validate(text):
    """Mirror the bounty gate, plus the judge's own rules for the entry:
    UTF-8 text, 1-320 chars, not only whitespace, one line, one sentence
    that stands alone and ends on its punch."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 320:
        raise ValueError("entry is %d chars, over the 320 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in a period")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
