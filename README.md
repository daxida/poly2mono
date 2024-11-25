# poly2mono

Converts polytonic to monotonic.

Easily exportable to any language by using `dictionary.json`.

## Setup

```
pip install git+https://github.com/daxida/poly2mono
```

## Run

```
# Launches the GUI
p2m
# Updates the dictionary (if you want to add extra edge cases)
update
```

Run `pytest` for testing.

<img src="https://github.com/daxida/poly2mono/blob/master/others/example.png" style="width: 50%; height: 50%">

## Logic

The whole program is a chained replacement of key value pairs dumped in `dictionary.json`. It requires 4 passes of the original string.

The order of replacements is relevant. We use the fact that python dictionaries preserve insertion order.

Note that (1) and (4) are substitution at word level, but (2) and (3) are at character level.

1. Treat two special cases that require spirits:
   πως and που, which can be accented or not depending on the polytonic diacritic.
2. Remove spirits, f.e. "ἏΙ" => "Ά"
3. Remove diaeresis, f.e. "ούϊ" => "ούι"
4. Remove accents from monosyllables (lots of case by case)

# Links

- Translatum has a [converter](https://www.translatum.gr/converter/p2m/polytonika-se-monotonika.php) but it has a character limitation and quite some mistakes. It may still be a good option if you don't care about the mistakes and don't plan to use it on big texts.
- There is also [this](https://github.com/gitpan/Lingua-EL-Poly2Mono) perl module by Father Chrysostomos (I haven't tried it yet).
- [modern_greek_accentuation](https://github.com/PicusZeus/modern_greek_accentuation) also has a `convert_to_monotonic` function.
