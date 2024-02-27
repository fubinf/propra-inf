title: SSH-Tunnel
stage: draft
timevalue: 1.0
difficulty: 3
explains:
assumes: SSH
requires: venv
---
[SECTION::goal::idea]

 - Ich verstehe SSH-Porttunnel und weiß wie ich sie nutze.

[ENDSECTION]
[SECTION::background::default]

OpenSSH bietet eine sehr mächtige Weiterleitungsfunktion, die den Verkehr an einem Quellport durch einen SSH-Prozess tunnelt (und verschlüsselt) und ihn dann an einen Port auf einem Zielhost weiterleitet. Dieser Mechanismus ist als Port Tunnelling oder Port Forwarding bekannt und bietet große Vorteile:

- Firewalls umgehen, um auf Ports auf entfernten Hosts zuzugreifen.
- Zugriff von außen auf einen Host in Ihrem privaten Netzwerk.
- Verschlüsselung für den gesamten Datenaustausch.

[ENDSECTION]
[SECTION::instructions::detailed]

### Vorbereitungen

- [ER] Kopieren Sie die Datei `webserver.py` auf Ihr System.

```python
[INCLUDE::webserver.py]
```

- [ER] Stellen Sie sicher, dass sie [PARTREF::venv] eingerichtet haben.

### Starten des Webservers und des Porttunnels

- [EC] Kopieren Sie das Programm mit scp nach `andorra.imp.fu-berlin.de`:  
    `scp /path/to/webserver.py username@andorra.imp.fu-berlin.de:~`

- [EC] Öffnen Sie den Porttunnel:  
       `ssh username@andorra.imp.fu-berlin.de -L 8080:localhost:16300`  
         
       `username@andorra.imp.fu-berlin.de`: hiermit authentifizieren Sie sich gegen den Server  
       `-L`: gibt an, dass Sie einen Porttunnel öffnen möchten  
       `8080`: gibt an, welchen Port sie lokal für den Tunnel öffnen möchten  
       `localhost:16300`: gibt an, auf welchem Port der Service zuhören soll  

- [EC] Installieren Sie `Flask` mit pip: `pip install flask`

- [EC] Starten sie den Webserver: `python webserver.py`

- [EC] Öffnen Sie in einem Browser auf Ihrem System: `localhost:8080`

- [EC] Nachdem Sie erfolgreich `Hello Tunnel` im Browser gesehen haben, schließen Sie den Webserver auf `andorra` per `STRG+C` im Terminal.

### X11 Weiterleitung

- [EC] Durch einen X11-Tunnel wird das X Window System auf dem entfernten Rechner an Ihren lokalen Rechner geleitet. Dazu übergeben Sie ssh einfach die Option -Y.
- `ssh -Y username@andorra.imp.fu-berlin.de`

- [EC] Öffnen Sie `firefox` oder `chromium` um sicherzustellen, dass die X11-Weiterleitung aktiv ist.

- [EC] Schließen Sie den Browser.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

