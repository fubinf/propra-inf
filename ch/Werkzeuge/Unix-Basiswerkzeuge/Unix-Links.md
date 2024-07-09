title: Links in Unix
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen
---
TODO_1_condric:

- Wir hatten schon besprochen dass "Lesen Sie folgenden Artikel" doof ist.
- Ich finde die Quelle schwach. Der Witz bei Hardlinks ist doch, dass man einzelne löschen kann,
  ohne dass das die anderen tangiert und _ohne_ dass eine Kopie der Datei entsteht.
  Der Artikel suggeriert hingegen fast, dass `cp` und `ln` ohne `-s` das Gleiche sei.
  Verwirrend!
- Man sollte nach Verschieben und Löschen auch noch Editieren:
  Die meisten Editoren editieren eine Datei _nicht_, sondern nennen Sie nach .bak um
  und legen eine neue an. Hingegen kann man mit `echo mehr! >>datei` eine Datei wirklich ändern.  
  Mit diesem Paar von Operationen verstehen man den Unterschied Hardlink/Softlink am eindrucksvollsten
  und versteht auch, warum niemand hardlinks benutzt: Man will über die Art der Änderungen an
  Dateien (Ändern vs. Neuschreiben) meist nicht nachdenken.

[SECTION::goal::idea]
Ich verstehe den Unterschied zwischen Hardlink und Symlink.  
Ich weiß, wie ich diese anlege.
[ENDSECTION]

[SECTION::background::default]
Links in Linux bieten eine flexible und effiziente Möglichkeit, Dateien und Verzeichnisse zu 
organisieren, Speicherplatz zu sparen und die Verwaltung von Dateien zu erleichtern.
[ENDSECTION]

[SECTION::instructions::detailed]
Lesen Sie den Beitrag [HREF::https://wiki.ubuntuusers.de/ln/] von ubuntuusers über Links durch.  
Lesen Sie insbesondere die Abschnitte **Anwendung/Terminal** und **Beispiele**.

### Erstellen von Links

Wir brauchen erstmal einen Ordner und ein paar Dateien, damit wir darauf die Links verknüpfen 
können.

- [EC] Erstellen sie zwei Dateien namens `softdata` und `harddata` unter `~/physical/`, mit
  dem Dateiinhalt "Ich bin softdata" bzw. "Ich bin harddata".

Nachdem wir jetzt den Ordner und die Dateien erstellt haben, brauchen wir noch Links auf den Dateien.

- [EC] Erstellen sie einen [TERMREF::Symlink] `~/links/symlink1` auf `~/physical/softdata` mit 
  Angabe des absoluten Pfades: `ln -s ~/physical/softdata ~/links/symlink1`
- [EC] Erstellen sie einen [TERMREF::Symlink] `~/links/symlink2` auf `~/physical/softdata` mit
  Angabe eines relativen Pfades: `ln -s ../physical/softdata ~/links/symlink2`
- [EC] Erstellen sie einen [TERMREF::Hardlink] `~/links/hardlink` aus `~/physical/harddata` .

Wir haben zwei Symlinks erstellt. Einmal mit einem relativen Pfad und mit einem expliziten Pfad.
Des Weiteren haben wir einen Hardlink erstellt.

### Verstehen der Links

- [EC] Geben Sie den Dateistrukturbaum von `~/physical` und von `~/links` mit der Option `-i` aus:
  `ls -li ~/physical`  
  `ls -li ~/links`

Die Option -i zeigt die Inodes der jeweiligen Dateien an.  
Am Anfang der Zeile der Ausgabe erscheinen Zahlen, die die Inodes repräsentieren.  
Inodes sind vereinfacht gesagt eindeutige Identifikatoren für jede Datei eines Unix-Systems.

- [EQ] Vergleichen Sie die Inodes von `hardlink` und `harddata`. 

Symlinks werden mit dem Pfeil `->` angezeigt. Der Pfeil gibt **genau** an, worauf der Link zeigt.

### Verschieben von Links

Links haben besondere Eigenschaften. Abhängig davon, ob die Links verschoben werden, die Daten verschoben 
werden, oder aber die Daten gelöscht werden. Verschieben Sie erstmal die Links und erklären Sie 
was passiert. 

- [EC] Verschieben Sie den Symlink `~/links/symlink1` nach `/tmp`.
- [EQ] Funktioniert der Symlink `symlink1` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Verschieben Sie den Symlink `~/links/symlink2` nach `/tmp`.
- [EQ] Funktioniert der Symlink `symlink2` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Verschieben Sie den Hardlink `~/links/hardlink` nach `/tmp`.
- [EQ] Funktioniert der Hardlink noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Verschieben Sie die Links `symlink1`, `symlink2`, `hardlink` zurück nach `~/links/`.

### Verschieben von Daten

Sie haben gesehen, was mit den Links passiert, wenn sie verschoben werden.
Jetzt verschieben Sie die Daten und erklären Sie was passiert.

- [EC] Verschieben Sie die Datei `~/physical/softdata` nach `/tmp/`.
- [EQ] Funktioniert der Symlink `~/links/symlink1` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Verschieben Sie die Datei `~/physical/harddata` nach `/tmp/`.
- [EQ] Funktioniert der Hardlink `~/links/hardlink` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Schieben Sie die Dateien `sofdata`, `harddata` wieder zurück nach `~/physical/`.

### Löschen von Daten

Zuguterletzt löschen wir die Daten. 

- [EC] Löschen Sie die Datei `~/physical/softdata`.
- [EQ] Funktionieren die Symlinks unter `~/links/` noch? Wenn ja, warum? Wenn nein, warum nicht?
- [EC] Löschen Sie die Datei `~/physical/harddata`.
- [EQ] Funktioniert der Hardlink `~/links/hardlink` noch? Wenn ja, warum? Wenn nein, warum nicht?

### Reflektion

- [EQ] Nennen Sie zwei Gründe, warum Symlinks sinnvoller sind.
- [EQ] Nennen sie zwei Beispiele, wo sich Hardlinks trotzdem lohnen könnten.

### Aufräumen

- [EC] Löschen Sie den Ordner `physical`.
- [EC] Löschen Sie den Ordner `links` einschließlich den Daten im Ordner.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Erwartung]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]