title: SSH
stage: beta
timevalue: 1.5
difficulty: 2
---

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
<replacement id='ssh-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>


### Secure Shell installieren

[EC] Aktualisieren Sie Ihr System

[EC] Installieren Sie das Paket `openssh-client`

[NOTICE]
Stellen Sie sicher, dass Sie sich im Netz der Hochschule befinden, nötigenfalls über VPN. 
Unter Umständen kann die Verbindung zum Zielserver sonst nicht hergestellt werden.
[ENDNOTICE]

[NOTICE]
Um SSH-Sitzungen zu beenden, geben Sie den Befehl `exit` ein.
[ENDNOTICE]

### Per [TERMREF::SSH] auf einem entferntem Rechner anmelden

Secure Shell oder auch Secure Socket Shell (SSH) ist ein sicheres Verfahren um sich mit Rechnern 
zu verbinden.
Damit die Verbindung sicher ist, brauchen wir Verfahren, die das absichern.
Das erste Verfahren ist die [TERMREF::Symmetrische Verschlüsselung].
Bei diesem Verfahren wird ein geheimer Schlüssel zwischen zwei Instanzen ausgetauscht, um die per 
SSH gesendeten Daten zu ver- und entschlüsseln.

Lesen Sie ab dem Abschnitt **How Does SSH Work** bis einschließlich dem Abschnitt **Symmetric Encryption** von 
[HREF::https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work].

[EC] Verbinden Sie sich per `ssh` mit dem Zielserver.

Wenn Sie sich das erste Mal mit dem Zielserver verbinden, dann werden Sie nach der Authentizität 
des entfernten Rechners gefragt. Hier wurden sogenannte `host_keys` zwischen beiden Instanzen ausgetauscht.
Diese `host_keys` sind ein Teil der symmetrischen Verschlüsselung für SSH.

Lesen Sie den Abschnitt **Session Encryption Negotiation** von 
[HREF::https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work].

