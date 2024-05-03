title: Eigenheiten von JavaScript
stage: draft
timevalue: 1
difficulty: 2
assumes: JS-Syntax
---
[SECTION::goal::idea]

Ich kenne häufige mögliche Fallstricke, über die ich beim Entwickeln mit JavaScript stolpern könnte.

[ENDSECTION]
[SECTION::background::default]

In der Aufgabe [PARTREF::JS-Syntax] ging es darum, welche Dinge sich JavaScript mit vielen anderen
Sprachen teilt. Hier geht es darum, auf Unterschiede einzugehen, denn genau diese können einem auf
die Füße Fallen, wenn man mit Vorwissen aus anderen Sprachen ankommt.

[ENDSECTION]
[SECTION::instructions::detailed]

[EQ] Welche Datentypen für Zahlen gibt es in JavaScript?

[EQ] Wie geht JavaScript mit optionalen Argumenten für Funktionen um? Das heißt, was muss ich tun,
um eine Funktion mit weniger als der vollen Menge an Argumenten aufzurufen?

[EQ] Was passiert, wenn man eine Funktion mit zu vielen Argumenten aufruft?

[NOTICE]
Als Folge der vorherigen beiden Fragen müssen Sie oft vorsichtig sein, wenn es um die Verwendung
von Methodenreferenzen geht! Grundsätzlich ist `list.map(doSomething)` eine valide Syntax, aber es
kann sein, dass es etwas anderes tut als `list.map(element -> doSomething(element))`.
[ENDNOTICE]

[EQ] JavaScript bietet zwei verschiedene Möglichkeiten, anonyme Funktionen zu definieren.
Es gibt `function(arg) { code }` und `arg => { code }`. Worin unterscheiden sich diese?

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
