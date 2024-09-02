title: Access Control Lists für Dateien
stage: beta
timevalue: 1.5
difficulty: 2
assumes: apt, Gruppen, sudo, Shell-Grundlagen2, Umgang-mit-Verzeichnissen
---

[SECTION::goal::idea]

Kann Access-Control-Lists für Dateien und Verzeichnisse einrichten und interpretieren.

[ENDSECTION]

[SECTION::background::default]

ACLs (Access Control Lists) sind Listen, die den Zugriff auf Ressourcen regeln
und dabei auch über mehr als einen Benutzer und mehr als eine Gruppe Erlaubnisse oder Sperren
ausdrücken können. 
ACLs werden bei Bedarf zusätzlich zu den Unix-Standardberechtigungen gesetzt.

[ENDSECTION]

[SECTION::instructions::detailed]

Stellen Sie sich vor, Sie arbeiten in einer Firma mit zwei Geschäftsführern und einer Abteilung 
Rechnungswesen. 
Die Geschäftsführer und die Abteilung Rechnungswesen haben im System jeweils ihre 
eigene Rechtegruppe. 
Des Weiteren hat das Rechnungswesen einen Ordner, wo sie Rechnungen ablegen. 
Auf diesen Ordner hat die Geschäftsführung keinen Zugriff, möchte diesen (lesend) jetzt aber haben, 
um sich bei Bedarf sofort über den aktuellen Stand informieren zu können. 

Es gibt eine Gruppe Rechnungswesen, die `rwx`-Rechte auf den Rechnungsordner hat. 
Des Weiteren hat `other` die Rechte `---`. 
Die Geschäftsführer haben eine eigene Gruppe Geschäftsführer. 
Würde man jetzt die Gruppe auf Geschäftsführer ändern, würde die Abteilung Rechnungswesen 
keinen Zugriff mehr auf den Ordner haben.
Eine zusätzliche Gruppe RechnungswesenUndGeschäftsführer hilft auch nicht,
denn Schreibzugriff sollen und wollen die Geschäftsführer nicht bekommen -- wovon sich
im Geschäftsleben alsbald Ausnahmen einstellen.

Solch eine Situation, wo die normalen Unix-Dateirechte nicht flexibel genug sind,
lässt sich mit ACLs lösen.


### ACL installieren

- [EC] Aktualisieren Sie ihr System.
- [EC] Installieren Sie das Paket `acl`.


### Testumgebung erstellen

- [EC] Erstellen Sie die Nutzer `gf1`, `gf2`, `rewe1`, `rewe2`.
- [EC] Erstellen Sie zwei Gruppen `geschaeftsfuehrer` und `rechnungswesen`.
- [EC] Fügen Sie die Nutzer `gf1`, `gf2` zur Gruppe `geschaeftsfuehrer` zu und 
  `rewe1`, `rewe2` zur Gruppe `rechnungswesen`.

[HINT::Schwierig?]
Sie haben sich doch vergewissert, dass Sie über das Vorwissen aus den
als "Assumes" angegebenen Aufgaben verfügen?
[ENDHINT]

Erstellen Sie die nächsten Ordner und Dateien mit Ihrem persönlichen Nutzer.
Der wird also deren Eigentümer.
Eigentümer und Superuser können ACLs ändern.

- [EC] Erstellen Sie die Ordner `/tmp/rechnungen/`, `/tmp/rechnungen/aktuell/`, `/tmp/rechnungen/neu/`.
- [EC] Erstellen Sie in `/tmp/rechnungen/aktuell/` die Dateien `rechnung1`, `rechnung2`.
  (Jede Datei in dieser Aufgabe sollte einen kurzen Text inklusive des Dateinamens enthalten.)
- [EC] Erstellen Sie in `/tmp/rechnungen/neu/` die Dateien `rechnung17`, `rechnung18`.
- [EC] Ändern Sie die Rechte von den erstellten Ordnern, Subordnern und Dateien so ab, dass Ihr 
    persönliches Nutzerkonto und die gleichnamige Gruppe Lese-, Schreib- und Ausführrechte haben,
    aber `other` keine Rechte haben.

Die oben frisch erstellten Nutzer sollen erstmal keine Rechte auf die Daten haben.


