title: Links in Unix
stage: draft
timevalue: 1.0
difficulty: 2
---

TODO_1_condric:

- Bitte ein präzises mentales Modell herstellen: Von "die Daten" zu sprechen ist viel zu unscharf.
  Wir brauchen erstens inodes und dahinterliegende Daten als Konzept und zweitens Verzeichniseinträge.
- Die Aufgabe sollte für symlinks unbedingt sowohl mit einem absoluten als auch mit einem
  relativen Pfad arbeiten und einen Schritt beinhalten, wo der ganze Baum verlegt wird
  und dann der relative Link intakt bleibt (während in der jetzigen der absolute intakt bleibt).
- Und bitte eine Musterlösung formulieren.

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

Wir brauchen erstmal einen Ordner und ein paar Dateien, damit wir darauf die Links verknüpfen 
können.

- [EC] Erstellen sie zwei Dateien namens `softdata` und `harddata` unter `~/physical/`, mit
  dem Dateiinhalt "Ich bin softdata" bzw. "Ich bin harddata".

Nachdem wir jetzt den Ordner und die Daten haben, brauchen wir noch die Links auf die Daten.

- [EC] Erstellen sie einen [TERMREF::Symlink] von `softdata` unter `~/symlinks/symlink`.
- [EC] erstellen sie einen [TERMREF::Hardlink] von `harddata` unter `~/symlinks/hardlink`.

### Verschieben von Links

Links haben besondere Eigenschaften, wenn die Links verschoben werden, die Daten verschoben 
werden, oder aber die Daten gelöscht werden. Verschieben Sie erstmal die Links und erklären Sie 
was passiert. 

- [EC] Was passiert mit dem [TERMREF::Symlink] `~/links/symlink`, wenn Sie es nach `/tmp/` 
   verschieben.
- [EC] Was passiert mit dem [TERMREF::Hardlink] `~/links/hardlink`, wenn Sie es nach `/tmp/` 
   verschieben.
- [EC] Schieben Sie wieder beide Links zurück nach `~/links/`.

### Verschieben von Dateien

- [EC] Was passiert mit dem [TERMREF::Symlink] `~/links/symlink`, wenn Sie die Datei 
   `~/physical/softdata` nach `/tmp/` verschieben.
- [EC] Was passiert mit dem [TERMREF::Symlink] `~/links/harddata`, wenn Sie die Datei 
   `~/physical/harddata` nach `/tmp/` verschieben.
- [EC] Schieben Sie die Dateien wieder zurück nach `~/physical/`.

### Löschen von Links

- [EC] Was passiert mit dem [TERMREF::Symlink], wenn sie die Datei `~/physical/softdata` löschen.
- [EC] Was passiert mit dem [TERMREF::Hardlink], wenn sie die Datei `~/physical/harddata` löschen.

### Reflektion

- [EQ] Nennen Sie zwei Gründe, warum [TERMREF::Symlinks] sinnvoller sind.
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