title: SSH-Reversetunnel
stage: draft
timevalue: 1.0
difficulty: 3
assumes: SSH, SSH-Tunnel
---
[SECTION::goal::idea]

 - Ich verstehe SSH-Reversetunnel und weiß wie ich sie nutze.

[ENDSECTION]
[SECTION::background::default]

Genauso wie Sie sich die Umgebung von einem entfernten Rechner zu sich holen können, können Sie auch Ihre Umgebung auf den entfernten Rechner bringen.  
Ein Reversetunnel wird mit dem Flag `-R` aufgerufen.

[ENDSECTION]
[SECTION::instructions::loose]

### Voraussetzungen

- [ER] Stellen Sie sicher, dass auf Ihrem System `python3`, `pip` und `Flask` installiert sind.

### Reversetunnel

- [EC] Starten Sie den Webserver aus der Aufgabe [PARTREF::SSH] auf Ihrem Rechner.

- [EC] Verbinden Sie sich per SSH auf `andorra` mit aktiviertem Reversetunnel auf den Port aus dem Skript und mit aktivierter X11-Weiterleitung.

- [EC] Öffnen Sie einen Browser Ihrer Wahl `chromium` oder `firefox`.

- [EC] Schließen Sie den Browser und den Webserver.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Kommandoprotokoll.md]

[ENDSECTION]