Lesen Sie den Abschnitt **SSH Host Fingerprint** bis einschließlich **Warnung bei geänderten Fingerprints**
von [HREF::https://wiki.ubuntuusers.de/SSH/].

[EQ] Was wären mögliche Gründe, wenn Ihnen das System meldet, dass sich der `host_key` des 
entfernten Rechners geändert hat? Nennen Sie zwei Beispiele.

[EC] Schließen Sie ihre SSH-Sitzung.


### Per [TERMREF::Schlüsselpaar] auf einem entfernten Rechner anmelden

Sie haben sich vorhin mit Ihrem Passwort angemeldet. 
Dabei wurde zum Übermitteln des Passworts an den Server eine symmetrische Verschlüsselung benutzt.
Jetzt werden wir uns mit einem asymmetrischen Verfahren auf dem Zielserver anmelden,
sodass der Server den privaten Schlüssel nie erfahren muss.
Dafür müssen wir und erstmal ein Schlüsselpaar erstellen, dieses mit einem Passwort schützen und 
dann den öffentlichen Schlüssel auf den Server kopieren.

Lesen Sie den Abschnitt **Asymmetric Encryption** von 
[HREF::https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work].

Lesen Sie die Optionen **-t**, **-b** und die **Description** der ssh-keygen(1) 
[manpage](https://man.openbsd.org/ssh-keygen.1).

Wir verwenden in diesem Beispiel den Verschlüsselungstyp ed25519, welcher hochsichere und relativ 
kleine Schlüssel erstellt. ed25519 basiert auf elliptischen Kurven und bietet im Vergleich zu 
klassischen Verfahren wie RSA eine kompaktere und effizientere Lösung bei ähnlichem 
Sicherheitsniveau. Ein weiterer wichtiger Verschlüsselungstyp ist RSA mit einer Schlüssellänge von 
4096 Bit (RSA4096). Dieser erstellt deutlich längere Schlüssel und ist aufgrund 
seiner breiten Unterstützung und langjährigen Verwendung in vielen Systemen und Protokollen weit 
verbreitet.

[EC] Erstellen Sie ein Schlüsselpaar mit dem Verschlüsselungstyp `ed25519`, auf Ihrem lokalen Rechner. 
Setzen Sie ein Passwort für das Schlüsselpaar, das Sie sonst nirgends benutzen, denn Sie werden
mit diesem Schlüsselpaar nach einiger Zeit enorm vieles abgesichert haben.

Es sollten nun zwei neue Dateien unter `~/.ssh/` vorhanden sein. `ed25519` ist Ihr privater Schlüssel 
und sollte von Ihnen gut aufbewahrt werden. `ed25519.pub` ist Ihr öffentlicher Schlüssel. Diesen 
kopieren wir auf den Zielserver, damit Sie sich damit anmelden können.  

Lesen Sie die ssh-copy-id(1) 
[manpage](https://manpages.debian.org/testing/openssh-client/ssh-copy-id.1.en.html).  
Verstehen Sie insbesondere das **example** am Ende. 

[EC] Kopieren Sie Ihren öffentlichen Schlüssel auf den Zielserver.

[EC] Geben Sie ihn zusätzlich mit `cat` auf das Terminal aus.
Von hier aus könnten Sie ihn nun mit Copy/Paste mit der Maus für andere Zwecke in z.B.
Textfenster auf Webseiten kopieren, was beispielsweise zum Konfigurieren eines git-Servers nötig ist
(und was wir in Aufgabe [PARTREF::git-SSH] benutzen werden).

Ihr öffentlicher Schlüssel sollte jetzt auf dem Zielserver unter `~/.ssh/authorized_keys` gespeichert sein. 

[EC] Melden Sie sich auf dem Zielserver an. 

[EQ] Beschreiben Sie kurz, was sich geändert hat.


### Nutzen eines [TERMREF2::SSH-Agent::-en]

Stellen Sie sich vor, Sie sind ein Administrator in einer mittelständischen Firma. Sie 
verwalten 100 virtuelle Maschinen. Auf jeder dieser Maschinen ist ihr öffentlicher SSH-Schlüssel 
hinterlegt. Für die Entschlüsselung haben Sie ein 25-stelliges zufällig generiertes Passwort 
gewählt. Jetzt müssen Sie jedes Mal Ihr langes kompliziertes Passwort neu eingeben, wenn Sie sich 
auf einem der virtuellen Maschinen anmelden wollen. Um das zu umgehen und trotzdem die Sicherheit 
der Schlüssel beizubehalten, gibt es den SSH-Agenten.

Lesen Sie die Absätze am Anfang und am Ende der **Description** der 
[Manpage von ssh-agent(1)](https://man.openbsd.org/ssh-agent.1).

Lesen Sie die 3 Absätze am Anfang der **Description** der
[Manpage von ssh-add(1)](https://man.openbsd.org/ssh-add.1).

[EC] Starten Sie den SSH-Agenten.

[EC] Fügen Sie Ihren Schlüssel dem Agenten hinzu.  

[EC] Verbinden Sie sich mit dem Zielserver.

[EQ] Was hat sich geändert?  


### Automatisieren

Es ist umständlich den SSH-Agenten jedesmal neu zu starten, nachdem man sich angemeldet hat. 
Deswegen erstellen wir uns einen Alias, der das für uns erledigt.

Lesen Sie die **Syntax** und die **Dauerhafte Verwendung** im
[Beitrag über `alias`](https://wiki.ubuntuusers.de/alias/) auf ubuntuusers.

[EC] Erstellen Sie einen Alias `ssha`, welches den Agenten startet und Ihre Schlüssel in den Agenten 
kopiert. Zeigen Sie ihn im Kommandoprotokoll vor, z.B. mit `grep`.

Jetzt haben Sie eine schnelle Möglichkeit den SSH-Agenten zu starten.  
[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll und Markdowndokument]
[PROT::ALT:ssh.prot] 

### Markdown-Antworten
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
