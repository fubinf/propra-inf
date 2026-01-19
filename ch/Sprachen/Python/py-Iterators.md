title: "Iteratoren in Python"
stage: alpha
timevalue: 2
difficulty: 3
---

[SECTION::goal::idea]
Ich verstehe das Iterator-Protokoll in Python und kann eigene Iterator-Klassen implementieren,
um Daten effizient zu verarbeiten.
[ENDSECTION]

[SECTION::instructions::loose]

### Grundlagen verstehen

Anhand [dieses Artikels](https://realpython.com/python-iterators-iterables/)
werden wir Iteratoren in Python praktisch kennenlernen.

Lesen Sie die Abschnitte:

- ["Understanding Iteration in Python"](https://realpython.com/python-iterators-iterables/#understanding-iteration-in-python)
- ["Getting to Know Python Iterators"](https://realpython.com/python-iterators-iterables/#getting-to-know-python-iterators)
- ["Creating Different Types of Iterators"](https://realpython.com/python-iterators-iterables/#creating-different-types-of-iterators)
- ["Creating Generator Iterators"](https://realpython.com/python-iterators-iterables/#creating-generator-iterators)
- ["Doing Memory-Efficient Data Processing With Iterators"](https://realpython.com/python-iterators-iterables/#doing-memory-efficient-data-processing-with-iterators)

Beantworten Sie danach diese Kernfragen:

[EQ] Was ist ein Iterator? Welche zwei Methoden muss ein Objekt implementieren,
um ein Iterator zu sein, und was macht jede dieser Methoden?

[EQ] Wann und warum sollte man einen Iterator statt einer einfachen Liste verwenden?
Nennen Sie mindestens zwei konkrete Situationen.

[EQ] Was passiert, wenn `__next__()` keine weiteren Elemente mehr hat?
Wie signalisiert ein Iterator das Ende der Iteration?

### Aufgabe 1: Einfacher Iterator mit Filterung

[ER] Erweitern Sie die untenstehende Iterator-Klasse `NumIterator`,
die eine Liste von Zahlen akzeptiert und 
optional nach geraden oder ungeraden Zahlen filtern kann.

```python
class NumIterator:
    def __init__(self, sequence, filter_cond='all'):
        if isinstance(sequence, list) and all(isinstance(item, int) for item in sequence) and len(sequence) > 0:
            self.sequence = sequence
        else:
            raise ValueError("Input sequence has to be a list of integers")
        self.index = 0
        if isinstance(filter_cond, str) and filter_cond in ['odd', 'even', 'all']:
            self.filter_cond = filter_cond
        else:
            raise ValueError("Filter condition must be 'even', 'odd', or 'all'")
    
    def __iter__(self):
        # TODO: Implementieren
        pass
    
    def __next__(self):
        # TODO: Implementieren
        # Tipp: Überspringen Sie Zahlen, die nicht zur Filterbedingung passen
        pass

# Testbeispiel:
a = list(range(1, 11))

print('Alle Zahlen:')
for item in NumIterator(a):
    print(item)

print('\nGerade Zahlen:')
for item in NumIterator(a, 'even'):
    print(item)

print('\nUngerade Zahlen:')
for item in NumIterator(a, 'odd'):
    print(item)
```

### Aufgabe 2: Datei-Iterator

[ER] Implementieren Sie einen Iterator `FileLineIterator`, 
der eine Textdatei Zeile für Zeile durchläuft,
aber nur Zeilen zurückgibt, 
die nicht leer sind und nicht mit `#` beginnen (Kommentare).

Ihre Implementierung soll:

- Die Datei beim Erstellen des Iterators öffnen
- Jede Zeile beim Iterieren automatisch von Whitespace bereinigen (`.strip()`)
- Leere Zeilen und Kommentarzeilen überspringen
- Die Datei korrekt schließen, wenn die Iteration beendet ist

```python
class FileLineIterator:
    def __init__(self, filename):
        # TODO: Implementieren
        pass
    
    def __iter__(self):
        # TODO: Implementieren
        pass
    
    def __next__(self):
        # TODO: Implementieren
        # Tipp: Nutzen Sie eine while-Schleife, um übersprungene Zeilen zu handhaben
        pass

# Testbeispiel:
# Erstellen Sie eine Datei 'test.txt' mit folgendem Inhalt:
# # Dies ist ein Kommentar
# Zeile 1
# 
# Zeile 2
# # Noch ein Kommentar
# Zeile 3

# for line in FileLineIterator('test.txt'):
#     print(line)
```

### Aufgabe 3: Batch-Iterator

[ER] Implementieren Sie einen Iterator `BatchIterator`, 
der eine Liste in Chunks (Stapel) einer bestimmten Größe aufteilt.
Dies ist nützlich für die Verarbeitung großer Datenmengen in kleineren Portionen.

Beispiel: `[1, 2, 3, 4, 5, 6, 7]` mit `batch_size=3` sollte `[1, 2, 3]`, 
dann `[4, 5, 6]`, dann `[7]` liefern.

```python
class BatchIterator:
    def __init__(self, data, batch_size):
        # TODO: Implementieren
        pass
    
    def __iter__(self):
        # TODO: Implementieren
        pass
    
    def __next__(self):
        # TODO: Implementieren
        pass

# Testbeispiel:
data = list(range(1, 21))
for batch in BatchIterator(data, batch_size=5):
    print(batch)
```

### Aufgabe 4: Generator-Funktionen

Generatoren sind eine elegante Möglichkeit, Iteratoren zu erstellen, ohne eine vollständige Klasse 
mit `__iter__()` und `__next__()` zu implementieren. Sie verwenden das `yield`-Schlüsselwort.

[EQ] Was ist der Unterschied zwischen `return` und `yield` in einer Funktion?
Was passiert, wenn eine Funktion `yield` verwendet?

[ER] Schreiben Sie eine Generator-Funktion `countdown(n)`, die von n bis 1 herunterzählt.
Verwenden Sie `yield`, um jeden Wert zurückzugeben.
Testen Sie den Generator, indem Sie ihn in einer `for`-Schleife durchlaufen.

```python
def countdown(n):
    # TODO: Implementieren
    pass

# Test
print('Countdown:')
for num in countdown(5):
    print(num)
```

[ER] Implementieren Sie einen Generator `filter_long_lines(filename, min_length)`, 
der nur Zeilen aus einer Datei zurückgibt, die mindestens eine bestimmte Länge haben.
Der Generator soll:
- Die Datei Zeile für Zeile durchgehen (nicht alles auf einmal einlesen!)
- Jede Zeile von Whitespace bereinigen
- Nur Zeilen yielden, die mindestens `min_length` Zeichen lang sind
- Die Datei automatisch schließen, wenn alle Zeilen verarbeitet wurden

Dies ist speichereffizient, da nie die gesamte Datei im Speicher gehalten werden muss.

```python
def filter_long_lines(filename, min_length):
    # TODO: Implementieren
    pass

# Test: Nur Zeilen mit mindestens 10 Zeichen
print('\nLange Zeilen (mind. 10 Zeichen):')
for line in filter_long_lines('test.txt', 10):
    print(f"  ({len(line)} Zeichen): {line}")
```

### Aufgabe 5: Speichereffiziente Datenverarbeitung

Diese Aufgabe demonstriert die praktischen Vorteile von Iteratoren bei großen Datenmengen.

[EQ] Was gibt `print()` aus, wenn Sie einen Iterator direkt ausgeben (z.B. `print(NumIterator([1,2,3]))`)?
Warum ist das so? Wie können Sie stattdessen die Werte des Iterators anzeigen?

[ER] Verwenden Sie Ihren `NumIterator` von Aufgabe 1 und rufen Sie `next()` mehrfach manuell auf.
Erstellen Sie einen Iterator für die Zahlen 1 bis 10 (nur gerade Zahlen).
Holen Sie die ersten drei Werte einzeln mit `next()` und geben Sie sie aus.
Konvertieren Sie dann die verbleibenden Werte mit `list()` in eine Liste und geben Sie diese aus.

```python
# TODO: Implementieren
even_iter = NumIterator(list(range(1, 11)), 'even')
print('\nManuelle next() Aufrufe:')
# Erste Zahl mit next()
# Zweite Zahl mit next()
# Dritte Zahl mit next()
# Rest als Liste mit list()
```

[ER] Implementieren Sie einen Iterator `SquaresIterator`, der Quadratzahlen von 1 bis n generiert.
Im Gegensatz zu einer Liste, die alle Werte sofort berechnet und speichert,
soll Ihr Iterator die Quadratzahlen erst bei Bedarf berechnen (on-demand).

Vergleichen Sie dann den Speicherverbrauch:

1. Liste: Alle Quadratzahlen von 1 bis 1.000.000 in einer Liste
2. Iterator: Ihr `SquaresIterator` für Quadratzahlen von 1 bis 1.000.000

Verwenden Sie `sys.getsizeof()`, um den Speicherverbrauch zu messen.

```python
import sys

class SquaresIterator:
    def __init__(self, n):
        # TODO: Implementieren
        pass
    
    def __iter__(self):
        # TODO: Implementieren
        pass
    
    def __next__(self):
        # TODO: Implementieren
        pass

n = 1_000_000

# Liste: alle Werte sofort im Speicher
squares_list = [x**2 for x in range(1, n+1)]

# Iterator: Werte werden erst bei Abruf berechnet
squares_iter = SquaresIterator(n)

print(f'\nSpeicherverbrauch Liste: {sys.getsizeof(squares_list):,} bytes')
print(f'Speicherverbrauch Iterator: {sys.getsizeof(squares_iter):,} bytes')

# Erste 5 Werte des Iterators ausgeben
print('\nErste 5 Quadratzahlen aus dem Iterator:')
for i in range(5):
    print(next(squares_iter))
```

[EQ] Analysieren Sie die Speicherverbrauch-Ergebnisse. 
Warum verbraucht der Iterator so viel weniger Speicher als die Liste?
Was passiert mit den berechneten Werten bei einem Iterator, nachdem sie mit `next()` abgerufen wurden?
In welchen Situationen würden Sie einen Iterator einer Liste vorziehen?

[ENDSECTION]

[SECTION::submission::information,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Musterlösungen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
