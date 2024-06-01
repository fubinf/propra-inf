title: Access Control Lists
stage: alpha
timevalue: 2
difficulty: 3
assumes: apt, Gruppen, sudo, Umgang-mit-Verzeichnissen
---

[SECTION::goal::idea]

Ich verstehe ACLs und weiß wie ich diese ändern kann.

[ENDSECTION]

[SECTION::background::default]

ACLs (Access Control Lists) sind Listen, die den Zugriff auf Ressourcen regeln. 
ACLs werden zusätzlich zu den Unix-Standardberechtigungen gesetzt.

[ENDSECTION]

[SECTION::instructions::detailed]

Stellen Sie sich vor Sie arbeiten in einer Firma mit zwei Geschäftsführern. Die Firma hat eine 
Abteilung Rechnungswesen. Diese Abteilung hat ihren eigenen Ordner, wo sie ihre Daten ablegen. 
Jetzt wollen die Geschäftsführer auch Zugriff auf einen bestimmten Ordner der Abteilung 
Rechnungswesen bekommen, damit Sie da auch Dateien lesen und ablegen können. Mit den normalen 
Unix-Rechten werden wir da schnell in Probleme geraten. [TERMREF::ACLs] lösen dieses Problem komfortabler. Wir 
bringen Ihnen diese hier näher.

### Testumgebung erstellen

- [EC] Erstellen Sie zwei Nutzer `aclnutzer1` und `aclnutzer2`.
- [EC] Erstellen Sie zwei Gruppen `aclgroup1` und `aclgroup2`.
- [EC] Fügen Sie den Nutzer `aclnutzer1` zur Gruppe `aclgroup1` und `aclnutzer2` zur Gruppe `aclgroup2`.

Erstellen Sie die nächsten Ordner und Dateien mit Ihrem persönlichen Nutzer, nicht mit `aclnutzer1` 
oder `aclnutzer2`.

- [EC] Erstellen Sie den Ordner `/folder`
- [EC] Ändern Sie den Nutzer und die Gruppe des Ordners `/folder` zu ihrem persönlichen 
    Nutzerkonto und die dazugehörige Grupppe.
- [EC] Erstellen Sie den Ordner `/folder/subfolder1/`.
- [EC] Erstellen Sie den Ordner `/folder/subfolder2/`.
- [EC] Erstellen Sie die Dateien `folder_data1`, `folder_data2` in `folder`.
- [EC] Erstellen Sie die Dateien `subfolder1_data1`, `subfolder1_data2` in `subfolder1`.
- [EC] Erstellen Sie die Dateien `subfolder2_data1`, `subfolder2_data2` in `subfolder2`.
- [EC] Ändern Sie die Rechte von den erstellten Ordnern, Subordnern und Dateien so ab, dass Ihr 
    persönliches Nutzerkonto und die gleichnamige Gruppe Lese-, Schreib- und Ausführrechte hat.

Die Nutzer `aclnutzer1` und `aclnutzer2` sollen erstmal keine Rechte auf die Daten haben.

### Überblick verschaffen

