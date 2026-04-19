title: "json: Einlesen und manipulieren von JSON-Objekten"
stage: beta
timevalue: 1.5
difficulty: 2
explains: JSON
requires: encoding-and-open
---

[SECTION::goal::idea]
Ich verstehe die grundlegende [TERMREF::JSON]-Notation.  
Ich kann in Python JSON-Dateien einlesen und manipulieren.
[ENDSECTION]


[SECTION::background::default]
[TERMREF::JSON] repräsentiert Datenstrukturen.
Es ist einfach zu lesen und zu schreiben, flexibel und anpassungsfähig.
Es erlaubt die Darstellung komplexer Datenstrukturen, darunter verschachtelte Objekte und Arrays,
wodurch es sich für die Repräsentation von Daten in einer Vielzahl von Szenarien eignet.
Von einfachen Konfigurationsdateien bis hin zu komplexen [TERMREF::API]-Antworten findet JSON 
breite Anwendung in der Softwareentwicklung.

Durch die Verwendung des `json`-Moduls in Python können Sie JSON-Daten mühelos als eine 
entsprechende Python-Datenstruktur laden oder umgekehrt eine solche Python-Datenstruktur im 
JSON-Format schreiben.
[ENDSECTION]


[SECTION::instructions::detailed]

### JSON Syntax verstehen

