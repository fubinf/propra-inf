title: Klassen extrahieren
stage: draft
timevalue: 0.5
difficulty: 2
profiles:
assumes:
requires:
---
[SECTION::goal::idea]

- Ich verstehe, wie ich Klassen aus anderen Klassen extrahieren kann.
- Ich verstehe, wie ich meinen Code verändern muss, damit diese Änderung funktioniert.
- Ich verstehe, wann es nützlich ist diese Refaktorisierung durchzuführen.

[ENDSECTION]
[SECTION::background::default]

Code schreiben kann am Anfang sehr einfach sein.
Etwas Datenstruktur hier, etwas Funktionalität da... und irgendwann hat man ein Produkt, 
mit dem man etwas anfangen kann.
Achtet man aber anfangs nicht so sehr darauf, dass der Entwurf des Programms logisch und gut wartbar ist, 
können einem später Stolpersteine entgegenkommen.
Möchte man das Programm später um Funktionalität erweitern, kann es nun schwierig sein diese einzubauen. 

[ENDSECTION]
[SECTION::instructions::detailed]

Lesen Sie sich den Eintrag [https://refactoring.guru/extract-class](https://refactoring.guru/extract-class)
durch und beschreiben Sie in eigenen Worten

- welches Problem diese Refaktorisierung löst,
- wie die Refaktorisierung durchgeführt werden kann und
- auf welche Fallstricke man bei der Benutzung dieser Refaktorisierung achten soll.

Recherchieren und beschreiben Sie außerdem, wie Ihre IDE Ihnen hilft diese Refaktorisierung durchzuführen.

[ENDSECTION]
[SECTION::submission::information]

Die Abgabe besteht aus einem Markdown-Dokument.

[ENDSECTION]

[INSTRUCTOR::Kurzfassung]
Klassenextraktion hilft Klassen mehr zu spezialisieren, sie sollen nach Möglichkeit nur eine Aufgabe haben.
Das fördert das _Single Responsibility Principle_.
PyCharm hilft über den Refactor-Dialog bei der Durchführung.
[ENDINSTRUCTOR]