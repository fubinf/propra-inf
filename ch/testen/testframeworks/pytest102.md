title: Pytest - Fixtures
description: |
  Lernen Sie hier, was Fixtures sind und wie sie helfen Tests zu entwerfen.
timevalue: 1.5
difficulty: 3
profiles: TEST
assumes: pytest101
requires:
---
[SECTION::goal::idea]

Oftmals benötigten ich zum Testen bestimmte Voraussetzungen, die erfüllt sein müssen.
Ohne eine Datenbank kann ich keine Tests über Datenbankabfragen gestalten, ohne Webserver
wird es schwer, Abfragen über WebAPIs zu testen.
In dieser Einheit lernen ich, wie ich mit Fixtures diese Hürde angehen kann.

[ENDSECTION]
[SECTION::background::default]

Fixtures sind Teile von Software, die vor einem Test initialisiert werden und damit
Voraussetzungen erfüllen, die ein System hat.
Setzen Sie sich mithilfe der pytest-Dokumentation und bei Bedarf weiteren Quellen mit den
folgenden Fragen auseinander:

[ENDSECTION]
[SECTION::instructions::loose]

1. Wie erstellt man einfache Fixtures in pytest?
2. Wie können Sie Fixtures verwenden, um wiederkehrende Testdaten oder -umgebungen zu verwalten?
3. Was ist der Unterschied zwischen "function scope", "class scope" und "module scope" bei
   Fixtures und wann sollten Sie sie jeweils verwenden?
4. Wie können Sie Fixture-Abhängigkeiten in pytest definieren?
5. Wie können Sie in pytest mit Fixture-Finalizern aufräumen oder Ressourcen freigeben?
6. Wie können Fixtures automatisch für alle Tests im Scope bereitgestellt werden?

[pytest - About fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.
html#about-fixtures)
[pytest - How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

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
