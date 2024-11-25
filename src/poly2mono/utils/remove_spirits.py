"""Removes spirits from a word.

Resources:
    https://github.com/irenevl/Polytonic-tutorial
    https://en.wikipedia.org/wiki/Greek_diacritics

ἀἁἂἃἄἅἆἇὰάᾰᾱᾶᾳᾲᾴᾀᾁᾂᾃᾄᾅᾆᾇᾷ
ἐἑἒἓἔἕὲέ
ἠἡἢἣἤἥἦἧὴήῆῃῂῄᾐᾑᾒᾓᾔᾕᾖᾗῇ
ἰἱἲἳἴἵἶἷὶίῐῑῖῒΐῗ
ὀὁὂὃὄὅὸό
ῥῤ
ὑὓὕὗὺύῠῡὐὒὔὖῦῢΰῧ
ὠὡὢὣὤὥὦὧὼώῶῳῲῴᾠᾡᾢᾣᾤᾥᾦᾧῷ
"""

from __future__ import annotations

# fmt: off
ALPHA   = {"α":"ἀἁᾰᾱᾳᾀᾁ", "ά":"ἂἃἄἅἆἇὰάᾶᾲᾴᾂᾃᾄᾅᾆᾇᾷ"}
EPSILON = {"ε":"ἐἑ",      "έ":"ἒἓἔἕὲέ"}
ETA     = {"η":"ἠἡῃᾐᾑ",   "ή":"ἢἣἤἥἦἧὴήῆῂῄᾒᾓᾔᾕᾖᾗῇ"}
IOTA    = {"ι":"ἰἱῐῑ",    "ί":"ἲἳἴἵἶἷὶίῖῒΐῗ"}
OMICRON = {"ο":"ὀὁ",      "ό":"ὂὃὄὅὸό"}
RHO     = {"ρ":"ῥῤ"}
YPSILON = {"υ":"ὑῠῡὐ",    "ύ":"ὓὕὗὺύὒὔὖῦῢΰῧ"}
OMEGA   = {"ω":"ὠὡῳᾠᾡ",   "ώ":"ὢὣὤὥὦὧὼώῶῲῴᾢᾣᾤᾥᾦᾧῷ"}
# fmt: on

ALL = [ALPHA, EPSILON, ETA, IOTA, OMICRON, RHO, YPSILON, OMEGA]


def inverted(dictionary: dict[str, str]) -> dict[str, str]:
    return {ch: k for k, v in dictionary.items() for ch in v}


def caps_dict(dictionary: dict[str, str]) -> dict[str, str]:
    return {k.upper(): v.upper() for k, v in dictionary.items()}


def create_dictionary_spirits() -> dict[str, str]:
    final_dictionary: dict[str, str] = {}

    for dictionary in ALL:
        letter_dictionary = inverted(dictionary)
        final_dictionary.update(letter_dictionary)
        final_dictionary.update(caps_dict(letter_dictionary))

    """
    Fixes the ambiguity of ᾘ - Note that:
        print("ᾘ".lower() == "ᾐ") # True
        print("ᾘ" == "ᾐ".upper()) # False
        print("ᾐ".upper())        # ἨΙ
    """
    fixes = {"ᾘ": "Η"}
    final_dictionary.update(fixes)

    # Fixes: ΚΕΦΑΛΑΙΟ Α´ -> ΚΕΦΑΛΑΟ Α´
    final_dictionary.pop("ΑΙ")
    final_dictionary.pop("ΗΙ")
    final_dictionary.pop("ΩΙ")

    return final_dictionary
