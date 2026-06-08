title: "Blackbox-Testing einer REST-API über den CRUD-Lebenszyklus"
stage: draft
timevalue: 1.5
difficulty: 3
assumes: pytest-Methodik-Blackbox, m_requests, m_json, http-REST
---

<!--
SKIZZE — bitte ausarbeiten.
Dies ist die EINE Task mit echter Eigensubstanz aus der aufgelösten Taskgroup Testen/API.
Sie gehört hierher, weil REST-API-Testen ein Spezialfall des Blackbox-Testens ist
(testen gegen die Spezifikation / das beobachtbare Verhalten, Server-Interna unbekannt).
Voraussetzung pytest-Methodik-Blackbox liefert die Methodik, m_requests/m_json die Mechanik,
http-REST das Domänenwissen — all das hier NICHT wiederholen, sondern voraussetzen.

Kern (der eigentliche didaktische Wert): EIN zusammenhängender Test, der den gesamten
Lebenszyklus eines Objekts an einem Endpunkt durchspielt und nach jedem Schritt per
assert das beobachtbare Verhalten prüft:

    GET (erwartet 404)  -> POST (anlegen, ID aus Response einfangen)
    -> GET (erwartet 200, Felder prüfen)  -> Felder ändern -> PUT (aktualisieren)
    -> GET (erwartet geänderte Werte)  -> DELETE  -> GET (erwartet wieder 404)

Wichtige Punkte für die Ausarbeitung:
- Mit POST statt PUT anlegen ist realistischer (Server vergibt die ID), zwingt aber dazu,
  die zurückgegebene ID aus dem JSON-Response zu extrahieren und durch die Folge-Requests
  zu fädeln. Genau das ist die Substanz — bitte so gestalten, nicht mit fester ID abkürzen.
- Assertions auf HTTP-Statuscodes UND auf Response-Felder (nicht nur "lief durch").
- Negativtests einbauen (GET/DELETE auf nicht existierende ID -> 404; ggf. 403-Überlegung
  aus der alten ResponseApi hier aufgehen lassen).
- pytest-Fixture für Setup/Teardown (sicherstellen, dass das Testobjekt am Ende gelöscht ist),
  damit der Test wiederholbar ist (Stichwort Idempotenz der Testumgebung).
- Hinweis auf die Flakiness der öffentlichen Petstore-API: ein selbst gebauter FastAPI-Service
  ([PARTREF::FastAPI-CRUD]) wäre die stabilere Zieladresse — als optionale Variante anbieten.
Schwierigkeitsgrad 3: ein Hinweis genügt, wie man den richtigen Doku-Abschnitt findet;
nicht jeden Schritt vorkauen.
-->

[SECTION::goal::experience]

- Ich kann eine REST-API als Blackbox systematisch testen.
- Ich kann den vollständigen CRUD-Lebenszyklus eines Objekts in einem zusammenhängenden Test
  prüfen und dabei Statuscodes und Antwortdaten per `assert` verifizieren.

[ENDSECTION]
[SECTION::background::default]

Das Testen einer [TERMREF::REST]-API ist ein Spezialfall des Blackbox-Testens
([PARTREF::pytest-Methodik-Blackbox]): Sie prüfen das beobachtbare Verhalten gegen die
Spezifikation, ohne den Server-Code zu kennen.
Besonders aussagekräftig wird das, wenn ein einzelner Test ein Objekt durch seinen ganzen
Lebenszyklus begleitet — vom Anlegen über Lesen und Ändern bis zum Löschen — und nach jedem
Schritt prüft, ob der Server sich erwartungsgemäß verhält.

[ENDSECTION]
[SECTION::instructions::tricky]

### Testplan für den Lebenszyklus
<!-- time estimate: 20 min -->

<!-- TODO(Ah3n0): Studierende einen Testplan für eine Petstore-Ressource (z.B. /pet) entwerfen
     lassen, der die volle CRUD-Sequenz inkl. der erwarteten Statuscodes je Schritt auflistet. -->

- [ER] Erstellen Sie als Markdown-Tabelle einen Testplan für den Lebenszyklus eines `pet`:
  je Zeile die Aktion (HTTP-Methode + Endpunkt), die mitgegebenen Daten und den erwarteten
  Statuscode. Beginnen und enden Sie mit einem Lese-Versuch auf eine nicht existierende ID.

### Den Lebenszyklus-Test schreiben
<!-- time estimate: 50 min -->

<!-- TODO(Ah3n0): Gerüst vorgeben (Funktions-/Variablennamen festlegen, A6.6), aber die
     Implementierung der einzelnen Schritte den Studierenden überlassen. Kernpunkte oben. -->

- [ER] Schreiben Sie in `test_pet_lifecycle.py` einen pytest-Test, der Ihren Testplan umsetzt:
  Legen Sie ein `pet` per `POST` an, fangen Sie die vom Server vergebene `id` aus dem
  [TERMREF::Response] ein und verwenden Sie sie in allen Folge-Requests.
  Prüfen Sie nach jedem Schritt per `assert` den Statuscode und — wo sinnvoll — einzelne Felder.

- [ER] Ergänzen Sie eine pytest-Fixture, die das Testobjekt am Ende zuverlässig löscht
  (Teardown), damit der Test wiederholbar bleibt.

- [EQ] Warum ist es wichtig, dass Ihr Test nach Abschluss keinen Zustand hinterlässt?
  Welche REST-Bedingung und welcher Begriff aus [TERMREF::Idempotenz] helfen beim Argumentieren?

### Negativtests
<!-- time estimate: 20 min -->

- [ER] Ergänzen Sie Tests für Fehlerfälle: ein `GET` und ein `DELETE` auf eine garantiert nicht
  existierende `id`. Welcher Statuscode wird erwartet?

- [EC] Führen Sie alle Tests aus und dokumentieren Sie das Ergebnis im Protokoll.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
