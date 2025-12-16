title: "Generatoren"
stage: alpha
timevalue: 1.0
difficulty: 3
assumes: py-Iterators, py-List-Comprehensions, py-Funktionale-Programmierung
---

[SECTION::goal::idea]

Ich kann Generatoren in Python verwenden, um eigene Iteratoren effizient und verständlich zu 
implementieren

[ENDSECTION]

[SECTION::background::default]

Iteratoren sind ein grundlegender Baustein in Python:
Viele Datentypen, wie Listen oder Tupel, aber auch benutzerdefinierte Objekte implementieren die 
Iterator-Schnittstelle und ermöglichen so zum Beispiel ein einfaches Durchlaufen über for-Schleifen.

Wer einen eigenen Iterator definieren will, muss hierfür alle Zustände, sowie die notwendigen 
Funktionen selbst verwalten, was die Erstellung eines simplen Iterators zur 
sequenziellen Datenverabredung verkomplizieren kann.
Eine Alternative können Generatoren sein, die nach außen wie eine Funktion aussehen, sich aber 
wie ein Iterator verhalten.
So lassen sich viele Iteratoren kompakter und lesbarer implementieren.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitung

Lesen Sie den Abschnitt über Generatoren in folgendem 
[How-To-Artikel](https://docs.python.org/3/howto/functional.html#generators).

Legen Sie die Datei `py-Generators.py` an und fügen Sie dort Ihre Lösungen für 
die folgenden Programmieraufgaben ein.


### Iterator selber schreiben

Für die Aufgabe möchten wir einen Sliding Window-Iterator implementieren.
Dieser soll einen Iterable erhalten und dann davon immer ein "Fenster" zurückgeben und 
anschließend eine Position vorrücken.

Beispiel:  
Input: `[1,2,3,4,5]`, Fenstergröße 3  
Output: `[1,2,3], [2,3,4], [3,4,5]`

[ER] Erstellen Sie die Klasse `SlidingWindowIterator`.
Implementieren Sie die Methode `__init__()`, die das Objekt mit den Parametern `data` (Iterable)
und `window_size` (int) initialisiert.
Gegebenenfalls müssen Sie hier auch weitere Attribute für die Klasse definieren.  
Implementieren Sie auch die für Iteratoren notwendigen Methoden `__iter__()` und `__next__()`, 
wobei die erste nur das Objekt selbst zurückgibt und die zweite immer das nächste Fenster erstellt 
und zurückgibt, bis die Input-Daten erschöpft sind.
Falls das Fenster größer ist als die Menge der Input-Daten, soll trotzdem das unvollständige 
Fenster einmal ausgegeben werden.
Sobald die Input-Daten erschöpft sind, soll die Funktion die Exception `StopIteration` werfen.

[ER] Testen Sie nun den Iterator, indem Sie folgendermaßen Instanzen davon erzeugen und ausgeben:  
```python
values1 = [10, 20, 30, 40, 50]
values2 = [60, 70]
print("sliding window iterator:")
for w in SlidingWindowIterator(values1, 3):
    print(w)
for w in SlidingWindowIterator(values2, 3):
    print(w)
```


### Vom Iterator zum Generator

Nun wollen wir dasselbe nochmal machen, allerdings nun unter der Verwendung eines Generators. 

Generatoren sehen zunächst wie normale Funktionen aus. 
Sie enthalten allerdings ein bestimmtes Schlüsselwort: `yield`. 
Das ermöglicht es, die Funktion wie einen Iterator zu verwenden: wird `next()` auf den Generator 
ausgeführt, wird die Funktion bis zum nächsten `yield` Keyword ausgeführt und der damit verbundene 
Wert zurückgegeben. 
Die Funktion wird anschließend nicht beendet, sondern bleibt weiter im Speicher, sodass sie beim 
nächsten Aufruf von `next()` an der gleichen Stelle fortfährt, bis erneut `yield` aufgerufen wird 
oder sie terminiert. 
So lässt sich ein Iterator schnell und einfach wie eine Funktion definieren.

[ER] Definieren Sie den Generator `sliding_window()`, der äquivalent zum Iterator agiert.

[ER] 
```python
print("\nsliding window generator:")
for w in sliding_window(values1, 3):
    print(w)
for w in sliding_window(values2, 3):
    print(w)
```

[EQ] Vergleichen Sie nun beide Lösungen:
Welche empfinden Sie als besser verständlich und leichter zu implementieren?
In welchen Fällen würden Sie die eine Variante der anderen vorziehen?

### Generator Expressions

Eine weitere praktische Alternative zur Erstellung eigener Iteratoren sind **Generator 
Expressions**. 
Diese funktionieren genauso wie [PARTREFMANUAL::py-List-Comprehensions::List Comprehensions], 
aber mit dem Unterschied, dass sie keine Liste, sondern einen Generator erzeugen. 
Syntaktisch unterscheiden sie sich nur durch ihre Klammern (`()` statt `[]`).
So lassen sich die Vorteile von Iteratoren auch für solche kurzen Ausdrücke 

[ER] Schreiben Sie eine Generator Expression, die für jedes Fenster des Sliding Window 
Generators den durchschnittlichen Wert berechnet.
Verwenden Sie als Eingabedaten `values1` und Fenstergröße 3.
```python
print("\naverages with generator expression:")
averages = ...
for a in averages:
    print(a)
```

[EQ] Sind Generator Expressions genauso mächtig wie Generatoren/Iteratoren?
Falls nein, worin liegen ihre Grenzen?


### Programmlauf für die Abgabe

[EC] Führen Sie das gesamte so erzeugte Programm `py_Generators.py` einmal aus.

[ENDSECTION]

[SECTION::submission::reflection,information,snippet,trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Antworten prüfen und Codedurchsicht]
Code lesen und manuell grob auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und Abgaben, die nicht die in der Aufgabe geforderten Werkzeuge verwenden, 
zurückweisen.

Der Generator sollte sichtbar kompakter sein als der Iterator.

Beispiellösung siehe [TREEREF::/Sprachen/Python/py-Generators.py]

[INCLUDE::ALT:]

### Kommandoprotokoll

[PROT::ALT:py-Generators.prot]
[ENDINSTRUCTOR]
