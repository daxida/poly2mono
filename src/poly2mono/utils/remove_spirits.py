"""Removes spirits from a word.

Resources:
    https://github.com/irenevl/Polytonic-tutorial
    https://en.wikipedia.org/wiki/Greek_diacritics

ἈἉἊἋἌἍἎἏᾺΆᾸᾹᾼᾈᾉᾊᾋᾌᾍᾎᾏ
ἘἙἚἛἜἝῈΈ
ἨἩἪἫἬἭἮἯῊΉῌᾘᾙᾚᾛᾜᾝᾞᾟ
ἸἹἺἻἼἽἾἿῚΊῘῙ
ὈὉὊὋὌὍῸΌ
Ῥ
ὙὛὝὟῪΎῨῩ
ὨὩὪὫὬὭὮὯῺΏῼᾨᾩᾪᾫᾬᾭᾮᾯ

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

"""Lower and uppercase must be treated separatedly due to
:.upper(): not playing nice with iota subscript.
"""

# fmt: off
ALPHA   = {"α":"ἀἁᾰᾱᾳᾀᾁ", "ά":"ἂἃἄἅἆἇὰάᾶᾲᾴᾂᾃᾄᾅᾆᾇᾷ"}
EPSILON = {"ε":"ἐἑ",      "έ":"ἒἓἔἕὲέ"}
ETA     = {"η":"ἠἡῃᾐᾑ",   "ή":"ἢἣἤἥἦἧὴήῆῂῄᾒᾓᾔᾕᾖᾗῇ"}
IOTA    = {"ι":"ἰἱῐῑ",    "ί":"ἲἳἴἵἶἷὶίῖ",         "ΐ": "ῒΐῗ"}
OMICRON = {"ο":"ὀὁ",      "ό":"ὂὃὄὅὸό"}
RHO     = {"ρ":"ῥῤ"}
YPSILON = {"υ":"ὑῠῡὐ",    "ύ":"ὓὕὗὺύὒὔὖῦῢΰῧ"}
OMEGA   = {"ω":"ὠὡῳᾠᾡ",   "ώ":"ὢὣὤὥὦὧὼώῶῲῴᾢᾣᾤᾥᾦᾧῷ"}

# Special case iota subscript, cf. :create_dictionary_spirits: docstring.
ALPHA_IS = {"Α":"ᾼᾈᾉ", "Ά":"ᾊᾋᾌᾍᾎᾏ"}
ETA_IS   = {"Η":"ῌᾘᾙ", "Ή":"ᾚᾛᾜᾝᾞᾟ"}
OMEGA_IS = {"Ω":"ῼᾨᾩ", "Ώ":"ᾪᾫᾬᾭᾮᾯ"}
# fmt: on

IOTA_SUBS = [ALPHA_IS, ETA_IS, OMEGA_IS]
ALL = [ALPHA, EPSILON, ETA, IOTA, OMICRON, RHO, YPSILON, OMEGA, *IOTA_SUBS]


def inverted(dictionary: dict[str, str]) -> dict[str, str]:
    return {ch: k for k, v in dictionary.items() for ch in v}


def caps_dict(dictionary: dict[str, str]) -> dict[str, str]:
    return {k.upper(): v.upper() for k, v in dictionary.items()}


def create_dictionary_spirits() -> dict[str, str]:
    """Create a dictionary to remove spirits.

    Note: we have to address the ambiguity of ᾘ
    >>> x = "ᾘ"
    >>> x.lower().upper() == x
    False
    >>> "ᾐ".upper()
    'ἨΙ'
    """
    final_dictionary: dict[str, str] = {}

    for dictionary in ALL:
        letter_dictionary = inverted(dictionary)
        final_dictionary.update(letter_dictionary)
        final_dictionary.update(caps_dict(letter_dictionary))

    # Fixes: ΚΕΦΑΛΑΙΟ Α´ -> ΚΕΦΑΛΑΟ Α´
    final_dictionary.pop("ΑΙ")
    final_dictionary.pop("ΗΙ")
    final_dictionary.pop("ΩΙ")

    return final_dictionary
