title: Git per SSH nutzen 
stage: beta
timevalue: 0.5
difficulty: 2
requires: ssh
---

[SECTION::goal::product]
Ich lerne, wie ich mich mithilfe von SSH mit dem Git-Server authentifiziere und die Remote-URL 
meines Git-Repositories so ändere, dass beim Pushen und Pullen Git anstelle von HTTPS verwendet 
wird.
[ENDSECTION]

[SECTION::background::default]
Im Laufe des ProPra sollten Sie bereits einige Male Ihre Abgaben mit Git gepusht haben.
Vermutlich fanden Sie es ziemlich nervig, jedes Mal das Passwort neu eingeben zu müssen?
Aber niemand, der sich auskennt, macht das so:
Glücklicherweise gibt es mit SSH eine Möglichkeit, sich auch ohne wiederholte Passworteingabe
sicher beim Git-Server zu authentifizieren. Wie das funktioniert, lernen wir hier.
[ENDSECTION]

[SECTION::instructions::detailed]
Git kann denselben ssh-Schlüssel benutzen, den Sie bei [PARTREF::ssh] angelegt haben.

Wir haben zwei Schritte zu tun:

1. Den eigenen Public-Key auf dem Git-Server hinterlegen.
2. Lokal in unserem git-Repo den `git remote`-URL vom aktuellen `https`-URL
   auf den passenden `ssh`-URL umstellen.
   Der Remote-URL beschreibt, mit welchem Git-Server git bei Kommandos wie
   `push` und `pull` Kontakt aufnimmt.

Das Verfahren ist vor allem für Schritt 1 bei jedem Typ Git-Server leicht verschieden. 
Lesen Sie nach, wie es jeweils geht:

- [bei GitLab](https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account)
- [bei GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)


### Schritt 1

Hinterlegen Sie nun Ihren Schlüssel auf den Server.
Quälen Sie sich nicht lange mit dem `clip`-Kommando, sondern benutzen Sie lieber einfach 
Copy/Paste mit Maus und Tastatur.

[EC] [Prüfen Sie die Verbindung](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)


### Schritt 2

Lesen Sie in der 
[Hilfe von `git remote`](https://git-scm.com/docs/git-remote)
nach wie man

- vorhandene Remote-URLs anzeigt
- zusätzliche remote-URLs zufügt
- existierende remote-URLs ersetzt

[EC] Zeigen Sie Ihren aktuellen https-Remote-URl an.

[EC] Holen Sie sich den ssh-URL vom Git-Server und überschreiben Sie damit den existierenden
https-Remote-URL in Ihrem lokalen Repo.

[EC] Probieren Sie aus, ob die neue Verbindungsart funktioniert.
(Wenn Sie die obigen Erklärungen verstanden haben, ist klar, welche zwei möglichen Kommandos 
dafür infrage kommen.)

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
