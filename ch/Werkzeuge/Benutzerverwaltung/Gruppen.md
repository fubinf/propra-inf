title: Gruppen
stage: draft
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

Ich verstehe Gruppen in Linux und wie ich diese anwenden kann.

[ENDSECTION]
[SECTION::background::default]

In Linux spielen Gruppen eine wichtige Rolle bei der Verwaltung von Benutzerrechten und der Organisation von Benutzern auf einem System.

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

