title: APT Paketverwaltung
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea,trial]
Ich kann `apt` zur Verwaltung von Debian-Softwarepaketen anwenden.
[ENDSECTION]

[SECTION::background::default]
`apt` ist bei Debian Systemen das standardmäßige Paketverwaltungssystem. Mit `apt` werden Pakete 
gesucht, installiert, deinstalliert und aktualisiert.
[ENDSECTION]

[SECTION::instructions::detailed]
Lesen Sie diesen [Beitrag](https://wiki.ubuntuusers.de/apt/apt/) von ubuntuusers, 
insbesondere die Kapitel **Pakete verwalten** und **Suchen/Durchsuchen**.


### System aktualisieren

Insbesondere zum Schutz vor Sicherheitslücken sollte man die installierten Pakete
auch auf einem anscheinend gut funktionierenden Systeme regelmäßig aktualisieren.

- [EC] Aktualisieren Sie ihr System.


### Pakete suchen, installieren, auflisten

In dieser Aufgabe nehmen wir als Beispiel den `midnight commander`. 
Das ist ein textbasierter, halbgrafischer Dateimanager -- ziemlich praktisch.

- [EC] Suchen Sie mit `apt` nach dem Begriff `midnight commander`.
- [EC] Geben Sie die Paketinformationen des Paketes von `midnight commander` aus.
- [EC] Installieren Sie das Paket.
- [EC] Geben Sie die Liste aller installierten(!) Pakete aus, deren Namen mit `m` beginnen.


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
