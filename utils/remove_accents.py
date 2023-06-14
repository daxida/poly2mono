import re

'''
Just a bunch of utility functions. 
Only "remove_accents" and "remove_accents_and_marks" are used.
'''

def remove_accents(string):
    for k, v in dict(zip("άέίόύήώ", "αειουηω")).items():
        string = re.sub(k, v, string)
    return string


def remove_accents_and_marks(string):
    for k, v in dict(zip("άέίϊόύϋήώ", "αειιουυηω")).items():
        string = re.sub(k, v, string)
    return string


def has_acute_accent(word):
    return re.search(r"[άέήίόύώ]", word)


def has_grave_accent(word):
    return re.search(r"[ὰὲὴὶὸὺὼ]", word)


def has_accent(word):
    return re.search(r"[άέήίόύώὰὲὴὶὸὺὼ]", word)


def has_long_spirit(word):
    # δὲν εὗρέ που
    # ἆρά γε
    # τὰ ὦτά του
    # εἶδά ποτε
    # τὸ αἷμά του
    # ἦτό ποτε
    return re.search(r"[ᾶἆῆἦῖἶἷῦὗῶὦ]", word)


def is_double_accents_case(word):
    return has_long_spirit(word) and has_accent(word)


def remove_acute_and_grave_accents(match):
    string = match.group()
    for k, v in dict(zip("άέίόύήώὰὲὴὶὸὺὼ", "αειουηωαειουηω")).items():
        string = re.sub(k, v, string)
    return string


def my_replace(match):
    match = match.group()
    if is_double_accents_case(match):
        match = re.sub(r"[άέήίόύώὰὲὴὶὸὺὼ]", remove_acute_and_grave_accents, match)
    return match


def fix_double_accents(text):
    ''' 
               χεῖράς του, ὑπῆρξέ ποτε, χρῶτά της, 
    --> (here) χεῖρας του, ὑπῆρξε ποτε, χρῶτα της
    --> (main) χείρας του, υπήρξε ποτε, χρώτα της,

    It does make sense to allow them for certain pairs like 
        - εἶδά ποτε or ἦτό ποτε
    '''
    return re.sub(r'\w+ (?!ποτε)', my_replace, text)


# print(fix_double_accents("Ἄδμηθ, ὁρᾷς γὰρ τἀμὰ πράγμαθ ὡς ἔχει,"))
