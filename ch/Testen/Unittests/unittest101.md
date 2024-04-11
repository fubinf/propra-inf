title: Unittest in Python - Grundlagen
stage: draft
timevalue: 1.5
difficulty: 2
---

TODO_1_ruhe: Bitte in eine aktive Aufgabe verwandeln:
- Kleines zu testendes Progrämmchen im Aufgabentext vorgeben
- Und dann immer abwechselnd ein Häppchen was lesen
- und dann den praktischen Schritt dazu machen
- bis man am Ende alle untigen Aufgaben als [ER] (und am Ende einmal [EC] erledigt hat).
- [EQ] bleibt allenfalls für Test Discovery und Testorganisation übrig.
- setUp() und erst recht tearDown() müssen von mir aus nicht zwingend vorkommen,
  erst recht nicht im praktischen Teil.

[SECTION::goal::idea]

- Ich kann Unittests in Python beschreiben.
- Ich kann mit den Grundlagen vom Python-Testframework `unittest` umgehen.

[ENDSECTION]

[SECTION::background::default]

Auch erfahrene Programmierer machen Fehler, daher ist es entscheidend, eine zuverlässige Lösung für
die Verifikation des Codes zu haben. Unittests bieten eine automatisierte Möglichkeit, um die
Funktionalität des Codes zu überprüfen und potenzielle Fehler aufzudecken, bevor sie zu größeren
Problemen führen.

[ENDSECTION]

[SECTION::instructions::detailed]

`unittest` ist das von Python mitgelieferte Testframework.
Nutzen Sie die [`unittest`-Dokumentation](https://docs.python.org/3.10/library/unittest.html)
sowie bei Bedarf weitere Quellen,
um sich anhand der folgenden Fragen in das Framework einzuarbeiten.

- [EQ] Wie werden Testfälle in `unittest` erstellt?
- [EQ] Wie sollen die Testskripte, Testklassen und Testfunktionen benannt werden?
- [EQ] Was ist "test discovery" und wie funktioniert diese in `unittest`?
- [EQ] Wie werden die Tests mit `unittest` durchgeführt?
- [EQ] Wie können die Tests organisiert werden?
- [EQ] Was sind die Methoden `setUp()` und `tearDown()` und wie wendet man sie an?
- [EQ] Welche Assertions stehen zur Verfügung und wie können diese am besten genutzt werden?
- [EQ] Welche Informationen stellt der Output eines Tests zur Verfügung?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
