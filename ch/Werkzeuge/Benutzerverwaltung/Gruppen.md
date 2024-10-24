title: Gruppen
stage: beta
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

Verstehen Sie die **Synopsis** (insbesondere die Punkte des Befehls `addgroup`) und lesen Sie die 
**Description**, insbesondere die Abschnitte **Add a group** und 
**Add an existing user to an existing group** der 
[adduser(8) manpage](https://manpages.debian.org/bookworm/adduser/adduser.8.en.html) 
(ja, das ist kein Irrtum).

- [EC] Erstellen Sie eine neue Gruppe namens `propra`.
- [EC] Fügen sie der Gruppe `propra` den Account `nutzer1` hinzu.
- [EC] Wechseln Sie zu `nutzer1`.
- [EC] Erstellen Sie als `nutzer1` eine Datei namens `datei1` mit dem Inhalt "ich bin datei1".
- [EC] Stellen Sie mit `chmod` sicher, dass `datei1` volle Rechte (rwx) für seine Gruppe hat
  und keine Rechte (---) für Other.

Verstehen Sie die **Synopsis**, lesen Sie die **Description** (Einleitung reicht) und die **Examples** der
[chgrp(1) manpage](https://linux.die.net/man/1/chgrp)

- [EC] Wechseln Sie zurück zu Ihrem personlichen Nutzer.
- [EC] Ändern Sie mit `chgrp` die Gruppe der `datei1` zu `propra`.
- [EC] Wechseln Sie zu `nutzer2`.
- [EC] Versuchen Sie die Datei `datei1` auszugeben.

Wie Sie merken, können Sie die Datei nicht lesen. `nutzer2` ist nicht der Besitzer der Datei, 
ist nicht in der Gruppe `propra` und Other dürfen die Datei nicht lesen.

### Standardgruppe setzen

Die Standardgruppe eines Nutzers gibt an, welche Gruppe neue Dateien eines Nutzers bekommen sollen.
Das Ändern dieser Gruppe kann sinnvoll sein, 
wenn man über eine gemeinsame Gruppe Dateien mit anderen Benutzern teilen möchte.

Lesen Sie die Abschnitte **Synopsis**, **Description** und die **Optionen** **-a, -g, -G** der 
[usermod(8) manpage](https://linux.die.net/man/8/usermod)

- [EC] Wechseln Sie zu `nutzer1`.
- [EC] Erstellen sie eine Datei `datei2` mit dem Inhalt "ich bin datei2".
- [EQ] Welche Berechtigungen hat die Datei? Welchen Nutzer und welche Gruppe hat die Datei?
- [EC] Wechseln Sie zurück zu Ihrem persönlichen Nutzer.
- [EC] Erstellen Sie eine neue Gruppe namens `standard`. 
- [EC] Setzen Sie die Gruppe `standard` als Standardgruppe für den Nutzer `nutzer1`.
- [EC] Wechseln Sie zu `nutzer1`.
- [EC] Erstellen Sie eine Datei `datei3`.
- [EQ] Schauen Sie sich die Berechtigungen der beiden Dateien an. Was fällt auf? 
  Was folgt daraus für eine Zusammenarbeit mit gemeinsamen Dateien?
- [EC] Wechseln Sie zurück zu Ihrem persönlichen Nutzer.
- [EC] Setzen Sie die Gruppe von `nutzer1` wieder zurück auf den vorherigen Wert.

### Nutzer und Gruppe löschen

Damit Ihr System nicht vollgemüllt wird, löschen wir noch die gerade erstellten Nutzer, Gruppen und Dateien.

Lesen Sie die Abschnitte **Synopsis**, **Description** und **Remove a group** der 
[deluser(8) manpage](https://manpages.debian.org/bookworm/adduser/deluser.8.en.html).

- [EC] Löschen Sie die erstellten Nutzer `nutzer1`, `nutzer2` und deren home-Verzeichnis.
- [EC] Löschen Sie die erstellten Gruppen `propra` und `standard`.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:Gruppen.prot]
[ENDINSTRUCTOR]

[INSTRUCTOR::Markdowndokument]

[INCLUDE::ALT:]
[ENDINSTRUCTOR]