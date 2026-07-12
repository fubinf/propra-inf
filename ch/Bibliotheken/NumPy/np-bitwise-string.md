title: NumPy Bitwise-Operationen und String-Funktionen
stage: alpha
timevalue: 1.5
difficulty: 2
requires: np-Einführung
---

[SECTION::goal::idea,experience]

- Ich verstehe die grundlegenden Bitwise-Operationen in NumPy und kann sie anwenden.
- Ich verstehe, wovon das Ergebnis einer Bitwise-Operation abhängt.
- Ich kann NumPy-String-Funktionen für die Textverarbeitung einsetzen.

[ENDSECTION]

[SECTION::background::default]

Bitwise-Operationen arbeiten auf der binären Darstellung von Zahlen. String-Funktionen 
ermöglichen vektorisierte Textverarbeitung in NumPy-Arrays.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwissen

Für die Bitwise-Operationen in dieser Aufgabe sind Grundkenntnisse der Binärdarstellung von 
Zahlen und des Zweierkomplements hilfreich (wie Ganzzahlen als Bitfolgen dargestellt werden, 
wie negative Zahlen darin kodiert werden). Falls Ihnen diese fehlen, helfen folgende Quellen:

- [Dualsystem (Wikipedia)](https://de.wikipedia.org/wiki/Dualsystem)
- [Zweierkomplement (Wikipedia)](https://de.wikipedia.org/wiki/Zweierkomplement)

### Grundlagen der NumPy Bitwise-Operationen

Bitwise-Operationen arbeiten direkt auf der binären Darstellung von Zahlen: Jede Position 
einer Binärzahl repräsentiert eine Zweierpotenz, z. B. steht `00001101` für 
`1×8 + 1×4 + 0×2 + 1×1 = 13`.

Python selbst kennt bereits die Operatoren `&`, `|`, `^`, `~`, `<<` und `>>` für 
Bitwise-Operationen auf einzelnen ganzen Zahlen. NumPy bietet dieselben Operationen als 
Funktionen an, die zusätzlich zwei Dinge ermöglichen:

- **Vektorisierung**: Die Operation wird gleichzeitig auf jedes Element eines Arrays angewendet, 
  statt nur auf eine einzelne Zahl.
- **Feste Bit-Breite**: Python-Ganzzahlen haben beliebig viele Stellen und laufen nie über. 
  NumPy-Arrays haben dagegen einen festen `dtype` (z. B. `int8` mit genau 8 Bit), der die 
  Anzahl verfügbarer Bits begrenzt. Das ist wichtig für `invert()` und die 
  Verschiebungsoperationen weiter unten, da sich das Ergebnis innerhalb dieser festen 
  Bit-Breite berechnet.

Die wichtigsten Bitwise-Funktionen in NumPy sind:

- `numpy.bitwise_and()`: Führt eine bitweise UND-Operation durch
- `numpy.bitwise_or()`: Führt eine bitweise ODER-Operation durch  
- `numpy.bitwise_xor()`: Führt eine bitweise XOR-Operation durch
- `numpy.invert()`: Führt eine bitweise Negation durch
- `numpy.left_shift()`: Verschiebt Bits nach links
- `numpy.right_shift()`: Verschiebt Bits nach rechts

Um sich die Bitdarstellung einer Zahl ausgeben zu lassen (z. B. um Ergebnisse der obigen 
Funktionen nachzuvollziehen), bietet NumPy die Funktion `binary_repr`:

```python
numpy.binary_repr(num, width=None)
```

- `num`: die darzustellende Ganzzahl
- `width` (Default `None`): Mindestanzahl der Stellen der Ausgabe, mit führenden Nullen 
  aufgefüllt (z. B. `width=8` erzwingt eine 8-stellige Ausgabe wie `00001101`)

```python
import numpy as np

print(np.binary_repr(13, width=8))  # '00001101'
```

### Bitweise UND, ODER und XOR Operationen: `bitwise_and`, `bitwise_or`, `bitwise_xor`

```python
numpy.bitwise_and(x1, x2)  # bitweises UND: 1 nur dort, wo beide Operanden 1 sind
numpy.bitwise_or(x1, x2)   # bitweises ODER: 1 dort, wo mindestens ein Operand 1 ist
numpy.bitwise_xor(x1, x2)  # bitweises XOR: 1 dort, wo genau ein Operand 1 ist
```

- `x1`, `x2`: Ganzzahl- oder Boolean-Arrays (gleicher Shape oder broadcastbar), auf denen bitweise verknüpft wird

`np.bool_` ist NumPys eigener Boolean-Datentyp für Array-Elemente (analog zu `np.int8` oder 
`np.complex128`); bei booleschen Arrays entsprechen die Bitwise-Operationen den logischen 
Operationen UND/ODER/XOR.

```python
import numpy as np

# Bitweise Operationen mit Arrays
arr1 = np.array([True, False, True], dtype=np.bool_)
arr2 = np.array([False, True, False], dtype=np.bool_)

result_and = np.bitwise_and(arr1, arr2)
result_or = np.bitwise_or(arr1, arr2)
result_xor = np.bitwise_xor(arr1, arr2)

print("AND:", result_and)  # [False False False]
print("OR:", result_or)    # [True  True  True]
print("XOR:", result_xor)  # [True  True  True]
```

[ER] Implementieren Sie bitweise Operationen mit verschiedenen Datentypen:

- Erstellen Sie zwei Arrays mit ganzen Zahlen: `a = np.array([13, 17])` und `b = np.array([5, 8])`
- Führen Sie `np.bitwise_and(a, b)`, `np.bitwise_or(a, b)` und `np.bitwise_xor(a, b)` durch
- Geben Sie sowohl die Ergebnisse als auch die binären Darstellungen aus (verwenden Sie `np.binary_repr()`)
- Erklären Sie in Kommentaren, wie die Ergebnisse zustande kommen
<!-- ER1 -->
<!-- time estimate: 15 min -->

### Bit-Verschiebungen: `left_shift` und `right_shift`

Bit-Verschiebungsoperationen verschieben die Bits einer Zahl um eine feste Anzahl 
Positionen:

```python
numpy.left_shift(x1, x2)   # verschiebt die Bits von x1 um x2 Positionen nach links
numpy.right_shift(x1, x2)  # verschiebt die Bits von x1 um x2 Positionen nach rechts
```

- `x1`: Ganzzahl-Array, dessen Bits verschoben werden
- `x2`: Anzahl der Positionen, um die verschoben wird

```python
import numpy as np

# Links-Verschiebung entspricht Multiplikation mit 2^n
left_result = np.left_shift(10, 2)  # 10 << 2 = 40
print("10 << 2 =", left_result)

# Rechts-Verschiebung entspricht ganzzahliger Division durch 2^n  
right_result = np.right_shift(40, 2)  # 40 >> 2 = 10
print("40 >> 2 =", right_result)
```

[EQ] Warum entspricht eine Links-Verschiebung um `n` Positionen einer 
Multiplikation mit `2^n`? Berechnen Sie mental das Ergebnis von `np.left_shift(7, 3)` 
und erklären Sie Ihren Rechenweg mit der binären Darstellung.
<!-- EQ1 -->

[ER] Arbeiten Sie mit Bit-Verschiebungen in Arrays:

- Erstellen Sie ein Array `values = np.array([5, 12, 25, 48])`
- Verschieben Sie alle Werte um 1 Position nach links
- Verschieben Sie alle Werte um 2 Positionen nach rechts
- Vergleichen Sie die Ergebnisse mit mathematischen Operationen (`*2` bzw. `//4`)
- Dokumentieren Sie Ihre Beobachtungen
<!-- ER2 -->
<!-- time estimate: 20 min -->

### Bitweise Negation mit `invert`

Die `invert()`-Funktion kehrt jedes einzelne Bit einer Zahl um (aus 0 wird 1 und 
umgekehrt):

```python
numpy.invert(x)
```

- `x`: Ganzzahl- oder Boolean-Array, dessen Bits umgekehrt werden

Bei vorzeichenbehafteten Ganzzahltypen wie `int8` wird das Ergebnis als 
Zweierkomplement interpretiert: Das höchstwertige Bit zeigt das Vorzeichen an 
(1 = negativ), und eine negative Zahl `-n` wird als Bitmuster von `n - 1` mit 
umgekehrten Bits dargestellt. Deshalb ergibt das Umkehren aller Bits einer Zahl `n` 
immer `-(n + 1)`:

```python
import numpy as np

# Bitweise Negation
arr = np.array([1, 2], dtype=np.int8)
inverted = np.invert(arr)
print("Original:", arr)
print("Inverted:", inverted)  # [-2, -3]
```

Um ein Array in einen anderen `dtype` umzuwandeln, bietet NumPy die Methode `astype`:

```python
ndarray.astype(dtype)
```

- `dtype`: Ziel-Datentyp, in den die Elemente des Arrays umgewandelt werden (z. B. `np.uint8` 
  oder `str`); es wird immer ein neues Array zurückgegeben, das ursprüngliche bleibt unverändert

[HINT::Bit für Bit vorgehen] Schreiben Sie sich zuerst die 8-Bit-Darstellung 
von `1` auf (`np.binary_repr(1, width=8)`), kehren Sie jedes Bit einzeln um, und 
prüfen Sie erst danach, welche negative Zahl dieses Bitmuster im Zweierkomplement 
bzw. als vorzeichenlose Zahl repräsentiert.
[ENDHINT]

[ER] Untersuchen Sie den Einfluss des `dtype` auf `invert()`:

- Erstellen Sie `arr = np.array([1, 2], dtype=np.int8)` und wenden Sie `np.invert()` darauf an
- Wandeln Sie `arr` mit `arr.astype(np.uint8)` um und wenden Sie `np.invert()` auch darauf an
- Geben Sie beide Ergebnisse aus
<!-- ER3 -->

[EQ] Warum liefert `np.invert()` bei `int8` negative Werte, bei `uint8` aber nicht, obwohl 
dieselben Bits umgekehrt werden? Nutzen Sie Ihre Ergebnisse aus der vorherigen Aufgabe für 
Ihre Erklärung.
<!-- EQ2 -->
<!-- time estimate: 20 min -->

### NumPy String-Funktionen Grundlagen: `char.upper`, `char.lower`

NumPy bietet umfangreiche Funktionen für String-Verarbeitung durch das `numpy.char`-Modul. 
Diese Funktionen arbeiten vektorisiert auf String-Arrays: Sie wenden eine String-Operation 
auf jedes Element eines Arrays gleichzeitig an. Wie bei einzelnen Python-Strings verändern 
sie das ursprüngliche Array nicht, sondern geben immer ein neues Array mit den Ergebnissen 
zurück.

```python
numpy.char.upper(a)  # wandelt jedes Element in Großbuchstaben um
numpy.char.lower(a)  # wandelt jedes Element in Kleinbuchstaben um
```

- `a`: Array von Strings, dessen Elemente umgewandelt werden

```python
import numpy as np

# String-Arrays erstellen
strings = np.array(['Hello', 'World', 'NumPy'])
print("Original:", strings)

# Grundlegende String-Operationen
upper_strings = np.char.upper(strings)
lower_strings = np.char.lower(strings)
print("Uppercase:", upper_strings)
print("Lowercase:", lower_strings)
```

### String-Verbindungen und Multiplikationen: `char.add`, `char.multiply`

```python
numpy.char.add(x1, x2)     # hängt die Elemente von x1 und x2 paarweise aneinander
numpy.char.multiply(a, i)  # wiederholt jedes Element von a i-mal
```

- `x1`, `x2`: Arrays von Strings gleicher Länge, deren Elemente paarweise aneinandergehängt werden
- `a`: Array von Strings, das wiederholt wird
- `i`: Anzahl der Wiederholungen pro Element

```python
import numpy as np

# String-Verbindung
arr1 = np.array(['Hello', 'Good'])
arr2 = np.array([' World', 'bye'])
combined = np.char.add(arr1, arr2)
print("Combined:", combined)  # ['Hello World' 'Goodbye']

# String-Wiederholung
repeated = np.char.multiply('Python ', 3)
print("Repeated:", repeated)  # 'Python Python Python '
```

[ER] Implementieren Sie verschiedene String-Operationen:

- Erstellen Sie ein Array `names = np.array(['Alice', 'Bob', 'Charlie'])`
- Erstellen Sie ein Array `greetings = np.array(['Hallo', 'Hi', 'Hey'])`
- Verbinden Sie entsprechende Elemente mit `np.char.add()` und fügen Sie ein Leerzeichen dazwischen ein
- Verwenden Sie `np.char.multiply()`, um jeden Namen 2-mal zu wiederholen
- Konvertieren Sie alle Namen in Großbuchstaben mit `np.char.upper()`
<!-- ER4 -->
<!-- time estimate: 15 min -->

### String-Formatierung und -Bearbeitung: `char.center`, `char.strip`, `char.replace`

```python
numpy.char.center(a, width, fillchar=' ')  # zentriert jeden String in einem Feld der Breite width
numpy.char.strip(a)                        # entfernt Leerzeichen am Anfang und Ende
numpy.char.replace(a, old, new)            # ersetzt alle Vorkommen von old durch new
```

- `a`: Array von Strings, das bearbeitet wird
- `width`: Zielbreite, auf die zentriert wird
- `fillchar` (Default `' '`): Füllzeichen links/rechts vom zentrierten String
- `old`, `new`: zu ersetzendes Teilstück bzw. Ersatz-Teilstück (bei `replace`)

```python
import numpy as np

# String-Zentrierung und Polsterung
centered = np.char.center('NumPy', 15, fillchar='*')
print("Centered:", centered)  # '*****NumPy*****'

# String-Bereinigung
messy_strings = np.array(['  hello  ', '  world  '])
cleaned = np.char.strip(messy_strings)
print("Cleaned:", cleaned)  # ['hello' 'world']

# String-Ersetzung
text = np.array(['Python', 'NumPy', 'Pandas'])
replaced = np.char.replace(text, 'y', 'i')
print("Replaced:", replaced)  # ['Pithon' 'NumPi' 'Pandas']
```

[ER] Arbeiten Sie mit String-Formatierung:

- Erstellen Sie ein Array `words = np.array(['Python', 'NumPy', 'Pandas'])`
- Zentrieren Sie jeden String in einem Feld der Breite 10 mit `np.char.center()`
- Erstellen Sie ein Array mit Strings, die Leerzeichen am Anfang und Ende haben
- Verwenden Sie `np.char.strip()` zum Entfernen der Leerzeichen
- Nutzen Sie `np.char.replace()`, um alle 'y' durch 'i' zu ersetzen
<!-- ER5 -->
<!-- time estimate: 15 min -->

### String-Teilung und -Verbindung: `char.split`, `char.join`, `char.find`

```python
numpy.char.split(a, sep=None)  # teilt jeden String an sep in eine Liste von Teilstrings
numpy.char.join(sep, a)        # verbindet die Teilstrings jedes Elements mit dem Trennzeichen sep
numpy.char.find(a, sub)        # gibt die erste Fundposition von sub zurück, oder -1 falls nicht enthalten
```

- `a`: Array von Strings, das verarbeitet wird
- `sep` (Default `None`): Trennzeichen; bei `split` ohne Angabe wird an beliebigem Leerraum
  getrennt, bei `join` verbindet es die Teilstrings
- `sub`: gesuchtes Teilstück (bei `find`); der Rückgabewert ist die erste Fundposition
  oder `-1`, falls `sub` nicht enthalten ist

```python
import numpy as np

# String-Teilung
sentences = np.array(['Hello World', 'NumPy Arrays'])
words = np.char.split(sentences)
print("Split:", words)

# String-Verbindung mit Trennzeichen
word_list = np.array([['a', 'b', 'c'], ['x', 'y', 'z']])
joined = np.char.join('-', word_list)
print("Joined:", joined)  # ['a-b-c' 'x-y-z']

# Zeichen in Strings finden
emails = np.array(['user@domain.com', 'admin@site.org'])
at_positions = np.char.find(emails, '@')
print("Position of '@':", at_positions)  # [ 4  5]
# Gibt -1 zurück, wenn nicht gefunden
not_found = np.char.find(emails, 'xyz')
print("Position of 'xyz':", not_found)  # [-1 -1]
```

[ER] Implementieren Sie erweiterte String-Operationen:

- Erstellen Sie ein Array mit E-Mail-Adressen: `emails = np.array(['user@domain.com', 'admin@site.org'])`
- Verwenden Sie `np.char.split(emails, '@')` zum Aufteilen bei '@'
- Erstellen Sie ein Array von Wörtern und verbinden Sie sie mit `np.char.join()`
- Verwenden Sie `np.char.replace()` zum Ersetzen von Domänen-Endungen
- Testen Sie `np.char.find()` zum Auffinden von Zeichen in Strings
<!-- ER6 -->
<!-- time estimate: 10 min -->

### Weiterführend

- [NumPy Bitwise Operations](https://numpy.org/doc/stable/reference/routines.bitwise.html)
- [NumPy String Functions](https://numpy.org/doc/stable/reference/routines.char.html)

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Knackpunkte

- [EREFR::1]: `bitwise_and`/`bitwise_or`/`bitwise_xor` liefern die korrekten Ergebnisse und die
  über `np.binary_repr()` ausgegebenen Bitmuster stimmen mit den Kommentaren überein
- [EREFQ::2]: die Erklärung, warum `int8` und `uint8` bei `invert()` unterschiedliche Vorzeichen
  liefern, verweist korrekt auf die Interpretation des Bitmusters (Vorzeichenbit vs. kein
  Vorzeichenbit) statt auf einen Unterschied in der eigentlichen Bit-Operation
- [EREFR::6]: `split`/`join`/`replace`/`find` liefern für alle Elemente des Arrays die
  korrekten Ergebnisse

### Fragen und Python-Dateien
[INCLUDE::ALT:np-bitwise-string.md]

[ENDINSTRUCTOR]
