title: rsync
stage: alpha
timevalue: 1
difficulty: 2
assumes: Umgang-mit-Verzeichnissen
---
[SECTION::goal::idea]
- Ich verstehe wie rsync funktioniert und wie ich dieses anwende.
[ENDSECTION]

[SECTION::background::default]
`rsync` ist ein Programm, um Dateien zwischen lokalen oder entfernten Pfaden abzugleichen.
[ENDSECTION]

[SECTION::instructions::detailed]

Lesen Sie sich diesen [Beitrag](https://wiki.ubuntuusers.de/rsync/) von ubuntuusers über rsync durch.  
Lesen Sie insbesondere den Abschnitt **Anwendung** und verstehen Sie, was die Option `-a` macht.

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

Man muss immer darauf achten, wie die Befehle aussehen. Sonst hat man hinterher doppelt so viel 
Arbeit. Schauen Sie sich in der nächsten Aufgabe beide Befehle genau an.

- [EC] Erstellen Sie den Ordner `/tmp/propra_sync`.
- [EQ] Führen Sie nacheinander beide Befehle aus und beschreiben Sie was sie beobachten:  
    `rsync -a /home/username/rsync_copy_data /tmp/propra_rsync/`  
    `rsync -a /home/username/rsync_copy_data/ /tmp/propra_rsync/`  

Merken Sie sich dieses Verhalten von rsync. Es gibt weitere Kopier-Befehle, die eine ähnliche 
Semantik haben.

Wie im "Hintergrund" beschrieben, können Daten auf einen entfernten Pfad kopiert werden.  
Lesen Sie unter dem Abschnitt **Beispiele** des Beitrags
[Beitrag](https://wiki.ubuntuusers.de/rsync/#Beispiele) von ubuntuusers über rsync die Beispiele 
durch.

- [EC] Kopieren Sie die Daten von Ihrem System auf den Zielserver.  
  Andersrum funktioniert es auch.
- [EC] Kopieren Sie die Daten vom Zielserver auf ihr System.

rsync hat einen ganz bestimmten Vorteil gegenüber anderen Kopier-Befehlen. Es vergleicht die zu 
kopierenden Daten, bevor sie kopiert werden, somit werden nur die Daten kopiert, die verändert 
wurden. Somit wird rsync gerne als Backup-Lösung genutzt, da es nur die veränderten Daten kopiert. 

Zur Veranschaulichung ändern wir eine Datei aus den vorhin erstellten Dateien und kopieren Sie in 
einen Ordner.

- [EC] Kopieren Sie die Dateien aus dem Ordner `/home/username/rsync_copy_data` per rsync in den `/tmp/propra_sync` Ordner. 
- [EC] Fügen Sie der Datei `/home/username/rsync_copy_data/datei_1.txt` zufälligen Text hinzu.  
- [EC] Kopieren Sie die Dateien aus dem Ordner `/home/username/rsync_copy_data` per rsync in den `/tmp/propra_sync` Ordner. 
- [EC] Vergewissern Sie sich, dass die Datei `datei1.txt` in den `/tmp/propra_sync` Ordner geändert wurde.

[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]

[INCLUDE::../../_include/Instructor-Auseinandersetzung.md]

- [EREFQ::1] Bei dem ersten Befehl fehlt ein `/`. Damit verändert sich das Ergebnis von rsync.

[ENDINSTRUCTOR]