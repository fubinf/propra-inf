title: "Funktionale Programmierung in Python"
stage: beta
timevalue: 1.5
difficulty: 3
assumes: py-Iterators, m_pprint
---

[SECTION::goal::idea]
Ich habe ein paar grundlegende Methoden der funktionalen Programmierung in Python kennengelernt 
und kann sie verwenden, um meine Codequalität zu verbessern.
[ENDSECTION]


[SECTION::background::default]
Python ist eine Multi-Paradigmen-Sprache, das heißt neben prozeduralen und objektorientierten 
Programmierparadigmen bietet Python auch Möglichkeiten, um funktionale Programme zu 
schreiben.
Mit [TERMREF2::Funktionale Programmierung::funktionaler Programmierung] ist es einfacher, korrekten 
Code zu schreiben und auch einfacher, diesen Code zu testen.
Daher schauen wir uns hier ein paar der Werkzeuge und Built-in Funktionen an, um Python-Code im 
funktionalen Programmierstil zu schreiben.

[NOTICE]
Auch wenn Python diese und weitere Werkzeuge unterstützt, bleibt es vorwiegend eine 
imperative Sprache. Ziel der Aufgabe ist es nicht, _rein_ funktionale Programme zu schreiben, 
sondern Schleifen und Variablenzuweisungen bleiben weiter erlaubt und sinnvoll.
Die funktionale Programmierung wird z.B. auf Ebene von Unterprogramm-Schnittstellen
angewandt, aber nicht unbedingt _innerhalb_ eines Unterprogramms. 
[ENDNOTICE]
[ENDSECTION]


[SECTION::instructions::detailed]

### Warum funktionale Programmierung?

Wer bisher nur mit imperativer Programmierung in Berührung gekommen ist (prozedural und/oder
objektorientiert), fragt sich vielleicht, 
was funktionale Programmierung überhaupt ist und wozu sie gut sein soll.

