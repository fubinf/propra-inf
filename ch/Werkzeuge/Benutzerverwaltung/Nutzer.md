title: Nutzer
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: sudo
---

[SECTION::goal::idea]
Ich verstehe wie man einen Nutzer erstellt, bei einem Nutzer die Rechte ändert, einen Nutzer 
löscht und welche Befehle ich dafür nutzen muss.
[ENDSECTION]

[SECTION::background::default]
Nutzer in Linux sind individuelle Konten, die es den Benutzern ermöglichen, auf einem System zu 
arbeiten und Ressourcen zu nutzen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Neuen Nutzer erstellen

Stellen Sie sich vor, Sie sind ein Administrator in einer mittelständischen Firma. Ein neuer 
Mitarbeiter wurde angestellt. Sie wurden beauftragt diesen Nutzer einzurichten. Sie informieren 
sich, wie man Nutzer auf Linux einrichtet und finden zwei Möglichkeiten: `useradd` und `adduser`.
Sie probieren beide aus, damit Sie sich entscheiden können, welche von beiden Sie später weiter
nutzen möchten.

Verstehen Sie die **Synopsis**, lesen Sie die **Description**, und die Optionen **-g, -N, -U** der 
useradd(8) [manpage](https://linux.die.net/man/8/useradd).

- [EC] Erstellen Sie einen neuen Nutzer namens `user1` mit dem Befehl `useradd`.

Lesen Sie die **Description** der passwd(5) [manpage](https://linux.die.net/man/5/passwd).

- [EQ] Erklären Sie die einzelnen Spalten des Nutzers `user1` aus der `/etc/passwd`.
- [EC] Überprüfen Sie ob der home-Ordner von `user1` vorhanden ist.

Verstehen Sie die **Synopsis**, lesen Sie die **Description** und lesen Sie die Abschnitte 
**Add a normal user** und **Add a system user** der adduser(8) 
[manpage](https://manpages.debian.org/bookworm/adduser/adduser.8.en.html).

- [EC] Erstellen Sie einen neuen Nutzer namens `user2` mit dem `adduser` Befehl.  
    Bei den persönlichen Fragen, lassen Sie die Felder leer.
- [EQ] Erklären Sie den Unterschied der Befehle `useradd` und `adduser`.

### Passwörter für Nutzer setzen

Lesen Sie in den manpages von [useradd](https://linux.die.net/man/8/useradd) und 
[adduser](https://manpages.debian.org/bookworm/adduser/adduser.8.en.html) nach, wie man ein 
Passwort setzt.

- [EC] Setzen Sie ein Passwort für beide oben erstellte Nutzer.

### Ändern der Rechte für Nutzer

Ein Mitarbeiter kündigt und Sie sind zuständig, dass die Nutzerkonten des Mitarbeiters gesperrt 
werden.

Schauen Sie in der [useradd(8)](https://linux.die.net/man/8/useradd) manpage nach Optionen, wie 
man Nutzer sperrt.

- [EC] Sperren Sie die Nutzer `user1` und `user2`.

Nachdem die Nutzer gesperrt wurden und eine datenschutzrechtliche konforme Zeitspanne vorbei ist, 
müsssen Nutzer und Dateien des Nutzers auf dem System gelöscht werden.

Schauen Sie in der [useradd(8)](https://linux.die.net/man/8/useradd) manpage nach Optionen, wie 
man Nutzer und deren Dateien löscht.

- [EC] Löschen Sie beide Nutzer und all deren Dateien von Ihrem System.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[EREFC::6] Prüfen ob die Option für alle Dateien gesetzt ist.
