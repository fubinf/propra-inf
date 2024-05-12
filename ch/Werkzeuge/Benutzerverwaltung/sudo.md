title: Sudo
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe sudo, ich kann es anwenden und ich weiß, wie ich sudo-Rechte verteilen kann.
[ENDSECTION]

[SECTION::background::default]
Sudo ist der Befehl, um dem Nutzer Administratorrechte zu geben. Man sollte mit Vorsicht mit `sudo` umgehen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Sudo verstehen und nutzen

Lesen Sie den Glossareinträge [TERMREF::sudo].  
Lesen Sie den [Beitrag](https://wiki.ubuntuusers.de/sudo/) über sudo von ubuntuusers bis zum 
Abschnitt **Installation**.

- [EC] Versuchen Sie die Datei `/etc/shadow` mit einem beliebigen Editor zu lesen.

Sie können die Datei nicht lesen. Der Nutzer und die Gruppe der Datei gehören zu `root` und Sie 
haben keine Leserechte für die Datei. 

- [EC] Setzen Sie nun ein sudo vor Ihren Befehl aus der Aufgabe [EREFC::1].

Durch sudo haben sie zeitweise Administratorrechte für Ihren Nutzer bekommen. Somit haben Sie die 
Möglichkeit bekommen, die Datei zu lesen.  

Damit Sie sudo nutzen können, müssen Sie in der sudo Gruppe sein. Um das zu prüfen, muss Ihr 
Nutzername hinter der sudo-Gruppe in der Datei /etc/group vorhanden sein.

- [EC] Suchen Sie in der Datei `/etc/group` nach der sudo Gruppe und Ihrem Nutzernamen.

### Neuen Nutzer erstellen und sudo-Rechte verteilen

- [EC] Erstellen Sie nun einen neuen Benutzer `sudotest`:  

    `sudo adduser sudotest`.  
    Lassen sie bei allen Fragen die Felder leer.  
    (Wir werden mehr auf die Nutzererstellung in [PARTREF::Nutzer] eingehen.)

Lesen Sie den Glossareintrag [TERMREF::su] und lesen Sie die **Synopsis** und die **Description** der 
su(1) [manpage](https://manpages.debian.org/bookworm/util-linux/su.1.en.html).

- [EC] Melden Sie sich als `sudotest` an.
- [EC] Versuchen Sie mit dem Nutzer sudotest die Datei `/etc/shadow` zu lesen.

    Sie können die Datei immer noch nicht lesen, auch wenn Sie `sudo` vor den Befehl setzen.  
    Der Nutzer ist nämlich noch nicht in der Gruppe `sudo`. Lassen Sie uns das erledigen.  

- [EC] Wechseln Sie zurück zu Ihrem Nutzer und fügen Sie `sudotest` der Gruppe `sudo` hinzu:

    `usermod -aG sudo sudotest`  

    (Wir werden mehr auf die Gruppen in [PARTREF::Gruppen] eingehen.)

- [EC] Prüfen Sie, ob `sudotest` die Datei `/etc/shadow` lesen kann.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]