"""
Utility functions.
Only "remove_accents" and "remove_accents_and_marks" are used.
"""

import re
from typing import Match


def remove_accents(string: str) -> str:
    translation_table = str.maketrans("άέίόύήώ", "αειουηω")
    return string.translate(translation_table)


def remove_accents_and_marks(string: str) -> str:
    translation_table = str.maketrans("άέίϊόύϋήώ", "αειιιουυηω")
    return string.translate(translation_table)


def has_acute_accent(word: str) -> Match[str] | None:
    return re.search(r"[άέήίόύώ]", word)


def has_grave_accent(word: str) -> Match[str] | None:
    return re.search(r"[ὰὲὴὶὸὺὼ]", word)


def has_accent(word: str) -> Match[str] | None:
    return re.search(r"[άέήίόύώὰὲὴὶὸὺὼ]", word)


def has_long_spirit(word: str) -> Match[str] | None:
    # δὲν εὗρέ που
    # ἆρά γε
    # τὰ ὦτά του
    # εἶδά ποτε
    # τὸ αἷμά του
    # ἦτό ποτε
    return re.search(r"[ᾶἆῆἦῖἶἷῦὗῶὦ]", word)


def is_double_accents_case(word: str) -> bool:
    return has_long_spirit(word) is not None and has_accent(word) is not None


def remove_acute_and_grave_accents(match: Match[str]) -> str:
    gp = match.group()
    translation_table = str.maketrans("άέίόύήώὰὲὴὶὸὺὼ", "αειουηωαειουηω")
    return gp.translate(translation_table)


def double_accents_repl(match: Match[str]) -> str:
    gp = match.group()
    if is_double_accents_case(gp):
        return re.sub(r"[άέήίόύώὰὲὴὶὸὺὼ]", remove_acute_and_grave_accents, gp)
    return gp


def fix_double_accents(text: str) -> str:
    """
               χεῖράς του, ὑπῆρξέ ποτε, χρῶτά της,
    --> (here) χεῖρας του, ὑπῆρξε ποτε, χρῶτα της
    --> (main) χείρας του, υπήρξε ποτε, χρώτα της,

    It does make sense to allow them for certain pairs like
        - εἶδά ποτε or ἦτό ποτε
    """
    return re.sub(r"\w+ (?!ποτε)", double_accents_repl, text)


if __name__ == "__main__":
    #       v        v    <= Modifies these two
    test = "Ἄδμηθ, ὁρᾷς γὰρ τἀμὰ πράγμαθ ὡς ἔχει,"
    print(fix_double_accents(test))
