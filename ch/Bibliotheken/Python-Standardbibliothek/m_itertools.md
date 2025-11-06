title: "itertools: Komplexe Iterationen effizient schreiben"
stage: draft
timevalue: 1.5
difficulty: 3
assumes: py-Iterators, py-Funktionale-Programmierung
---

[SECTION::goal::idea]
Ich verstehe die Idee hinter `iterator` Objekten und dem `itertools`-Modul und kann diese 
benutzen, um komplexere Iteratoren effizient zu implementieren.
[ENDSECTION]


[SECTION::background::default]
Pythons `Iterator`-Objekte haben viele Vorteile.
Sie können eine bessere Alternative zu langen, verschachtelten Schleifen sein und sind durch 
[TERMREF::Lazy Evaluation] vor allem bei großen Datenmengen speichereffizienter.

Beim Arbeiten mit großen Datenmengen führt man häufig ähnliche oder leicht abgewandelte 
Operationen aus: Füge alle Elemente hintereinander an, wiederhole sie unendlich oft, bilde neue 
Kombinationen u.s.w.
Um solche häufig vorkommenden Operationen nicht immer neu zu implementieren, sollte man 
stattdessen auf bereits bestehende Bibliotheken zurückgreifen.

`itertools` stellt eine Sammlung solcher Operationen bereit, die direkt mit Iteratoren arbeiten 
und, die sich im Stil der [TERMREF2::Funktionale Programmierung::funktionalen Programmierung] 
verketten lassen, um so noch komplexere Iteratoren zu generieren.
So bildet das Modul eine Art eigene Algebra für Iteratoren.

<!--
Große Datenmengen iterativ durchzugehen gehört zum Alltag eines Programmierers.
Python bietet hierfür das `iterator`-Konzept, dass von vielen Datentypen implementiert wird (z.B.
`list`, `str`), aber auch bei eigenen Objekten angewendet werden kann.
Das ermöglicht gut lesbare, sowie effiziente Iterationen über große Datenmengen.

Für gewöhnlich verwendet man Schleifen für solche Iterationen, wobei man häufig ähnliche 
Operationen ausführt (z.B. alle Werte einer Liste aufsummieren, oder alle Permutationen bilden).
Python mit `itertools` eine Sammlung von häufig verwendeten Operationen, die direkt auf 
Iteratoren angewendet werden können und wiederum neue erzeugen.
Das Modul ist somit ein nützliches Werkzeug, da sich hiermit komplizierte iterative Anweisungen in 
meist kürzere, besser lesbare und sogar performantere Anweisungen umwandeln lassen.
-->
[ENDSECTION]


[SECTION::instructions::detailed]


### Vorbereitung

