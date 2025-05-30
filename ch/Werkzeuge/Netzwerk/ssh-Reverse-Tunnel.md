title: SSH-Reversetunnel
stage: alpha
timevalue: 0.5
difficulty: 3
assumes: ssh, ssh-Tunnel, X11-Weiterleitung
---
[SECTION::goal::idea]
 - Ich verstehe SSH-Reversetunnel und weiß wie ich sie nutze.
[ENDSECTION]

[SECTION::background::default]
Genauso wie Sie sich die Umgebung von einem entfernten Rechner zu sich holen können, können Sie 
auch Ihre Umgebung auf einen entfernten Rechner bringen.
[ENDSECTION]

[SECTION::instructions::loose]

<replacement id='ssh-Reverse-Tunnel-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Reversetunnel

Angenomen Sie wollen testen, ob eine Datenbank, die auf Ihrem Rechner liegt, mit dem entfernten System funktioniert.  
Zur Veranschaulichung nutzen wir hier den Webserver aus der [PARTREF::ssh-Tunnel]-Aufgabe.

Schauen Sie sich die [Beispiele](https://wiki.ubuntuusers.de/SSH/#SSH-Tunnel) von SSH-Tunneln von 
ubuntuusers an.  
Lesen Sie die Option **-R** der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EC] Starten Sie den Webserver aus der Aufgabe [PARTREF::ssh-Tunnel] auf Ihrem Rechner.

Öffnen Sie jetzt ein neues Kommandofenster. Führen Sie den nächsten Befehl im neuen Fenster aus.

- [EC] Verbinden Sie sich per SSH auf den Zielserver mit aktiviertem Reversetunnel auf den Port 
   9007 und mit aktivierter X11-Weiterleitung.
- [EC] Öffnen Sie einen Browser Ihrer Wahl auf dem Zielserver.

Nachdem Sie erfolgreich Ihren Dateibaum im Browser gesehen haben, können Sie den Browser, den 
Webserver und den Porttunnel wieder schließen.

- [EC] Schließen Sie den Browser.
- [EC] Schließen Sie die SSH-Verbindung.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
