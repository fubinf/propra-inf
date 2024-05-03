title: Links in Unix
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe den Unterschied zwischen Hardlink und Symlink.  
Ich weiß, wie ich diese anlege.
[ENDSECTION]

[SECTION::background::default]
Links in Linux bieten eine flexible und effiziente Möglichkeit, Dateien und Verzeichnisse zu 
organisieren, Speicherplatz zu sparen und die Verwaltung von Dateien zu erleichtern.
[ENDSECTION]

[SECTION::instructions::detailed]
Lesen Sie sich den [Beitrag](https://wiki.ubuntuusers.de/ln/) von ubuntuusers über Links durch.  
Lesen Sie insbesondere die Abschnitte **Anwendung/Terminal** und **Beispiele**.

### Erstellen von Links

- [EC] Erstellen sie zwei Dateien namens `softdata` und `harddata` unter `~/physical/`, und 
schreiben Sie jeweils softdata und harddata in die Datei.
- [EC] Erstellen sie einen [TERMREF::Symlink] von `softdata` unter `~/symlinks/symlink`.
- [EC] erstellen sie einen [TERMREF::Hardlink] von `harddata` unter `~/symlinks/hardlink`.
fddsaf

### Verschieben von Links und Dateien

- [EC] Was passiert mit dem [TERMREF::Symlink] `~/links/symlink`, wenn Sie es nach `/tmp/` verschieben.
- [EC] Was passiert mit dem [TERMREF::Hardlink] `~/links/hardlink`, wenn Sie es nach `/tmp/` verschieben.
- [EC] Schieben Sie wieder beide Links zurück nach `~/links/`.
- [EC] Was passiert mit dem [TERMREF::Symlink] `~/links/symlink`, wenn Sie die Datei `~/physical/softdata` nach `/tmp/` verschieben.
- [EC] Was passiert mit dem [TERMREF::Symlink] `~/links/harddata`, wenn Sie die Datei `~/physical/harddata` nach `/tmp/` verschieben.

### Löschen von Links

- [EC] Was passiert mit dem [TERMREF::Symlink], wenn sie die Datei `~/physical/softdata` löschen.
- [EC] Was passiert mit dem [TERMREF::Hardlink], wenn sie die Datei `~/physical/harddata` löschen.

### Reflektion

- [EQ] Nennen Sie drei Gründe, warum [TERMREF::Symlinks] sinnvoller sind.
- [EQ] Nennen sie zwei Beispiele, wo sich [TERMREF::Hardlinks] lohnen könnten.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Erwartung]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
Bei den Symlinks darauf achten, dass der ganze Pfad angegeben wird.

[ENDINSTRUCTOR]