Lesen Sie die [getfacl(1) manpage](https://linux.die.net/man/1/getfacl) bis einschließlich 
**Permissions**.

- [EC] Geben Sie die ACLs von `folder` aus.
- [EC] Geben Sie die ACLs von `subfolder1` aus.
- [EC] Geben Sie die ACLs von `subfolder2` aus.
- [EC] Geben Sie die ACLs von `subfolder1_data1` aus. 
- [EC] Geben Sie die ACLs von `subfolder2_data1` aus.

Sie haben gerade die normalen Unix-Rechte im [TERMREF::ACL] Format gesehen.  
Setzen wir ein paar [TERMREF::ACLs].

### ACLs setzen

Lesen Sie die [setfacl(1) manpage](https://linux.die.net/man/1/setfacl) bis einschließlich 
**Permissions**, die Optionen **-R, -b**, die **Examples** und die **ACL Entries**.

Im Nachfolgenden wird mit Schreibrechten Schreib- und Leserechte gemeint.

- [EC] Geben Sie `aclnutzer1` und `aclnutzer2` Leserechte auf den Ordner `folder`.
- [EC] Geben Sie `aclnutzer1` Schreibrechte auf den Ordner `subfolder1` mit einer ACL Änderung.
- [EC] Geben Sie `aclnutzer2` Schreibrechte auf den Ordner `subfolder2` mit einer ACL Änderung.
- [EC] Geben Sie `aclnutzer1` Schreibrechte auf die Datei `subfolder1_data1` mit einer ACL Änderung.
- [EC] Geben Sie `aclnutzer2` Schreibrechte auf die Datei `subfolder2_data2` mit einer ACL Änderung.
- [EC] Geben Sie die ACLs von `subfolder1`, `subfolder2`, `subdfolder1_data1`, `subdfolder1_data2`, 
    `subdfolder2_data1` und `subdfolder2_data2` aus.

### Testen

Wenn alles richtig verlaufen ist, dann sollten Sie jetzt mit den Nutzern in die jeweiligen Dateien schreiben können.

- [EC] Schreiben Sie mit `aclnutzer1` "aclnutzer1 hat das geschrieben" in die Datei `subfolder1_data1`.
- [EC] Schreiben Sie mit `aclnutzer2` "aclnutzer2 hat das geschrieben" in die Datei `subfolder2_data2`.

### Default ACLs

Sie haben vorhin einzeln alle Rechte gesetzt. Dies lässt sich komfortabler lösen, indem man 
`default ACLs` setzt. Die `default ACLs` vererben die Rechte des Ordner auf alle darunter liegenden 
Ordner und Daten, sofern man dies explizit angibt oder diese nach der ACL-Änderung neu erstellt 
werden.

Wir werden die Rechte hier jetzt mit den Gruppen bearbeiten. Das gilt natürlich analog auch für 
die Nutzer.

- [EC] Geben Sie `aclgroup1` Schreibrechte auf den Ordner `subfolder1` und den darunterliegenden Dateien.
- [EC] Setzen Sie eine default-ACL für `aclgroup1` mit Schreibrechten auf den Ordner `subfolder1` 
    und den darunterliegenden Dateien.
- [EC] Geben Sie `aclgroup2` Schreibrechte auf den Ordner `subfolder2` und den darunterliegenden Dateien.
- [EC] Setzen Sie eine default-ACL für `aclgroup2` mit Schreibrechten auf den Ordner `subfolder2` 
    und den darunterliegenden Dateien.
- [EC] Erstellen Sie mit Ihrem persönlichen Nutzer zwei Dateien `subfolder1_data3` und 
    `subfolder2_data3` in den jeweiligen Ordnern.
- [EC] Geben Sie die ACLs von `subfolder1`, `subfolder2`, `subdfolder1_data1`, `subdfolder1_data2`, 
    `subdfolder1_data3`, `subdfolder2_data1`, `subdfolder2_data2` und `subdfolder2_data3` aus.

Wie Sie sehen wurden bei den neu erstellten Dateien `subfolder1_data3` und `subfolder2_data3` 
automatisch die Rechte für die jeweiligen Gruppen mit hinzugefügt.

### Testen

Wenn alles richtig verlaufen ist, dann sollten die nächsten Befehle alle erfolgreich sein.

- [EC] Schreiben Sie mit `aclnutzer1` "aclnutzer1 hat das geschrieben" in die Datei `subfolder1_data3`.
- [EC] Schreiben Sie mit `aclnutzer2` "aclnutzer2 hat das geschrieben" in die Datei `subfolder2_data3`.
- [EC] Erstellen Sie mit `aclnutzer1` eine neue Datei namens `subfolder1_data4` in den Ordner 
    `subfolder1`.
- [EC] Erstellen Sie mit `aclnutzer2` eine neue Datei namens `subfolder2_data4` in den Ordner 
    `subfolder2`.

Versuchen wir jetzt mit den Nutzern in die Ordner zu schreiben, in denen die Nutzer keinen Zugriff 
haben.  
Die nächsten Befehle sollten fehlschlagen.

- [EC] Erstellen Sie mit `aclnutzer1` eine neue Datei namens `subfolder2_data5` in den Ordner 
    `subfolder2`.
- [EC] Erstellen Sie mit `aclnutzer2` eine neue Datei namens `subfolder1_data5` in den Ordner 
    `subfolder1`. 

### Aufräumen

- [EC] Entfernen Sie alle ACL-Einträge der Ordner `folder`, `subfolder1`, `subfolder2` und den 
    jeweils darunterliegenden Dateien mit nur einem Befehl.
- [EC] Nachdem Sie die Rechte entfernt haben, löschen Sie `folder`, `subfolder1`, `subfolder2` und die 
    jeweils darunterliegenden Dateien
- [EC] Löschen Sie die Nutzer `aclnutzer1`, `aclnutzer2` und die Gruppen `aclgroup1`, `aclgroup2`.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[ENDINSTRUCTOR]
