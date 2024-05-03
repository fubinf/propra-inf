title: Nutzer
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: sudo
---

[SECTION::goal::idea]
Ich verstehe wie man einen Nutzer erstellt, bei einem Nutzer die Rechte ändert, einen Nutzer löscht und welche Befehle ich dafür nutzen muss.
[ENDSECTION]

[SECTION::background::default]
Nutzer in Linux sind individuelle Konten, die es den Benutzern ermöglichen, auf einem System zu arbeiten und Ressourcen zu nutzen.
[ENDSECTION]

[SECTION::instructions::detailed]
Machen Sie sich mit den Kommandos in diesem [Beitrag](https://wiki.ubuntuusers.de/Benutzer_und_Gruppen/) vertraut.  

### Neuen Nutzer erstellen

- [EC] Erstellen Sie einen neuen Nutzer namens `otto` mit dem Befehl `useradd`:  
    `sudo useradd otto`  
- [EQ] Öffnen Sie die `/etc/passwd` und erklären Sie die einzelnen Spalten des Nutzers `otto`.
- [EC] Überprüfen Sie ob der home-Ordner von otto vorhanden ist.
- [EC] Erstellen Sie einen neuen Nutzer namens Bob mit dem `adduser` Befehl.  
    Bei den persönlichen Fragen, lassen Sie die Felder leer.
- [EQ] Erklären Sie den Unterschied der Befehle `useradd` und `adduser`.

### Passwörter für Nutzer setzen

- [EC] Setzen Sie ein Passwort für beide oben erstellte Nutzer.

### Ändern der Rechte für Nutzer

In den meisten Firmen müssen Nutzer eines Systems nach bestimmten Datenschutzrichtlinien aufvewahrt werden. Somit müssen diese erst gesperrt werden.

- [EC] Sperren Sie die Nutzer `bob` und `otto`.

Nachdem die Nutzer gesperrt wurden und eine bestimmte Zeitspanne vorbei ist, müsssen Nutzer und Dateien des Nutzers auf dem System gelöscht werden.

- [EC] Löschen Sie beide Nutzer und all deren Dateien von Ihrem System.
[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::heading]
[EREFC::6] Prüfen ob die Option für alle Dateien gesetzt ist.
[ENDINSTRUCTOR]
