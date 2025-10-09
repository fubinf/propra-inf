title: tar - das Archivierungsprogramm
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen, redirect
---

[SECTION::goal::idea]
Ich weiß was `tar` ist und wie ich damit Archive erstellen, anzeigen und entpacken kann.
Ich kenne den Nutzen von Kompression und kann große Archive mit `split` teilen und wieder zusammenfügen.
[ENDSECTION]


[SECTION::background::default]
`tar` (kurz für “tape archiver”) erstellt und liest Archive, indem mehrere Dateien zu einer Archivdatei
zusammengefasst werden. Früher diente es zur Bandsicherung, heute wird es für Backups, Softwareverteilung
und Projektarchivierung eingesetzt. 
[ENDSECTION]


[SECTION::instructions::detailed]

### Testdateien erstellen

```bash
#!/bin/bash

# 5 Dateien erstellen
for i in {001..100}; do
    echo "Ich bin der Inhalt der Datei $i" > "tar_datei_$i"
done

echo "$i Dateien wurden erstellt."c
```

Erstellen Sie in ihrem [TERMREF::Hilfsbereich] einen neuen Ordner `tar`.

Wechseln Sie in den neuen Ordner.

Erstellen Sie eine neue Datei `tar_create_data.sh` mit oberem Inhalt, im neu erstellten Ordner.

[WARNING]
Das Skript erstellt 100 Dateien im gerade geöffneten Ordner.
[ENDWARNING]

[EC] Führen Sie das Skript aus: `bash tar_create_data.sh`


### `tar`-Archive erstellen

`tar` fasst mehrere Dateien und Verzeichnisse in einer einzigen Archivdatei zusammen. 
Ursprünglich wurde `tar` entwickelt, um Daten auf Magnetbändern zu sichern.
Heute ist `tar` der Standard für Backups, Softwarepakete und den Austausch von Projekten. 

Lesen Sie den Abschnitt **Syntax** und verstehen Sie insbesondere die **Optionen c,f,J,z** der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/).

Schauen Sie sich die **Beispiele** zum **Anlegen** von Archiven der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/) an.

[EC] Erstellen Sie ein `.tar`-Archiv mit den gerade 100 erstellten Dateien.

Neben dem Erstellen von Archiven, kann `tar` Archive auch komprimieren. 
Es stehen mehrere Algorithmen zur Verfügung, wir beschränken uns hier auf zwei.

Angenommen Sie möchten 100 Dateien per Mail versenden.
Ihr Mailprogramm erlaubt es Ihnen nicht, weil die Daten zu groß sind. 
Mit einem komprimierten `tar`-Archiv können Sie alle Dateien in einer komprimierten Datei bündeln 
und so einfacher verschicken.

Die Dateiendung eines `tar`-Archivs ist nicht zwingend, aber praktisch: 
Konventionelle Endungen wie `.tar`, `.tar.gz` oder `.tar.xz` machen sofort erkennbar, welcher 
Komprimierungsalgorithmus verwendet wurde.

[EC] Erstellen Sie ein mit `gzip` komprimiertes `.tar.gz`-Archiv mit den 100 Dateien.

[EC] Erstellen Sie ein mit `xz` komprimiertes `tar.xz`-Archiv mit den 100 Dateien.

[EQ] Vergleichen Sie die Größen der drei Archive.


### `tar`-Archive anzeigen

Angenommen Sie müssen ein Programm installieren.
Dieses haben Sie als `tar.gz` heruntergeladen.
Bevor Sie es installieren, möchten Sie nachschauen, wie die Datenstruktur im Archiv aufgebaut ist, 
damit Sie entscheiden können, wo Sie es installieren möchten.

Lesen und verstehen Sie die **Optionen t,v** der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/).

Schauen Sie sich die **Beispiele** zum **Anzeigen** von Archiven der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/) an.

[EC] Schauen Sie sich den Inhalt des erstellten `gzip`-komprimierten Archivs an.
    Kürzen Sie mit `head -10` für das Kommandoprotokoll ab.

[EC] Schauen Sie sich den Inhalt des erstellten `gzip`-komprimierten Archivs mit mehr Details an.
    Kürzen Sie mit `head -10` für das Kommandoprotokoll ab.


### `tar`-Archive auspacken

Sie haben sich das `tar`-Archiv angeschaut und möchten es jetzt entpacken, damit Sie es später 
installieren können, falls nötig.

Lesen und verstehen Sie die **Optionen x,C** der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/).

Schauen Sie sich die **Beispiele** zum **Extrahieren** von Archiven der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/) an.

[EC] Erstellen Sie einen neuen Ordner im `tar`-Ordner namens, `entpackt`.

[EC] Entpacken Sie das mit `xz` komprimierte Archiv in den Ordner `entpackt` ohne den Ordner zu 
    wechseln.


### `tar`-Archive splitten und zusammenfügen

Sie haben ein `tar`-Archiv erstellt und Ihr Mailprogramm sagt immer noch, dass die Daten zu groß sind.
Auch nachdem Sie sie komprimiert haben.
Jetzt wollen Sie das Archiv aufteilen, damit Sie es in einzelnen Mails verschicken können.

Lesen und verstehen Sie die Abschnitte **Benutzung, Beispiele** und insbesondere die 
**Optionen b,l,d** der 
[ubuntuusers split-Seite](https://wiki.ubuntuusers.de/split/).

[EC] Erstellen Sie einen neuen Ordner `split` im `tar`-Ordner.

[EC] Kopieren Sie das `.tar`-Archiv in den Ordner `split`.

[EC] Wechseln Sie in den Ordner `split`.

[EC] Teilen Sie das `.tar`-Archiv in 5 gleich große `tar`-Archive auf. 
    Nummerieren Sie die Archive und vergeben Sie den Namen `split_tar.tar.`.

[EC] Teilen Sie das `.tar`-Archiv mit einem Zeilenabstand von 40 auf. 
    Benennen Sie die neuen Archive `line_split_tar.tar`.

Sie haben auf die Mail eine Antwort mit gesplitteten Archiven zurückbekommen.
Damit Sie das aufgeteilte Archiv wieder entpacken können, müssen Sie sie wieder zusammenfügen.

Lesen und verstehen Sie den Abschnitt **Zusammenführen** der 
[ubuntuusers split-Seite](https://wiki.ubuntuusers.de/split/).

[EC] Fügen Sie das `tar`-Archiv, welches in 5 gleich große Teile getrennt wurde, wieder zusammen. 
    Benennen Sie es `cat_tar.tar`

[EC] Listen Sie den Ordner `split` in Listenform auf.


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
[PROT::ALT:tar.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
