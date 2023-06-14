import json
from remove_spirits import create_dictionary_spirits
from monosyllables import create_dictionary_monosyllables
import os

'''
Dumps the final dictionary into a JSON 
'''

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
file_path = os.path.join(parent_dir, "dictionary.json")

def create_dictionary():
    final_dictionary = dict()
    final_dictionary.update(create_dictionary_spirits())
    final_dictionary.update(create_dictionary_monosyllables())

    with open(file_path, 'w', encoding='utf-8') as out:
        json.dump(final_dictionary, out, ensure_ascii=False)

create_dictionary()
