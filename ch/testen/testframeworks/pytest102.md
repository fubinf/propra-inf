title: pytest - Fixtures
description: |
  Lernen Sie hier, was Fixtures sind und wie sie helfen Tests zu entwerfen. 
timevalue: 1.5
difficulty: 3
assumes: pytest101
---
!!! goal 
    Oftmals benötigten Sie zum Testen bestimmte Voraussetzungen, die erfüllt sein müssen.
    Ohne eine Datenbank können Sie keine Tests über Datenbankabfragen gestalten, ohne Webserver 
    wird es schwer, Abfragen über WebAPIs zu testen.
    Setzen Sie sich hier mit Fixtures auseinander, die diese Hürde angehen.

Fixtures sind Teile von Software, die vor einem Test initialisiert werden und damit 
Voraussetzungen erfüllen, die ein System hat.
Setzen Sie sich mithilfe der pytest-Dokumentation und bei Bedarf weiteren Quellen mit den 
folgenden Fragen auseinander:

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


!!! submission
    Die Abgabe besteht aus einem Markdown-Dokument mit den Antworten zu den oben gestellten Fragen.
    Halten Sie die Antworten kurz.
    Sie dürfen Code-Beispiele benutzen, wenn diese zur Antwort hilfreich sind.
    Geben Sie Quellen an, wenn Sie andere als die gegebenen Quellen hinzuziehen.
    