[EQ] Lesen Sie die Einleitung von diesem 
[Artikel über funktionale Programmierung in Python](https://docs.python.org/3/howto/functional.html). 
Nennen und beschreiben Sie kurz die zwei aus Ihrer Sicht wichtigsten Vorteile von funktionaler 
Programmierung, die im Artikel genannt werden.

Überfliegen Sie anschließend auch den Rest des Artikels. 
Die einzelnen Abschnitte enthalten Erklärungen zu den hier behandelten und geforderten 
Werkzeugen und helfen Ihnen bei der Bearbeitung der Aufgaben.


### Vorbereitung

Legen Sie die Datei `py-Funktionale-Programmierung.py` an und fügen Sie dort Ihre Lösungen für 
die folgenden Programmieraufgaben ein.


### Lambda-Funktionen

Funktionen sind, wie der Name schon sagt, die Basis funktionaler Programmiersprachen. 
Typischerweise unterteilt man in funktionaler Programmierung ein Problem in kleinere 
Teilprobleme und löst diese unabhängig in eigenen Funktionen, die sich meist wiederum in 
Funktionen unterteilen (Teile-und-Herrsche-Verfahren, divide and conquer). 
Als Ergebnis erhält man eine umfangreiche Sammlung an Funktionen, die man immer mal auch in anderen 
Projekten wiederverwenden kann.

Nicht immer will man aber eine Funktion global definieren, z.B. wenn es nicht sinnvoll ist, sie 
außerhalb des Kontexts wiederzuverwenden oder die Definition länger ist, als der Code, den sie 
ausführen soll.
Für den Fall kann man Lambda-Funktionen (auch genannt anonyme Funktionen) definieren. 
Das sind kleine Funktionen, die nur aus einem einzigen Ausdruck bestehen dürfen, also keine 
Anweisungen wie z.B. Zuweisung, `if`-Anweisung oder Schleifen benutzen können.

Ob man Lambda-Funktionen verwenden sollte, ist eine Stilfrage: richtig eingesetzt können 
sie den Code übersichtlicher gestalten, aber auch den gegenteiligen Effekt haben, z.B. wenn man 
versucht, zu viel darin unterzubringen.

Als [TERMREF::first-class citizen] können Funktionen wie Variablen gehandhabt werden, und so als 
Parameter, sowie auch als Rückgabewert von anderen Funktionen fungieren 
([TERMREF::Funktion höherer Ordnung]).

[ER] Verwenden Sie die `sorted()`-Funktion, um die unten stehende Liste zu sortieren. 
Die Liste soll zwar alphabetisch sortiert werden, allerdings so, als wäre das Wort rückwärts 
geschrieben. 
Die Elemente der Liste selbst sollen dabei allerdings nicht verändert werden, sondern lediglich 
ein anderer "Schlüssel" für die Sortierung verwendet werden. 
Übergeben Sie daher eine entsprechende Lambda-Funktion an das `key` Argument von `sorted()`, die 
diesen Schlüssel aus dem Wort generiert.  
```python
fruits = ['apple', 'banana', 'blueberry', 'orange', 'peach', 'pear']
print("sorted by last letters:", ...)
```

[HINT::sortierte Liste zur Kontrolle]
`['banana', 'orange', 'apple', 'peach', 'pear', 'blueberry']`
[ENDHINT]

[ER] Schreiben Sie eine Funktion `choose_operator(word)`. 
Diese soll anhand des gegebenen Wortes entscheiden, um welche Art von mathematischem Operator es 
sich handelt und entsprechend eine Lambda-Funktion zurückgeben, die diese Operation durchführt. 
Es genügt, wenn die Funktion die vier Grundrechenarten unterscheiden kann und sie sollte 
mindestens die englische Schreibweise erkennen (1 **plus** 2, 4 **divided by** 2 etc.). 
Wird kein Operator erkannt, soll die zurückgegebene Funktion immer `None` zurückgeben. 
Testen Sie die Funktion folgendermaßen:  
```python
print("\n8 times 3 =", choose_operator("times")(8, 3))
print("10 minus 4 =", choose_operator("minus")(10, 4))
print("15 divided by 3 =", choose_operator("divided by")(15, 3))
print("9 plus 7 =", choose_operator("plus")(9, 7))
```

[NOTICE]
Im wirklichen Leben würde man anstatt solcher einfachen Lambda-Funktionen sinnvollerweise
lieber die Standardfunktionen aus dem Modul `operator` der Standardbibliothek nehmen,
denn die Standardbibliothek bietet ausgereifte Implementierungen, die auch seltene Fälle
korrekt mit abdecken.  
Für die Grundrechenarten macht das vielleicht keinen Unterschied, aber in anderen Fällen
früher als man denkt.
[ENDNOTICE]


### Generatoren

Generatoren sehen zunächst wie ganz normale Funktionen aus. 
Sie enthalten allerdings ein bestimmtes Schlüsselwort: `yield`. 
Das ermöglicht es, die Funktion wie einen Iterator zu verwenden: wird `next()` auf den Generator 
ausgeführt, wird die Funktion bis zum nächsten `yield` Keyword ausgeführt und der damit verbundene 
Wert zurückgegeben. 
Die Funktion wird anschließend nicht beendet, sondern bleibt weiter im Speicher, sodass sie beim 
nächsten Aufruf von `next()` an der gleichen Stelle fortfährt, bis erneut `yield` aufgerufen wird 
oder sie terminiert. 
So lässt sich ein Iterator schnell und einfach wie eine Funktion definieren.

Bei Bedarf lesen Sie nochmal den 
[Abschnitt zu Generatoren](https://docs.python.org/3/howto/functional.html#generators) im 
How-To-Artikel.

[ER] Definieren Sie einen Generator `generate_substrings(text: str, delimiter: str)`. 
Dieser soll einen String entgegennehmen und in jeder Iteration den nächsten Substring bis zum 
nächsten Trennzeichen (delimiter) zurückgeben. 
Rufen Sie anschließend Ihren Generator folgendermaßen auf:  
```python
gen = generate_substrings("Generatoren sind sehr praktisch.", " ")
print("\nfirst three words:", list([next(gen) for _ in range(3)]))
```

[NOTICE]
Um Strings bei einem Delimiter aufzuspalten, verwendet man i.d.R. die 
[`split()`](https://docs.python.org/3/library/stdtypes.html#str.split) Funktion vom String-Datentyp.
Diese arbeitet jedoch nicht mit Iteratoren und würde daher das Konzept eines Generators, 
jedes Element einzeln auf Abruf zu generieren, umgehen.
__Verzichten__ Sie hier daher auf die Verwendung der Funktion.
[ENDNOTICE]

[HINT::Was benötige ich dafür?]
Schreiben Sie einen einfachen Algorithmus, der in dem String nach dem Delimiter sucht und die 
einzelnen gefundenen Strings "wirft".
Wenn Sie bereits Erfahrung mit regulären Ausdrücken in Python haben, können Sie auch 
[PARTREFMANUAL::m_re::re.finditer()] verwenden.
[ENDHINT]

Eine weitere praktische Alternative zur Erstellung eigener Iteratoren sind **Generator 
Expressions**. 
Diese funktionieren genauso wie [PARTREFMANUAL::py-List-Comprehensions::List Comprehensions], 
aber mit dem Unterschied, dass sie keine Liste, sondern einen Generator erzeugen. 
Syntaktisch unterscheiden sie sich nur durch ihre Klammern (`()` statt `[]`).
Wenn man das Ergebnis nur der Reihe nach mit einer Schleife weiterverarbeitet und
die Zahl der Elemente groß ist, spart das viel Speicherplatz ein und 
obwohl sich alles wie die Arbeit mit Listen anfühlt, kann man sogar
Datenmengen verarbeiten, die gar nicht in den Speicher passen würden.


### `map()`, `filter()` und ihre Kolleginnen

Einige der [Built-in Funktionen](https://docs.python.org/3/howto/functional.html#built-in-functions) 
von Python haben einen engen Bezug zu funktionaler Programmierung.
Viele finden sich ähnlich auch in rein funktionalen Sprachen wieder. 
Zu diesen Funktionen gehören:  
`map()`, `filter()`, `zip()`, `sorted()`, `any()`, `all()` und `enumerate()`.

Die folgenden Aufgaben lassen sich mithilfe mindestens einer der genannten Funktionen lösen. 
Geben Sie das Ergebnis, sofern sinnvoll, als Iterator zurück. 
Zusätzlich kann es durchaus hilfreich sein, auch Lambda-Ausdrücke oder Generatoren zu verwenden, 
sowie Ihre Lösungen aus den vorherigen Teilaufgaben wiederzuverwenden.

[HINT::Wie gebe ich das Ergebnis eines Iterators in der Kommandozeile aus?]
Iteratoren geben bei Ausgabe mit `print()` nur einen String von z.B. der Form
`<map object at 0x7f1029289420>` 
zurück.
Das liegt daran, dass der Iterator selbst keine Werte enthält.
Um die Ergebnisse auszugeben, muss der Iterator zuerst ausgewertet und die Werte in eine 
andere Datenstruktur geschrieben werden, z.B. mit `list()`.
[ENDHINT]

[ER] Filtern Sie die gegebene Liste `numbers`, sodass alle Zahlen übrig bleiben, die durch einen 
gegebenen Wert teilbar sind.  
```python
numbers = list(range(10))
print("\ndivisible by 2", ...)
print("divisible by 7", ...)
```

[HINT::Was benötige ich dafür?]
Filtern von Iterables funktioniert mithilfe von 
[`filter()`](https://docs.python.org/3/library/functions.html#filter).
Als Filter-Kriterium lässt sich eine Funktion übergeben, die ein Objekt entgegennimmt und einen 
Boolean zurückgibt. 
[ENDHINT]


[ER] Sie wollen aus einem Text alle Wörter erhalten, die ein gegebenes Kriterium erfüllen, sowie 
deren Position im Text. 
Schreiben Sie dafür die Funktion `positions_of_matching_words(text, condition)`.
Zurückgegeben werden soll eine Liste mit Tupeln, bestehend aus Wort und Position.
Übergeben Sie an die Funktion den u.s. Text, sowie eine Funktion, die prüft, ob ein Wort den 
Buchstaben `y` enthält.    
```python
t = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore."
res = positions_of_matching_words(t, ...)
print("\nposition of all words with letter 'y':", ...)
```

[HINT::Was benötige ich dafür?]
Um, wie in funktionalen Sprachen üblich, ohne Schleifen auszukommen, aber trotzdem alle Elemente 
wie mit einer Zählvariable zu nummerieren, ist 
[`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) geeignet.
Außerdem könnte Ihnen die Lösung von einer der vorherigen Aufgaben behilflich sein.
[ENDHINT]


[ER] Aus einem Datensatz haben Sie eine Reihe von Produkten sowie deren Preise in Euro jeweils als 
Liste importiert. 
Als Ergebnis möchten Sie die einzelnen Produkte als Dictionary darstellen, jeweils mit den 
Schlüsseln `product` und `price`. 
Fassen Sie Produkte und Preise jeweils zu Tupeln zusammen. 
Verwenden Sie dann das Zwischenergebnis, um aus den Tupeln jeweils Dictionaries zu erstellen.  
```python
prod = ["Laptop", "Smartphone", "Tablet", "Monitor"]
some_products = ...
prices = [999.00, 599.59, 299.95, 199.99]
print("\nproducts with prices")
pprint.pp(some_products)
```

[HINT::So soll das Ergebnis aussehen]
```python
[{'product': 'Laptop', 'price': 999.0},
 {'product': 'Smartphone', 'price': 599.59},
 {'product': 'Tablet', 'price': 299.95},
 {'product': 'Monitor', 'price': 199.99}]
```
[ENDHINT]

[HINT::Was benötige ich dafür?]
Mithilfe von [`zip()`](https://docs.python.org/3/library/functions.html#zip) lassen sich zwei 
oder mehr Iterables paarweise in Tupel verpacken (also `[1,2,3], [a,b,c] --> [(1,a),(2,b),(3,c)]`).
Anschließend können sie jedes dieser Tupel in ein Dictionary verwandeln.
Da Sie die Produkte noch mehrmals benötigen, speichern Sie sie in einer Liste.
[ENDHINT]

[ER] Sie wollen nun eine Funktion `convert_currency(products, rate)` schreiben, 
die anhand eines Wechselkurses die Preise der Produkte in eine andere Währung umrechnet. 
Zurück soll ein Iterator gegeben werden, der die Produkte mit den umgerechneten Preisen zurückgibt. 
Testen Sie anschließend Ihre Funktion folgendermaßen:  
```python
products_in_usd = convert_currency(some_products, 1.13)
p = next(products_in_usd)
print("\nThe", p["product"], "costs", p["price"], "USD")
```

[HINT::Was benötige ich dafür?]
Mit [`map()`](https://docs.python.org/3/library/functions.html#map) lässt sich eine gegebene 
Funktion auf alle Elemente eines Iterables anwenden.
Die gegebene (Lambda-)Funktion kann so definiert werden, dass sie das Produkt mit umgerechneten 
Preis zurückgibt.
[ENDHINT]

[ER] Sie haben nun eine weitere Liste `stock = (4, 0, 1, 7)`, die angibt, wie viele Produkte 
Sie jeweils noch auf Lager haben. 
Schreiben Sie eine Funktion `add_attributes(products, key, values)`, die zu einem Produkt ein neues 
Attribut hinzufügt, also Schlüssel und Wert ins Dictionary einfügt.  
Fügen Sie anschließend `stock` mithilfe der Funktion in ihre Produkte aus vorheriger Aufgabe ein. 
Prüfen Sie schließlich Ihre neue Produktliste, ob manche Produkte nicht mehr auf Lager sind und 
geben Sie das erste solche Produkt aus.  
```python
print("product not in stock:", ...)
```

[HINT::Was benötige ich dafür?]
Hier sind mehrere Schritte notwendig:

Zuerst ordnet man jedes Produkt mit seinem neuen Attribut __paarweise zusammen__.

Dann muss auf jedes Produkt __eine Funktion angewandt__ werden, die das neue Schlüssel-Wert-Paar 
hinzufügt.
Normalerweise verwendet man `dict[key] = value` um Elemente in ein Dictionary hinzuzufügen. 
Lambda Funktionen unterstützen allerdings keine Zuweisungen, daher können Sie stattdessen:

- statt einer Lambda-Funktion eine separate Funktion definieren oder
- den `**`-Operator verwenden, um ein Dictionary zu "entpacken" (`**dict`) und anschließend das 
  Key-Value-Paar hinzufügen.

Anschließend kann das Ergebnis wieder entsprechend __gefiltert__ werden.
[ENDHINT]


### Programmlauf für die Abgabe

[EC] Führen Sie das gesamte so erzeugte Programm `py-Funktionale-Programmierung.py` einmal aus.


### Funktional vs. imperativ

Schauen Sie sich die letzte Aufgabe noch einmal an. 
Schreiben Sie zum Vergleich die Funktion noch einmal ohne die Verwendung von Built-in Funktionen 
und Iteratoren (diese Fassung müssen Sie nicht mit abgeben, können es aber).

[EQ] Vergleichen Sie die beiden Lösungen. 
Welche Variante empfinden Sie als besser lesbar?  
Stellen Sie sich vor (oder probieren Sie es aus), sie übergeben an die beiden Funktion mehrere 
Millionen Produkte. Denken Sie, dass die Funktionen sich unterschiedlich verhalten und wenn ja, 
inwiefern?  
Wie schätzen Sie die beiden Funktionen hinsichtlich ihrer Laufzeit und Speichernutzung ein und 
wie lässt sich ggf. dadurch der Unterschied erklären?

[HINT::Worin unterscheiden sich die beiden Ansätze?]
Schauen Sie sich in 
<!-- LINK_CHECK: status=403 -->
[folgendem Artikel](https://labex.io/tutorials/python-how-to-implement-lazy-evaluation-in-a-python-iterator-397687) 
die Bedeutung von [TERMREF::Lazy Evaluation] noch einmal an, und wie dies mit Iteratoren 
zusammenhängt.
[ENDHINT]


### Weiterführende Aufgaben

Mit den bisher in der Aufgabe gezeigten Werkzeugen lässt sich schon einiges anfangen. Es gibt 
aber noch weitere Module in der Python-Standardbibliothek, die weitere, fortgeschrittene Funktionen 
bieten, um noch effizienter funktionale Programme zu schreiben:

- Das [PARTREFMANUAL::m_itertools::itertools-Modul] bietet weitere Werkzeuge, um effiziente 
  Operationen auf und mit Iteratoren durchzuführen.
- Das [PARTREFMANUAL::m_functools::functools-Modul] bietet weitere Hilfsmittel für die 
  Verwendung von Funktionen höherer Ordnung.
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

Beispiellösung siehe [TREEREF::/Sprachen/Python/py-Funktionale-Programmierung.py]

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
