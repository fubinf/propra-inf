title: HTTP-Statuscodes verstehen und klassifizieren
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: http-GET
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

**4xx**: Client Error - The request contains bad syntax or cannot be fulfilled

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
- `102 Processing (WebDAV)`: Server verarbeitet die Anfrage, aber keine Antwort verfügbar
- `103 Early Hints`: Ermöglicht Preloading von Ressourcen während der Serververarbeitung

[EQ] In welchen Situationen würde ein Server den Statuscode `100 Continue` senden?
Beschreiben Sie ein typisches Szenario und erklären Sie, warum dieser Code nützlich ist.

<!-- time estimate: 10 min -->

### 2xx - Erfolgsantworten (200-299)  

Diese Codes zeigen an, dass die Anfrage erfolgreich verarbeitet wurde:

**Grundlegende Erfolgscodes:**

- `200 OK`: Standard-Erfolgscode für GET-, POST- und andere Anfragen
- `201 Created`: Eine neue Ressource wurde erfolgreich erstellt (meist bei POST/PUT)
- `202 Accepted`: Anfrage akzeptiert, aber noch nicht vollständig verarbeitet
- `204 No Content`: Erfolgreiche Verarbeitung, aber keine Inhalte zurückgegeben

**Spezielle Erfolgscodes:**

- `203 Non-Authoritative Information`: Erfolg, aber Metadaten von Drittquelle
- `205 Reset Content`: Client soll das sendende Dokument zurücksetzen
- `206 Partial Content`: Partielle Inhalte bei Range-Anfragen
- `207 Multi-Status (WebDAV)`: Multiple Statuscodes für verschiedene Ressourcen
- `208 Already Reported (WebDAV)`: Vermeidet doppelte Auflistung in Collections
- `226 IM Used (HTTP Delta encoding)`: Antwort repräsentiert angewendete Instanzmanipulationen

[EQ] Welcher Unterschied besteht zwischen den Statuscodes `200 OK` und `204 No Content`?
Wann würde man jeden der beiden verwenden? Geben Sie konkrete Beispiele.

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

**Veraltete Codes:**

- `305 Use Proxy`: Deprecated aus Sicherheitsgründen
- `306 unused`: Nicht mehr verwendet, nur reserviert

(Optional) Ausführliche Informationen zu Redirects finden Sie in der
[MDN-Dokumentation zu Redirects](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections).

[EQ] Erklären Sie den Unterschied zwischen `301 Moved Permanently` und `308 Permanent Redirect`.
Warum wurden die neuen 307/308-Codes eingeführt?

<!-- time estimate: 10 min -->

### 4xx - Client-Fehlerantworten (400-499)

Diese Codes zeigen Fehler in der Client-Anfrage an:

**Grundlegende Client-Fehler:**

- `400 Bad Request`: Anfrage hat syntaktische Fehler
- `401 Unauthorized`: Authentifizierung erforderlich (eigentlich "Unauthenticated")
- `403 Forbidden`: Server verweigert Zugriff trotz Authentifizierung  
- `404 Not Found`: Angeforderte Ressource existiert nicht
- `405 Method Not Allowed`: HTTP-Methode für diese Ressource nicht erlaubt

**Authentifizierung und Autorisierung:**

- `407 Proxy Authentication Required`: Proxy-Authentifizierung nötig
- `408 Request Timeout`: Server-Timeout bei inaktiver Verbindung
- `409 Conflict`: Request konfligiert mit aktuellem Server-Status
- `410 Gone`: Ressource dauerhaft entfernt (stärker als 404)

**Anfrage-spezifische Fehler:**

- `411 Length Required`: Content-Length Header fehlt
- `412 Precondition Failed`: Vorbedingungen nicht erfüllt
- `413 Payload Too Large`: Request-Body zu groß
- `414 URI Too Long`: Request-URI zu lang
- `415 Unsupported Media Type`: Medienformat nicht unterstützt
- `416 Range Not Satisfiable`: Angeforderte Range ungültig
- `417 Expectation Failed`: Expect-Header kann nicht erfüllt werden

**Spezielle und moderne Codes:**

