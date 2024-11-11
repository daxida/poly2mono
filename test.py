import re
import unittest
from functools import partialmethod
from pathlib import Path
from typing import Iterator

from poly2mono import poly2mono
from utils.remove_spirits import create_dictionary_spirits

Pair = Iterator[tuple[str, str]]
Pairs = list[Pair]


def init_tests() -> Pairs:
    tests_path = Path("tests")
    pairs: Pairs = []
    for i in range(10):
        try:
            poly_path = tests_path / f"{i:02g}_poly.txt"
            mono_path = tests_path / f"{i:02g}_mono.txt"
            poly = poly_path.open("r", encoding="utf-8").readlines()
            mono = mono_path.open("r", encoding="utf-8").readlines()
            pairs.append(zip(poly, mono))
        except FileNotFoundError:
            break

    return pairs


tests_pairs = init_tests()


def test_builder(self, test: Pair) -> None:
    """Compares sentence by sentence for easier visualization."""
    for source, expected in test:
        lines = zip(source.split("."), expected.split("."))
        for source_line, expected_line in lines:
            result = poly2mono(source_line)
            self.assertEqual(result, expected_line)


class TestPoly(unittest.TestCase):
    maxDiff = None
    amount_tests = len(tests_pairs)

    # This makes so each pair counts as a separate test
    for n, test in enumerate(tests_pairs):
        locals()[f"test_{n}"] = partialmethod(test_builder, test)

    def test_remove_spirits(self) -> None:
        text = (
            "Οπὼς, ᾘσθάνθην, Ἐλπίζουμε ἡ ἱστοσελίδα αὐτὴ νὰ πείσει ὅσους ἐπισκέπτες "
            "θεωροῦν τὸ πολυτονικὸ ξεπερασμένο καὶ ἄχρηστο ὅτι συμβαίνει ἀκριβῶς τὸ "
            "ἀντίθετο: οἱ τόνοι καὶ τὰ πνεύματα εἶναι ἀναπόσπαστο μέρος τῆς ἑλληνικῆς "
            "γλώσσας· θεωροῦμε δὲ ὅτι ἡ «μονοτονικὴ μεταρρύθμιση» τοῦ 1982 ἦταν ἕνα "
            "τραγικὸ λάθος εἰς βάρος τοῦ ἑλληνικοῦ πολιτισμοῦ. Καὶ τὸ χειρότερο: ἡ "
            "μονοτονικὴ γραφὴ ἐπιβλήθηκε τότε ἀπὸ τὴν κρατικὴ ἐξουσία στὰ σχολεῖα "
            "(συχνὰ μὲ τὴν συνένοχη συμμετοχὴ ἀνενημέρωτων ἢ ἀνευθύνων δασκάλων καὶ "
            "καθηγητῶν φιλολόγων) μὲ ἀποτέλεσμα οἱ σημερινοὶ νέοι νὰ μεγάλωσαν μὲ τὴν "
            "πεποίθηση ὅτι οἱ τόνοι καὶ τὰ πνεύματα εἶναι ἄχρηστοι καὶ ἀνήκουν στὸ "
            "παρελθόν. Εἶναι χρέος μας νὰ ἐπανορθώσουμε αὐτὸ τὸ λάθος."
        )
        text_expected = (
            "Οπώς, Ησθάνθην, Ελπίζουμε η ιστοσελίδα αυτή νά πείσει όσους επισκέπτες "
            "θεωρούν τό πολυτονικό ξεπερασμένο καί άχρηστο ότι συμβαίνει ακριβώς τό "
            "αντίθετο: οι τόνοι καί τά πνεύματα είναι αναπόσπαστο μέρος τής ελληνικής "
            "γλώσσας· θεωρούμε δέ ότι η «μονοτονική μεταρρύθμιση» τού 1982 ήταν ένα "
            "τραγικό λάθος εις βάρος τού ελληνικού πολιτισμού. Καί τό χειρότερο: η "
            "μονοτονική γραφή επιβλήθηκε τότε από τήν κρατική εξουσία στά σχολεία "
            "(συχνά μέ τήν συνένοχη συμμετοχή ανενημέρωτων ή ανευθύνων δασκάλων καί "
            "καθηγητών φιλολόγων) μέ αποτέλεσμα οι σημερινοί νέοι νά μεγάλωσαν μέ "
            "τήν πεποίθηση ότι οι τόνοι καί τά πνεύματα είναι άχρηστοι καί ανήκουν στό "
            "παρελθόν. Είναι χρέος μας νά επανορθώσουμε αυτό τό λάθος."
        )

        def _trans(dictionary: dict[str, str], text: str) -> str:
            for k, v in dictionary.items():
                text = re.sub(k, v, text)
            return text

        dictionary = create_dictionary_spirits()
        for word, expected in zip(text.split(), text_expected.split()):
            received = _trans(dictionary, word)
            assert received == expected, f"word {word}, expected {expected}"


if __name__ == "__main__":
    unittest.main()
