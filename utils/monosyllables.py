"""
Remove accents from monosyllables.
"""

from remove_accents import remove_accents
from typing import List, Dict

# fmt: off
'''
References:
    https://www.lexilogia.gr/threads/Πάρ-το-ή-παρ-το-ο-τόνος-διατηρείται-ή-όχι.4207/

TODO: 
    add this 
    http://www.polytoniko.org/mathi2.php?newlang=el
    maybe this too???
    https://en.wiktionary.org/wiki/Category:Ancient_Greek_1-syllable_words
'''

'''
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
'''

# ARTICLES
ARTICLES_MSC = ['ό', 'τόν', 'τό', 'τού', 'οί', 'τούς', 'τών', 'τούν']
ARTICLES_NEU = ['τό', 'τού', 'τά', 'τούς', 'τών']
# No ή due to ambiguity
ARTICLES_FEM = ['τήν', 'τή', 'τής', 'οί', 'τίς', 'τές', 'τών']

# έξ is ambiguous with εξ (=εκ)
NUMBERS = [
    "τρείς", "τρίς", 'δίς', #"έξ"
]

VERBS = [
    "δώ", "δεί",
    "φά", "φάν", 
    "πάς", "πά",
    "πώ", "πής", 'πούν', 'πές', 'πέ', 'πή', 'πείς',
    'μπής', 'μπή',
    'μπάς',
    'κλαίς', 
    'λές',
    'βρή', 'βρεί',
    'βγώ', 'βγούν', 'βγή', 'βγής',
    'ζή', 'ζής', 'ζώ',
    'φάς',
]

SUBSTANTIVES = [
    'ούς',
    'ρούς', 'ρούν',
    'γειά',
    'βιά', 
    'πύρ',
    'παίς', 
    'γή', 'γήν', 'γής',
    'φώς',
    'ζήν',
    'πλού', 'πλούς', 'πλούν',
    'πούς', 
    'νού', 'νούς', 'νούν',
    'χείρ',
    'νύξ',
    'θρούς', 'θρούν', 'θρού',
    'φρού', # φρού-φρού
]

SHORTENED = [
    'σύ', 'σείς', 'κεί', 'κύρ', 'γώ', 'θέ', 'σά'
]

# διά is correct
ANCIENT = [
    'στάς', 
    'ού',
    'ά', 'ούκ', 'γάρ', 'τόδ',
    'σύν', 'νύν',
    'όν', 'οίς',
    'ήν', 'ής', 
    'σής', 'σήν', 'σών',
    'ώσθ',
    'τώνδ',
    'εύ',
    'τοίς',
    'σώ', 'σοί',
    'μοί', 
    'ίν', 'κρά',
]

OTHERS = [
    'πιό', 'πιά',
    'πάν', 'κάν',
    'μιά', 'μιάς',
    'ώ', 'ώς',
    'ναί', 'νά',
    'μές',
    'πρίν', 'πρός', 'πρό',
    'τί', 'γιά',
    'μή', 'μήν',
    'άν', 'θά',
    'καί', 'κί',   
    'δέ', 'δέν', 'μέν',
    'μά', 'σάν',
    'πλήν', 
    'άχ', 'φεύ', 'ώχ', 'δά',
    'βρέ', 'ρέ', 'μπρέ', 
    'γαύ', 
    'άς', 
    # to order
]

# Can appear naturally with accent
AMBIGUOUS = [
    #'πώς', 'πού',
    'μέ', 'σέ', 
    'μάς', 'σάς', 
    'μού', 'σού',
]

# https://en.wiktionary.org/wiki/Category:Greek_articles
SIGMA_START = [
    'στά', 'στή', 'στήν', 'στής', 'στίς', 
    'στό', 'στόν', 'στού', 'στούς', 'στών'
]
TAU_START = [
    'τά', 'τάις', 'τάς', 'τή', 'τήν', 'τής', 'τίς', 
    'τό', 'τόις', 'τόν', 'τού', 'τούς', 'τώ', 'τών'
]


