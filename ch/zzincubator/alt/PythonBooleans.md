title: Flow Control - Booleans
timevalue: 0.25
difficulty: 1
---
TODO: Aktuell noch auf Python gemünzt. Verallgemeinerung  notwendig.

Programme sind meist komplexer als einfache Skripte, die Zeile für Zeile ausführen. In der Regel
müssen vorher für die Ausführung bestimmter Schritte Voraussetzungen erfüllt sein. Die Grundlage
hierfür bieten die Booleans, also die Wahrheitswerte _wahr_ und _falsch_ bzw. `True` und `False`.

!!! notice 
    Sehen Sie diese Aufgaben nicht nur als reine Textaufgaben an. Nutzen Sie die Zeit und spiele mit
    dem Gelernten etwas in der [TA2::PythonREPL::REPL] herum! Manchmal lassen sich Fragen auch
    einfacher klären, wenn man sie einfach direkt ausprobiert.

Recherchieren Sie in der
[Dokumentation](https://docs.python.org/3.8/library/stdtypes.html#truth-value-testing) zu den
folgenden Fragen:

  - Wie werden die Wahrheitswerte `True` und `False` in der Sprache ausgedrückt?
  - Werden auch andere Ausdrücke als `True` oder `False` angenommen?
  - Mit welchen Operationen können Booleans ausgewertet werden?

!!! instructor
    Hier geht es um die unären und binären Operatoren zwischen tatsächlichen Wahrheitswerten.

Ein Programm, dass nur mit `True` und `False` arbeitet wäre allerdings ziemlich schwierig zu bauen.
In der Realität werden eher Werte oder Objekte verglichen. Vergleichsoperatoren prüfen den
Zusammenhang zwischen zwei gegebenen Werten und geben einen Boolean zurück.

Recherchieren Sie weiter in der
[Dokumentation](https://docs.python.org/3.8/library/stdtypes.html#truth-value-testing) zu den
folgenden Fragen:

  - Welche Vergleiche sind standardmäßig vorhanden?
  - Lassen sich verschiedene Datentypen vergleichen?
  - Erlaubt die Sprache, dass man das Verhalten von Vergleichen selbst definiert?


TODO: Bessere Aufgabe überlegen, viel zu einfach.

!!! submission "Abgabeformat"
    Beschreiben Sie in wenigen Sätzen, wie Booleans in Python benutzt werden. Beschreiben Sie auch,
    welche Operationen zwischen Booleans möglich sind und welche Vergleiche standardmäßig in Python
    definiert sind.

    Schreiben Sie dann einen in Python syntaktisch richtigen Boolschen Ausdruck mit den
    folgenden Eigenschaften auf: Der Ausdruck muss vier verschiedene Variablen (a, b, c, d) 
    benutzen und es müssen sowohl boolsche Operatoren, als auch Vergleiche vertreten sein. 
    Beschreiben Sie zuletzt diesen Ausdruck in natürlicher Sprache!

!!! instructor
    Die gültigen Operatoren und Vergleiche sind direkt in der Dokumentation zu finden.