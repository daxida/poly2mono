import argparse
import json
import re
from pathlib import Path
from typing import Match

from poly2mono.utils.remove_accents import fix_double_accents

DICT_PATH = Path(__file__).parent / "dictionary.json"
DICTIONARY = json.load(DICT_PATH.open("r", encoding="utf-8"))


def poly2mono(text: str) -> str:
    def replace(m: Match[str]) -> str:
        """FIX and ACCENTS dictionaries work with words (\bword\b)
        but SPIRITS and DIAERESIS work with characters.
        """
        word = m.group(0)
        if word in subdict:
            return subdict[word]

        # Do not remove accents from abbreviated words:
        # > Ἂς πά᾽ νὰ εἶσαι.
        # > Ας πά᾽ να είσαι.
        # This has the side effect of not removing accents
        # when the apostrophe mark is used to quote.
        if m.end() < len(text) and text[m.end()] in "'᾽":
            return word

        return subdict[f"\\b{word}\\b"]

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
