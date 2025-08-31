title: "Go-Grundlagen: Referenztypen vs. Werttypen"
stage: alpha
timevalue: 3.5
difficulty: 2
explains: Slice (Golang)
assumes: go-basics
---

[SECTION::goal::idea,experience]
Ich habe mich mit den weiteren Konzepten von Go auseinandergesetzt und kenne die 
Unterschiede zwischen Referenz- und Werttypen.
[ENDSECTION]

[SECTION::background::default]
TODO
[ENDSECTION]

[SECTION::instructions::detailed]

### Referenz- und Werttypen

Mit _Referenztypen_ sind in der Regel die Typen gemeint, die sich wie ein Zeiger (Pointer)
verhalten.
Das bedeutet unter anderem:

- der Nullwert ist `nil`
- sie enthalten intern Zeiger auf Daten
- sie zeigen "pass-by-reference"-Verhalten

_Werttypen_ sind anders: Sie stellen wirklich die Werte dar, sie sind **die Daten selbst**.
Primitive Datentypen (Zahlen, boolesche Werte und Zeichenketten) sind Werttypen.

Alle Werttypen teilen sich folgende Eigenschaften:

- der Nullwert ist nicht `nil`
- sie zeigen "pass-by-value"-Verhalten: beim Zuweisen oder Übergeben als Parameter wird eine Kopie
  erstellt
- Vergleichbarkeit: zwei Variablen von einem Werttyp dürfen mittels `==` sinnvoll verglichen werden

Nun betrachten wir Arrays, Slices und Maps detaillierter aus der Perspektive von Wert- und
Referenztypen.

[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]
**Kommandoprotokoll**

TODO

**Lösungen**

TODO

Musterlösung der Programmieraufgabe siehe hier: TODO
[ENDINSTRUCTOR]
