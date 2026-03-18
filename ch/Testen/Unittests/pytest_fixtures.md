title: Fixtures mit dem Pytest-Framework
stage: alpha
timevalue: 2.0
difficulty: 2
assumes: m_pytest
---

[SECTION::goal::idea]
Ich kann Fixtures mit dem Pytest Framework anwenden.
[ENDSECTION]


[SECTION::background::default]
Oftmals benötigt ein Test, dass bestimmte Voraussetzungen hergestellt werden.
Fixtures sind ein zentrales Konzept in Pytest, das es ermöglicht,
wiederverwendbaren Code zur Vor- und Nachbereitung (Setup und Teardown) von Tests bereitzustellen.
Somit sind sie insbesondere dafür geeignet, um Testdaten bereitzustellen.
[ENDSECTION]


[SECTION::instructions::detailed]
Nutzen Sie die folgende Übersicht parallel zum Bearbeiten der Aufgaben:

[Pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

Wir betrachten zuerst das Grundlegende.

### Das Problem ohne Fixtures
<!-- time estimate: 5 min -->

Betrachten Sie folgenden Testcode für eine Webanwendung:

```python
def test_user_registration():
    # Setup
    db = Database("test.db")
    db.connect()
    db.create_tables()
    user_service = UserService(db)
    
    # Test
    result = user_service.register("alice", "alice@test.com", "password123")
    assert result.success == True
    
    # Cleanup
    db.delete_all_users()
    db.disconnect()
    os.remove("test.db")

def test_user_login():
    # Setup
    db = Database("test.db")
    db.connect() 
    db.create_tables()
    user_service = UserService(db)
    user_service.register("alice", "alice@test.com", "password123") 
    
    # Test
    result = user_service.login("alice", "password123")
    assert result.success == True
    
    # Cleanup
    db.delete_all_users()
    db.disconnect()
    os.remove("test.db")
```

[EQ] Welche Probleme erkennen Sie in diesem Code? Notieren Sie mindestens 3 Probleme.


### Das Fixture-Konzept entdecken
<!-- time estimate: 10 min -->

Pytest löst die Schwächen des obigen Codes mit "Fixtures".

Fixtures sind wiederverwendbare Setup-Komponenten.
Sie werden sehen, wie man damit jedem Test "frische" Ressourcen so mitgeben kann, 
dass Tests nur deklarieren müssen, was sie brauchen; es ist kein einziges zusätzliches Statement nötig. 
Zugleich kann man damit die Setup-Logik übersichtlich von der Test-Logik trennen.

Erstellen Sie die Datei `test_discovery.py` und implementieren Sie die folgenden Tests  
mit einer einfachen Klasse:

```python
class PseudoUserservice:
    def __init__(self):
        self.users = {}
    
    def register(self, username, email, password):
        if username in self.users:
            return type('Result', (), {'success': False})()
        self.users[username] = {'email': email, 'password': password}
        return type('Result', (), {'success': True})()
    
    def login(self, username, password):
        user = self.users.get(username)
        if user and user['password'] == password:
            return type('Result', (), {'success': True})()
        return type('Result', (), {'success': False})()

def test_user_registration():
    service = PseudoUserservice()
    result = service.register("alice", "alice@test.com", "password123") 
    assert result.success == True

def test_user_login():
    service = PseudoUserservice()
    service.register("alice", "alice@test.com", "password123")  # Pre-condition
    result = service.login("alice", "password123")
    assert result.success == True
```


#### Setup deklarativ machen
<!-- time estimate: 15 min -->

Pytest Fixtures lösen das, indem man Setup-Code einmal als Fixture definiert und ihn in beliebig vielen Tests wiederverwendet.

```python
@pytest.fixture
def user_service():
    return PseudoUserservice()

def test_user_registration(user_service):
    ...
```

[ER] Ergänzen Sie Ihre `test_discovery.py` um diese Fixture, und modifizieren Sie beide Tests,
um die Fixture zu nutzen.

Ein Test kann auch mehrere Fixtures gleichzeitig verwenden – er listet sie einfach als mehrere
Parameter auf.
Suchen Sie in der oben verlinkten Pytest-Übersicht nach dem Abschnitt
„A test/fixture can request more than one fixture at a time" und lesen Sie ihn.

Zum Beispiel:

```python
@pytest.fixture
def credentials():
    return {"email": "alice@test.com", "password": "secret"}

def test_login(user_service, credentials):
    user_service.register("alice", credentials["email"], credentials["password"])
    result = user_service.login("alice", credentials["password"])
    assert result.success == True
```

[EQ] Stellen Sie sich eine Testdatei mit Dutzenden Tests vor, die verschiedene Kombinationen
von Fixtures verwenden.
Welchen Vorteil hat es, wenn alle benötigten Fixtures als Parameter in der Signatur stehen?


#### Fixture Scopes: wann welcher?
<!-- time estimate: 25 min -->

Manche Fixtures sind aufwendig: eine Datenbankverbindung aufbauen, Testdaten laden oder
einen Server starten kann Sekunden dauern.
Mit dem Standard-Scope `"function"` wird das Setup für jeden einzelnen Test wiederholt.

Simulieren Sie das mit `time.sleep()`:

```python
import time

@pytest.fixture
def slow_service():
    time.sleep(1)  # Simuliert langsames Setup (z.B. DB-Verbindung aufbauen)
    return PseudoUserservice()

def test_slow_1(slow_service):
    slow_service.register("alice", "alice@test.com", "secret")
    assert True

def test_slow_2(slow_service):
    slow_service.register("bob", "bob@test.com", "secret")
    assert True

def test_slow_3(slow_service):
    assert True
```

[EC] Fügen Sie diesen Code zu `test_discovery.py` hinzu und messen Sie die Laufzeit:
`pytest -v test_discovery.py`

[EQ] Wie viele Sekunden dauert die Testsuite insgesamt?
Was wäre bei 100 Tests, die diese Fixture verwenden?

Pytest bietet verschiedene Scopes für Fixtures:

- `function`: Neue Instanz für jeden Test (Standard, beste Isolation)
- `class`: Eine Instanz für alle Tests einer Test-Klasse
- `module`: Eine Instanz für alle Tests einer Datei
- `session`: Eine Instanz für die gesamte Test-Session

Ändern Sie nun den Scope auf `"module"`:

```python
@pytest.fixture(scope="module")
def slow_service():
    time.sleep(1)
    return PseudoUserservice()
```

[EC] Führen Sie die Tests erneut aus: `pytest -v test_discovery.py`

[EQ] Wie verändert sich die Laufzeit, und warum?
Was müssen Sie beachten, wenn mehrere Tests dieselbe Instanz teilen?

[HINT::Ich verstehe nicht, was dabei schiefgehen kann]
Im `function`-Scope bekommt jeder Test eine frische Instanz – Zustandsänderungen eines Tests
sind für andere Tests unsichtbar.
Im `module`-Scope teilen sich alle Tests dieselbe Instanz: Wenn ein Test Nutzerdaten speichert
oder andere Zustandsänderungen vornimmt, sehen das alle nachfolgenden Tests ebenfalls.
Tests müssen deshalb so geschrieben sein, dass sie nicht auf Zustand angewiesen sind,
den ein anderer Test hinterlassen hat.
[ENDHINT]

Wenn Sie fertig sind, entfernen Sie `slow_service` und die drei zugehörigen Tests wieder.

#### Setup und Teardown: Das Cleanup-Problem
<!-- time estimate: 30 min -->

Manche Tests erstellen Dateien, Datenbank-Einträge oder andere Ressourcen.  
Was passiert, wenn diese nicht aufgeräumt werden?

Betrachten Sie dieses problematische Beispiel:

```python
import os
import pytest

@pytest.fixture(scope="module")
def temp_file():
    filename = "debug_output.txt"
    print(f"Setup: Erstelle {filename}")
    with open(filename, "w") as f:
        f.write("Test war hier!")
    return filename

def test_creates_temp_file(temp_file):
    assert os.path.exists(temp_file)
    with open(temp_file) as f:
        assert "Test war hier" in f.read()
    
    with open(temp_file, "a") as f:
        f.write(" - Test 1 war hier!")

def test_another_temp_file(temp_file):
    with open(temp_file) as f:
        content = f.read()
    print(f"Dateiinhalt: {content}")
    assert content == "Test war hier!"
```

[EQ] Führen Sie den Code aus. Was ist hier das Problem?

Wir könnten den Scope ändern, aber nehmen wir mal an, dass wir ihn für unsere Testsammlung an dieser
Stelle benötigen.
Dann haben wir noch eine andere - gute - Möglichkeit: Aufräumen.

Hier ist eine Möglichkeit, um am Ende der Testdatei aufzuräumen.
Sie verwenden cleanup(), um die Datei zu löschen.

```python
@pytest.fixture(scope="module")
def temp_file(request):  # <- request muss Parameter sein!
    filename = "debug_output.txt"
    print(f"Setup: Erstelle {filename}")
    with open(filename, "w") as f:
        f.write("Test war hier!")
    
    def cleanup():
        print(f"Teardown: Lösche {filename}")
        if os.path.exists(filename):
            os.remove(filename)
    
    request.addfinalizer(cleanup)
    return filename
```

Jedoch benötigen wir das Zurücksetzen der Datei *zwischen* den Tests, nicht erst am Ende.

```python
@pytest.fixture(scope="module")
def temp_file_manager(request):
    filename = "debug_output.txt"
    original_content = "Test war hier!"
    
    def reset_file():
        print(f"Reset: Setze {filename} zurück")
        with open(filename, "w") as f:
            f.write(original_content)
    
    def cleanup():
        print(f"Teardown: Lösche {filename}")
        if os.path.exists(filename):
            os.remove(filename)
    
    # Erste Erstellung
    reset_file()
    request.addfinalizer(cleanup)
    
    class FileManager:
        def __init__(self):
            self.filename = filename
            self.original_content = original_content
        
        def reset(self):
            reset_file()
    
    return FileManager()

def test_creates_temp_file(temp_file_manager):
    assert os.path.exists(temp_file_manager.filename)
    with open(temp_file_manager.filename) as f:
        assert "Test war hier" in f.read()
    
    with open(temp_file_manager.filename, "a") as f:
        f.write(" - Test 1 war hier!")

def test_another_temp_file(temp_file_manager):
    # Datei vor diesem Test zurücksetzen
    temp_file_manager.reset()
    
    with open(temp_file_manager.filename) as f:
        content = f.read()
    print(f"Dateiinhalt: {content}")
    assert content == "Test war hier!"  # Funktioniert jetzt!
```

[ER] Implementieren Sie die `temp_file_manager`-Fixture aus dem Codebeispiel oben in Ihrer
`test_discovery.py` und ersetzen Sie damit `temp_file` in beiden Tests.
Stellen Sie sicher, dass `test_another_temp_file` besteht – unabhängig davon,
ob `test_creates_temp_file` vorher gelaufen ist.

[EQ] Was passiert, wenn ein Test einen Fehler wirft? Wird Cleanup trotzdem ausgeführt?

Das Ganze kann man auch mit Hilfe einer Hilfsklasse umsetzen, was es übersichtlicher gestaltet.

```python
class TempFileManager:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, "w") as f:
            f.write("Standardinhalt")
    
    def write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)
    
    def read(self):
        with open(self.filename) as f:
            return f.read()
    
    def cleanup(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

@pytest.fixture
def file_manager(request):
    manager = TempFileManager("managed_file.txt")
    request.addfinalizer(manager.cleanup)
    return manager

def test_creates_temp_file(file_manager):
    file_manager.write("Test content")
    assert file_manager.read() == "Test content"

def test_another_temp_file(file_manager):
    file_manager.write("Test content")
    assert file_manager.read() == "Test content"
```

Hier stellen wir in unserer Fixture sicher, dass `request.addfinalizer(manager.cleanup)`
nach Ablauf des Fixture-Scopes ausgeführt wird – also nach dem letzten Test, der die Fixture nutzt.

#### Fixtures teilen: conftest.py
<!-- time estimate: 15 min -->

Sie haben mehrere Test-Dateien, die alle ähnliche Fixtures brauchen.
Jetzt schauen wir uns an, wie Pytest dieses Problem lösen kann.

Erstellen Sie eine Datei `conftest.py` mit geteilten Fixtures:

```python
import pytest

class PseudoUserservice:
    def __init__(self):
        self.users = {}
        print(f"Neuer UserService erstellt (ID: {id(self)})")
    
    def register(self, username, email, password):
        if username in self.users:
            return type('Result', (), {'success': False})()
        self.users[username] = {'email': email, 'password': password}
        return type('Result', (), {'success': True})()

@pytest.fixture
def fresh_user_service():
    """Frischer UserService für jeden Test."""
    return PseudoUserservice()
```

Erstellen Sie eine zweite Testdatei `test_sharing.py`:

```python
def test_in_other_file(fresh_user_service):
    result = fresh_user_service.register("bob", "bob@test.com", "pass")
    assert result.success == True
```

Wenn Sie den Test ausführen, sehen Sie, dass es magischerweise funktioniert.
Dabei haben wir `conftest.py` doch gar nicht in `test_sharing.py` importiert.

Folgendes haben Sie gerade beobachtet:

1. **Automatisches Laden:** Pytest lädt automatisch alle `conftest.py` Dateien im aktuellen
   Verzeichnis und allen übergeordneten Verzeichnissen
2. **Fixture-Discovery:** Pytest scannt diese conftest.py Dateien nach @pytest.fixture
   Dekoratoren und registriert sie global
3. **Namensauflösung:** Wenn ein Test einen Parameter fresh_user_service hat, sucht pytest
   automatisch nach einer gleichnamigen Fixture in:

   - Der gleichen Datei
   - conftest.py im gleichen Verzeichnis
   - conftest.py in übergeordneten Verzeichnissen
   - Eingebauten pytest Fixtures

Kein Import nötig: Das ist ein spezielles Feature von pytest - normale Python-Import-Regeln
gelten hier nicht.
Und warum nehmen wir nicht einfach den Import?

Vorweg, natürlich geht auch das!
Sie könnten es wie folgt umsetzen:

```python
from conftest import fresh_user_service

def test_with_explicit_import(fresh_user_service):
    result = fresh_user_service.register("charlie", "charlie@test.com", "pass")
    assert result.success == True
```

[EQ] Ganz intuitiv: Welche Vor- und Nachteile sehen Sie in den beiden Varianten?

#### Eingebaute Fixtures verstehen
<!-- time estimate: 15 min -->

Pytest bringt viele eingebaute Fixtures mit. Hier sind drei wichtige:

- `tmp_path`: Temporäre Dateien/Verzeichnisse für File-IO-Tests
- `capsys`: Output-Testing, Debug-Ausgaben validieren
- `monkeypatch`: Funktionen, Umgebungsvariablen und Attribute durch Attrappen ersetzen

Lesen Sie nach, was jede davon tut:

[Built-in fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html)

[EQ] Skizzieren Sie für jede der drei ein Testszenario, in dem Ihnen der Einsatz sinnvoll erscheint.

Experimentieren Sie mit eingebauten Fixtures:

```python
import sys

def test_tmp_path_experiment(tmp_path):
    # tmp_path ist ein pathlib.Path zu einem temporären Verzeichnis
    test_file = tmp_path / "experiment.txt"
    test_file.write_text("Das ist ein Test")
    
    assert test_file.read_text() == "Das ist ein Test"
    print(f"Temporäres Verzeichnis: {tmp_path}")

def test_capsys_experiment(capsys):
    print("Das ist eine Debug-Ausgabe")
    print("Und noch eine Zeile", file=sys.stderr)
    
    captured = capsys.readouterr() 
    assert "Debug-Ausgabe" in captured.out
    assert "noch eine Zeile" in captured.err
```

[EC] Fügen Sie beide Tests zu `test_discovery.py` hinzu und führen Sie sie aus:
`pytest -v test_discovery.py`

#### Reflexion: Wann und Warum Fixtures?
<!-- time estimate: 5 min -->

Sie haben verschiedene Fixture-Konzepte kennengelernt. Reflektieren Sie:

[EQ] Fixtures verändern die Art, wie Sie über Tests nachdenken:
weg von "Setup-Code schreiben" hin zu "Dependencies deklarieren".
Die eigentliche Testlogik wird damit sehr viel besser erkennbar.
Welcher Nachteil steht dem gegenüber?
[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
