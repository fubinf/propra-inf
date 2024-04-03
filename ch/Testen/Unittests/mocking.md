title: Mocking in pytest
stage: alpha
timevalue: 2.0
difficulty: 3
assumes: pytest101, pytest102
---
# Review (DM)
 - Hintergrund-Sektion enthält hier (z.T.) die Aufgabenbeschreibung. Das sollte wohl eher Teil der Aufgabeninstruktionen sein.
 - ggf. Quelle(n) als Hilfestellung, wenn mehr als Wikipedia erwartet wird.
 - Ziele ergänzt (siehe commit diff)

[SECTION::goal::idea]

- Ich kann beschreiben, was "Mocks" sind und wie sie in pytest Anwendung finden.
- Ich kann "Mocks" von anderen Testmethoden abgrenzen.
- Ich kann begründen, wann die Anwendung von "Mocks" sinnvoll ist.

[ENDSECTION]
[SECTION::background::default]

In dieser Aufgabe werden wir uns mit dem Konzept des "Code Mocking" und der Verwendung von pytest
als Testframework auseinandersetzen.
Mocking ermöglicht es, reale Abhängigkeiten und externe Ressourcen in Tests zu simulieren, um Tests
zu isolieren und zuverlässigere Ergebnisse zu erzielen.  
Recherchieren Sie hierzu anhand der folgenden Leitfragen.

[ENDSECTION]
[SECTION::instructions::loose]

- [EQ] Was versteht man genau unter dem Begriff "Code Mocking"?
- [EQ] Welches Problem versucht Code Mocking zu lösen?
- [EQ] Welchen Unterschied gibt es zwischen Mocking und Fixtures?
   Ergänzen sie sich gegenseitig?
- [EQ] Wie werden Mock-Objekte zur Nutzung in pytest erstellt?
- [EQ] In welchen Situationen sollten wir Mocks verwenden, und wann sollten wir auf echte
   Implementierungen zugreifen?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
