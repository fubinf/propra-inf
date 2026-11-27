title: "Sudo: Kommandos als Superuser ausführen"
stage: beta
timevalue: 1.0
difficulty: 2
explains: sudo, su
assumes: redirect
---

[SECTION::goal::idea]
Ich verstehe `sudo`, ich kann es anwenden und ich weiß, wie ich `sudo`-Rechte verteilen kann.
Ich weiß, warum `sudo` beim Umleiten in eine geschützte Datei nicht hilft.
[ENDSECTION]


[SECTION::background::default]
"sudo" steht für "substitute user and do".
`sudo` ist der Befehl, um dem Nutzer Administratorrechte zu geben.
Mit diesen Rechten darf man auf einem Unixsystem so ziemlich alles tun.

Achtung: Das fühlt sich anfangs natürlich cool an, ist aber auch fürchterlich heikel,
denn man kann dabei leicht etwas versehentlich kaputt machen.
Bitte seien Sie bei der Verwendung von `sudo` immer **sehr** vorsichtig.
Wir haben Sie gewarnt...
[ENDSECTION]


[SECTION::instructions::detailed]

[FOLDOUT::Abweichungen unter macOS]
Diese Aufgabe ist nicht für macOS gedacht.
Die Benutzerverwaltung unter macOS weicht zu stark von Linux ab:
Die hier benutzten Kommandos und Dateien gibt es dort teils nicht, teils verhalten sie sich anders.
[ENDFOLDOUT]


### `sudo` verstehen und nutzen

Lesen Sie die Seite
[HREF::https://wiki.ubuntuusers.de/sudo]
bis zum (teilweise unsinnigen) Abschnitt **Installation**.

[EC] Versuchen Sie die Datei `/etc/shadow` anzuzeigen: `cat /etc/shadow`.

Sie können die Datei nicht lesen, weil Ihnen das [TERMREF::Leserecht] für die Datei fehlt.

[EC] Setzen Sie nun ein `sudo` vor Ihren Befehl aus der Aufgabe [EREFC::1].

Durch `sudo` haben Sie zeitweise Administratorrechte für Ihren Nutzer bekommen.
Das Administratorkonto, auf Unix genannt "root" (also "Wurzel"), hat alle denkbaren
Rechte.
Dadurch haben Sie die Möglichkeit bekommen, die Datei zu lesen.

Damit Sie `sudo` nutzen können, müssen Sie in der Gruppe `sudo` sein.
Das ist der Fall, wenn Ihr Nutzername in der Datei `/etc/group`
bei der Gruppe `sudo` aufgeführt ist.

[EC] Suchen Sie in der Datei `/etc/group` nach der Gruppe `sudo` und Ihrem Nutzernamen:
`grep sudo /etc/group`.


### Neuen Nutzer erstellen und `sudo`-Rechte verteilen

[EC] Erstellen Sie nun einen neuen Benutzer `sudotest`:  
`sudo adduser sudotest`.
(Vergeben Sie ein Passwort und lassen Sie bei den übrigen Fragen die Felder leer.  
Wir werden in [PARTREF::Benutzerkonten] genauer auf die Benutzererstellung eingehen.)

Lesen Sie den Glossareintrag [TERMREF::su].
Lesen Sie dann in der
[su(1) manpage](https://manpages.debian.org/stable/util-linux/su.1.en.html)
die Abschnitte **SYNOPSIS** und **DESCRIPTION**.

[EC] Melden Sie sich als `sudotest` an.

Versuchen Sie mit dem Nutzer `sudotest` die Datei `/etc/shadow` zu lesen.  
Sie können die Datei wieder nicht lesen, selbst wenn Sie `sudo` vor den Befehl setzen.  
Der Nutzer `sudotest` ist nämlich noch nicht in der Gruppe `sudo`.
Lassen Sie uns das erledigen.

[EC] Wechseln Sie zurück zu Ihrem normalen Nutzer
und fügen Sie `sudotest` der Gruppe `sudo` hinzu:  
`sudo usermod -aG sudo sudotest`
(Wir werden auf Gruppen genauer in [PARTREF::Gruppen] eingehen.)

[EC] Prüfen Sie, ob `sudotest` die Datei `/etc/shadow` lesen kann.


### Reflexion: Wer schreibt eigentlich?

Arbeiten Sie für diesen Abschnitt wieder als Ihr normaler Nutzer.

[EC] Versuchen Sie, eine Zeile in eine neue Datei unter `/etc` zu schreiben:
`sudo echo "propra" > /etc/propra-sudo-test.txt`

Lesen Sie in der
[bash(1) manpage](https://manpages.debian.org/stable/bash/bash.1.en.html)
den ersten Satz des Abschnitts **REDIRECTION**.

[EQ] Obwohl `sudo` davorsteht, bekommen Sie `Permission denied`.
Welcher Prozess öffnet `/etc/propra-sudo-test.txt` zum Schreiben, und mit wessen Rechten läuft er?

[HINT::Wer öffnet die Datei?]
Wer wertet laut dem gelesenen Satz das `>` aus, und wann?
Mit wessen Rechten läuft Ihre Shell?
[ENDHINT]

[EC] Schreiben Sie die Zeile so in die Datei, dass es klappt.
Benutzen Sie dafür [TERMREF::tee] und `|`.

[HINT::Wie hilft `tee`?]
`tee` öffnet die Datei selbst.
Also muss `tee` mit Root-Rechten laufen, `echo` nicht.
[ENDHINT]

[EC] Prüfen Sie den Inhalt.

Die Datei gehört jetzt `root`, weil `tee` mit Root-Rechten lief und sie angelegt hat.
Lesen dürfen Sie sie trotzdem, denn neue Dateien sind normalerweise für alle lesbar.
Zum Löschen brauchen Sie dagegen wieder `sudo`, weil Ihr Nutzer im Verzeichnis `/etc` nichts entfernen darf.

[EC] Löschen Sie die Datei wieder.
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
[PROT::ALT:sudo.prot]


### Markdowndokument

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
