title: SSH-Tunnel
stage: alpha
timevalue: 0.5
difficulty: 3
assumes: ssh
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

Lesen Sie den Paragraphen SSH-Tunnel des [SSH-Beitrags](https://wiki.ubuntuusers.de/SSH) von 
ubuntuusers durch.

Lesen Sie die Option **-L** der [ssh(1) manpage](https://man.openbsd.org/ssh).

- [EC] Öffnen Sie einen Porttunnel vom Zielserver auf Port 9007 und leiten Sie es auf localhost weiter.

Nicht wundern, POSIX-konform gibt es keine Bestätigung, dass der Porttunnel geöffnet wurde.

Solange die SSH-Verbindung erfolgreich war, wurde auch der Porttunnel aufgebaut.

Beide Systeme sind jetzt mit einem verschlüsselten Tunnel auf `Port 9007` verbunden.

Jetzt holen wir uns veranschaulicht mit einem kleinen Befehl die Arbeitsumgebung vom Zielserver auf 
unser System.

[WARNING]
Führen Sie den nächsten Befehl in einem Dateibaum mit ganz unwichtigen Daten. Mit dem Befehl öffnen 
Sie den Port 9007 öffentlich sichtbar für das Internet. Also mit Vorsicht benutzen. 
[ENDWARNING]

- [EC] Starten sie den Webserver auf dem Zielserver: `python -m http.server 9007`.
- [EC] Öffnen Sie einen Browser auf Ihrem System, nicht dem Zielserver (!), und greifen Sie auf 
    localhost mit Port 9007 zu.

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

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:ssh-Tunnel.prot] 

[ENDINSTRUCTOR]
