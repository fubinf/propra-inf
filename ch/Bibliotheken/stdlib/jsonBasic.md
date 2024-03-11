title: Grundlagen JSON-Objekt
stage: alpha
timevalue: 1.0
difficulty: 2
explains: JSON
assumes: PythonDataStructures
---
1) "..der gegebenen Informationen ein(e)" -> "..der gegebenen Informationen ein"

--------

[SECTION::goal::trial]

- Ich kann ein [TERMREF::JSON]-Objekt lesen und bearbeiten

[ENDSECTION]
[SECTION::background::default]

JSON ist nicht nur einfach zu lesen und zu schreiben, sondern auch äußerst flexibel und
anpassungsfähig. Es erlaubt die Darstellung komplexer Datenstrukturen, darunter verschachtelte
Objekte und Arrays, wodurch es sich ideal für die Repräsentation von Daten in einer Vielzahl von
Szenarien eignet. Von einfachen Konfigurationsdateien bis hin zu komplexen [TERMREF::API]-Antworten
findet JSON breite Anwendung in der Softwareentwicklung und im Datenaustausch zwischen Anwendungen.

Bei der Einführung in JSON werden wir uns nicht nur damit beschäftigen, wie das Format strukturiert
ist und wie man es liest und erstellt, sondern auch seine Rolle im größeren Kontext des
Datenaustauschs und der Datenaustauschformate betrachten. Zusätzlich wollen wir die Vor- und
Nachteile in Bezug Alternativen wie XML oder YAML im Blick haben.

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
- [EQ] Gibt es irgendwelche speziellen Regeln für das Formatieren von JSON?

Recherchieren Sie im Netz:

- [EQ] Welche Haupteingenschaften machen JSON so populär?
- [EQ] Warum wird JSON als 'leichtgewichtig' bezeichnet?
- [EQ] Stellen Sie JSON bezüglich der Lesbarkeit, Effizienz und Verwendungsszenarien YAML und XML
  gegenüber
- [EQ] Bietet JSON die Möglichkeit Kommentare bzw. Kommentarzeilen einzubinden?

### JSON-Objekt erstellen

Jetzt sind sie gefragt. Sie sollen im Folgenden anhand der gegebenen Informationen ein eigenes
JSON-Objekt erstellen.

- [ER] Erstellen Sie ein JSON-Objekt mit dem Namen `books.json` anhand der folgenden Vorgabe.

```md
Ein Buch, das von einem Autor namens "Alice" geschrieben wurde. Der Titel des Buches lautet 
"Die Abenteuer von Alice im Wunderland" und es hat 200 Seiten.
```

- [ER] Ergänzen Sie aus [EREFR::1] die Eigenschaften `ISBN` und `Auflage` mit beliebigen Werten.
- [ER] Erstellen Sie ein JSON-Objekt mit dem Namen `student.json` anhand der folgenden Vorgabe.

```md
Ein Student namens "Max" besucht die Universität. Max hat die Fächer Softwaretechnik, Lineare
Algebra und das Programmierpraktikum gewählt. Das Programmierpraktikum ist sein Lieblingsfach. Seine Lieblingsprogrammiersprache ist Python. Die Vorlesungszeiten für jedes Fach sind wie folgt:
- Softwaretechnik: Montag und Mittwoch von 10:00 bis 12:00 Uhr
- Lineare Algebra: Dienstag und Donnerstag von 14:00 bis 16:00 Uhr
- Programmierpraktikum: keine

Max strebt folgende Wunschnoten für jedes Fach an:
- Softwaretechnik: 1,2
- Lineare Algebra: 2,4
- Programmierpraktikum: 1,0
```

- [ER] Ergänzen Sie aus [EREFR::3] einen weiteren Studenten.

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

- [EREFR::2] Mögliche Lösung:

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
            "Zeit": "10:00 - 12:00 Uhr"
          },
          {
            "Tag": "Mittwoch",
            "Zeit": "10:00 - 12:00 Uhr"
          }
        ],
        "Wunschnote": 1.2
      },
      {
        "Fachname": "Lineare Algebra",
        "Lieblingsfach": false,
        "Vorlesungszeiten": [
          {
            "Tag": "Dienstag",
            "Zeit": "14:00 - 16:00 Uhr"
          },
          {
            "Tag": "Donnerstag",
            "Zeit": "14:00 - 16:00 Uhr"
          }
        ],
        "Wunschnote": 2.4
      },
      {
        "Fachname": "Programmierpraktikum",
        "Lieblingsfach": true,
        "Vorlesungszeiten": "",
        "Wunschnote": 1.0
      }
    ]
  }
}
```

[ENDINSTRUCTOR]
