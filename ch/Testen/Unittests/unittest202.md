title: Unittest in Python - Mocking Anwendung
stage: beta
timevalue: 4.0
difficulty: 4
assumes: m_unittest, mocking
---

[SECTION::goal::idea]

- Ich bin in der Lage, grundlegende Unittests in verschiedenen Anwendungsbereichen zu mocken.

[ENDSECTION]
[SECTION::background::default]

Hier erhalten Sie die Gelegenheit Ihre Mocking Erfahrung auszuspielen. Dabei kommen API Mocks,
Dateienmocks, SQL Mocks und Klassenmocks in den Vordergrund. Solche Mocks sind zeimlich oft anzufinden
und daher als eine wichtige Grundlage im Umgang mit Unittests zu sehen.

[ENDSECTION]
[SECTION::instructions::loose]

Zu jeder Aufgabe wird es eine kleine Funktion geben, die in einer bestimmten Datei abgelegt ist.
Erstellen Sie diese Datei um anschließend damit zu arbeiten.
Ihre Aufgabe ist es, die externen Abhängigkeiten und Seiteneffekte zu Ihren Tests zu isolieren,
damit Sie sich auf das Testen der eigentlichen Logik einer Funktionen und Methoden konzentrieren
können.

- [ER] Schreiben Sie einen Unittest für eine Funktion *get_weather_data()*, die sich in der Datei
  *weather.py* befindet, die eine externe API aufruft. Mocken Sie den API-Aufruf, um sicherzustellen,
  dass keine echten Netzwerkanfragen während des Tests gemacht werden.

```Python
import requests

def get_weather_data(city):
    url = f"https://example-weather-api.com/data?city={city}"
    response = requests.get(url)
    return response.json()
```

- [ER] Schreiben Sie einen Unittest für eine Funktion *read_log_file()* aus der Datei *my_logs.py*,
  die eine Datei liest und verarbeitet. Mocken Sie die Dateioperationen, um zu verhindern, dass
  während der Tests echte Dateien gelesen oder geschrieben werden.

```Python
def read_log_file(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                count += 1
    return count
```

- [ER] Schreiben Sie einen Unittest für eine Funktion *process_user_data()* in der Datei
  *user_manager.py*, die von einer Klasse in Ihrem Projekt abhängt. Mocken Sie die Abhängigkeit,
  um isolierte Tests durchzuführen.

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

- [ER] Schreiben Sie eine Funktion *get_user_age()* aus der Datei *my_db_module.py*, die das Alter
  eines Benutzers aus einer SQL-Datenbank abruft. Schreiben Sie anschließend Unittests für diese
  Funktion, wobei die Datenbankverbindung und -abfragen gemockt werden, um keine echte Datenbank zu
  verwenden.

```Python
import sqlite3

def get_user_age(user_id):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    # Abfrage des Nutzers mit ID Bezug
    cursor.execute("SELECT age FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
```

[ENDSECTION]

[SECTION::submission::program]

Reichen Sie für jede der Aufgaben [EREFR::1], [EREFR::2], [EREFR::3] und [EREFR::4]
Ihre Python-Dateien ein.

[ENDSECTION]

[INSTRUCTOR::Lösungsvorschläge]
Lösungen könnten so aussehen:

- [EREFR::1] Wetter-Mocking

```Python
import unittest
from unittest.mock import patch
from weather import get_weather_data

class TestWeatherAPI(unittest.TestCase):
    # Infos zum Decorator Patch:
    # Isolation von Externen Abhängigkeiten, Automatisierung des Cleanups, Simulieren von Verhalten
    @patch('weather.requests.get')
    def test_get_weather_data(self, mock_get):
        # Ein beispielhaftes Response-Objekt, kann beliebig sein
        # hier soll jedoch erkennbar sein, dass Daten zurück gegeben werden
        example_response = {
            "temperature": 22,
            "weather": "sunny"
        }

        # Mock-Konfiguration, um das Response-Objekt zurückzugeben
        mock_get.return_value.json.return_value = example_response

        # Führe die zu testende Funktion aus
        response = get_weather_data("Berlin")

        # Überprüfe, ob die Funktion das erwartete Ergebnis liefert
        self.assertEqual(response, example_response)

        # Stelle sicher, dass `requests.get` mit der richtigen URL aufgerufen wurde
        mock_get.assert_called_with("https://example-weather-api.com/data?city=Berlin")

if __name__ == '__main__':
    unittest.main()
```

