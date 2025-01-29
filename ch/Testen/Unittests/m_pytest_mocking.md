title: Pytest in Python - Mocking Anwendung
stage: alpha
timevalue: 3.0
difficulty: 2
assumes: m_pytest
---

[SECTION::goal::idea]

- Ich kann grundlegende Unittests in verschiedenen Anwendungsbereichen mocken.
- Ich kann beschreiben, was "Mocks" sind und wie sie in pytest Anwendung finden.
- Ich kann "Mocks" von anderen Testmethoden abgrenzen.
- Ich kann begründen, wann die Anwendung von "Mocks" sinnvoll ist.

[ENDSECTION]

[SECTION::background::default]

Unittests auf elementare Module sind kein Problem.
Aber wenn ein Modul von vielen anderen Dingen abhängt, stellt sich die Frage, ob man die
alle mittesten soll und will.

Mocking ist ein Mechanismus, der das Nicht-Mittesten erlaubt, indem eine Abhängigkeit
durch einen simplen Dummy ersetzt wird, der gerade genug kann für den aktuellen Testfall.
Typische Fälle für solche Abhängigkeiten sind
externe Web-APIs,
Dateien mit bestimmten Eigenschaften,
Datenbanksysteme
oder irgendwelche eigenen Klassen, die für den Testzweck zu kompliziert zu konfigurieren sind,
weil dazu noch viele weitere Objekte als Voraussetzung nötig wären, die selber wiederum... --
und so weiter.

[ENDSECTION]
[SECTION::instructions::loose]

### Vorbereitung

