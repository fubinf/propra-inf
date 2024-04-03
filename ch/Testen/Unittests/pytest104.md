title: Pytest - Parametrisierte Tests
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: pytest101, pytest103
---
# Review (DM)
- Hintergrund-Sektion enthält hier (z.T.) die Aufgabenbeschreibung. Das sollte wohl eher Teil der Aufgabeninstruktionen sein.
- Frage 2 und 4 sind inhaltlich sehr nah beeinander. Entweder konkretisieren (Vor/Nachteile bei der Verwendung in pytest/generell) oder zusammenfassen.

[SECTION::goal::idea]

- Ich kann Tests unter Anwendung von parametrisierten Tests besser gestalten.

[ENDSECTION]
[SECTION::background::default]

Es gibt Tests, die mit vielen Eingabeparametern versorgt werden müssen, um alle Randfälle
abzudecken.
Der naive Weg hierzu wäre, alle Kombinationen in einzelnen Tests festzuhalten.

Ein besonderes Mark in pytest ist `@pytest.mark.parametrize`.
So können Sie Tests mit vielen Eingabeparametern versorgen, ohne diese nicht mehrfach schreiben zu
müssen.  
Setzen Sie sich mithilfe der pytest-Dokumentation und bei Bedarf weiteren Quellen mit den
folgenden Fragen auseinander:

[ENDSECTION]
[SECTION::instructions::loose]

- [EQ] Was sind parametrisierte Tests und warum sind sie bei Softwaretests wichtig?
- [EQ] Wie unterscheiden sich parametrisierte Tests von herkömmlichen (nicht-parametrisierten) Tests
   in pytest?
- [EQ] Wie werden parametrisierte Tests in pytest implementiert? Geben Sie Beispiele für die Syntax
   und die Verwendung von parametrisierten Tests.
- [EQ] Welche Vorteile bieten parametrisierte Tests im Vergleich zu nicht-parametrisierten Tests?
   Gibt es auch Nachteile?
- [EQ] Welche Arten von Parametern können in pytest für die Tests verwendet werden?
- [EQ] Welche speziellen pytest-Funktionen und -Dekoratoren sind für parametrisierte Tests verfügbar?
   Wie können Sie sie effektiv nutzen?
- [EQ] Wie können Sie mithilfe von parametrisierten Tests in pytest Grenzfälle und seltene Szenarien
   effektiv testen?  

[How to parametrize fixtures and test functions](https://docs.pytest.
org/en/stable/how-to/parametrize.html)

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
