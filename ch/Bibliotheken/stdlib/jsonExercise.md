title: Python JSON-Objekte manipulieren
stage: alpha
timevalue: 2.0
difficulty: 3
explains: JSON
requires: jsonBasic
---
[SECTION::goal::trial]

- Ich kann das Paket `json` verwenden, um JSON-Dateien in Python zu bearbeiten

[ENDSECTION]
[SECTION::background::default]

Durch die Verwendung des json-Pakets in Python können Sie JSON-Daten mühelos laden,
analysieren, aktualisieren und speichern. Diese Fähigkeit ist von unschätzbarem Wert,
wenn Sie mit Web-APIs arbeiten, Daten zwischen verschiedenen Anwendungen austauschen
oder einfach nur Daten in einem strukturierten Format verwalten müssen. Zusätzlich ist
diese Bibliothek ein sehr nützlicher Helfer in der Entwicklung von Webanwendungen,
in der Datenanalyse oder der Automatisierung von Aufgaben.

[ENDSECTION]
[SECTION::instructions::detailed]

### JSON mit Python

Im folgenden wollen wir mit dem von Ihnen erstellten JSON-Objekt aus Aufgabe [EREFR::3] der Übung [PARTREF::jsonBasic] weiter arbeiten.

- [ER] Erstellen Sie ein Python Script, dass diese Datei einliest.

[HINT::JSON-Funktion]

- [json.loads()](https://docs.python.org/3/library/json.html#json.loads) bietet die Möglichkeit das
JSON-Objekt wie ein Python Dictionary zu verwenden und erleichtert die Handhabung.
- [open()](https://docs.python.org/3/library/functions.html#open) bietet die Möglichkeit
  Informationen aus Dateien zu lesen

[ENDHINT]

- [ER] Erstellen Sie eine Funktion, die die Wunschnote eines Faches von einem Studenten ändert.
- [ER] Erstellen Sie eine Funktion, die das Lieblingsfach eines Studenten ändert.
- [ER] Erstellen Sie eine Funktion, die ein Studienfach zu einem Studenten hinzufügt.
- [ER] Erstellen Sie eine Funktion, die einen neuen Studenten mit allen möglichen Eigenschaften.
  anlegt. Der Student soll beim Anlegen mindestens ein Fach belegen, ansonsten folgt eine
  Fehlermeldung.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Quellcode.md]
[ENDSECTION]
