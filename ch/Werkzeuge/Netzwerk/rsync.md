title: Dateien mit rsync abgleichen
stage: alpha
timevalue: 1
difficulty: 2
assumes: Umgang-mit-Verzeichnissen
---

[SECTION::goal::idea]
Ich verstehe wie rsync funktioniert und wie ich dieses anwende.
[ENDSECTION]


[SECTION::background::default]
`rsync` gleicht Dateien zwischen lokalen oder entfernten Pfaden ab.
Es prüft vor dem Kopieren, welche Dateien sich geändert haben und überträgt nur diese.
[ENDSECTION]


[SECTION::instructions::detailed]

### rsync installieren

Aktualisieren Sie Ihr System und installieren Sie das Paket `rsync`:
`sudo apt update && sudo apt upgrade -y && sudo apt install rsync`

Lesen Sie die Abschnitte **Description und Usage** der 
[rsync(1) manpage](https://manpages.debian.org/stable/rsync/rsync.1.en.html).

Die **additional features** aus dem Abschnitt **Description** können Sie überspringen.

<replacement id='rsync-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>


### Testdateien erstellen

[EC] Erstellen Sie einen Ordner `rsync_copy_data` in Ihrem [TERMREF::Hilfsbereich].

Jetzt brauchen wir noch Dateien in diesem Ordner. Führen Sie den nächsten Befehl aus:

[EC] `touch ws/tmp/rsync_copy_data/datei{1..5}`


### Verhalten von `rsync`

[EC] Erstellen Sie den Ordner `rsync_destination` in Ihrem [TERMREF::Hilfsbereich].

[WARNING]
Man arbeitet mit `rsync` meistens auf ganzen (oftmals großen) Dateibäumen.
Dadurch können schon kleine Tippfehler beim Kommando sehr unerfreuliche Auswirkungen haben,
also bitte Vorsicht!
[ENDWARNING]

Führen Sie nacheinander die folgende beiden (gleichen) Befehle aus: 

[EC] `rsync -a ~/ws/tmp/rsync_copy_data ~/ws/tmp/rsync_destination/` 

Schauen Sie sich die Dateien im Ordner `rsync_destination` an.

[EC] `rsync -a ~/ws/tmp/rsync_copy_data/ ~/ws/tmp/rsync_destination/`

Schauen Sie sich die Dateien im Ordner `rsync_destination` nochmal an.

[EQ] Was ist der Unterschied im Verhalten der beiden Kommandos?

[NOTICE]
Merken Sie sich dieses Verhalten von rsync. 
Im Gegensatz zu anderen Kopier-Befehlen hat der nachgestellte Schrägstrich (_trailing slash_) beim 
Quellverzeichnis bei `rsync` eine entscheidende Bedeutung.
[ENDNOTICE]


### Backup mit rsync

Lesen und verstehen Sie die Optionen **--archive, --verbose, --dry-run** der 
[rsync(1) manpage](https://manpages.debian.org/stable/rsync/rsync.1.en.html).

Lesen Sie erst die Optionen in der **Options Summary** und danach in der **Options**.

Nutzen Sie für die nächsten Aufgaben immer die Option `-v` zusätzlich.

`rsync` bietet einen entscheidenden Vorteil gegenüber herkömmlichen Kopierbefehlen: Es überprüft vor
dem Kopieren, welche Dateien sich geändert haben, und überträgt nur diese. 
Deshalb eignet sich `rsync` besonders gut für Backups, da nur geänderte Dateien kopiert werden und 
Zeit sowie Speicherplatz gespart werden.

Zur Veranschaulichung ändern wir eine Datei aus den vorhin erstellten Dateien und kopieren Sie in 
einen Ordner.

[EC] Erstellen Sie einen neuen Ordner `rsync_destination2` in Ihrem [TERMREF::Hilfsbereich].

[EC] Kopieren Sie die Dateien aus dem Ordner `rsync_copy_data` per rsync in den 
`rsync_destination2` Ordner.

[EC] Fügen Sie der Datei `rsync_copy_data/datei1` den Text `Ich wurde veraendert` 
hinzu.

Bevor wir die Datenübertragung starten, ist es sinnvoll, `rsync` im Dry-Run-Modus auszuführen, 
um zu simulieren, welche Dateien am Ende kopiert würden. Die Simulation minimiert das Risiko von 
unbeabsichtigtem Datenverlust, da man dann nochmal überprüft, was das Kommando machen würde.

[EC] Führen Sie einen `rsync`-dry-run durch, um die Dateien aus `rsync_copy_data` mit dem Zielordner 
`rsync_destination2` abzugleichen.

Jetzt wo wir gesehen haben, dass nur die veränderte Datei kopiert würde, kopieren wir diese nun.

[EC] Gleichen Sie die Dateien aus dem Ordner `rsync_copy_data` per rsync mit dem 
`rsync_destination2` Ordner ab.


### Kopieren auf entfernte Systeme

`rsync` bietet die Möglichkeit, Dateien auf einen entfernten Pfad zu kopieren, wie zum Beispiel in
die Cloud oder in Ihre Colocation.

Lesen Sie aus der **Synopsis** den Punkt **Access via remote shell** aus der 
[rsync(1) manpage](https://manpages.debian.org/stable/rsync/rsync.1.en.html).

[EC] Kopieren Sie den Ordner `rsync_copy_data` aus Ihrem [TERMREF::Hilfsbereich] in Ihren 
`home`-Ordner des Zielservers.

Die Stärke von rsync liegt darin, dass man durch einfaches Vertauschen von Quelle und Ziel die 
Dateien vom Remote-Server genauso herunterladen kann, wie man sie hochgeladen hat.

[EC] Erstellen Sie einen neuen Ordner `rsync_destination3` in Ihrem [TERMREF::Hilfsbereich].

[EC] Kopieren Sie die in der vorherigen Aufgabe kopierten Dateien vom Zielserver auf ihr System in den
Ordner `rsync_destination3` in Ihren [TERMREF::Hilfsbereich].


### Reflektion

[EQ] Wie stellt rsync sicher, dass nur geänderte Dateien erneut kopiert werden?

[EQ] Welche Unterschiede gibt es zwischen der Verwendung von rsync und anderen Kopierbefehlen wie `cp`?

[EQ] Wie könnten Sie überprüfen, ob die Synchronisation tatsächlich alle Änderungen übernommen hat?
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
[PROT::ALT:rsync.prot]
### Markdowndokument
[INCLUDE::ALT:]
[ENDINSTRUCTOR]