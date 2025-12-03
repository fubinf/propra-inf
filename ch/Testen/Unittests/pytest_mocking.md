title: "'unittest.mock': Ersetzen von Objekten für Testzwecke"
stage: alpha
timevalue: 3.0
difficulty: 3
assumes: m_pytest
---

[SECTION::goal::idea]

- Ich kann beschreiben, was Attrappen ("Mocks") sind und wie sie in pytest Anwendung finden.
- Ich kann grundlegende Unittests mittels Attrappen realisieren.
- Ich kann begründen, wann die Anwendung von Attrappen sinnvoll ist.
[ENDSECTION]


[SECTION::background::default]
Unittests auf elementare Module sind kein Problem.
Aber wenn ein Modul von vielen anderen Dingen abhängt, stellt sich die Frage, ob man die
alle mittesten soll und will.
Falls es _nicht_ sinnvoll zu sein scheint, kann man es mithilfe von Attrappen vermeiden,
die an die Stelle jener anderen Module treten.

Für manche Zwecke ist das mehr eine Geschmacksfrage, in anderen Fällen, vor allem für
Tests, die mit Zeit zu tun haben, ist es eine unverzichtbare Testtechnik.
[ENDSECTION]

[SECTION::instructions::loose]

### Vorbereitung

Verschaffen Sie sich einen groben Überblick über die 
[Dokumentation von `unittest.mock`](https://docs.python.org/3/library/unittest.mock.html).

### Aufgaben 

Zu jeder Aufgabe wird es eine zu testende Funktion geben, die in der Aufgabe vorgegeben ist und
die Sie jeweils in einer separaten Datei ablegen sollen.
Der Name dieser Datei ist jeweils oben in dem Codeblock angegeben, z.B. 
`mock_example_1.py`.

Ihre Aufgabe ist es, die externen Abhängigkeiten und Seiteneffekte zu Ihren Tests zu isolieren,
damit Sie sich auf das Testen der eigentlichen Logik Ihrer Funktionen und Methoden konzentrieren
können.

#### Abhängigkeitsbezogenes Mocking

Wir wollen, dass die zu testende Funktion ihre Abhängigkeiten (z. B. API- oder Datenbankzugriffe)
nicht intern erzeugt, sondern als Argument erhält.
Dadurch lässt sich das Verhalten gezielt im Test kontrollieren, ohne auf globale Patches zurückzugreifen.
Diese Methode nennt sich [TERMREF::Dependency Injection].

- [ER] Schreiben Sie einen Test für `process_user()`, die sich in der Datei `mock_example_1.py`
  befindet, indem Sie ein manuell erstelltes Mock-Objekt als `user_service` einspeisen.
  Der Test soll überprüfen, ob process_user() das Ergebnis korrekt verarbeitet und zurückgibt.
  Verwenden Sie kein `patch()` oder `Mock()` aus pytest-mock oder unittest.mock, sondern schreiben
  Sie ein eigenes Testobjekt.

```Python
# mock_example_1.py

class UserService:
    def fetch_user(self, user_id):
        # Stelle Sie sich vor, dass hier ein echter API-Aufruf stattfinden würde
        return {"id": user_id, "name": "Max Mustermann"}

def process_user(user_id, user_service):
    user = user_service.fetch_user(user_id)
    return f"User: {user['name']} (ID: {user['id']})"
```

Falls man keinen sauberen Weg hat, ein Mock-Objekt einzuspeisen (z. B. weil die Abhängigkeit im
Code hart kodiert ist), kann man als technischen Workaround `patch` oder `mock_open` verwenden.
In den folgenden Aufgaben sehen Sie solche Szenarien.

#### Mocking einer Web-API

In dieser Aufgabe lernen Sie, wie man externe Abhängigkeiten wie Web-APIs im Test durch Mocking
ersetzt.
Der Fokus liegt darauf, den Einfluss externer Systeme – hier: eine [TERMREF::HTTP]-Anfrage an einen
Wetterdienst – gezielt zu isolieren, um die Logik der Funktion zuverlässig und reproduzierbar zu
testen.
Dazu werden Sie den Netzwerkaufruf mit einem Mock-Objekt simulieren, ohne dass tatsächlich eine
Verbindung zum Internet hergestellt wird.

- [ER] Schreiben Sie einen Pytest für die Funktion `get_weather_data()` wie unten angegeben, die
  sich in der Datei `mock_example_2.py` befinden soll und eine Web-API aufruft.
  Mocken Sie den API-Aufruf `requests.get`, um sicherzustellen, dass während des Tests keine
  echte Netzwerkanfrage gemacht wird, denn diese dauert erstens relativ lange und könnte zweitens
  (wie in unserem Fall) fehlschlagen, wenn der betreffende externe Server nicht antwortet -- wozu
  es viele Gründe geben kann.  
  Der Test soll erwarten, dass die Antwort `{"temperature": 22, "weather": "sunny"}` lautet.
  Er soll außerdem sicherstellen, dass wirklich der korrekte URL angefragt wurde.

```Python
# mock_example_2.py

import requests

def get_weather_data(city):
    url = f"https://example-weather-api.com/data?city={city}"
    response = requests.get(url)
    return response.json()
```

[HINT::Mockobjekte einsetzen]
Betrachten Sie den Bereich `patch` in der offiziellen Dokumentation.
Wir können `patch` nutzen, um bestimmte Objekte oder Funktionen während der Ausführung eines Tests
zu ersetzen (zu "mocken"). 
Dies ermöglicht es uns, das Verhalten des ersetzten Teils genau so zu gestalten, wie es für unseren Test
am günstigsten ist,
und somit sicherzustellen, dass der Test isoliert und unabhängig von externen Faktoren bleibt.
[ENDHINT]

**Warum Mocking hier sinnvoll ist**: Netzwerkanfragen können langsam und unzuverlässig sein. Durch
Mocking können wir sicherstellen, dass unsere Tests schnell und zuverlässig sind.

#### Mocking von Dateioperationen

In dieser Aufgabe geht es darum, Dateioperationen beim Testen gezielt zu isolieren.
Der Zugriff auf das Dateisystem ist fehleranfällig, langsam und macht Tests oft unhandlich,
weil echte Dateien erstellt oder bereitgestellt werden müssten.
Stattdessen lernen Sie hier, wie man die eingebaute `open`-Funktion mit `mock_open` ersetzt,
um gezielt das gewünschte Leseverhalten zu simulieren.

- [ER] Schreiben Sie einen Pytest für die Funktion `read_log_file()`, die sich in der Datei
  `mock_example_3.py` befinden soll und eine Datei liest und verarbeitet. Mocken Sie die
  Dateioperationen, um zu verhindern, dass während der Tests echte Dateien gelesen oder geschrieben
  werden.
  Der Test soll zwei Zeilen mit "ERROR" betrachten plus eine Zeile ohne.

```Python
# mock_example_3.py

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
Wir können `mock_open` nutzen, um die eingebaute open-Funktion zu mocken. Dies ermöglicht es uns,
Dateizugriffe zu simulieren, ohne tatsächlich Dateien lesen oder schreiben zu müssen. `mock_open` ist
besonders nützlich, um das Verhalten von Funktionen zu testen, die Dateien öffnen und lesen oder
schreiben, ohne dass echte Dateien benötigt werden.
[ENDHINT]

**Warum Mocking hier sinnvoll ist**: Dateioperationen können langsam sein und erfordern spezielle
Testdateien. Durch Mocking können wir diese Abhängigkeiten eliminieren.

#### Mocking von Klassenmethoden

In dieser Aufgabe untersuchen Sie zwei Varianten, wie man Methoden von Klassen testen kann –
insbesondere sogenannte Klassenmethoden.
Im ersten Fall wird durch sauberen Testentwurf ([TERMREF::Dependency Injection]) die externe Abhängigkeit
explizit übergeben.
Im zweiten Fall ist das nicht vorgesehen, weshalb `patch()` als technischer Workaround zum Einsatz
kommt.
Beide Varianten zeigen typische Wege auf, wie man Klassenmethoden in Pytest testen und isolieren kann.

- [ER] Schreiben Sie einen Test für `process_user_data()` mit Dependency Injection, die sich in der
  Datei `mock_example_4.1.py` befinden soll.
  Erstellen Sie ein eigenes Mock-Objekt und übergeben Sie es der Funktion. (Vgl. [EREFR::1])
  Verwenden Sie kein patch().

- [ER] Schreiben Sie einen Pytest für die Funktion `process_user_data()`, die sich in der Datei
  `mock_example_4.2.py` befinden soll und die von einer Klasse in Ihrem Projekt abhängt.
  Mocken Sie diese Variabnte mit `patch()`.

```Python
# mock_example_4.1.py

class UserManager:
    def __init__(self, backend):
        self.backend = backend

    @classmethod
    def process_user_data(cls, user_id, backend):
        instance = cls(backend)
        return instance.backend.get_user_data(user_id)
```

```Python
# mock_example_4_2.py

class UserManager:
    def get_user_data(self, user_id):
        return {"name": "Max Mustermann", "email": "max@example.com"}

    @classmethod
    def process_user_data(cls, user_id):
        instance = cls()
        return instance.get_user_data(user_id)
```

**Warum Mocking hier sinnvoll ist**: Die Klasse `UserManager` könnte komplexe Abhängigkeiten haben.
Durch Mocking können wir diese Abhängigkeiten eliminieren und uns auf die Logik von `process_user_data`
konzentrieren.

#### Mocking von Datenbankoperationen

In dieser Aufgabe lernen Sie, wie man Datenbankzugriffe beim Testen durch Mocking ersetzt.
Der Zugriff auf echte Datenbanken bringt viele Herausforderungen mit sich – von der Performance
über die Testdatenpflege bis hin zur Reproduzierbarkeit von Ergebnissen.

- [ER] Schreiben Sie eine Funktion `get_user_age()`, die sich in der Datei `mock_example_5.py`
  befinden soll und die das Alter eines Benutzers aus einer SQL-Datenbank abruft. Schreiben Sie
  anschließend Unittests für diese Funktion, wobei die Datenbankverbindung und -abfragen gemockt
  werden, um keine echte Datenbank zu verwenden.

```Python
# mock_example_5.py

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
Wir könnten ebenfalls MagicMock nutzen, um ein Mock-Objekt zu erstellen, das sich wie ein echtes
Objekt verhält und Methodenaufrufe sowie deren Rückgabewerte simulieren kann. 
MagicMock ist besonders nützlich, wenn wir komplexe Objekte oder Methoden mit mehreren Attributen
und Methoden mocken müssen.
In diesem Fall wird MagicMock verwendet, um das Verhalten des Datenbank-Cursors zu simulieren,
einschließlich der Rückgabe von Ergebnissen für SQL-Abfragen.
[ENDNOTICE]

**Warum Mocking hier sinnvoll ist**: Datenbankoperationen können langsam und komplex sein. Durch
Mocking können wir sicherstellen, dass unsere Tests schnell und zuverlässig sind.

#### Fehlerzustände mit Mocking simulieren

Fehler treten in der echten Welt auf – aber selten dann, wenn man es im Test braucht.
Mocking erlaubt es uns, genau diese Situationen gezielt herbeizuführen, um zu überprüfen,
ob unser Code robust reagiert (Fehlerbehandlung, Logging, Retry, Defaults etc.).

- [ER] Schreiben Sie einen Test für `get_weather_data()`, bei dem `requests.get()` absichtlich eine
  Ausnahme (`requests.exceptions.ConnectionError`) auslöst.
  Testen Sie, ob `get_weather_data()` damit richtig umgeht und z. B. `None` oder eine passende
  Fehlermeldung zurückgibt.
  Verwenden Sie `patch()`, um den Fehler gezielt auszulösen.
  Die getestete Funktion soll in `mock_example_7.py` liegen.

```Python
# mock_example_7.py

import requests

def get_weather_data(city):
    url = f"https://example-weather-api.com/data?city={city}"
    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.ConnectionError:
        return None
```

### Reflektion: "Wann sollte man wie mocken und wann lieber nicht?"

#### Testdoubles: "Mocken ist nicht gleich mocken"

Überfliegen Sie den
[Artikel von Martin Fowler zu "Mocking"](https://martinfowler.com/articles/mocksArentStubs.html).
Lesen Sie den Bereich der Testdoubles.

- [ER] Betrachten Sie die folgende Funktion `send_email_to_users(users, email_service)`, die sich in
  der Datei `mock_example_6.py` befinden soll und entscheiden Sie, welche Art von Testdouble
  (Dummy, Fake, Stub, Spy, Mock) am besten geeignet ist. Implementieren Sie die entsprechenden
  Testdoubles und schreiben Sie Pytests für diese Funktion.

```python
# mock_example_6.py

def send_email_to_users(users, email_service):
    for user in users:
        email_service.send_email(user['email'], "Welcome!", "Hello, welcome to our service!")
```

#### Vor- und Nachteile vom Mocking

Nutzen Sie den folgenden Artikel von Robert C. Martin (oft genannt "Uncle Bob") zum Thema
["When to Mock"](https://blog.cleancoder.com/uncle-bob/2014/05/10/WhenToMock.html).

- [EQ] Stimmen Sie den Aussagen von "Uncle Bob" zu?
  Welcher am meisten? Warum?
  Welcher am wenigsten? Warum?

#### Abhängiges vs. manuelles Testen

- [EQ] Reflektieren Sie: Was ist gegenüber dem Dependency Injection sauberer als bei patch()?

- [EQ] Reflektieren Sie: Warum haben Sie sich für das entsprechende Testdouble aus Aufgabe [EREFR::6]
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
