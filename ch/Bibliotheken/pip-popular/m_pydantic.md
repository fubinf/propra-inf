title: Pydantic
stage: beta
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
Pydantic macht die Arbeit mit strukturierten Daten in Python deutlich einfacher.
Es prüft automatisch die Datentypen, konvertiert Werte und sorgt dafür, dass Daten
zuverlässig von und zu JSON verarbeitet werden können.
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

[ER] Erstellen Sie eine eigene Datenklasse `GradeEntry` mit dem `@dataclasses.dataclass`-Decorator
mit den Attributen `name: str`, `course: str`, `grade: float` und `date: datetime`.
Erzeugen Sie ein `GradeEntry`-Exemplare `a`.
Geben Sie es mit `print()` aus.

Bei der Ausgabe auf der Konsole sehen Sie, dass als Ergebnis kein gültiger
JSON-String ausgegeben wird.

Im Modul `dataclasses` gibt es die Funktion
[`asdict()`](https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict).
Importieren Sie `dataclasses`, um diese Funktion nutzen zu können.

[ER] Erzeugen Sie mit `dataclasses.asdict(a)` aus `a` einen `dict`, speichern Sie
diesen in `a_dict` und geben Sie `a_dict` aus.

Wie Sie sehen, ist `a_dict` immer noch kein gültiger JSON-String.

[ER] Importieren Sie das
[`json` Modul](https://docs.python.org/3/library/json.html),
um `a_dict` mit `json.dumps()` zu serialisieren, speichern Sie das Ergebnis in
`a_json` und geben Sie es aus.

[HINT::TypeError: Object of type datetime is not JSON serializable]
Übergeben Sie beim `json.dumps()`-Aufruf ein Argument `default=str`.
Dann wird `str()` zur Wandlung benutzt, wenn ein `TypeError` geworfen wird,
was bei `datetime`-Attributen der Fall ist; siehe die
[Dokumentation von `json.dumps()`](https://docs.python.org/3/library/json.html#json.dumps).
[ENDHINT]

Dadurch erhalten Sie in `a_json` nun einen gültigen JSON-String.

[ER] Importieren Sie `json.loads()` aus dem
[json Modul](https://docs.python.org/3/library/json.html),
um Ihren JSON-String in ein Python-`dict` zu laden.
Erzeugen Sie aus diesem `dict` wieder ein neues Exemplar `a_parsed` Ihrer Klasse `GradeEntry`.
Geben Sie `a_parsed` und `type(a_parsed.date)` aus.

Wie Sie merken, ist das Serialisieren eines Objekts in einen JSON-String und das
Deserialisieren (Parsen) eines JSON-Strings in ein Python-Objekt
auf diese Weise nicht trivial.
Außerdem müssen Sie sich beim Parsen selbst um die richtigen Typen kümmern.
In `a_parsed` ist `date` kein `datetime` mehr, sondern ein `str`.

### Model mit `Pydantic`

Pydantic ist eine Bibliothek, die das Serialisieren, Parsen und Validieren übernimmt
und dabei auch die richtigen Datentypen erzeugt.

Installieren Sie die Pydantic Bibliothek mit `pip install pydantic`
auf Ihrem System und lesen Sie die
[Pydantic Dokumentation](https://docs.pydantic.dev/latest/concepts/models/)
bis einschließlich zum Abschnitt "Data conversion".

[ER] Erstellen Sie eine neue Klasse `GradeEntry2`, die von Pydantics `BaseModel` erbt
und wieder das oben gegebene JSON-Schema abbildet.

[ER] Erzeugen Sie ein neues `GradeEntry2`-Exemplar `c`.

[ER] Serialisieren Sie `c` zu einem JSON-String, speichern Sie diesen String
in der neuen Variable `c_json` und geben Sie ihn auf der Konsole aus.

[HINT::Pydantic Model zu JSON-String serialisieren]
Nutzen Sie dafür `model_dump_json()`, die jede Klasse hat, die von `BaseModel` erbt;
siehe die
[Pydantic Dokumentation für `model_dump_json()`](https://docs.pydantic.dev/latest/concepts/serialization/#modelmodel_dump_json).
[ENDHINT]

[ER] Erzeugen Sie ein neues `GradeEntry2`-Exemplar `c_parsed`.
Laden Sie diesmal aber die Daten aus `c_json`.

[HINT::JSON-String zu Pydantic Model parsen]
Nutzen Sie dafür `GradeEntry2.model_validate_json()`, das Sie von `BaseModel` geerbt haben;
siehe die
[Pydantic Dokumentation für `model_validate_json()`](https://docs.pydantic.dev/latest/concepts/models/#validating-data).
[ENDHINT]

[ER] Geben Sie `c_parsed` und geben Sie den Datentyp von `c_parsed.date` aus.

Wie Sie erkennen können ist `c_parsed` wieder ein `GradeEntry2`-Exemplar und
`date` ist auch vom Datentyp `datetime` ohne, dass Sie das erneut manuell angeben mussten.

[EC] Führen Sie Ihr Programm einmal aus.

[EQ] Wann ist es sinnvoller, Pydantic zu benutzen, als `dataclasses.dataclass`
aus der Python Standardbibliothek?
[ENDSECTION]


[SECTION::submission::trace,reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Codedurchsicht]
[INCLUDE::ALT:]

Beispiellösung (siehe auch [TREEREF::/Bibliotheken/pip-popular/m_pydantic.py]):
```py
[INCLUDE::ALT:/../itree.zip/Bibliotheken/pip-popular/m_pydantic.py]
```
[ENDINSTRUCTOR]
