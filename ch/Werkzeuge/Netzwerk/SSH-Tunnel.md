title: SSH-Tunnel
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: SSH, venv, apt
---
[SECTION::goal::idea]
 - Ich verstehe SSH-Porttunnel und weiß wie ich sie nutze.
[ENDSECTION]

[SECTION::background::default]
OpenSSH bietet eine sehr mächtige Weiterleitungsfunktion, die den Verkehr an einem Quellport durch 
einen SSH-Prozess tunnelt (und verschlüsselt) und ihn dann an einen Port auf einem Zielhost 
weiterleitet. Dieser Mechanismus ist als Port Tunnelling oder Port Forwarding bekannt.
[ENDSECTION]

[SECTION::instructions::detailed]

<replacement id='targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>



### Vorbereitungen

- [ER] Kopieren Sie die Datei `webserver.py` auf Ihr System.

```python
[INCLUDE::webserver.py]
```

- [ER] Stellen Sie sicher, dass sie [PARTREF::venv] eingerichtet haben.

### Starten des Webservers und des Porttunnels

Angenommen Sie haben in Ihrer Firma eine komplizierte Entwicklungsumgebung eingerichtet, die viel 
Rechenkapazität benötigt. Sie wollen sich diese Entickwlungsumgebung auf Ihrem Notebook der Firma 
einrichten, aber merken schnell, dass es nicht funktionieren wird. Sie lernen von SSH-Tunneln und 
versuchen somit die Entwicklungsumgebung auf ihrem Rechner zum Laufen zu bekommen.

Zur Veranschaulichung der Tunnel werden wir hier einen kleinen Webserver nutzen, der 
"Hello Tunnel!" anzeigt. 

Schauen Sie sich die [Beispiele](https://wiki.ubuntuusers.de/SSH/#scp) von `scp` von ubuntuusers an.

- [EC] Kopieren Sie das Programm mit `scp` auf den Zielserver.

Stellen Sie sicher, dass sie ein [PARTREF::venv] auf Ihrem System eingerichtet haben.

- [EC] Installieren Sie `Flask` mit pip in ihrer [TERMREF::venv] auf dem Zielserver.

Schauen Sie sich die [Beispiele](https://wiki.ubuntuusers.de/SSH/#SSH-Tunnel) von SSH-Tunneln von 
ubuntuusers an.  
Lesen Sie die Option **-L** der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EC] Starten sie den Webserver auf dem Zielserver.

[NOTICE]
Falls Sie WSL nutzen und Sie keine Möglichkeit haben graphische Programme zu starten, können Sie 
sich den textbasiereten Browser `lynx` installieren und nutzen.  
Seiten öffnen Sie, indem Sie die Seite nach dem Kommando hinzufügen: `lynx host:port`.  
Den Browser schließen Sie mit `q` und dann `Enter` oder `y`.
[ENDNOTICE]

- [EC] Öffnen Sie einen Porttunnel mit dem angegebenen Port aus dem `webserver.py` Skript.
- [EC] Öffnen Sie einen Browser auf Ihrem System, nicht dem Zielserver (!), und geben die Adresse 
   an, die Ihnen vom Skript genannt wurde.

Nachdem Sie erfolgreich `Hello Tunnel` im Browser gesehen haben, können Sie den Browser, den 
Webserver und den Porttunnel wieder schließen.

### X11 Weiterleitung

Die X11 Weiterleitung ermöglicht es Ihnen grafische Programme von einem entfernten Rechner auf 
ihrem Rechner anzeigen zu lassen.  
Stellen Sie sich vor, Sie arbeiten an einem CAD-Modell und brauchen dafür wieder eine sehr hohe 
Rechenleistung. Sie haben versucht das Modell auf ihrem Rechner zu starten, aber das Programm 
stürzt jedes Mal ab.  
Als Veranschaulichung nehmen wir hier den Browser `chromium`.

Lesen Sie die Optionen -**Y** und **-X** der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EQ] Erklären Sie den Unterschied der beiden Optionen.
- [EC] Verbinden Sie sich mit dem Zielserver mit aktivierter X11-Weiterleitung.
- [EC] Starten Sie `chromium`.

Nachdem sich `chromium` erfolgreich geöffnet hat, können Sie den Browser und die Verbindung wieder schließen.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Erwartung]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]

[ENDINSTRUCTOR]

