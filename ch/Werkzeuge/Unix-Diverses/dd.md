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
`dd` ist ein Unix-Klassiker mit einer Mission: Daten blockweise zu kopieren und dabei optional zu 
konvertieren oder zu transformieren.
Während `cp` für normale Dateien ausreicht, glänzt `dd` bei vier Szenarien:

- Disk-Imaging: Komplette Festplatten oder Partitionen als Datei sichern (backup ohne 
  Dateisystem)
- Datenträger-Klone: Bit-für-Bit-Kopie einer Festplatte auf eine andere
- Bootfähige USB-Sticks: ISO-Dateien auf USB-Laufwerke schreiben
- Niedriger I/O-Level: Direkte Kontrolle über Blockgröße, Skip- und Count-Parameter

Warnung: `dd` ist auch berüchtigt dafür, dass unvorsichtige Nutzer damit massive Datenmengen 
zerstört haben.
Das Kommando hat wenige Parameter, aber Input `if=` und Output `of=`-Optionen sind leicht 
zu verwechseln.
[ENDSECTION]


[SECTION::instructions::detailed]

Lesen Sie im [ubuntuusers dd-Artikel](https://wiki.ubuntuusers.de/dd/) den Abschnitt 
**Aufruf** und **Optionen**.
Achten Sie besonders auf die Bedeutung von `if` und `of`.

### Testumgebung vorbereiten

Bevor Sie mit echten Dateien und Datenträgern experimentieren, erstellen wir einen sicheren 
Testbereich.

Erstellen Sie das Verzeichnis `~/ws/tmp/dd` und navigieren Sie dorthin.

Erstellen Sie eine Testdatei namens `quelle.txt` mit folgendem Inhalt: (ohne Zeilennummern)
```
Dies ist eine Testdatei für dd.
Sie enthält drei Zeilen Text.
Das ist die letzte Zeile.
```

[EC] Geben Sie die Dateigröße von `quelle.txt` wieder.


### Die Basis-Syntax

Das Grundkonzept von `dd` ist simpel: Lesen vom Input, Schreiben zum Output.

[EC] Kopieren Sie `quelle.txt` mit `dd` auf `kopie1.txt`.

[EC] Überprüfen Sie mit `diff`, dass die Kopie identisch mit dem Original ist.


### Blockgröße und Geschwindigkeit verstehen

Lesen Sie im [GNU coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html#dd-invocation)
den Abschnitt über `bs=BYTES`.

Standardmäßig arbeitet `dd` mit einer Blockgröße von **512 Bytes**.
Das ist sicher, aber sehr langsam.

Größere Blöcke sind schneller (weniger Systemaufrufe), verbrauchen aber mehr RAM-Speicher.
Für Experimente: Probieren Sie Werte zwischen 1K und 64M, je nach verfügbarem RAM.
Das gängigste Best-Practice: `64M` für Backup/Imaging, `4K` für Standard-Dateikopien.

[EC] Kopieren Sie `quelle.txt` mit einer Blockgröße von 4 Kilobytes zu `kopie2.txt`.

[EQ] Wie viel schneller könnte diese Kopie theoretisch sein als die Standard-Kopie?


### Nur einen Teil einer Datei kopieren: count und skip

Lesen Sie in der [dd(1) man page](https://man7.org/linux/man-pages/man1/dd.1.html)
die Erklärungen zu `skip` und `count`.
Achten Sie darauf, wie diese Parameter mit der Blockgröße `bs` zusammenhängen.

Ein praktisches, realistisches Szenario sind **MBR-Backups**.
Die Master Boot Record (MBR) einer Festplatte ist der allererste Block (512 Bytes) und enthält 
den Bootloader und die Partitionstabelle.
Sysadmins sichern sie regelmäßig, um schnell von Fehlern oder Ausfällen zu regenerieren.
Mit `count=1 bs=512` extrahieren Sie genau diese 512 Bytes aus einer Festplatte oder eines Images:

[EC] Erstellen Sie zuerst eine Testdatei `festplatte.img` mit zufälligen Daten:
```
dd if=/dev/urandom of=festplatte.img bs=512 count=10 status=progress
```

Dies simuliert eine kleine 5-KB-„Festplatte".

[EC] Extrahieren Sie nur die **ersten 512 Bytes** (den MBR) in die Datei `mbr_backup.img`.

[EC] Überprüfen Sie die Größe von `mbr_backup.img`.

[EQ] Warum haben wir exakt `count=1` und `bs=512` gewählt?


### Status und Feedback während der Kopie

Lesen Sie im [GNU coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html#dd-invocation)
die Dokumentation zur `status` Option.
Verstehen Sie, welche Informationen die verschiedenen Status-Level ausgeben.

Bei großen Dateien, die mit mit `dd` kopiert werden, wartet man lange ohne Rückmeldung.

[EC] Kopieren Sie `quelle.txt` in die Datei `kopie3.txt` noch einmal mit Fortschrittsanzeige.

[EQ] Welche Informationen zeigt `status=progress` an?


### Praktisches Szenario: Ein Datei-Backup

Lesen Sie im [Arch Linux Wiki – dd](https://wiki.archlinux.org/title/Dd) den Abschnitt
**"Create disk image"**.
Verstehen Sie, wie `dd` mit Pipes (`|`) kombiniert wird und wie Kompression dabei hilft,
Backups kleiner zu machen.

Stellen Sie sich vor, Sie möchten eine wichtige Datei regelmäßig sichern.
Ein häufiges Backup-Szenario ist das Speichern auf einen anderen Datenträger.

Wir simulieren das, indem wir eine „Festplatte-Image"-Datei erstellen.

[EC] Erstellen Sie eine große Test-Datei mit zufälligen Daten (1000 MB):
```
dd if=/dev/urandom of=testdisk.img bs=1M count=1000 status=progress
```

Dies erzeugt eine 1000-MB-Datei basierend auf Zufallsdaten (ähnlich wie ein Disk-Image).

[EC] Erstellen Sie ein komprimiertes Backup dieser „Festplatte". Nutzen Sie `gzip > testdisk.img.gz`.

[EC] Überprüfen Sie, wie viel Speicher das komprimierte Backup braucht.

[EQ] Wie viel Speicher hat die Kompression eingespart und warum?

[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll und Markdown-Dokument]
[INCLUDE::ALT:]
[PROT::ALT:dd.prot]
[ENDINSTRUCTOR]
