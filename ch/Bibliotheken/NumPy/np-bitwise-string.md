title: NumPy Bitwise-Operationen und String-Funktionen
stage: alpha
timevalue: 2.5
difficulty: 2
assumes: np-Einführung, np-array, np-array2, py-Fstrings, py-List-Comprehensions
---

[SECTION::goal::idea,experience]

- Ich verstehe die grundlegenden Bitwise-Operationen in NumPy und kann sie anwenden.
- Ich verstehe, wie das Ergebnis einer Bitwise-Operation vom Datentyp der Array-Elemente abhängt.
- Ich kann NumPy-String-Funktionen für die Textverarbeitung einsetzen.
- Ich kann die Laufzeit einer vektorisierten Operation mit der einer Python-Schleife vergleichen und
  weiß, dass ein Beschleunigungsfaktor nur zusammen mit seinem Vergleichspartner aussagekräftig ist.
- Ich habe gemessen, dass die Vektorisierung bei String-Operationen deutlich weniger einbringt als
  bei numerischen.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet neben numerischen auch bitweise und stringbezogene Operationen an, die direkt auf der
binären bzw. textuellen Darstellung der Daten arbeiten.
Diese Aufgabe behandelt die wichtigsten Bitwise-Funktionen sowie ausgewählte NumPy-String-Funktionen
für die Textverarbeitung.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für die Bitwise-Operationen in dieser Aufgabe sind Grundkenntnisse der Binärdarstellung von Zahlen
und des Zweierkomplements nötig (wie Ganzzahlen als Bitfolgen dargestellt werden, wie negative
Zahlen darin kodiert werden).
Falls Ihnen diese fehlen, arbeiten Sie zuerst die folgenden Quellen durch:

