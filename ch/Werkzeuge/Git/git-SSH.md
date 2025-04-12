title: Git nutzen mit SSH
stage: alpha
timevalue: 0.1
difficulty: 1
requires: ssh
---

[SECTION::goal::product]

Ich lerne, wie ich mich mithilfe von SSH mit dem Git-Server authentifiziere und die Remote-URL 
meines Git-Repositories so ändere, dass beim Pushen und Pullen Git anstelle von HTTPS verwendet 
wird.

[ENDSECTION]

[SECTION::background::default]

Im Laufe des ProPra sollte man bereits einige Male seine Abgaben mit Git gepusht haben und dabei 
festgestellt haben, dass es ziemlich nervig ist, jedes Mal sein Passwort neu eingeben zu müssen.
Glücklicherweise gibt es mit SSH eine Möglichkeit, sich sicher und dauerhaft mit dem Git-Server 
zu authentifizieren. Wie das funktioniert, lernen wir hier.

[ENDSECTION]

[SECTION::instructions::detailed]

Wie wir unseren SSH-Schlüssel generieren und finden, haben wir bereits in [PARTREF::ssh] gelernt.
Daher überspringen wir diesen Schritt und gehen direkt ins Detail.

Zunächst müssen wir unseren Schlüssel dem Git-Server hinzufügen. Das Verfahren ist zwar bei den 
meisten Anbietern ähnlich, unterscheidet sich jedoch in Details.

In unserem ProPra arbeiten wir mit GitLab. Die Schritte, wie man den SSH-Key zum GitLab-Account 
hinzufügt, finden Sie [in der GitLab Dokumentation](https://docs.gitlab.com/ee/user/ssh.html#
add-an-ssh-key-to-your-gitlab-account).

Für andere Anbieter wie GitHub lohnt sich bei Bedarf ebenfalls ein Blick in die jeweilige 
Dokumentation.

- [EC] Fügen Sie Ihren öffentlichen SSH-Key zu Ihrem FU-GitLab-Account hinzu und testen Sie, ob 
Sie sich erfolgreich mit dem FU-GitLab Server verbinden können.

Anschließend müssen wir die Remote-URL des lokalen Git-Repositories aktualisieren, da diese 
derzeit noch versucht, sich per HTTPS zu authentifizieren. Dazu ersetzen wir die bestehende 
Remote-URL durch die Git-URL, die in der Projektansicht von GitLab angegeben ist.

- [EC] Ersetzen Sie mit dem entsprechenden Git-Befehl die HTTPS remote-URL Ihres lokalen 
Repositories 
durch die richtige Git-URL.
- [EC] Testen Sie, ob die Remote-URL korrekt gesetzt und die Verbindung nun über SSH hergestellt 
wird.

Wenn alle vorherigen Schritte korrekt ausgeführt wurden, sollten Sie jetzt in der Lage sein, 
Änderungen in Ihrem ProPra-Repo zu pushen und zu pullen, ohne jedes Mal Ihr Account-Passwort 
eingeben zu müssen.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Markdowndokument]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
