title: "FastAPI-CRUD"
stage: beta
timevalue: 1.5
difficulty: 2
explains:
assumes: m_datetime, http-POST, http-Status
requires: FastAPI-GET
---


[SECTION::goal::trial]
Ich kann mit FastAPI eine [TERMREF::REST-API] mit CRUD-Endpunkten bereitstellen:
Erstellen, Lesen, Aktualisieren und Löschen von Daten.
[ENDSECTION]


[SECTION::background::default]
In vielen Webanwendungen werden Daten über standardisierte HTTP-Operationen verwaltet.
Mit FastAPI ist es nur wenig Aufwand, die [TERMREF::CRUD]-Funktionalität in diesem Stil umzusetzen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

Kopieren Sie als Startpunkt den Quellcode aus der Aufgabe [PARTREF::FastAPI-GET] in `FastAPI-CRUD.py`.


### `C`: Create

In einer REST-API wird eine POST-Anfrage gesendet, um eine neue Ressource zu erstellen.
Die HTTP-Methode, auf die ein Endpunkt reagiert, kann im Dekorator angegeben werden.
Bei einer GET-Anfrage wird die Funktion mit `@app.get("/pfad")` dekoriert.
Dies funktioniert für andere HTTP-Methoden analog.
Für eine POST-Anfrage kann dementsprechend `@app.post("/pfad")` genutzt werden.

[ER] Erstellen Sie einen neuen POST-Endpunkt `create_grade_entry()` mit dem Pfad `/grade`.
Schreiben Sie in der Funktion vorerst `pass`, damit Sie das Programm ausführen können
und öffnen Sie diesen Endpunkt in der interaktiven Dokumentation.

Sie sehen, dass der neue Endpunkt bei Erfolg mit Code `200` antwortet.
Auf eine POST-Anfrage wird [PARTREFMANUAL::http-Status::wie sie wissen]
in der Regel aber nicht `200` geantwortet,
sondern `201`, mit der Bedeutung `Created`.

