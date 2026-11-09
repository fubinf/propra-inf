title: "REST: Architekturstil für Web-APIs"
stage: alpha
timevalue: 1.0
difficulty: 2
explains: REST, Endpunkt, Swagger
assumes: http-Status, http-State
---

[SECTION::goal::idea]

- Ich kann eine Operation in der SwaggerUI erbropen und die Spezifikation lesen.
- Ich verstehe REST als Architekturstil und kann die wichtigsten REST-Bedingungen benennen.
- Ich kann den Aufbau einer REST-API (Ressourcen, Endpunkte, Methoden) lesen und einordnen.
- Ich kann den unterschied zwischen REST und HTTP erklären.

[ENDSECTION]


[SECTION::background::default]
Moderne Web-APIs folgen überwiegend dem Architekturstil [TERMREF::REST].
Die Bausteine [TERMREF::HTTP]-Methoden, [TERMREF::HTTP-Statuscode]s und
die Zustandslosigkeit von [TERMREF::HTTP] haben Sie bereits einzeln kennengelernt.
An dieser Stelle werden Sie diese Bausteine zu dem Gesamtbild zusammensetzen,
das Ihnen anschließend in vielen APIs begegnet,
die Sie benutzen, bauen (beispielsweise in [PARTREF::FastAPI-GET]) oder testen.
[ENDSECTION]


[SECTION::instructions::loose]


### Eine REST-API benutzen

