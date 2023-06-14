# poly2mono

Converts polytonic to monotonic.

Uses tkinter for the interface. If you don't need it, just run poly2mono directly onto your string text.

Like https://www.translatum.gr/converter/p2m/polytonika-se-monotonika.php but with no character limitations and with less mistakes. 

Translatum may still be a good option if you don't care too much about occasional typos and don't plan to use it on big texts.

## Setup

Requires tkinter `py -m pip install tk`

## Run

Just run `py main.py` (Windows) on the root of this repo.

You will see a window to put your text and a button to remove the polytonic.

<img src="https://github.com/daxida/poly2mono/blob/master/example.png" style="width: 50%; height: 50%">
          
## Logic
The whole program is nothing but a chained replacement of key value pairs dumped in dictionary.json.

The building process is based on the insertion order of the final dictionary:
1. Treat special cases that require spirits
2. Remove spirits
3. Remove accents from monosyllables (lots of case by case)

By the end, the final dictionary is of the form:
- Regex: intended substitution. Ex: '\\bΣτής\\b': 'Στης'

# Links

There's also this but I haven't tried it: https://github.com/gitpan/Lingua-EL-Poly2Mono
