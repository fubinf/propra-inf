title: Links in Unix
stage: beta
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen
---

[SECTION::goal::idea]
Ich verstehe den Unterschied zwischen Hardlinks und Symlinks.  
Ich kann mit den jeweiligen Links umgehen: ich weiß wie sie erstellt, editiert und gelöscht werden.
[ENDSECTION]

[SECTION::background::default]
Links in Linux bieten eine flexible und effiziente Möglichkeit, Dateien und Verzeichnisse zu 
organisieren, Speicherplatz zu sparen und die Verwaltung von Dateien zu erleichtern.
[ENDSECTION]

[SECTION::instructions::detailed]

### Erstellen von Links

Lesen Sie die Beschreibung im obigen Teil, die **Examples** am Ende und die Option **-s** aus dem 
[GNU Manual](https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html) über Links.

Wir brauchen einen Ordner und Dateien, damit wir darauf die Links verknüpfen können.
Wir verwenden hierfür den [TERMREF::Hilfsbereich].

- [EC] Erstellen Sie einen Ordner `~/ws/tmp/physical/`.
- [EC] Erstellen Sie zwei Dateien namens `softdata` und `harddata` unter `~/ws/tmp/physical/`, mit
  dem Dateiinhalt "Ich bin softdata" bzw. "Ich bin harddata".

Nachdem wir den Ordner und die Dateien erstellt haben, brauchen wir Links auf den Dateien.

- [EC] Erstellen Sie einen Ordner `~/ws/tmp/links/`
- [EC] Erstellen Sie einen [TERMREF::Symlink] `~/ws/tmp/links/symlink1` auf `~/ws/tmp/physical/softdata` mit 
  Angabe des absoluten Pfades: `ln -s ~/ws/tmp/physical/softdata ~/ws/tmp/links/symlink1`
- [EC] Erstellen Sie einen [TERMREF::Symlink] `~/ws/tmp/links/symlink2` auf `~/ws/tmp/physical/softdata` mit
  Angabe eines relativen Pfades: `ln -s ../physical/softdata ~/ws/tmp/links/symlink2`
- [EC] Erstellen Sie einen [TERMREF::Hardlink] `~/ws/tmp/links/hardlink` auf `~/ws/tmp/physical/harddata` .

Wir haben zwei Symlinks erstellt, je einmal mit einem relativen und mit einem absoluten Pfad.
Des Weiteren haben wir einen Hardlink erstellt.

### Verstehen der Links

- [EC] Geben Sie den Dateistrukturbaum von `~/ws/tmp/physical` und von `~/ws/tmp/links` mit der Option `-i` aus:
  `ls -li ~/ws/tmp/physical`  
  `ls -li ~/ws/tmp/links`

Die Option -i zeigt die Inodes der jeweiligen Dateien an.  
Am Anfang der Zeile der Ausgabe erscheinen Zahlen, die die Inodes repräsentieren.  
Inodes sind vereinfacht gesagt eindeutige Identifikatoren für jede Datei eines Unix-Systems.

- [EQ] Vergleichen Sie die Inodes von `hardlink` und `harddata`. 

Symlinks werden mit dem Pfeil `->` angezeigt. Der Pfeil gibt **genau** an, worauf der Link zeigt.

### Verschieben von Links

Links haben besondere Eigenschaften. Abhängig davon, ob die Links verschoben werden, die Daten verschoben 
werden, oder aber die Daten gelöscht werden. Verschieben Sie erstmal die Links und erklären Sie 
was passiert. 

- [EC] Verschieben Sie den Symlink `~/ws/tmp/links/symlink1` nach `/tmp`.
- [EQ] Funktioniert der Symlink `symlink1` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Verschieben Sie den Symlink `~/ws/tmp/links/symlink2` nach `/tmp`.
- [EQ] Funktioniert der Symlink `symlink2` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Verschieben Sie den Hardlink `~/ws/tmp/links/hardlink` nach `/tmp`.
- [EQ] Funktioniert der Hardlink `hardlink` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Verschieben Sie die Links `symlink1`, `symlink2`, `hardlink` zurück nach `~/ws/tmp/links`.

### Verschieben von Daten

Sie haben gesehen, was mit den Links passiert, wenn diese verschoben werden.
Jetzt verschieben Sie die Daten und erklären Sie was passiert.

- [EC] Verschieben Sie die Datei `~/ws/tmp/physical/softdata` nach `/tmp`.
- [EQ] Funktioniert der Symlink `symlink1` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Verschieben Sie die Datei `~/ws/tmp/physical/harddata` nach `/tmp`.
- [EQ] Funktioniert der Hardlink `hardlink` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Schieben Sie die Dateien `sofdata`, `harddata` wieder zurück nach `~/ws/tmp/physical`.

### Löschen von Daten

Zuguterletzt löschen wir die Daten. 

- [EC] Löschen Sie die Datei `~/ws/tmp/physical/softdata`.
- [EQ] Funktionieren die Symlinks unter `~/ws/tmp/links` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Löschen Sie die Datei `~/ws/tmp/physical/harddata`.
- [EQ] Funktioniert der Hardlink `hardlink` noch? Wenn ja, warum? Wenn nein, warum nicht?

### Reflektion

- [EQ] Welche Art von Links würden Sie bei Desktopsymbolen nutzen? Begründen Sie.
- [EQ] Welche Art von Links würden Sie nutzen, falls Sie schneller auf einen Ordner zugreifen möchten, 
der tief im Ordnerbaum des Systems ist? Begründen Sie.
- [EQ] Welche Art von Links würden Sie bei Backups nutzen? Begründen Sie.

### Aufräumen

- [EC] Löschen Sie den Ordner `physical`.
- [EC] Löschen Sie den Ordner `links` einschließlich den Daten im Ordner.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll + Markdown]

[PROT::ALT:Unix-Links.prot]
## Markdown-Antworten
[INCLUDE::ALT:]

[ENDINSTRUCTOR]