import argparse
import json
import re
from typing import Match

from utils.remove_accents import fix_double_accents

"""
    TOFIX:
        ΚΕΦΑΛΑΙΟ Α´ -> ΚΕΦΑΛΑΟ Α´
"""

with open("dictionary.json", "r", encoding="utf-8") as i:
    dictionary = json.load(i)


def poly2mono(text: str) -> str:
    def replace(match: Match[str]) -> str:
        # The FIX and ACCENTS dictionaries work with words (\bword\b)
        # but the SPIRITS works with characters, so we need to take into
        # account this distinction to find the original word from a match.
        word = match.group(0)
        key = f"\\b{word}\\b"
        if word in subdict:
            return subdict[word]
        else:
            return subdict[key]

    text = fix_double_accents(text)
    for subdict in dictionary.values():
        pat = "|".join(key for key in subdict)
        text = re.sub(pat, replace, text)

    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    args = parser.parse_args()
    converted_text = poly2mono(args.text)
    print(converted_text)


if __name__ == "__main__":
    main()
