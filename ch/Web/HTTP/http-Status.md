title: HTTP-Statuscodes verstehen und klassifizieren
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: http-GET, http-POST
---

[SECTION::goal::idea]
Ich verstehe die Bedeutung und Klassifizierung von HTTP-Statuscodes 
und kann häufige sowie spezielle Codes korrekt interpretieren.
[ENDSECTION]

[SECTION::background::default]
Jeder HTTP-Request wird mit einem Response beantwortet, der einen dreistelligen Statuscode enthält.
Diese Codes sind essentiell für das Verständnis der Kommunikation zwischen Client und Server
und helfen dabei, Probleme zu diagnostizieren oder den Erfolg einer Anfrage zu bestätigen.

[ENDSECTION]

[SECTION::instructions::detailed]

### HTTP-Statuscodes: Grundlagen und Kategorien

HTTP-Statuscodes sind dreistellige Zahlen, die in fünf Kategorien unterteilt sind:

**1xx**: Informational - Request received, continuing process

**2xx**: Success - The action was successfully received, understood, and accepted  

**3xx**: Redirection - Further action must be taken in order to complete the request

**4xx**: Client Error - The request contains bad syntax or cannot be fulfilled. 
Der entscheidende Punkt ist, dass den Server keine Verantwortung trifft. 
Nur der Client kann das Problem lösen.

**5xx**: Server Error - The server failed to fulfill an apparently valid request

