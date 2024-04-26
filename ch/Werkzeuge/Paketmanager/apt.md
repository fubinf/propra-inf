title: APT Paketverwaltung
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe wie `apt` funktioniert und wie ich es anwenden kann
[ENDSECTION]

[SECTION::background::default]
`apt` ist bei Debian Systemen das standardmäßige Paketverwaltungssystem. Mit `apt` werden Pakete 
beispielsweise installiert, deinstalliert und aktualisiert.
[ENDSECTION]

[SECTION::instructions::detailed]
Lesen Sie diesen [Beitrag](https://wiki.ubuntuusers.de/apt/apt/) von ubuntuusers, 
insbesondere die Kapitel **Pakete verwalten** und **Suchen/Durchsuchen**.

### System aktualisieren

Systeme sollten immer aktuell sein, also fangen wir auch mit einem aktuellen System an.

- [EC] Aktualisieren Sie ihr System.

### Pakete installieren
In dieser Aufgabe nehmen wir als Beispiel den `midnight commadner`. Es ist ein textbasierter Commander.

- [EC] Suchen Sie mit `apt` nach dem Begriff `midnight commander`.
- [EC] Geben Sie die Informationen des Paketes von `midnight commander` aus.
- [EC] Installieren Sie den `midnight commander`.
- [EC] Geben Sie die Liste von installierten Paketen aus und stellen Sie sicher, dass der `midnight commander` installiert wurde.

### Pakete deinstallieren
Bei einer Aktualisierung ihres Systems werden die alten Pakete nicht gelöscht, sondern bleiben auf ihrem System liegen.

- [EC] Finden Sie im [Beitrag](https://wiki.ubuntuusers.de/apt/apt/) das Kommando, um veraltete 
Pakete von Ihrem System zu löschen und führen Sie es aus.

Pakete können manuell deinstalliert werden. Es gibt zwei verschieden Kommandos dafür.

- [EQ] Erklären Sie den Unterschied zwischen den Optionen `remove` und `purge`.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]
