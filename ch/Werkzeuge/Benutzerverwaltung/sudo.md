title: Sudo
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Nutzer
---

[SECTION::goal::idea]
Ich verstehe sudo, ich kann es anwenden und ich weiß, wie ich sudo-Rechte verteilen kann.
[ENDSECTION]

[SECTION::background::default]
Sudo ist der Befehl, um dem Nutzer Adminrechte zu erteilen. Somit sollte man mit Vorsicht damit umgehen.
[ENDSECTION]

[SECTION::instructions::detailed]

Lesen Sie sich die Glossareinträge [TERMREF::sudo] und [TERMREF::su] durch.

### Sudo verstehen und nutzen

Versuchen sie /etc/shadow zu öffnen

- [EC] Öffnen Sie `/etc/shadow` mit einem beliebigen Editor.

Wie Sie sehen, können Sie die Datei nicht öffnen, da der Nutzer und die Gruppe der Datei zu `root` gehören.

- [EC] Prüfen Sie obige Aussage nach.
- [EC] Setzen sie ein sudo vor Ihren Befehl aus der Aufgabe [EREFC::1].

Durch sudo haben sie zeitweise Administratorrechte für Ihren Nutzer bekommen, somit können Sie jetzt auch 
die Datei öffnen und schreiben.  
Sie haben Adminrechte, weil Ihr Nutzer in der Gruppe sudo vorhanden ist.

- [EC] Öffnen Sie die Datei `/etc/group` und prüfen Sie obige Aussage.

### Neuen Nutzer erstellen und sudo-Rechte verteilen

- [EC] Erstellen Sie nun einen neuen Benutzer `sudotest`.
- [EC] Melden Sie sich als `sudotest` an.
- [EC] Nun versuchen Sie wieder `/etc/shadow` zu öffnen.
- [EC] Wechseln Sie zurück zu Ihrem Nutzer und fügen Sie `sudotest` der Gruppe `sudo` hinzu.
- [EC] Prüfen sie jetzt, ob `sudotest` die Datei `/etc/shadow` lesen kann.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]
