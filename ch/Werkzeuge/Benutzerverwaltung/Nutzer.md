title: nutzer
stage: draft
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

Ich verstehe wie man einen Nutzer erstellt, bei einem Nutzer die Rechte ändert, einen Nutzer löscht und welche Befehle ich dafür nutzen muss.

[ENDSECTION]
[SECTION::background::default]

Linux Systeme sind meist Systeme, die von mehreren Nutzern gleichzeitig genutzt werden. Somit braucht jeder Nutzende ein eigenes Konto.

[ENDSECTION]
[SECTION::instructions::detailed]
### Neuen Nutzer erstellen

- [EC] Erstellen Sie einen neuen Nutzer namens `otto` mit dem Befehl `useradd`:  
    `sudo useradd otto`  

- [EQ] Öffnen Sie die `/etc/passwd` und erklären Sie die einzelnen Spalten des Nutzers `otto`.

- [EC] Überprüfen Sie ob der home-Ordner von otto vorhanden ist.

- [EC] Erstellen Sie einen neuen Nutzer namens Bob mit dem `adduser` Befehl.  
    Bei den persönlichen Fragen, lassen Sie die Felder leer.

- [EQ] Erklären Sie den Unterschied der Befehle `useradd` und `adduser`.

### Passwörter für Nutzer setzen

- [EC] Setzen Sie ein Passwort für beide oben erstellte Nutzer. Nutzen Sie dafür den Befehl `passwd`.

### Ändern der Rechte für Nutzer

Nach bestimmten Datenschutzrichtlinien müssen Benutzer eines Systems aufbewahrt werden. Somit müssen sie erst gesperrt werden.  
- [EC] Nutzen sie `usermod` um den Nutzer `bob` und `otto` zu sperren.

Nachdem die Nutzer gesperrt wurden und eine bestimmte Zeitspanne vorbei ist, müsssen Nutzer und Dateien des Nutzers auf dem System gelöscht werden.  
- [EC] Nutzen Sie den Befehl `deluser` um alle Dateien der Nutzer und die Nutzer selber von ihrem System zu löschen.
[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::heading]
[EREFC::7] Prüfen ob die Option für alle Dateien gesetzt ist.
[ENDINSTRUCTOR]
