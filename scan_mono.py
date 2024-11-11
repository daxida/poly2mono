"""Scan for accented monosyllables.

Read a polytonic text, remove the polytonic and return
all the monosyllables that still have an accent.

This is useful to identify monosyllables that should be
stripped from their accent after polytonic removal.
"""

import argparse
import re
from pathlib import Path

from greek_accentuation.syllabify import syllabify

from poly2mono import poly2mono

VOWEL_ACCENTED = re.compile(r"[έόίύάήώ]")

CORRECT_MONO = {"είς", "έν", "έκ", "έξ", "πώς", "πού", "ή", "σόι"}

CORRECT_NOT_MONO = {"δαυίδ", "πλάι", "άι"}
"""Correct spelling but wrongly treated as monosyllable by syllabify."""

TRANSLITERATIONS_IT = {"νόν", "βά", "φάρ", "γράν", "κέ"}
TRANSLITERATIONS_FR = {"πρί", "φίξ", "ίλ"}
TRANSLITERATIONS_TR = {"βέ"}
TRANSLITERATIONS_EN = {"άιλς", "όβ", "δέμ"}
TRANSLITERATIONS_LA = {"έτ", "σούμ"}
TRANSLITERATIONS_OTHERS = {"βάζ", "ίστ", "νέ"}

TRANSLITERATIONS = {
    *TRANSLITERATIONS_IT,
    *TRANSLITERATIONS_FR,
    *TRANSLITERATIONS_TR,
    *TRANSLITERATIONS_EN,
    *TRANSLITERATIONS_LA,
    *TRANSLITERATIONS_OTHERS,
}

TYPOS = {"άγ", "φαί", "φαίς", "τρός", "τεύχ"}

OTHERS = {
    "λέν",
    "έστ",
    "σί",
    "μείς",
    "χέι",
    "μί",
    "μνά",
    "ρείζ",
    "τύ",
    "πλί",
    "λάι",
    "τώκ",
    "νάι",
    "χρόν",
    "ψί",
    "βόι",
    "σεί",
    "θείς",
    "ώκ",
}

TO_IGNORE = {*CORRECT_MONO, *CORRECT_NOT_MONO, *TRANSLITERATIONS, *TYPOS, *OTHERS}


def get_accented_monosyllables(text: str) -> list[str]:
    accented_monosyllables = set()
    word_re = re.compile(r"(?<!\S)[\w᾽]+(?!\S)")

    for line in re.split(r"[\n.]", text):
        words = word_re.findall(line, re.UNICODE)

        for word in words:
            if "᾽" in word:
                continue

            word = word.lower()
            syllables = syllabify(word)
            if len(syllables) == 1 and VOWEL_ACCENTED.search(syllables[-1]):
                if word not in TO_IGNORE:
                    print(f"{word:5} | {line:50}")
                    accented_monosyllables.add(word)

    return sorted(accented_monosyllables)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("ipath", type=Path, help="Path to the input text file.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    ipath = args.ipath
    text = ipath.open("r", encoding="utf-8").read()
    text_mono = poly2mono(text)
    accented_monosyllables = get_accented_monosyllables(text_mono)
    print("Accented monosyllables found:", accented_monosyllables)
