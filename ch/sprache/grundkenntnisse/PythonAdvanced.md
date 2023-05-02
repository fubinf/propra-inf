title: Python Advanced -- Lambdas, Iteratoren, Error Handling
description: |
  Ein kleiner Einblick in einige fortgeschrittene 
timevalue: 1
difficulty: 1
assumes: PythonBasics101, PythonBasics102, PythonBasics103, PythonOOP
---
!!! goal
    In dieser Einheit geht es darum einen kurzen Einblick in weitere Funktionen zu bekommen, die 
    Python von Haus aus mitbringt. 
    Auch wenn diese Funktionen nicht zwingend im Zusammenhang zueinander stehen, bietet diese 
    Auswahl einen Einstieg.
    

Recherchieren Sie die Konzepte Lambda (anonyme Funktionen), Iteratoren und Exceptions in Python.

Folgende Seiten eignen sich gut als zusätzliche Quellen:

 * [Python Documentation - Lambda Expressions](https://docs.python.org/3.8/tutorial/controlflow.
html#lambda-expressions) 
 * [Python Documentation - Iterators](https://docs.python.org/3.8/tutorial/classes.html#iterators)
 * [Python Documentation - Errors and Exceptions](https://docs.python.org/3.8/tutorial/errors.html)


!!! submission
    Erläutern Sie, was passiert, wenn sie in Python eine Lambda-Funktion mit einer Variable
    definieren und anschließend die Variable verwenden. Beispiel:

    ```python
       i = 3
       f = lambda: print(i)
       i = 4
       f()
    ```

    Machen Sie Vorschläge, wie Sie ein anderes Verhalten erzeugen könnten. Es ist okay, wenn
    keine Ihrer Ideen funktioniert, nennen Sie sie dennoch.

    Erläutern Sie kurz, wie Iteratoren funktionieren. Welchen Vorteil hat die Verwendung von
    Iteratoren gegenüber Listen?

    Was ist die Basis-Klasse für alle Exceptions in Python? Wie erzeugen Sie eine Exception,
    wenn Ihnen im Programmablauf eine unerwartete Situation begegnet?

    In den PythonBasics102 haben Sie eine Besonderheit von Pythons Kontrollstrukturen
    kennengelernt, sie auch hier vorhanden ist. Welche ist das und wie wird sie verwendet?

!!! instructor
    Da eine korrekte Lösung für das Problem der Variablen mit Lambdas nicht explizit erfordert
    ist, muss auch keine korrekte Lösung in der Abgabe vorliegen. Ideen sollten aber da sein.

    Eine ganz banale Lösung, die hier (und in vielen anderen Sprachen) funktioniert, ist, den
    Wert von i vorher in eine andere Variable zuzuweisen. Das funktioniert selbstverständlich
    nicht mit veränderbaren Datenstrukturen, aber darum geht es hier auch gar nicht
