title: rsync
stage: draft
timevalue: 0.5
difficulty: 2
---
[SECTION::goal::idea]

- Ich verstehe wie rsync funktioniert und wie ich dieses anwende.

[ENDSECTION]
[SECTION::background::default]

`rsync` ist ein Programm, um Dateien zwischen lokalen oder entfernten 
Pfaden abzugleichen. Dabei werden zunächst die Größe und die Änderungszeit 
der Dateien in Quelle und Ziel verglichen („Quick Check“-Algorithmus). 
Dadurch werden nur die Dateien behandelt, bei denen es Änderungen gegeben hat.

[ENDSECTION]
[SECTION::instructions::detailed]

### Testdateien erstellen

- [ER] Kopieren Sie die Datei `rsync_copy_data.sh` auf Ihr System in Ihren home-Ordner und führen Sie es mit `bash rsync_copy_data.sh` aus.  
Es erstellt einen neuen Ordner `rsync_copy_data` mit 20 Textdateien.

```bash
[INCLUDE::rsync_copy_data.sh]
```

- [ER] Prüfen Sie, ob der Unterordner `rsync_copy_data` und die Textdateien vorhanden sind.

### Nutzen von rsync

- [EQ] Führen Sie nacheinander beide Befehle aus und beschreiben Sie was sie beobachten:  
    `rsync -a /home/username/rsync_copy_data /tmp/propra_rsync/`  
    `rsync -a /home/username/rsync_copy_data/ /tmp/propra_rsync/`  
    `-a` wendet den Befehl rekursiv an und kopiert fast alle Attribute der Daten mit

- [EC] Wie im "Hintergrund" beschrieben, kann man Daten auch auf einen entfernten Pfad kopieren.  
    Kopieren Sie die Daten von Ihrem System auf `andorra`:  
    `rsync -avP /home/username/rsync_copy_data username@andorra.imp.fu-berlin.de:/home/username/`  
    `-v` zeigt die ausgeführten Schritte an  
    `-P` gibt eine Fortschrittsanzeige wieder  

- [EC] Andersrum funktioniert das genauso:
    `rsync -avP username@andorra.imp.fu-berlin.de:/home/username/rsync_copy_data /tmp/`

- [EQ] Fügen Sie der Datei `/home/username/rsync_copy_data/datei_1.txt` zufälligen Text hinzu, damit sich das `modification date` der Datei ändert.  
    Führen Sie den `rsync`-Befehl danach aus:  
    `rsync -a /home/username/rsync_copy_data /tmp/propra_rsync/`  
    Was beobachten Sie?


[ENDSECTION]
[SECTION::submission::reflection]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
