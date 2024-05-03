title: SSH-Reversetunnel
stage: alpha
timevalue: 0.5
difficulty: 3
assumes: SSH, SSH-Tunnel
---
[SECTION::goal::idea]
 - Ich verstehe SSH-Reversetunnel und weiß wie ich sie nutze.
[ENDSECTION]

[SECTION::background::default]
Genauso wie Sie sich die Umgebung von einem entfernten Rechner zu sich holen können, können Sie 
auch Ihre Umgebung auf einen entfernten Rechner bringen.  
[ENDSECTION]

[SECTION::instructions::loose]

<replacement id='targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Voraussetzungen

- [ER] Stellen Sie sicher, dass auf Ihrem System `python3`, `pip` und `Flask` installiert sind.

### Reversetunnel

Angenomen Sie wollen testen, ob eine Datenbank, die auf Ihrem Rechner liegt, mit dem entfernten System funktioniert.  
Zur Veranschaulichung nutzen wir hier den Webserver aus der [PARTREF::SSH-Tunnel]-Aufgabe.

Schauen Sie sich die [Beispiele](https://wiki.ubuntuusers.de/SSH/#SSH-Tunnel) von SSH-Tunneln von 
ubuntuusers an.  
Lesen Sie die Option **-R** der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EC] Starten Sie den Webserver aus der Aufgabe [PARTREF::SSH-Tunnel] auf Ihrem Rechner.
- [EC] Verbinden Sie sich per SSH auf den Zielserver mit aktiviertem Reversetunnel auf den Port 
   aus dem Skript und mit aktivierter X11-Weiterleitung.
- [EC] Öffnen Sie einen Browser Ihrer Wahl.

Nachdem Sie erfolgreich `Hello Tunnel` im Browser gesehen haben, können Sie den Browser, den 
Webserver und den Porttunnel wieder schließen.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[ENDINSTRUCTOR]
