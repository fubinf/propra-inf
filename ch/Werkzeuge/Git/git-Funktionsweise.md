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


### Hilfe finden

Es gibt viele git-Kommandos und sehr viele Arten, diese zu benutzen.
Niemand hat das alles im Kopf.  

- Sucht man nach dem Namen eines Kommandos, hilft `git help`.  
- Ist einem zum Kommando `xyz` eine Option entfallen oder unbekannt,
  geht es mit `git help xyz` weiter (oder gleichwertig: `man git-xyz`).  
- Einen (eher selten nützlichen) Überblick und Verweise auf (schon eher nützliche) andere 
  lokale Informationsquellen) liefert `man git`.
- Wenn man ausführlicher nachlesen will, ist meist die Webseite besser:
  [HREF::https://git-scm.com/doc]

Es ist völlig normal, anfangs nicht alles zu verstehen, was auf einer solchen Hilfeseite steht.
Je häufiger Sie git verwenden und je mehr Aufgaben Sie im ProPra mit git erledigen, desto mehr
werden Sie auch von den Hilfeseiten verstehen.

Bis dahin: Konzentrieren Sie sich auf das, was für Sie gerade relevant ist und was Sie bereits
verstehen.
[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Die 5 Ideen liefern alle Antworten]
Die Hauptpunkte entsprechen den Überschriften auf "What is Git?": 
Schnappschüsse, lokale Operationen, Hashes, Zufügen-statt-Ändern, Zustände modified/staged/committed.
[ENDINSTRUCTOR]
