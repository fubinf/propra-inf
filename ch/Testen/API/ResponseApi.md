title: API Antworten verarbeiten
stage: draft
timevalue: 0
difficulty: 3
assumes: RestApi, m_json1
---
[SECTION::goal::idea]

- Ich kann nach einem Request den erhalten [TERMREF::JSON] Response verarbeiten
- Ich kann das Ergebnis automatisiert [TERMREF::verifizieren]

[ENDSECTION]
[SECTION::background::default]

Mit einem API [TERMREF::Request] erhält man unterschiedliche Antworten zurück. Neben dem [TERMREF::HTTP-Statuscode],
werden [TERMREF::Header-Metadaten] und manchmal auch [TERMREF::Response]-Daten zurückgegeben.

[ENDSECTION]
[SECTION::instructions::tricky]

Wenn wir einen API Request absetzen, wollen wir oftmals direkt erfahren, welchen HTTP-Statuscode wir erhalten haben.

- [EQ] Welche Bedeutung haben die folgenden Statuscode-Berieche: `2xx`, `3xx`, `5xx`?
- [EQ] Was bedeuten die spezifischen Statuscodes `201`, `404`, `503`?
- [EQ] Wenn ein API-Negativtest einen Statuscode `403` liefert, ist er dann fehlgeschlagen?

Wir werden uns einen echten JSON Response aus dem Netz holen und im folgenden verarbeiten. Betrachten Sie dazu die
uns bereits bekannte [Petstore-Seite](https://petstore.swagger.io).

[ER] Erstellen Sie ein Python Script zum Abfragen des `GET`-Petstore-Endpunkt `/pet/findByStatus` mit einem beliebigen Status
`available`, `pending`, oder `sold` aus.

In einem Regressionstest möchte man gerne auf Aktionen aufbauen, die bestimmte Daten erzeugen, manipulieren oder einfach nur
Daten auslassen. Daher werden wir mit diesem Response weiter arbeiten und die erhaltenen Daten etwas verfeinern.

- [ER] Erweitern Sie den Code und filtern Sie den Statuscode aus dem Response.
- [EQ] Warum ist der Statuscode `200` und nicht `201`?

In dem erhaltenen Response ist ein Array enthalten. Dieses Array besitzt JSON Objekte. Wir wollen einen Blick auf alle
erhaltenen Werte des Feldes `id` werfen. 
Nutzen Sie das [PARTREFMANUAL::m_json1::json]-Modul, um an diese Informationen heranzukommen.

- [ER] Filtern Sie alle erhaltenen `id`-Werte aus dem Response.
- [ER] Erweitern Sie den Code so, dass alle Werte in einem Array stehen.

Jetzt wollen wir diese Werte an einer anderen Schnittstelle anwenden.

- [ER] Erstellen Sie ein Python Script zum Abfragen der `GET`-Petstore-Schnittstelle `/pet/{tId}`.
- [EC] Verwenden Sie den unter [EREFR::5] erstellten Code mit allen unter [EREFR::4] erzeugten id's.
- [EQ] Gibt es einen Statuscode ungleich `200`? Falls ja, warum, falls nein, warum nicht?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::heading]

- [EREFQ::5] Hier sollte die Antwort nein sein, da alle ID's vorab abgefragt wurden. Falls doch ja heraus kommt, kann es zu einer Überschneidung mit einem anderen Nutzer geben, der dieses Objekt verändert hat.

[ENDINSTRUCTOR]
