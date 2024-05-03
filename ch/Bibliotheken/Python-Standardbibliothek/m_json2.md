title: Python JSON-Objekte manipulieren
stage: beta
timevalue: 1.0
difficulty: 3
explains: JSON
requires: encoding_and_open,m_json1
---
[SECTION::goal::trial]

Ich kann das Paket `json` verwenden, um JSON-Daten in Python zu lesen und zu schreiben

[ENDSECTION]
[SECTION::background::default]

Durch die Verwendung des `json`-Moduls in Python können Sie JSON-Daten mühelos 
als eine entsprechende Python-Datenstruktur laden
oder umgekehrt eine solche Python-Datenstruktur im JSON-Format schreiben.

[ENDSECTION]
[SECTION::instructions::detailed]

### JSON mit Python

- Lesen Sie grob die [Dokumentation von Modul `json`](https://docs.python.org/3/library/json.html)
  bis zu `json.loads()`.
- Im Folgenden wollen wir mit dem von Ihnen erstellten JSON-Objekt `m_json_student.json`
  aus [PARTREF::m_json1] weiter arbeiten.
- [ER] Erstellen Sie ein Python Script, dass diese Datei einliest.

[HINT::JSON lesen]
Öffnen Sie die Datei mit `open()`, im text mode.
Dann können Sie entweder direkt mit `json.load()` aus der File Handle lesen
oder rufen selber `.read()` und übergeben den String an `json.loads()`.
Die meisten optionalen Parameter brauchen Sie nicht.
[ENDHINT]

- [ER] Erstellen Sie eine Funktion 
  `hat_uni(json, studentname: str, wochentag: str) -> bool`,
  die `True` liefert, falls der Student existiert und an dem Wochentag eine Veranstaltung hat.
  `False` andernfalls.
- [ER] Rufen Sie `hat_uni` für Max für Donnerstag und für Freitag auf und geben Sie die Ergebnisse 
  mit `print` aus.
- [ER] Erstellen Sie eine Funktion 
  `setze_wunschnote(json, studentname: str, fachname: str, wunschnote: float)`, 
  die bei einem Studenten die Wunschnote eines Faches ändert.
  Falls Student, Fach oder Wunschnote nicht existieren, tut die Funktion nichts.
- [ER] Setzen Sie für Max die Wunschnote für Lineare Algebra auf 2,3.
- [ER] Schreiben Sie das geänderte Objekt in die Datei `m_json_student2.json`.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
Geben Sie auch `m_json_student2.json` ab.

[ENDSECTION]
[INSTRUCTOR::Kurz Code und Ergebnis prüfen]

- Stehen in `m_json2.py` sinnvoll aussehende Funktionen `hat_uni()` und `setze_wunschnote()`
wie oben beschrieben?
- Gibt es `m_json_student2.json` mit einer Lineare-Algebra-Wunschnote von 2,3?

[ENDINSTRUCTOR]