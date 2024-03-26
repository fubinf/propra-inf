title: Dateiberechtigungen
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe Dateiberechtigungen und wie ich diese ändern kann.
[ENDSECTION]

[SECTION::background::default]
Dateiberechtigungen in Linux spielen eine entscheidende Rolle bei der Sicherheit und dem Zugriff auf Dateien und Verzeichnisse.
[ENDSECTION]

[SECTION::instructions::detailed]

### Dateiberechtigungen

Lesen Sie sich [TERMREF::Dateiberechtigungen] durch.  
Lesen Sie sich diesen [Beitrag](https://wiki.ubuntuusers.de/Rechte/) über chmod durch.

- [EC] Erstellen Sie eine Datei namens `berechtigungen`.
- [EC] Schauen Sie sich die Berechtigungen der Datei mit `ls -l` an. Beschreiben Sie die Berechtigungen der Datei.
- [EC] Geben Sie der Gruppe für die Datei volle Zugriffsrechte. Nutzen Sie dafür `chmod`.
- [EC] Ändern Sie den Eigentümer der Datei zu `bob`. Nutzern Sie dafür `chown`.
- [EC] Ändern Sie die Gruppe zu `bob`. Nutzen Sie dafür `chgrp`.


[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

