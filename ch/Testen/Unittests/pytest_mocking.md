title: "'unittest.mock': Ersetzen von Objekten für Testzwecke"
stage: alpha
timevalue: 2.5
difficulty: 3
assumes: m_pytest
---

[SECTION::goal::idea]

- Ich kann beschreiben, was Attrappen sind und warum sie für Tests nützlich sind.
- Ich kann verschiedene Techniken zur Verwendung von Attrappen in pytest anwenden.
- Ich kann begründen, wann Monkeypatching vs. Dependency Injection sinnvoll ist.
- Ich kann grundlegende Unittests mittels Attrappen realisieren.

[ENDSECTION]

[SECTION::background::default]
Unittests auf elementare Module sind kein Problem.
Aber wenn ein Modul von vielen anderen Dingen abhängt, stellt sich die Frage, ob man die
alle mittesten soll und will.
Falls es _nicht_ sinnvoll zu sein scheint, kann man es mithilfe von Attrappen vermeiden,
die an die Stelle jener anderen Module treten.

Für manche Zwecke ist das mehr eine Geschmacksfrage, in anderen Fällen, vor allem für
Tests, die mit Zeit/Datum zu tun haben, ist es eine unverzichtbare Testtechnik.

Stellen Sie sich vor, Sie wollen eine Funktion testen, die Wetterinformationen von einer Web-API abruft,
das Ergebnis in einer Datenbank speichert und eine E-Mail verschickt.
Für einen Unittest wollen Sie aber weder auf das Internet zugreifen, noch eine echte Datenbank verwenden,
noch echte E-Mails versenden.

Hier kommen **Attrappen** ins Spiel: Ersatzobjekte, die sich semantisch wie die echten Abhängigkeiten verhalten,
aber voll unter Ihrer Kontrolle stehen und sich im Verhalten genau für die Bedürfnisse des Tests
zuschneidern lassen.

[ENDSECTION]

[SECTION::instructions::detailed]

Nutzen Sie zum Bearbeiten der Aufgaben die folgende Dokumentation nach Bedarf:

- die Übersicht [Pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html),
  insbesondere den Abschnitt "How to monkeypatch/mock";
