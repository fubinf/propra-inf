title: "FastAPI-GET"
stage: alpha
timevalue: 1.5
difficulty: 2
explains:
assumes: http-GET
requires: m_pydantic
---


[SECTION::goal::idea]
Ich kann eine mit mehreren GET-Endpunkten mit dem FastAPI Framework erstellen.
Ich kann diese Endpunkte über die [TERMREF::Swagger]-UI und über den Browser ausprobieren.
[ENDSECTION]

[SECTION::background::default]
FastAPI ist ein Python-Webframework, um eine [TERMREF::REST-API] zu entwickeln.
FastAPI bietet eine simple Syntax, um unterschiedliche Endpunkte zu definieren
und validiert durch Pydantic die Ein- und Ausgaben.
[ENDSECTION]


[SECTION::instructions::detailed]


### Vorbereitung

Erstellen Sie die Datei `FastAPI-GET.py`.
Schreiben Sie den Quellcode, den Sie im Verlauf dieser Aufgabe erzeugen, in diese Datei.

[ER] Installieren Sie FastAPI mit `pip`.
_Beachten Sie auch die Anführungszeichen, damit es in allen Terminals funktioniert._

```sh
pip install "fastapi[standard]"
```


### Eine eigene REST-API erstellen

In einer REST-API greifen Clients über die HTTP-Methoden auf Ressourcen zu,
die durch eindeutige Pfade (Endpunkte) identifiziert werden.
Wichtig ist, dass jede Anfrage zustandslos ist.
Der Server speichert keine Informationen über vorherige Anfragen.
In jeder Anfrage müssen alle Daten mitgesendet werden, die zur Bearbeitung notwendig sind.

