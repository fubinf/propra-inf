title: Dateiberechtigungen
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Nutzer
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
Lesen Sie sich diesen [Beitrag](https://wiki.ubuntuusers.de/Rechte/) über `chmod` durch.

- [EC] Erstellen Sie eine Datei namens `berechtigungen`.
- [EC] Schauen Sie sich die Berechtigungen der Datei mit `ls -l` an. Beschreiben Sie die Berechtigungen der Datei.
- [EC] Geben Sie der Gruppe für die Datei volle Zugriffsrechte.
- [EC] Ändern Sie den Eigentümer von `berechtigungen` zu `bob`.
- [EC] Ändern Sie die Gruppe von `berechtigungen` zu `bob`.
- [EQ] Was macht dieses Kommando: `chmod 0754 ~/berechtigungen && sudo chown 1001:1001 ~/berechtigungen`?


[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]

