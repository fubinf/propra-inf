title: NumPy Bitwise-Operationen und String-Funktionen
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: np-Einführung, np-array, np-index-slice, np-array2, np-array3
---

[SECTION::goal::idea,experience]

- Ich verstehe die grundlegenden Bitwise-Operationen in NumPy und kann sie anwenden.
- Ich kann NumPy String-Funktionen für die Textverarbeitung verwenden.
- Ich beherrsche die Verwendung von `numpy.bitwise_and`, `numpy.bitwise_or`, `numpy.bitwise_xor` und verwandten Funktionen.
- Ich kann `numpy.char` Funktionen für String-Manipulationen effektiv einsetzen.

[ENDSECTION]

[SECTION::background::default]

Bitwise-Operationen und String-Funktionen sind essenzielle Werkzeuge in NumPy für 
fortgeschrittene Datenverarbeitung. Bitwise-Operationen arbeiten auf Binärebene und 
sind wichtig für Optimierungen und spezielle Berechnungen. String-Funktionen 
ermöglichen effiziente Textverarbeitung in NumPy-Arrays und sind unerlässlich für 
die Analyse von Textdaten in wissenschaftlichen Anwendungen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Grundlagen der NumPy Bitwise-Operationen

Bitwise-Operationen arbeiten direkt auf der binären Darstellung von Zahlen. 
NumPy bietet eine Reihe von Funktionen für solche Bit-Level-Operationen, 
die sowohl mit einzelnen Werten als auch mit Arrays arbeiten können.

Die wichtigsten Bitwise-Funktionen in NumPy sind:

- `numpy.bitwise_and()`: Führt eine bitweise UND-Operation durch
- `numpy.bitwise_or()`: Führt eine bitweise ODER-Operation durch  
- `numpy.bitwise_xor()`: Führt eine bitweise XOR-Operation durch
- `numpy.invert()`: Führt eine bitweise Negation durch
- `numpy.left_shift()`: Verschiebt Bits nach links
- `numpy.right_shift()`: Verschiebt Bits nach rechts

Optional: Für eine umfassende Übersicht siehe:
[NumPy Bitwise Operations](https://numpy.org/doc/stable/reference/routines.bitwise.html)

### Bitweise UND, ODER und XOR Operationen: `bitwise_and`, `bitwise_or`, `bitwise_xor`

```python
import numpy as np

# Bitweise Operationen mit Arrays
arr1 = np.array([True, False, True], dtype=bool)
arr2 = np.array([False, True, False], dtype=bool)

result_and = np.bitwise_and(arr1, arr2)
result_or = np.bitwise_or(arr1, arr2)
result_xor = np.bitwise_xor(arr1, arr2)

print("AND:", result_and)  # [False False False]
print("OR:", result_or)    # [True  True  True]
print("XOR:", result_xor)  # [True  True  True]
```

[EQ] Erklären Sie, warum bei der XOR-Operation von `[True, False, True]` und 
`[False, True, False]` das Ergebnis `[True, True, True]` ist. Was bedeutet XOR 
und wie funktioniert es auf Bit-Ebene?
<!-- EQ1 -->

[ER] Implementieren Sie bitweise Operationen mit verschiedenen Datentypen:

- Erstellen Sie zwei Arrays mit ganzen Zahlen: `a = np.array([13, 17])` und `b = np.array([5, 8])`
- Führen Sie `np.bitwise_and(a, b)`, `np.bitwise_or(a, b)` und `np.bitwise_xor(a, b)` durch
- Geben Sie sowohl die Ergebnisse als auch die binären Darstellungen aus (verwenden Sie `np.binary_repr()`)
- Erklären Sie in Kommentaren, wie die Ergebnisse zustande kommen
<!-- ER1 -->
<!-- time estimate: 15 min -->

### Bit-Verschiebungen: `left_shift` und `left_shift`

Bit-Verschiebungsoperationen sind fundamental für verschiedene mathematische Operationen 
und Optimierungen:

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
<!-- EQ2 -->

[ER] Arbeiten Sie mit Bit-Verschiebungen in Arrays:

- Erstellen Sie ein Array `values = np.array([5, 12, 25, 48])`
- Verschieben Sie alle Werte um 1 Position nach links
- Verschieben Sie alle Werte um 2 Positionen nach rechts
- Vergleichen Sie die Ergebnisse mit mathematischen Operationen (`*2` bzw. `//4`)
- Dokumentieren Sie Ihre Beobachtungen
<!-- ER2 -->
<!-- time estimate: 15 min -->

### Bitweise Negation mit `invert`

Die `invert()` Funktion kehrt alle Bits um. Bei vorzeichenbehafteten Zahlen 
verwendet sie das Zweierkomplement:

```python
import numpy as np

# Bitweise Negation
arr = np.array([1, 2], dtype=np.int8)
inverted = np.invert(arr)
print("Original:", arr)
print("Inverted:", inverted)  # [-2, -3]
```

[EQ] Erklären Sie, warum `np.invert(1)` bei `dtype=int8` das Ergebnis `-2` liefert. 
Beschreiben Sie die Schritte der Zweierkomplement-Berechnung ausführlich.
<!-- EQ3 -->
<!-- time estimate: 10 min -->

Optional: Zur Vertiefung des Zweierkomplements siehe:
[Two's Complement](https://en.wikipedia.org/wiki/Two%27s_complement)

### NumPy String-Funktionen Grundlagen: `char.upper`, `char.lower`

NumPy bietet umfangreiche Funktionen für String-Verarbeitung durch das `numpy.char` Modul. 
Diese Funktionen arbeiten vektorisiert auf String-Arrays:

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

Optional: Vollständige Referenz der numpy.char Funktionen:
[NumPy String Functions](https://numpy.org/doc/stable/reference/routines.char.html)

### String-Verbindungen und Multiplikationen: `char.add`, `char.multiply`

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
<!-- ER3 -->
<!-- time estimate: 15 min -->

### String-Formatierung und -Bearbeitung: `char.center`, `char.strip`, `char.replace`

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
<!-- ER4 -->
<!-- time estimate: 10 min -->

### String-Teilung und -Verbindung: `char.split`, `char.join`, `char.find`

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
<!-- ER5 -->
<!-- time estimate: 10 min -->

### Kombinierte Anwendung: Bitwise-Operationen und Strings

[ER] Erstellen Sie eine komplexe Anwendung, die beide Konzepte kombiniert:

- Erstellen Sie ein Array von Zahlen: `numbers = np.array([15, 31, 63, 127])`
- Konvertieren Sie diese in binäre String-Darstellungen mit einer eigenen Funktion
- Verwenden Sie Bitwise-Operationen um zu prüfen, ob Zahlen ungerade sind (Hinweis: `& 1`)
- Erstellen Sie String-Labels für gerade/ungerade Zahlen mit `np.char` Funktionen
- Kombinieren Sie Zahlen und Labels in einem formatierten Ausgabe-Array
<!-- ER6 -->
<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-bitwise-string.md]

[ENDINSTRUCTOR]
