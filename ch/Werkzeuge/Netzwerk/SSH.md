title: SSH
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: Shell-Grundlagen, apt
---

TODO_1_condric

- Was ist der "erste Abschnitt" der Quelle? Leseauftrag lieber passend zu den Teilaufgaben stückeln.
- K1: Was sollen die Punkte vor den Kommandos?
- K2: Die Leute sollten selbst in der manpage gewisse Sachen nachschlagen.  
  Hier reichen uns Rechnernamen, IPs sind für Fortgeschrittene und dann nicht schwierig.
- Ob Ctrl-D funktioniert, hängt von Shelleinstellungen ab.  
- Der Teil über Authentizität ist vage und kaum verständlich.
  Gute Quelle suchen, eng umgrenzten Leseauftrag geben, Frage dazu stellen.
- Man-in-the-Middle-Angriff ist _nicht_ wahrscheinlich, sondern nur denkbar.
  Und dann mit yes zu antworten wäre absurd.
- K3: Da fehlt der Leseauftrag. Wir sind hier bei "einfach".
- K4: Da fehlt ein Leseauftrag. Schlüsselerzeugung muss konzeptuell (grob) verstanden sein.
- K5: Leseauftrag bitte. Die sind immer so schmal wie möglich, gell?
  Die Manpage von `ssh-copy-id` ist vergleichsweise kurz, aber immer noch viel zu lang für
  ein pauschales "Lies die manpage": Was genau soll ich via manpage rausfinden?
- K7 (auskommentiert): Für meine Begriffe gehört ssh-agent fest zu ssh, denn erst dann
  versteht man, warum das Schlüsselpaar auch praktisch besser ist als ein Passwort.  
  Ich verwende folgende Aliase:  
  `alias ssha='eval ``ssh-agent``; ssh-add'`  
  `alias sshae='echo export SSH_AUTH_SOCK=$SSH_AUTH_SOCK'\'';'\'' export SSH_AGENT_PID=$SSH_AGENT_PID'`  
  Die (oder etwas Ähnliches) sollten sich die Teilnehmenden ins .bashrc eintragen und verstehen,
  was die tun und wie man sie benutzt. Der zweite dient dazu, einen vorhandenen ssh-agent in
  neuen Shells bekannt zu machen, statt immer wieder zusätzliche zu starten.
- Wenn die Aufgabe länger als 2 Stunden wird, ist das OK, 
  aber bislang sind die 2 Stunden sogar weit übertrieben, oder?
- Bitte nicht so lange Zeilen schreiben, sondern auf ca. 100 Zeichen begrenzen. 

[SECTION::goal::idea]
 - Ich verstehe was SSH (Secure Shell) ist und wie ich mich auf einem entfernten Rechner anmelden kann.
 - Ich verstehe wie ich ein Schlüsselpaar erstelle und wie ich diesen nutze und was der Vorteil davon ist.
 - Ich verstehe wie der ssh-agent funktioniert und wie ich diesen nutze.
[ENDSECTION]

[SECTION::background::default]
Die Sicherung von Daten durch Verschlüsselung ist in vielen Bereichen moderner 
Systemadministration von größter Bedeutung. Im Gegensatz zu unsicheren Lösungen wie telnet, 
rlogin oder FTP wurde das Protokoll SSH (Secure Shell) mit Blick auf die Sicherheit entwickelt.
Mit Hilfe der Public-Key-Kryptographie authentifiziert es sowohl die Hosts als auch die Benutzer
und verschlüsselt den gesamten nachfolgenden Informationsaustausch.
[ENDSECTION]

[SECTION::instructions::detailed]

<replacement id='targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Prüfen ob SSH installiert ist

- [EC] Stellen Sie sicher, dass der `openssh-client` installiert ist:  
      - `apt list --installed | grep openssh-client`  
   Ist der openssh-client nicht auf Ihrem System installiert, holen Sie das mit diesen zwei 
   Befehlen nach:  
      - `sudo apt update`  
      - `sudo apt -y install openssh-client`  

[NOTICE]
Stellen Sie sicher, dass Sie sich im Netz der Universität oder im VPN befinden. Unter Umständen 
kann die Verbindung zum Zielserver nicht hergestellt werden.
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

- [EC] Erstellen Sie ein Schlüsselpaar mit dem Verschlüsselungstyp `ed25519`. Setzen Sie ein neues 
Passwort für das Schlüsselpaar.

Es sollten nun zwei neue Dateien unter `~/.ssh/` vorhanden sein. `ed25519` ist Ihr privater Schlüssel 
und sollte von Ihnen gut aufbewahrt werden. `ed25519.pub` ist Ihr öffentlicher Schlüssel. Diesen 
kopieren wir auf den Zielserver, damit Sie sich damit anmelden können.  

Lesen Sie die ssh-copy-id(1) 
[manpage](https://manpages.debian.org/testing/openssh-client/ssh-copy-id.1.en.html).  
Verstehen Sie insbesondere das example was am Ende gegeben ist. 

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

- [EC] Starten Sie den SSH-Agenten.
- [EC] Fügen Sie Ihren Schlüssel dem Agenten hinzu.  
- [EC] Verbinden Sie sich mit dem Zielserver.
- [EQ] Was hat sich geändert?  

Es ist umständlich den SSH-Agenten jedes mal neu zu starten, wenn man sich angemeldet hat. 

Lesen Sie die **Syntax** und die **Dauerhafte Verwendung** des 
[Beitrags](https://wiki.ubuntuusers.de/alias/) von ubuntuusers über `alias`.

- [EC] Erstellen Sie einen Alias `ssha`, welches den Agenten startet und Ihre Schlüssel in den Agenten 
   kopiert.
- [EC] Fügen Sie den Alias Ihrer `.bashrc` hinzu. Somit ist Ihr Alias nach jeder Anmeldung verfügbar.

Jetzt haben Sie schon eine schnellere Möglichkeit den SSH-Agenten zu starten.  
Es gibt aber eine elegantere Lösung. Man lässt den Agenten beim Anmelden automatisch starten.

Lesen Sie den Abschnitt **Bequem4** von [PARTREF::Shell-Grundlagen] 

- [EC] Modifizieren Sie Ihre `.bashrc` so, dass der ssh-agent gestartet wird und Ihre Schlüssel 
   hinzugefügt werden.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Erwartung]

[INCLUDE::../../_include/Instructor-Auseinandersetzung.md]

[ENDINSTRUCTOR]