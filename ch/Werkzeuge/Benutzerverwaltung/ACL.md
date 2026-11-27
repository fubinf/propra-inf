title: Access Control Lists für Dateien
stage: beta
timevalue: 1.5
difficulty: 2
assumes: Gruppen, sudo, Shell-Grundlagen2, Umgang-mit-Verzeichnissen
---

[SECTION::goal::idea]
Ich kann Access-Control-Lists für Dateien und Verzeichnisse einrichten und interpretieren.
Ich weiß, warum eine ACL auf einem Verzeichnis nicht für die Dateien darin gilt.
[ENDSECTION]


[SECTION::background::default]
ACLs (Access Control Lists) sind Listen, die den Zugriff auf Ressourcen regeln
und dabei auch über mehr als einen Benutzer und mehr als eine Gruppe Erlaubnisse oder Sperren
ausdrücken können.
ACLs werden bei Bedarf zusätzlich zu den Unix-Standardberechtigungen gesetzt.
[ENDSECTION]


[SECTION::instructions::detailed]

[FOLDOUT::Abweichungen unter macOS]
Diese Aufgabe ist nicht für macOS gedacht.
Die Benutzerverwaltung unter macOS weicht zu stark von Linux ab:
Die hier benutzten Kommandos und Dateien gibt es dort teils nicht, teils verhalten sie sich anders.
[ENDFOLDOUT]

Stellen Sie sich vor, Sie arbeiten in einer Firma mit zwei Geschäftsführern und einer Abteilung
Rechnungswesen.
Die Geschäftsführer und die Abteilung Rechnungswesen haben im System jeweils ihre
eigene Rechtegruppe.
Des Weiteren hat das Rechnungswesen ein Verzeichnis, in dem sie Rechnungen ablegen.
Auf dieses Verzeichnis hat die Geschäftsführung keinen Zugriff,
möchte diesen (lesend) jetzt aber haben,
um sich bei Bedarf sofort über den aktuellen Stand informieren zu können.

Es gibt eine Gruppe Rechnungswesen, die `rwx`-Rechte auf das Rechnungsverzeichnis hat.
Des Weiteren hat `other` die Rechte `---`.
Die Geschäftsführer haben eine eigene Gruppe Geschäftsführer.
Würde man jetzt die Gruppe auf Geschäftsführer ändern, würde die Abteilung Rechnungswesen
keinen Zugriff mehr auf das Verzeichnis haben.
Eine zusätzliche Gruppe RechnungswesenUndGeschäftsführer hilft auch nicht,
denn Schreibzugriff sollen und wollen die Geschäftsführer nicht bekommen -- wovon sich
im Geschäftsleben alsbald Ausnahmen einstellen.

Solch eine Situation, wo die normalen Unix-Dateirechte nicht flexibel genug sind,
lässt sich mit ACLs lösen.


### ACL installieren

Aktualisieren Sie Ihr System und installieren Sie das Paket `acl`:
`sudo apt update && sudo apt upgrade -y && sudo apt install acl`


### Testumgebung erstellen

[EC] Erstellen Sie die Nutzer `gf1`, `gf2`, `rewe1`, `rewe2`.

[EC] Erstellen Sie zwei Gruppen `geschaeftsfuehrer` und `rechnungswesen`.

[EC] Fügen Sie die Nutzer `gf1`, `gf2` zur Gruppe `geschaeftsfuehrer` zu und
`rewe1`, `rewe2` zur Gruppe `rechnungswesen`.

[HINT::Schwierig?]
Sie haben sich doch vergewissert, dass Sie über das Vorwissen aus den
als "Assumes" angegebenen Aufgaben verfügen?
[ENDHINT]

Erstellen Sie die nächsten Verzeichnisse und Dateien mit Ihrem persönlichen Nutzer.
Der wird also deren Eigentümer.
Eigentümer und Superuser können ACLs ändern.

[EC] Erstellen Sie die Verzeichnisse `/tmp/rechnungen/`, `/tmp/rechnungen/aktuell/`
und `/tmp/rechnungen/neu/`.

[EC] Erstellen Sie in `/tmp/rechnungen/aktuell/` die Dateien `rechnung1`, `rechnung2`.
(Jede Datei in dieser Aufgabe sollte einen kurzen Text inklusive des Dateinamens enthalten.)

[EC] Erstellen Sie in `/tmp/rechnungen/neu/` die Dateien `rechnung17`, `rechnung18`.

[EC] Ändern Sie die Rechte der erstellten Verzeichnisse, Unterverzeichnisse und Dateien so ab,
dass Ihr persönliches Nutzerkonto und die gleichnamige Gruppe Lese-, Schreib- und Ausführrechte
haben, aber `other` keine Rechte haben.

Die oben frisch erstellten Nutzer sollen erstmal keine Rechte auf die Daten haben.