- [Dualsystem (Wikipedia)](https://de.wikipedia.org/wiki/Dualsystem)
- [Zweierkomplement (Wikipedia)](https://de.wikipedia.org/wiki/Zweierkomplement)

Die Zeitschätzungen der Bitwise-Abschnitte setzen dieses Vorwissen voraus; wer es sich erst parallel
aneignet, braucht entsprechend länger.

### Grundlagen der NumPy-Bitwise-Operationen

Bitwise-Operationen arbeiten direkt auf der binären Darstellung von Zahlen: Jede Position einer
Binärzahl repräsentiert eine Zweierpotenz, z. B. steht `00001101` für `1×8 + 1×4 + 0×2 + 1×1 = 13`.

Praktisch braucht man das vor allem, um mehrere Informationen in einer einzigen Zahl unterzubringen
und einzeln wieder herauszuholen: Statusflags oder Zugriffsrechte liegen als einzelne Bits in einem
Integer, eine RGB-Farbe steckt als drei Bytes in einem 32-Bit-Wert.
`bitwise_and` prüft oder maskiert dann einzelne Bits, `left_shift` und `right_shift` schieben das
gewünschte Feld an die richtige Stelle.

Python selbst kennt bereits die Operatoren `&`, `|`, `^`, `~`, `<<` und `>>` für Bitwise-Operationen
auf einzelnen ganzen Zahlen.
NumPy bietet dieselben Operationen als Funktionen an; gegenüber den Python-Operatoren auf einzelnen
Zahlen unterscheiden sie sich in zwei Punkten:

- **Vektorisierung**: Die Operation wird gleichzeitig auf jedes Element eines Arrays angewendet,
  statt nur auf eine einzelne Zahl.
- **Feste Bit-Breite**: Python-Ganzzahlen haben beliebig viele Stellen und laufen nie über.
  NumPy-Arrays haben dagegen einen festen `dtype` (z. B. `int8` mit genau 8 Bit), der die Anzahl
  verfügbarer Bits begrenzt.
  Das ist wichtig für `invert()` und die Verschiebungsoperationen weiter unten, da das Ergebnis
  innerhalb dieser festen Bit-Breite berechnet wird.

Auf Arrays lassen sich auch die Operatoren selbst verwenden; sie tun dort genau dasselbe wie die
Funktionen (`a & b` ist gleichwertig zu `np.bitwise_and(a, b)`, `a ^ b` zu `np.bitwise_xor(a, b)`,
`~a` zu `np.invert(a)`, `a << n` zu `np.left_shift(a, n)`).
Die Kommentare in den folgenden Beispielen nutzen diese kürzere Schreibweise.

Die wichtigsten Bitwise-Funktionen in NumPy sind:

- `numpy.bitwise_and()`: Führt eine bitweise UND-Operation durch
- `numpy.bitwise_or()`: Führt eine bitweise ODER-Operation durch
- `numpy.bitwise_xor()`: Führt eine bitweise XOR-Operation durch
- `numpy.invert()`: Führt eine bitweise Negation durch
- `numpy.left_shift()`: Verschiebt Bits nach links
- `numpy.right_shift()`: Verschiebt Bits nach rechts

Um sich die Bitdarstellung einer Zahl ausgeben zu lassen (z. B. um Ergebnisse der obigen Funktionen
nachzuvollziehen), bietet NumPy `binary_repr`:

```python
numpy.binary_repr(num, width=None)
```

- `num`: die darzustellende Ganzzahl
- `width` (Standard `None`): genaue Stellenzahl der Ausgabe.
  Positive Zahlen werden mit führenden Nullen aufgefüllt (`width=8` liefert für `13` die Ausgabe
  `00001101`), negative als Zweierkomplement dieser Breite (`width=8` liefert für `-4` die Ausgabe
  `11111100`).
  Reicht die Breite für die Zahl nicht aus, gibt es einen `ValueError`.

```python
import numpy as np

print(np.binary_repr(13, width=8))  # '00001101'
```

<!-- time estimate: 10 min -->

### Bitweise UND-, ODER- und XOR-Operationen: `bitwise_and`, `bitwise_or`, `bitwise_xor`

```python
numpy.bitwise_and(x1, x2)  # bitweises UND: 1 nur dort, wo beide Operanden 1 sind
numpy.bitwise_or(x1, x2)   # bitweises ODER: 1 dort, wo mindestens ein Operand 1 ist
numpy.bitwise_xor(x1, x2)  # bitweises XOR: 1 dort, wo genau ein Operand 1 ist
```

- `x1`, `x2`: Ganzzahl- oder Boolean-Arrays (gleicher Form oder broadcastbar), die bitweise
  verknüpft werden

Bei booleschen Arrays (`dtype=np.bool_`) entsprechen die Bitwise-Operationen den logischen
Operationen UND/ODER/XOR.
Das ist der häufigste Anlass, in NumPy überhaupt zu `&` und `|` zu greifen: Beim Filtern werden
damit mehrere Bedingungen zu einer Maske verknüpft, etwa `arr[(arr > a) & (arr < b)]` in
[PARTREF::np-index-slice].

```python
import numpy as np

# Bitweise Operationen mit Arrays
arr1 = np.array([True, True, False], dtype=np.bool_)
arr2 = np.array([True, False, False], dtype=np.bool_)

result_and = np.bitwise_and(arr1, arr2)
result_or = np.bitwise_or(arr1, arr2)
result_xor = np.bitwise_xor(arr1, arr2)

print("AND:", result_and)  # [ True False False]
print("OR:", result_or)    # [ True  True False]
print("XOR:", result_xor)  # [False  True False]
```

An der ersten Position sind beide Operanden `True`; genau dort trennen sich ODER (`True`) und XOR
(`False`).

[ER] Wenden Sie die drei Verknüpfungen auf Ganzzahl-Arrays an:

- Erstellen Sie zwei Arrays mit ganzen Zahlen: `a` mit den Werten `[13, 17]` und `b` mit den Werten
  `[5, 24]`
- Führen Sie `np.bitwise_and(a, b)`, `np.bitwise_or(a, b)` und `np.bitwise_xor(a, b)` durch
- Geben Sie sowohl die Ergebnisse als auch die binären Darstellungen aus (verwenden Sie
  `np.binary_repr()` mit `width=8`, damit die Bitmuster untereinander ausgerichtet sind)
- Erklären Sie in Kommentaren, wie die Ergebnisse zustande kommen

<!-- time estimate: 15 min -->

### Bit-Verschiebungen: `left_shift` und `right_shift`

Bit-Verschiebungsoperationen verschieben die Bits einer Zahl um eine feste Anzahl Positionen:

```python
numpy.left_shift(x1, x2)   # verschiebt die Bits von x1 um x2 Positionen nach links
numpy.right_shift(x1, x2)  # verschiebt die Bits von x1 um x2 Positionen nach rechts
```

- `x1`: Ganzzahl-Array (oder einzelne Ganzzahl), dessen Bits verschoben werden
- `x2`: Anzahl der Positionen, um die verschoben wird

```python
import numpy as np

# Links-Verschiebung entspricht Multiplikation mit 2ⁿ
left_result = np.left_shift(10, 2)  # 10 << 2 = 40
print("10 << 2 =", left_result)

# Rechts-Verschiebung entspricht ganzzahliger Division durch 2ⁿ
right_result = np.right_shift(40, 2)  # 40 >> 2 = 10
print("40 >> 2 =", right_result)
```

Diese Entsprechung gilt aber nur, solange das Ergebnis in den verwendeten `dtype` passt.
Bits, die über dessen Breite hinausgeschoben werden, gehen verloren:

```python
import numpy as np

schmal = np.array([64, 100], dtype=np.int8)
print(np.left_shift(schmal, 2))                  # [   0 -112]
print(np.left_shift(np.array([64, 100]), 2))     # [256 400] (Standard-dtype, breit genug)
```

Bei `64 = 01000000` wandert das einzige gesetzte Bit aus den 8 Bit hinaus, übrig bleibt `0`.
Bei `100 = 01100100` bleibt das Bitmuster `10010000` stehen; als `int8` gelesen ist das `-112`, denn
dort zeigt das oberste Bit das Vorzeichen an (mehr dazu im Abschnitt zu `invert` weiter unten).

[EQ] Berechnen Sie im Kopf das Ergebnis von `np.left_shift(7, 3)` und erklären Sie Ihren
Rechenweg mit der binären Darstellung.

[ER] Arbeiten Sie mit Bit-Verschiebungen in Arrays:

- Erstellen Sie ein Array `values` mit den Werten `[5, 12, 25, 48]`
- Verschieben Sie alle Werte um 1 Position nach links
- Verschieben Sie alle Werte um 2 Positionen nach rechts
- Vergleichen Sie die Ergebnisse mit den arithmetischen Operationen (`*2`, `//4` und `/4`), z. B. mit
  dem aus [PARTREF::np-array] bekannten `np.array_equal()`
- Ein RGB-Farbwert steckt als drei Bytes in einer Zahl: bei `0xFF8800` (die Schreibweise `0x...`
  steht für eine Hexadezimalzahl, je zwei Stellen entsprechen einem Byte) ist `0xFF` = 255 der Rot-,
  `0x88` = 136 der Grün- und `0x00` = 0 der Blauanteil.
  Erstellen Sie ein Array `farben` mit den Werten `[0xFF8800, 0x3366CC]` und holen Sie mit
  `np.right_shift()` und `np.bitwise_and()` die drei Farbanteile als je ein eigenes Array heraus
- Geben Sie zusätzlich `np.right_shift(farben, 8)` ohne die Maskierung aus und erklären Sie im
  Kommentar, wozu `np.bitwise_and()` hier nötig ist

[HINT::Ich weiß beim Farbwert nicht, um wie viele Stellen ich schieben muss]
Ein Byte sind 8 Bit.
Der Blauanteil steht ganz unten, der Grünanteil 8 Bit darüber, der Rotanteil noch einmal 8 Bit
darüber.
`np.bitwise_and(x, 0xFF)` behält von `x` genau die untersten 8 Bit.
[ENDHINT]

[EQ] Bei `5` und `25` weicht Ihr Verschiebungsergebnis von einer gewöhnlichen Division ab: `5 / 4`
wäre `1.25`, die Verschiebung liefert `1`.
Schreiben Sie die Bitmuster von `5` und des verschobenen Ergebnisses auf und benennen Sie, welche
Bits dabei verschwinden.
Warum kann eine Rechts-Verschiebung deshalb immer nur abschneiden und nie runden?

<!-- time estimate: 30 min -->

### Bitweise Negation: `invert`

`invert()` kehrt jedes einzelne Bit einer Zahl um (aus 0 wird 1 und umgekehrt):

```python
numpy.invert(x)
```

- `x`: Ganzzahl- oder Boolean-Array, dessen Bits umgekehrt werden

Bei vorzeichenbehafteten Ganzzahltypen wie `int8` wird das Ergebnis als Zweierkomplement
interpretiert: Das höchstwertige Bit zeigt das Vorzeichen an (1 = negativ), und eine negative Zahl
`-n` wird als Bitmuster von `n - 1` mit umgekehrten Bits dargestellt.
Deshalb ergibt das Umkehren aller Bits einer Zahl `n` dort `-(n + 1)`:

```python
import numpy as np

# Bitweise Negation
arr = np.array([1, 2], dtype=np.int8)
inverted = np.invert(arr)
print("Original:", arr)
print("Inverted:", inverted)  # [-2 -3]
```

Um ein Array in einen anderen `dtype` umzuwandeln, bietet NumPy die Array-Methode `astype`:

```python
ndarray.astype(dtype)
```

- `dtype`: Ziel-Datentyp, in den die Elemente des Arrays umgewandelt werden (z. B. `np.uint8`); es
  wird immer ein neues Array zurückgegeben, das ursprüngliche bleibt unverändert

[ER] Untersuchen Sie den Einfluss des `dtype` auf `invert()`:

- Erstellen Sie ein Array `arr` mit den Werten `[3, 10]` als `np.int8` und wenden Sie `np.invert()`
  darauf an
- Wandeln Sie `arr` mit `arr.astype(np.uint8)` um und wenden Sie `np.invert()` auch darauf an
- Geben Sie beide Ergebnisse aus

[EQ] Warum liefert `np.invert()` bei `int8` negative Werte, bei `uint8` aber nicht, obwohl
dieselben Bits umgekehrt werden?
Nutzen Sie Ihre Ergebnisse aus dem vorigen Schritt für Ihre Erklärung.

[HINT::Ich sehe nicht, wie dasselbe Bitmuster zwei verschiedene Zahlen ergeben kann]
Schreiben Sie sich zuerst die 8-Bit-Darstellung von `3` auf (`np.binary_repr(3, width=8)`), kehren
Sie jedes Bit einzeln um, und prüfen Sie erst danach, welche Zahl dieses Bitmuster im
Zweierkomplement bzw. als vorzeichenlose Zahl repräsentiert.
[ENDHINT]

<!-- time estimate: 20 min -->

### Grundlagen der NumPy-String-Funktionen: `strings.upper`, `strings.lower`

NumPy bietet zwei Module für vektorisierte String-Verarbeitung: `numpy.strings` ist das aktuelle,
`numpy.char` gilt laut
[NumPy String Functions](https://numpy.org/doc/stable/reference/routines.strings.html)
als Legacy.
Wir verwenden daher `numpy.strings`, außer für `split`/`join`, die es dort nicht gibt.

[FOLDOUT::Warum gibt es zwei Module?]
`numpy.char` war vor NumPy 2.0 der einzige Ort für String-Funktionen und nur auf Strings fester
Breite ausgelegt; es erhält keine Updates mehr und könnte in einer künftigen Hauptversion entfernt
werden.
[ENDFOLDOUT]

Diese Funktionen arbeiten vektorisiert auf String-Arrays: Sie wenden eine String-Operation in einem
einzigen Aufruf auf jedes Element eines Arrays an.
Wie bei einzelnen Python-Strings verändern sie das ursprüngliche Array nicht, sondern geben immer
ein neues Array mit den Ergebnissen zurück.

Der Geschwindigkeitsvorteil gegenüber einer Python-Schleife fällt hier deutlich kleiner aus als bei
numerischen NumPy-Operationen.
Im letzten Abschnitt dieser Aufgabe messen Sie beide Vorteile selbst nach und vergleichen sie.

```python
numpy.strings.upper(a)  # wandelt jedes Element in Großbuchstaben um
numpy.strings.lower(a)  # wandelt jedes Element in Kleinbuchstaben um
```

- `a`: Array von Strings, dessen Elemente umgewandelt werden

```python
import numpy as np

# String-Arrays erstellen
strings = np.array(['Hello', 'World', 'NumPy'])
print("Original:", strings)

# Grundlegende String-Operationen
upper_strings = np.strings.upper(strings)
lower_strings = np.strings.lower(strings)
print("Uppercase:", upper_strings)
print("Lowercase:", lower_strings)
```

<!-- time estimate: 5 min -->

### String-Verbindungen und Multiplikationen: `strings.add`, `strings.multiply`

```python
numpy.strings.add(x1, x2)     # hängt die Elemente von x1 und x2 paarweise aneinander
numpy.strings.multiply(a, i)  # wiederholt jedes Element von a i-mal
```

- `x1`, `x2`: Arrays von Strings gleicher Form oder broadcastbar, deren Elemente paarweise
  aneinandergehängt werden
- `a`: Array von Strings, das wiederholt wird
- `i`: Anzahl der Wiederholungen pro Element

```python
import numpy as np

# String-Verbindung
arr1 = np.array(['Hello', 'Good'])
arr2 = np.array([' World', 'bye'])
combined = np.strings.add(arr1, arr2)
print("Combined:", combined)  # ['Hello World' 'Goodbye']

# String-Wiederholung
repeated = np.strings.multiply(np.array(['Python ', 'NumPy ']), 3)
print("Repeated:", repeated)  # ['Python Python Python ' 'NumPy NumPy NumPy ']
```

[ER] Implementieren Sie verschiedene String-Operationen:

- Erstellen Sie ein Array `names` mit den Werten `['Alice', 'Bob', 'Charlie']`
- Erstellen Sie ein Array `greetings` mit den Werten `['Hallo', 'Hi', 'Hey']`
- Verbinden Sie `greetings` und `names` mit `np.strings.add()` zu Grußformeln der Form
  `'Hallo Alice'`, also mit einem Leerzeichen zwischen Gruß und Namen
- Verwenden Sie `np.strings.multiply()`, sodass jeder Name zweimal hintereinander steht
- Konvertieren Sie alle Namen in Großbuchstaben mit `np.strings.upper()`

[HINT::Ich sehe nicht, wie ich mit `np.strings.add()` ein Leerzeichen dazwischen bekomme]
Die Funktion nimmt genau zwei Argumente, es braucht also zwei Schritte.
Hängen Sie zuerst an jedes Element von `greetings` ein Leerzeichen an — dank Broadcasting genügt
dafür der einzelne String `' '` — und verbinden Sie das Ergebnis dann mit `names`.
[ENDHINT]

<!-- time estimate: 15 min -->

### String-Formatierung und -Bearbeitung: `strings.center`, `strings.strip`, `strings.replace`

```python
numpy.strings.center(a, width, fillchar=' ')  # zentriert jeden String auf die Breite width
numpy.strings.strip(a)                        # entfernt Leerzeichen am Anfang und Ende
numpy.strings.replace(a, old, new)            # ersetzt alle Vorkommen von old durch new
```

- `a`: Array von Strings, das bearbeitet wird
- `width`: Zielbreite, auf die zentriert wird; geht die Aufteilung nicht glatt auf, stehen links
  und rechts unterschiedlich viele Füllzeichen
- `fillchar` (Standard `' '`): Füllzeichen links/rechts vom zentrierten String
- `old`, `new`: zu ersetzendes Teilstück bzw. Ersatz-Teilstück (bei `replace`)

```python
import numpy as np

# String-Zentrierung und Polsterung
centered = np.strings.center(np.array(['NumPy', 'Pandas']), 12, fillchar='*')
print("Centered:", centered)  # ['***NumPy****' '***Pandas***']

# String-Bereinigung
messy_strings = np.array(['  hello  ', '  world  '])
cleaned = np.strings.strip(messy_strings)
print("Cleaned:", cleaned)  # ['hello' 'world']

# String-Ersetzung
text = np.array(['Python', 'NumPy', 'Pandas'])
replaced = np.strings.replace(text, 'y', 'i')
print("Replaced:", replaced)  # ['Pithon' 'NumPi' 'Pandas']
```

[ER] Arbeiten Sie mit String-Formatierung:

- Erstellen Sie ein Array `words` mit den Werten `['Style', 'Yellow', 'Syntax']`
- Zentrieren Sie jeden String in einem Feld der Breite 10 mit `np.strings.center()`
- Erstellen Sie ein Array `messy_words` mit den Werten
  `['  Style  ', '   Yellow   ', ' Syntax ']`
- Verwenden Sie `np.strings.strip()` zum Entfernen der Leerzeichen
- Nutzen Sie `np.strings.replace()`, um in `words` alle `'y'` durch `'i'` zu ersetzen

[EQ] Eines der drei Wörter kommt aus der Ersetzung unverändert heraus.
Welches, und woran liegt das?
Was müssten Sie ändern, damit auch dort ersetzt wird?

<!-- time estimate: 20 min -->

### String-Teilung, Zeichen-Verbindung und Teilstring-Suche: `char.split`, `char.join`, `strings.find`

`find` gibt es in beiden Modulen; wir nutzen daher wie zuvor das aktuelle `numpy.strings`, für
`split`/`join` bleibt es bei `numpy.char`.

[FOLDOUT::Warum fehlen `split` und `join` in `numpy.strings`?]
`split` liefert für jedes Element eine unterschiedlich lange Python-Liste von Teilstrings zurück;
das lässt sich nicht als einheitliches Array-Element abbilden und passt daher nicht zu den übrigen
Funktionen aus `numpy.strings`, die immer genau ein Ergebnis pro Element liefern.
`join` liefert dagegen durchaus ein gewöhnliches String-Array zurück, wurde bei der Einführung von
`numpy.strings` aber schlicht nicht mit übernommen.
[ENDFOLDOUT]

```python
numpy.char.split(a, sep=None)     # teilt jeden String an sep in eine Liste von Teilstrings
numpy.char.join(sep, seq)         # fügt sep zwischen die einzelnen Zeichen jedes Strings in seq ein
numpy.strings.find(a, sub)        # erste Fundposition von sub, oder -1 falls nicht enthalten
```

- `a`, `seq`: Array von Strings, das verarbeitet wird
- `sep`: Trennzeichen; bei `split` (Standard `None`) wird ohne Angabe an beliebigem Leerraum getrennt;
  bei `join` ist `sep` verpflichtend und wird zwischen die Zeichen innerhalb jedes einzelnen Strings
  von `seq` eingefügt (nicht zwischen mehrere Array-Elemente)
- `sub`: gesuchtes Teilstück (bei `find`)

```python
import numpy as np

# String-Teilung
sentences = np.array(['Hello World', 'NumPy Arrays'])
split_words = np.char.split(sentences)
print("Split:", split_words)  # [list(['Hello', 'World']) list(['NumPy', 'Arrays'])]

# Trennzeichen zwischen die Zeichen jedes Strings einfügen
codes = np.array(['abc', 'xyz'])
joined = np.char.join('-', codes)
print("Joined:", joined)  # ['a-b-c' 'x-y-z']

# Zeichen in Strings finden
emails = np.array(['user@domain.com', 'admin@site.org'])
at_positions = np.strings.find(emails, '@')
print("Position of '@':", at_positions)  # [4 5]
# Gibt -1 zurück, wenn nicht gefunden
not_found = np.strings.find(emails, 'xyz')
print("Position of 'xyz':", not_found)  # [-1 -1]
```

[ER] Implementieren Sie erweiterte String-Operationen:

- Erstellen Sie ein Array `codes` mit den Produktcodes `['AB-12-XY', 'CD-34-ZT']`
- Teilen Sie `codes` mit `np.char.split()` an den Bindestrichen auf
- Erstellen Sie ein Array `abbr` mit den Kürzeln `['DE', 'FR']` und fügen Sie mit `np.char.join()`
  zwischen die Buchstaben jedes Kürzels einen Punkt ein
- Verwenden Sie `np.strings.replace()`, um in `codes` alle Bindestriche durch Unterstriche zu
  ersetzen
- Ermitteln Sie mit `np.strings.find()` die Position des ersten Bindestrichs in jedem Element von
  `codes`

<!-- time estimate: 10 min -->

### Geschwindigkeitsvergleich mit einer Python-Schleife: `strings.startswith`

Wie groß der eingangs erwähnte Geschwindigkeitsvorteil wirklich ist, messen Sie jetzt selbst nach.

```python
numpy.strings.startswith(a, prefix)  # prüft für jedes Element, ob es mit prefix beginnt
```

- `a`: Array von Strings, das geprüft wird
- `prefix`: das zu suchende Präfix

```python
import numpy as np

files = np.array(['summary.txt', 'report_2023.csv', 'report_2024.csv'])
mask = np.strings.startswith(files, 'report')
print(mask)  # [False  True  True]
```

Um den Zeitunterschied zwischen zwei Operationen zu messen, bietet Pythons Standardbibliothek das
`time`-Modul: `time.perf_counter()` gibt einen Zeitpunkt in Sekunden mit der höchsten verfügbaren
Auflösung zurück und ist damit für kurze Laufzeiten gedacht (anders als `time.time()`, das die
verstellbare Systemuhr abliest).
Ruft man es vor und nach einer Operation auf, ergibt die Differenz die benötigte Laufzeit.
Eine einzelne Messung schwankt allerdings stark, je nachdem was der Rechner sonst gerade tut;
deshalb misst man mehrfach und nimmt die kürzeste Zeit, denn sie ist am wenigsten gestört.
Mit der in [PARTREF::py-Fstrings] eingeführten f-String-Formatierung mit Präzisionsangabe (`:.5f`)
lässt sich die Ausgabe auf sinnvolle Nachkommastellen begrenzen:

```python
import time

zeiten = []
for lauf in range(5):
    start = time.perf_counter()
    # ... Operation, deren Dauer gemessen werden soll ...
    zeiten.append(time.perf_counter() - start)
dauer = min(zeiten)
print(f'Kürzeste Dauer: {dauer:.5f} Sekunden')
```

[ER] Messen Sie den Geschwindigkeitsunterschied zwischen `np.strings.startswith` und einer
Python-Schleife an einem größeren Array.
Die Schleife messen Sie dabei zweimal, einmal über das Array selbst und einmal über eine daraus
erzeugte Python-Liste.
Zum Schluss messen Sie dasselbe für eine numerische Operation, damit Sie einen Maßstab haben, an dem
Sie die String-Faktoren einordnen können.
Legen Sie alle fünf Messungen in eine gemeinsame Schleife, sodass in jedem Durchlauf jede Operation
einmal an die Reihe kommt, jede mit ihrer eigenen Zeitenliste.
So treffen Schwankungen der Maschine alle Messungen gleichmäßig und die Faktoren bleiben
untereinander vergleichbar:

- Erstellen Sie ein Array `words` mit 100000 Strings der Form `'produkt0'`, `'produkt1'`, ...,
  `'produkt99999'` (z. B. mit einer List Comprehension aus [PARTREF::py-List-Comprehensions] und
  `np.array`)
- Messen Sie mit dem `time`-Modul die Laufzeit von `np.strings.startswith(words, 'produkt123')` und
  nehmen Sie wie oben gezeigt die kürzeste aus 5 Wiederholungen
- Messen Sie auf dieselbe Weise die Schleife `[w.startswith('produkt123') for w in words]`
- Messen Sie auf dieselbe Weise dieselbe Schleife über `words_list = list(words)`, wobei die
  Umwandlung selbst außerhalb der Messung stattfindet
- Messen Sie nach demselben Muster eine numerische Operation: `zahlen * 2` auf einem mit
  `np.arange(100000)` erzeugten Array gegen die Schleife `[x * 2 for x in zahlen_liste]`, wobei
  `zahlen_liste = list(range(100000))` wieder außerhalb der Messung entsteht — in dieser Liste sollen
  bewusst echte Python-Ganzzahlen stehen und nicht die Elemente des Arrays
- Geben Sie alle fünf Zeiten (5 Nachkommastellen, `:.5f`) aus, dazu die beiden String-Faktoren
  gegenüber `np.strings.startswith` und den Zahlen-Faktor gegenüber `zahlen * 2`
  (je 1 Nachkommastelle, `:.1f`)

[HINT::Wie überprüfe ich mein Ergebnis?]
`np.strings.startswith` ist deutlich schneller als beide Schleifen, und die Schleife über das Array
ist noch einmal erheblich langsamer als die über die Liste.
Auch bei der numerischen Messung ist der NumPy-Aufruf klar schneller als die Schleife.
Konkrete Zahlen hängen stark von Ihrer Maschine ab; entscheidend sind diese Verhältnisse, nicht
bestimmte Werte.
[ENDHINT]

[EQ] Beide Schleifen berechnen dasselbe Ergebnis, liefern aber deutlich verschiedene Faktoren.
Welche der beiden Messungen beantwortet die Frage "Wie viel bringt hier die Vektorisierung?" fairer,
und was folgt daraus für eine Aussage der Form "NumPy ist N-mal schneller als Python"?

[EQ] Stellen Sie den Zahlen-Faktor und den String-Faktor der Listen-Schleife nebeneinander.
Bestätigt Ihre Messung die Aussage vom Beginn des String-Teils, dass Vektorisierung dort weniger
einbringt als bei numerischen Operationen?
Begründen Sie mit Ihren Zahlen.

<!-- time estimate: 25 min -->

### Weiterführend

- [NumPy Bitwise Operations](https://numpy.org/doc/stable/reference/routines.bitwise.html)
- [NumPy String Functions (`numpy.strings`)](https://numpy.org/doc/stable/reference/routines.strings.html):
  aktuelles Modul, in dieser Aufgabe überwiegend verwendet
- [NumPy String Operations (`numpy.char`)](https://numpy.org/doc/stable/reference/routines.char.html):
  Legacy-Modul, hier nur noch für `split`/`join` verwendet

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::2] + [EREFQ::2]: die drei Farbanteile entstehen mit der jeweils richtigen
  Verschiebungsweite **und** der Maskierung `np.bitwise_and(..., 0xFF)`; wer die Maske weglässt,
  erhält für Rot und Grün Werte weit über 255 und damit keine Farbanteile mehr.
  Die Erklärung dazu benennt, dass eine Verschiebung die herausgeschobenen Bits verwirft und die
  übrigen stehen lässt; dieselbe Einsicht wird in der Frage am Beispiel `5 >> 2` von der anderen
  Seite geprüft
- [EREFQ::3]: die Erklärung, warum `int8` und `uint8` bei `invert()` unterschiedliche Vorzeichen
  liefern, verweist korrekt auf die Interpretation des Bitmusters (Vorzeichenbit vs. kein
  Vorzeichenbit) statt auf einen Unterschied in der eigentlichen Bit-Operation
- [EREFR::6]: `np.char.join` ist richtig verstanden: das Trennzeichen steht zwischen den Zeichen
  jedes einzelnen Strings (`'DE'` → `'D.E'`), nicht zwischen den Array-Elementen; wer es als
  Verbinder der Elemente auffasst, erzeugt hier ein falsches Ergebnis.
  `split`/`replace`/`find` liefern für alle Elemente die korrekten Ergebnisse
- [EREFR::7] + [EREFQ::5] + [EREFQ::6]: alle fünf Zeiten sind gemessen, die Schleife über das Array
  ist klar langsamer als die über die Liste, und der Zahlen-Faktor liegt klar über dem String-Faktor
  der Listen-Schleife (konkrete Zahlen sind maschinenabhängig und daher kein Prüfkriterium).
  Studierende erkennen, dass die Messung über die Liste der fairere Vergleich für die Vektorisierung
  ist, dass ein einzelner Faktor ohne Angabe des Vergleichspartners wenig aussagt, und dass ihre
  eigenen Zahlen die kleinere Wirkung der Vektorisierung bei String-Operationen bestätigen

### Fragen und Python-Dateien
[INCLUDE::ALT:np-bitwise-string.md]

[ENDINSTRUCTOR]
