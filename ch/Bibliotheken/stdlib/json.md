title: Python JSON-Objekte
stage: alpha
timevalue: 3.0
difficulty: 3
explains: JSON
assumes: PythonDataStructures
---
[SECTION::goal::trial]

- Ich kann ein JSON-Objekt lesen und bearbeiten
- Ich kann das Paket `json` verwenden, um JSON-Dateien in Python zu bearbeiten

[ENDSECTION]
[SECTION::background::default]

JSON ist nicht nur einfach zu lesen und zu schreiben, sondern auch sehr flexibel. Es erlaubt
die Darstellung komplexer Datenstrukturen, einschließlich verschachtelter Objekte und Arrays.
Dadurch eignet es sich ideal für die Darstellung von Daten in vielen verschiedenen Szenarien,
von einfachen Konfigurationsdateien bis hin zu komplexen API-Antworten.

In dieser Einführung werden wir uns damit beschäftigen, wie JSON strukturiert ist, wie man es
liest und schreibt, und wie es in der Praxis verwendet wird.

[ENDSECTION]
[SECTION::instructions::detailed]

### JSON Syntax

Betrachten Sie das folgende JSON-Objekt und beantworten Sie folgende Fragen mit Hilfer der
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

- [EQ] Warum ist JSON so populär?

### JSON-Objekt erstellen

Jetzt sind sie gefragt. Sie sollen im folgenden anhand der gegebenen Informationen eine eigenes JSON-Obnjekt erstellen.

- [ER] Erstellen Sie ein JSON-Objekt mit dem Namen `student.json` anhand der folgenden Vorgabe.

```md
Ein Buch, das von einem Autor namens "Alice" geschrieben wurde. Der Titel des Buches lautet 
"Die Abenteuer von Alice im Wunderland" und es hat 200 Seiten.
```

- [ER] Erstellen Sie ein JSON-Objekt anhand der folgenden Vorgabe.

```md
Ein Student namens "Max" besucht die Universität. Max hat die Fächer Softwaretechnik, Lineare Algebra und das
Programmierpraktikum gewählt. Das Programmierpraktikum ist sein Lieblingsfach. Seine Lieblingsprogrammiersprache
ist Python. Die Vorlesungszeiten für jedes Fach sind wie folgt:
- Softwaretechnik: Montag und Mittwoch von 10:00 bis 12:00 Uhr
- Lineare Algebra: Dienstag und Donnerstag von 14:00 bis 16:00 Uhr
- Programmierpraktikum: keine

Max strebt folgende Wunschnoten für jedes Fach an:
- Softwaretechnik: 1,2
- Lineare Algebra: 2,4
- Programmierpraktikum: 1,0
```

- [ER] Ergänzen Sie aus [EREFR:1] zwei weitere Bücher.

### JSON mit Python

Im folgenden wollen wir mit dem von Ihnen erstellten JSON-Objekt aus Aufgabe [EREFR:2] weiter arbeiten.

- [ER] Erstellen Sie zusätzlich ein Python Script, dass diese Datei einliest.

[HINT::VisibleTitle]

[json.loads()](https://www.w3schools.com/python/python_json.asp) bietet die Möglichkeit das JSON-Objekt wie ein Python Dictionary zu verwenden.

[ENDHINT]

- [ER] Ändern Sie über eine Funktion die Wunschnote `Lineare Algebra` in 2,0 ab.
- [ER] Ergänzen Sie einen weiteren beliebigen Studenten über eine Funktion.

### JSON Performance

Betrachten Sie folgenden Artikel auf [Medium](https://medium.com/data-science-community-srm/json-is-incredibly-slow-heres-what-s-faster-ca35d5aaf9e8)

- [EQ] Welcher entscheidenede Nachteil wird hier addressiert und welche Gründe werden genannt?
- [EQ] Welche Tips werden gegeben, um diesen Nachteil bestmöglich entgegen zu wirken?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Kommandoprotokoll.md]
[INCLUDE::../../_include/Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::possible solution]

- [EREFR:1] Mögliche Lösung:

```JSON
{
  "Autor": "Alice",
  "Titel": "Die Abenteuer von Alice im Wunderland",
  "Seitenzahl": 200
}
```

- [EREFR:2] Mögliche Lösung:

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
