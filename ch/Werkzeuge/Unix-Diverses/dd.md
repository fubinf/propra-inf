title: "dd - Dateien und Datenträger auf niedriger Ebene kopieren"
stage: alpha
timevalue: 2.0
difficulty: 3
assumes: redirect
explains: dd
---

[SECTION::goal::experience]
Ich verstehe, wie das Kommando `dd` auf niedriger Ebene Daten kopiert und konvertiert.
Ich kann `dd` sicher für praktische Aufgaben wie Datei-Backups und Datenträger-Imaging einsetzen.
Ich bin mir der Gefahren bewusst und weiß, welche Vorsichtsmaßnahmen zu ergreifen sind.
[ENDSECTION]


[SECTION::background::default]
`dd` kopiert Daten blockweise und kann sie dabei optional konvertieren oder transformieren.
Anders als `cp` eignet es sich besonders für diese Szenarien:

- Disk-Imaging: Komplette Festplatten oder Partitionen als Datei sichern (Backup ohne Dateisystem)
- Datenträger-Klone: Bit-für-Bit-Kopie einer Festplatte auf eine andere
- Niedriger I/O-Level: Direkte Kontrolle über Blockgröße, Skip- und Count-Parameter

Warnung: `dd` ist auch berüchtigt dafür, dass unvorsichtige Nutzer damit massive Datenmengen 
zerstört haben.
Das Kommando hat wenige Parameter, aber Inputfile `if=` und Outputfile `of=`-Optionen sind leicht 
zu verwechseln -- tückisch!
[ENDSECTION]


[SECTION::instructions::detailed]

