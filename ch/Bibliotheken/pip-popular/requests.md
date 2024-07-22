title: Python requests
stage: draft
timevalue: 1.5
difficulty: 3
assumes: HTTP, WebAPIs, pip
---

[SECTION::goal::trial]

Ich kann das Python-Paket `requests` für verschiedene Arten von HTTP-Anfragen verwenden.

[ENDSECTION]

[SECTION::background::default]

Da viele moderne Anwendungen auf externe Dienste angewiesen sind, die über [TERMREF::API]
kommunizieren, ist das Beherrschen einer http-Bibliothek wichtig.
Es gibt in der Standardbibliothek [http.client](https://docs.python.org/3/library/http.client.html),
aber das ist recht umständlich, weshalb die meisten Programme lieber
das viel einfacher zu benutzende [`requests`](https://requests.readthedocs.io) verwenden.

[ENDSECTION]

[SECTION::instructions::loose]

Requests bietet benutzerfreundliche Methoden, die es ermöglichen, HTTP-Anfragen wie GET, POST, PUT
und DELETE zu verwenden, sowie Unterstützung für das Arbeiten mit Cookies, Sitzungen und
Authentifizierung. Diese Bibliothek ist äußerst vielseitig und wird häufig verwendet, um Webdaten
abzurufen, APIs zu integrieren, Webseiten zu testen und automatisierte Webanwendungen zu erstellen.

In dieser Aufgabe werden wir uns nur mit den Anfragen beschäftigen, jedoch keine Daten auswerten
oder manipulieren.

### Installation

Da es sich bei diesem Modul um eine externe Bibliothek handelt, die nicht Teil der
Python-Standardbibliothek ist, müssen Sie `requests` mittels [PARTREF::pip] installieren.

- [EQ] Welche Version haben Sie installiert?

### GET Anfrage

Diese Anfrage ist die einfachste Anfrage, da Sie i.d.R. keine [TERMREF::Payload] benötigt. Dennoch
eine interessante Anfrage, weil wir damit Daten erhalten. Sie wird nämlich dazu verwendet, um eine
Ressource auf einem Server anzufordern.

[NOTICE]
Technisch gesehen kann eine GET-Anfrage eine Payload besitzen, jedoch wird dies im Allgemeinen nicht
empfohlen und ist nicht üblich. Die Verwendung einer Payload in einer GET-Anfrage ist nicht im
Einklang mit den Standards von HTTP und kann zu unerwartetem Verhalten führen,
insbesondere bei der Zwischenspeicherung von Proxys oder Caches. In der Praxis ist es besser,
POST-Anfragen für den Austausch von Daten zu verwenden, die nicht leicht in die URL-Codierung
passen oder für Daten, die sicher übermittelt werden müssen. Schlussendlich ist es eine Frage der
Architektur und ob man Standards folgt, oder nicht.
[ENDNOTICE]

Ein allgemeiner GET-Request sieht wie folgt aus:

```python
import requests # Modul verwenden

# URL der Ressource, die abgerufen werden soll
url = 'https://example.com/api/resource'

# Senden einer GET-Anfrage an die URL und Speichern der Antwort
response = requests.get(url)

# Überprüfen des Statuscodes der Antwort
if response.status_code == 200:
    # Erfolgreiche Anfrage, die Antwort anzeigen
    print(response.text)
else:
    # Fehler bei der Anfrage, den Statuscode anzeigen
    print(f"Fehler: {response.status_code}")
```

[NOTICE]
Der in unserem Beispiel definierte Statuscode `200` kann je nach Schnittstelle variieren, da er
davon Abhängt, welche Eigenschaft die Schnittstelle aufweist. Zum Beispiel könnten gar keine Daten
zurückgegeben werden (Statuscode 204), oder wir haben einen Negativ-Berechtigungs-Test und erwarten
einen Statuscode 403 für einen nicht erlaubten Zugriff auf eine Ressource.
[ENDNOTICE]

- [ER] Erstellen Sie eine Python Datei mit einer GET Anfrage an die Schnittstelle:
  `https://petstore.swagger.io/v2/store/inventory`

- [EQ] Welchen Status-Code erhalten Sie?
- [EQ] Bekommen Sie einen [TERMREF::Response] Body zurück? Haben Sie dieses Verhalten bezüglich des
  Status Codes erwartet?

### Post Anfrage

Im Gegensatz zur GET-Anfrage kann ein POST-Anfrage eine Payload enthalten, die zusätzliche Daten an
den Server sendet. Die genaue Struktur und der Inhalt dieser Payload sind von der Implementierung
der Schnittstelle abhängig und sollten ausführlich in der API-Dokumentation beschrieben sein.

[HINT::URL-Parameter]
In API-Anfragen können Parameter häufig als Teil der URL-Codierung übergeben und dazu verwendet
werden, spezifische Ressourcen oder Daten auf dem Server anzufordern. Dabei wird am Ende der URL ein
definierter Parameter angefügt. Mehrere Parameter können kombiniert werden.

[HINT::Kombination]
Um mehrere Parameter in einer URL zu kombinieren, werden sie normalerweise durch das Zeichen "&"
getrennt. Jeder Parameter wird als Schlüssel/Wert-Paar dargestellt, wobei der Schlüssel und der Wert
durch das Zeichen "=" voneinander getrennt sind.

```bash
https://api.example.com/resource?key1=value1&key2=value2&key3=value3
```

[ENDHINT]

[ENDHINT]

[NOTICE]
In HTTP-POST-Anfragen werden Parameter häufig als Teil der Payload übermittelt.
[ENDNOTICE]

Ein allgemeiner POST-Request sieht wie folgt aus:

```python
import requests

# URL der Ressource, an die die POST-Anfrage gesendet werden soll
url = 'https://example.com/api/resource'

# Daten, die in der POST-Anfrage gesendet werden sollen (optional)
data = {'key': 'value'}

# Senden einer POST-Anfrage an die URL mit den angegebenen Daten
response = requests.post(url, data=data)

# Überprüfen des Statuscodes der Antwort
if response.status_code == 201:
    # Erfolgreiche Anfrage, die Antwort anzeigen
    print(response.text)
else:
    # Fehler bei der Anfrage, den Statuscode anzeigen
    print(f"Fehler: {response.status_code}")
```

- [ER] Erstellen Sie eine Python Datei mit einer POST Anfrage an die Schnittstelle:
  `https://petstore.swagger.io/v2/pet/{petId}`
- [EQ] Welche petId antwortet mit einem Status Code 404 und 200, und warum?
- [EQ] Wie können Sie einen Status Code `415 - Unsupportes Media Type` als Antwort erzeugen?
- [EQ] Wie kann ich mit dem zuvor gefundenen Problem den Status 415 beheben?

[HINT::Womit teste ich?]
Manche Fehler können nicht überall erzwungen (reprodfuiziert) werden. Daher werden beim Testen oftmals
mehrere Möglichkeiten betrachten. Versuchen Sie den Code 415 nicht über Swagger zu erzwingen.
[ENDHINT]

- [EQ] Wie können Sie einen Status Code `405 - Method Not Allowed` als Antwort erzeugen?
- [ER] Senden Sie jetzt einen erfolgreichen POST-Request an `https://petstore.swagger.io/v2/pet`.
  
[HINT::Payloadtyp]
Sicherlich versuchen Sie ein JSON in Ihrer Payload mitzugeben, was zu einem Fehler führt. Sie haben
dann zwei Möglichkeiten. 1. Sie überführen Ihre Payload in ein Pythond Dictionary, oder 2. Sie
verwendet json=<Variable> anstatt data=<Variable> in Ihrem Request.
[ENDHINT]

- [EQ] Worin unterscheiden sich die beiden Schnittstellen aus [EREFR::2] und [EREFR::3]?

Andere Schnittstellen wie PUT und DELETE funktionieren äquivalent zu POST.

- [EQ] Kann Python Request auch eine PATCH Anfrage senden? Was ist so besonders an einer PATCH
  Anfrage?

### Authentifikation

Nicht jede API ist frei zugänglich. Einige werden gar nicht öffentlich zur Verfügung gestellt,
andere sind eingeschränkt verwendbar. Für das folgende Beispiel verwenden wir die Schnittstelle
`https://reqres.in/api/login`.

Machen Sie sich mit der `Basic Authentication` auf der offiziellen
[Dokumentation](https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication)
vertraut.

- [ER] Implementieren Sie eine eingeschränkte Anfrage mit den Zugangsdaten `email=eve.holt@reqres.in`
  und `password=password` und geben Sie das Ergebnis aus.
- [EQ] Erläutern Sie, wie Sie mit diesem Ergebnis weiterarbeiten können? Gehen Sie insbesondere auf
  andere Anfragen ein.

Löschen Sie die Passwortmitgabe und wiederholen Sie die Anfrage.

- [EQ] Welche Antwort erhalten Sie?

### Abschluss

Sie haben nur einen kleinen Teil dieses `requests`-Moduls kennengelernt. Zahlreiche weitere Funktionen
stellt das Request-Modul zur Verfügung, um mit Header Informationen, Zertifikate oder mit Fehlermeldungen
zu arbeiten. Stöbern Sie in der genannten Dokumention herum, um einen tieferen Einklick zu erhalten.

[ENDSECTION]

[SECTION::submission::information,snippet]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Hinweise Tutor]

- [EREFQ::1] Stand 13. Juli 2024: Version 2.32.3. Somit >= dieser Version.
- [EREFR::1] Man nehme das GET-Beispiel und ändere die URL und den Statuscode in 200.
- [EREFQ::2] Wenn alles klappt: 200. Ansonsten diverse Fehlermeldungscodes wie 404, wenn die URL/
  der Endpunkt fehlerhaft ist, oder 'Fehler 200', wenn der Statuscode nciht angepasst wurde.
- [EREFQ::3] Bei Code 200: ja und ja, da ein Get ohne Antwort nicht Rest-Konform ist.
  Response sollte so aussehen:
  `{"sold":4,"string":763,"Happy":2,"unavailable":1,"pending":16,"available":205,"not available":2,"peric":2}`
  Dabei können die Zahlen im JSON bei jeden Request unterschiedlich ausfallen.
- [EREFR::2] Man nehme das GET-Beispiel und passe die URL, den Statuscode und die Methode in POST an.
- [EREFQ::4] die 1 sollte einen Code 200 bringen, da es vorhanden ist. Eine beliebig hohe ID einen Code 404,d a dieses Objekt
  nicht gefunden wurde.
- [EREFQ::5] Indem kein Wert in der URL mitgegeben wird. Der Code 415 zeigt, das Fehler in vielen
  banalen Situationen stecken können und diese auch niocht alle Dokumentiert sind. Über die
  Swagger - Petstore API Seite - kann dies nicht reproduziert werden, da Swagger selber diesen
  Fall abfängt. Diese Situation kann nur über ein Script erzeugt werden.
- [EREFQ::6] Indem ein Content Type im Code mitgegeben wird:

```python
# Header für die Anfrage
headers = {
    'Content-Type': 'application/json'
}
```

- [EREFQ::7] Indem ein falscher Datentyp mitgegeben wird, z.B. ein String

- [EREFR::3] Die entscheidene Anpassung ist die Mitgabe eines Payloads mit korrekten Data (im Swagger
  dokumentiert). ZUsätzlich ist hier darauf zu achten, dass `json` anstatt `data` im Request verwendet
  wird:

```python
import requests # Modul verwenden

# URL der Ressource, die abgerufen werden soll
url = 'https://petstore.swagger.io/v2/pet'

# Header für die Anfrage
headers = {
    'Content-Type': 'application/json'
}

# Daten, die in der POST-Anfrage gesendet werden sollen (optional)
# Beispiel-Daten, die im Body der POST-Anfrage gesendet werden
data = {
    "id": 100,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

# Senden einer POST-Anfrage an die URL mit den angegebenen Daten
response = requests.post(url, json=data, headers=headers)

# Überprüfen des Statuscodes der Antwort
if response.status_code == 200:
    # Erfolgreiche Anfrage, die Antwort anzeigen
    print(response.text)
else:
    # Fehler bei der Anfrage, den Statuscode anzeigen
    print(f"Fehler: {response.status_code, response.text}")
```

- [EREFQ::8] [EREFR::2] benötigt einen Parameter in der URL, wobei [EREFR::3] keinen zusätzlichen
  Parameter einfordert, dafür aber eine Payload im Body.

- [EREFQ::9] Ja, eine PATCH-Anfrage ist besonders, weil sie im Gegensatz zu einer PUT-Anfrage nur
  die angegebenen Änderungen an einer Ressource vornimmt, anstatt die Ressource vollständig zu ersetzen.

- [EREFR::4] Das Ergebnis ist ein JSON mit einem Token. Rückgabe: `{'token': 'QpwL5tke4Pnpja7X4'}`

Beispielimplentierung:

```python
import requests
from requests.auth import HTTPBasicAuth

# URL des Login-Endpunkts
url = 'https://reqres.in/api/login'

# Zugangsdaten
email = 'eve.holt@reqres.in'
password = 'password'

# Header für die Anfrage (optional)
headers = {
    'Content-Type': 'application/json'
}

# Daten für die POST-Anfrage
data = {
    'email': email,
    'password': password
}

# Senden der POST-Anfrage mit Basic Auth
response = requests.post(url, json=data, headers=headers, auth=HTTPBasicAuth(email, password))

# Überprüfen des Statuscodes der Antwort
if response.status_code == 200:
    # Erfolgreiche Anfrage, die Antwort anzeigen
    print('Erfolgreich:', response.json())
else:
    # Fehler bei der Anfrage, den Statuscode anzeigen
    print(f'Fehler: {response.status_code}, {response.text}')
```

- [EREFQ::10] Ein Token kann zeitbasiert gespeichert werden (Zeitbasiert, da es i.d.R. abläuft und erneut
  abgefragt werden muss), um so sicher weitere Anfragen ohne erneute Logins durchzuführen. Das ermöglicht
  einen sicheren Zugriff auf geschützte Ressourcen und Endpunkte, die sonst eine Authentifizierung
  erfordern.

- [EREFQ::11] Code 400 - Bad Request, da der erwartete Parameter `password` nicht angegebene wurde.

[ENDINSTRUCTOR]
