title: SSH Definition
stage: draft
timevalue: 1
difficulty: 1
profiles:
explains:
assumes:
requires:
---
[SECTION::goal::...]

Ich verstehe was SSH (Secure Shell) ist und wie ich mich auf einem entfernten Rechner anmelden kann.
.

[ENDSECTION]
[SECTION::background::default]

Die Sicherung von Daten durch Verschlüsselung ist in vielen Bereichen moderner Systemadministration von größter Bedeutung. Im Gegensatz zu unsicheren Lösungen wie telnet, rlogin oder FTP wurde das Protokoll SSH (Secure Shell) mit Blick auf die Sicherheit entwickelt. Mit Hilfe der Public-Key-Kryptographie authentifiziert es sowohl die Hosts als auch die Benutzer und verschlüsselt den gesamten nachfolgenden Informationsaustausch.

Mit dem Befehl `ssh` bauen Sie eine Fernsitzung mit dem SSH-Server auf. Dazu geben Sie den Benutzer, mit dem Sie sich auf dem entfernten Rechner verbinden, und die IP-Adresse oder den Hostnamen des entfernten Rechners an. Wenn Sie sich zum ersten Mal mit einem entfernten Rechner verbinden, erhalten Sie eine Meldung wie diese:
`The authenticity of host 'IP-Address' can't be established.`

Nachdem sie es mit y bestätigt haben, werden sie nach dem Passwort des entfernten Benutzers gefragt. Bei erfolgreicher Eingabe erhalten Sie eine Warnmeldung und werden dann beim entfertnetn Rechner angemeldet.

Da Sie zum ersten Mal eine Verbindung zum entfernten Server herstellen, kann seine Authentizität nicht anhand einer Datenbank überprüft werden. Daher stellt der entfernte Server seinen `key fingerprint` seines öffentlichen Schlüssel zur Verfügung. Sobald sie die Verbindung akzeptieren wird der öffentliche Schlüssel des entfernten Servers der Datenbank `known hosts` hinzugefügt, was die Authentifizierung des Server für zukunftige Verbindungen ermöglicht. Diese Liste der öffentlichen Schlüssel von `known hosts` wird in der Datei `knwon_hosts` gespeichert, die sich in `~/.ssh` befindet.

Sowohl `.ssh` als auch `known_hosts` wurden nach dem Aufbau der ersten Fernverbindung angelegt. `~/.ssh` ist das Standardverzeichnis für benutzerspezifische Konfigurations- und Authentifizierungsinformationen.

Wenn sie auf dem lokalen und dem entfernten Rechner denselben Benutzer verwenden, brauchen Sie den Benutzernamen beim Aufbau der SSH-Verbindung nicht anzugeben.

Mit `ssh` können Sie auch nur einen einzigen Befehl auf dem entfernten Rechner ausführen und dann zu Ihrem lokalen Terminal zurückkehren. (`ssh andorra.imp.fu-berlin.de ls ~/`)

[ENDSECTION]
[SECTION::instructions::...]

### Prüfen ob SSH installiert ist

Prüfen Sie auf Ihrem System oder Ihrer WSL-Umgebung mit dem Befehl `dpkg -l | grep openssh-client`, ob der openssh-client auf Ihrem System installiert ist. Falls das der Fall ist, können Sie direkt zu den Aufgaben springen.

Ist der openssh-client nicht auf Ihrem System installiert, holen Sie das mit diesen zwei Befehlen nach.
`sudo apt-get update`
`sudo apt install openssh-client`
Wenn Sie gefragt werden, ob Sie es installieren möchten, bestätigen Sie es mit einem y.

### Auf Andorra verbinden

Verbinden Sie sich per SSH auf `andorra.imp.fu-berlin.de`.

### Befehl auf Andorra ausführen

Geben Sie genau einen Befehl an, um auf `andorra.imp.fu-berlin.de` den Inhalt von `~.ssh/` Ihres Benutzers lokal auf Ihrem Terminal aufzulisten.


[WARNING]
[ENDWARNING]
[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::...]

Geben Sie eine .md Datei ab, in der die Befehle der letzten beiden Aufgaben entahlten sind.

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
