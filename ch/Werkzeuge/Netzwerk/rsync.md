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

Lesen Sie bis einschließlich **Null Output or DryRun, and Verbose** des Beitrages
[Rsync Cross Platform Tutorial](https://www.linode.com/docs/guides/rsync-cross-platform-tutorial/)

<replacement id='rsync-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

### Testdateien erstellen

```bash
#!/bin/bash

# Verzeichnis festlegen
unterordner="$HOME/ws/tmp/rsync_copy_data/"

# Sicherstellen, dass der Unterordner existiert
if [ ! -d "$unterordner" ]; then
    mkdir -p "$unterordner"
fi

# 5 Dateien erstellen
for i in {1..5}; do
    echo "Inhalt der Datei $i" > "$unterordner/datei_$i"
done

echo "$i Dateien wurden im Unterordner erstellt: $unterordner"
```

- [EC] Erstellen Sie eine Datei `rsync_copy_data.sh` auf Ihrem System mit obigem Inhalt.
  Das Skript erstellt einen neuen Ordner `rsync_copy_data` mit 5 Textdateien.  
- [EC] Führen Sie das Skript mit `bash rsync_copy_data.sh` aus.
  Prüfen Sie, ob der Unterordner `rsync_copy_data` und die Textdateien vorhanden sind.


### Nutzen von rsync

Man arbeitet mit `rsync` meistens auf ganzen (oftmals großen) Dateibäumen.
Dadurch können schon kleine Tippfehler beim Kommando sehr unerfreuliche Auswirkungen haben,
also bitte Vorsicht!

- [EC] Erstellen Sie den Ordner `/tmp/rsync_destination`.
- [EC] Führen Sie nacheinander beide Befehle aus  
    `rsync -a ~/ws/tmp/rsync_copy_data /tmp/rsync_destination/`  
    `rsync -a ~/ws/tmp/rsync_copy_data/ /tmp/rsync_destination/`  
- [EQ] Was ist der Unterschied im Verhalten der beiden Kommandos?

[NOTICE]
Merken Sie sich dieses Verhalten von rsync. Die meisten Kopier-Befehle (`cp`, `scp`, `rsync`...) 
nutzen diese Semantik.
[ENDNOTICE]

`rsync` bietet die Möglichkeit, Daten auf einen entfernten Pfad zu kopieren.

Lesen Sie den Abschnitt **Usage** der 
[rsync(1) manpage](https://manpages.debian.org/stable/rsync/rsync.1.en.html)

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

- [EC] Kopieren Sie die Dateien aus dem Ordner `~/ws/tmp/rsync_copy_data` per rsync in den 
       `/tmp/rsync_destination3` Ordner. 
- [EC] Fügen Sie der Datei `~/ws/tmp/rsync_copy_data/datei_1` den Text `Ich wurde veraendert` 
       hinzu.  
- [EC] Kopieren Sie die Dateien aus dem Ordner `~/ws/tmp/rsync_copy_data` per rsync in den 
       `/tmp/rsync_destination3` Ordner. 
- [EC] Vergewissern Sie sich, dass die Datei `datei1` in den `/tmp/rsync_destination3` Ordner geändert wurde.

### Reflektion

- [EQ] Wie stellt rsync sicher, dass nur geänderte Dateien erneut kopiert werden?
- [EQ] Welche Unterschiede gibt es zwischen der Verwendung von rsync und anderen Kopierbefehlen wie `cp`?
- [EQ] Wie könnten Sie überprüfen, ob die Synchronisation tatsächlich alle Änderungen übernommen hat?


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