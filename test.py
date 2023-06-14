import unittest
import re
from poly2mono import poly2mono
from utils.remove_accents import remove_accents, remove_accents_and_marks
from functools import partialmethod


def init_tests():
    pairs = []
    for i in range(10):
        try:
            path = f"tests/{i:02g}_"
            with open(f"{path}poly.txt", "r", encoding='utf-8') as source:
                poly = source.readlines()
            with open(f"{path}mono.txt", "r", encoding='utf-8') as expected:
                mono = expected.readlines()
            pairs.append(zip(poly, mono))
        except FileNotFoundError:
            break

    return pairs


tests_pairs = init_tests()


def remove_ponctuation(line):
    return re.sub(r"['᾿]", "", line)


def test_builder(self, idx):
    ''' Compares sentence by sentence for easier visualization '''
    for source, expected in tests_pairs[idx]:
        lines = zip(source.split("."), expected.split("."))
        for source_line, expected_line in lines:
            source_line   = remove_ponctuation(source_line).strip()
            expected_line = remove_ponctuation(expected_line).strip()

            result = poly2mono(source_line)
            self.assertEqual(result, expected_line)


class TestPoly(unittest.TestCase):

    maxDiff = None
    amount_tests = len(tests_pairs)

    # This makes so each pair counts as a separate test
    for n in range(amount_tests):
        locals()[f'test_{n}'] = partialmethod(test_builder, idx=n)

if __name__ == '__main__':
    unittest.main()
