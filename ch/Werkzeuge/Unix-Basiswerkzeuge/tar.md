title: tar-split - Archive aufteilen und wieder zusammenfügen
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen, redirect
---

[SECTION::goal::idea]
Ich weiß was `tar` ist und wie ich damit Archive erstellen, anzeigen und entpacken kann.
Ich kenne den Nutzen von Kompression und kann große Archive mit `split` aufteilen und wieder zusammenfügen.
[ENDSECTION]


[SECTION::background::default]
`tar` (kurz für “tape archiver”) erstellt und liest Archive, indem mehrere Dateien zu einer Archivdatei
zusammengefasst werden. 
Früher diente es zur Bandsicherung (und macht deshalb im Gegensatz zu z.B. `zip` seine
Schreibzugriffe ausschließlich sequenziell), heute wird es stark zur Softwareverteilung
und gelegentlich für Backups und Projektarchivierung eingesetzt. 
[ENDSECTION]


[SECTION::instructions::detailed]

### Testdateien erstellen

Erstellen Sie in ihrem [TERMREF::Hilfsbereich] einen neuen Ordner `tar`.

Wechseln Sie in den neuen Ordner.

[WARNING]
Das Skript erstellt 100 Dateien im gerade geöffneten Ordner.
[ENDWARNING]

[EC] Führen Sie diesen Befehl aus: 
`for i in {001..100}; do echo "Ich bin der Inhalt der Datei $i" > "tar_datei_$i"; done`


### `tar`-Archive erstellen

`tar` fasst mehrere Dateien und Verzeichnisse in einer einzigen Archivdatei zusammen. 
Lesen Sie den Abschnitt **Syntax** und verstehen Sie insbesondere die **Optionen c,f,J,z** der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/).

Verstehen Sie im Abschnitt **Beispiele** den Teil "Anlegen" der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/).

[EC] Erstellen Sie ein `.tar`-Archiv `meinarchiv.tar` mit den gerade erstellten 100 Dateien.

Neben dem Erstellen von Archiven kann `tar` Archive auch komprimieren. 
Es stehen mehrere Algorithmen zur Verfügung, wir beschränken uns hier auf zwei.

Angenommen Sie möchten 100 Dateien per Mail versenden.
Ihr Mailprogramm erlaubt es Ihnen nicht, weil die Daten zu groß sind. 
Mit einem komprimierten `tar`-Archiv können Sie alle Dateien in einer komprimierten Datei bündeln 
und so einfacher verschicken.

Die Dateiendung eines `tar`-Archivs ist von `tar` nicht vorgegeben, unterliegt faktisch aber
einer sehr einheitlichen Konvention: 
`.tar` sind unkomprimierte Archive, 
`.tar.gz` sind mit `gzip` komprimiert,
`.tar.xz` sind mit `xz` komprimiert.
`xz` komprimiert etwas stärker, braucht aber _sehr_ viel länger und ist weniger verbreitet.

[EC] Erstellen Sie ein mit `gzip` komprimiertes Archiv `meinarchiv.tar.gz` mit den 100 Dateien.

[EC] Erstellen Sie ein mit `xz` komprimiertes Archiv `meinarchiv.tar.xz` mit den 100 Dateien.

[EQ] Vergleichen Sie die Größen der drei Archive.
(Unsere Dateien ähneln sich sehr stark, deshalb lassen sie sich ungewöhnlich gut komprimieren.)


### `tar`-Archive anzeigen

Angenommen Sie müssen ein Softwarepaket installieren.
Dieses haben Sie als `tar.gz` heruntergeladen.
Bevor Sie es installieren, möchten Sie nachschauen, wie die Datenstruktur im Archiv aufgebaut ist, 
damit Sie entscheiden können, wo Sie es installieren möchten.

Lesen und verstehen Sie die **Optionen t,v** der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/).

Verstehen Sie im Abschnitt **Beispiele** den Teil "Anzeigen" der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/).

[EC] Zeigen Sie den Inhalt des erstellten `gzip`-komprimierten Archivs an.
Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.

[EC] Zeigen Sie den Inhalt des erstellten `gzip`-komprimierten Archivs mit mehr Details an.
Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.


### `tar`-Archive auspacken

Sie haben sich das `tar`-Archiv angeschaut und möchten es jetzt entpacken, damit Sie es später 
installieren können, falls nötig.

Lesen und verstehen Sie die **Optionen x,C** der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/).

Verstehen Sie im Abschnitt **Beispiele** den Teil "Extrahieren" der 
[ubuntuusers tar-Seite](https://wiki.ubuntuusers.de/tar/) an.

[EC] Erstellen Sie einen neuen Ordner im `tar`-Ordner namens, `entpackt`.

[EC] Entpacken Sie das mit `xz` komprimierte Archiv in den Ordner `entpackt` ohne den Ordner zu 
    wechseln.


### `tar`-Archive aufteilen ("splitten")

Sie haben nun ein komprimiertes Archiv erstellt, aber Ihr Mailprogramm sagt immer noch, 
dass die Daten zu groß sind.
Jetzt wollen Sie das Archiv aufteilen, damit Sie es in einzelnen Mails verschicken können.

Lesen und verstehen Sie die Abschnitte **Benutzung, Beispiele** und insbesondere die 
**Optionen b,d** der 
[ubuntuusers split-Seite](https://wiki.ubuntuusers.de/split/).

[EC] Erstellen Sie einen neuen Ordner `split` im `tar`-Ordner.

[EC] Kopieren Sie das `.tar`-Archiv in den Ordner `split`.

[EC] Wechseln Sie in den Ordner `split`.

[EC] Teilen Sie das `.tar`-Archiv in 5 gleich große Archive auf.
Vergeben Sie den Namen `split_meinarchiv.tar.` (mit Punkt am Ende).


### Aufgeteilte `tar`-Archive wieder zusammenfügen

Sie haben auf die Mail eine Antwort aus mehreren Emails mit gesplitteten Archivteilen zurückbekommen.
Damit Sie das aufgeteilte Archiv wieder entpacken können, müssen Sie die Teile wieder zusammenfügen.

Lesen und verstehen Sie den Abschnitt **Zusammenführen** der 
[ubuntuusers split-Seite](https://wiki.ubuntuusers.de/split/).

[EC] Fügen Sie das `tar`-Archiv, welches Sie in 5 gleich große Teile getrennt haben, wieder zusammen.
Benennen Sie das Resultat `cat_meinarchiv.tar`.

[EC] Prüfen Sie die Funktionstüchtigkeit des wieder zusammengefügten Archivs, indem Sie die Dateien von `cat_meinarchiv.tar`auflisten.
Kürzen Sie für das Kommandoprotokoll mit `head -10` ab.

[EC] Listen Sie den Ordner `split` mit mehr Details auf.


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
[PROT::ALT:tar.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
