"""Dumps the final dictionary used by poly2mono.py into a JSON."""

import json
from pathlib import Path

from monosyllables import create_dictionary_monosyllables
from remove_spirits import create_dictionary_spirits


def create_dictionary() -> None:
    """Cache the dictionary used for poly2mono."""
    # We initialize the final_dictionary with a couple words
    # that don't fit the logic but have a high priority:
    #   πῶς->πώς, πὼς->πως
    #   ποῦ->πού, ποὺ->που
    fix_dict = {
        "\\bπὼς\\b": "πως",
        "\\bποὺ\\b": "που",
    }
    spirits_dict = create_dictionary_spirits()
    accents_dict = create_dictionary_monosyllables()

    # Fix unnecessary ϊ in άϊ:
    # γάϊδουρος => γάιδουρος
    diaeresis = {
        "άϊ": "άι",
        "άϋ": "άυ",
        "έϊ": "έι",
        "έϋ": "έυ",
        "όϊ": "όι",
        "ούϊ": "ούι",  # ἀλληλούϊα
    }

    final_dictionary = {
        "FIX": fix_dict,
        "SPIRITS": spirits_dict,
        "DIAERESIS": diaeresis,
        "ACCENTS": accents_dict,
    }

    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent
    file_path = parent_dir / "dictionary.json"

    with file_path.open("w", encoding="utf-8") as out:
        json.dump(final_dictionary, out, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    create_dictionary()
