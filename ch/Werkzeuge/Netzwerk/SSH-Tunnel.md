title: SSH-Tunnel
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: SSH
---
[SECTION::goal::idea]

 - Ich verstehe SSH-Porttunnel und weiß wie ich sie nutze.

[ENDSECTION]

[SECTION::background::default]

OpenSSH bietet eine mächtige Weiterleitungsfunktion, die den Verkehr an einem Quellport durch 
einen SSH-Prozess tunnelt (und verschlüsselt) und ihn dann an einen Port auf einem Zielhost 
weiterleitet. Dieser Mechanismus ist als Port Tunnelling oder Port Forwarding bekannt.

[ENDSECTION]

[SECTION::instructions::detailed]

<replacement id='targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>


### Starten des Porttunnels

Schauen Sie sich die [Beispiele](https://wiki.ubuntuusers.de/SSH/#SSH-Tunnel) von SSH-Tunneln von 
ubuntuusers an.  
Lesen Sie die Option **-L** der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EC] Öffnen Sie einen Porttunnel auf Ihrem System mit Port 9007 und leiten Sie es auf localhost weiter.

[WARNING]
Führen Sie den nächsten Befehl in einem Dateibaum mit ganz unwichtigen Daten. Mit dem Befehl öffnen 
Sie den Port 9007 öffentlich sichtbar für das Internet. Also mit Vorsicht benutzen. 
[ENDWARNING]

- [EC] Starten sie den Webserver auf dem Zielserver: `python -m http.server 9007`.
- [EC] Öffnen Sie einen Browser auf Ihrem System, nicht dem Zielserver (!), und greifen Sie auf 
    den localhost mit Port zu.

Eine Liste Ihrer Dateien sollte jetzt sichtbar sein.

- [EC] Um die Funktionalität des Servers zu testen, laden Sie eine Datei runter.
- [EC] Schließen Sie den Browser.
- [EC] Schließen Sie den Python-Server auf dem Zielserver.
- [EC] Schließen Sie die Verbindung zum Zielserver.

[NOTICE]
[EREFC::3] bis [EREFC::5] kommen nicht ins Kommandoprotokoll.
[ENDNOTICE]

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:SSH-Tunnel.prot] 

[ENDINSTRUCTOR]


[INSTRUCTOR::Markdowndokument]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]