import json
import re

from utils.remove_accents import fix_double_accents

"""
    TOFIX:
        ΚΕΦΑΛΑΙΟ Α´ -> ΚΕΦΑΛΑΟ Α´
"""

with open("dictionary.json", "r", encoding="utf-8") as i:
    dictionary = json.load(i)


def poly2mono(text: str) -> str:
    text = fix_double_accents(text)
    for key, value in dictionary.items():
        text = re.sub(key, value, text)

    return text
