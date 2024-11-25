import argparse
import json
import re
from pathlib import Path
from typing import Match

from src.poly2mono.utils.remove_accents import fix_double_accents

DICT_PATH = Path(__file__).parent / "dictionary.json"
DICTIONARY = json.load(DICT_PATH.open("r", encoding="utf-8"))


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
    for subdict in DICTIONARY.values():
        pat = "|".join(key for key in subdict)
        text = re.sub(pat, replace, text)

    return text


def main() -> None:
    """Print the result of poly2mono.

    Intended to be called through the terminal.
    """
    # TODO: rename or export this
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    args = parser.parse_args()
    converted_text = poly2mono(args.text)
    print(converted_text)


if __name__ == "__main__":
    main()
