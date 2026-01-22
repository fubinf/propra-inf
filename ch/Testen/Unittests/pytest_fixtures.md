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
Fixtures ("Halterungen" für den Test -- ein seltsamer Ausdruck) sind ein zentrales Konzept in Pytest, 
das es ermöglicht, wiederverwendbaren Code zur Vor- und Nachbereitung (Setup und Teardown) von Tests 
bereitzustellen. 
Sie sind insbesondere geeignet, um Testdaten bereitzustellen.

[ENDSECTION]
[SECTION::instructions::detailed]

Nutzen Sie die Übersicht
[Pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
parallel zum Bearbeiten der Aufgaben.
Wir betrachten zu erst das Grundlegende.

#### Das Problem ohne Fixtures

[EQ] Betrachten Sie folgenden Testcode für eine Webanwendung:

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
    # Setup (identisch!)
    db = Database("test.db")
    db.connect() 
    db.create_tables()
    user_service = UserService(db)
    user_service.register("alice", "alice@test.com", "password123")
    
    # Test
    result = user_service.login("alice", "password123")
    assert result.success == True
    
    # Cleanup (identisch!)
    db.delete_all_users()
    db.disconnect()
    os.remove("test.db")
```

[EQ] Welche Probleme erkennen Sie in diesem Code? Notieren Sie mindestens 3 Probleme.

#### Das Fixture-Konzept entdecken

Pytest löst das obige Problem mit "Fixtures".

[EQ] Was vermuten Sie: Was ist der Kerngedanke hinter Fixtures? Was sollen sie erreichen?

[ER] Erstellen Sie die Datei `test_discovery.py` und implementieren Sie die folgenden Tests  
mit einer einfachen Mock-Klasse:

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
    # TODO: Viel Setup-Code hier
    service = MockUserService()
    result = service.register("alice", "alice@test.com", "password123") 
    assert result.success == True

def test_user_login():
    # TODO: Noch mehr Setup-Code hier - mit Duplizierung!
    service = MockUserService()
    service.register("alice", "alice@test.com", "password123")  # Pre-condition
    result = service.login("alice", "password123")
    assert result.success == True
```

[EC] Führen Sie die Tests aus. Sie funktionieren, aber was stört Sie daran?

#### Erste Fixture: Das Setup Problem lösen

[EQ] Pytest Fixtures lösen das Setup-Problem. Was erwarten Sie von der folgenden Syntax?

```python
@pytest.fixture
def user_service():
    return MockUserService()

def test_user_registration(user_service):
    result = user_service.register("alice", "alice@test.com", "password123")
    assert result.success == True
```

[ER] Ergänzen Sie Ihre `test_discovery.py` um diese Fixture und modifizieren Sie beide Tests,  
um die Fixture zu nutzen.

[EQ] Führen Sie die Tests aus. Was passiert? Was haben Sie gewonnen, was haben Sie verloren?

#### Das Isolationsproblem

[EQ] Fügen Sie einen dritten Test hinzu:

```python
def test_duplicate_registration(user_service):
    # Erst erfolgreich registrieren
    result1 = user_service.register("alice", "alice@test.com", "password123")
    assert result1.success == True
    
    # Zweite Registrierung desselben Users sollte fehlschlagen
    result2 = user_service.register("alice", "other@test.com", "other_pass")
    assert result2.success == False
```

[EQ] Führen Sie alle Tests aus. Was passiert? Warum funktioniert das manchmal, manchmal nicht?

[EQ] Sie haben ein **Test-Isolationsproblem** entdeckt. Was ist die Ursache?  
Welche Lösungsansätze fallen Ihnen ein?

#### Fixture Scopes verstehen


Pytest bietet verschiedene "Scopes" für Fixtures:

- `function` (default)
- `class` 
- `module`
- `session`

[EQ] Was vermuten Sie: Was bedeuten diese Scopes? Wann würden Sie welchen verwenden?

[ER] Experimentieren Sie mit Scopes. Fügen Sie folgende Fixtures zu Ihrer Datei hinzu:

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
Beispiel: Datei erstellen → Test → Datei löschen.

[EQ] Was erwarten Sie von diesem Code?

```python
@pytest.fixture
def temp_file():
    filename = "test_temp.txt"
    with open(filename, "w") as f:
        f.write("Testdaten")
    
    yield filename  # Hier passiert der Test
    
    os.remove(filename)  # Cleanup nach dem Test
```

[ER] Testen Sie das yield-Pattern:

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
Testen Sie es, indem Sie `assert False` in einen Test einfügen.

#### Fixtures teilen: conftest.py

[EQ] Sie haben mehrere Test-Dateien, die alle ähnliche Fixtures brauchen.  
Wie könnte Pytest dieses Problem lösen?

[ER] Erstellen Sie eine Datei `conftest.py` mit geteilten Fixtures:

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

[ER] Erstellen Sie eine zweite Testdatei `test_sharing.py`:

```python
def test_in_other_file(fresh_user_service):
    result = fresh_user_service.register("bob", "bob@test.com", "pass")
    assert result.success == True
```

[EQ] Was vermuten Sie: Können die Tests in `test_sharing.py` die Fixtures aus `conftest.py` nutzen,  
obwohl sie nicht importiert werden?

[EC] Testen Sie es. Was beobachten Sie?

#### Eingebaute Fixtures verstehen

[EQ] Pytest bringt viele eingebaute Fixtures mit. Hier sind drei wichtige:

- `tmp_path`: Temporäres Verzeichnis
- `capsys`: Output-Capturing  
- `monkeypatch`: Mocking/Patching

[EQ] Was vermuten Sie: Wozu sind diese gut? In welchen Testszenarien würden Sie sie einsetzen?

[ER] Experimentieren Sie mit eingebauten Fixtures:

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

[EQ] Welche realen Testprobleme lösen diese Fixtures? Fallen Ihnen Beispiele aus Ihren  
eigenen Projekten ein?

#### Reflexion: Wann und Warum Fixtures?

[EQ] Sie haben verschiedene Fixture-Konzepte kennengelernt. Reflektieren Sie:

1. **DRY-Prinzip**: Wie helfen Fixtures, Code-Duplizierung zu vermeiden?

2. **Test-Isolation**: Welche Scope sollten Sie standardmäßig verwenden und warum?

3. **Setup/Teardown**: Wann brauchen Sie yield? Nennen Sie 3 konkrete Beispiele.

4. **Eingebaute vs. eigene Fixtures**: Wann verwenden Sie `tmp_path`, wann schreiben Sie eigene?

[EQ] **Designentscheidung**: Sie entwickeln Tests für eine E-Commerce-API.  
Sie brauchen: Database-Setup, Test-Produkte, Test-User, Payment-Mock.

Skizzieren Sie eine Fixture-Architektur: Welche Fixtures erstellen Sie?  
Welche Scopes verwenden Sie? Welche Dependencies gibt es?

[EQ] **Anti-Pattern**: Was macht folgenden Code problematisch?

```python
@pytest.fixture(scope="session")
def user_database():
    db = Database()
    db.add_user("alice", "alice@test.com") 
    return db

def test_alice_login(user_database):
    result = user_database.login("alice", "password")
    assert result.success

def test_alice_deletion(user_database):
    user_database.delete_user("alice")
    assert "alice" not in user_database.users
```

Was würde passieren, wenn diese Tests in unterschiedlicher Reihenfolge laufen?

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