Lesen Sie im 
[ubuntuusers dd-Artikel](https://wiki.ubuntuusers.de/dd/) 
den Abschnitt **Aufruf** und **Optionen**.
Achten Sie besonders auf die Bedeutung von `if` und `of`.

### Testumgebung vorbereiten
Bevor Sie mit echten Dateien und Datenträgern experimentieren, erstellen wir einen sicheren 
Testbereich.

Erstellen Sie das Verzeichnis `~/ws/tmp/dd` und navigieren Sie dorthin.

Erstellen Sie eine Testdatei namens `quelle.txt` mit folgendem Inhalt:

```
Dies ist eine Testdatei für dd.
Sie enthält drei Zeilen Text.
Das ist die letzte Zeile.
```


### Die Basis-Syntax

Das Grundkonzept von `dd` ist simpel: Lesen vom Input, Schreiben zum Output.

[EC] Kopieren Sie `quelle.txt` mit `dd` auf `kopie1.txt`.

[EC] Überprüfen Sie mit `diff`, dass die Kopie identisch mit dem Original ist.

<!-- time estimate: 20 min -->

### Blockgröße, Geschwindigkeit und Live-Status verstehen
Lesen Sie im 
[GNU coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html#dd-invocation)
den Abschnitt über `bs=BYTES` sowie die Dokumentation zur Option `status`.

Standardmäßig arbeitet `dd` mit einer Blockgröße von 512 Bytes. 
Bei winzigen Dateien wie `quelle.txt` ist der Performance-Unterschied alternativer Blockgrößen 
nicht messbar. 
Um den Effekt des gelernten Features sichtbar und messbar zu machen, simulieren wir eine größere 
"Festplatte" mit viel leerem Speicherplatz (Nullen) und einem belegten Datenbereich.

[NOTICE]
Für die nächste Aufgabe brauchen Sie freien Speicherplatz von 10000 MB. 
Falls Sie nicht ausreichend freien Speicherplatz haben, dann müssen Sie in der nächsten Aufgabe 
die entsprechenden `count` und `seek` Optionen entsprechend Ihres Speicherplatzes anpassen.
[ENDNOTICE]

[EC] Erstellen Sie, falls möglich, eine 10010 MB große Test-Datei `testdisk.img`, 
bestehend aus 10000 MB Nullen und 10 MB Zufallsdaten:

```
dd if=/dev/zero of=testdisk.img bs=1M count=10000
dd if=/dev/urandom of=testdisk.img bs=1M count=10 seek=10000
```

[EC] Kopieren Sie `testdisk.img` zu `testdisk_slow.img` mit der Standard-Blockgröße von 512 Bytes. 
Nutzen Sie das Unix-Kommando `time` direkt vor dem `dd`-Aufruf, um die reale Zeitdauer zu messen.

[EC] Kopieren Sie `testdisk.img` zu `testdisk_fast.img` mit einer optimierten Blockgröße von `4M`. 
Messen Sie auch hier die Zeit mit `time`.

[EQ] Welchen Unterschied in der Ausführungszeit beobachten Sie?

Jedes Mal, wenn `dd` Daten liest oder schreibt, muss es einen Systemaufruf (`read()` / `write()`) 
an den Linux-Kernel richten. 
Ein Systemaufruf erfordert einen teuren Kontextwechsel zwischen dem User-Space und dem Kernel-Space.

* Bei `bs=512` und einer 10.010 MB großen Datei muss das System ca. 41.000.960 Systemaufrufe durchführen.
* Bei `bs=4M` genügen dafür lediglich ca. 5.006 Systemaufrufe.

Der immense Overhead der CPU-Kontextwechsel fällt bei der optimierten Blockgröße weg, 
wodurch die Festplatte bzw. SSD mit ihrer maximalen Input/Output-Geschwindigkeit arbeiten kann.

Bei großen Datenträgern laufen Kopiervorgänge oft minutenlang im Hintergrund. Ohne Rückmeldung 
bleibt unklar, ob das System hängt.

[EC] Kopieren Sie `testdisk.img` erneut zu `testdisk_progress.img` mit `bs=4M`, aktivieren Sie 
diesmal jedoch die Fortschrittsanzeige mit `status=progress`.

[EQ] Welche Metriken (z. B. übertragene Bytes, verstrichene Zeit, Transferrate) gibt 
`status=progress` während des laufenden Vorgangs aus? 

[EQ] Unterscheidet sich diese Anzeige von der finalen Zusammenfassung am Ende?

<!-- time estimate: 40 min -->


### Nur einen Teil einer Datei kopieren: `count` und `skip`
Lesen Sie in der 
[dd(1) man page](https://man7.org/linux/man-pages/man1/dd.1.html)
die Erklärungen zu `skip` und `count`.
Achten Sie darauf, wie diese Parameter mit der Blockgröße `bs` zusammenhängen.

Ein praktisches, realistisches Szenario sind **MBR-Backups**.
Der Master Boot Record (MBR) einer Festplatte ist der allererste Block (512 Bytes) und enthält 
den Bootloader und die Partitionstabelle.
Sysadmins sichern ihn regelmäßig, um sich nach Fehlern oder Ausfällen schnell erholen zu können.

[EC] Erstellen Sie zuerst eine separate, kleine Testdatei `mini_festplatte.img` (5 KB) mit rein 
zufälligen Daten:

```
dd if=/dev/urandom of=mini_festplatte.img bs=512 count=10
```

[EC] Extrahieren Sie nun präzise nur die **ersten 512 Bytes** (den MBR) aus `mini_festplatte.img` 
in die Datei `mbr_backup.img`.

[EC] Überprüfen Sie die exakte Dateigröße von `mbr_backup.img`.

[EQ] Warum haben wir für dieses Extraktionsszenario exakt `count=1` und `bs=512` gewählt?

<!-- time estimate: 20 min -->


### Praktisches Szenario: Ein komprimiertes Datei-Backup
Lesen Sie im 
[Arch Linux Wiki – dd](https://wiki.archlinux.org/title/Dd) 
den Abschnitt **"Create disk image"**.
Verstehen Sie, wie `dd` mit Pipes (`|`) kombiniert wird und wie Kompression dabei hilft,
Backups kleiner zu machen.

[EC] Erstellen Sie ein komprimiertes Backup von `testdisk.img`. 
Leiten Sie dazu die Standardausgabe von `dd` per Pipe (`|`) direkt an das Kompressionstool `gzip` 
weiter und schreiben Sie das Ergebnis in die Datei `testdisk.img.gz`.

[EC] Überprüfen Sie mittels `ls -lh`, wie viel Speicherplatz das komprimierte Backup im direkten 
Vergleich zur Originaldatei einnimmt.

[EQ] Wie viel Speicherplatz hat die Kompression prozentual eingespart? 

[EQ] Warum ist das Ergebnis bei einem ungenutzten Datenträger-Abbild so drastisch, 
während es bei reinen Zufallsdaten fehlschlagen würde?

<!-- time estimate: 40 min -->


[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll und Markdown-Dokument]
[INCLUDE::ALT:]
## Kommandoprotokoll
[PROT::ALT:dd.prot]
[ENDINSTRUCTOR]