title: Fixtures mit dem Pytest Framework
stage: alpha
timevalue: 3
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

Nutzen Sie die Übersicht
[Pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
parallel zum Bearbeiten der Aufgaben.
Wir betrachten zu erst das Grundlegende.

#### Das Problem ohne Fixtures

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

#### Das Fixture-Konzept entdecken

Pytest löst die von Ihnen erkannten Probleme mit "Fixtures".

Mit Fixtures werden Sie im folgenden Wiederverwendbare Setup-Komponenten kennenlernen.
Sehen, dass ,man jedem Test `frische` Ressourcen mitgeben kann und in Tests nur wirklich deklarieren,
was sie brauchen. Aber auch, dass man damit die Setup-Logik von Test-Logik trennen kann.

Erstellen Sie die Datei `test_discovery.py` und implementieren Sie die folgenden Tests  
mit einer einfachen Klasse:

[NOTICE]
Hier wird der Begriff Mock verwendet. Das Thema Mocking wird ebenfalls in diesem Kapitel behandelt,
hat hier aber keine aktive Anwendung.
[ENDNOTICE]

```python
class MockUserService:
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
    service = MockUserService()
    result = service.register("alice", "alice@test.com", "password123") 
    assert result.success == True

def test_user_login():
    service = MockUserService()
    service.register("alice", "alice@test.com", "password123")  # Pre-condition
    result = service.login("alice", "password123")
    assert result.success == True
```

[EC] Führen Sie die Tests aus. Sie funktionieren, aber was stört Sie daran?

#### Erste Fixture: Das Setup Problem lösen

Pytest Fixtures lösen das Problem mit einem `Setup`.

```python
@pytest.fixture
def user_service():
    return MockUserService()

def test_user_registration(user_service):
    # Testinhalt
```

[ER] Ergänzen Sie Ihre `test_discovery.py`, um diese Fixture und modifizieren Sie beide Tests,  
um die Fixture zu nutzen.

[EQ] Was haben Sie gewonnen, was haben Sie verloren?

#### Das Isolationsproblem

Ein `Setup` löst aber nicht alle Probleme alleine.
Fügen Sie folgenden Test zur Datei `test_discovery.py` hinzu:

```python
def test_duplicate_registration(user_service):
    result1 = user_service.register("alice", "alice@test.com", "password123")
    assert result1.success == True
    
    result2 = user_service.register("alice", "other@test.com", "other_pass")
    assert result2.success == False
```

[EQ] Führen Sie alle Tests aus. Was passiert? Warum funktioniert das manchmal, manchmal nicht?

[EQ] Sie haben ein **Test-Isolationsproblem** entdeckt. Was ist die Ursache?  
Welche Lösungsansätze fallen Ihnen ein?

#### Fixture Scopes verstehen

Pytest bietet verschiedene "Scopes" für Fixtures:

- `function`: Neue Instanz für jeden Test (beste Isolation)
- `class`: Eine Instanz für alle Tests einer Test-Klasse
- `module`: Eine Instanz für alle Tests einer Datei  
- `session`: Eine Instanz für die gesamte Test-Session

Experimentieren Sie mit Scopes.
Fügen Sie folgende Fixtures zu Ihrer Datei hinzu:

```python
@pytest.fixture(scope="function")
def function_service():
    print("Erstelle function_service")
    return MockUserService()

@pytest.fixture(scope="module")  
def module_service():
    print("Erstelle module_service") 
    return MockUserService()

def test_function_scope_1(function_service):
    print("test_function_scope_1 läuft")
    assert True

def test_function_scope_2(function_service):
    print("test_function_scope_2 läuft")
    assert True
    
def test_module_scope_1(module_service):
    print("test_module_scope_1 läuft")
    assert True

def test_module_scope_2(module_service):
    print("test_module_scope_2 läuft")
    assert True
```

[EC] Führen Sie die Tests mit `-s` aus: `pytest -s test_discovery.py`

[EQ] Analysieren Sie die Ausgabe. Wann wird welche Fixture erstellt?  
Was bedeutet das für Ihr Isolationsproblem?

#### Setup und Teardown: Das yield-Pattern

Manche Tests brauchen nicht nur Setup, sondern auch Cleanup (Teardown).  
Beispiel: Datei erstellen → Test → Datei löschen. (Wenn sinnvoll, immer ein gites Vorgehen.)

Testen Sie das yield-Pattern in einer neuen beliebigen Datei.
Testen Sie es, indem Sie auch `assert False` in einen Test einfügen.

```python
import os

@pytest.fixture  
def temp_file():
    filename = "test_temp.txt"
    print(f"Setup: Erstelle {filename}")
    with open(filename, "w") as f:
        f.write("Testdaten")
    
    yield filename
    
    print(f"Teardown: Lösche {filename}")
    os.remove(filename)

def test_file_exists(temp_file):
    assert os.path.exists(temp_file)
    with open(temp_file) as f:
        assert f.read() == "Testdaten"
```

[EQ] Was passiert, wenn ein Test einen Fehler wirft? Wird Teardown trotzdem ausgeführt?
[ER] Ergänzen Sie passende Testfälle zu `test_yield_success` und `test_yield_error`.  

#### Fixtures teilen: conftest.py

Sie haben mehrere Test-Dateien, die alle `ähnliche` Fixtures brauchen.  
Jetzt schauen wir uns an, wie Pytest dieses Problem lösen kann?

Erstellen Sie eine Datei `conftest.py` mit geteilten Fixtures:

```python
import pytest

class MockUserService:
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
    return MockUserService()
```

Erstellen Sie eine zweite Testdatei `test_sharing.py`:

```python
def test_in_other_file(fresh_user_service):
    result = fresh_user_service.register("bob", "bob@test.com", "pass")
    assert result.success == True
```

[EC] Können die Tests in `test_sharing.py` die Fixtures aus `conftest.py` nutzen,  
obwohl sie nicht importiert werden?

Folgendes habne Sie gerade beobachtet:

1. **Automatisches Laden:** Pytest lädt automatisch alle conftest.py Dateien im aktuellen Verzeichnis und allen übergeordneten Verzeichnissen
2. **Fixture-Discovery:** Pytest scannt diese conftest.py Dateien nach @pytest.fixture Dekoratoren und registriert sie global
3. **Namensauflösung:** Wenn ein Test einen Parameter fresh_user_service hat, sucht pytest automatisch nach einer gleichnamigen Fixture in:

- Der gleichen Datei
- conftest.py im gleichen Verzeichnis
- conftest.py in übergeordneten Verzeichnissen
- Eingebauten pytest Fixtures

Kein Import nötig: Das ist ein spezielles Feature von pytest - normale Python-Import-Regeln gelten hier nicht

#### Eingebaute Fixtures verstehen

Pytest bringt viele eingebaute Fixtures mit. Hier sind drei wichtige:

- `tmp_path`: Temporäre Dateien/Verzeichnisse für File-IO-Tests
- `capsys`: Output-Testing, Debug-Ausgaben validieren
- `monkeypatch`: Zeit, Umgebungsvariablen, externe APIs mocken

[EQ] In welchen Testszenarien würden Sie sie einsetzen?

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

#### Reflexion: Wann und Warum Fixtures?

Sie haben verschiedene Fixture-Konzepte kennengelernt. Reflektieren Sie:

[EQ] **Fixture-Philosophie:** Fixtures verändern die Art, wie Sie über Tests denken - weg von "Setup-Code schreiben" hin zu "Dependencies deklarieren". Wie beeinflusst diese Denkweise Ihren Ansatz beim Schreiben neuer Tests? Welche anderen Programmierkonzepte folgen einem ähnlichen "deklarativen" Ansatz?

[EQ] **Transfer und Grenzen:** Sie haben Fixtures in einem einfachen Mock-Szenario kennengelernt. Überlegen Sie sich ein konkretes Projekt aus Ihrem eigenen Erfahrungsbereich: Welche Setup-Situationen hätten Sie dort? Wo würden Fixtures helfen, wo könnten sie möglicherweise "zu viel des Guten" sein? Begründen Sie Ihre Einschätzung.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
