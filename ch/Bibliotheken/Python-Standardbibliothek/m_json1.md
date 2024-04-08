title: Grundlagen JSON-Objekt
stage: beta
timevalue: 1.0
difficulty: 2
explains: JSON
---
<!-- TODO_1: assumes: PythonDataStructures -->

[SECTION::goal::trial]

Ich kann die [TERMREF::JSON]-Notation lesen und schreiben.

[ENDSECTION]
[SECTION::background::default]

[TERMREF::JSON] repräsentiert Datenstrukturen.
Es ist einfach zu lesen und zu schreiben, flexibel und anpassungsfähig. 
Es erlaubt die Darstellung komplexer Datenstrukturen, darunter verschachtelte
Objekte und Arrays, wodurch es sich für die Repräsentation von Daten in einer Vielzahl von
Szenarien eignet. 
Von einfachen Konfigurationsdateien bis hin zu komplexen [TERMREF::API]-Antworten
findet JSON breite Anwendung in der Softwareentwicklung.
Man muss JSON also kennen.

[ENDSECTION]
[SECTION::instructions::detailed]

### JSON Syntax

Betrachten Sie das folgende JSON-Objekt und beantworten Sie folgende Fragen mit Hilfe der
folgenden Quelle [w3schools](https://www.w3schools.com/js/js_json_intro.asp)

```JSON
{
  "name": "John",
  "age": 30,
  "city": "New York",
  "isStudent": false,
  "hobbies": ["reading", "running", "cooking"]
}
```

- [EQ] Wie werden Schlüssel-Wert-Paare in JSON dargestellt?
- [EQ] Welche Datentypen werden im JSON-Objekt verwendet?
- [EQ] Wie werden Zeichenketten in JSON notiert?
- [EQ] Wie werden Zahlen in JSON dargestellt?
- [EQ] Wie werden boolesche Werte in JSON ausgedrückt?
- [EQ] Wie werden Arrays in JSON notiert?
- [EQ] Welche Regeln gelten für das Formatieren von JSON?

Recherchieren Sie im Netz:

- [EQ] Warum wird JSON als 'leichtgewichtig' bezeichnet?
- [EQ] Was sind die wichtigsten Stärken und Schwächen im Vergleich der drei
  Notationen JSON, YAML und XML?
- [EQ] Wie kann man bei JSON Kommentare einbinden?


### JSON-Objekt erstellen

Jetzt sind sie gefragt. Sie sollen im Folgenden anhand der gegebenen Informationen ein eigenes
JSON-Objekt erstellen.

- [ER] Erstellen Sie ein JSON-Objekt mit dem Namen `m_json_books.json` anhand der folgenden Vorgabe.
  Verwenden Sie Feldnamen in normaler Groß-/Kleinschreibung, obwohl man sonst tendenziell nur Kleinschreibung benutzt.

```md
Ein Buch, das von einem Autor namens "Alice" geschrieben wurde. Der Titel des Buches lautet 
"Die Abenteuer von Alice im Wunderland" und es hat 200 Seiten.
```

- [ER] Ergänzen Sie aus [EREFR::1] die Eigenschaften `ISBN` und `Auflage` mit beliebigen Werten.
- [ER] Erstellen Sie ein JSON-Objekt mit dem Namen `m_json_student.json` anhand der folgenden Vorgabe.
  Jeder Datenwert (z.B. "16:00") soll ein eigenes Feld bekommen.

```md
Ein Student namens "Max" besucht die Universität. 
Max hat die Fächer Softwaretechnik, Lineare Algebra und das Programmierpraktikum gewählt. 
Das Programmierpraktikum ist sein Lieblingsfach. 
Seine Lieblingsprogrammiersprache ist Python. 
Die Vorlesungszeiten für jedes Fach sind wie folgt:
- Softwaretechnik: Montag und Mittwoch von 10:00 bis 12:00 Uhr
- Lineare Algebra: Dienstag und Donnerstag von 14:00 bis 16:00 Uhr
- Programmierpraktikum: keine

Max strebt folgende Wunschnoten für jedes Fach an:
- Softwaretechnik: 1,3
- Lineare Algebra: 2,7
```

- [ER] Ergänzen Sie einen Eintrag für einen zweiten Studenten in das JSON-Objekt.
  Sie brauchen nur einen Namen anzugeben, die übrigen Felder können entfallen.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::heading]

- [EREFR::1] Mögliche Lösung:

```JSON
{
  "Autor": "Alice",
  "Titel": "Die Abenteuer von Alice im Wunderland",
  "Seitenzahl": 200
}
```

- [EREFR::2] Mögliche Lösung (es gibt natürlich viele andere):

```JSON
{
  "Student": {
    "Name": "Max",
    "Universität": "Universität XYZ",
    "Fächer": [
      {
        "Fachname": "Softwaretechnik",
        "Lieblingsfach": false,
        "Vorlesungszeiten": [
          {
            "Tag": "Montag",
            "Startzeit": "10:00",
            "Endzeit": "12:00"
          },
          {
            "Tag": "Mittwoch",
            "Startzeit": "10:00",
            "Endzeit": "12:00"
          }
        ],
        "Wunschnote": 1.3
      },
      {
        "Fachname": "Lineare Algebra",
        "Lieblingsfach": false,
        "Vorlesungszeiten": [
          {
            "Tag": "Dienstag",
            "Startzeit": "14:00",
            "Endzeit": "16:00"
          },
          {
            "Tag": "Donnerstag",
            "Startzeit": "14:00",
            "Endzeit": "16:00"
          }
        ],
        "Wunschnote": 2.7
      },
      {
        "Fachname": "Programmierpraktikum",
        "Lieblingsfach": true,
      }
    ]
  }
}
```

[ENDINSTRUCTOR]
