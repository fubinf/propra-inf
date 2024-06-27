title: Dateiberechtigungen
stage: beta
timevalue: 1.0
difficulty: 2
assumes: Manpages, Benutzerkonten, Umgang-mit-Verzeichnissen
explains: Rechte
---

[SECTION::goal::idea]
Ich verstehe Unix-Dateiberechtigungen und wie ich diese ändern kann.
[ENDSECTION]

[SECTION::background::default]
Dateiberechtigungen in Unix spielen eine entscheidende Rolle bei der Sicherheit eines Systems.
Da in Unix fast alles als Datei dargestellt ist (nicht nur normale Dateien), lässt sich mit
diesem einen, recht einfachen Mechanismus verblüffend viel bewerkstelligen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Dateiberechtigungen

Lesen Sie den Eintrag [TERMREF::Dateiberechtigungen].
Diese Berechtigungen geben also an, wer auf eine Datei oder einen Ordner zugreifen kann.

Lesen Sie [HREF::https://wiki.ubuntuusers.de/Rechte/] 
bis einschließlich Abschnitt **Zugriffsrecht**.

- [EC] Erstellen Sie eine Datei namens `Dateiberechtigungen1`.

Nachdem Sie die Datei erstellt haben, müssen wir erstmal herausfinden, wer Zugriff auf die Datei hat.

- [EC] Geben Sie die Berechtigungen nur dieser einen Datei mit `ls -l` aus. 
- [EQ] Geben Sie in eigenen Worten an, welche Berechtigungen die Datei hat: Wer darf was?.

Ein Mitarbeiter teilt Ihnen mit, dass er Zugriff auf eine Datei auf dem Server braucht. Nach einer 
Diskussion, entscheiden Sie und der Mitarbeiter, dass der Mitarbeiter die vollen Zugriffsrechte 
bekommt, genauso wie der Besitzer und der Gruppenbesitzer der Datei wird, weil der ursprüngliche 
Besitzer nicht mehr in der Firma arbeitet. 

- [EC] Erstellen Sie einen neuen Nutzer namens `rechtenutzer`.

Lesen Sie die Abschnitte **Anwendung** und **Aufruf** von 
[HREF::https://wiki.ubuntuusers.de/chmod/].

- [EC] Ändern Sie die Zugriffsrechte der Datei `Dateiberechtigungen1` so, dass der Nutzer und die Gruppe 
   Lese-, Schreib- und Ausführrechte hat.

Lesen Sie die Abschnitte **Syntax** und **Beispiele** von 
[HREF::https://wiki.ubuntuusers.de/chown/].

- [EC] Ändern Sie den Eigentümer von `Dateiberechtigungen1` zu `rechtenutzer`.

Lesen Sie die Abschnitte **Syntax** und **Beispiel** von 
[HREF::https://wiki.ubuntuusers.de/chgrp/].

- [EC] Ändern Sie die Gruppe von `Dateiberechtigungen1` zu `rechtenutzer`.
- [EQ] Beschreiben Sie in Ihren Worten, was dieses Kommando macht: 
   `chmod -R 0754 Dateiberechtigungsordner/ && sudo chown -R rechtenutzer:rechtenutzer Dateiberechtigungsordner/`?
- [EC] Löschen Sie die Datei `Dateiberechtigungen1` und den Benutzer `rechtenutzer`.

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]