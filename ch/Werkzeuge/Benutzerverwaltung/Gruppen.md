title: Gruppen
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Benutzerkonten, Dateiberechtigungen, sudo
---

[SECTION::goal::trial]
Ich verstehe Gruppen in Linux und wie ich diese bei Nutzern ändern kann.
[ENDSECTION]

[SECTION::background::default]
In Unix spielen Gruppen eine wichtige Rolle bei der Verwaltung von Benutzerrechten und der 
Organisation von Nutzern auf einem System.
Man braucht sie, wenn Dateien von mehreren aber nicht allen Benutzern zugreifbar sein sollen.
[ENDSECTION]

[SECTION::instructions::detailed]
### Nutzer erstellen

- [EC] Erstellen Sie zwei neue Nutzer namens `nutzer1` und `nutzer2`.

### Gruppe erstellen

Lesen Sie die Abschnitte **Synopsis** und **Description** (Einleitung reicht) der 
[adduser(8) manpage](https://linux.die.net/man/8/adduser) (ja, das ist kein Irrtum).

- [EC] Erstellen Sie eine neue Gruppe namens `propra`.
- [EC] Fügen sie der Gruppe `propra` den Account `nutzer1` hinzu.
- [EC] Wechseln Sie zu `nutzer1`.
- [EC] Erstellen Sie als `nutzer1` eine Datei namens `datei1` mit dem Inhalt "ich bin datei1".
- [EC] Stellen Sie mit `chmod` sicher, dass `datei1` volle Rechte (rwx) für seine Gruppe hat
  und keine Rechte (---) für Other.

Lesen Sie die Abschnitte **Synopsis**, **Description** und **Examples** der
[chgrp(1) manpage](https://linux.die.net/man/1/chgrp)

- [EC] Ändern Sie mit `chgrp` die Gruppe der `datei1` zu `propra`.
- [EC] Melden Sie sich als `nutzer2` an und versuchen Sie die `datei1` auszugeben.

Wie Sie merken, können Sie die Datei nicht lesen. 

### Standardgruppe setzen

Die Standardgruppe eines Nutzers gibt an, welche Gruppe neue Dateien eines Nutzers bekommen sollen.
Das Ändern dieser Gruppe kann sinnvoll sein, 
wenn man über eine gemeinsame Gruppe Dateien mit anderen Benutzern teilen möchte.

- [EC] Gehen Sie zurück zu `nutzer1`.
- [EC] Erstellen sie eine Datei `datei2`.
- [EC] Welche Berechtigungen hat die Datei? Welchen Nutzer und welche Gruppe hat die Datei?
- [EC] Erstellen Sie eine neue Gruppe namens `standard`. 

Lesen Sie die Abschnitte **Synopsis**, **Description** und die **Optionen** -a, -g, -G der 
[usermod(8) manpage](https://linux.die.net/man/8/usermod)

- [EC] Setzen Sie die Gruppe `standard` als Standardgruppe für den Nutzer `nutzer1`.
- [EC] Erstellen Sie (weiterhin als Nutzer `nutzer1`) eine Datei `datei3`.
- [EQ] Schauen Sie sich die Berechtigungen der beiden Dateien an. Was fällt auf?
  Was folgt daraus für eine Zusammenarbeit mit gemeinsamen Dateien?
- [EC] Setzen Sie die Gruppe von `nutzer1` wieder zurück auf den vorherigen Wert.

### Nutzer und Gruppe löschen

Damit Ihr System nicht vollgemüllt wird, löschen wir noch die gerade erstellten Nutzer und Gruppen.

Lesen Sie die Abschnitte **Synopsis**, **Description** und **Remove a group** der 
[deluser(8) manpage](https://manpages.debian.org/jessie/adduser/deluser.8.en.html).

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