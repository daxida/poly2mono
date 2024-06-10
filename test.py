import unittest
from functools import partialmethod
from typing import Iterator

from poly2mono import poly2mono

Pair = Iterator[tuple[str, str]]
Pairs = list[Pair]


def init_tests() -> Pairs:
    pairs: Pairs = []
    for i in range(10):
        try:
            path = f"tests/{i:02g}_"
            with open(f"{path}poly.txt", "r", encoding="utf-8") as source:
                poly = source.readlines()
            with open(f"{path}mono.txt", "r", encoding="utf-8") as expected:
                mono = expected.readlines()
            pairs.append(zip(poly, mono))
        except FileNotFoundError:
            break

    return pairs


tests_pairs = init_tests()


def test_builder(self, test: Pair) -> None:
    """Compares sentence by sentence for easier visualization"""
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


if __name__ == "__main__":
    unittest.main()
