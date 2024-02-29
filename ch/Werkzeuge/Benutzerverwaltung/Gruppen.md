title: gruppen
stage: draft
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

Ich verstehe Gruppen in Linux und wie ich diese anwenden kann.

[ENDSECTION]
[SECTION::background::default]

Genauso wie es Nutzer in Linux gibt, gibt es auch Gruppen. Gruppen sind nützlich, zum Beispiel, wenn amn mehreren Nutzern Zugriff auf bestimmte Dateien geben möchte.

[ENDSECTION]
[SECTION::instructions::detailed]
### Nutzer erstellen

- [EC] Erstellen Sie einen neuen Nutzer namens `bob`

### Gruppe erstellen

- [EC] Erstellen Sie eine neue Gruppe namens `propra`. Nutzen Sie dafür `groupadd`.

- [EC] Fügen sie die Gruppe Bob hinzu. Nutzen sie dafür `adduser`.

### Standardgruppe setzen

- [EC] Erstellen sie eine beliebige Datei mit dem Nutzer `bob`.

- [EC] Erstellen Sie eine neue Gruppe namens `standard`. Nutzen Sie dafür `groupadd`.

- [EC] Setzen Sie diese Gruppe als Standardgruppe für den Nutzer `bob`. Nutzen Sie dafür `usermod`.

- [EC] Erstellen Sie eine beliebige Datei mit dem Nutzer `bob`.

- [EQ] Schauen Sie sich die Berechtigungen der beiden Dateien an. Was fällt auf?

- [EC] Setzen Sie die Standardgruppe von `bob` wieder zurück. Nutzen sie dafür `usermod`.

### Nutzer und Gruppe löschen

- [EC] Löschen Sie den gerade erstellten Nutzer `bob`.

- [EC] Zuguterletzt löschen Sie beide erstellten Gruppen wieder. Nutzen Sie dafür `delgroup`.
[ENDSECTION]
[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]