### Überblick verschaffen

Lesen Sie die [getfacl(1) manpage](https://linux.die.net/man/1/getfacl) bis einschließlich 
**Permissions**.

- [EC] Geben Sie die ACLs von `/tmp/rechnungen/` aus.

Sie haben gerade die normalen Unix-Rechte im [TERMREF::ACL] Format gesehen.  
Setzen wir ein paar ACLs.


### ACLs setzen

Lesen Sie die [setfacl(1) manpage](https://linux.die.net/man/1/setfacl) bis einschließlich 
**Permissions**, die Optionen **-m, -R, -b, -k**, die **Examples** und die **ACL Entries**.

- [EC] Ändern Sie die Gruppe zu `rechnungswesen` für den Ordner `/tmp/rechnungen/` und alle 
   Unterordner und Dateien.
- [EC] Fügen Sie per ACL die Gruppe `geschaeftsfuehrer` dem Ordner `/tmp/rechnungen/` 
  mit den Rechten `r-x` hinzu.
- [EC] Fügen Sie per ACL die Gruppe `geschaeftsfuehrer` dem Ordner `/tmp/rechnungen/neu` 
  mit den Rechten `rwx` hinzu,
  denn in diesem Verzeichnis soll die Geschäftsführung auch Schreibrechte haben.


### Testen

- [EC] Geben Sie ACLs von `/tmp/rechnungen/` aus.
- [EC] Geben Sie ACLs von `/tmp/rechnungen/aktuell` aus.
- [EC] Geben Sie ACLs von `/tmp/rechnungen/neu` aus.

Wenn alles richtig verlaufen ist, dann sollte die Geschäftsführung jetzt Zugriff auf die Rechnungen 
in `neu` haben, aber nicht auf die in `aktuell`.
Das probieren wir nun aus:

- [EC] Melden Sie sich als `gf1` an.
- [EC] Erstellen Sie eine neue Rechnung `rechnung19` im Ordner `/tmp/rechnungen/neu/`.
- [EC] Versuchen Sie die Rechnung `/tmp/rechnungen/neu/rechnung17` zu lesen.
- [EC] Versuchen Sie den Ordner `/tmp/rechnungen/aktuell` zu öffnen.

Wie sie sehen, fehlt der Geschäftsführung die Berechtigung um die Rechnungen in `aktuell` zu lesen. 
Das müssen wir noch ändern.


### Rekursiv ACL setzen und testen

- [EC] Melden Sie sich als `gf1` ab; Sie sind also wieder Sie selbst und können ACLs ändern.
- [EC] Fügen Sie rekursiv per ACL die Gruppe `geschäftsführung` dem Ordner `/tmp/rechnungen/neu` 
   mit den Rechten `rwx` hinzu.
- [EC] Melden Sie sich als `gf1` an.
- [EC] Fügen Sie der Rechnung `/tmp/rechnungen/neu/rechnung17` den Text `von gf1 bearbeitet` hinzu.
- [EC] Geben Sie ACLs von `/tmp/rechnungen/neu` aus.

Somit hat jetzt die Geschäftsführung vollen Zugriff auf `neu`.


### Aufräumen

Nachdem wir das jetzt alles getestet haben, üben wir noch das ACL-Aufräumen.

- [EC] Melden Sie sich als `gf1` ab.
- [EC] Entfernen Sie alle ACL-Einträge der Ordner `/tmp/rechnungen/`, `/tmp/rechnungen/aktuell/`, 
   `/tmp/rechnungen/neu/` und der jeweils darunterliegenden Dateien mit nur einem Befehl.


### Löschen

- [EC] Nachdem Sie die Rechte entfernt haben, löschen Sie `/tmp/rechnungen/`, `/tmp/rechnungen/aktuell/`, 
   `/tmp/rechnungen/neu/` und die jeweils darunterliegenden Dateien mit nur einem Befehl.
- [EC] Löschen Sie die Nutzer `gf1`, `gf2`, `rewe1`, `rewe2` und die Gruppen `geschaeftsfuehrer`, 
   `rechnungswesen`.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kommandprotokoll]
[PROT::ALT:ACL.prot] 
[ENDINSTRUCTOR]