Öffnen Sie die Seite [Swagger-Petstore](https://petstore.swagger.io).
Dies ist die grafische Darstellung der Petstore API.
Öffnen Sie dort die Operation `GET /pet/findByStatus`.
Sie können diese mit dem Button "Try it out" und anschließend "Execute" ausprobieren.

- [EQ] Nennen Sie welche HTTP-Methode verwendet und welcher HTTP-Statuscode
in der Antwort zurückgesendet wird.

[HINT::Fehlermeldung `For 'status': Required field is not provided.`]
Diese Operation erwartet, dass Sie einen Status auswählen, nach welchem gefiltert werden soll.
Wählen Sie unter `Parameters` `status` einen der drei Werte aus und klicken Sie
erneut auf "Execute".
[ENDHINT]

Sie haben die REST-API Petstore erfolgreich verwendet.
Die Oberfläche, die Sie auf der Webseite sehen ist nicht REST, sondern die
[TERMREF2::Swagger::SwaggerUI], die die in JSON gespeicherte [TERMREF::OpenAPI]-Spezifikation
darstellt.
Die JSON-Datei finden Sie am Anfang der Seite unter der Überschrift
[HREF::https://petstore.swagger.io/v2/swagger.json].
[TERMREF::OpenAPI] ist ein weit verbreiteter Standard zur Darstellung und Dokumentation einer REST-API.

<!-- time estimate: 5 min -->


### Eine API Spezifikation lesen

In einer OpenAPI-Spezifikation werden API-Funktionen über Pfade und HTTP-Methoden beschrieben.
Je Pfad können mehrere unterschiedliche HTTP-Methoden verfügbar sein.
Die Kombination von Pfad, HTTP-Methode und Pfadparametern wird in [TERMREF::Swagger] *Operation*
genannt.

[NOTICE]
In der SwaggerUI wird jede Operation als eigener Punkt dargestellt.
In der JSON-Datei sehen Sie dagegen, dass je Pfad mehrere Operationen stehen können.

Diese Trennung ist in der SwaggerUI nötig, weil sich jede Operation einzeln
mit dem "Try it out"-Button ausprobieren lässt.
[ENDNOTICE]

Je Operation sehen Sie in [TERMREF::Swagger], ...

- welche Parameter möglich und welche erforderlich sind.
- welche Daten und HTTP-Statuscodes als Antwort gesendet werden können.

zusätzlich wenn Sie die Operation ausprobieren auch

- wie die HTTP-Anfrage (Request) aussah.
- welche HTTP-Antwort (Response) (Header + Body) vom Server zurückgesendet wurde.


- [EQ] Betrachten Sie sich die Operation GET `/pet/{petId}`.
  Welche Parameter können angegeben werden und welche Antworten sind möglich?
  Nennen Sie jeweils den HTTP-Statuscode und das Schema der Daten?

<!-- time estimate: 10 min -->


### Was REST ist (und was nicht)?

Lesen Sie den Glossareintrag [TERMREF::REST] sowie als vertiefende Quelle den Abschnitt
"Guiding Principles of REST" auf
[restfulapi.net](https://restfulapi.net/).

- [EQ] Nennen Sie die REST-Bedingungen und erklären Sie zwei in je einem Satz von diesen
  mit eigenen Worten anhand jeweils einer Operation der Petstore-API.

- [EQ] Eine der REST-Bedingungen kennen Sie als HTTP-Eigenschaft bereits aus [PARTREF::http-State].
  Erklären Sie welche es ist und was sie für einen einzelnen Request konkret bedeuten.
  Nennen Sie eine Operation in Petstore an der dies deutlich wird.

- [EQ] REST und HTTP unterscheiden sich.
  Nennen Sie etwas,  das REST fordert, aber HTTP nicht erzwingt.

<!-- time estimate: 20 min -->


### Ressourcen und Endpunkte

Lesen Sie den Abschnitt "What is a Ressource?" auf
[restfulapi.net](https://restfulapi.net/resource-naming/).
Ressourcen können alle Informationen sein, die über die API erreichbar sein sollen.

Die Operationen der API werden über unterschiedliche Pfade und HTTP-Methoden erreicht.
Die Kombination der Basis URL und des Pfads heißt [TERMREF::Endpunkt].
Endpunkte sollten nicht direkt nach der Aktion die passiert benannt werden, sondern
nach der Ressource, mit welcher gearbeitet wird.
Die Aktion sollte folglich nicht durch den Endpunkt beschrieben werden.
Es handelt sich hierbei nur um Konventionen, die nicht erzwungen werden können.
Lesen Sie nun den Abschnitt "Best Practices" auf der gleichen Seite, in dem
die üblichen REST Namenskonventionen angegeben sind.

- [EQ] Die verbreitete Namenskonvention empfiehlt Ressourcennamen im Plural (`/pets`).
  Sehen Sie sich den [Swagger-Petstore](https://petstore.swagger.io) an:
  Welche Schreibweise benutzt er?
  Wie passt das zur Konvention?

<!-- time estimate: 15 min -->


### CRUD und die HTTP-Methoden

Viele REST-APIs nutzen als Transportprotokoll HTTP.
Für unterschiedliche Aktionen auf einer Ressource können einzelne HTTP-Methoden
zugeordnet werden.

- [EQ] Schauen Sie sich die Endpunkte in der Gruppe `pet` an und ordnen Sie die
  vier [TERMREF::CRUD]-Operationen den einzelnen Operationen in dieser Gruppe zu.
  An welcher Stelle gibt es Unterschiede zur Zuordnung im Glossar?

Erstellen Sie nun ein eigenes eigenes `Pet` mit der Operation `POST /pet`.
Wenn Sie eine Operation ausprobieren, füllt Swagger den Body bereits mit Beispieldaten aus.
Aktualisieren Sie anschließend Ihr erstelltes `Pet` mit der Operation `PUT /pet`.
Sie dafür im Body die `id` Ihres `Pet` anpassen und eine Änderung vornehmen,
beispielsweise indem Sie den Namen ändern.

- [EQ] Wie unterscheiden sich die verwendeten Operationen `PUT` und `POST`?
  Erläutern Sie den Unterschied mithilfe des Begriffs [TERMREF::Idempotenz].

Allerdings ist auch dies nur Konvention, die Idempotzens muss serverseitig implementiert werden.
Aktualisieren Sie ihr `Pet` erneut und nutzen dieses mal die Operation `POST /pet`.
Dies geht in Petstore problemlos, ist aber eher untypisch in REST-APIs.
REST gibt Konventionen für Operationen vor, kann diese aber nicht garantieren.

<!-- time estimate: 10 min -->

[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Prüfhilfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]