- Installieren Sie `pytest` mittels `pip install pytest`.
- Verschaffen Sie sich einen Überblick über die offizielle Dokumentation zu `unittest.mock`
  [hier](https://docs.python.org/3/library/unittest.mock.html).

### Aufgaben 

Zu jeder Aufgabe wird es eine kleine Funktion geben, die in einer Datei abzulegen ist.

- Erstellen Sie die Datei `m_pytest_mocking.py`, um anschließend damit zu arbeiten.

Ihre Aufgabe ist es, die externen Abhängigkeiten und Seiteneffekte zu Ihren Tests zu isolieren,
damit Sie sich auf das Testen der eigentlichen Logik einer Funktionen und Methoden konzentrieren
können.

#### Aufgabe 1: Mocking einer externen API

- [ER] Schreiben Sie einen Pytest für die Funktion `get_weather_data()`, die sich in der Datei
  `m_pytest_mocking.py` befinden soll und eine externe API aufruft. Mocken Sie den API-Aufruf, um
  sicherzustellen, dass keine echten Netzwerkanfragen während des Tests gemacht werden.

```Python
import requests

def get_weather_data(city):
    url = f"https://example-weather-api.com/data?city={city}"
    response = requests.get(url)
    return response.json()
```

[HINT::Mockobjekte ersetzen]
Betrachten Sie den Bereich `patch` in der offiziellen Dokumentation.
Wir können patch nutzen, um bestimmte Objekte oder Funktionen während der Ausführung eines Tests
zu ersetzen (zu mocken). Dies ermöglicht es uns, das Verhalten von Abhängigkeiten zu kontrollieren
und sicherzustellen, dass der Test isoliert und unabhängig von externen Faktoren bleibt.
[ENDHINT]

**Warum Mocking hier sinnvoll ist**: Netzwerkanfragen können langsam und unzuverlässig sein. Durch
Mocking können wir sicherstellen, dass unsere Tests schnell und zuverlässig sind.

#### Aufgabe 2: Mocking von Dateioperationen

- [ER] Schreiben Sie einen Pytest für die Funktion `read_log_file()`, die sich in der Datei
  `m_pytest_mocking.py` befinden soll und eine Datei liest und verarbeitet. Mocken Sie die
  Dateioperationen, um zu verhindern, dass während der Tests echte Dateien gelesen oder geschrieben
  werden.

```Python
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
Wir können mock_open nutzen, um die eingebaute open-Funktion zu mocken. Dies ermöglicht es uns,
Dateizugriffe zu simulieren, ohne tatsächlich Dateien lesen oder schreiben zu müssen. mock_open ist
besonders nützlich, um das Verhalten von Funktionen zu testen, die Dateien öffnen und lesen oder
schreiben, ohne dass echte Dateien benötigt werden.
[ENDHINT]

**Warum Mocking hier sinnvoll ist**: Dateioperationen können langsam sein und erfordern spezielle
Testdateien. Durch Mocking können wir diese Abhängigkeiten eliminieren.

#### Aufgabe 3: Mocking von Klassenmethoden

- [ER] Schreiben Sie einen Pytest für die Funktion `process_user_data()`, die sich in der Datei
  `m_pytest_mocking.py` befinden soll und die von einer Klasse in Ihrem Projekt abhängt. Mocken Sie die
  Abhängigkeit, um isolierte Tests durchzuführen.

```Python
class UserManager:
    def get_user_data(self, user_id):
        # Stellen Sie sich vor, dass hier echte Netzwerkanfragen stattfinden
        return {"name": "Max Mustermann", "email": "max@example.com"}

def process_user_data(user_id):
    user_manager = UserManager()
    user_data = user_manager.get_user_data(user_id)
    # Stellen Sie sich vor, dass diese Daten hier weiter verarbeitet werden
    return user_data
```

**Warum Mocking hier sinnvoll ist**: Die Klasse `UserManager` könnte komplexe Abhängigkeiten haben.
Durch Mocking können wir diese Abhängigkeiten eliminieren und uns auf die Logik von `process_user_data`
konzentrieren.

#### Aufgabe 4: Mocking von Datenbankoperationen

- [ER] Schreiben Sie eine Funktion `get_user_age()`, die sich in der Datei `m_pytest_mocking.py`
  befinden soll und die das Alter eines Benutzers aus einer SQL-Datenbank abruft. Schreiben Sie
  anschließend Unittests für diese Funktion, wobei die Datenbankverbindung und -abfragen gemockt
  werden, um keine echte Datenbank zu verwenden.

```Python
import sqlite3

def get_user_age(user_id):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
```

[HINT::Klasse]
Betrachten Sie den Bereich `MagicMock` in der offiziellen Dokumentation.
Wir können MagicMock nutzen, um ein Mock-Objekt zu erstellen, das sich wie ein echtes Objekt verhält und
Methodenaufrufe sowie deren Rückgabewerte simulieren kann. MagicMock ist besonders nützlich, wenn
wir komplexe Objekte oder Methoden mit mehreren Attributen und Methoden mocken müssen. In diesem
Fall wird MagicMock verwendet, um das Verhalten des Datenbank-Cursors zu simulieren, einschließlich
der Rückgabe von Ergebnissen für SQL-Abfragen.
[ENDHINT]

**Warum Mocking hier sinnvoll ist**: Datenbankoperationen können langsam und komplex sein. Durch
Mocking können wir sicherstellen, dass unsere Tests schnell und zuverlässig sind.

### Reflektion: "Wann sollte man wie mocken und wann lieber nicht"

#### Testdoubles: "Mocken ist nicht gleich mocken"

Überfliegen Sie den Artikel von Martin Fowler [hier](https://martinfowler.com/articles/mocksArentStubs.html).
Lesen Sie den Bereich der Testdoubles.

- [ER] Betrachten Sie die folgende Funktion `send_email_to_users(users, email_service)`, die sich in
  der Datei `m_pytest_mocking.py` befinden soll und entscheiden Sie, welche Art von Testdouble
  (Dummy, Fake, Stub, Spy, Mock) am besten geeignet ist. Implementieren Sie die entsprechenden
  Testdoubles und schreiben Sie Pytests für diese Funktion.

```python
def send_email_to_users(users, email_service):
    for user in users:
        email_service.send_email(user['email'], "Welcome!", "Hello, welcome to our service!")
```

#### Vor- und Nachteile vom Mocking

Nutzen Sie den folgenden Artikel von Robert C. Martin zum Thema ["When to Mock"](https://blog.cleancoder.com/uncle-bob/2014/05/10/WhenToMock.html).

- [EQ] Stimmen Sie den Aussagen von `Uncle Bob` zu? Welche Aussagen können Sie warum besonders unertstreichen?
- [EQ] Fallen Ihnen weitere Argumente ein, wann Mocking weniger bis gar nicht sinnvoll ist und die
  nicht im Artikel erwähnt wurden?

[HINT::Überlegungshilfen]

- **Wann Mocking sinnvoll ist**:
  - Externe Schnittstellen: Wenn echte Integrationen zu langsam, unzuverlässig oder schwer einzurichten sind.
  - Kritische Abhängigkeiten: Wenn andere Systemteile Fehlerquellen sind und den Fokus vom eigentlichen
  Code ablenken würden.
  - Wenn echte Implementierungen schwer (z. B. wegen Datenbanken oder Web-Services) oder unnötig
  aufwendig zu verwenden sind.
  - Um Tests gezielt nur auf einen Teil der Anwendung zu fokussieren und so „echte“ externe
  Seiteneffekte auszuschließen.
- **Wann Mocking weniger sinnvoll ist**:
  - Übermäßiges Mocken: Zu viel Einsatz von Mocks kann zu künstlichen, schwer wartbaren Tests führen.
  - Abgrenzung von Stubs und Mocks: Mocks werden nicht nur für Rückgabewerte genutzt, sondern auch,
  um Aufrufe (z. B. Methodenaufrufe) zu überprüfen.
  - Wenn die reale Implementierung effizient genug getestet werden kann (Mocking könnte hier mehr schaden als helfen).

[ENDHINT]

[ENDSECTION]

[SECTION::submission::program]

Reichen Sie für jede der Aufgaben [EREFR::1], [EREFR::2], [EREFR::3] und [EREFR::4]
Ihre Python-Dateien ein.

[ENDSECTION]

[INSTRUCTOR::Lösungsvorschläge]

- [EREFR::1] Wetter-Mocking

```Python
import pytest
from unittest.mock import patch
from m_pytest_mocking import get_weather_data

def test_get_weather_data():
  with patch('m_pytest_mocking.requests.get') as mock_get:
    # Beispielantwort für den Mock
    example_response = {"temperature": 22, "weather": "sunny"}
    mock_get.return_value.json.return_value = example_response
    
    # Aufruf der zu testenden Funktion
    response = get_weather_data("Berlin")
    
    # Überprüfung der Rückgabe
    assert response == example_response
    
    # Überprüfung, ob die richtige URL aufgerufen wurde
    mock_get.assert_called_with("https://example-weather-api.com/data?city=Berlin")
```

- [EREFR::2] Datei Mocking

```Python
import pytest
from unittest.mock import mock_open, patch
from m_pytest_mocking import read_log_file

def test_read_log_file():
  with patch('builtins.open', mock_open(read_data="ERROR at line 1\nOK at line 2\nERROR at line 3\n")) as mock_file:
    # Aufruf der zu testenden Funktion
    result = read_log_file('dummy_log_file.txt')
    
    # Überprüfung der Rückgabe
    assert result == 2
    
    # Überprüfung, ob die richtige Datei geöffnet wurde
    mock_file.assert_called_with('dummy_log_file.txt', 'r')
```

- [EREFR::3] Objekt Mocking

```Python
import pytest
from unittest.mock import patch
from m_pytest_mocking import process_user_data

def test_process_user_data():
  with patch('m_pytest_mocking.UserManager') as MockUserManager:
    mock_user_manager = MockUserManager.return_value
    mock_user_manager.get_user_data.return_value = {"name": "Mock User", "email": "mock@example.com"}
    
    # Aufruf der zu testenden Funktion
    result = process_user_data(123)
    
    # Überprüfung der Rückgabe
    assert result == {"name": "Mock User", "email": "mock@example.com"}
    
    # Überprüfung, ob die richtige Methode aufgerufen wurde
    mock_user_manager.get_user_data.assert_called_with(123)
```

- [EREFR::4] Datenbank Mocking

```Python
import pytest
from unittest.mock import MagicMock, patch
from m_pytest_mocking import get_user_age

def test_get_user_age():
    with patch('m_pytest_mocking.sqlite3') as mock_sqlite:
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = [25]
        mock_sqlite.connect.return_value.cursor.return_value = mock_cursor
        
        # Aufruf der zu testenden Funktion
        age = get_user_age(123)
        
        # Überprüfung der Rückgabe
        assert age == 25
        
        # Überprüfung, ob die richtige SQL-Abfrage ausgeführt wurde
        mock_cursor.execute.assert_called_with("SELECT age FROM users WHERE id = ?", (123,))
```

### Reflektionsteil

- [EREFR::5] Dummy

```Python
import pytest
from unittest.mock import MagicMock, patch
from m_pytest_mocking import send_email_to_users

def test_send_email_to_users_with_dummy():
    with patch('m_pytest_mocking.print') as mock_print:
        users = [
            {"email": "user1@example.com"},
            {"email": "user2@example.com"},
            {"email": "user3@example.com"}
        ]
        
        # Dummy-Implementierung des Email-Services
        class DummyEmailService:
            def send_email(self, email, subject, body):
                print(f"Sending email to {email}: {body}")
        
        email_service = DummyEmailService()
        
        # Aufruf der zu testenden Funktion
        send_email_to_users(users, email_service)
        
        # Überprüfung der Ausgaben
        mock_print.assert_any_call("Sending email to user1@example.com: Hello, welcome to our service!")
        mock_print.assert_any_call("Sending email to user2@example.com: Hello, welcome to our service!")
        mock_print.assert_any_call("Sending email to user3@example.com: Hello, welcome to our service!")
```

- [EREFR::6] FAKE

```Python
def test_send_email_to_users_with_fake():
    users = [{"email": "user1@example.com"}, {"email": "user2@example.com"}]
    class FakeEmailService:
        def __init__(self):
            self.sent_emails = []
        def send_email(self, email, subject, body):
            self.sent_emails.append((email, subject, body))
    email_service = FakeEmailService()
    send_email_to_users(users, email_service)
    assert len(email_service.sent_emails) == 2
    assert email_service.sent_emails[0] == ("user1@example.com", "Welcome!", "Hello, welcome to our service!")
    assert email_service.sent_emails[1] == ("user2@example.com", "Welcome!", "Hello, welcome to our service!")
```

- [EREFR::7] Stub

```Python
def test_send_email_to_users_with_stub():
    users = [{"email": "user1@example.com"}, {"email": "user2@example.com"}]
    class StubEmailService:
        def send_email(self, email, subject, body):
            return "Email sent"
    email_service = StubEmailService()
    send_email_to_users(users, email_service)
    # Keine Assertion notwendig, da Stub-Objekte vorgefertigte Antworten liefern
```

- [EREFR::8] Spy

```Python
def test_send_email_to_users_with_spy():
    users = [{"email": "user1@example.com"}, {"email": "user2@example.com"}]
    class SpyEmailService:
        def __init__(self):
            self.sent_emails = []
        def send_email(self, email, subject, body):
            self.sent_emails.append((email, subject, body))
    email_service = SpyEmailService()
    send_email_to_users(users, email_service)
    assert len(email_service.sent_emails) == 2
    assert email_service.sent_emails[0] == ("user1@example.com", "Welcome!", "Hello, welcome to our service!")
    assert email_service.sent_emails[1] == ("user2@example.com", "Welcome!", "Hello, welcome to our service!")
```

- [EREFR::9] Mock

```Python
def test_send_email_to_users_with_mock():
    users = [{"email": "user1@example.com"}, {"email": "user2@example.com"}]
    
    class TestEmailService:
        def __init__(self):
            self.sent_emails = []
        
        def send_email(self, email, subject, body):
            self.sent_emails.append((email, subject, body))
    
    email_service = TestEmailService()
    send_email_to_users(users, email_service)
    
    assert len(email_service.sent_emails) == 2
    assert email_service.sent_emails[0] == ("user1@example.com", "Welcome!", "Hello, welcome to our service!")
    assert email_service.sent_emails[1] == ("user2@example.com", "Welcome!", "Hello, welcome to our service!")

```

Das Ergebnis alle Tests sollte so enden:

```bash
(.venv) student@MBP test % pytest
=========================== test session starts ============================
platform darwin -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/student/propra-inf
collected 9 items                                                          

test_m_pytest_mocking.py .........                                           [100%]

============================ 9 passed in 0.05s =============================
(.venv) student@MBP test % 
```

- [EREFQ::1] Hier wäre es schön folgende Erkenntnisse heruaszulesen:

Wann einsetzen?
- Externe Schnittstellen: Immer dann, wenn echte Integrationen zu langsam, unzuverlässig oder schwer
  einzurichten sind.
- Kritische Abhängigkeiten: Wenn andere Systemteile Fehlerquellen sind und den Fokus vom eigentlichen
  Code ablenken würden.
- Wenn echte Implementierungen schwer (z. B. wegen Datenbanken oder Web-Services) oder unnötig
  aufwendig zu verwenden sind.
- Um Tests gezielt nur auf einen Teil der Anwendung zu fokussieren und so „echte“ externe
  Seiteneffekte auszuschließen.

Worauf achten?
- Übermäßiges Mocken: Zu viel Einsatz von Mocks kann zu künstlichen, schwer wartbaren Tests führen.
- Abgrenzung von Stubs und Mocks: Mocks werden nicht nur für Rückgabewerte genutzt, sondern auch, um
  Aufrufe (z. B. Methodenaufrufe) zu überprüfen.
- Wenn die reale Implementierung effizient genug getestet werden kann (Mocking könnte hier mehr
  schaden als helfen).

- [EREFQ::2] Die verschiedenen Testebenen sind ebenfalls wichtig: In Unit-Tests wird oft stärker auf
  Mocks zurückgegriffen, während sie bei End-to-End-Tests eher unangebracht sind, da hier die Anwendung
  in ihrer Gesamtheit aus Kundensicht geprüft wird. In Integrationstests werden die Abhängigkeiten
  zwischen den einzelnen Komponenten geprüft, weshalb hier sehr stark mit Bedacht gemockt werden sollte.

[ENDINSTRUCTOR]
