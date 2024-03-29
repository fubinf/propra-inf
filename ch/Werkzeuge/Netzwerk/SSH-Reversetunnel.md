title: SSH-Reversetunnel
stage: alpha
timevalue: 1.0
difficulty: 3
assumes: SSH
requires: SSH-Tunnel
---
[SECTION::goal::idea]

 - Ich verstehe SSH-Reversetunnel und weiß wie ich sie nutze.

[ENDSECTION]

[SECTION::background::default]

Genauso wie Sie sich die Umgebung von einem entfernten Rechner zu sich holen können, können Sie auch Ihre Umgebung auf den entfernten Rechner bringen.  
Ein Reversetunnel wird mit dem Flag `-R` aufgerufen.

[ENDSECTION]

[SECTION::instructions::loose]

<replacement id='targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Voraussetzungen

- [ER] Stellen Sie sicher, dass auf Ihrem System `python3`, `pip` und `Flask` installiert sind.

### Reversetunnel

- [EC] Starten Sie den Webserver aus der Aufgabe [PARTREF::SSH-Tunnel] auf Ihrem Rechner.
- [EC] Verbinden Sie sich per SSH auf den Zielserver mit aktiviertem Reversetunnel auf den Port aus dem Skript und mit aktivierter X11-Weiterleitung.
- [EC] Öffnen Sie einen Browser Ihrer Wahl. Sie sollten "Hello World" in Ihrem Fenster sehen.
- [EC] Schließen Sie den Browser und den Webserver.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]
