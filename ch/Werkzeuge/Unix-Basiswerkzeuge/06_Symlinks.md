title: Symlinks
stage: alpha
timevalue: 1.0
difficulty: 2
---

TODO_1_condric:

- Kaum jemand sagt Softlink, Symlink ist weitaus gebräuchlicher.
- Die beiden Glossareinträge versteht niemand, der es nicht schon vorher weiß.
  Da muss ein guter Quellenverweis dazu.
- Wer es schon vorher weiß, erkennt, dass die Beschreibung von Hardlink falsch ist:
  Das sind keine "alternativen" Einträge. Jeder Eintrag ist ein Hardlink; alle gleichberechtigt.
- Die ubuntuusers-Quelle sagt das auch so.
- Hardlinks sind auch problematisch, weil man bei Änderungen an Dateien meist nicht so genau weiß,
  ob die vorhandene Datei modifiziert wird oder eine ganz frische geschrieben.
  Aber dann bekommt man eine völlig andere Semantik.
- Die Aufgabe sollte klarer stellen, dass man Hardlinks selten benutzt, sondern nur unbedingt
  wissen muss, was das ist -- und sei es, um besser zu verstehen, was Symlinks sind.


[SECTION::goal::idea]
Ich verstehe den Unterschied zwischen Hard- und [TERMREF::Softlink]. Ich weiß, wie ich diese anlege.
[ENDSECTION]

[SECTION::background::default]
Links in Linux bieten eine flexible und effiziente Möglichkeit, Dateien und Verzeichnisse zu 
organisieren, Speicherplatz zu sparen und die Verwaltung von Dateien zu erleichtern.
[ENDSECTION]

[SECTION::instructions::detailed]
Lesen sie sich den (Beitrag)[https://wiki.ubuntuusers.de/ln/] von ubuntuusers über Links durch

### Erstellen von Links
- [EC] Erstellen sie zwei Dateien namens `softdata` und `harddata` unter `~/physical/`, und 
schreiben Sie jeweils softdata und harddata in die Datei.
- [EC] Erstellen sie einen [TERMREF::Softlink] der ersten Datei unter ~/symlinks/softlink.
- [EC] erstellen sie einen [TERMREF::Hardlink] der zweiten datei unter ~/symlinks/hardlink.

### Verschieben von Links und Dateien
- [EC] Was passiert mit dem [TERMREF::Softlink] `~/symlinks/softlink`, wenn Sie es nach /tmp/ verschieben.
- [EC] Was passiert mit dem [TERMREF::Hardlink] `~/symlinks/hardlink`, wenn Sie es nach /tmp/ verschieben.
- [EC] Schieben Sie wieder beide Links zurück nach `~/symlinks/`.
- [EC] Was passiert mit dem [TERMREF::Softlink] `~/symlinks/softlink`, wenn Sie die Datei `~/physical/softdata` nach `/tmp/` verschieben.
- [EC] Was passiert mit dem [TERMREF::Softlink] `~/symlinks/harddata`, wenn Sie die Datei `~/physical/harddata` nach `/tmp/` verschieben.

### Löschen von Links
- [EC] Was passiert mit dem [TERMREF::Softlink], wenn sie die Datei `~/physical/softdata` löschen.
- [EC] Was passiert mit dem [TERMREF::Hardlink], wenn sie die Datei `~/physical/harddata` löschen.

### Reflektion
- [EQ] Nennen sie jeweils zwei Beispiele, wo `softlinks` beziehungsweise `hardlinks` sinnvoll sind

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::heading]
Bei den Softlinks darauf achten, dass der ganze Pfad angegeben wird.
[ENDINSTRUCTOR]