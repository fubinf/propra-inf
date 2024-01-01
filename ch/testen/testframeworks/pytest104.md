title: Pytest - Parametrisierte Tests
stage: draft
timevalue: 1.5
difficulty: 3
profiles: TEST
assumes: pytest101, pytest103
requires:
---
[SECTION::goal::idea]

Es gibt Tests, die mit vielen Eingabeparametern versorgt werden müssen, um alle Randfälle
abzudecken.
Der naive Weg hierzu wäre, alle Kombinationen in einzelnen Tests festzuhalten.
Hier setze ich mich mit dieser Aufgabe damit auseinander, wie parametrisierte Tests mir dabei helfen
können, meine Tests besser zu gestalten.

[ENDSECTION]
[SECTION::background::default]

Ein besonderes Mark in pytest ist `@pytest.mark.parametrize`.
So können Sie Tests mit vielen Eingabeparametern versorgen, ohne diese nicht mehrfach schreiben zu
müssen.  
Setzen Sie sich mithilfe der pytest-Dokumentation und bei Bedarf weiteren Quellen mit den
folgenden Fragen auseinander:

[ENDSECTION]
[SECTION::instructions::loose]

1. Was sind parametrisierte Tests und warum sind sie in der Softwaretestung wichtig?
2. Wie unterscheiden sich parametrisierte Tests von herkömmlichen (nicht-parametrisierten) Tests
   in pytest?
3. Wie werden parametrisierte Tests in pytest implementiert? Geben Sie Beispiele für die Syntax
   und die Verwendung von parametrisierten Tests.
4. Welche Vorteile bieten parametrisierte Tests im Vergleich zu nicht-parametrisierten Tests?
   Gibt es auch Nachteile?
5. Welche Arten von Parametern können in pytest für die Tests verwendet werden?
6. Welche speziellen Pytest-Funktionen und -Dekoratoren sind für parametrisierte Tests verfügbar?
   Wie können Sie sie effektiv nutzen?
7. Wie können Sie mithilfe von parametrisierten Tests in pytest Edge Cases und seltene Szenarien
   effektiv testen?  

[How to parametrize fixtures and test functions](https://docs.pytest.
org/en/stable/how-to/parametrize.html)

[WARNING]
[ENDWARNING]

[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::information]

Die Abgabe besteht aus einem Markdown-Dokument mit den Antworten zu den oben gestellten Fragen.
Halten Sie die Antworten kurz.
Sie dürfen Code-Beispiele benutzen, wenn diese zur Antwort hilfreich sind.
Geben Sie Quellen an, wenn Sie andere als die gegebenen Quellen hinzuziehen.

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
