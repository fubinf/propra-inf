title: Gruppen
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Nutzer, Dateiberechtigungen, sudo
---

[SECTION::goal::idea]
Ich verstehe Gruppen in Linux und wie ich diese bei Nutzern ändern kann.
[ENDSECTION]

[SECTION::background::default]
In Linux spielen Gruppen eine wichtige Rolle bei der Verwaltung von Benutzerrechten und der 
Organisation von Nutzern auf einem System.
[ENDSECTION]

[SECTION::instructions::detailed]
### Nutzer erstellen

- [EC] Erstellen Sie zwei neuen Nutzer namens `nutzer1` und `nutzer2`.

### Gruppe erstellen

- [EC] Erstellen Sie eine neue Gruppe namens `propra`.
- [EC] Fügen sie die Gruppe `propra` `nutzer1` hinzu.
- [EC] Melden Sie sich als `nutzer1` an.
- [EC] Erstellen Sie eine Datei namens `datei1` mit `nutzer1`.

Lesen Sie die Abschnitte **Synopsis**, **Description** und **Examples** der
chgrp(1) [manpage](https://linux.die.net/man/1/chgrp)

- [EC] Ändern Sie die Gruppe der datei1 zu propra.
- [EC] Melden Sie sich als `nutzer2` an und versuchen Sie die `datei1` zu bearbeiten.

Wie Sie merken, können Sie die Datei nicht bearbeiten. Es gibt jedoch noch eine Möglichkeit ohne dass 
`nutzer2` der Gruppe `propra` zugehörig ist, um die Datei zu bearbeiten.

- [EC] Finden Sie die Möglichkeit heraus und wenden Sie sie an.

### Standardgruppe setzen

Die Standardgruppe eines Nutzers gibt an, welche Gruppe die Dateien eines Nutzers haben sollen 
und worauf dieser Nutzer Zugriff haben soll.
Das Ändern diese Gruppe kann sinnvoll sein, wenn man seine Dateien mit anderen Mitarbeitern auf 
seinem System teilen möchte, indem man nur die Dateiberechtigungen ändern kann.

- [EC] Erstellen sie eine Datei `datei2` mit dem Nutzer `nutzer1`.
- [EC] Welche Berechtigungen hat die Datei. Welchen Nutzer und welche Gruppe hat die Datei.

Lesen Sie die Abschnitte **Synopsis** und **Description** der adduser(8) 
[manpage](https://linux.die.net/man/8/adduser).

- [EC] Erstellen Sie eine neue Gruppe namens `standard`. 

Lesen Sie die Abschnitte **Synopsis**, **Description** und die **Optionen** -a, -g, -G der 
usermod(8) [manpage](https://linux.die.net/man/8/usermod)

- [EC] Setzen Sie die Gruppe `standard` als Standardgruppe für den Nutzer `nutzer1`.
- [EC] Erstellen Sie eine Datei `datei3` mit dem Nutzer `nutzer1`.
- [EQ] Schauen Sie sich die Berechtigungen der beiden Dateien an. Was fällt auf?
- [EC] Setzen Sie die Gruppe von `nutzer1` wieder zurück.

### Nutzer und Gruppe löschen

Damit Ihr System nicht vollgemüllt wird, löschen wir noch die gerade erstellten Nutzer und Gruppen.

Lesen Sie die Abschnitte **Synopsis**, **Description** und **Remove a group** der deluser(8) 
[manpage](https://manpages.debian.org/jessie/adduser/deluser.8.en.html).

- [EC] Löschen Sie die erstellten Nutzer.
- [EC] Löschen Sie die erstellten Gruppen.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]

[ENDINSTRUCTOR]