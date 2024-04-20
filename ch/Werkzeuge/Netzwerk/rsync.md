title: rsync
stage: alpha
timevalue: 1
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

Lesen Sie sich diesen [Beitrag](https://wiki.ubuntuusers.de/rsync/) von ubuntuusers über rsync durch.

<replacement id='targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Testdateien erstellen

- [EC] Kopieren Sie die Datei `rsync_copy_data.sh` auf Ihr System in Ihren home-Ordner und führen Sie es mit `bash rsync_copy_data.sh` aus.  
Es erstellt einen neuen Ordner `rsync_copy_data` mit 20 Textdateien.

```bash
[INCLUDE::rsync_copy_data.sh]
```

- [EC] Prüfen Sie, ob der Unterordner `rsync_copy_data` und die Textdateien vorhanden sind.

### Nutzen von rsync

- [EQ] Führen Sie nacheinander beide Befehle aus und beschreiben Sie was sie beobachten:  
    `rsync -a /home/username/rsync_copy_data /tmp/propra_rsync/`  
    `rsync -a /home/username/rsync_copy_data/ /tmp/propra_rsync/`  

Wie im "Hintergrund" beschrieben, können Daten auf einen entfernten Pfad kopiert werden.  
- [EC] Kopieren Sie die Daten von Ihrem System auf den Zielserver.  
Andersrum funktioniert es auch.
- [EC] Kopieren Sie die Daten vom Zielserver auf ihr System.
- [EC] Fügen Sie der Datei `/home/username/rsync_copy_data/datei_1.txt` zufälligen Text hinzu.  
    Kopieren Sie die Datei per rsync auf in den `/tmp/propra_sync` Ordner. 
- [EQ] Was fällt Ihnen auf?


[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
