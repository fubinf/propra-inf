title: "'unittest.mock': Ersetzen von Objekten für Testzwecke"
stage: alpha
timevalue: 3.0
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
Tests, die mit Zeit zu tun haben, ist es eine unverzichtbare Testtechnik.

Stellen Sie sich vor, Sie wollen eine Funktion testen, die Wetterinformationen von einer Web-API abruft,
das Ergebnis in einer Datenbank speichert und eine E-Mail verschickt.
Für einen Unittest wollen Sie aber weder auf das Internet zugreifen, noch eine echte Datenbank verwenden,
noch echte E-Mails versenden.

Hier kommen **Attrappen** ins Spiel - Ersatzobjekte, die sich wie die echten Abhängigkeiten verhalten,
aber unter Ihrer Kontrolle stehen.

[ENDSECTION]

[SECTION::instructions::detailed]

Nutzen Sie die Übersicht
[Pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
und die [Dokumentation von `unittest.mock`](https://docs.python.org/3/library/unittest.mock.html)
parallel zum Bearbeiten der Aufgaben.

### Warum Attrappen? Das Problem verstehen

Betrachten Sie folgenden realitätsnahen Code, der mehrere externe Abhängigkeiten hat:

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
            server.login('bot@example.com', 'password')
            server.sendmail('bot@example.com', user_email, 
                          f"Achtung: Es ist sehr kalt in {city}!")
    
    return weather_data['main']['temp']
```

[EQ] Was sind die Probleme, wenn Sie diesen Code direkt testen wollten?

Die vin Ihnen identifizierten Probleme können wir umgehen.
Was wir dafür machen müssen, sehen wir im folgenden Kapitel.

### Zwei Wege zum Ziel: Monkeypatching vs. Dependency Injection

Es gibt grundsätzlich u.a. zwei gute Techniken, um Abhängigkeiten durch Attrappen zu ersetzen:

**Monkeypatching:** Zur Laufzeit wird das Original durch die Attrappe ersetzt.

- Vorteil: Funktioniert ohne Codeänderung an der zu testenden Funktion
- Nachteil: "Magisch", schwieriger zu verstehen, mehr Redundanz im Testcode

**Dependency Injection:** Die Abhängigkeit wird als Parameter übergeben.

- Vorteil: Explizit, sauber, einfach zu verstehen  
- Nachteil: Erfordert Umgestaltung des zu testenden Codes

Wir schauen uns beide Ansätze an, beginnend mit dem `Monkeypatching`, da wir hier keine
Vorbedingungen benötigen.

#### Erste Schritte: Monkeypatching mit patch()

Zu jeder kommenden Aufgabe wird es eine zu testende Funktion geben, die in der Aufgabe vorgegeben
ist oder von Ihnen erstellt werden soll.
Der Name dieser Datei ist jeweils oben in dem Codeblock als Kommentar angegeben,
z.B.  `mock_example_1.py`.

Lassen Sie uns mit einem einfachen Beispiel beginnen. Erstellen Sie die Datei `weather_simple.py`:

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
Das ist langsam, abhängig vom Internet und Sie haben keine Kontrolle über die Antwort.

Mit Monkeypatching ersetzen wir `requests.get` durch eine Attrappe:

```python
# test_weather_simple.py
import pytest
from unittest.mock import patch
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

[NOTICE]
Eventuell ist Ihnen aufgefallen, dass Sie trotz des Mocking dennoch das in der Hauptfunktion
verwendete request-Modul installieren müssen.
In der Praxis fällt das weniger auf, da Sie bei der Entwicklung der Funktionen bewusst auf das
Modul zugreifen wollen würde.
[ENDNOTICE]

[EQ] Was passiert bei der Ausführung von `patch('weather_simple.requests.get')`?
Erklären Sie den Mechanismus in eigenen Worten.

[HINT::Patching]
Sie könne [patch()](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch)
auch in der Dokumentation nachlesen.
[ENDHINT]

##### Das Problem mit Monkeypatching: Redundanz

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

[ER] Schreiben Sie einen Test für `get_weather_summary()` mit Monkeypatching.
Testen Sie mindestens 2 Städte mit unterschiedlichen Wetterdaten.

[HINT::Return]
Da die Funktion mehrere API-Aufrufe macht (einen pro Stadt), können Sie nicht einfach
`return_value` verwenden. Nutzen Sie stattdessen `side_effect` mit einer Funktion oder 
einem Mapping, um für jede Stadt unterschiedliche Antworten zu geben.
[ENDHINT]

[HINT::Payload]
`requests.get()` gibt ein Response-Objekt zurück, das eine `.json()` Methode hat.
Ihre Attrappe muss das nachahmen (Sie benötigen dafür `from unittest.mock import MagicMock`):

```python
mock_response = MagicMock()
mock_response.json.return_value = {'main': {'temp': 25.0}, 'weather': [{'description': 'sunny'}]}
```

[ENDHINT]

[HINT::URL-Parsing]
Um zu wissen, welche Antwort für welche Stadt zurückgegeben werden soll, müssen Sie
die URL analysieren. Eine einfache Lösung ist, in der URL nach "q=Stadtname" zu suchen:

```python
if "q=Berlin" in url:
    return berlin_response
elif "q=München" in url:
    return muenchen_response
```

[ENDHINT]

Eventuell sind Sie bei der Testfallerstellung mit Monkeypatching nicht so gut vorangekommen, wie Sie
es sich vielleicht erhofft haben.

[EQ] Was stört Sie an Ihrem Testcode? Welche Teile der ursprünglichen Funktion haben Sie im
Testcode "nachbauen" müssen?

#### Der elegantere Weg: Dependency Injection

Dependency Injection bedeutet: Die Abhängigkeit wird "von außen" übergeben statt intern erstellt.

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

[ER] Implementieren Sie eine Depency Injection für die Funktion `get_weather_summary()`.

[HINT::Weiteres Objekt betrachten]
Auch hier werden Sie sich bestimmt die Zähne ausbeißen, denn so ganz ohne etwas Anpassung wird es
nicht gehen.
Sicherlich haben Sie im obigen Beispiel erkannt, dass ein weiteres Object von der Funktion
akzeptiert wird. Wir verwenden hier das sogenannte `None-Pattern` und beinhaltet einen guten
Kompromiss zwischen Usability. und Testability.
Demnach, werden Sie bei der UUmstellung Ihres Tests eine APIMock-Klasse benötigen, die Sie in
der Datei `weather_injectable.py` bereits verwendet haben.
[ENDHINT]

### Praxis: Verschiedene Szenarien

Jetzt sind Sie sicherlich schon etwas warm.
Das wollen wir ausnutzen und uns noch mit drei kleinen Themen beschäftigen, die nichts mit API
zu tun haben, aber genauso gerne vorkommen.

Nachdem Sie die beiden Grundtechniken kennengelernt haben, wenden wir sie nun
auf verschiedene realistische Szenarien an. Dabei können Sie selbst entscheiden,
welche Technik für das jeweilige Problem besser geeignet ist.

#### Szenario 1: Dependency Injection mit manueller Attrappe

Hier beginnen wir mit dem sauberen Ansatz: Die Funktion ist bereits für 
Dependency Injection entworfen.

In dieser Aufgabe geht es darum, Dateioperationen beim Testen gezielt zu isolieren.
Der Zugriff auf das Dateisystem ist fehleranfällig, langsam und macht Tests oft unhandlich,
weil echte Dateien erstellt oder bereitgestellt werden müssten.
Stattdessen lernen Sie hier, wie man die eingebaute `open`-Funktion mit `mock_open` ersetzt,
um gezielt das gewünschte Leseverhalten zu simulieren.

- [ER] Schreiben Sie einen Test für die Funktion `read_log_file()`, die sich in der Datei
  `file_example.py` befinden soll und eine Datei liest und verarbeitet.
  Ersetzen Sie die Dateioperationen durch eine Attrappe, um zu verhindern, dass während der
  Tests echte Dateien gelesen oder geschrieben werden.
  Der Test soll zwei Zeilen mit "ERROR" betrachten plus eine Zeile ohne.

```Python
# file_example.py
def read_log_file(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                count += 1
    return count
```

[HINT::Dateioperationen]
Betrachten Sie den Bereich `mock_open` in der offiziellen Dokumentation.
Wir können `mock_open` nutzen, um die eingebaute open-Funktion durch eine Attrappe zu ersetzen.
Dies ermöglicht es uns, Dateizugriffe zu simulieren, ohne tatsächlich Dateien lesen oder schreiben
zu müssen. `mock_open` ist besonders nützlich, um das Verhalten von Funktionen zu testen, die
Dateien öffnen und lesen oder schreiben, ohne dass echte Dateien benötigt werden.
[ENDHINT]

**Warum Attrappen hier sinnvoll sind**: Dateioperationen können langsam sein und erfordern spezielle
Testdateien. Durch Attrappen können wir diese Abhängigkeiten eliminieren.

#### Szenario 2: Datenbankoperationen mit MagicMock

In dieser Aufgabe lernen Sie, wie man Datenbankzugriffe beim Testen durch Attrappen ersetzt.
Der Zugriff auf echte Datenbanken bringt viele Herausforderungen mit sich – von der Performance
über die Testdatenpflege bis hin zur Reproduzierbarkeit von Ergebnissen.

- [ER] Schreiben Sie einen Test für die Funktion `get_user_age()`, die sich in der Datei
  `database_example.py` befinden soll und die das Alter eines Benutzers aus einer SQL-Datenbank
  abruft.
  Schreiben Sie einen Pytest für diese Funktion, wobei die Datenbankverbindung und -abfragen durch
  Attrappen ersetzt werden, um keine echte Datenbank zu verwenden.

```Python
# database_example.py
import sqlite3

def get_user_age(user_id):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
```

[NOTICE]
Wir könnten ebenfalls MagicMock nutzen, um ein Attrappen-Objekt zu erstellen, das sich wie ein echtes
Objekt verhält und Methodenaufrufe sowie deren Rückgabewerte simulieren kann. 
MagicMock ist besonders nützlich, wenn wir komplexe Objekte oder Methoden mit mehreren Attributen
und Methoden durch Attrappen ersetzen müssen.
In diesem Fall wird MagicMock verwendet, um das Verhalten des Datenbank-Cursors zu simulieren,
einschließlich der Rückgabe von Ergebnissen für SQL-Abfragen.
[ENDNOTICE]

**Warum Attrappen hier sinnvoll sind**: Datenbankoperationen können langsam und komplex sein. Durch
Attrappen können wir sicherstellen, dass unsere Tests schnell und zuverlässig sind.

#### Szenario 3: Fehlerzustände simulieren

Fehler treten in der echten Welt auf – aber selten dann, wenn man es im Test braucht.
Attrappen erlauben es uns, genau diese Situationen gezielt herbeizuführen, um zu überprüfen,
ob unser Code robust reagiert (Fehlerbehandlung, Logging, Retry, Defaults etc.).

- [ER] Schreiben Sie einen Test für `get_weather_data()`, bei dem `requests.get()` absichtlich eine
  Ausnahme (`requests.exceptions.ConnectionError`) auslöst.
  Testen Sie, ob `get_weather_data()` damit richtig umgeht und z. B. `None` oder eine passende
  Fehlermeldung zurückgibt.
  Verwenden Sie `patch()`, um den Fehler gezielt auszulösen.
  Die getestete Funktion soll in `error_example.py` liegen.

```Python
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

### Reflektion: "Wann sollte man Attrappen verwenden und wann lieber nicht?"

#### Testdoubles: "Attrappen sind nicht alle gleich"

Überfliegen Sie den
[Artikel von Martin Fowler zu "Mocking"](https://martinfowler.com/articles/mocksArentStubs.html).
Lesen Sie den Bereich der Testdoubles.

- [ER] Betrachten Sie die folgende Funktion `send_email_to_users(users, email_service)`, die sich in
  der Datei `testdoubles_example.py` befinden soll und entscheiden Sie, welche Art von Testdouble
  (Dummy, Fake, Stub, Spy, Mock) am besten geeignet ist. Implementieren Sie die entsprechenden
  Testdoubles und schreiben Sie Tests für diese Funktion.

```python
# testdoubles_example.py
def send_email_to_users(users, email_service):
    for user in users:
        email_service.send_email(user['email'], "Welcome!", "Hello, welcome to our service!")
```

#### Vor- und Nachteile von Attrappen

Nutzen Sie den folgenden Artikel von Robert C. Martin (oft genannt "Uncle Bob") zum Thema
["When to Mock"](https://blog.cleancoder.com/uncle-bob/2014/05/10/WhenToMock.html).

- [EQ] Stimmen Sie den Aussagen von "Uncle Bob" zu?
  Welcher am meisten? Warum?
  Welcher am wenigsten? Warum?

#### Dependency Injection vs. Monkeypatching

- [EQ] Reflektieren Sie: Was ist an Dependency Injection sauberer als bei patch()?

- [EQ] Reflektieren Sie: Warum haben Sie sich für das entsprechende Testdouble aus der Testdoubles-Aufgabe
  entschieden, und nicht für die anderen Möglichkeiten?

[ENDSECTION]

[SECTION::submission::program]

Reichen Sie für jede der Aufgaben [EREFR::1], [EREFR::2], [EREFR::3], [EREFR::4], [EREFR::5],
[EREFR::6] und [EREFR::7] eine Python-Dateien ein.

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
