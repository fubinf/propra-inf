title: SSH
stage: alpha
timevalue: 2.0 
difficulty: 2
---
[SECTION::goal::idea]

 - Ich verstehe was SSH (Secure Shell) ist und wie ich mich auf einem entfernten Rechner anmelden kann.
 - Ich verstehe wie ich ein Schlüsselpaar erstelle und wie ich diesen nutze.

[ENDSECTION]

[SECTION::background::default]

Die Sicherung von Daten durch Verschlüsselung ist in vielen Bereichen moderner Systemadministration von größter Bedeutung. Im Gegensatz zu unsicheren Lösungen wie telnet, rlogin oder FTP wurde das Protokoll SSH (Secure Shell) mit Blick auf die Sicherheit entwickelt. Mit Hilfe der Public-Key-Kryptographie authentifiziert es sowohl die Hosts als auch die Benutzer und verschlüsselt den gesamten nachfolgenden Informationsaustausch.

[ENDSECTION]

[SECTION::instructions::detailed]

Lesen Sie den ersten Abschnitt des [Beitrags](https://wiki.ubuntuusers.de/SSH/) von ubuntuusers über SSH durch.

<replacement id='targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Prüfen ob SSH installiert ist

- [EC] Stellen Sie sicher, dass der `openssh-client` installiert ist:  
   . `dpkg -l | grep openssh-client`  
   Ist der openssh-client nicht auf Ihrem System installiert, holen Sie das mit diesen zwei Befehlen nach:  
   . `sudo apt update`  
   . `sudo apt -y install openssh-client`  

[NOTICE]
Stellen Sie sicher, dass Sie sich im Netz der Universität oder im VPN befinden. Unter Umständen kann die Verbindung zum Zielserver nicht hergestellt werden.
[ENDNOTICE]

### Per [TERMREF::SSH] auf einem entferntem Rechner anmelden

- [EC] Im Allgemeinen verbindet man sich mit einem entfernten Rechner per `ssh username@hostname` beziehungsweise mit `ssh username@IP-address` um sich per IP-Adresse anzumelden.  
   Falls Ihr Nutzername auf Ihrem System identisch zu dem Nutzernamen auf dem entfernten Rechner ist, dann können sie `username` auslassen.  
   Dann sieht der Befehl so aus `ssh hostname` beziehungsweise `ssh IP-address` um sich per IP-Adresse anzumelden.  
   Verbinden Sie sich nun mit dem Zielsever: `ssh username@zielserver`  
   Die SSH-Sitzung beenden Sie per `exit` oder auch per Tastaturshortcut `STRG + D`.  
   *Wenn Sie sich das erste Mal mit dem Zielserver verbinden, dann werden Sie nach der Authentizität des entfernten Rechners gefragt.*  
   *Daraufhin wird der öffentliche Schlüssel des Servers auf Ihrem Rechner unter `.ssh/authorized_keys` gespeichert. Nachdem der Schlüssel gespeichert wurde, werden Sie im Normalfall nicht mehr nach der Authentizität gefragt.*  
   *Falls sich die Authentizität des Rechners geändert hat, ist die Wahrscheinlichkeit hoch, dass es ein Man-in-the-Middle-Angriff sein könnte.*
   *Bestätigen Sie die Aufforderung mit `yes`.*

- [EC] Es ist per SSH auch möglich direkt Befehle auf dem entfernten Rechner auszuführen und die Ausgabe auf dem eigenen Terminal auszugeben.  
   Man fügt den auszuführenden Befehl ans Ende des SSH-Befehls an.  
   Geben Sie den Dateistrukturbaum von `/home/username/.ssh` aus.


### Per [TERMREF::Schlüsselpaar] auf einem entfernten Rechner anmelden

- [EC] Sie haben sich gerade mit Ihrem Passwort angemeldet. Es gibt auch die Möglichkeit sich mit einem Schlüsselpaar anzumelden. Durch dieses Schlüsselpaar wird die Sicherheit der Verbindung nochmal stark erhöht.  
   Erstellen Sie ein Schlüsselpaar mit dem Verschlüsselungstyp `ed25519`: `ssh-keygen -t ed25519`  
   Speichern Sie es am Standardspeicherort `~/.ssh/` und geben Sie dem Schlüssel eine Passphrase.

- [EC] Es sollten nun zwei neue Dateien unter `~/.ssh/` vorhanden sein. `ed25519` ist Ihr privater Schlüssel und sollte von Ihnen gut aufbewahrt werden. `ed25519.pub` ist Ihr öffentlicher Schlüssel. Diesen kopieren wir auf den Zielserver, damit Sie sich damit anmelden können.  
   Nutzen Sie den Befehl `ssh-copy-id`.  
   Kopieren Sie Ihren öffentlichen Schlüssel auf den Zielserver.

- [EC] Melden Sie sich jetzt auf den Zielserver an. Beschreiben Sie kurz was sich geändert hat.

<!-- ### Nutzen eines SSH-Agenten

- [EC] Stellen Sie sich mal vor, Sie sind ein Administrator in einer mittelständischen Firma. Sie verwalten 100 virtuelle Maschinen. Auf jeder dieser Maschinen ist ihr SSH-Schlüssel hinterlegt. Für die Entschlüsselung haben Sie ein 25-stelliges zufällig generiertes Passwort gewählt. Jetzt müssen Sie jedes Mal Ihr langes kompliziertes Passwort neu eingeben, wenn Sie sich auf einem der VMs anmelden wollen. Um das zu umgehen und trotzdem die Sicherheit der Schlüssel beizubehalten, gibt es den SSH-Agenten. Mit dem SSH-Agenten müssen Sie ihre Passphrase nur beim Starten des Agenten eingeben und danach übernimmt der Agent das Anmelden auf den virtuellen Maschinen, weil der Agent Ihren Schlüssel zwischenspeichert.  
  
    Starten Sie den SSH-Agenten mit: `ssh-agent /bin/bash`  
    Fügen Sie Ihren Schlüssel dem Agenten hinzu: `ssh-add`  
    Geben Sie Ihre Passphrase ein.  
    Verbinden Sie sich nun ein letztes Mal mit dem Zielserver.   -->

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

