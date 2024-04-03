title: Pytest - Fixtures
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: pytest101
---
# Review (DM)
- Hintergrund-Sektion enthält hier (z.T.) die Aufgabenbeschreibung. Das sollte wohl eher Teil der Aufgabeninstruktionen sein.


[SECTION::goal::idea]

- Ich kann Fixtures einordnen und anwenden

[ENDSECTION]
[SECTION::background::default]

Oftmals benötigten ich zum Testen bestimmte Voraussetzungen, die erfüllt sein müssen.
Ohne eine Datenbank kann ich keine Tests über Datenbankabfragen gestalten, ohne Webserver
wird es schwer, Abfragen über WebAPIs zu testen.

Fixtures sind Teile von Software, die vor einem Test initialisiert werden und damit
Voraussetzungen erfüllen, die ein System hat.
Setzen Sie sich mithilfe der pytest-Dokumentation und bei Bedarf weiteren Quellen mit den
folgenden Fragen auseinander:

[ENDSECTION]
[SECTION::instructions::loose]

- [EQ] Wie erstellt man einfache Fixtures in pytest?
- [EQ] Wie können Sie Fixtures verwenden, um wiederkehrende Testdaten oder -umgebungen zu verwalten?
- [EQ] Was ist der Unterschied zwischen "function scope", "class scope" und "module scope" bei
   Fixtures und wann sollten Sie sie jeweils verwenden?
- [EQ] Wie können Sie Fixture-Abhängigkeiten in pytest definieren?
- [EQ] Wie können Sie in pytest mit Fixture-Finalizern aufräumen oder Ressourcen freigeben?
- [EQ] Wie können Fixtures automatisch für alle Tests im Scope bereitgestellt werden?

[pytest - About fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.
html#about-fixtures)
[pytest - How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
