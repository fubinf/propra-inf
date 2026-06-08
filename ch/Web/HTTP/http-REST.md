title: "REST: Architekturstil für Web-APIs"
stage: draft
timevalue: 1.0
difficulty: 2
explains: REST, Endpunkt
assumes: http-Status, http-State
---

<!--
SKIZZE — bitte ausarbeiten.
Diese Task bündelt die REST-Konzepte, die bisher verstreut (und dupliziert) in der
aufgelösten Taskgroup Testen/API steckten. Sie gehört konzeptionell ins Kapitel Web,
weil REST ein Architekturthema ist und kein Testthema.
Ziel: Studierende verstehen REST als Architekturstil, können eine vorhandene REST-API
(Aufbau, Endpunkte, Methoden) lesen und haben eine existierende ausprobiert.
Das sollte vmtl. assumes m_request machen und ähnlichen Code als Basis vorgeben wie weiland in Testen/API/RestApi.
pytest-Methodik-REST baut hierauf auf.
Das meiste HTTP-Vorwissen (Methoden, Statuscodes, Zustandslosigkeit) ist bereits durch
http-GET/http-POST/http-Status/http-State abgedeckt — also NICHT erneut erklären,
sondern per PARTREF darauf verweisen und hier nur die REST-Klammer darüber legen.
Die Aufgabenvorschläge unten sind viel zu viel Theorie (stark ausdünnen!) und noch keine Praxis (ergänzen!).
Schwierigkeitsgrad 2: schrittweise anleiten, präzise Doku-Koordinaten angeben.
-->

[SECTION::goal::idea]

- Ich verstehe REST als Architekturstil und kann die wichtigsten REST-Bedingungen benennen.
- Ich kann den Aufbau einer REST-API (Ressourcen, Endpunkte, Methoden) lesen und einordnen.
- Ich kann erklären, warum REST und HTTP nicht dasselbe sind.
[ENDSECTION]


[SECTION::background::default]
Moderne Web-APIs folgen überwiegend dem Architekturstil [TERMREF::REST].
Sie haben die Bausteine — [TERMREF::HTTP]-Methoden, [TERMREF::HTTP-Statuscode]s und
die Zustandslosigkeit von [TERMREF::HTTP] — bereits einzeln kennengelernt.
Hier setzen wir sie zu dem Gesamtbild zusammen, das Ihnen anschließend in jeder API begegnet,
die Sie benutzen, bauen ([PARTREF::FastAPI-GET]) oder testen.
[ENDSECTION]


[SECTION::instructions::loose]

### Was REST ist (und was nicht)

<!-- TODO(Ah3n0): kurze, präzise Einführung; das Glossar liefert die Definition. -->
Lesen Sie den Glossareintrag [TERMREF::REST] sowie als vertiefende Quelle den Abschnitt
"Guiding Principles of REST" auf
[restfulapi.net](https://restfulapi.net/).

- [EQ] Nennen Sie die REST-Bedingungen und erklären Sie zwei davon in je einem Satz
  mit eigenen Worten.

- [EQ] Eine der REST-Bedingungen kennen Sie als HTTP-Eigenschaft bereits aus [PARTREF::http-State].
  Welche ist es, und was bedeutet sie konkret für einen einzelnen Request?

- [EQ] Begründen Sie: Warum sind REST und HTTP nicht dasselbe?
<!-- time estimate: xx min -->

### Ressourcen und Endpunkte

<!-- TODO(Ah3n0): Begriff Endpunkt einführen (Glossar [TERMREF::Endpunkt]).
     Hier den Singular/Plural-Punkt SAUBER aufnehmen: restfulapi.net empfiehlt Plural (/pets),
     viele reale APIs (z.B. der Swagger-Petstore) benutzen aber Singular (/pet).
     Das ist ein lehrreicher Konvention-vs-Realität-Punkt — als solchen rahmen, nicht als Fehler. -->

- [EQ] Wie ist ein REST-[TERMREF::Endpunkt] aufgebaut (Basis-URL + Ressourcenpfad)?
  Geben Sie ein Beispiel an.

- [EQ] Die verbreitete Namenskonvention empfiehlt Ressourcennamen im Plural (`/pets`).
  Sehen Sie sich den [Swagger-Petstore](https://petstore.swagger.io) an: Welche Schreibweise
  benutzt er? Wie passt das zur Konvention zusammen?
<!-- time estimate: xx min -->

### CRUD und die HTTP-Methoden

<!-- TODO(Ah3n0): die zentrale Abbildung CRUD <-> HTTP-Methoden herausarbeiten.
     Glossar: [TERMREF::CRUD], [TERMREF::Idempotenz]. Methoden sind aus http-GET/http-POST bekannt. -->

- [EQ] Ordnen Sie die vier [TERMREF::CRUD]-Operationen den HTTP-Methoden
  `POST`, `GET`, `PUT`, `DELETE` zu.

- [EQ] Worin unterscheiden sich `PUT` und `POST`?
  Erläutern Sie den Unterschied mit Hilfe des Begriffs [TERMREF::Idempotenz]
  und je einem konkreten Beispiel-Endpunkt.
<!-- time estimate: xx min -->

### Eine reale REST-API lesen

<!-- TODO(Ah3n0): kleine praktische Lese-/Orientierungsübung am Petstore,
     damit die Theorie konkret wird (A3.6: der Effekt soll sichtbar sein).
     NOCH KEIN requests-Code — das gehört nach m_requests / pytest-Methodik-REST. -->

- [EQ] Welche Ressourcen-Kategorien (z.B. `/pet`, `/store`, `/user`) bietet der Petstore an,
  und welche HTTP-Methoden sind je verfügbar? Nennen Sie pro Kategorie mindestens zwei.
<!-- time estimate: xx min -->
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Prüfhilfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