Bevor wir in die Funktionsweise des Moduls eintauchen, wollen wir die Syntax von JSON kennenlernen.
Betrachten Sie das folgende JSON-Objekt und lesen Sie die folgende
[Einführung auf w3schools](https://www.w3schools.com/js/js_json_intro.asp).

```JSON
{
  "name": "John",
  "age": 30,
  "city": "New York",
  "isStudent": false,
  "hobbies": ["reading", "running", "cooking"]
}
```

Beantworten Sie nun die folgenden Fragen stichpunktartig:

[EQ] Wie werden Schlüssel-Wert-Paare in JSON dargestellt und wie werden Sie voneinander getrennt?

[EQ] Was ist ein Objekt in JSON und wie wird es dargestellt?

[EQ] Welche Datentypen verwendet unser JSON-Objekt?
Geben sie für jeden an, wie er in JSON dargestellt wird.

Recherchieren Sie für die folgenden Fragen ggf. im Netz:

[EQ] Werte können in JSON noch zwei weitere Datentypen annehmen. Welche sind das?

[EQ] Wie kann man in JSON Kommentare einbinden?

[EQ] Welche Regeln gelten für das Formatieren (Zeilenumbrüche, Einrückung) in JSON?

[EQ] JSON wird häufig als 'leichtgewichtig' bezeichnet.
Vergleichen Sie es mit zwei weiteren Datenstrukturformaten diesbezüglich.
Bringt die Leichtgewichtigkeit evtl. auch Nachteile mit sich?
`<!-- time estimate: 20 min -->`


### JSON-Objekt erstellen

Jetzt sind Sie gefragt. Sie sollen im Folgenden anhand der gegebenen Informationen eigene
JSON-Objekte erstellen.

[ER] Erstellen Sie ein JSON-Objekt anhand der folgenden Vorgabe.
Trennen Sie die Datenwerte möglichst voneinander (z.B. Tag und Uhrzeit) und Überlegen Sie sich 
eine geeignete Struktur, um die Arbeit mit dem Objekt möglichst einfach zu gestalten.
Schreiben Sie die Schlüsselnamen in Englisch und verwenden Sie eine einheitliche 
[TERMREF::Namenskonvention].
Speichern Sie das Objekt als Datei unter dem Namen `m_json_students.json`.

> Ein Student namens "Max" besucht die Universität.
> Max hat die Fächer Softwaretechnik, Lineare Algebra und das Programmierpraktikum gewählt.
> Das Programmierpraktikum ist sein Lieblingsfach.
> Seine Lieblingsprogrammiersprache ist Python.
> Die Vorlesungszeiten für jedes Fach sind wie folgt:
> 
> - Softwaretechnik: Montag und Mittwoch von 10:00 bis 12:00 Uhr
> - Lineare Algebra: Dienstag und Donnerstag von 14:00 bis 16:00 Uhr
> - Programmierpraktikum: keine
> 
> Max strebt folgende Wunschnoten für jedes Fach an:
> 
> - Softwaretechnik: 1,3
> - Lineare Algebra: 2,7

[ER] Ergänzen Sie einen weiteren Eintrag für einen zweiten Studenten in das JSON-Objekt.
Sie brauchen nur einen Namen anzugeben, die übrigen Felder können entfallen.
`<!-- time estimate: 10 min -->`


### JSON mit Python

Nun wollen wir unsere erstellten JSON-Objekte in Python einlesen und manipulieren.

Legen Sie die Datei `m_json.py` an und fügen Sie dort Ihre Lösungen für die folgenden 
Programmieraufgaben ein.

Lesen Sie grob die
[Dokumentation vom Modul `json`](https://docs.python.org/3/library/json.html)
bis zum Abschnitt `Encoders and Decoders`.

[EQ] Zum Serialisieren und Deserialisieren stellt das Modul jeweils zwei Funktionen zur 
Verfügung: `dump`, `dumps`, `load` und `loads`.
Was ist der Unterschied zwischen den Funktionen mit und ohne `s`?

[ER] Lesen Sie nun das JSON-Objekt aus der Datei `m_json_students.json` ein und speichern Sie die 
Datenstruktur in der Variable `students`.
Serialisieren Sie anschließend das Objekt wieder in einen String und geben Sie diesen aus.
Der String sollte leserlich formatiert sein.

[NOTICE]
Zum formatierten Ausgeben eines JSON-Objektes und anderer Datenstrukturen in der Konsole ist das 
Modul [PARTREF2::m_pprint::pprint] noch besser geeignet.
Verwenden Sie in dieser Aufgabe zu Übungszwecken nur Funktionen aus `json`.
[ENDNOTICE]

[ER] Erstellen Sie eine Funktion 
`has_lecture(students_obj, student_name: str, weekday: str) -> bool`,
die einen Wahrheitswert zurückgibt, ob der Student existiert und an dem Wochentag eine 
Veranstaltung hat.

[ER] Rufen Sie `has_lecture()` für Max jeweils für Donnerstag und Freitag auf und geben Sie die 
Ergebnisse mit `print` nachvollziehbar aus.

[ER] Erstellen Sie eine Funktion 
`set_target_grade(students_obj, student_name: str, course_name: str, target_grade: float)`, 
die bei einem Studenten die Wunschnote eines Fachs ändert.
Falls Student, Fach oder Wunschnote nicht existieren, soll die Funktion keine neuen Werte erstellen.

[ER] Setzen Sie für Max die Wunschnote für Lineare Algebra auf 2,3.
Versuchen Sie auch, die Note für das Programmierpraktikum auf 1,5 zu ändern, auch wenn sie nicht 
existiert.

[ER] Schreiben Sie das geänderte Objekt in die Datei `m_json_students2.json`.
Der Inhalt der Datei soll ebenfalls gut lesbar sein.
`<!-- time estimate: 60 min -->`
[ENDSECTION]


[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
Geben Sie ebenfalls beide JSON Dateien ab.

[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::JSON Objekt und Kommandoprotokoll prüfen]
JSON Objekt in [TREEREF::m_json_students.json] mit Kommandoprotokoll vergleichen.
Bei Abweichungen oder Auffälligkeiten zusätzlich den Code prüfen.

[INCLUDE::ALT:]

### `m_json_students.json`:

```JSON
[INCLUDE::ITREE:m_json_students.json]
```

### Kommandoprotokoll

[PROT::ALT:m_json.prot]
[ENDINSTRUCTOR]
