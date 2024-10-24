title: Dateien mit rsync kopieren
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

### rsync installieren

- [EC] Aktualisieren Sie Ihr System.
- [EC] Installieren Sie das Paket `rsync`

Lesen Sie die ersten vier Abschnitte bis einschließlich **Usage** und die Option **-a** der 
[rsync(1) manpage](https://manpages.debian.org/bookworm/rsync/rsync.1.en.html)

<replacement id='rsync-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Testdateien erstellen

```bash
[INCLUDE::rsync_copy_data.sh]
```

- [EC] Erstellen Sie eine Datei `rsync_copy_data.sh` auf Ihrem System mit obigem Inhalt von 
  `rsync_copy_data.sh`.
    - Das Skript erstellt einen neuen Ordner `rsync_copy_data` mit 20 Textdateien.  
    - Prüfen Sie, ob der Unterordner `rsync_copy_data` und die Textdateien vorhanden sind.
- [EC] Führen Sie das Skript mit `bash rsync_copy_data.sh` aus.

### Nutzen von rsync

Es ist wichtig, stets auf die Struktur der Befehle zu achten, da sonst später doppelt so viel 
Arbeit anfällt. Prüfen Sie daher in der nächsten Aufgabe beide Befehle sorgfältig.

- [EC] Erstellen Sie den Ordner `/tmp/rsync_destination`.
- [EC] Führen Sie nacheinander beide Befehle aus  
    `rsync -a ~/rsync_copy_data /tmp/rsync_destination/`  
    `rsync -a ~/rsync_copy_data/ /tmp/rsync_destination/`  
- [EQ] Was haben Sie beobachtet.

[NOTICE]
Merken Sie sich dieses Verhalten von rsync. Die meisten Kopier-Befehle (`cp`, `scp`, `rsync`...) 
nutzen diese Semantik.
[ENDNOTICE]

`rsync` bietet die Möglichkeit, Daten auf einen entfernten Pfad zu kopieren.

Lesen Sie den Abschnitt **Usage** der 
[rsync(1) manpage](https://manpages.debian.org/bookworm/rsync/rsync.1.en.html)

- [EC] Kopieren Sie die den Ordner `rsync_copy_data` von Ihrem System auf Ihren 
       home-Ordner des Zielservers.  
  `rsync` kann die Daten auch in die umgekehrte Richtung kopieren.  
- [EC] Kopieren Sie die in der vorherigen Aufgabe kopierten Daten vom Zielserver auf ihr System in 
       einen neuen Ordner `/tmp/rsync_destination2`.

### Backup mit rsync

rsync hat einen ganz bestimmten Vorteil gegenüber anderen Kopier-Befehlen. Es vergleicht die zu 
kopierenden Daten, bevor sie kopiert werden, somit werden nur die Daten kopiert, die verändert 
wurden. Deswegen wird rsync gerne als Backup-Lösung genutzt, da es nur die veränderten Daten kopiert. 

Zur Veranschaulichung ändern wir eine Datei aus den vorhin erstellten Dateien und kopieren Sie in 
einen Ordner.

- [EC] Kopieren Sie die Dateien aus dem Ordner `/home/username/rsync_copy_data` per rsync in den `/tmp/rsync_destination3` Ordner. 
- [EC] Fügen Sie der Datei `/home/username/rsync_copy_data/datei_1` den Text `Ich wurde veraendert` hinzu.  
- [EC] Kopieren Sie die Dateien aus dem Ordner `/home/username/rsync_copy_data` per rsync in den `/tmp/rsync_destination3` Ordner. 
- [EC] Vergewissern Sie sich, dass die Datei `datei1` in den `/tmp/propra_sync` Ordner geändert wurde.

[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:rsync.prot]
[ENDINSTRUCTOR]

[INSTRUCTOR::Markdowndokument]

[INCLUDE::ALT:]
[ENDINSTRUCTOR]