[ER] Lesen Sie in der
[FastAPI Dokumentation die ersten Schritte](https://fastapi.tiangolo.com/tutorial/first-steps/)
und erstellen Sie den "Hello World" Endpunkt mit dem Pfad `/`, wie es in dort beschrieben ist.

Mit FastAPI wird ebenfalls ein eigenes Kommando `fastapi` installiert.
Dieses kann genutzt werden, um sowohl während der Entwicklung als auch der Veröffentlichung,
einen Webserver zu starten.

[ER] Starten Sie Ihr Programm mit dem Kommando:

```sh
fastapi dev FastAPI-GET.py
```

Wenn das Kommando erfolgreich war, wird in Ihrer Kommandozeile ein Link angezeigt,
mit welchem Sie den Server erreichen:
[HREF::http://127.0.0.1:8000].
Wenn Sie diese Seite in Ihrem Browser aufrufen, sehen Sie die "Hello World"
Antwort.

FastAPI erzeugt automatisch eine interaktive Dokumentation Ihrer API.
Sie erreichen diese
[Swagger UI](https://github.com/swagger-api/swagger-ui)
unter:
[HREF::http://127.0.0.1:8000/docs].

[NOTICE]
Im _ProPra_ wird immer nur mit der "Swagger UI" gearbeitet.
Lesen Sie in der
[FastAPI Dokumentation für weitere Details zur automatische Dokumentation](https://fastapi.tiangolo.com/features/#automatic-docs).
[ENDNOTICE]

[ER] Öffnen Sie die automatisch generierte Dokumentation.
Dort sehen Sie genau einen Endpunkt mit dem Pfad `/`.
Außerdem wird der Funktionsname des Endpunkts als Beschreibung angezeigt.
Aus `def root()` wird `Root`.

[ER] Probieren Sie diesen Endpunkt aus.

Nach dem Erproben wird im Abschnitt "Curl" angezeigt, wie die Anfrage aussah,
die zu dem Endpunkt gesendet wurde.
Sie sehen außerdem die Antwort des Server und den HTTP-Statuscode.

Dort steht jetzt der Code `200` und als Antwort:

```json
{
  "message": "Hello, World!"
}
```

Darunter sehen Sie welche möglichen Antworten gesendet werden können.
Dabei wird immer die Kombination `Code`, Beschreibung und wenn vorhanden das
`Schema` der Antwort angegeben.

Beim Endpunkt wurde nicht spezifiziert, was das Antwortschema ist.
Daher wird dort standardmäßig `"string"` angezeigt.
Die einfachste Form dieses Schema zu ergänzen, ist es in der Funktionssignatur einen
Rückgabetyp anzugeben.

[ER] Ergänzen Sie daher `def read_root() -> dict[str, str]`.

Wenn Sie die Datei speichern, sehen Sie, dass das Programm automatisch neugestartet wird.
Diese Funktion kennen Sie möglicherweise schon aus einem anderen Framework als `Hot Reload`.
Sie müssen Ihr Browserfenster dennoch neu laden, da nur der Server automatisch
neugestartet wird.

Sie sehen, dass nun nicht mehr `"string"` als Antwort gesendet wird.

[WARNING]
Das Antwortschema wird von FastAPI nicht automatisch überprüft.
Als noch kein Antwortschema angegeben war, gab es keinen Fehler.
Dann ist nur die Dokumentation falsch, aber nicht das Programm.
In der OpenAPI-Dokumentation wird das Schema lediglich beschrieben, allerdings nicht durchgesetzt.
Besonders bei öffentlichen API ist es allerdings von hoher Bedeutung das Antwortschema
möglichst genau anzugeben, damit andere Entwickler wissen, was sie erwarten können.
[ENDWARNING]

Allerdings ist auch `dict[str, str]` noch ungenau.
Da FastAPI unter anderem auf `Pydantic` basiert, ist es auch möglich relativ einfach
ein genaues Rückgabeschema zu definieren.

[ER] Importieren Sie zunächst `BaseModel` von `pydantic` und erstellen Sie
die Klasse `Greetings`, die von `BaseModel` erbt, mit dem Attribut `hello: str`.

[ER] Erstellen Sie einen neuen GET-Endpunkt `hello()` unter dem Pfad `/hello`,
der `Greetings` zurückgibt.
Geben Sie in dieser Funktion vorerst ein `Greetings`-Exemplar mit `hello="World"` zurück.

[ER] Probieren Sie diesen Endpunkt aus.
In der Dokumentation sehen Sie nun als Schema, dass JSON zurückgegeben wird
und es genau einen `hello` Schlüssel gibt.

Der Endpunkt wird im folgenden so erweitert, dass ein Parameter mit einem Namen
übergeben werden kann.
Dieser Parameter soll in der `Query` der URL mit angegeben werden können.
Die Query sind Schlüssel-Wert-Paare hinter dem `?` in einer URL.
In der Regel sind das optionale Werte, dass ist aber nur Konvention.
Sie können diese Parameter auch in Endpunkten erzwingen.

[ER] Lesen Sie in der FastAPI Dokumentation den Abschnitt
[Query Parameter](https://fastapi.tiangolo.com/tutorial/query-params/).
Ergänzen Sie dann in `hello()` das Argument `name`.
Geben Sie vorerst keinen Datentyp.

Wenn Sie nun die Dokumentation neu laden, sehen Sie, dass der Endpunkt `/hello`
einen Parameter erwartet vom Typ `any`.

[ER] Ergänzen Sie deswegen in `hello(name)`, den Datentyp `str` und weisen Sie
dem Argument in der Funktion direkt den Standartwert `"World"` zu.
Geben Sie `name` im `Greetings`-Exemplar zurück.

[ER] Probieren Sie den Endpunkt erneut aus und probieren Sie ihn mit Ihrem Namen aus.

---

[ER] Kopieren Sie nun Ihre Klasse `GradeEntry2` aus der `m_pydantic` Aufgabe und
fügen Sie sie als `GradeEntry` hier ein.

[ER] Erstellen Sie diese Variable `fake_db`:

```py
fake_db: list[GradeEntry] = [
    GradeEntry(name="Alice", course="Math", grade=1.7, date=datetime(2024, 4, 10)),
    GradeEntry(name="Bob", course="Physics", grade=2.3, date=datetime(2024, 4, 12)),
    GradeEntry(name="Charlie", course="Physics", grade=1.3, date=datetime(2024, 4, 15)),
    GradeEntry(name="Bob", course="Math", grade=2.0, date=datetime(2024, 4, 18)),
    GradeEntry(name="Alice", course="Physics", grade=1.0, date=datetime(2024, 4, 20)),
]
```

[ER] Erstellen Sie einen neuen GET-Endpunkt `read_grades()` mit dem Pfad `/grades`.
Dieser Endpunkt soll die Liste `fake_db` zurückgeben, um alle Einträge abrufen zu können.

[ER] Erstellen Sie einen neuen GET-Endpunkt `read_students()` mit dem Pfad `/students`.
Dieser Endpunkt soll `set[str]` zurückgeben (doppelte Namen werden, als dieselbe
Person gewertet).
Geben Sie ein Set mit allen Namen in `fake_db` zurück.

[ER] Erstellen Sie einen weiteren GET-Endpunkt `read_courses()` mit dem Pfad `/courses`.
Dieser soll erneut ein Set aller Kursnamen in `fake_db` zurückgeben.
Ergänzen Sie analog zu `/students` den passenden Rückgabetyp und die Logik.

Eine weitere Möglichkeit Parameter in einem Endpunkt zu übergeben, ist es diese direkt
im Pfad mitzugeben.
Beispielsweise um zu ermöglichen, dass alle Kurse einer Person angezeigt werden:
`/student/Bob` oder `/student/Alice`.

[ER] Lesen Sie in der FastAPI Dokumentation den Abschnitt
[Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/).

[ER] Erstellen Sie den GET-Endpunkt `read_grades_of_student(name: str)` mit dem
Pfad `/students/{name}`.
Dieser soll die Liste aller `GradeEntry` dieser Person zurückgeben.

[ER] Erstellen Sie analog dazu den GET-Endpunkt `read_grades_of_course` mit dem
Pfad `/courses/{name}` der die Liste alle `GradeEntry` in dem Kurs zurückgibt.

---

Zum Abschluss der Aufgabe werden nun die einzelnen Endpunkte jeweils einmal
Aufgerufen und in einem Kommandoprotokoll erfasst.

[ER] Beenden Sie Ihre Server. Dazu können Sie in der Konsole, in der der Server
läuft <kbd>Strg</kbd>+<kbd>c</kbd> eingeben.

[EC] Starten Sie den Server mit `fastapi dev FastAPI-GET.py` und öffnen Sie
die automatische Dokumentation in ihrem Browser.

[EC] Probieren Sie den Endpunkt `/` genau einmal aus.

[EC] Probieren Sie den Endpunkt `/hello` genau einmal ohne Parameter und einmal
mit Ihrem Namen aus.

[EC] Probieren Sie den `/grades` Endpunkt einmal aus.

[EC] Probieren Sie den Endpunkt `/students` und `/courses` jeweils einmal aus.

[EC] Probieren Sie den Endpunkt `/student/{name}` jeweils einmal aus mit dem Namen
`Alice` und `Bob` aus.

[EC] Probieren Sie den Endpunk `/course/{name}` jeweils einmal aus mit dem Namen
`Math` und `Physics` aus.

[ENDSECTION]


[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]

[INCLUDE::ALT:FastAPI-GET.md]

### Kommandoprotokoll

[PROT::ALT:FastAPI-GET.prot]

Musterlösung siehe [TREEREF::/Bibliotheken/Frameworks/FastAPI-GET.py]
[ENDINSTRUCTOR]
