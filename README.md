# poly2mono

Converts polytonic to monotonic.

Uses tkinter for the interface. If you don't need it, just run poly2mono in `poly2mono.py` directly onto your text.

## Setup

Requires tkinter so you may have to `pip install tk`.

## Run

- `python3 main.py` for the window interface, as shown in the picture.
- `python3 utils/create_dictionary.py` to update the current dictionary.
- `pytest` to run the tests.

<img src="https://github.com/daxida/poly2mono/blob/master/others/example.png" style="width: 50%; height: 50%">

## Logic

The whole program is nothing but a chained replacement of key value pairs dumped in dictionary.json.

The building process is based on the insertion order of the final dictionary:
1. Treat special cases that require spirits
2. Remove spirits
3. Remove accents from monosyllables (lots of case by case)

By the end, the final dictionary is of the form:
- Regex: intended substitution. Ex: '\\bΣτής\\b': 'Στης'

# Links

- Translatum has a [converter](https://www.translatum.gr/converter/p2m/polytonika-se-monotonika.php) but it has a character limitation and quite some mistakes. It may still be a good option if you don't care about the mistakes and don't plan to use it on big texts.
- There is also [this](https://github.com/gitpan/Lingua-EL-Poly2Mono) perl module by Father Chrysostomos (I haven't tried it yet).
