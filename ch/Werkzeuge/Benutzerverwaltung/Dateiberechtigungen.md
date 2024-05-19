title: Dateiberechtigungen
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Nutzer, Umgang-mit-Verzeichnissen
---

[SECTION::goal::idea]
Ich verstehe Dateiberechtigungen und wie ich diese ändern kann.
[ENDSECTION]

[SECTION::background::default]
Dateiberechtigungen in Linux spielen eine entscheidende Rolle bei der Sicherheit und dem Zugriff 
auf Dateien und Verzeichnissen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Dateiberechtigungen

Die [TERMREF::Dateiberechtigungen] geben an, wer Zugriff auf Dateien und Ordner hat.

Lesen Sie bis zum Abschnitt **Zugriffsrecht** den [Beitrag](https://wiki.ubuntuusers.de/Rechte/) 
von ubuntuusers über Rechte.

- [EC] Erstellen Sie eine Datei namens `berechtigungen`.

Nachdem Sie die Datei erstellt haben, müssen wir erstmal herausfinden, wer Zugriff auf die Datei hat.

- [EC] Geben Sie die Berechtigungen der Datei `berechtigungen` mit `ls -l` aus. 
- [EQ] Geben Sie in Ihren Worten an, welche Berechtigungen die von Ihnen erstellte Datei 
   `berechtigungen` hat.

Ein Mitarbeiter teilt Ihnen mit, dass er Zugriff auf eine Datei auf dem Server braucht. Nach einer 
Diskussion, entscheiden Sie und der Mitarbeiter, dass der Mitarbeiter die vollen Zugriffsrechte 
bekommt, genauso wie der Besitzer und der Gruppenbesitzer der Datei wird, weil der ursprüngliche 
Besitzer nicht mehr in der Firma arbeitet. 

- [EC] Erstellen Sie einen neuen Nutzer namens `nutzer`.

Lesen Sie die Abschnitte **Anwendung** und **Aufruf** des 
[Beitrags](https://wiki.ubuntuusers.de/chmod/) von ubuntuusers über chmod.

- [EC] Ändern Sie die Zugriffsrechte der Datei `berechtigungen` so, dass der Nutzer und die Gruppe 
   Lese-, Schreib- und Ausführrechte hat.

Lesen Sie die Abschnitte **Syntax** und **Beispiele** des 
[Beitrags](https://wiki.ubuntuusers.de/chown/) von ubuntuusers über chown.

- [EC] Ändern Sie den Eigentümer von `berechtigungen` zu `nutzer`.

Lesen Sie die Abschnitte **Syntax** und **Beispiel** des 
[Beitrags](https://wiki.ubuntuusers.de/chgrp/) von ubuntuusers über chgrp.

- [EC] Ändern Sie die Gruppe von `berechtigungen` zu `nutzer`.

Mit dem Wissen was Sie oben erlangt haben.

- [EQ] Beschreiben Sie in Ihren Worten, was dieses Kommando macht: 
   `chmod -R 0754 ~/berechtigungen && sudo chown -R nutzer:nutzer ~/berechtigungen`?


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[ENDINSTRUCTOR]