title: "HTTP POST: Daten an Server übermitteln (request body, forms)"
stage: alpha
timevalue: 2
difficulty: 2
assumes: http-GET
---

[SECTION::goal::idea,experience]

Ich verstehe Aufbau und Bedeutung einer POST-Anfrage und -Antwort in HTTP und kann 
die Unterschiede zu GET-Anfragen erklären.

[ENDSECTION]

[SECTION::background::default]

Während GET-Anfragen hauptsächlich zum Abrufen von Daten verwendet werden, benötigen 
moderne Webanwendungen auch die Möglichkeit, Daten an Server zu senden. 
Bei der Benutzerregistrierung, dem Hochladen von Dateien oder der Übermittlung 
von Formulardaten ist die POST-Methode das zentrale Werkzeug für die 
Datenübertragung im Web.

[ENDSECTION]

[SECTION::instructions::detailed]

### HTTP-Methoden im Überblick

HTTP definiert verschiedene Methoden (auch "Verben" genannt) für unterschiedliche 
Arten von Anfragen. Die beiden wichtigsten sind:

- **GET**: Zum Abrufen von Ressourcen vom Server (schon gelernt in [PARTREF::http-GET])
- **POST**: Zum Senden von Daten an den Server zur Verarbeitung

(Optional) Lesen Sie zunächst die grundlegende Erklärung zu 
[HTTP-Methoden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

[EQ] Welche weiteren HTTP-Methoden gibt es neben GET und POST, und wofür werden 
sie typischerweise verwendet?
<!-- time estimate: 15 min -->

### POST vs. GET: Die wichtigsten Unterschiede

POST unterscheidet sich in mehreren wichtigen Aspekten von GET:

**Datenübertragung:**

- GET: Parameter werden in der URL übertragen (`/search?query=beispiel&page=1`)
- POST: Daten werden im Request Body übertragen (nicht sichtbar in der URL)

**Sicherheit:**

- GET: Parameter sind in URL, Browser-Historie und Server-Logs sichtbar
- POST: Daten sind nicht in der URL sichtbar (aber trotzdem nicht automatisch verschlüsselt!)

**Datenmenge:**

- GET: Begrenzt durch maximale URL-Länge (ca. 2048 Zeichen)
- POST: Praktisch unbegrenzte Datenmenge möglich

**Caching und Wiederholung:**

- GET: Wird von Browsern gecacht und kann problemlos wiederholt werden
- POST: Wird nicht gecacht; Browser warnen vor Wiederholung

[EQ] Lesen Sie mehr über 
[POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)
Warum ist POST "nicht idempotent" im Gegensatz zu GET? 
Geben Sie ein praktisches Beispiel an.
<!-- time estimate: 15 min -->

### Aufbau einer POST-Anfrage

Eine POST-Anfrage hat folgenden grundlegenden Aufbau:

```http
POST /mypath HTTP/1.1
Host: myserver.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 35

myfield1=myvalue1&myfield2=myvalue2
```

Die wichtigsten Header bei POST:

- `Content-Type`: Gibt das Format der übertragenen Daten an
- `Content-Length`: Gibt die Länge des Request Body in Bytes an

### Content-Type Varianten

POST-Anfragen können verschiedene Datenformate übertragen:

**1. application/x-www-form-urlencoded** (Standard für HTML-Formulare):
```
myname=Max+Mustermann&myemail=max%40example.com&myage=25
```

**2. application/json** (für APIs):
```json
{
  "myname": "Max Mustermann",
  "myemail": "max@example.com", 
  "myage": 25
}
```

**3. multipart/form-data** (für Datei-Uploads):
```
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="myfile"; filename="mydocument.txt"
Content-Type: text/plain

Dateiinhalt hier...
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

(Optional) Eine detaillierte Erklärung der 
[Content-Types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)

[EC] Erstellen Sie eine Datei `HTTP-POST-form.crlf` mit einer POST-Anfrage, 
die folgende Formulardaten an `httpbin.org` (Port 80) zum Pfad `/post` sendet::

- username: "testuser"
- password: "geheim123"
- remember: "on"

Verwenden Sie `application/x-www-form-urlencoded` als Content-Type und 
vergessen Sie nicht die korrekte Content-Length.
<!-- time estimate: 30 min -->

### POST-Anfrage mit netcat testen

Genau wie bei GET können wir POST-Anfragen manuell mit `netcat` testen.

[NOTICE]
Achten Sie darauf, dass alle Zeilen mit CRLF enden und zwischen Header und Body 
eine Leerzeile steht. 
Die Content-Length muss exakt der Anzahl Bytes im Body 
entsprechen (inklusive der CRLF-Zeichen im Body).
[ENDNOTICE]

[EC] Testen Sie Ihre POST-Anfrage mit einem öffentlichen Test-Service:
Senden Sie die Anfrage an `httpbin.org` (Port 80) an den Pfad `/post`.
Dieser Service gibt die empfangenen Daten zur Kontrolle zurück.

Führen Sie aus: `nc httpbin.org 80 <HTTP-POST-form.crlf`
<!-- time estimate: 10 min -->

### POST mit curl

Für praktische Zwecke ist `curl` oft einfacher als das manuelle Erstellen 
von HTTP-Anfragen:

```bash
curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "myfield1=myvalue1&myfield2=myvalue2"
```

Für JSON-Daten:
```bash
curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/json" \
  -d '{"myname": "Max", "myage": 25}'
```

[EC] Verwenden Sie `curl`, um eine POST-Anfrage mit JSON-Daten zu senden:
```json
{
  "myaction": "register",
  "myuser": {
    "myname": "Anna Schmidt",
    "myemail": "anna@example.com"
  }
}
```
<!-- time estimate: 20 min -->

### POST-Response analysieren

POST-Antworten folgen dem gleichen Format wie GET-Antworten, aber die 
Statuscodes haben oft andere Bedeutungen:

- **200 OK**: Anfrage erfolgreich verarbeitet
- **201 Created**: Neue Ressource wurde erstellt
- **400 Bad Request**: Ungültige Daten gesendet
- **401 Unauthorized**: Authentifizierung erforderlich
- **422 Unprocessable Entity**: Daten syntaktisch korrekt, aber semantisch ungültig

(Optional) Zusätzlich lesen Sie über 
[HTTP-Statuscodes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

[EQ] Welcher der oben genannten fünf Statuscodes wäre in folgenden Situationen jeweils angemessen?

 - Formular wurde korrekt übermittelt und verarbeitet
 - Zugriff verweigert, da keine gültige Anmeldung vorliegt
 - Gesendete Daten sind fehlerhaft oder unvollständig
 - Daten sind formal korrekt, verletzen aber eine fachliche Regel 
 (z. B. Benutzername existiert bereits)
 - Neue Ressource (z. B. Benutzerkonto) erfolgreich angelegt

<!-- time estimate: 10 min -->

### HTML-Formulare und POST

HTML-Formulare verwenden standardmäßig POST für die Datenübertragung:

```html
<form action="/mysubmit" method="POST">
  <input type="text" name="myusername" required>
  <input type="email" name="myemail" required>
  <input type="password" name="mypassword" required>
  <button type="submit">Registrieren</button>
</form>
```

[EC] Erstellen Sie eine Datei `registration-form.html` mit folgendem HTML-Code 
und testen Sie das Formular, indem Sie es im Browser öffnen, ausfüllen und absenden. 
Die Antwort von `httpbin` zeigt die übermittelten Daten im Feld form. 
Reichen Sie die von httpbin zurückgegebene Formularausgabe ein.

```html
<!DOCTYPE html> 
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Testformular</title>
</head>
<body>
  <h1>Formular-Test mit httpbin</h1>
  <form action="https://httpbin.org/post" method="POST">
    <label>Vorname: <input type="text" name="firstname" required></label><br>
    <label>Nachname: <input type="text" name="lastname" required></label><br>
    <label>E-Mail: <input type="email" name="email" required></label><br>
    <label>Geburtsdatum: <input type="date" name="birthdate"></label><br>
    <label><input type="checkbox" name="newsletter" value="yes"> Newsletter abonnieren</label><br>
    <button type="submit">Absenden</button>
  </form>
</body>
</html>

```
<!-- time estimate: 10 min -->

### Sicherheitsaspekte bei POST

Obwohl POST sicherer als GET ist, gibt es wichtige Sicherheitsüberlegungen:

**HTTPS verwenden:**
POST-Daten sind nur bei HTTPS verschlüsselt. Bei HTTP sind sie im Klartext übertragbar.

**CSRF-Schutz:**
Cross-Site Request Forgery Angriffe können POST-Anfragen missbrauchen.

**Input-Validierung:**
Alle POST-Daten müssen serverseitig validiert werden.

(Optional) Lesen Sie mehr über 
[Web-Sicherheit](https://developer.mozilla.org/en-US/docs/Web/Security)

[EQ] Warum reicht es nicht aus, dass POST-Daten nicht in der URL stehen, 
um sie als "sicher" zu betrachten?
<!-- time estimate: 10 min -->

[ENDSECTION]

[SECTION::submission::information,snippet,trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
Geben Sie auch die Dateien `HTTP-POST-form.crlf` und `registration-form.html` mit ab.

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Eingabedateien

Die POST-Anfrage sollte etwa so aussehen:
```
POST /post HTTP/1.1
Host: httpbin.org
Content-Type: application/x-www-form-urlencoded
Content-Length: 48

username=testuser&password=geheim123&remember=on
```

Das HTML-Formular sollte vollständig und funktional sein.

### Fragen

Die Antworten sollten zeigen, dass die Studierenden die praktischen Unterschiede 
zwischen GET und POST verstehen, insbesondere bezüglich Sicherheit, Caching und Datenübertragung.

[INCLUDE::ALT:http-POST.md]

### Kommandoprotokoll

Sollte sowohl netcat- als auch curl-Befehle enthalten und die entsprechenden Responses zeigen.
[PROT::ALT:http-POST.prot]

[ENDINSTRUCTOR]