- `418 I'm a teapot`: RFC 2324 Aprilscherz (HTCPCP)
- `421 Misdirected Request`: Request an falschen Server gerichtet
- `422 Unprocessable Entity (WebDAV)`: Syntaktisch korrekt, aber semantisch fehlerhaft
- `423 Locked (WebDAV)`: Ressource gesperrt
- `424 Failed Dependency (WebDAV)`: Abhängige Anfrage fehlgeschlagen
- `425 Too Early`: Server riskiert keine Replay-Attacke
- `426 Upgrade Required`: Protokoll-Upgrade erforderlich
- `428 Precondition Required`: Bedingte Anfrage erforderlich
- `429 Too Many Requests`: Rate Limiting aktiv
- `431 Request Header Fields Too Large`: Header-Felder zu groß
- `451 Unavailable For Legal Reasons`: Rechtlich blockiert

**Experimentelle Codes:**

- `402 Payment Required`: Reserviert für zukünftige Zahlungssysteme

[EQ] Sie entwickeln eine Web-API und ein Client sendet einen POST-Request an einen Endpunkt,
der nur GET-Requests akzeptiert. Welchen Statuscode sollten Sie zurückgeben?

[EQ] Ein Client überschreitet das Rate Limit Ihrer API. Welcher Statuscode ist angemessen?

<!-- time estimate: 10 min -->

### 5xx - Server-Fehlerantworten (500-599)

Diese Codes zeigen Probleme auf der Serverseite an:

**Grundlegende Server-Fehler:**

- `500 Internal Server Error`: Allgemeiner, unerwarteter Serverfehler
- `501 Not Implemented`: Server unterstützt die Anfrage-Methode nicht
- `502 Bad Gateway`: Gateway/Proxy erhielt ungültige Antwort vom Upstream-Server
- `503 Service Unavailable`: Server temporär nicht verfügbar (Wartung/Überlastung)
- `504 Gateway Timeout`: Gateway/Proxy-Timeout beim Upstream-Server
- `505 HTTP Version Not Supported`: HTTP-Version nicht unterstützt

**Erweiterte Server-Fehler:**

- `506 Variant Also Negotiates`: Serverkonfigurationsfehler bei Content Negotiation
- `507 Insufficient Storage (WebDAV)`: Nicht genug Speicherplatz
- `508 Loop Detected (WebDAV)`: Endlosschleife bei Anfrageverarbeitung
- `510 Not Extended`: Server benötigt Erweiterungen für die Anfrage
- `511 Network Authentication Required`: Netzwerk-Authentifizierung erforderlich

(Optional) Weitere Informationen zu Server-Fehlern finden Sie in der
[HTTP-Fehlerbehandlung Dokumentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses).

[EQ] Ein Webserver ist aufgrund von Wartungsarbeiten temporär nicht verfügbar.
Welchen Statuscode sollte er zurückgeben?

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

(Optional) Weitere ungewöhnliche HTTP-Statuscodes sind in der
[Complete List of HTTP Status Codes](https://httpstatuses.com/) dokumentiert.

### Praktische Anwendung und Diagnose

[EQ] Stellen Sie sich vor, Sie betreiben einen Online-Video-Streaming-Dienst.
Ordnen Sie die folgenden Situationen den passenden HTTP-Statuscodes zu 
und begründen Sie Ihre Entscheidung. Verfügbare Statuscodes:
`200 OK`, `301 Moved Permanently`, `302 Found`, 
`404 Not Found`, `500 Internal Server Error`, `502 Bad Gateway`

 - **a)** Ein Benutzer ruft erfolgreich die Startseite der Plattform auf.
 - **b)** Während einer Live-Übertragung antwortet der Upstream-Streaming-Server 
nicht mehr rechtzeitig, weil er überlastet ist.
 - **c)** Beim Abspielen einer Episode tritt auf dem Server 
ein unerwarteter Fehler in der Videotranscodierung auf.
 - **d)** Ein Benutzer ruft die Seite einer Serie auf, 
die vor Monaten aus dem Angebot entfernt wurde.
 - **e)** Eine laufende Aktion verschiebt den Zugriff auf einen Trailer 
vorübergehend auf eine andere URL, die später wieder zurückgesetzt wird.
 - **f)** Eine beliebte Serie wurde dauerhaft auf eine neue URL verschoben, 
und alle zukünftigen Aufrufe sollen auf diese neue Adresse verweisen.

<!-- time estimate: 10 min -->

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]