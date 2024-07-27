title: Access Control Lists
stage: alpha
timevalue: 1.5
difficulty: 2
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

Stellen Sie sich vor, Sie arbeiten in einer Firma mit zwei Geschäftsführern und einer Abteilung 
Rechnungswesen. Die Geschäftsführer und die Abteilung Rechnungswesen haben im System jeweils ihre 
eigene Rechtegruppe. Des Weiteren hat das Rechnungswesen einen Ordner, wo sie Rechnungen ablegen. 
Auf diesen Ordner hat die Geschäftsführung keinen Zugriff, möchte diesen jetzt aber haben, da sie 
auch Rechnungen in diesem Ordner ablegen möchten, um Umwege per Mail zu vermeiden.

Es gibt eine Gruppe Rechnungswesen, die `rwx`-Rechte auf den Rechnungsordner hat. Des Weiteren hat 
`other` die Rechte `---`. Die Geschäftsführer haben eine eigene Gruppe Geschäftsführer. Würde man 
jetzt die Gruppe auf Geschäftsführer ändern, würde die Abteilung Rechnungswesen keinen Zugriff mehr 
auf den Ordner haben. Hier helfen uns jetzt die ACLs.

### ACL installieren

- [EC] Aktualisieren Sie ihr System.
- [EC] Installieren Sie das Paket `acl`.

### Testumgebung erstellen

- [EC] Erstellen Sie die Nutzer `gf1`, `gf2`, `rw1`, `rw2`.
- [EC] Erstellen Sie zwei Gruppen `geschaeftsfuerer` und `rechnungswesen`.
- [EC] Fügen Sie die Nutzer `gf1`, `gf2` zur Gruppe `geschaeftsfuerer` und `rw1`, `rw2` zur Gruppe 
   `rechnungswesen`.

Erstellen Sie die nächsten Ordner und Dateien mit Ihrem persönlichen Nutzer, nicht mit `aclnutzer1` 
oder `aclnutzer2`.

- [EC] Erstellen Sie den Ordner `/tmp/rechnungen/`
- [EC] Ändern Sie den Nutzer und die Gruppe des Ordners `/tmp/rechnungen` zu ihrem persönlichen 
    Nutzerkonto und die dazugehörige Grupppe.
- [EC] Erstellen Sie den Ordner `/tmp/rechnungen/2023/`.
- [EC] Erstellen Sie den Ordner `/tmp/rechnungen/2024/`.
- [EC] Erstellen Sie die Dateien `rechnung20230101`, `rechnung20230201` in `/tmp/rechnungen/2024/`.
- [EC] Erstellen Sie die Dateien `rechnung20240101`, `rechnung20240201` in `/tmp/rechnungen/2023/`.
- [EC] Ändern Sie die Rechte von den erstellten Ordnern, Subordnern und Dateien so ab, dass Ihr 
    persönliches Nutzerkonto und die gleichnamige Gruppe Lese-, Schreib- und Ausführrechte hat,
    und das `other` keine Rechte haben.

Die gerade erstellten Nutzer sollen erstmal keine Rechte auf die Daten haben.

### Überblick verschaffen

Lesen Sie die [getfacl(1) manpage](https://linux.die.net/man/1/getfacl) bis einschließlich 
**Permissions**.

- [EC] Geben Sie die ACLs von `/tmp/rechnungen/` aus.

Sie haben gerade die normalen Unix-Rechte im [TERMREF::ACL] Format gesehen.  
Setzen wir ein paar ACLs.

### ACLs setzen

Lesen Sie die [setfacl(1) manpage](https://linux.die.net/man/1/setfacl) bis einschließlich 
**Permissions**, die Optionen **-m, -R, -b, -k**, die **Examples** und die **ACL Entries**.

- [EC] Ändern Sie die Gruppe zu `rechnungswesen` für den Ordner `/tmp/rechnungen/` und allen 
   Subordnern und Rechnungen.
- [EC] Fügen Sie per ACL die Gruppe `geschäftsführung` dem Ordner `/tmp/rechnungen/` mit den Rechten `r-x` hinzu.
- [EC] Fügen Sie per ACL die Gruppe `geschäftsführung` dem Ordner `/tmp/rechnungen/2024` mit den Rechten `rwx` hinzu.

### Testen

- [EC] Geben Sie ACLs von `/tmp/rechnungen/` aus.
- [EC] Geben Sie ACLs von `/tmp/rechnungen/2023` aus.
- [EC] Geben Sie ACLs von `/tmp/rechnungen/2024` aus.

Wenn alles richtig verlaufen ist, dann sollte die Geschäftsführung jetzt Zugriff auf die Rechnungen 
aus 2024 haben, aber nicht aus 2023.

- [EC] Melden Sie sich als `gf1` an.
- [EC] Erstellen Sie eine neue Rechnung `rechnung20240301` im Ordner `/tmp/rechnungen/2024/`.
- [EC] Versuchen Sie die Rechnung `/tmp/rechnungen/2024/rechnung20240101` zu lesen.
- [EC] Versuchen Sie den Ordner `/tmp/rechnungen/2023` mit dem Nutzer `gf1` zu öffnen.

Wie sie sehen fehlt der Geschäftsführung die Berechtigung um die Rechnungen aus 2023 zu lesen. 
Das ist so gewollt. Aber die Geschäftsführung kann die Rechnungen aus 2024 nicht lesen. Das müssen 
wir ändern.

- [EC] Melden Sie sich als `gf1` ab

### Rekursiv ACL setzen und testen

- [EC] Fügen Sie rekursiv per ACL die Gruppe `geschäftsführung` dem Ordner `/tmp/rechnungen/2024` 
   mit den Rechten `rwx` hinzu.
- [EC] Fügen Sie der Rechnung `/tmp/rechnungen/2024/rechnung20240101` den Text `gf1 hat das bearbeitet` hinzu.
- [EC] Geben Sie ACLs von `/tmp/rechnungen/2024` aus.

Somit hat jetzt die Geschäftsführung vollen Zugriff auf den Rechnungsordner 2024.

### Aufräumen

Nachdem wir das jetzt alles getestet haben müssen wir auch wieder aufräumen.

- [EC] Entfernen Sie alle ACL-Einträge der Ordner `/tmp/rechnungen/`, `/tmp/rechnungen/2023/`, 
   `/tmp/rechnungen/2024/` und den jeweils darunterliegenden Dateien mit nur einem Befehl.

### Löschen

- [EC] Nachdem Sie die Rechte entfernt haben, löschen Sie `/tmp/rechnungen/`, `/tmp/rechnungen/2023/`, 
   `/tmp/rechnungen/2024/` und die jeweils darunterliegenden Dateien.
- [EC] Löschen Sie die Nutzer `gf1`, `gf2`, `rw1`, `rw2` und die Gruppen `geschaeftsfuerer`, 
   `rechnungswesen`.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
