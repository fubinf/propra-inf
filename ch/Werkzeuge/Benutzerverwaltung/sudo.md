title: "Sudo: Kommandos als Superuser ausführen"
stage: beta
timevalue: 1.0
difficulty: 2
explains: sudo, su
---

[SECTION::goal::idea]
Ich verstehe sudo, ich kann es anwenden und ich weiß, wie ich sudo-Rechte verteilen kann.
[ENDSECTION]

[SECTION::background::default]
"sudo" steht für "substitute user and do".
Sudo ist der Befehl, um dem Nutzer Administratorrechte zu geben. 
Mit diesen Rechten darf man auf einem Unixsystem so ziemlich alles tun.

Achtung: Das fühlt sich anfangs natürlich cool an, ist aber auch fürchterlich heikel,
denn man kann dabei leicht etwas versehentlich kaputt machen.
Bitte seien Sie bei der Verwendung von `sudo` immer **sehr** vorsichtig.
Wir haben Sie gewarnt...
[ENDSECTION]

[SECTION::instructions::detailed]

### Sudo verstehen und nutzen

Lesen Sie [HREF::https://wiki.ubuntuusers.de/sudo] bis zum (teilweise unsinnigen)
Abschnitt **Installation**.

- [EC] Versuchen Sie die Datei `/etc/shadow` anzuzeigen: `less /etc/shadow`.

Sie können die Datei nicht lesen, weil Ihnen das [TERMREF::Leserecht] für die Datei fehlt. 

- [EC] Setzen Sie nun ein sudo vor Ihren Befehl aus der Aufgabe [EREFC::1].

Durch sudo haben sie zeitweise Administratorrechte für Ihren Nutzer bekommen. 
Das Administratorkonto, auf Unix genannt "root" (also "Wurzel"), hat alle denkbaren
Rechte.
Dadurch haben Sie die Möglichkeit bekommen, die Datei zu lesen.  

Damit Sie `sudo` nutzen können, müssen Sie in der Gruppe `sudo` sein. Um das zu prüfen, muss Ihr 
Nutzername bei der sudo-Gruppe in der Datei /etc/group aufgeführt sein.

- [EC] Suchen Sie in der Datei `/etc/group` nach der sudo Gruppe und Ihrem Nutzernamen:
  `grep sudo /etc/group`.

### Neuen Nutzer erstellen und sudo-Rechte verteilen

- [EC] Erstellen Sie nun einen neuen Benutzer `sudotest`:  
    `sudo adduser sudotest`. (Lassen Sie bei allen Fragen die Felder leer.  
    Wir werden in [PARTREF::Benutzerkonten] genauer auf die Benutzererstellung eingehen.)

Lesen Sie den Glossareintrag [TERMREF::su] und lesen Sie die **Synopsis** und die **Description** der 
su(1) [manpage](https://manpages.debian.org/bookworm/util-linux/su.1.en.html).

- [EC] Melden Sie sich als `sudotest` an.
- [EC] Versuchen Sie mit dem Nutzer sudotest die Datei `/etc/shadow` zu lesen.  
  Sie können die Datei wieder nicht lesen, selbst wenn Sie `sudo` vor den Befehl setzen.  
  Der Nutzer `sudotest` ist nämlich noch nicht in der Gruppe `sudo`. Lassen Sie uns das erledigen.  
- [EC] Wechseln Sie zurück zu Ihrem normalen Nutzer und fügen Sie `sudotest` der Gruppe `sudo` hinzu:  
  `usermod -aG sudo sudotest` (Wir werden auf Gruppen genauer in [PARTREF::Gruppen] eingehen.)
- [EC] Prüfen Sie, ob `sudotest` die Datei `/etc/shadow` lesen kann.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[ENDINSTRUCTOR]