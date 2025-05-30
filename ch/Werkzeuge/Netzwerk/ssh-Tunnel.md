title: SSH-Tunnel
stage: beta
timevalue: 0.5
difficulty: 3
assumes: ssh
---
[SECTION::goal::idea]
Ich verstehe SSH-Porttunnel und weiß wie ich sie nutze.
[ENDSECTION]

[SECTION::background::default]
Mit einem Porttunnel kann man einen Netzwerkport eines entfernten Rechners so aussehen lassen
(und nutzen) als wäre er ein lokaler Port. 
Die Daten laufen dabei durch eine verschlüsselte Tunnelverbindung.
Damit lassen sich zahllose Problemstellungen lösen, die mit nichtöffentlichen Netzresourcen zu tun haben.

[ENDSECTION]

[SECTION::instructions::detailed]

<replacement id='ssh-Tunnel-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>


### Starten des Porttunnels

Verstehen Sie den 
[Abschnitt "SSH-Tunnel" des SSH-Beitrags](https://wiki.ubuntuusers.de/SSH) 
von ubuntuusers.
Verstehen Sie die Option `-L` in der [ssh(1) manpage](https://man.openbsd.org/ssh).

[EC] Auf Ihrem Rechner (`localhost`): Öffnen Sie einen Porttunnel vom Port 9007 des Zielservers 
zu Port 9009 von `localhost`.
Bitte nicht wundern, POSIX-konform gibt es keine Bestätigung, dass der Porttunnel geöffnet wurde.
Wenn die SSH-Verbindung erfolgreich war, wurde auch der Porttunnel aufgebaut.
Beide Systeme sind jetzt also mit einem verschlüsselten Tunnel verbunden.

[EQ] Die Frage, welcher Port bei `-L` der lokale und welcher der entfernte ist, kann leicht verwirren,
zumal das Tunneln auch andersherum funktioniert, wenn die schon vorhandene Netzressource 
mit geöffnetem Port nicht auf der fernen, sondern auf der lokalen Seite liegt (Rückwärtstunnel: `-R`,
siehe Aufgabe [PARTREF::ssh-Reverse-Tunnel]).
Denken Sie sich eine Eselsbrücke für beide Fälle aus, die auch den jeweiligen Namen der Option erklärt, 
und beschreiben Sie sie.

Jetzt holen wir uns (veranschaulicht mit einem kleinen Webserver) die Arbeitsumgebung des Zielservers
auf unser lokales System.

[WARNING]
Führen Sie den nächsten Befehl in einem Dateibaum aus,
der nur unwichtige Daten enthält, die problemlos öffentlich werden dürfen,
denn der Befehl öffnet den Port 9007 des Zielservers u.U. öffentlich sichtbar für das gesamte Internet.
[ENDWARNING]

- Auf dem Zielserver: Starten sie den Webserver `python -m http.server 9007`.
- Auf Ihrem Rechner: Öffnen Sie einen Browser und greifen Sie auf localhost mit Port 9009 zu.

Eine Dateien-Liste Ihres Verzeichnisses auf dem Zielserver(!) sollte jetzt im Browser
Ihres eigenen Rechners sichtbar sein, durch den Tunnel herbeigeschleust.

- Auf Ihrem Rechner: Um die Funktionalität des Servers zu testen, laden Sie eine Datei runter.
- Auf Ihrem Rechner: Schließen Sie den Browser.
- Auf dem Zielserver: Schließen Sie den Python-Server.
- Auf Ihrem Rechner: Schließen Sie die Tunnelverbindung zum Zielserver.

Kopieren Sie beide Teile des Kommandoprotokolls zusammen in eine Kommandoprotokolldatei.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:ssh-Tunnel.prot] 

[ENDINSTRUCTOR]
