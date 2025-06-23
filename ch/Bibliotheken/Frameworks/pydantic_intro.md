title: Pydantic Intro
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: m_json2, py-OOP-Inheritance
---


[SECTION::goal::idea]

Ich verstehe den Zweck und die Anwendung von Pydantic in Python-Projekten und kann einfache
Datenmodelle erstellen und verwenden.
Ich kann den Unterschied zu Datenklassen zu erklären und geeignete Einsatzgebiete erkennen.

[ENDSECTION]


[SECTION::background::default]

In Python können Datenklassen verwendet werden, um strukturierte Daten zu modellieren – etwa Objekte
mit bestimmten Attributen.
Sie sind nützlich, enthalten aber keine eingebaute Validierung, keine automatische Typkonvertierung
und keine Unterstützung für JSON-Parsing.

Pydantic erweitert dieses Konzept: Es erlaubt das Erstellen von Klassen, die auf strengen Typen
basieren. Die Felder werden validiert, automatisch konvertiert (z. B. Strings zu `datetime`), und
lassen sich einfach in JSON konvertieren oder daraus erzeugen.
Besonders in Webframeworks wie FastAPI ist Pydantic das Rückgrat für Datenvalidierung.

[ENDSECTION]


[SECTION::instructions::detailed]

### Model mit `dataclass`

Das Modul
[dataclasses](https://docs.python.org/3/library/dataclasses.html)
der Python Standardbibliothek beinhaltet das den Decorator `@dataclass`.
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

Erstellen Sie eine eigene dataclass `GradeEntry` und erzeugen Sie zwei Instanzen von `GradeEntry`.

[ER] Nutzen Sie die `print()` Funktion um diese beiden Instanzen auf die Konsole zu drucken.

[ER] Geben Sie auch das Ergebnis des Vergleichs Operators `==`, wenn sie Objekt
a mit a und a mit b vergleichen aus.

Bei der Ausgabe auf der Konsole sehen Sie, dass als Ergebnis kein valider
JSON String ausgegeben wird.

Nutzen Sie das built-in `__dict__` Attribut Ihrer `GradeEntry` Klasse,
um daraus ein `dict` zu erzeugen.

[ER] Geben Sie das Ergebnis von dem `__dict__` Attribute einer Ihrer Instanzen aus.

Wie Sie erkenne können ist das Ergebnis immer noch kein valider json String.

Nutzen sie die `dumps` Funktion aus dem
[json Modul](https://docs.python.org/3/library/json.html), um den `__dict__` zu serialisieren
und speichern Sie das Ergebnis in einer neuen Variable.

[HINT::TypeError: Object of type datetime is not JSON serializable]
Übergeben sie den `default=str` als Parameter der `dumps` Funktion.
Diese Funktion wird aufgerufen wenn ein TypeError geworfen wird,
was beim type `datetime` der Fall ist.
[ENDHINT]

Nutzen Sie die `loads` Funktion aus dem
[json Modul](https://docs.python.org/3/library/json.html),
um Ihren json String in ein Python `dict` zu laden.
Erzeugen Sie aus diesem dict wieder eine neue Instanz Ihrer `GradeEntry` Klasse.

[ER] Geben Sie das Ergebnis der neuen Instanzen aus.

[EQ] Wird das Datum automatisch als `datetime` Objekt geparst?

Wie Sie merken ist das serialisieren eines Object in einen JSON String und das Parsen eines
JSON Strings in ein Python Objekt
auf diese Weise nicht trivial.
Außerdem müssen Sie sich beim Parsen selbst, um die richtigen Typen kümmern.


### Model mit `Pydantic`

Pydantic ist ein Framework, dass das Serialisieren und das Parsen und Validieren übernimmt.

[ER] Lesen Sie die [Pydantic Dokumentation](https://docs.pydantic.dev/latest/concepts/models/)
bis einschließlich zum Abschnitt "Data conversion".

Erstellen Sie eine neue Klasse `GradeEntry2` das von Pydantics `BaseModel` erbt
und wieder das obengegebene JSON Schema abbildet.
Erzeugen Sie nun eine neue Instanz der Klasse `GradeEntry2`.

[ER] Serialisieren Sie diese Instanz zu einem JSON String, speichern Sie diesen String
in einer neuen Variable und geben Sie den String auf der Konsole aus.

[HINT::Pydantic Model zu JSON String serialisieren]
Nutzen Sie dafür die `model_dump_json()` Funktion die jede Klasse hat, die von `BaseModel` erbt.
[ENDHINT]

Laden Sie den String nun in eine neue Instanz der `GradeEntry2` Klasse

[HINT::JSON String zu Pydantic Model parsen]
Nutzen Sie dafür die `GradeEntry2.model_validate_json()` Funktion die jede Klasse hat,
die von `BaseModel` erbt.
[ENDHINT]

---

[EQ] Beschreiben Sie kurz wann es sinnvoller ist Pydantic zu benutzen, als `@dataclass`
aus der Python Standardbibliothek.

[EC] Führen Sie Ihre Datei einmal aus und schreiben Sie die Ausgabe in ein Kommandoprotokoll.
Jede Aufgabe [EREFR::1], [EREFR::2], ... fügt ein neues `print()` Statement hinzu.

[ENDSECTION]


[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]