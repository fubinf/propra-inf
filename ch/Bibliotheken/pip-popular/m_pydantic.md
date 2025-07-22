title: Pydantic
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: m_json2, m_datetime, m_dataclasses, py-OOP-Inheritance
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
basieren. Die Felder werden validiert, automatisch konvertiert (beispielsweise Datumstrings
zu `datetime`) und lassen sich einfach von und zu JSON konvertieren.
Besonders in Webframeworks, wie FastAPI ist Pydantic das Rückgrat für Datenvalidierung.
[ENDSECTION]


[SECTION::instructions::detailed]

### Model mit `dataclass`

Gegeben sei das folgende JSON Objekt:

```json
{
  "name": "Alan Turing",
  "course": "ALP-1",
  "grade": 2.0,
  "date": "2025-05-05T11:30:00"
}
```

[ER] Erstellen Sie eine eigene Datenklasse `GradeEntry` mit dem `@dataclass` Decorator aus dem Modul
[dataclasses](https://docs.python.org/3/library/dataclasses.html)
mit den Attribute `name: str`, `course: str`, `grade: float` und `date: datetime`.
Erzeugen Sie zwei Exemplare `a` und `b` von `GradeEntry`.
Geben Sie die beiden Exemplare mit `print()` aus.

[ER] Geben Sie auch das Ergebnis des Vergleichsoperators `==` aus, wenn Sie Objekt
`a` mit `a` und `a` mit `b` vergleichen.

Bei der Ausgabe auf der Konsole sehen Sie, dass als Ergebnis kein gültiger
JSON-String ausgegeben wird.

Im Modul `dataclasses` gibt es die Funktion
[`asdict()`](https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict).
Importieren Sie diese mit `from dataclasses import asdict` in Ihre Datei.

[ER] Erzeugen Sie mit `asdict()` aus Ihrem Exemplar `a` einen `dict`, speichern Sie
diesen in `a_dict` und geben Sie `a_dict` aus.

Wie Sie sehen, ist `a_dict` immer noch kein gültiger JSON-String.

[ER] Importieren Sie `dumps()` aus dem
[json Modul](https://docs.python.org/3/library/json.html),
um `a_dict` zu serialisieren, speichern Sie das Ergebnis in der neuen Variable `a_json`
und geben Sie es aus.

[HINT::TypeError: Object of type datetime is not JSON serializable]
Übergeben Sie beim `dumps()`-Aufruf ein Argument `default=str`.
Dann wird `str()` zur Wandlung benutzt, wenn ein `TypeError` geworfen wird,
was bei `datetime`-Attributen der Fall ist; siehe die
[Dokumentation von `dumps`](https://docs.python.org/3/library/json.html#json.dumps).
[ENDHINT]

Dadurch erhalten Sie in `a_json` nun einen gültigen JSON-String.

[ER]  Importieren Sie `loads()` aus dem
[json Modul](https://docs.python.org/3/library/json.html),
um Ihren JSON-String in ein Python-`dict` zu laden.
Erzeugen Sie aus diesem `dict` wieder ein neues Exemplar `a_parsed` Ihrer Klasse `GradeEntry`.
Geben Sie `a_parsed` und den Datentyp von `a_parsed.date` aus.

[HINT::Datentyp eines Objekts prüfen]
Wenn Sie den Datentyp von einem Objekt prüfen möchten können Sie `type()`
in Python verwenden.
[ENDHINT]

Wie Sie merken, ist das Serialisieren eines Objekts in einen JSON-String und das
Deserialisieren (Parsen) eines JSON-Strings in ein Python-Objekt
auf diese Weise nicht trivial.
Außerdem müssen Sie sich beim Parsen selbst, um die richtigen Typen kümmern.
In `a_parsed` ist `date` kein `datetime` sondern vom Datentyp `str`.


### Model mit `Pydantic`

Pydantic ist eine Bibliothek, die das Serialisieren, Parsen und Validieren übernimmt
und dabei auch die richtigen Datentypen erzeugt.

[ER] Installiere Sie die Pydantic Bibliothek mit `pip install pydantic`
auf Ihrem System und lesen Sie die
[Pydantic Dokumentation](https://docs.pydantic.dev/latest/concepts/models/)
bis einschließlich zum Abschnitt "Data conversion".

[ER] Erstellen Sie eine neue Klasse `GradeEntry2`, die von Pydantics `BaseModel` erbt
und wieder das oben gegebene JSON-Schema abbildet.

[ER] Erzeugen Sie ein neues Exemplar `c` der Klasse `GradeEntry2`.

[ER] Serialisieren Sie `c` zu einem JSON-String, speichern Sie diesen String
in der neuen Variable `c_json` und geben Sie ihn auf der Konsole aus.

[HINT::Pydantic Model zu JSON-String serialisieren]
Nutzen Sie dafür `model_dump_json()`, die jede Klasse hat, die von `BaseModel` erbt;
siehe die
[Pydantic Dokumentation für `model_dump_json()`](https://docs.pydantic.dev/latest/concepts/serialization/#modelmodel_dump_json).
[ENDHINT]

[ER] Erzeugen Sie ein neues `GradeEntry2`-Exemplar `c_parsed`. Laden Sie diesmal aber die Daten
aus `c_json`.

[HINT::JSON-String zu Pydantic Model parsen]
Nutzen Sie dafür `GradeEntry2.model_validate_json()`, das Sie von `BaseModel` geerbt haben;
siehe die
[Pydantic Dokumentation für `model_validate_json()`](https://docs.pydantic.dev/latest/concepts/models/#validating-data).
[ENDHINT]

[ER] Geben Sie `c_parsed` und geben Sie den Datentyp von `c_parsed.date` aus.

Wie Sie erkennen können ist `c_parsed` wieder ein `GradeEntry2`-Exemplar und
`date` ist auch korrekt vom Datentyp `datetime` ohne, dass Sie das erneut manuell
angeben mussten.

[EC] Führen Sie Ihr Programm einmal aus.
[ENDSECTION]


[SECTION::submission::trace,reflection]

Beschreiben Sie kurz, wann es sinnvoller ist, Pydantic zu benutzen, als `@dataclass`
aus der Python Standardbibliothek.

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]

[INCLUDE::ALT:]

Beispiellösung siehe [TREEREF::/Bibliotheken/pip-popular/m_pydantic.py]

[ENDINSTRUCTOR]
