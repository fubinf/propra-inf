title: SSH
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: Shell-Grundlagen, apt, Manpages
---

TODO_1_condric:

- Wie bei git gilt auch hier, dass wir ein (korrektes, wenn auch vereinfachtes) mentales Modell vermitteln sollten.
- Was symmetrische oder asymmetrische Verschlüsselung ist, dürfen wir voraussetzen
  (nur jeweils Glossareintrag mit Verweis auf passende Quelle), ebenso kryptographische Hashfunktionen.
- Aber was davon an welcher Stelle zum Zug kommt, um SSH abzusichern, sollten sich die Leute
  hier erarbeiten; am besten in der Reihenfolge "erst machen, dann verstehen".
- Im Prinzip leisten die Leseaufträge davon einiges, aber der Detailgrad passt nicht gut
  zum Ziel. Siehe z.B. "Verifying host keys", wo die Konzepte vermischt sind mit sehr technischen
  Einzelheiten. Wir müssen dafür sorgen, dass die Erkenntnis geleitet passiert und wir
  nicht viel mehr Information anbieten als im jeweiligen Schritt nötig ist.
  Wenn die manpage nichts Passendes hat, müssen wir was anderes finden und wenn das nicht klappt,
  es selber erledigen. Müsste aber klappen, denn ssh besprechen auch Unis.
- Das praktische Benutzen läuft parallel.
- Ich sollte also nicht nur lernen: "So loggste dich ein und das ist _irgendwie_ sicher.",
  sondern die Sicherheitseigenschaften (mich authentisieren, Rechner authentisieren, Verkehr
  vertraulich halten) zerlegen und auf die technischen Einzelteile abbilden können
  (Passwort, mein privater Schlüssel, mein öff. Schlüssel, Rechnerschlüssel, dessen Fingerprint,
  symmetr. Sitzungsschlüssel, symmetr. Chipher, assymetr. Verfahren, Signaturverfahren;
  alles nur grob) und das pro Schritt des Prozesses.
- Es liegt für mich nicht auf der Hand, wie die Aufgabe dann aussieht...
- Es liegt aber auf der Hand, dass sie deutlich umfangreicher wird und länger dauern darf.
  Das ist aber eine Stelle, an der in er Praxis enormer Wissensmangel herrscht, der auch immer
  wieder zu Sicherheitslücken führt, z.B. weil Server so konfiguriert sind, dass der Klient
  sie beim Verbindungsaufbau auf uralte und wenig sichere Verfahren herunterhandeln kann.
  Idealerweise würden unsere Leute solcher Sachverhalte gewahr (auch wenn Sie die Einzelheiten,
  was gut und was zu alt ist, gar nicht kennen).
- Was man auch verstehen sollte: Wo liegt und welchen Schutz hat mein Geheimmaterial?
  Passwort nur im Kopf, beim (häufigen!) Eingeben wenig geschützt; 
  privater Schlüssel in verschlüsselter und von Dateirechten geschützter Datei;
  geladener privater Schlüssel (im ssh-Agent) im Hauptspeicher meines Rechners, auch im Standby.
- Gut möglich, dass man einiges von diesem Pensum in eine zweite, fortgeschrittene Aufgabe
  hochdrücken kann.
- Anspruchsvoll!

[SECTION::goal::trial]
Ich kann mich mit SSH (Secure Shell) auf einem entfernten Rechner anmelden und habe mir
ein Schlüsselpaar erstellt und den SSH-Agenten eingerichtet, um das wie ein Profi tun zu können.
[ENDSECTION]

[SECTION::background::default]
Bei der Systemadministration geht es die halbe Zeit um Sicherheit.
Zwei wichtige Themen dafür sind Authentisierung und verschlüsselte Kommunikation.
Das sind Kernkompetenzen von SSH, dem Schweizer Messer unter den Netzwerk-Werkzeugen,
mit dem man sich unbedingt gut auskennen muss.
[ENDSECTION]

[SECTION::instructions::detailed]

<replacement id='SSH-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Prüfen ob SSH installiert ist

- [EC] Stellen Sie sicher, dass der `openssh-client` installiert ist:  
      - `apt list --installed openssh-client`  
   Ist der openssh-client nicht auf Ihrem System installiert, holen Sie das mit diesen zwei 
   Befehlen nach:  
      - `sudo apt update`  
      - `sudo apt -y install openssh-client`  

[NOTICE]
Stellen Sie sicher, dass Sie sich im Netz der Hochschule befinden, nötigenfalls über VPN. 
Unter Umständen kann die Verbindung zum Zielserver sonst nicht hergestellt werden.
[ENDNOTICE]

### Per [TERMREF::SSH] auf einem entferntem Rechner anmelden

Lesen Sie die kurze Beschreibung der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EC] Verbinden Sie sich mit dem Zielserver per ssh.

Wenn Sie sich das erste Mal mit dem Zielserver verbinden, dann werden Sie nach der Authentizität 
des entfernten Rechners gefragt.