- [EREFR::2] Datei Mocking

```Python
import unittest
from unittest.mock import mock_open, patch
from my_logs import read_log_file 

class TestReadLogFile(unittest.TestCase):

    # Infos zum Dekorator patch:
    # - 'builtins.open': Dies gibt an, dass die eingebaute open-Funktion, die normalerweise für Dateioperationen verwendet wird, 
    # gemockt werden soll. builtins ist das Modul, das die eingebauten Funktionen in Python enthält.
    # - new_callable=mock_open: Der Parameter new_callable gibt an, welche Klasse oder Funktion verwendet werden soll, um das 
    # Mock-Objekt zu erstellen. mock_open ist eine Hilfsfunktion aus dem unittest.mock-Modul, die speziell dafür entwickelt wurde, 
    # die open-Funktion zu mocken. Sie erstellt ein Mock-Objekt, das sich ähnlich wie ein Dateiobjekt verhält.
    # - read_data="...": Der Parameter read_data wird in mock_open verwendet, um den Inhalt der gemockten Datei festzulegen. 
    # In diesem Fall simulieren wir eine Datei mit drei Zeilen Text. Jedes Vorkommen von \n repräsentiert einen Zeilenumbruch, 
    # genau wie in einer echten Datei.
    @patch('builtins.open', new_callable=mock_open, read_data="ERROR at line 1\nOK at line 2\nERROR at line 3\n")
    def test_read_log_file(self, mock_file):
        # Teste, dass die Funktion die korrekte Anzahl von ERROR-Zeilen zählt
        file_path = 'dummy_log_file.txt'
        result = read_log_file(file_path)
        self.assertEqual(result, 2)

        # Stelle sicher, dass die Datei wie erwartet geöffnet wurde
        mock_file.assert_called_with(file_path, 'r')

if __name__ == '__main__':
    unittest.main()

```

- [EREFR::3] Objekt Mocking

```Python
import unittest
from unittest.mock import patch
from user_manager.py import UserManager

class TestProcessUserData(unittest.TestCase):
    # Infos zum Decorator Patch:
    # - String 'user_manager.py.UserManager' gibt den Pfad, unter dem das zu mockende Objekt im Test gefunden werden kann.
    @patch('user_manager.py.UserManager')
    def test_process_user_data(self, mock_user_manager):
        # Konfigurieren Sie den Mock, um eine vordefinierte Antwort zurückzugeben
        mock_user_manager.return_value.get_user_data.return_value = {"name": "Mock User", "email": "mock@example.com"}

        user_id = 123
        result = process_user_data(user_id)

        # Überprüfen Sie, ob das Ergebnis wie erwartet ist
        self.assertEqual(result, {"name": "Mock User", "email": "mock@example.com"})

        # Stellen Sie sicher, dass get_user_data mit dem richtigen Argument aufgerufen wurde
        mock_user_manager.return_value.get_user_data.assert_called_with(user_id)

if __name__ == '__main__':
    unittest.main()
```

- [EREFR::4] Datenbank Mocking

```Python
import unittest
from unittest.mock import MagicMock, patch
from my_db_module import get_user_age

class TestGetUserAge(unittest.TestCase):

    @patch('my_db_module.sqlite3')
    def test_get_user_age(self, mock_sqlite):
        # Erstellen eines Mock-Cursors
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = [25]

        # Mock der connect-Methode, um einen Mock-Cursor zurückzugeben
        mock_sqlite.connect.return_value.cursor.return_value = mock_cursor

        age = get_user_age(123)
        self.assertEqual(age, 25)

        # Überprüfen, ob die richtigen SQL-Befehle ausgeführt wurden
        mock_cursor.execute.assert_called_with("SELECT age FROM users WHERE id = ?", (123,))

if __name__ == '__main__':
    unittest.main()
```

[ENDINSTRUCTOR]
