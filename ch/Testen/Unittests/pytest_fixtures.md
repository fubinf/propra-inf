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

[EQ] Führen Sie die Tests aus. Sie funktionieren, aber was stört Sie daran?

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

#### Das Isolationsproblem demonstrieren

Jetzt demonstrieren wir bewusst ein Isolationsproblem.

```python
def test_user_registration(user_service):
    result = user_service.register("alice", "alice@test.com", "password123") 
    assert result.success == True

def test_user_login(user_service):
    user_service.register("alice", "alice@test.com", "password123")
    result = user_service.login("alice", "password123")
    assert result.success == True

def test_expects_alice_exists(user_service):
    assert "alice" in user_service.users, "Alice sollte bereits registriert sein!"
    result = user_service.login("alice", "password123")
    assert result.success == True
```

Führen Sie die Tests mit `-v` aus: `pytest -v test_discovery.py`.

Es sollte nicht fehlerfrei durchlaufen.

Sie haben ein **Test-Isolationsproblem** entdeckt.

[EQ] Beschreiben Sie in eigenen Worten, was das Problem ist.

[HINT::MoveIt]
Um einen besseren Eindruck zu bekommen, verändern Sie doch einfach einmal die Reihenfolge der Tests.
[ENDHINT]

Ersetzen Sie jetzt die Fixture durch folgenden Teil:

```python
@pytest.fixture(scope="module")
def user_service():
    return MockUserService()
```

Führen Sie die Test erneut aus.
Sie werden erkennen, dass alle Tests fehlerfrei laufen.
Aber Sie sind noch nicht mit der Testfallerstellung fertig.

Ergänzen Sie folgenden Testfall am Ende Ihrer Testdatei und führen Sie alle erneut Testfälle aus.

```python
def test_clean_start_assumption(user_service):
    assert len(user_service.users) == 0, f"UserService sollte leer sein, hat aber: {user_service.users}"
    
    result = user_service.register("bob", "bob@test.com", "password456")
    assert result.success == True
```

Uff, das hat nicht funktioniert.
Jetzt könnten Sie natürlich wieder den Scope verändern.
Toben Sie sich gerne damit aus.
Das wird leider nicht funktionieren.
Warum da so ist, dazu müssen wir erst einmal Fixture Scopes betrachten.

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

Wenn Sie fertig sind, entfernen Sie diese Ergänzungen wieder.

Das aktuelle Dilemma ist, dass wir nicht alle Testfälle gleichzeitig erfolgreich durchlaufen
lassen können. Auch der vorhandene Scope hilft uns da nicht weiter.
Eine Lösung wäre, einen weiteren Scope einzuführen.

[EC] Ergänzen Sie einen weiteren Fixture Scope so, dass wirklich alle Testfälle erfolgreich sind.

[HINT::Reference]

1. Bedenken Sie, dass die Fixtures von den Testfällen gezielt genutzt werden, d.h. ein Testfall
   referenziert auf ein Fixture.
2. Ein Fixture alleine ist oftmals nicht ausreichend.
   Hier haben Sie eine Abhängigkeit der Reihenfolge erkannt.
   Der eine Scope hat eine Abhängigkeit, der andere keine, d.h. Sie müssen evt. einen weiteren
   Testfall mit in den Scope aufnehmen, um den fehlgeschlagenen Test erfolgreich zu bekommen.

[ENDHIN]

#### Setup und Teardown: Das Cleanup-Problem

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

[EQ] Testen Sie den Code und führen Sie ihn aus. Was ist hier das Problem?

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

Jedoch wollen wir nicht am Ende löschen, sondern brauchen diese tolle Funktion viel früher.

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

[ER] Implementieren Sie ein Teardown/Cleanup nach jedem Testfall.

[EQ] Was passiert, wenn ein Test einen Fehler wirft? Wird Cleanup trotzdem ausgeführt?

Das Ganze kann man auch mit Hilfe einer Hilfklasse umsetzen, was es übersichtlicher egstaltet.

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

Hier stellen wir in unserem Fixture sicher, dass wir immer 
`request.addfinalizer(manager.cleanup)` nach jedem test ausführen.

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
