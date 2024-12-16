title: SSH-Tunnel
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: SSH, rsync
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


### Vorbereitungen

- [ER] Erstellen Sie eine Datei `webserver.py` mit unterem Inhalt auf Ihrem Rechner.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Tunnel'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

- [ER] Stellen Sie sicher, dass sie [PARTREF::venv] eingerichtet haben.

### Starten des Webservers und des Porttunnels

Angenommen Sie haben in Ihrer Firma eine komplizierte Entwicklungsumgebung eingerichtet, die viel 
Rechenkapazität benötigt. Sie wollen sich diese Entickwlungsumgebung auf Ihrem Notebook der Firma 
einrichten, aber merken schnell, dass es nicht funktionieren wird. Sie lernen von SSH-Tunneln und 
versuchen somit die Entwicklungsumgebung auf ihrem Rechner zum Laufen zu bekommen.

Zur Veranschaulichung der Tunnel werden wir hier einen kleinen Webserver nutzen, der 
"Hello Tunnel" anzeigt. 

- [EC] Kopieren Sie das Skript `webserver.py` mit `rsync` auf den Zielserver.
- [EC] Melden Sie sich auf dem Zielserver an.
- [EC] Installieren Sie `Flask` mit pip in ihrer [TERMREF::venv] auf dem Zielserver.

Schauen Sie sich die [Beispiele](https://wiki.ubuntuusers.de/SSH/#SSH-Tunnel) von SSH-Tunneln von 
ubuntuusers an.  
Lesen Sie die Option **-L** der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EC] Starten sie den Webserver auf dem Zielserver: `python webserver.py`.

[NOTICE]
Falls Sie WSL nutzen und Sie keine Möglichkeit haben graphische Programme zu starten beziehungsweise 
nicht möchten, können Sie sich den textbasiereten Browser `lynx` installieren und nutzen.  
Seiten werden mit diesem Kommando geöffnet: `lynx host:port`.  
Den Browser wird mit `q` und dann mit `Enter` oder `y` geschlossen.
[ENDNOTICE]

- [EC] Öffnen Sie einen Porttunnel mit dem angegebenen Port aus dem `webserver.py`-Skript.
- [EC] Öffnen Sie einen Browser auf Ihrem System, nicht dem Zielserver (!), und geben die Adresse 
       aus dem Skript an.

Jetzt sollten oben links im Fenster 'Hello Tunnel' stehen.

- [EC] Schließen Sie den Browser.
- [EC] Schließen Sie die Verbindung.

### X11 Weiterleitung

Die X11 Weiterleitung ermöglicht es Ihnen grafische Programme von einem entfernten Rechner auf 
ihrem Rechner anzeigen zu lassen.  
Stellen Sie sich vor, Sie arbeiten an einem CAD-Modell und brauchen dafür wieder eine sehr hohe 
Rechenleistung. Sie haben versucht das Modell auf ihrem Rechner zu starten, aber das Programm 
stürzt jedes Mal ab.  
Als Veranschaulichung nehmen wir hier den Browser `firefox`.

Lesen Sie die Optionen **-Y** und **-X** der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EQ] Erklären Sie den Unterschied der Optionen **-Y, -X**.

[NOTICE]
Verbinden Sie sich wenn möglich mit der sichereren Variante der beiden oben genannten Optionen.
[ENDNOTICE]

- [EC] Verbinden Sie sich mit dem Zielserver mit aktivierter X11-Weiterleitung.
- [EC] Starten Sie `firefox`.
- [EC] Öffnen Sie `google.com`.
- [EC] Schließen Sie `firefox`.
- [EC] Schließen Sie die Verbdindung.

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