[ER] Lesen Sie in der
[FastAPI Dokumentation](https://fastapi.tiangolo.com/tutorial/response-status-code/),
wie Sie mit Code `201` antworten können und ergänzen Sie dementsprechend Ihren Endpunkt.

Es ist üblich, dass bei einer POST-Anfrage bei Erfolg das vollständige Objekt, das
erstellt wurde, zurückgesendet wird.
Dadurch können Missverständnisse darüber, wie die Objekte auf dem Server gespeichert wurden,
vermindert werden.

[ER] Ergänzen Sie als Rückgabetyp `GradeEntry`, damit in der Dokumentation das
korrekte Schema angezeigt wird.



[ER] In einer POST-Anfrage sendet man in der Regel Daten im Rumpf der Anfrage mit.
Ergänzen Sie in `create_grade_entry()` das Argument `data: GradeEntry`
und schauen Sie sich den Endpunkt erneut in der Dokumentation an.

Sie sehen nun, dass ein "Request Body" erwartet wird und durch welches Schema sich
dieser auszeichnet.
Anders als bei einem GET-Endpunkt wird das Argument `data` nicht in der _Query_,
sondern im _Body_ erwartet.
Durch die Datenvalidierung durch _Pydantic_ ist es nicht möglich, falsche Datentypen anzugeben.

[ER] Ergänzen Sie nun die Logik, die `data` in die Liste `fake_db` hinzufügt.

Wenn Sie nun einen Test-Eintrag hinzufügen, können Sie sowohl mehrfach
den gleichen Eintrag erstellen, als auch `date` selbst festlegen.
Häufig ist es nicht erwünscht, dass beim Erstellen alle Parameter vom Client festgelegt
werden.
So soll `date` verlässlich das Datum sein, an welchem der Eintrag erstellt wurde.

[ER] Es ist folglich notwendig, dass ein anderes Schema für die Daten, die im Endpunkt
übergeben werden können, erstellt wird.
Erstellen Sie eine neue Klasse `GradeEntryCreate(BaseModel)` und ergänzen Sie die
Attribute `name: str`, `course: str` und `grade: float`.
Ändern Sie den Datentyp von `data` zu `GradeEntryCreate`.

[ER] Passen Sie nun die Logik des Endpunktes so an, dass die folgenden Kriterien erfüllt werden:

- `date` wird auf das aktuelle Datum gesetzt.
  Dafür können sie `now()` aus dem `datetime` Module nutzen.
- Ein neuer Eintrag darf nur erstellt werden, wenn die Kombination aus `name` und `course`
  noch nicht existiert.
  Falls doch, nutzen Sie `raise ValueError("Entry already exists.")`, um einen Fehler zu werfen.
- Bei Erfolg, soll das erstellte `GradeEntry`-Exemplar zurückgegeben werden.

[ER] Probieren Sie Ihren Endpunkt einmal aus, und prüfen Sie mit Ihrem `/grades` Endpunkt,
ob der neue Eintrag erstellt wurde.
Versuchen Sie danach den bereits erstellten Eintrag erneut anzulegen.

Sie sehen, dass beim erneuten Hinzufügen nun der Code `500` zurückgeben wird.
Dies ist falsch, da die betreffende Ausnahme ja nicht aus Versehen,
sondern gewollt erzeugt wurde.

[ER] Lesen Sie in der FastAPI Dokumentation nach, wie Sie
[eigene Fehlercodes senden](https://fastapi.tiangolo.com/tutorial/handling-errors/#use-httpexception)
können.
Ändern Sie entsprechend, dass dort der Code `409` geantwortet wird.


### `R`: Read

Die Endpunkte, mit denen die Daten gelesen werden können, wurden bereits in der
vorherigen Aufgabe erstellt.
Daher ist hier nichts weiter zu tun.


### `U`: Update

`PUT` und `PATCH` sind die beiden HTTP-Methoden, um Einträge zu aktualisieren.
Bei einer PUT-Anfrage muss der vollständige Eintrag gesendet werden.
Wenn mehrfach dieselbe PUT-Anfrage gesendet wurde, ändert sich der Gesamtzustand nicht.

Bei einer PATCH-Anfrage werden nur die angegeben Felder geändert.
Wenn mehrfach dieselbe PATCH-Anfrage gesendet wird, können dennoch unterschiedliche
Antworten folgen.

Das Datum `date` soll auch bei einer Änderung vom Server aktualisiert werden.
Folglich sollten Änderungen an einem Eintrag mit einer PATCH-Anfrage aktualisiert werden,
da bei jeder Aktualisierung, immer wieder das Datum geändert wird.
Dieses Verhalten könnte man mit einer PUT-Anfrage nicht normkonform umsetzten.

[ER] Erstellen Sie einen neuen PATCH-Endpunkt `update_grade_entry()` mit dem Pfad
`/grade` und dem Argument `data: GradeEntryCreate`.
Ergänzen Sie die Logik:

- `date` soll auf das aktuelle Datum aktualisiert werden.
- Falls der Eintrag noch nicht existiert, soll Code `404` gesendet werden.
- Bei Erfolg soll das `GradeEntry`-Exemplar in `fake_db` gespeichert und zurückgesendet werden.

[NOTICE]
Sie sehen in der Dokumentation, dass Sie mittlerweile zwei Endpunkte mit dem gleichen Pfad
`/grade` erstellt haben.
Dennoch funktionieren Beide und es sind keine Fehler vorhanden.
Ursächlich dafür ist, dass die beiden Endpunkte unterschiedliche HTTP-Methoden verwenden
und deswegen vom Server unterschieden werden können.
[ENDNOTICE]


### `D`: Delete

Zuletzt fehlt ein Endpunkt, um Einträge wieder löschen zu können.
Dafür kann die HTTP-Methode DELETE genutzt werden.

[ER] Erstellen Sie einen neuen DELETE-Endpunkt `delete_grade_entry()` mit
dem Pfad `/grade`. Ergänzen Sie die beiden Parameter `student_name` und `course_name`
als Query-Parameter, um den Eintrag identifizieren zu können.
Falls der Eintrag nicht existiert, soll der Fehler `404` geantwortet werden.
Bei Erfolg soll diesmal der Code `204` ohne Daten zurückgegeben werden.

---

Zum Abschluss der Aufgabe werden nun die einzelnen Endpunkte jeweils einmal
aufgerufen und in einem Kommandoprotokoll erfasst.

[ER] Beenden Sie Ihre Server. Dazu können Sie in der Konsole, in der der Server
läuft, <kbd>Strg</kbd>+<kbd>c</kbd> eingeben.

[EC] Starten Sie den Server mit `fastapi dev FastAPI-CRUD.py` und öffnen Sie
die automatische Dokumentation in ihrem Browser.
Führen Sie nun nacheinander diese Aktionen aus:

- Erstellen Sie zweimal dasselbe Exemplar über Ihren POST-Endpunkt `/grade`.
- Aktualisieren Sie das Exemplar über Ihren PATCH-Endpunkt `/grade`.
- Versuchen Sie nun ein Exemplar, das nicht existiert, über Ihren
PATCH-Endpunkt `/grade` zu aktualisieren.
- Löschen Sie nun ein Exemplar über Ihren DELETE-Endpunk `/grade`.

[ENDSECTION]


[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

<!-- @PROGRAM_TEST_SKIP: reason="Output contains uncontrollable status codes and timestamps" manual_test_required=true -->

[INSTRUCTOR::Codedurchsicht]

[INCLUDE::ALT:FastAPI-CRUD.md]


### Musterlösung

Musterlösung siehe [TREEREF::FastAPI-CRUD.py]

```py
[INCLUDE::ITREE:FastAPI-CRUD.py]
```

[ENDINSTRUCTOR]
