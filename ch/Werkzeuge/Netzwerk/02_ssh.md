title: Schlüsselpaar erstellen
stage: draft
timevalue: 1.0
difficulty: 1
profiles:
explains:
assumes:
requires:
---
[SECTION::goal::...]

Ich verstehe wie ich ein Schlüsselpaar erstelle und wie ich dieses nutze um mich per SSH auf einem entfernten Rechner anmelde.
.

[ENDSECTION]
[SECTION::background::default]

Sie können Ihren SSH-Client so einrichten, dass er bei der Anmeldung keine Passwörter, sondern stattdessen öffentliche Schlüssel verwendet. Dies ist die bevorzugte Methode, da es wesentlich sicherer ist, sich über SSH mit einem entfernten Server zu verbinden. Dafür ist zunächst ein Schlüsselpaar auf dem Client-Rechner zu erstellen, und zwar mit `ssh-keygen` und der Option `-t`, die den gewünschten Verschlüsselungstyp angibt. Es folgen Fragen nach dem Pfad, in dem das Schlüsselpaar gespeichert werden soll (`~/.ssh/` ist praktisch und auch der Standardspeicherort), und nach einer Passphrase. Diese ist zwar optional, wird aber dringend empfohlen.

`ssh-keygen -t ecdsa`

Mit der Option `-b` beim Erzeugen des Schlüsselpaares mit `ssh-keygen` geben Sie die Schlüsselgröße in Bits an. (zum Beispiel ssh-keygen -t ecdsa -b 521)

id_ecdsa
 Privater Schlüssel

id_ecdsa.pub
 Öffentlicher Schlüssel

Nun fügen Sie ihren öffentlichen Schlüssel zu Datei `~/.ssh/authorized_keys` des Benutzers hinzu, mit dem Sie sich auf dem entfernten Rechner anmelden wollen - wenn das Verzeichnis `~/.shh` noch nicht existiert, erstellen Sie es zunächst. Es gibt verschiedene Methoden, Ihren öffentlichen Schlüssel auf den entfernten Server zu kopieren: mit einem USB-Stick, mit dem Befehl `scp` (wird später noch behandelt) oder indem sie den Befehl `ssh-copy-id` wie folgt nutzen:
`ssh-copy-id -i /home/user/.ssh/id_ecdsa.pub user@host`

Sobald Ihr öffentlicher Schlüssel der Datei `authorized_keys` auf dem entfernten Host hinzugefügt wurde, werden Sie ab jetzt mit dem Schlüssel auf dem entfernten Rechner verbunden.

[ENDSECTION]
[SECTION::instructions::...]

### Schlüsselpaar erstellen

Erstellen Sie auf Ihrem Client-Rechner ein Schlüsselpaar `ed25519` mit 256 Bit und einem Passwort ihrer Wahl.

### Zweites Schlüsselpaar erstellen

Erstellen Sie auf Ihrem Client-Rechner ein Schlüsselpaar `RSA` mit 4096 Bit und einem Passwort ihrer Wahl.

### Kopieren der Schlüssel und Anmelden auf dem entfernten Rechner

Kopieren Sie Ihren öffentlichen `ed25519` Schlüssel auf `andorra.imp.fu-berlin.de` und verbinden Sie sich daraufhin auf den entfernten Rechner.
Schildern Sie in 1-2 kurzen Sätzen, was sich verändert hat.

[WARNING]
[ENDWARNING]
[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::...]

Geben Sie eine .md Datei ab, in der alle Befehle und Schilderungen enthalten sind.
.

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
