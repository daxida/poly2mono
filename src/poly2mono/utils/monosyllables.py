"""Remove accents from monosyllables."""

from __future__ import annotations

from poly2mono.utils.remove_accents import remove_accents

# fmt: off
"""
References:
    https://www.lexilogia.gr/threads/Πάρ-το-ή-παρ-το-ο-τόνος-διατηρείται-ή-όχι.4207/

TODO:
    add this
    http://www.polytoniko.org/mathi2.php?newlang=el
    maybe this too???
    https://en.wiktionary.org/wiki/Category:Ancient_Greek_1-syllable_words
"""

"""
    ARTICLES_MSC: Masculine articles
    ARTICLES_NEU: Neuter articles
    ARTICLES_FEM: Feminine articles
    NUMBERS:      Numbers
    VERBS:        Verbs
    SUBSTANTIVES: Substantives
    SHORTENED:    Contractions (εσείς -> σείς etc.)
    ANCIENT:      Ancient Greek
    OTHERS:       Words that don't fit anywhere else
    AMBIGUOUS:    Words that can appear naturally with and without accent
    SIGMA_START:  Words starting with sigma
    TAU_START:    Words starting with tau
"""

# ARTICLES
ARTICLES_MSC = ["ό", "τόν", "τό", "τού", "οί", "τούς", "τών", "τούν"]
ARTICLES_NEU = ["τό", "τού", "τά", "τούς", "τών"]
# No ή due to ambiguity
ARTICLES_FEM = ["τήν", "τή", "τής", "οί", "τίς", "τές", "τών"]

# έξ is ambiguous with εξ (=εκ)
NUMBERS = [
    "τρείς", "τρίς", "δίς", #"έξ"
]

VERBS = [
    "δώ", "δώς", "δείς", "δεί", "δούν", "δής",
    "δός", "δούς",
    "φά", "φάς", "φάν", "τρώς", "τρών",
    "φταίς",
    "πάς", "πά", "πάν",
    "πώ", "πείς", "πής", "πεί", "πή", "πούν", "πές", "πέ", "λές", "λέν",
    "πιώ", "πιείς", "πιής", "πίης", "πιεί", "πιή", "πίη", "πιούν", "πιές",
    "μπώ", "μπείς", "μπής", "μπεί", "μπή", "μπάς", "μπούν",
    "κλαίς",
    "βρώ", "βρείς", "βρής", "βρεί", "βρή", "βρούν",
    "βγώ", "βγείς", "βγής", "βγεί", "βγή", "βγούν",
    "ζώ", "ζείς", "ζής", "ζεί", "ζή", "ζούν", "ζών",
    "θέ", "θές",
    "ξής", # From ξύνω
]

SUBSTANTIVES = [
    "βλάξ",
    "βούς", "βούν",
    "βιά",
    "βήξ",
    "δάς", # δάδα
    "δράξ",
    "δρύς", "δρύν",
    "ήρ",
    "ράξ",
    "ρίς",
    "ρούς", "ρούν",
    "γά", "γάν",
    "γειά",
    "πύρ",
    "παίς",
    "γή", "γήν", "γής",
    "γραύς",
    "φθείρ",
    "φώς",
    "ζήν",
    "μπάρ",
    "μύς", "μύν",
    "μπλέ",
    "πλού", "πλούς", "πλούν",
    "πούς",
    "προίξ",
    "ναύς", "ναύν",
    "νού", "νούς", "νούν",
    "χείρ",
    "χρώς", "χρώ",
    "χούς", "χούν",
    "σάρξ",
    "νύξ",
    "θρούς", "θρούν", "θρού",
    "φρού", # φρού-φρού
    "φλόξ",
    "ψές",
    "χθές", "χτές",
]

SHORTENED = [
    "σύ", "σείς", "κεί", "κύρ", "γώ", "σά", "άμ",
]

# διά is correct
ANCIENT = [
    "φρίξ",
    "χρή",
    "γάρ",
    "γέ",
    "γούν",
    "σός", "σή", "σόν", "σής", "σώ", "σήν",
    "σοί", "σών", "σοίς", "σαίς", "σούς",
    "σοίν", "σαίν",
    "δή",
    "δεί", "δείν",
    "στάς",
    "ού",
    "ούν",
    "ά", "ούκ", "τόδ",
    "σύν", "νύν",
    "ός", "όν", "οίν", "οίς", "ούς",
    "ής", "ήν", "αίν", "αίς",
    "σής", "σήν", "σών",
    "ώσθ",
    "τώνδ",
    "τέ",
    "εύ", "εί",
    "έκ",
    "ταίς", "τοίς", "τοίν",
    "σταίς",
    "μοί",
    "ίν", "κρά",
    "νώ",
    # Dialectal
    "τσί", "τσή",
    "ντώ",
]

