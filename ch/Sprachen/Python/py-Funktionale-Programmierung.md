title: "Funktionale Programmierung in Python"
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Python-Iterators, m_pprint
---

[SECTION::goal::idea]

Ich habe ein paar grundlegende Methoden der funktionalen Programmierung in Python kennengelernt 
und kann sie verwenden, um meine Codequalität zu verbessern.

[ENDSECTION]

[SECTION::background::default]

Python ist eine Multi-Paradigmen-Sprache, das heißt neben prozeduralen und objektorientierten 
Programmierparadigmen beherrscht Python auch einige Möglichkeiten, um funktionale Programme zu 
schreiben.
Auch wenn funktionale Programmierung nicht zwingend notwendig ist, um gute Programme zu 
schreiben, kann es von Vorteil sein, die Grundlagen zu kennen, um z.B. an passenden 
Stellen "eleganteren" Code zu schreiben. 
Daher schauen wir uns hier ein paar der Werkzeuge und Built-in Funktionen an, um Python-Code im 
funktionalen Programmierstil zu schreiben.

[NOTICE]
Auch wenn Python diese und weitere Werkzeuge unterstützt, bleibt es vorwiegend eine 
imperative Sprache. Ziel der Aufgabe ist es als nicht, rein funktionale Programme zu schreiben 
(Schleifen und Variablenzuweisungen sind hier also weiter erlaubt).
[ENDNOTICE]

[ENDSECTION]

[SECTION::instructions::detailed]

### Warum funktionale Programmierung?

Diejenigen, die das Modul funktionale Programmierung bereits gehört haben, sollten bereits etwas 
mit dem Begriff anfangen können. 
Wer aber bisher nur mit imperativer Programmierung in Berührung gekommen ist, fragt sich 
womöglich, was funktionale Programmierung überhaupt ist und wozu es gut sein soll.

