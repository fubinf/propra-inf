title: Pydantic Intro
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: m_json2, py-OOP-Inheritance
---


[SECTION::goal::idea]

- Ich verstehe den Zweck und die Anwendung von Pydantic in Python-Projekten und kann einfache
  Datenmodelle erstellen und verwenden.
- Ich kann den Unterschied zu Datenklassen zu erklären und geeignete Einsatzgebiete erkennen.
[ENDSECTION]


[SECTION::background::default]
In Python können Datenklassen verwendet werden, um strukturierte Daten zu modellieren, also Objekte
mit bestimmten Attributen.
Sie sind nützlich, enthalten aber keine eingebaute Validierung, keine automatische Typkonvertierung
und keine Unterstützung für JSON-Parsing.

Pydantic erweitert dieses Konzept: Es erlaubt das Erstellen von Klassen, die auf strengen Typen
basieren. Die Felder werden validiert, automatisch konvertiert (z. B. Datumstrings zu `datetime`), und
lassen sich einfach von und zu JSON konvertieren.
Besonders in Webframeworks wie FastAPI ist Pydantic das Rückgrat für Datenvalidierung.
[ENDSECTION]


[SECTION::instructions::detailed]

### Model mit `dataclass`

Das Modul
[dataclasses](https://docs.python.org/3/library/dataclasses.html)
der Python Standardbibliothek beinhaltet den Decorator `@dataclass`.
Lesen Sie in der Dokumentation nach, wie dieser Decorator eingesetzt werden kann und welche
Funktionalität er hinzufügt.

[EQ] Auf welchen Objekten kann der `@dataclass` Decorator verwendet werden?

[EQ] Was wird dem Objekt durch den Decorator hinzugefügt?

Gegeben sei das folgende JSON Objekt

```json
{
  "name": "Alan Turing",
  "course": "ALP-1",
  "grade": 2.0,
  "date": "2025-05-05T11:30:00"
}
```

Erstellen Sie eine eigene dataclass `GradeEntry` und erzeugen Sie zwei Exemplare `a` und `b` von `GradeEntry`.

[ER] Nutzen Sie die `print()` Funktion um diese beiden Exemplare auf die Konsole zu drucken.

[ER] Geben Sie auch das Ergebnis des Vergleichsoperators `==` aus, wenn sie Objekt
`a` mit `a` und `a` mit `b` vergleichen.

Bei der Ausgabe auf der Konsole sehen Sie, dass als Ergebnis kein gültiger
JSON-String ausgegeben wird.

Nutzen Sie das built-in `__dict__` Attribut Ihrer `GradeEntry` Klasse,
um daraus ein `dict` zu erzeugen.

[ER] Geben Sie das `__dict__`-Attribut eines Ihrer Exemplare aus.

Wie Sie sehen, ist das Ergebnis immer noch kein gültiger JSON-String.

Nutzen sie die `dumps` Funktion aus dem
[json Modul](https://docs.python.org/3/library/json.html), 
um `__dict__` zu serialisieren
und speichern Sie das Ergebnis in einer neuen Variable.

[HINT::TypeError: Object of type datetime is not JSON serializable]
Übergeben sie beim `dumps`-Aufruf ein Argument `default=str`.
Dann wird die Funktion `str` zur Wandlung benutzt, wenn ein `TypeError` geworfen wird,
was bei `datetime`-Attributen der Fall ist; siehe die
[Dokumentation von `dumps`](https://docs.python.org/3/library/json.html#json.dumps).
[ENDHINT]

Nutzen Sie die `loads` Funktion aus dem
[json Modul](https://docs.python.org/3/library/json.html),
um Ihren JSON-String in ein Python-`dict` zu laden.
Erzeugen Sie aus diesem `dict` wieder eine neue Instanz Ihrer `GradeEntry`-Klasse.

[ER] Geben Sie die neuen Exemplare aus.

[EQ] Wird das Datum automatisch als `datetime`-Objekt geparst?

Wie Sie merken, ist das Serialisieren eines Objekts in einen JSON-String und das 
Deserialisieren (Parsen) eines JSON-Strings in ein Python-Objekt
auf diese Weise nicht trivial.
Außerdem müssen Sie sich beim Parsen selbst, um die richtigen Typen kümmern.


### Model mit `Pydantic`

Pydantic ist ein Framework, das das Serialisieren und das Parsen und Validieren übernimmt.

[ER] Lesen Sie die 
[Pydantic Dokumentation](https://docs.pydantic.dev/latest/concepts/models/)
bis einschließlich zum Abschnitt "Data conversion".

Erstellen Sie eine neue Klasse `GradeEntry2`, die von Pydantics `BaseModel` erbt
und wieder das oben gegebene JSON-Schema abbildet.
Erzeugen Sie ein neues Exemplar der Klasse `GradeEntry2`.

[ER] Serialisieren Sie dieses Exemplar zu einem JSON-String, speichern Sie diesen String
in einer neuen Variable und geben Sie ihn auf der Konsole aus.

[HINT::Pydantic Model zu JSON-String serialisieren]
Nutzen Sie dafür die `model_dump_json()`-Funktion, die jede Klasse hat, die von `BaseModel` erbt.
[ENDHINT]

Laden Sie den String nun in ein neues Exemplar von `GradeEntry2`. 

[HINT::JSON String zu Pydantic Model parsen]
Nutzen Sie dafür `GradeEntry2.model_validate_json()`, das Sie von `BaseModel` geerbt haben.
[ENDHINT]

---

[EQ] Beschreiben Sie kurz, wann es sinnvoller ist, Pydantic zu benutzen, als `@dataclass`
aus der Python Standardbibliothek.

[EC] Führen Sie Ihr Programm einmal aus.
(Jede Aufgabe [EREFR::1], [EREFR::2], ... fügte ein neues `print()` Statement hinzu.)
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::???]
Hinweise an die Tutoren zur Aufgabenkorrektur
INCLUDE::ALT:
TREEREF::Pfad/zu/Musterlösung
PROT::Pfad/zu/Kommandoprotokoll
[ENDINSTRUCTOR]
