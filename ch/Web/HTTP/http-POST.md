title: "HTTP POST: Daten an Server übermitteln (request body, forms)"
stage: beta
timevalue: 1.5
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
sie typischerweise verwendet (stichwortartige Antwort reicht)?
<!-- EQ1 -->
<!-- time estimate: 15 min -->


### POST vs. GET: Die wichtigsten Unterschiede

POST unterscheidet sich in mehreren wichtigen Aspekten von GET:

**Semantik (der wichtigste Unterschied):**

- GET: Ist wirkungsfrei (idempotent), verändert also den Server-Zustand nicht.
- POST: Verändert den Zustand auf dem Server; es kann Daten erstellen, ändern oder löschen.

GET wird also zum Abrufen von Informationen verwendet, während POST zum Senden von Daten zur Verarbeitung dient.

**Datenübertragung:**

- GET: Parameter werden in der URL übertragen (`/search?query=beispiel&page=1`),
  sind also in der Browser-Historie und in Server-Logs sichtbar.
  Die Datenmenge ist begrenzt durch die maximale URL-Länge von faktisch ca. 2048 Zeichen.
- POST: Daten werden im Request Body übertragen und sind nicht sichtbar in der URL.
  Die übertragbare Datenmenge ist nicht beschränkt. 

**Caching und Wiederholung:**

- GET: Der Request kann wegen der Wirkungsfreiheit problemlos wiederholt werden.
  Das Resultat wird von Browsern gecacht.
- POST: Da der Request eine Wirkung hat, bedeuten zwei gleiche Requests eventuell etwas anderes
  als nur einer. Caching ist deshalb nicht möglich und Browser warnen vor einer Wiederholung.

[EQ] Erklären Sie den semantischen Unterschied zwischen GET und POST anhand eines konkreten Szenarios 
aus dem Alltag, das sowohl GET als auch POST enthält.
Beschreiben Sie, warum die HTTP-Methode für den jeweiligen Zweck semantisch korrekt ist und 
was passieren würde, wenn man die falsche Methode verwendete.
<!-- EQ2 -->
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

[ER] Erstellen Sie eine Datei `http-POST-form.crlf` mit einer POST-Anfrage, 
die folgende Formulardaten an `httpbin.org` (Port 80) zum Pfad `/post` sendet::

- username: "testuser"
- password: "geheim123"
- remember: "on"

Verwenden Sie `application/x-www-form-urlencoded` als Content-Type und 
vergessen Sie nicht die korrekte Content-Length.
<!-- ER1 -->
<!-- time estimate: 15 min -->


### Varianten beim `Content-Type`

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

[EQ] Recherchieren Sie, wann man die verschiedenen Content-Type-Varianten verwendet. 
Welche Vor- und Nachteile hat jede Variante? Wann würden Sie `application/json` 
statt `application/x-www-form-urlencoded` verwenden?
<!-- EQ3 -->

[HINT::Wo finde ich im Netz dazu eine gute Diskussion?]
[MDN: Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)   
[JSON vs Form Data](https://stackoverflow.com/questions/4007969/application-x-www-form-urlencoded-or-multipart-form-data)
[ENDHINT]
<!-- time estimate: 15 min -->


### POST-Anfrage mit netcat testen

Genau wie bei GET können wir POST-Anfragen manuell mit `netcat` testen.

[EC] Testen Sie Ihre POST-Anfrage mit einem öffentlichen Test-Service:
Senden Sie die Anfrage an `httpbin.org` (Port 80) an den Pfad `/post`.
Dieser Service gibt die empfangenen Daten zur Kontrolle zurück.
Führen Sie aus: `nc httpbin.org 80 <http-POST-form.crlf`
<!-- EC1 -->
<!-- time estimate: 10 min -->

[HINT::Meine Anfrage funktioniert nicht!]
Achten Sie darauf, dass alle Zeilen mit CRLF enden und zwischen Header und Body 
eine Leerzeile steht. 
Die Content-Length muss exakt der Anzahl Bytes im Body 
entsprechen (inklusive der CRLF-Zeichen im Body).
[ENDHINT]


### POST mit JSON-Daten

Lassen Sie uns das gleiche Beispiel wie oben verwenden, aber diesmal mit JSON-Format:

[ER] Erstellen Sie eine Datei `http-POST-json.crlf` mit einer POST-Anfrage, 
die die gleichen Daten wie oben an `httpbin.org` (Port 80) zum Pfad `/post` sendet, 
aber im JSON-Format.
Verwenden Sie `application/json` als Content-Type und achten Sie auf die korrekte JSON-Syntax.
<!-- ER2 -->

[EC] Führen Sie aus: `nc httpbin.org 80 <http-POST-json.crlf`
<!-- EC2 -->
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

[ER] Erstellen Sie eine Datei `http-POST-registration-form.html` mit folgendem HTML-Code 
und testen Sie das Formular, indem Sie es im Browser öffnen, ausfüllen und absenden. 
Die Antwort von `httpbin` zeigt die übermittelten Daten im Feld form. 
Reichen Sie die von httpbin zurückgegebene Formularausgabe als `http-POST-registration-form-result.html` ein.

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
<!-- ER3 -->
<!-- time estimate: 10 min -->
[ENDSECTION]


[SECTION::submission::information,snippet,trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]

### Eingabedateien

Die POST-Anfrage `http-POST-form.crlf` sollte etwa so aussehen (mit CR LF als Zeilentrenner):
```
[INCLUDE::ALT:http-POST-form.txt]
```

### Fragen

[INCLUDE::ALT:http-POST.md]

### Kommandoprotokoll

Sollte netcat-Befehle enthalten und die entsprechenden Responses zeigen.
[PROT::ALT:http-POST.prot]

[ENDINSTRUCTOR]