- [EQ] Lesen Sie die Einleitung vom 
  [Artikel über funktionale Programmierung in Python](https://docs.python.org/3/howto/functional.html). 
  Nennen und beschreiben Sie kurz einige der Vorteile von funktionaler Programmierung, die im 
  Artikel genannt werden.

Überfliegen Sie anschließend auch den Rest des Artikels. 
Die einzelnen Abschnitte enthalten Erklärungen zu den in den folgenden Aufgaben behandelten 
Werkzeugen und können Ihnen bei der Bearbeitung der Aufgaben nützlich sein.

### Lambda-Funktionen

Funktionen sind, wie der Name schon sagt, die Basis funktionaler Programmiersprachen. 
Typischerweise unterteilt man in funktionaler Programmierung ein Problem in kleinere 
Teilprobleme und löst diese unabhängig in eigenen Funktionen, die sich meist wiederum in 
Funktionen unterteilen (Teile-und-Herrsche-Verfahren, divide and conquer). 
Als Ergebnis erhält man eine umfangreiche Sammlung an Funktionen, die man auch in anderen 
Projekten einfach wiederverwenden kann.

Nicht immer will man aber eine Funktion global definieren, z.B. wenn es nicht sinnvoll ist, sie 
außerhalb des Kontexts wiederzuverwenden oder die Definition länger ist, als der Code, den sie 
ausführen soll.
Für den Fall kann man Lambda-Funktionen (auch genannt anonyme Funktionen) definieren. 
Das sind kleine, einzeilige Funktionen, die simple Probleme lösen können.
Dafür sind sie allerdings in ihrer Komplexität eingeschränkt und können keine 
mehrzeiligen Anweisungen beinhalten.

Ob man Lambda-Funktionen verwenden sollte, ist meistens eine Stilfrage: richtig eingesetzt können 
sie den Code übersichtlicher gestalten, aber auch den gegenteiligen Effekt haben, z.B. wenn man 
versucht, zu viel innerhalb einer Zeile unterzubringen.

- [ER] Schreiben Sie eine Lambda-Funktion, die berechnet, ob sich eine Zahl ganzzahlig durch 
  eine andere teilen lässt. Testen Sie die Funktion folgendermaßen:  
```python
divisible = lambda ...: ...
print("is 10 divisible by 2?", divisible(10, 2))
print("is 10 divisible by 3?", divisible(10, 3))
```

Als [TERMREF::first-class citizen] können Funktionen wie Variablen gehandhabt werden, und so auch
als Parameter sowie auch als Rückgabewert von anderen Funktionen fungieren 
([TERMREF::Funktion höherer Ordnung]). 

- [ER] Verwenden Sie die `sort()`-Funktion, um die unten stehende Liste zu sortieren. Die Liste 
  soll allerdings nicht alphabetisch, sondern nach Länge der Wörter sortiert werden. Übergeben Sie 
  daher eine entsprechende Lambda-Funktion an das `key` Argument.  
```python
fruits = ['apple', 'banana', 'blueberry', 'orange', 'peach', 'pear']
print("\nsorted by length:", ...)
```
- [ER] Definieren Sie die Funktion `add_prefix(prefix: str)`, die eine Funktion zurückgibt, 
  die ein Präfix an den übergebenen String anfügt. Testen Sie Ihre Funktion folgendermaßen:  
```python
greeting = add_prefix("\nHallo ")
farewell = add_prefix("Auf Wiedersehen ")
print(greeting("Welt"))
print(farewell("Welt"))
```

### Generatoren

Generatoren sehen zunächst wie ganz normale Funktionen aus. 
Sie enthalten allerdings ein bestimmtes Schlüsselwort: `yield`. 
Das ermöglicht es, die Funktion wie einen Iterator zu verwenden: wird `next()` auf den Generator 
ausgeführt, wird die Funktion bis zum nächsten `yield` Keyword ausgeführt und der damit verbundene 
Wert zurückgegeben. 
So lässt sich ein Iterator schnell und einfach wie eine Funktion definieren.

- [ER] Definieren Sie einen Generator `generate_substrings(input: str, delimiter: str)`. 
  Dieser soll einen String entgegennehmen und in jeder Iteration den nächsten Substring bis zum 
  nächsten Trennzeichen (delimiter) zurückgeben. 
  Rufen Sie anschließend Ihren Generator folgendermaßen auf:  
```python
gen = generate_substrings("Generatoren sind sehr praktisch.", " ")
print("\nfirst three words:", list([next(gen) for _ in range(3)]))
```

### Built-in Functions

Einige der Built-in Funktionen von Python haben einen näheren Bezug zu funktionaler 
Programmierung und lassen sich teils auch in rein funktionalen Sprachen wiederfinden. 
Zu diesen Funktionen gehören:  
`map()`, `filter()`, `zip()`, `sorted()`, `any()`, `all()` und `enumerate()`.

Jede der folgenden Aufgaben soll mithilfe mindestens einer der genannten Funktionen gelöst werden. 
Zusätzlich kann es durchaus hilfreich sein, auch Lambda-Ausdrücke oder Generatoren zu verwenden. 
Sie können auch Lösungen aus den vorherigen Teilaufgaben wiederverwenden.

- [ER] Filtern Sie die gegebene Liste `numbers`, sodass alle Zahlen übrig bleiben, die durch einen 
  gegebenen Wert teilbar sind.  
```python
numbers = list(range(10))
print("\ndivisible by 2", ...)
print("divisible by 7", ...)
```
- [ER] Schreiben Sie eine Funktion `first_word_with_letter(text: str, letter: str)`, die das erste 
  Wort in `text` zurückgibt, das den gegebenen Buchstaben enthält, sowie die Position des Wortes im 
  Text.  
```python
res = first_word_with_letter("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore.", "y")
print("\nthe first word with the letter 'y' is '", res[0], "' at position", res[1]) 
```
- [ER] Sie haben die folgende Liste von Produkten sowie die Preise in Euro. Schreiben Sie eine 
  Funktion `convert_currency(products: list, rate: float)`, die ein Iterable mit allen Produkten 
  und den umgerechneten Preisen zurückgibt.
  Testen Sie anschließend die Funktion folgendermaßen:
```python
some_products = [
    {"product": "Laptop", "price": 999.00},
    {"product": "Smartphone", "price": 599.59},
    {"product": "Tablet", "price": 299.95},
    {"product": "Monitor", "price": 199.99}
]

products_in_dollar = convert_currency(some_products, 1.04)
p = next(products_in_dollar)
print("\nThe", p.get("product"), "costs", p.get("price"), "USD")
```
- [ER] Nehmen Sie die folgenden Rabatte (in Prozent): `[30, 25, 50, 10]` 
  Wenden Sie sie in der gegebenen Reihenfolge auf die Produkte der vorherigen Aufgabe an. 
  Geben Sie anschließend alle Produkte aus, die weniger als 500€ kosten.
```python
print("\ndiscounted products cheaper than 500€:")
pprint.pprint(..., sort_dicts=False)
```

### Funktional vs. imperativ

- [EQ] Schauen Sie sich die letzte Aufgabe an. Überlegen Sie sich, wie Sie das Problem auf 
  "klassischem Wege" imperativ lösen würden (es genügt den Code zu beschreiben, sie brauchen ihn 
  nicht abzugeben). 
  Vergleichen Sie die beiden Lösungen und geben Sie ihre Meinung dazu, welchen Lösungsansatz Sie 
  "besser" finden und warum.

### Weiterführende Aufgaben

Mit den bisher in der Aufgabe gezeigten Werkzeugen lässt sich schon einiges anfangen. Es gibt 
aber noch weitere Module in der Python-Standardbibliothek, die weitere, fortgeschrittene Funktionen 
bieten, um noch effizienter funktionale Programme zu schreiben:

- Das [PARTREFMANUAL::m_itertools::itertools-Modul] bietet weitere Werkzeuge, um effiziente 
  Operationen auf und mit Iteratoren durchzuführen.
- Das [PARTREFMANUAL::m_functools::functools-Modul] bietet weitere Hilfsmittel für die 
  Verwendung von Funktionen höherer Ordnung.

[ENDSECTION]

[SECTION::submission::information,trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Antworten prüfen und Codedurchsicht]

Code lesen und manuell grob auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und Abgaben, die nicht die in der Aufgabe geforderten Werkzeuge verwenden,  
zurückweisen.

Beispiellösung siehe [TREEREF::/Sprachen/Python/Python-Funktionale-Programmierung.py]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
