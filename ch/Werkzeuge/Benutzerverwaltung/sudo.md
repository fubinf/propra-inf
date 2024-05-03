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

Lesen Sie sich die Glossareinträge [TERMREF::sudo] und [TERMREF::su] durch.

### Sudo verstehen und nutzen

Versuchen sie /etc/shadow zu öffnen

- [EC] Öffnen Sie `/etc/shadow` mit einem beliebigen Editor.

Wie Sie sehen, können Sie die Datei nicht öffnen, da der Nutzer und die Gruppe der Datei zu `root` gehören.

- [EC] Prüfen Sie obige Aussage nach.
- [EC] Setzen sie ein sudo vor den Befehl aus der Aufgabe [EREFC::1].

Durch sudo haben sie zeitweise Administratorrechte für Ihren Nutzer bekommen, somit können Sie jetzt auch 
die Datei öffnen und schreiben.  
Sie haben Adminrechte, weil Ihr Nutzer in der Gruppe sudo vorhanden ist.

- [EC] Öffnen Sie die Datei `/etc/group` und bestätigen Sie obige Aussage.

### Neuen Nutzer erstellen und sudo-Rechte verteilen

- [EC] Erstellen Sie nun einen neuen Benutzer `sudotest`:  

    `sudo adduser sudotest`.  
    Lassen sie bei allen Fragen die Felder leer.  
    (Wir werden mehr auf die Nutzererstellung in [PARTREF::Nutzer] eingehen.)

- [EC] Melden Sie sich als `sudotest` an.
- [EC] Nun versuchen Sie wieder `/etc/shadow` zu öffnen.  
    Sie können die Datei immer noch nicht öffnen, auch wenn Sie `sudo` vor den Befehl setzen.  
    Der Nutzer ist nämlich noch nicht in der Gruppe `sudo`. Lassen Sie uns das erledigen.  
- [EC] Wechseln Sie zurück zu Ihrem Nutzer und fügen Sie `sudotest` der Gruppe `sudo` hinzu:

    `usermod -aG sudo sudotest`  

    (Wir werden mehr auf die Gruppen in [PARTREF::Gruppen] eingehen.)

- [EC] Prüfen sie jetzt, ob `sudotest` die Datei `/etc/shadow` lesen kann.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]
