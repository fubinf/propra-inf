title: Extrahieren von Code
stage: alpha
timevalue: 2
difficulty: 2
---

TODO_pietrak:

- timevalue ist ziemlich groß. Die Beantwortung der Fragen inkl. Bearbeitung der 3 Artikel dauert weniger als 2 Stunden. 

- Die Frage "wie wird diese Refaktorierung per Hand durchgeführt" ist gut, damit der Student lernt, wie man schrittweise Refaktorierung durchführt. Das ist alles schon genug detailliert erklärt in jedem der 3 Artikel, aber im Rahmen dieser Frage könnten wir dazu ein refaktorierungsbedürftiges (Python-)Beispiel für jede der Refaktorierungsmethoden zur Verfügung stellen, sodass man anhand dieser Beispiele selbst auch die jeweilige Refaktorierungsmethode durchführt. 

PS: Falls du der Meinung wärest, dass man ohne die oben vorgeschlagene Erweiterung auf refaktorierungsbedürftige Beispiele die Refaktorierungsschritte genug verstehen würde, dann könntest du den stage auf "beta" erhöhen und an Final-Review weiterleiten. 
---

[SECTION::goal::idea]

- Ich verstehe, wie ich Variablen, Methoden und Klassen extrahieren kann.
- Ich verstehe, wie ich meinen Code verändern muss, damit diese Änderung funktioniert.
- Ich verstehe, wann es nützlich ist, diese Refaktorierungen durchzuführen.

[ENDSECTION]
[SECTION::background::default]

Code schreiben kann am Anfang sehr einfach sein.
Etwas Datenstruktur hier, etwas Funktionalität da... und irgendwann hat man ein Produkt, 
mit dem man etwas anfangen kann.
Achtet man aber anfangs nicht so sehr darauf, dass der Entwurf des Programms logisch und gut  
wartbar ist, können einem später Stolpersteine entgegenkommen.
Möchte man das Programm später um Funktionalität erweitern, kann es nun schwierig sein diese 
einzubauen.

[ENDSECTION]
[SECTION::instructions::detailed]

Erstellen Sie ein Markdown-Dokument `extraction-of-code.md` und erstellen Sie darin die drei 
Überschriften `Extraktion von Variablen`, `Extraktion von Methoden` und `Extraktion von Klassen`.
Lesen Sie anschließend die drei Artikel 
[Extract Variable](https://refactoring.guru/extract-variable), 
[Extract Method](https://refactoring.guru/extract-method) und 
[Extract Class](https://refactoring.guru/extract-class), 
und beantworten Sie anschließend zu **jedem** Artikel jeweils die folgenden Fragen: 

- [EQ] Welches Problem löst diese Refaktorierung?
- [EQ] Wie wird diese Refaktorierung per Hand durchgeführt?
- [EQ] Auf welche Fallstricke soll man bei dieser Refaktorierung achten?
- [EQ] Recherchieren und beschreiben Sie, wie Ihre IDE Ihnen hilft diese Refaktorierung
  durchzuführen.  
  Bietet Ihre IDE Ihnen hierfür eine Funktion an?  
  Wie löst man diese Funktion aus?

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kurzfassung]

- Variablenextraktion hilft u. a. Ausdrücke verständlicher zu machen.
- PyCharm hilft über den Refactor-Dialog bei der Durchführung.

- Methodenextraktion hilft Code deutlich lesbarer zu machen und vermeidet Code-Duplikation.
- PyCharm hilft über den Refactor-Dialog bei der Durchführung.

- Klassenextraktion hilft Klassen mehr zu spezialisieren, sie sollen nach Möglichkeit nur eine 
  Aufgabe haben.
  Das fördert das _Single Responsibility Principle_.
- PyCharm hilft über den Refactor-Dialog bei der Durchführung.

[ENDINSTRUCTOR]
