title: "FastAPI Dependency Injection"
stage: alpha
timevalue: 1
difficulty: 2
requires: FastAPI-GET
---


[SECTION::goal::idea]

Ich kann eine Abhängigkeit (Dependency) erstellen, um eine gemeinsame Funktionalitäten
in mehreren Endpunkten bereitzustellen.

[ENDSECTION]


[SECTION::background::default]

In einer wachsenden Anwendung ist es wichtig, wiederkehrende Funktionalitäten bzw.
Abhängigkeiten zentral zu lösen, um dies nicht in mehreren Endpunkt wiederholen zu müssen.

In FastAPI gibt es mit dem Konzept der _Dependency Injection_ einen komfortablen Weg,
mehreren Endpunkten eine Abhängigkeit bereitzustellen.

_Dependency Injection_ bedeutet, dass eine ein Endpunkt bestimmte Werte oder Objekte
nicht selbst erstellt, sondern diesem automatisch bereitgestellt werden.

[ENDSECTION]


[SECTION::instructions::detailed]


### Vorbereitung

Kopieren Sie als Startpunkt den Quellcode aus der Aufgabe [PARTREF::FastAPI-GET]
in `FastAPI-Dependency-Injection.py`.


### Pagination

Eine typischer Anwendungsfall in einer REST-API ist das Aufteilen der Antwort auf mehrere Seiten.
Das wird vor allem notwendig, wenn die Antwortliste nicht nur wenige sondern eine
große Anzahl Einträge enthält.
Wenn diese Antwort nun jeweils 100 Einträge pro Seite enthält, wird die Antwortzeit
deutlich reduziert.
Dieses Aufteilen wird auch _Pagination_ genannt.

[ER] Ergänzen Sie die beiden _Query_-Parameter `page: int` und `limit: int` im
Endpunkt `/grades`.
`page` ist die Seitenanzahl und `limit` die Anzahl der Elemente pro Seite.
Passen Sie die Logik ihres Endpunkt so an, dass nur der entsprechende Ausschnitt
aus der Liste zurückgegeben wird.
Wenn die letzte Seite (oder darüber hinaus) erreicht wurde, soll kein Fehler geworfen
werden, sondern lediglich eine leere Liste zurückgegeben werden.

Diese beiden Parameter sind nun notwendig, damit die Anfrage nicht scheitert.
Dieses Verhalten funktioniert zwar, ist jedoch umständlich.

[ER] Probieren den Endpunkt aus und testen Sie unterschiedliche Werte, wie beispielsweise
sehr große oder negative Zahlen, zu übergeben.

Sie sehen, dass es problemlos möglich ist, `limit` auf `1.000.000` zu setzen.
Solch große Antworten senden zu müssen, sollte dennoch verhindert werden.
Auch negative Werte funktionieren, sind aber in praktischen APIs häufig nicht erwünscht.

[ER] Lesen Sie in der FastAPI Dokumentation, wie Sie
[`Query`-Parameter mit Validierung](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
definieren können.
Lesen Sie dazu auch, wie
[nummerische Grenzen](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-or-equal)
gesetzt werden können.

[ER] Ergänzen Sie folglich geeignete Grenzen und Standardwerte.
Da `fake_db` nur sehr kurz ist, setzen Sie `page` auf `0` und `limit` auf `2`.
Wobei `page` größer gleich `0` sein sollte und `limit` größer `0` und kleiner gleich `10`.

[ER] Probieren Sie Ihren Endpunkt und die Parameter mit Grenzwerten aus.


### Dependency Injection

Nun haben Sie bei einem Endpunkt erfolgreich _Pagination_ implementiert.
Um das gleiche Verhalten auf weitere Endpunkte zu übertragen, müssten Sie nun die
Parameter kopieren und bei einem anderen Endpunkt einfügen.
Wenn Sie daraufhin Grenzen oder die Standardwerte ändern wöllten, müssten Sie dies bei allen
Endpunkten manuell durchführen.
Dies kann zu Inkonsistenz führen, was unerwünscht ist.

Stattdessen bietet FastAPI die Möglichkeit diese Parameter als _Abhängigkeit_ den
Endpunkten bereitzustellen.
Dazu muss eine eigene Funktion erstellt werden, in der die Parameter definiert und
auch notwendiger Code ausgeführt werden kann.

[ER] Lesen Sie auf der Seite
["Dependencies"](https://fastapi.tiangolo.com/tutorial/dependencies/)
in der FastAPI Dokumentation, wie sie Dependencies erstellen und nutzen können.

[ER] Erstellen Sie die Klasse `Pagination(BaseModel)` mit den Attributen
`page: int` und `limit: int`.
Ergänzen Sie in dieser Klasse mit dem
[`@property`-Decorator](https://docs.python.org/3/library/functions.html#property)
`start` und `end`, die aus `page` und `limit` berechnet werden sollen.

[ER] Erstellen Sie analog dazu die Funktion `pagination_params` und definieren Sie
dort als Argumente `page` und `limit`, wie Sie es im Endpunkt durchgeführt haben.
Die Funktion soll `Pagination` mit `page` und `limit` erzeugen und zurückgeben.

[ER] Erstellen Sie die Dependency `PaginationDep`, wie es in "Share Annotated dependencies"
beschrieben ist.

[ER] Verwenden Sie nun die Dependency `PaginationDep` in ihrem Endpunkt `/grades`.

Sie können nun diese Dependency auch in anderen Endpunkten verwenden.
Allerdings wird Sie nicht automatisch in einem Endpunkt verwendet.

[ER] Ändern Sie die Endpunkte `/students` und `/courses` so, dass diese auch
Pagination unterstützen.

[EQ] Nennen Sie eine weitere Nutzungsmöglichkeiten der Dependency Injection im Programm.

---

Zum Abschluss der Aufgabe werden nun die einzelnen Endpunkte jeweils einmal
aufgerufen und in einem Kommandoprotokoll erfasst.

[ER] Beenden Sie Ihre Server. Dazu können Sie in der Konsole, in welcher der Server
läuft, <kbd>Strg</kbd>+<kbd>c</kbd> eingeben.

[EC] Starten Sie den Server mit `fastapi dev FastAPI-Dependency-Injection.py` und
öffnen Sie die automatische Dokumentation in ihrem Browser.
Rufen Sie anschließend die folgenden Endpunkte jeweils einmal auf:

- `/grades`
- `/grades?page=1&limit=5`
- `/grades?page=0&limit=20`
- `/students`
- `/students?page=1&limit=5`
- `/courses`
- `/courses?page=1&limit=5`

[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Codedurchsicht]

[INCLUDE::ALT:FastAPI-Dependency-Injection.md]

### Musterlösung

Musterlösung siehe [TREEREF::FastAPI-Dependency-Injection.py]

```py
[INCLUDE::ITREE:FastAPI-Dependency-Injection.py]
```

[ENDINSTRUCTOR]