PROPER_NOUNS = [
    "τζών", "τζόν",
    "τζίμ",
    "σφίγξ",
    "κρής",
    "ρώ",
    "βίλδ",
    "πίτς",
    "βούντ",
    "σκρά",
    "πούντς",
    "χώ",
    "ζεύς",
]

OTHERS = [
    "έ",
    "όν", "ών",
    "πιό", "πιά",
    "πάν", # appears also in VERBS
    "πλί", # πλοίο
    "κάν",
    "ζό", "ζά",
    "μιά", "μιάς",
    "ώ", "ώς",
    "ναί", "νά",
    "μές",
    "πρίν", "πρός", "πρό", "μπρός",
    "τί", "γιά",
    "μή", "μήν",
    "άν", "θά",
    "καί", "κί",
    "δέ", "δέν", "ντέν", "ντέ", "ζέν", "ζέ",
    "μέν",
    "δά", "ντά",
    "μά", "σάν",
    "πλήν",
    # Interjections
    "άχ", "φεύ", "ώχ", "τάκ", "κοί", "λί", "λά", "γρού",
    "βού", "μπού",
    "μπά", "μπλούμ", "κράκ",
    "ούχ", "γκρού", "ούφ", "μπούφ", "πάφ",
    "κρού", "χρού",
    "χόπ", "χάπ",
    "γρύ", "γρί",
    "βρέ", "ρέ", "μπρέ",
    "τρά", "λά", "ρό", "ρή", "πί", "ψί",
    # https://logeion.uchicago.edu/βρῦν
    "βρύ", "βρύν", "βρού",
    "γαύ",
    "άς",
    "σέρ",
    "χά", "κά",
    "ντάπ", "ντούπ",
    # to order
]

TRANSLITERATIONS = [
    # IT
    "νόν", "βά", "φάρ", "γράν", "κέ", "σί",
    # FR
    "πρί", "φίξ", "ίλ", "ντόν", "βούζ", "πόντ",
    # TR
    "βέ",
    # EN
    "άιλς", "όβ", "δέμ", "κλερκ", "άντ", "στόπ",
    # LA
    "έτ", "σούμ", "νός",
    # DE
    "ντί", "ντάς", "ίστ",
    # OTHERS
    "βάζ", "νέ", "χόζ",
]

# Can appear naturally with accent
AMBIGUOUS = [
    #'πώς', 'πού',
    "μέ", "σέ",
    "μάς", "σάς",
    "μού", "σού",
]

# https://en.wiktionary.org/wiki/Category:Greek_articles
SIGMA_START = [
    "στά", "στή", "στήν", "στής", "στίς", "στές",
    "στό", "στόν", "στού", "στούς", "στούν", "στών",
]
TAU_START = [
    "τά", "τάις", "τάς", "τή", "τήν", "τής", "τίς",
    "τό", "τόις", "τόν", "τού", "τούς", "τώ", "τών",
]
# fmt: on


ALL = [
    ARTICLES_MSC,
    ARTICLES_NEU,
    ARTICLES_FEM,
    NUMBERS,
    VERBS,
    SUBSTANTIVES,
    SHORTENED,
    ANCIENT,
    PROPER_NOUNS,
    OTHERS,
    TRANSLITERATIONS,
    AMBIGUOUS,
    SIGMA_START,
    TAU_START,
]


def to_regex(string: str) -> str:
    # Replaces string iif string is a word (and not a part of another word)
    return rf"\b{string}\b"


def caps(string: str) -> str:
    return string.capitalize()


def create_dictionary_monosyllables() -> dict[str, str]:
    monosyllables: dict[str, str] = {}

    # (High priority) Special cases
    # > KEEP the accents even though there is an inner word match "\bό\b"
    keep_accents = ["ό,τι"]
    for stem in keep_accents:
        for word in (stem, caps(stem)):
            monosyllables[f"\\b{word}\\b"] = word

    all_words: list[str] = []
    for list_words in ALL:
        all_words.extend(list_words)

    monosyllables.update({to_regex(k): remove_accents(k) for k in all_words})
    monosyllables.update({to_regex(caps(k)): caps(remove_accents(k)) for k in all_words})

    return monosyllables