Machen Sie sich mit der 
[Dokumentation von `itertools`](https://docs.python.org/3/library/itertools.html) vertraut und 
verschaffen Sie sich einen groben Überblick über die verschiedenen Funktionen, die dieses Modul 
zur Verfügung stellt.
Vor allem die Tabellen aller Funktionen mit Beispielen, sowie die 
[Recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes) könnten für Sie 
interessant sein.

Legen Sie die Datei `m_itertools.py` an und fügen Sie dort Ihre Lösungen für die folgenden 
Programmieraufgaben ein.

### Rückblick `iterator`

Iteratoren sind ein essenzielles Werkzeug in der 
[PARTREFMANUAL::py-Funktionale-Programmierung::Funktionalen Programmierung in Python] und 
Grundlage für die Verwendung von `itertools`.
Daher zuerst ein kleiner Rückblick:

[EQ] Nennen Sie nochmal kurz die Funktionsweise von Iteratoren und was sie von einer 
for-Schleife über alle Elemente unterscheidet.
Was macht sie potenziell effizienter?

Die Funktionen von `itertools` lassen sich grob in drei Kategorien aufteilen.
Wir schauen uns hier von jeder Kategorie exemplarisch ein paar der Funktionen an.
Jede der folgenden Aufgaben sollte mit mindestens einer Funktion aus `itertools` gelöst werden.


### Kombinatorische Iteratoren

Diese Kategorie umfasst Iteratoren, die nach bestimmten Vorgaben aus bestehenden Mengen neue 
Kombinationen bilden.
Die Konzepte könnten Ihnen bereits aus der Kombinatorik und Wahrscheinlichkeitsrechnung 
bekannt vorkommen.

[ER] In einer Urne befinden sich jeweils eine rote, gelbe, blaue und grüne Kugel.
Stellen Sie die Kugeln als Liste dar.
Geben Sie anschließend alle möglichen Kombinationen aus, zwei Kugeln aus der Urne zu ziehen.  
`print("draw 3 balls:", ...)`

[ER] Geben Sie nun alle Möglichkeiten aus, wenn nach dem Ziehen die Kugeln wieder zurückgelegt 
werden.  
`print("draw 3 with putting back", ...)`

[ER] Sie wollen für eine API automatisch Testfälle generieren, die alle möglichen Eingaben 
ausprobiert.
Die Schnittstelle akzeptiert folgende Eingabeparameter:
```python
statuses = ['active', 'inactive']
regions = ['us-east', 'eu-west', 'eu-east']
user_roles = ['admin', 'user', 'guest']
features = {
    'feature_a': [True, False],
    'feature_b': [True, False]
}
```
Erzeugen Sie alle möglichen Kombinationen an Parametern in der Form `('active', 'us-east', 
'admin', (True, True))`.
Geben Sie zur Überprüfung die Anzahl an erzeugten Testfällen aus:  
`print("number of test cases:", len(list(test_cases)))`

[HINT::Welche Funktion benötige ich?]
Hier muss das kartesische Produkt aller Eingaben erzeugt werden.
Eventuell muss dieses auch mehrmals angewendet werden.
[ENDHINT]


### Terminierende Iteratoren

Die Funktionen unter dieser Kategorie sind am umfangreichsten und unterscheiden sich stark in 
ihrer Funktionsweise.
Sie haben aber alle gemeinsam, dass sie über alle Eingabedaten iterieren und anschließend 
terminieren.

[ER] Sie haben einen Kontostand, sowie eine Liste an Einzahlungen und Abbuchungen.
Berechnen Sie den Kontostand nach jeder Transaktion.  
```python
balance = 500
transactions = [100, -45, -300, 555, -38]
print("balance after every transactions:", ...)
```

[HINT::Welche Funktion benötige ich?]
`accumulate()`
[ENDHINT]

[ER] Schreiben Sie eine Funktion `flatten()`, die einen Iterable nimmt und, falls er verschachtelte 
Iterables enthält, deren Elemente "entpackt" und als einen Iterator zurückgibt, ohne die 
Reihenfolge der Elemente zu verändern.
Als Beispiel: `[a,b,[c],[d,e]] --> [a,b,c,d,e]`  
`print("flattened list:", list(flatten([['a','b'],['c'],['d','e']])))`

[HINT::Welche Funktion benötige ich?]
In den Recipies auf der Doku-Seite finden Sie einen Hinweis.
[ENDHINT]

[ER] Gegeben sind die Punktestände zweier Spieler nach jedem Spielzug.
Nachdem ein Spieler passt, kann der andere noch weiterspielen, bis er ebenfalls passt, wodurch 
beide unterschiedlich viele Spielzüge haben können.
Zippen Sie beide Punktestände zusammen.
Wenn ein Spieler weniger Züge hat, soll sein letzter Punktestand wiederholt werden.  
```python
score_p1 = [0, 2, 5, 7, 8, 10, 15, 16]
score_p2 = [1, 2, 6, 9, 12]
print("scores per match:", ...)
```

[HINT::Welche Funktion benötige ich?]
`zip_longest()`
Bestimmen Sie den Füllwert vor Ausführung der Funktion.
[ENDHINT]

[ER] Neben der Ausgabe der Punktestände wollen Sie aber noch angeben, welcher Spieler gerade mit 
wie viel Punkten vorne liegt.
Erstellen Sie dafür mithilfe von `itertools.tee()` zwei unabhängige Iterables in Ihrer Lösung 
von [EREFR::6].  
Definieren Sie außerdem eine Funktion, die den aktuellen Punktestand entgegennimmt und ein Tupel 
zurückgibt, bestehend aus dem vorne liegenden Spieler (`"p1"`, `"p2"` oder `"draw"`), sowie die 
Anzahl an Punkten, die er vorne liegt.
Wenden Sie diese Funktion auf die einzelnen Punktestände an.  
`print("intermediate results", ...)`

[HINT::Welche Funktion benötige ich?]
`starmap()`
[ENDHINT]

[NOTICE]
Da Iteratoren nur einmal durchiteriert werden können, ist `tee()` eine praktische Methode, um 
mehrere identische, unabhängige Iteratoren zu erstellen.
Allerdings werden für jeden Iterator einzeln die Zustände im Speicher gehalten und neue Elemente 
separat generiert.
Für kurze lookaheads oder kleine Iteratoren ist das vernachlässigbar, aber wenn aufwändigere 
Iteratoren mehrfach komplett durchiteriert werden, ist es i.d.R. besser, die Ergebnisse als 
Liste zu speichern, also Speichereffizienz gegen Ausführungszeit einzutauschen.
[ENDNOTICE]

### Unendliche Iteratoren

Nicht alle Iteratoren müssen endlich sein, sondern können auch wie in einer Endlosschleife immer 
neue Elemente liefern, bis man selbst den Prozess beendet.

[ER] Ein Datensatz soll zyklich an mehrere Worker verteilt werden.
Dafür soll jeder Datensatz mit dem Namen des Workers kombiniert werden (z.B. 
`[(1, 'A'), (2, 'B'), ...]`).
Schreiben Sie die Funktion `assign_to_worker(data, worker)`, die genau dies vornimmt.  
```python
data = range(10)
worker = ['A', 'B', 'C']
print("assigned data:", ...)
```

[ER] Schreiben Sie eine Funktion `my_enumerate()`, die das Verhalten von 
[`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) imitiert.
Sie soll also einen Iterator, sowie einen Startwert entgegennehmen und wieder einen Iterator 
zurückgeben, der die Elemente mit der Zählvariable in einem Tupel zusammenfasst.  
`print("enumerate:", my_enumerate(('a','b','c'), 5))`

[HINT::Welche Funktion benötige ich?]
`count()`
[ENDHINT]


### Vergleich zu nativen Implementierungen

Nach dem kurzen Einblick schauen wir uns noch ein Beispiel an, wie `itertools` eingesetzt werden 
kann.

[EQ] Schauen Sie sich den folgenden Code an.
Was bewirkt er und wie ist er aufgebaut?

```python
def dice_throws_most_common_result(k: int, n: int):
    # generate all possible dice roll results
    results = []
    for i in range(n):
        if results == []:
            results = range(1, k + 1)
        else:
            new_results = []
            for j in range(1, k + 1):
                for r in results:
                    new_results.append(j + r)
            results = new_results

    # count the occurrences and return the most common ones
    results.sort()
    occurrence = []
    last = results[0]
    count = 0
    for r in results:
        if last == r:
            count += 1
        else:
            occurrence.append((last, count))
            count = 1
        last = r
    occurrence.append((last, count))
    occurrence.sort(key=lambda x: x[1], reverse=True)

    return [x for x in occurrence if x[1] == occurrence[0][1]]
```

[ER] Implementieren Sie nun dieselbe Funktion nochmal als 
`dice_throws_most_common_result_it(k: int, n: int)` mithilfe der Verwendung von `itertools`.

[HINT::Welche Funktionen aus itertools benötige ich?]
Alle Wurfergebnisse erzeugen: `product()`  
Ergebnisse nach Häufigkeit gruppieren: `groupby()`
Die größten Ergebnisse ausgeben: `takewhile()`
[ENDHINT]

[ER] Nun wollen wir beide Versionen vergleichen.
Verwenden Sie das folgende Konstrukt, um die Ausführungszeit ihrer Funktion zu testen:
```python
start = time.perf_counter()
# ihre Funktion
duration = time.perf_counter() - start
```
Dafür brauchen wir folgende Funktion aus dem `time` Modul, mit der wir die Ausführungszeit der 
Funktionen testen:  
`time.perf_counter()`


Zum Testen führen Sie für beide Funktionen mit 10000 Elementen aus.
Beobachten Sie zusätzlich in einem System-Monitor (z.B. Task-Manager auf Windows oder htop auch 
Linux) die Arbeitsspeicherauslastung ihres Systems.


### Programmlauf für die Abgabe

[EC] Führen Sie das gesamte so erzeugte Programm `m_itertools.py` einmal aus.


### Fazit

Nachdem Sie nun einen Überblick über das Modul erlangt haben, geben Sie Ihre Einschätzung:

[EQ] In welcher Situation würden Sie die Verwendung von `itertools` vor anderen Methoden, wie 
z.B. Schleifen, bevorzugen?

[EQ] Gibt es eventuell auch Fälle, in denen `itertools` Nachteile mit sich bringt?
[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Quellcode.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]
Den Code grob auf Richtigkeit prüfen.
Das Kommandoprotokoll mit Musterausgabe vergleichen und bei Abweichung gezielt im Code 
nachprüfen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen.

Schleifen im Code können ein Hinweis darauf sein, dass Iteratoren und `itertools` nicht 
ordnungsgemäß verwendet wurden.

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_itertools.py]

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
