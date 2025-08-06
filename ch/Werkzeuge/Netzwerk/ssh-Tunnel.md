title: "ssh-Tunnel und Ports"
stage: beta
timevalue: 1.0
difficulty: 3
explains: Netzwerkport, Firewall
assumes: ssh
---

[SECTION::goal::idea]

- Ich verstehe, was SSH-Tunnel sind. 
- Ich verstehe die IP-Konzepte dahinter. 
- Ich weiß wie ich SSH-Tunnel verwenden kann.
[ENDSECTION]


[SECTION::background::default]
Mit einem Porttunnel kann man einen Netzwerkport eines entfernten Rechners so aussehen lassen
(und nutzen) als wäre er ein lokaler Port. 
Die Daten laufen dabei durch eine verschlüsselte Tunnelverbindung.
Damit lassen sich zahllose Problemstellungen lösen, die mit nicht-öffentlichen Netzresourcen zu tun haben.
Umgekehrt geht es aber auch: Eine lokale Netzwerkressource auf einem fernen Rechner wie eine
_dort_ lokale aussehen lassen.
Das ist der umgekehrte Tunnel ("reverse tunnel") für den Export.
[ENDSECTION]


[SECTION::instructions::detailed]

<replacement id='ssh-tunnel-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Ports und Firewalls

Ein [TERMREF::Netzwerkport] ist ein logischer Zugangspunkt auf einem Computer.
Er wird durch eine Nummer identifiziert und weist Netzwerkdaten der richtigen Anwendung zu. 
Es gibt 65536 Ports, die in die Bereiche privilegierte Ports, registrierte Ports und 
dynamische/private Ports unterteilt sind.

Eine [TERMREF::Firewall] überwacht den Netzwerkverkehr, indem sie alle Pakete auf allen Ports analysiert
und dann entscheidet was verworfen oder weitergeleitet wird.
Somit wird ein Netzwerk oder auch ein Rechner vor unerwünschten Zugriffen und schädlichen Daten geschützt.

SSH nutzt den System-Port 22 für Verbindungen. 

### Verständnis von SSH-Tunneln

Mit einem Porttunnel können Sie einen Netzwerkport eines entfernten Rechners so aussehen lassen, 
als wäre er ein lokaler Port. Das nennt man einen Tunnel aufbauen. Hierbei können die Portnummer der 
entfernten und lokalen Seite verschieden sein.

