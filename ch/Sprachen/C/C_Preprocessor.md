title: "C Präprozessor"
stage: draft
timevalue: 1.5
difficulty: 3
assumes: C_CompilerAssemblerLinker
---
[SECTION::goal::idea]
Ich verstehe was der Präprozessor ist.
[ENDSECTION]

[SECTION::background::default]
Wie in [PARTREF::C_CompilerAssemblerLinker] erwähnt dreht es sich hier gänzlich
um den Präprozessor.

Der C Präprozessor ist ein elementarer Bestandteil der C-Sprache, denn ohne den
Präprozessor wäre es doch recht mühsam, Programme zu entwickeln. Die
Hauptaufgaben sind:

- Einbinden von Header-Dateien
- Konditionale Ersetzungen
- Makros

Zu beachten ist: Der Präprozessor ist Teil der Übersetzung Ihres Programmes.
Die Funktionsweise des Präprozessors ist vergleichbar einer Textersetzung,
was im Umkehrschluss bedeutet, dass Sie nach dem Präprozessor-Schritt keine
Anzeichen der von Ihnen eingeführten Makroname, `#includes` oder Konditionalen
mehr finden können.
[ENDSECTION]

[SECTION::instructions::detailed]
### Einbinden von Header-Dateien
#### Was sind Header-Dateien
TODO:
#### Aufgaben
TODO:

### Konditionale Ersetzung
TODO:

### Makros
TODO:
- Sondermakros
  - `error`
  - `#`
  - `##`
  - `__FILE__`, `__LINE__`
[ENDSECTION]