(Optional) Mehr Details zu HTTP-Statuscodes finden Sie in der
[MDN-Dokumentation zu HTTP-Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
sowie in der 
[offiziellen IANA Status Code Registry](https://www.iana.org/assignments/http-status-codes).

### 1xx - Informationsantworten (100-199)

Diese Codes signalisieren, dass der Server die Anfrage erhalten hat und sie weiter verarbeitet:

**Häufige 1xx-Codes:**

- `100 Continue`: Der Client soll mit seiner Anfrage fortfahren
- `101 Switching Protocols`: Der Server wechselt zu einem anderen Protokoll

[EQ] In welchen Situationen würde ein Server den Statuscode `100 Continue` senden?
Beschreiben Sie ein typisches Szenario und erklären Sie, warum dieser Code nützlich ist.

[NOTICE]
Lesen Sie die 
[100 Continue](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100) 
für detaillierte Informationen zu diesem Statuscode.
[ENDNOTICE]

<!-- time estimate: 10 min -->

### 2xx - Erfolgsantworten (200-299)  

Diese Codes zeigen an, dass die Anfrage erfolgreich verarbeitet wurde:

**Grundlegende Erfolgscodes:**

- `200 OK`: Standard-Erfolgscode für GET-, POST- und andere Anfragen
- `201 Created`: Eine neue Ressource wurde erfolgreich erstellt (meist bei POST/PUT)
- `202 Accepted`: Anfrage akzeptiert, aber noch nicht vollständig verarbeitet
- `204 No Content`: Erfolgreiche Verarbeitung, aber keine Inhalte zurückgegeben

[EQ] Welcher Unterschied besteht zwischen den Statuscodes `200 OK` und `204 No Content`?
Wann würde man jeden der beiden verwenden? Geben Sie konkrete Beispiele.

[NOTICE]
Vergleichen Sie die 
[200 OK](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) 
und 
[204 No Content](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204) 
für die Unterschiede.
[ENDNOTICE]

<!-- time estimate: 10 min -->

### 3xx - Umleitungsnachrichten (300-399)

Diese Codes fordern den Client auf, weitere Schritte zu unternehmen:

**Standard-Umleitungen:**

- `300 Multiple Choice`: Mehrere mögliche Antworten verfügbar
- `301 Moved Permanently`: Ressource wurde dauerhaft verschoben
- `302 Found`: Ressource wurde temporär verschoben
- `303 See Other`: Client soll GET-Request an andere URI senden
- `304 Not Modified`: Ressource unverändert (für Caching)

**Erweiterte Umleitungen:**

- `307 Temporary Redirect`: Wie 302, aber HTTP-Methode darf nicht geändert werden
- `308 Permanent Redirect`: Wie 301, aber HTTP-Methode darf nicht geändert werden

[EQ] Erklären Sie die subtilen Unterschiede zwischen `301 Moved Permanently`, 
`302 Found` und `303 See Other`. Warum ist diese Unterscheidung in der Praxis wichtig?

[NOTICE]
Lesen Sie die 
[301 Moved Permanently](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301), 
[302 Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302) 
und 
[303 See Other](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/303) 
für die Unterschiede.
[ENDNOTICE]

[EQ] Erklären Sie den Unterschied zwischen `301 Moved Permanently` und `308 Permanent Redirect`.
Warum wurden die neuen 307/308-Codes eingeführt?

[NOTICE]
Lesen Sie die 
[301 Moved Permanently](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301) 
und 
[308 Permanent Redirect](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/308) 
für die Unterschiede.
[ENDNOTICE]

<!-- time estimate: 10 min -->

### 4xx - Client-Fehlerantworten (400-499)

Diese Codes zeigen Fehler in der Client-Anfrage an:

**Grundlegende Client-Fehler:**

- `400 Bad Request`: Anfrage hat syntaktische Fehler
- `401 Unauthorized`: Authentifizierung erforderlich (eigentlich "Unauthenticated")
- `403 Forbidden`: Server verweigert Zugriff trotz Authentifizierung  
- `404 Not Found`: Angeforderte Ressource existiert nicht
- `405 Method Not Allowed`: HTTP-Methode für diese Ressource nicht erlaubt

**Weitere wichtige Client-Fehler:**

- `408 Request Timeout`: Server-Timeout bei inaktiver Verbindung
- `409 Conflict`: Request konfligiert mit aktuellem Server-Status
- `429 Too Many Requests`: Rate Limiting aktiv

**Spezielle Codes:**

- `418 I'm a teapot`: RFC 2324 Aprilscherz (HTCPCP)
- `451 Unavailable For Legal Reasons`: Rechtlich blockiert

[EQ] Sie entwickeln eine Web-API und ein Client sendet einen POST-Request an einen Endpunkt,
der nur GET-Requests akzeptiert. Welchen Statuscode sollten Sie zurückgeben?

[NOTICE]
Konsultieren Sie die 
[405 Method Not Allowed](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/405) 
für die korrekte Verwendung dieses Statuscodes.
[ENDNOTICE]

[EQ] Ein Client überschreitet das Rate Limit (Anfrage-Limit) Ihrer API. Welcher Statuscode ist angemessen?



[NOTICE]
**Rate Limiting** ist eine Technik, bei der die Anzahl der Anfragen pro Zeiteinheit 
(beispielsweise maximal 100 Anfragen pro Minute) begrenzt wird, um Server vor Überlastung zu schützen 
und faire Nutzung zu gewährleisten.

Lesen Sie die 
[429 Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) 
für Informationen zu Rate Limiting.
[ENDNOTICE]

<!-- time estimate: 10 min -->

### 5xx - Server-Fehlerantworten (500-599)

Diese Codes zeigen Probleme auf der Serverseite an:

**Grundlegende Server-Fehler:**

- `500 Internal Server Error`: Allgemeiner, unerwarteter Serverfehler
- `501 Not Implemented`: Server unterstützt die Anfrage-Methode nicht
- `502 Bad Gateway`: Gateway/Proxy erhielt ungültige Antwort vom Upstream-Server
- `503 Service Unavailable`: Server temporär nicht verfügbar (Wartung/Überlastung)
- `504 Gateway Timeout`: Gateway/Proxy-Timeout beim Upstream-Server

[EQ] Ein Webserver ist aufgrund eines Festplattendefekts nicht verfügbar.
Welchen Statuscode sollte er zurückgeben?

[NOTICE]
Konsultieren Sie die 
[503 Service Unavailable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) 
für die korrekte Verwendung bei Wartungsarbeiten.
[ENDNOTICE]

<!-- time estimate: 10 min -->

### Historische und kulturelle Besonderheiten

Einige Statuscodes haben interessante Hintergründe:

**RFC 2324 und Aprilscherze:**

`418 I'm a teapot`: Stammt aus RFC 2324 (1998), 
dem "Hyper Text Coffee Pot Control Protocol" (HTCPCP). 
Wird heute ironisch für ungültige Anfragen oder als Erkennungszeichen verwendet.

**Rechtliche und politische Codes:**

`451 Unavailable For Legal Reasons`: Eingeführt 2015, 
benannt nach Ray Bradburys "Fahrenheit 451", für rechtlich blockierte Inhalte.

### Praktische Anwendung und Diagnose

[EQ] Stellen Sie sich vor, Sie betreiben einen Online-Video-Streaming-Dienst.
Ordnen Sie die folgenden Situationen den passenden HTTP-Statuscodes zu 
und begründen Sie Ihre Entscheidung. Verfügbare Statuscodes:
`200 OK`, `301 Moved Permanently`, `302 Found`, 
`404 Not Found`, `500 Internal Server Error`, `502 Bad Gateway`

 - **a)** Ein Benutzer ruft erfolgreich die Startseite der Plattform auf.
 - **b)** Während einer Live-Übertragung antwortet der Upstream-Streaming-Server 
(der ursprüngliche Server, von dem der Inhalt kommt) nicht mehr rechtzeitig, 
weil er überlastet ist.
 - **c)** Beim Abspielen einer Episode tritt auf dem Server 
ein unerwarteter Fehler in der Videotranscodierung auf.
 - **d)** Ein Benutzer ruft die Seite einer Serie auf, 
die vor Monaten aus dem Angebot entfernt wurde.
 - **e)** Eine laufende Aktion verschiebt den Zugriff auf einen Trailer 
vorübergehend auf eine andere URL, die später wieder zurückgesetzt wird.
 - **f)** Eine beliebte Serie wurde dauerhaft auf eine neue URL verschoben, 
und alle zukünftigen Aufrufe sollen auf diese neue Adresse verweisen.

[NOTICE]
Für diese praktische Übung können Sie die [HTTP Status Codes Referenz](https://httpstatuses.com/) 
als Nachschlagewerk verwenden, um die korrekten Statuscodes zu identifizieren.
[ENDNOTICE]

<!-- time estimate: 10 min -->

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]