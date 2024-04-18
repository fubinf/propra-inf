title: Wie funktioniert git?
stage: beta
timevalue: 0.75
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe 5 Grundideen der Funktionsweise von git und habe ein korrektes
mentales Modell von git.
[ENDSECTION]

[SECTION::background::default]
Wenn man diese 5 Tatsachen nicht kennt, bleibt vieles in git rätselhaft,
das an sich gar nicht sehr kompliziert ist.
[ENDSECTION]

[SECTION::instructions::loose]

### Einlesen

Lesen Sie [What is Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) gründlich durch.
Identifizieren und verstehen Sie die fünf Ideen.

Neugierig geworden?
Dann lesen Sie gleich auf
"[Recording Changes to the Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)" 
weiter.
Das dortige Wissen wird zwar erst für spätere Aufgaben relevant, ergänzt die Grundideen
aber gut um zugehörige praktische Aspekte.

### Reflektieren

- [EQ] Fassen Sie die fünf Hauptpunkte in eigenen Worten in je einem Satz zusammen.
- [EQ] Wenn man eine Datei so ändert, dass ihre Größe und ihr Zeitstempel gleich bleiben,
  woran kann git trotzdem feststellen, dass sie geändert wurde?
- [EQ] Warum kann man git auch unterwegs oder ohne Internet gut benutzen?
- [EQ] Warum gehen viele Operationen in git so schnell?
- [EQ] In welchen drei Punkten lässt sich der Git workflow einfach zusammenfassen?


[ENDSECTION]
[SECTION::submission::reflection]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Die 5 Ideen liefern alle Antworten]
Die Hauptpunkte entsprechen den Überschriften auf "What is Git?": 
Schnappschüsse, lokale Operationen, Hashes, Zufügen-statt-Ändern, Zustände modified/staged/committed.
[ENDINSTRUCTOR]