Schauen Sie sich auf der 
[ssh(1) manpage](https://man.openbsd.org/ssh) 
die Option `-L` an.
Verwirrende Beschreibung!

Verstehen Sie stattdessen diese 
[grafische Erklärung von SSH-Tunneln](https://iximiuz.com/ssh-tunnels/ssh-tunnels-2000-opt.png)
und den entsprechenden Abschnitt 
[Local Port Forwarding](https://iximiuz.com/en/posts/ssh-tunnels/) 
der dazugehörigen Seite.

[NOTICE]
**Eselsbrücke**

Der Optionsname gibt an, wo der neue Port angelegt wird: 

- L lokal
- R remote

Dann folgt der neue Port, dann kommt der Hostname, der auf der _anderen_ Seite ausgewertet wird 
(also bei -L remote und bei -R lokal), dann der zugehörige schon existierende Port. 
Wenn also als Host `localhost` dasteht, bezeichnet das für -L den Remotesever und für -R den lokalen Rechner.

Insgesamt ist das Format also

- `-L newlocalport:remotehostname:existingremoteport`
- `-R newremoteport:localhostname:existinglocalport`
[ENDNOTICE]

Schauen Sie sich nun nochmals die Beschreibung der Option `-L` auf der [ssh(1) manpage](https://man.openbsd.org/ssh) an.

Diesmal sollten Sie verstehen können, was hier gemeint ist (jedenfalls für den hier
besprochenen port-basierten Aufruf). 
Meistens fehlt das Hintergrundwissen, wenn man eine `manpage` nicht versteht; 
in seltenen Fällen (wie hier) liegt es aber auch an der Formulierung der `manpage` selbst.

### SSH-Tunnel aufbauen

[EC] Auf Ihrem Rechner (`localhost`): Öffnen Sie einen Porttunnel vom Port 9007 des Zielservers (siehe oben)
zu Port 9009 von `localhost`.

Bitte nicht wundern, POSIX-konform gibt es keine Bestätigung, dass der Porttunnel geöffnet wurde.
Wenn die SSH-Verbindung erfolgreich war (und die Shell sich meldet), wurde auch der Porttunnel aufgebaut.
Beide Systeme sind jetzt also mit einem verschlüsselten Tunnel verbunden.

Jetzt holen wir uns (veranschaulicht mit einem kleinen Webserver) die Arbeitsumgebung des Zielservers
auf unser lokales System.

[WARNING]
Führen Sie den nächsten Befehl in einem Dateibaum aus,
der _nur unwichtige Daten_ enthält, die problemlos öffentlich werden dürfen, denn
der Befehl öffnet den Port 9007 des Zielservers u.U. öffentlich sichtbar für das gesamte Internet.
[ENDWARNING]

[EC] Auf dem Zielserver: Starten sie den Webserver `python -m http.server 9007`.
     (Wenn 9007 dort nicht frei ist, benutzen Sie einen anderen Port; aber lokal bleibt es bei 9009.)

- Auf Ihrem Rechner: Öffnen Sie einen Browser und greifen Sie auf localhost mit Port 9009 zu.
- Auf Ihrem Rechner: Browser wieder schließen.
- Auf dem Zielserver: Schließen Sie den Webserver.
- Auf dem Zielserver: Schließen Sie die SSH-Verbindung.


### Reverse-Tunnel aufbauen

Jetzt machen wir das gleiche Spiel umgekehrt: 
Wir exportieren einen lokalen Webserver nach Remote.

Betrachten Sie nochmals die
[grafische Erklärung von SSH-Tunneln](https://iximiuz.com/ssh-tunnels/ssh-tunnels-2000-opt.png)
und nun den Abschnitt 
[Remote Port Forwarding](https://iximiuz.com/en/posts/ssh-tunnels/) 
der dazugehörigen Seite.

Schauen Sie sich diesmal die Option `-R` von der [ssh(1) manpage](https://man.openbsd.org/ssh) an.

[EC] Auf Ihrem Rechner: Starten sie den Webserver `python -m http.server 9007`.
Für das Arbeitsverzeichnis gilt die gleiche Warnung wie oben.

[EC] Auf Ihrem Rechner: Öffnen Sie einen Porttunnel vom Port 9007 Ihres Rechners 
zu Port 10007 auf `localhost` des Zielservers.

[NOTICE]
Falls der Port 10007 belegt ist, nehmen Sie einen anderen Port aus dem 10000er-Bereich.
[ENDNOTICE]

Verstehen Sie auf folgender Seite den Abschnitt 
[Download files or webpage using curl](https://itsfoss.com/download-files-from-linux-terminal/#download-files-or-webpage-using-curl).

[EC] Auf dem Zielserver: Laden Sie eine Datei aus Ihrem Dateibaum mit `curl` herunter.

- Auf dem Zielserver: Schließen Sie die Verbindung.
- Auf Ihrem Rechner: Schließen Sie den Webserver.

Kopieren Sie alle Teile des Kommandoprotokolls zusammen in eine Kommandoprotokolldatei.
Haben Sie daran gedacht, auf dem Zielserver das gleiche Format des Shell-Prompts einzustellen
wie in ihrem ProPra-Arbeitsverzeichnis?
Sonst klappt die Anzeige des Kommandoprotokolls in der sedrila-Webapp nicht und Ihr_e Tutor_in
guckt unglücklich bis grimmig.

Fazit: SSH-Tunnel sind eine Art Schweizer Messer für viele Problemstellungen im Bereich Netzdienste.
(Allerdings braucht man für eine dauerhafte Nutzung weitere Mechanismen, die den Tunnel nach
Störungen immer wieder frisch aufbauen.)
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:ssh-Tunnel.prot]
[ENDINSTRUCTOR]
