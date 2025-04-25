
title: "`for`-Schleife in Python"
stage: draft
timevalue: 0.1
difficulty: 2
---

[SECTION::goal::idea]

.

[ENDSECTION]

[SECTION::background::default]

.

[ENDSECTION]

[SECTION::instructions::loose]

Bearbeiten Sie erst den Abschnitt "Traversing Built-in Collections in Python".

[ER]

Wir beginnen mit einer einfachen Aufgabe:
Geben Sie mithilfe einer `for`-Schleife alle geraden Zahlen in der 
Liste `numbers` aus.

```python
numbers = [2,5,3,6,1,2,0,33,10]
```

- Arbeiten Sie erstmal index-basiert, das heißt mit der `range()`-Funktion.
- Danach schreiben Sie eine zweite Variante der Lösung aber gehen Sie diesmal 
element-basiert vor.
Greifen Sie also direkt auf die Elemente der Liste auf, 
ohne mit `range()` zu arbeiten. 
- Welche Variante gefällt Ihnen? Eignet sich eine bestimmer Variante 
für alle möglichen Fälle?

[ER] 

Eine spannendere Aufgabe jetzt aus der Realwelt:
Schreiben Sie ein Python-Programm, das die Klasse einer IPv4-Adresse bestimmt – 
also ob sie zu Klasse A, B, C, D oder E gehört.

Hintergrund:
Eine IPv4-Adresse wie `192.168.1.1` besteht aus vier Zahlen, 
getrennt mit einem Punkt. 
Die erste Zahl (z. B. 192) entscheidet, zu welcher Klasse die Adresse gehört.
Früher wurden Adressen in Klassen aufgeteilt, damit man große,
mittlere oder kleine Netzwerke erkennen konnte.
Hier die einfache Einteilung:
A: 0 – 127
B: 128 – 191
C: 192 – 223
D: 224 – 239
E: 240 – 255

Beispiel:
Wenn die IP-Adresse `10.0.0.1` ist, soll das Programm ausgeben:
"Die Adresse `10.0.0.1` ist eine Adresse der Klasse A."

[HINT::Lösungshinweise]

- Machen Sie zur Erleichterung Gebrauch von der `split()`-Funktion.
- Vergessen Sie nicht, dass die Eingabe ein String ist und 
Sie eventuell Typumwandlung durchführen müssen.

[ENDHINT]

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Musterlösung]
.
[ENDINSTRUCTOR]