- die [Dokumentation von `unittest.mock`](https://docs.python.org/3/library/unittest.mock.html).

Für diese Aufgabe benötigen Sie ein ganzes Verzeichnis `pytest_mocking/`.

### Warum Attrappen? Das Problem verstehen

Betrachten Sie folgenden Code, der mehrere externe Abhängigkeiten hat:

```python
# weather_app.py
import requests
import sqlite3
import smtplib
from datetime import datetime

def get_weather_and_notify(city, user_email):
    # 1. Web-API Aufruf
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=KEY"
    response = requests.get(api_url)
    weather_data = response.json()
    
    # 2. Datenbank-Operation
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weather_logs (city, temperature, timestamp) VALUES (?, ?, ?)",
        (city, weather_data['main']['temp'], datetime.now())
    )
    conn.commit()
    conn.close()
    
    # 3. E-Mail versenden
    if weather_data['main']['temp'] < 0:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('bot@example.com', SMTP_PASSWORD)
            server.sendmail('bot@example.com', user_email, 
                          f"Achtung: In {city} herrscht Frost!")
    
    return weather_data['main']['temp']
```

[EQ] Was sind die Probleme oder Nachteile, wenn Sie diesen Code direkt testen wollten?
Nennen Sie mindestens einen Punkt für jeden der drei Schritte.

Diese Probleme können wir mit folgenden Methoden umgehen:
<!-- time estimate: 5 min -->

### Was ist eine Attrappe?

Eine Attrappe ist ein Objekt, das nach außen die gleiche Schnittstelle anbietet wie das Original,
bei der Funktionalität aber "nur so tut, als ob"; in einer Weise, die für den Testzweck passend ist.

Im Beispiel oben könnte die Web-Client-Attrappe z.B. ein immer gleiches hart kodiertes JSON-Objekt
liefern.
Die SMTP-Server-Attrappe würde aufzeichnen was passiert: Login mit den-und-den Daten war erfolgreich/erfolglos;
die-und-die Email wurde verschickt usw.
Der Test könnte anschließend diese Aufzeichnungen abfragen und mit den Erwartungen vergleichen.
<!-- time estimate: 5 min -->

### Zwei Wege zum Ziel: Monkeypatching vs. Dependency Injection

Es gibt grundsätzlich zwei Techniken, um Abhängigkeiten durch Attrappen zu ersetzen:

**Monkeypatching:** Zur Laufzeit wird das Original durch die Attrappe ersetzt.

- Vorteil: Funktioniert ohne Codeänderung an der zu testenden Funktion
- Nachteil: "Magisch", schwieriger zu verstehen, Testcode benötigt komplexen Patching-Schritt

**Dependency Injection:** Die Abhängigkeit wird als Parameter übergeben.
Man übergibt im echten Produktionscode einen echten Web-Client, eine echte Datenbankverbindung
und einen echten Email-Server.
Im Testcode benutzen wir stattdessen drei Attrappen mit der entsprechenden (Pseudo-)Funktionalität.

- Vorteil: Explizit, sauber, einfach zu verstehen
- Nachteil: Erfordert Umgestaltung des zu testenden Codes

Wir schauen uns beide Ansätze an, beginnend mit dem Monkeypatching, da wir hier keine
Vorbedingungen benötigen.
<!-- time estimate: 5 min -->

#### Erste Schritte: Monkeypatching mit `patch()`

Zu jeder kommenden Aufgabe wird es eine zu testende Funktion geben, die in der Aufgabe vorgegeben
ist oder von Ihnen erstellt werden soll.
Der Name der Datei ist jeweils oben in dem Codeblock als Kommentar angegeben,
z.B.  `mock_example_1.py`.

Lassen Sie uns mit einem einfachen Beispiel beginnen. Erstellen Sie folgende Datei `weather_simple.py`:

```python
# weather_simple.py
import requests

def get_temperature(city):
    """Ruft die aktuelle Temperatur für eine Stadt ab."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=DEMO_KEY"
    response = requests.get(url)
    data = response.json()
    return data['main']['temp']
```

Ohne Attrappen müssten Sie für jeden Test eine echte HTTP-Anfrage stellen.
Das ist langsam, braucht eine Internetverbindung und Sie haben keine Kontrolle über die Antwort.

Mit Monkeypatching ersetzen wir `requests.get` durch eine Attrappe:

```python
# test_weather_simple.py
from unittest.mock import patch

import pytest

from weather_simple import get_temperature


def test_get_temperature():
    # Mit patch() ersetzen wir requests.get durch eine Attrappe
    with patch('weather_simple.requests.get') as mock_get:
        # Wir definieren, was die Attrappe zurückgeben soll
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'main': {'temp': 15.5}}
        
        # Jetzt können wir die echte Funktion testen
        temperature = get_temperature("Berlin")
        
        # Verifikation: Richtige Antwort?
        assert temperature == 15.5
        
        # Verifikation: Wurde die richtige URL aufgerufen?
        expected_url = "https://api.openweathermap.org/data/2.5/weather?q=Berlin&appid=DEMO_KEY"
        mock_get.assert_called_once_with(expected_url)
```

[ER] Implementieren Sie beide Dateien und führen Sie den Test aus.

[EQ] Was passiert bei der Ausführung von `patch('weather_simple.requests.get')`?
Erklären Sie den Mechanismus in eigenen Worten; ein Satz genügt.

[HINT::Ich weiß nicht, was `patch()` intern macht]
Schauen Sie in der [Dokumentation von `unittest.mock`](https://docs.python.org/3/library/unittest.mock.html)
nach dem Abschnitt "patch".
Dort wird erklärt, wie `patch()` den angegebenen Namen zur Laufzeit durch ein Mock-Objekt
ersetzt und ihn nach dem `with`-Block automatisch wiederherstellt.
[ENDHINT]
<!-- time estimate: 30 min -->

#### Das Problem mit Monkeypatching: Redundanz

Monkeypatching funktioniert, hat aber Nachteile.
Betrachten Sie eine komplexere Funktion:

```python
# weather_complex.py
import requests

def get_weather_summary(cities):
    """Ruft Wetterdaten für mehrere Städte ab und erstellt eine Zusammenfassung."""
    summaries = []
    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=KEY"
        response = requests.get(url)
        data = response.json()
        
        summary = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        summaries.append(summary)
    
    return summaries
```

[ER] Schreiben Sie einen Test für `get_weather_summary(['Berlin', 'Stuttgart', 'Hamburg'])` mit Monkeypatching.

[HINT::Wie baut man mehrere verschiedene Resultate im selben Patch?]
Da die Funktion mehrere API-Aufrufe macht (einen pro Stadt), können Sie nicht einfach
`return_value` verwenden.
Nutzen Sie `side_effect` mit einer Funktion,
um für jede Stadt unterschiedliche Antworten zu geben.
[ENDHINT]

Für die Attrappe des Response-Objekts empfehlen wir `MagicMock()` aus `unittest.mock`.
`MagicMock()` ist eine Unterklasse von `Mock()` und unterstützt zusätzlich Dunder-Methoden
(`__len__()`, `__iter__()`, `__contains__()` usw.), die Python z. B. für `len()`, `for`-Schleifen
oder den `in`-Operator implizit aufruft.
`patch()` verwendet intern ebenfalls `MagicMock()` als Default.

Das Thema `MagicMock()` verfolgen wir hier nicht weiter, aber Sie sollten davon schon einmal
gehört haben, daher hier zur Verdeutlichung, wo der Unterschied liegt.

```python
# Mit Mock() fehlt Unterstützung für implizit aufgerufene Dunder-Methoden:
m = Mock()
print(len(m))   # TypeError: object of type 'Mock' has no len()

# Mit MagicMock() gibt es sinnvolle Standardwerte:
mm = MagicMock()
print(len(mm))  # 0 – MagicMock implementiert __len__() automatisch
```

[HINT::Wie baut man das Response-Objekt?]
`requests.get()` gibt ein Response-Objekt zurück, das eine `.json()` Methode hat.
Ihre Attrappe muss das nachahmen. Am einfachsten geht das mit `unittest.mock.MagicMock`.

[HINT::Ich verstehe den Aufbau des Response-Objekts nicht.]

```python
mock_response = MagicMock()
mock_response.json.return_value = {'main': {'temp': 25.0}, 'weather': [{'description': 'sunny'}]}
```

[ENDHINT]

[ENDHINT]

[HINT::Das mit dem URL wird aber ziemlich unelegant, oder?]
Um zu wissen, welche Antwort für welche Stadt zurückgegeben werden soll, müssen Sie
den URL analysieren. 
Dafür muss man aber nicht den ganzen URL im Mock-Code reproduzieren.
Eine einfache Lösung ist, darin nach `f"q={city}"` zu suchen.
[ENDHINT]

Eventuell sind Sie bei der Testfallerstellung mit Monkeypatching nicht so gut vorangekommen, wie Sie
es sich vielleicht erhofft haben.

[EQ] Was stört Sie an Ihrem Testcode? Welche Teile der ursprünglichen Funktion haben Sie im
Testcode "nachbauen" müssen?
<!-- time estimate: 30 min -->

#### Der elegantere Weg: Dependency Injection

Dependency Injection bedeutet: Die Attrappe wird dem Produktivcode vom Testcode förmlich übergeben
statt ihm sozusagen heimlich untergeschoben zu werden.

Schauen wir uns die Umgestaltung an:

```python
# weather_injectable.py
import requests

class WeatherAPI:
    """Kapselt den API-Zugriff"""
    def __init__(self, api_key="DEMO_KEY"):
        self.api_key = api_key
    
    def get_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url)
        return response.json()

def get_temperature_injectable(city, weather_api=None):
    """Temperatur abrufen mit Dependency Injection"""
    if weather_api is None:
        weather_api = WeatherAPI()  # Standard-Implementierung
    
    data = weather_api.get_weather(city)
    return data['main']['temp']
```

Jetzt können wir eine einfache Test-Attrappe schreiben:

```python
# test_weather_injectable.py
import pytest
from weather_injectable import get_temperature_injectable

class WeatherAPIMock:
    """Einfache Attrappe für WeatherAPI"""
    def __init__(self, temperature=20.0):
        self.temperature = temperature
        self.called_cities = []
    
    def get_weather(self, city):
        self.called_cities.append(city)
        return {'main': {'temp': self.temperature}}

def test_get_temperature_injectable():
    # Attrappe erstellen
    mock_api = WeatherAPIMock(temperature=25.5)
    
    # Funktion testen
    temp = get_temperature_injectable("München", weather_api=mock_api)
    
    # Verifikationen
    assert temp == 25.5
    assert "München" in mock_api.called_cities
```

[ER] Implementieren Sie beide Dateien und führen Sie den Test aus.

[ER] Implementieren Sie analog eine Dependency Injection für die Funktion `get_weather_summary()` von vorhin.

[NOTICE]
Für die genaue Form der Injektion gibt es verschiedene Ansätze.
Wir verwenden hier das sogenannte `None-Pattern`; es liefert eine Kombination von
guter Benutzbarkeit (nur der Testcode muss eine Attrappe injizieren; der Produktivcode tut nichts dergleichen)
und guter Testbarkeit (der Testcode kann ohne Umstände die gewünschte Attrappe injizieren).
[ENDNOTICE]
<!-- time estimate: 10 min -->

### Praxis: Verschiedene Szenarien

Nachdem Sie die beiden Grundtechniken kennengelernt haben, wenden wir sie nun
auf verschiedene praxistypische Szenarien an. Dabei können Sie selbst entscheiden,
welche Technik für das jeweilige Problem besser geeignet ist.

#### Szenario 1: Dateioperationen

Hier wird die eingebaute `open`-Funktion per Monkeypatching ersetzt.

In dieser Aufgabe geht es darum, Dateioperationen beim Testen gezielt zu isolieren.
Der Zugriff auf das Dateisystem ist fehleranfällig, langsam und macht Tests oft unhandlich,
weil echte Dateien erstellt oder bereitgestellt werden müssten.
Stattdessen lernen Sie hier, wie man die eingebaute `open`-Funktion mit `mock_open` ersetzt,
um gezielt das gewünschte Leseverhalten zu simulieren.

[ER] Schreiben Sie einen Test für die Funktion `read_log_file()`, die sich in der Datei
`file_example.py` befinden soll und eine Datei liest und verarbeitet.
Ersetzen Sie die Dateioperationen durch eine Attrappe, um zu verhindern, dass während der
Tests echte Dateien gelesen oder geschrieben werden.
Der Test soll zwei Zeilen mit "ERROR" betrachten plus eine Zeile ohne.

```python
# file_example.py
def read_log_file(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                count += 1
    return count
```

[HINT::Meine Attrappenidee macht ganz schön viel Arbeit!]
Eine File Handle hat ganz schön viel Funktionalität und sogar schon in unserem Minibeispiel
ist der Aufwand, dafür selbst eine Attrappe zu schreiben, nicht ganz klein.

Aber es gibt eine bequeme Lösung für Monkeypatching in der Standardbibliothek:
Betrachten Sie den Abschnitt `mock_open` in der offiziellen Dokumentation.
Nehmen Sie sich Zeit, die Dokumentation ist nicht ganz einfach zu verstehen.
Sie können `mock_open` nutzen, um die eingebaute open-Funktion durch eine Attrappe zu ersetzen
und dann Dateizugriffe zu simulieren, ohne tatsächlich Dateien lesen oder schreiben zu müssen.
[ENDHINT]

**Warum Attrappen hier sinnvoll sind**: Dateioperationen können langsam sein und das Hantieren
mit mehreren kleinen Testdateien ist unnötig umständlich.
<!-- time estimate: 10 min -->

#### Szenario 2: Fehlerzustände simulieren

Fehler treten in der echten Welt auf – aber selten dann, wenn man es im Test braucht.
Attrappen erlauben es uns, genau diese Situationen gezielt herbeizuführen, um zu überprüfen,
ob unser Code robust reagiert (Fehlerbehandlung, Logging, Retry, Defaults etc.).

[ER] Schreiben Sie einen Test für `get_weather_data()`, bei dem `requests.get()` absichtlich eine
Ausnahme (`requests.exceptions.ConnectionError`) auslöst.
Testen Sie, ob `get_weather_data()` damit richtig umgeht und z. B. `None` oder eine passende
Fehlermeldung zurückgibt.
Verwenden Sie `patch()`, um den Fehler gezielt auszulösen.
Die getestete Funktion soll in `error_example.py` liegen.

```python
# error_example.py
import requests

def get_weather_data(city):
    url = f"https://example-weather-api.com/data?city={city}"
    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.ConnectionError:
        return None
```
<!-- time estimate: 10 min -->

### Reflexion: "Wann sollte man Attrappen verwenden und wann lieber nicht?"

#### Testdoubles: "Attrappen sind nicht alle gleich"

Lesen Sie den Abschnitt "The Difference Between Mocks and Stubs" im
[Artikel von Martin Fowler zu "Mocking"](https://martinfowler.com/articles/mocksArentStubs.html).
Der Artikel behandelt Mock, Stub und Fake.
Für diese Aufgabe verwenden wir die vollständige Taxonomie nach Gerard Meszaros,
die fünf Arten von Testdoubles unterscheidet:

- **Dummy**: Wird als Parameter übergeben, aber nie wirklich benutzt (reiner Platzhalter).
- **Fake**: Funktionierende, aber vereinfachte Implementierung (z. B. In-Memory statt Datenbank).
- **Stub**: Gibt kontrollierte, vordefinierte Antworten zurück; prüft keine Aufrufe.
- **Spy**: Zeichnet Aufrufe auf, damit der Test sie hinterher verifizieren kann.
- **Mock**: Vorkonfiguriert mit Erwartungen; schlägt fehl, wenn diese nicht erfüllt werden.

[ER] Betrachten Sie die folgende Funktion `send_email_to_users(users, email_service)`, die sich in
der Datei `testdoubles_example.py` befinden soll, und entscheiden Sie, welche Art von Testdouble
(Dummy, Fake, Stub, Spy, Mock) für `email_service` am besten geeignet ist.
Implementieren Sie das Testdouble und schreiben Sie einen Test für diese Funktion.

```python
# testdoubles_example.py
def send_email_to_users(users, email_service):
    for user in users:
        email_service.send_email(user['email'], "Welcome!", "Hello, welcome to our service!")
```

[EQ] Reflektieren Sie: Warum haben Sie sich für das entsprechende Testdouble aus der Testdoubles-Aufgabe
entschieden, und nicht für die anderen Möglichkeiten?
<!-- time estimate: 20 min -->

#### Vor- und Nachteile von Attrappen

Lesen Sie den Artikel
"[When to Mock](https://blog.cleancoder.com/uncle-bob/2014/05/10/WhenToMock.html)"
von Robert C. Martin ("Uncle Bob").

[EQ] Uncle Bob empfiehlt, Attrappen auf Grenzüberschreitungen zu beschränken
(d. h. überall dort, wo Code aus einer Schicht in eine andere wechselt).
Stimmen Sie dieser Empfehlung zu?
Begründen Sie Ihre Antwort anhand eines konkreten Beispiels aus den Aufgaben oben.
<!-- time estimate: 25 min -->

#### Abschluss

[EC] Führen Sie Ihre Tests mit `pytest -v` aus.

[ENDSECTION]

[SECTION::submission::snippet,reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
