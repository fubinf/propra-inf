title: Fehlerbehandlung in Python
description: |
  Wir lernen mit Fehlern umzugehen.
timevalue: 0.5
difficulty: 2
assumes: PythonClasses
---
TODO: Noch sehr auf Python gemünzt. Verallgemeinerung für alle Sprachen nötig.

Häufig sind Fehler bei der Benutzung von Programmen vorprogrammiert (no pun intended). Beispiele
dafür sind z. B. Eingaben in Formaten, die vom Programm nicht bearbeitbar sind oder wenn man
versucht eine Datei zu laden, die gar nicht existiert. 

Belesen Sie sich in der Python-Dokumentation zum Thema [Errors and
Exceptions](https://docs.python.org/3.8/tutorial/errors.html). 
Versuchen Sie für sich folgende Fragen zu beantworten:

- Welche Ausdrücke werden in Python im Zusammenhang der Fehlerbehandlung benutzt?
- Wie sieht die Syntax für einen `try`-Ausdruck aus? Was muss gegeben sein, was ist optional?
- Welche Typen von Exceptions sind in Python vordefiniert? Nennen Sie drei Beispiele. 
- Wie lassen sich eigene Exceptions schreiben?

Schreiben Sie anschließend Programm, in der eine Division durch Null durchgeführt wird. 
Behandeln Sie den Fehler, damit das Programm nicht abstürzt.

!!! submission "Abgabeformat"
    Die Abgabe besteht einem lauffähigen Programm namens `errors`.