title: Python requests
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: WebAPIs, pip
---

TODO_2_ruhe:

- Diese Aufgabe braucht Grundlagen aus dem Webkapitel über http und URLs, denn hier sollte
  es nur um die Bibliothek gehen.
- So lange es passende Grundlagenaufgaben nicht gibt, können wir diese Aufgabe nicht sinnvoll
  in Betrieb nehmen.
- Die Aufgaben und Fragen scheinen mir überwiegend gut.
- Eine Ja/Nein-Frage wie "Überrascht Sie das Ergebnis?" ist aber nicht brauchbar;
  wir wollen ja die Gedanken dahinter zu sehen bekommen.
- INSTRUCTOR-Teil fehlt.

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
if response.status_code == 200:
    # Erfolgreiche Anfrage, die Antwort anzeigen
    print(response.text)
else:
    # Fehler bei der Anfrage, den Statuscode anzeigen
    print(f"Fehler: {response.status_code}")
```

- [ER] Erstellen Sie eine Python Datei mit einer POST Anfrage an die Schnittstelle:
  `https://petstore.swagger.io/v2/pet/{petId}`
- [EQ] Welche petId antwortet mit einem Status Code 404 und 200, und warum?
- [EQ] Wie können Sie einen Status Code `405 - Invalid` als Antwort erzeugen?
- [ER] Erweitern Sie Ihre Anfrage um die Parameter `name`und `status` (beide String)
- [EQ] Welchen Status konnten Sie als validen Wert identifizieren?

Andere Schnittstellen wie PUT und DELETE funktionieren äquivalent zu POST.

- [EQ] Kann Python Request auch eine PATCH Anfrage senden? Was ist so besonders an einer PATCH
  Anfrage?

### Authentifikation

Nicht jede API ist frei zugänglich. Einige werden gar nicht öffentlich zur Verfügung gestellt,
andere sind eingeschränkt verwendbar. Für das folgende Beispiel verwenden wir die Schnittstelle
`https://reqres.in/api/login`.

Machen Sie sich mit der `Basic Authentication` auf der offiziellen
[Dokumentation](https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication).

- [ER] Implementieren Sie eine eingeschränkte Anfrage mit den Zugangsdaten `email=eve.holt@reqres.in`
  und `password=password`.
- [EQ] Was enthält der Response-Body?
- [EQ] Erläutern Sie, wie Sie mit diesem Ergebnis weiterarbeiten können? Gehen Sie insbesondere auf
  andere Anfragen ein.

Ändern Sie das Passwort in `wrong_password` und wiederholen Sie die Anfrage.

- [EQ] Überrascht Sie das Ergebnis?

### Abschluss

Sie haben nur einen kleinen Teil dieses Moduls kennengelernt. Zahlreiche weitere Funktionen stellt
das Request-Modul zur Verfügung, um mit Header Informationen, Zertifikate oder mit Fehlermeldungen
zu arbeiten. Stöbern Sie in der genannten Dokumention herum, um einen tieferen Einklick zu erhalten.

[ENDSECTION]

[SECTION::submission::information,snippet]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]