Lesen Sie den Abschnitt **Verfying Host Keys** der ssh(1) 
[manpage](https://man.openbsd.org/ssh#VERIFYING_HOST_KEYS).

- [EQ] Was wären mögliche Szenarien, wenn Ihnen das System meldet, dass sich der `host_key` des 
   entfernten Rechners geändert hat. Nennen sie zwei Beispiele. 

Es ist per SSH auch möglich direkt Befehle auf dem entfernten Rechner auszuführen und die Ausgabe 
auf dem eigenen Terminal auszugeben.  

Lesen Sie die kurze Beschreibung der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EC] Geben Sie den Dateistrukturbaum von `/home/username/.ssh` vom Zielserver aus.


### Per [TERMREF::Schlüsselpaar] auf einem entfernten Rechner anmelden

Sie haben sich gerade mit Ihrem Passwort angemeldet. SSH bietet Ihnen die Möglichkeit, sich mit einem 
Schlüsselpaar anzumelden.

Lesen Sie die Optionen **-t**, **-b** und die **Description** der ssh-keygen(1) 
[manpage](https://man.openbsd.org/ssh-keygen.1).

- [EC] Erstellen Sie ein Schlüsselpaar mit dem Verschlüsselungstyp `ed25519`. 
  Setzen Sie ein Passwort für das Schlüsselpaar, das Sie sonst nirgends benutzen, denn Sie werden
  mit diesem Schlüsselpaar nach einiger Zeit enorm vieles abgesichert haben.

Es sollten nun zwei neue Dateien unter `~/.ssh/` vorhanden sein. `ed25519` ist Ihr privater Schlüssel 
und sollte von Ihnen gut aufbewahrt werden. `ed25519.pub` ist Ihr öffentlicher Schlüssel. Diesen 
kopieren wir auf den Zielserver, damit Sie sich damit anmelden können.  

Lesen Sie die ssh-copy-id(1) 
[manpage](https://manpages.debian.org/testing/openssh-client/ssh-copy-id.1.en.html).  
Verstehen Sie insbesondere das example am Ende. 

- [EC] Kopieren Sie Ihren öffentlichen Schlüssel auf den Zielserver.

Der öffentliche Schlüssel sollte jetzt auf dem Zielserver unter ihrem Nutzer gespeichert sein. 

- [EC] Melden Sie sich auf dem Zielserver an. 
- [EQ] Beschreiben Sie kurz was sich geändert hat.

### Nutzen eines SSH-Agenten

Stellen Sie sich vor, Sie sind ein Administrator in einer mittelständischen Firma. Sie 
verwalten 100 virtuelle Maschinen. Auf jeder dieser Maschinen ist ihr öffentlicher SSH-Schlüssel 
hinterlegt. Für die Entschlüsselung haben Sie ein 25-stelliges zufällig generiertes Passwort 
gewählt. Jetzt müssen Sie jedes Mal Ihr langes kompliziertes Passwort neu eingeben, wenn Sie sich 
auf einem der virtuellen Maschinen anmelden wollen. Um das zu umgehen und trotzdem die Sicherheit 
der Schlüssel beizubehalten, gibt es den SSH-Agenten.
  
Lesen sie die Paragraphen am Anfang und am Ende der **Description** der ssh-agent(1) 
[manpage](https://man.openbsd.org/ssh-agent.1).  
Lesen sie die 3 Paragraphen am Anfang der **Description** der ssh-add(1) 
[manpage](https://man.openbsd.org/ssh-add.1).

- [EC] Starten Sie den SSH-Agenten.
- [EC] Fügen Sie Ihren Schlüssel dem Agenten hinzu.  
- [EC] Verbinden Sie sich mit dem Zielserver.
- [EQ] Was hat sich geändert?  

Es ist umständlich den SSH-Agenten jedes mal neu zu starten, wenn man sich angemeldet hat. 
Deswegen erstellen wir uns einen Alias, der das für uns erledigt.

Lesen Sie die **Syntax** und die **Dauerhafte Verwendung** des 
[Beitrags](https://wiki.ubuntuusers.de/alias/) von ubuntuusers über `alias`.

- [EC] Erstellen Sie einen Alias `ssha`, welches den Agenten startet und Ihre Schlüssel in den Agenten 
   kopiert.
- [EC] Fügen Sie den Alias Ihrer `.bashrc` hinzu. Somit ist Ihr Alias nach jeder Anmeldung verfügbar.

Jetzt haben Sie schon eine schnellere Möglichkeit den SSH-Agenten zu starten.  
Es gibt aber eine elegantere Lösung. Man lässt den Agenten beim Anmelden automatisch starten.

Lesen Sie den Abschnitt **Bequem4** von [PARTREF::Shell-Grundlagen] 

- [EC] Modifizieren Sie Ihre `.bashrc` so, dass der SSH-Agent gestartet wird und Ihre Schlüssel 
   hinzugefügt werden.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Erwartung]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]

[ENDINSTRUCTOR]