ALL = [
    ARTICLES_MSC,
    ARTICLES_NEU,
    ARTICLES_FEM,
    NUMBERS,
    VERBS,
    SUBSTANTIVES,
    SHORTENED,
    ANCIENT,
    OTHERS,
    AMBIGUOUS,
    SIGMA_START,
    TAU_START
]
# fmt: on


def to_regex(string: str):
    # Replaces string iif string is a word (and not a part of another word)
    return rf"\b{string}\b"


def CAPS(string: str) -> str:
    return string[0].upper() + string[1:]


def create_dictionary_monosyllables() -> Dict[str, str]:
    monosyllables: Dict[str, str] = dict()

    all_words: List[str] = []
    for list_words in ALL:
        all_words.extend(list_words)

    monosyllables.update({to_regex(k): remove_accents(k) for k in all_words})
    monosyllables.update(
        {to_regex(CAPS(k)): CAPS(remove_accents(k)) for k in all_words}
    )

    return monosyllables


"""
def quick_test():
    def translate(dictionary, text):
        for k, v in dictionary.items():
            text = re.sub(k, v, text)
        return text

    dictionary = create_dictionary_monosyllables()
    # print(dictionary)

    text = "Ελπίζουμε η στό Στό Στόν Στόνι Τό ιστοσελίδα αυτή νά πείσει όσους επισκέπτες θεωρούν τό πολυτονικό ξεπερασμένο καί άχρηστο ότι συμβαίνει ακριβώς τό αντίθετο: οι τόνοι καί τά πνεύματα είναι αναπόσπαστο μέρος τής ελληνικής γλώσσας· θεωρούμε δέ ότι η «μονοτονική μεταρρύθμιση» τού 1982 ήταν ένα τραγικό λάθος εις βάρος τού ελληνικού πολιτισμού. Καί τό χειρότερο: η μονοτονική γραφή επιβλήθηκε τότε από τήν κρατική εξουσία στά σχολεία (συχνά μέ τήν συνένοχη συμμετοχή ανενημέρωτων ή ανευθύνων δασκάλων καί καθηγητών φιλολόγων) μέ αποτέλεσμα οι σημερινοί νέοι νά μεγάλωσαν μέ τήν πεποίθηση ότι οι τόνοι καί τά πνεύματα είναι άχρηστοι καί ανήκουν στό παρελθόν. Είναι χρέος μας νά επανορθώσουμε αυτό τό λάθος."
    text_expected = "Ελπίζουμε η στο Στο Στον Στόνι Το ιστοσελίδα αυτή να πείσει όσους επισκέπτες θεωρούν το πολυτονικό ξεπερασμένο και άχρηστο ότι συμβαίνει ακριβώς το αντίθετο: οι τόνοι και τα πνεύματα είναι αναπόσπαστο μέρος της ελληνικής γλώσσας· θεωρούμε δε ότι η «μονοτονική μεταρρύθμιση» του 1982 ήταν ένα τραγικό λάθος εις βάρος του ελληνικού πολιτισμού. Και το χειρότερο: η μονοτονική γραφή επιβλήθηκε τότε από την κρατική εξουσία στα σχολεία (συχνά με την συνένοχη συμμετοχή ανενημέρωτων ή ανευθύνων δασκάλων και καθηγητών φιλολόγων) με αποτέλεσμα οι σημερινοί νέοι να μεγάλωσαν με την πεποίθηση ότι οι τόνοι και τα πνεύματα είναι άχρηστοι και ανήκουν στο παρελθόν. Είναι χρέος μας να επανορθώσουμε αυτό το λάθος."
    
    for word, expected in zip(text.split(), text_expected.split()):
        assert translate(dictionary, word) == expected, f"word {word}, expected {expected}"

    print("Passed the test!")


quick_test()
"""