### Überblick verschaffen

<!-- @LINK_SPEC: status=403 -->
Lesen Sie die
[getfacl(1) manpage](https://linux.die.net/man/1/getfacl)
bis einschließlich **Permissions**.

[EC] Geben Sie die ACLs von `/tmp/rechnungen/` aus.

Sie haben gerade die normalen Unix-Rechte im [TERMREF::ACL]-Format gesehen.  
Setzen wir ein paar ACLs.


### ACLs setzen

<!-- @LINK_SPEC: status=403 -->
Lesen Sie die
[setfacl(1) manpage](https://linux.die.net/man/1/setfacl)
bis einschließlich **Permissions**, die Optionen `-m`, `-R`, `-b`, `-k`,
die **Examples** und die **ACL Entries**.

[EC] Ändern Sie die Gruppe zu `rechnungswesen` für das Verzeichnis `/tmp/rechnungen/`
und alle Unterverzeichnisse und Dateien.

[EC] Fügen Sie per ACL die Gruppe `geschaeftsfuehrer` dem Verzeichnis `/tmp/rechnungen/`
mit den Rechten `r-x` hinzu.

[EC] Fügen Sie per ACL die Gruppe `geschaeftsfuehrer` dem Verzeichnis `/tmp/rechnungen/neu`
mit den Rechten `rwx` hinzu,
denn in diesem Verzeichnis soll die Geschäftsführung auch Schreibrechte haben.


### Testen

[EC] Geben Sie ACLs von `/tmp/rechnungen/` aus.

[EC] Geben Sie ACLs von `/tmp/rechnungen/aktuell` aus.

[EC] Geben Sie ACLs von `/tmp/rechnungen/neu` aus.

Wenn alles richtig verlaufen ist, darf die Geschäftsführung jetzt in `neu` schreiben,
in `aktuell` aber nichts tun.
Das probieren wir nun aus:

[EC] Melden Sie sich als `gf1` an.

[EC] Erstellen Sie eine neue Rechnung `rechnung19` im Verzeichnis `/tmp/rechnungen/neu/`.

[EC] Versuchen Sie die Rechnung `/tmp/rechnungen/neu/rechnung17` zu lesen.

[EC] Versuchen Sie das Verzeichnis `/tmp/rechnungen/aktuell` zu öffnen.

[EQ] `gf1` darf `rechnung19` anlegen, aber `rechnung17` nicht lesen.
Woran liegt das?
Schauen Sie sich dazu die ACL von `neu` an, die Sie oben ausgegeben haben,
und überlegen Sie, wann und mit welchen Rechten `rechnung17` entstanden ist.

Dass `aktuell` gesperrt bleibt, ist so gewollt; dort haben wir keine ACL gesetzt.


### Rekursiv ACL setzen und testen

Mit `-R` setzt `setfacl` eine ACL auch auf alle Dateien unterhalb eines Verzeichnisses.

[EC] Melden Sie sich als `gf1` ab; Sie sind also wieder Sie selbst und können ACLs ändern.

[EC] Fügen Sie rekursiv per ACL die Gruppe `geschaeftsfuehrer`
dem Verzeichnis `/tmp/rechnungen/neu` mit den Rechten `rwx` hinzu.

[EC] Melden Sie sich als `gf1` an.

[EC] Fügen Sie der Rechnung `/tmp/rechnungen/neu/rechnung17` den Text `von gf1 bearbeitet` hinzu.

[EC] Geben Sie ACLs von `/tmp/rechnungen/neu` aus.

Somit hat die Geschäftsführung jetzt vollen Zugriff auf alle Dateien, die in `neu` liegen.
Für Dateien, die erst später dort angelegt werden, gilt das nicht automatisch.
Dafür gibt es Default-ACLs (Option `-d`), die wir hier nicht brauchen.


### Aufräumen

Nachdem wir das jetzt alles getestet haben, üben wir noch das ACL-Aufräumen.

[EC] Melden Sie sich als `gf1` ab.

[EC] Entfernen Sie alle ACL-Einträge der Verzeichnisse `/tmp/rechnungen/`,
`/tmp/rechnungen/aktuell/`, `/tmp/rechnungen/neu/` und der jeweils darunterliegenden Dateien
mit nur einem Befehl.


### Löschen

[EC] Nachdem Sie die Rechte entfernt haben, löschen Sie `/tmp/rechnungen/`,
`/tmp/rechnungen/aktuell/`, `/tmp/rechnungen/neu/` und die jeweils darunterliegenden Dateien
mit nur einem Befehl.

[EC] Löschen Sie die Nutzer `gf1`, `gf2`, `rewe1`, `rewe2` und die Gruppen `geschaeftsfuehrer`,
`rechnungswesen`.
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
[PROT::ALT:ACL.prot]


### Markdowndokument

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
