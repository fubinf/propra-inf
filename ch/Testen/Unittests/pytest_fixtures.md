title: Fixtures mit dem Pytest Framework
stage: alpha
timevalue: 2.5
difficulty: 3
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
[SECTION::instructions::loose]

Nutzen Sie das Feature 
[Pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
um die nachfolgenden Aufgaben zu lösen:

### Einfache Fixture-Daten bereitstellen

[ER] Legen Sie die Datei `test_pytest_fixtures.py` an.
Fügen Sie folgenden Test ein und ergänzen Sie die fehlende Fixture-Markierung:

```python
import pytest

@pytest.fixture
def example_fixture():
    return "Hello, World!"

def test_example(example_fixture):
    assert example_fixture == "Hello, World!"
```

`example_fixture` stellt also Testdaten bereit. 
Jeder Test, der genau diese Daten gebrauchen kann, kann das Fixture bennennen und damit aufrufen.

### Komplexere Fixture-Daten bereitstellen

Das gleiche Prinzip funktioniert natürlich auch mit komplexeren Datenstrukturen.

[ER] Ergänzen Sie folgenden Testfall in die Datei und vervollständigen Sie ihn.
Prüfen Sie in `test_user_data()` trivial, ob der Nutzername und die Email-Adresse korrekt sind.

```python
import pytest

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

@pytest.fixture
def user_data():
    return User(username="testuser", email="testuser@example.com")

def test_user_data(user_data):
    # Ergänzen Sie die fehlenden Asserts
    assert user_data.username == "testuser"
    assert user_data.email == "testuser@example.com"
```


### Komplexe Testdaten mit mehreren Fixtures

Ein Test kann auch mehr als eine Fixture benutzen.

[ER] Ergänzen Sie die fehlenden Fixtures, damit das (unveränderte) `test_combined_data()` funktioniert.

```python
import pytest

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

@pytest.fixture
def user_data3():
    return [User(f"testuser{i}", f"testuser{i}@example.com") for i in range(1, 4)]

@pytest.fixture
def product_data3():
    return [Product(f"Product{i}", i * 10.0) for i in range(1, 4)]

def test_combined_data(user_data3, product_data3):
    assert len(user_data3) == 3
    assert len(product_data3) == 3
    assert user_data3[0].username == "testuser1"
    assert product_data3[0].name == "Product1"
```

[HINT::Wie schaffe ich, dass das `len` funktioniert?]
Beide Fixtures liefern eine Liste, nicht nur ein einzelnes Objekt.
[ENDHINT]


### Vor- und Nachbedingung auf Testfallebene schaffen

- Legen Sie die Datei `unittests/test_pytest_fixtures4.py` an.

Verwenden Sie die folgende Klasseninitialisierung, um ...

```python
import pytest

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
```

- [ER] ... ein `user_setup_teardown()`-Fixture und ein `test_user()` zu erstellen, wobei:
`user_setup_teardown` sowohl die Erstellung, als auch die Löschung des Nutzer umsetzt und
`test_user` Nutzername und Passwort prüft

[HINT::Wie macht man Setup und Teardown?]
Ein Setup und Teardown in einem Fixture kann mit [yield](https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures-recommended) realisiert werden.
[ENDHINT]

### Fixture Scope

Die Fixture können in unterschiedlichen Bereichen eingesetzt werden. Prüfen Sie die möglichen
Bereiche für Fixtures in der oben angegebenen Dokumentation.

- [ER] Ergänzen Sie in [EREFR::4] den Scope `session`.

### Fixtures auslagern

Wenn wir schon Bereiche angeben können, sollten auch andere Tests, die nicht im selben Modul sind,
davon profitieren können.

- [ER] Lagern Sie die Fixture `user_setup_teardown()` aus [EREFR::4] in eine separate Datei
  `conftest.py` aus.
- [EC] Lassen Sie den Testfall erneut laufen.

### Build-In Fixtures

Pytest besitzt bereits einige definierte Fixtures. Eine Auflistung und eine Beschreibung finden
Sie [hier](https://docs.pytest.org/en/stable/reference/fixtures.html#built-in-fixtures)

- [ER] Erstellen Sie ein Cache Beispiel, indem ein Cache angefragt und geprüft wird. Falls der Wert
  `None` ist, soll er mit dem zu prüfenden Wert belegt werden.
- [EQ] Ich habe nach der Ausführung dieses Codes einne Blick in meinen Browser Cache geworfen. Einen
  neuen Cache Wert finde ich nicht. Ist meine Funktion deshlab falsch, oder liegt das an etwas anderem?

### Verwendung von eingebauten Fixtures

- Legen Sie die Datei `unittests/test_pytest_built_in_fixtures.py` an.

#### Aufgabe 1: Verwendung von `capsys`

Betrachten Sie die folgende Funktion:

```python
import pytest

def greet(name):
    print(f"Hello, {name}!")

def test_greet_output(capsys):
    greet("World")
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
```

- [ER] Erstellen Sie einen Test, der die Ausgabe von `stdout` mit `capsys` abfängt und überprüft, ob die Begrüßung korrekt ist.

[HINT::Referenz_capsys]
Weitere Informationen zur Verwendung von `capsys` finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function).
[ENDHINT]

#### Aufgabe 2: Verwendung von `tmpdir`

Betrachten Sie die folgende Funktion:

```python
import pytest

def write_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def test_write_to_file(tmpdir):
    file_path = tmpdir.join("test.txt")
    content = "Hello, pytest!"
    write_to_file(str(file_path), content)
    assert file_path.read() == content
```

- [ER] Erstellen Sie einen Test, der ein temporäres Verzeichnis mit `tmpdir` verwendet, um eine Datei zu erstellen und deren Inhalt zu überprüfen.

[HINT::Referenz_tmpdir]
Weitere Informationen zur Verwendung von `tmpdir` finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/tmpdir.html).
[ENDHINT]

#### Aufgabe 3: Verwendung von `monkeypatch`

Betrachten Sie die folgende Funktion:

```python
import pytest
import os

def get_current_directory():
    return os.getcwd()

def test_get_current_directory(monkeypatch):
    test_dir = "/test/directory"
    monkeypatch.setattr(os, "getcwd", lambda: test_dir)
    assert get_current_directory() == test_dir
```

- [ER] Erstellen Sie einen Test, der die Funktion `get_current_directory` mit `monkeypatch` patcht und überprüft, ob das aktuelle Verzeichnis korrekt zurückgegeben wird.

[HINT::Referenz_monkeypatch]
Weitere Informationen zur Verwendung von `monkeypatch` finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/monkeypatch.html).
[ENDHINT]

### Erweiterte Verwendung von `yield` in Fixtures

- Legen Sie die Datei `unittests/test_pytest_yield_fixture.py` an.

```python
import pytest

class Database:
    def connect(self):
        print("Connecting to database")
    def disconnect(self):
        print("Disconnecting from database")

@pytest.fixture
def db():
    db = Database()
    db.connect()
    yield db
    db.disconnect()

def test_db_connection(db):
    assert db is not None
```

- [ER] Erstellen Sie eine Fixture, die eine Datenbankverbindung herstellt und nach dem Test wieder trennt.

[HINT::Referenz_yield]
Weitere Informationen zur Verwendung von `yield` in Fixtures finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures-recommended).
[ENDHINT]

### Verwendung von `autouse`

- Legen Sie die Datei `unittests/test_pytest_autouse_fixture.py` an.

```python
import pytest

@pytest.fixture(autouse=True)
def setup_teardown():
    print("Setup")
    yield
    print("Teardown")

def test_example():
    assert True
```

- [ER] Erstellen Sie eine Fixture, die automatisch für jeden Test ausgeführt wird, ohne dass sie explizit angegeben werden muss.

[HINT::Referenz_autouse]
Weitere Informationen zur Verwendung von `autouse` in Fixtures finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/fixtures.html#autouse-fixtures).
[ENDHINT]

### Weitere Beispiele für eingebaute Fixtures

- Legen Sie die Datei `unittests/test_pytest_more_built_in_fixtures.py` an.

#### Aufgabe 1: Verwendung von `tmp_path`

Betrachten Sie die folgende Funktion:

```python
import pytest

def write_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def test_write_to_file_tmp_path(tmp_path):
    file_path = tmp_path / "test.txt"
    content = "Hello, tmp_path!"
    write_to_file(file_path, content)
    assert file_path.read_text() == content
```

- [ER] Erstellen Sie einen Test, der ein temporäres Verzeichnis mit `tmp_path` verwendet, um eine Datei zu erstellen und deren Inhalt zu überprüfen.

[HINT::Referenz_tmp_path]
Weitere Informationen zur Verwendung von `tmp_path` finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/tmpdir.html#the-tmp-path-fixture).
[ENDHINT]

#### Aufgabe 2: Verwendung von `caplog`

Betrachten Sie die folgende Funktion:

```python
import pytest
import logging

def log_message(message):
    logging.info(message)

def test_log_message(caplog):
    with caplog.at_level(logging.INFO):
        log_message("Test message")
    assert "Test message" in caplog.text
```

- [ER] Erstellen Sie einen Test, der die Log-Ausgabe mit `caplog` abfängt und überprüft, ob die Nachricht korrekt geloggt wurde.

[HINT::Referenz_caplog]
Weitere Informationen zur Verwendung von `caplog` finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/logging.html#caplog-fixture).
[ENDHINT]

### Reflektion

Sie haben eine kleine Übersicht über nützliche Fixtures kennengelernt.

- [EQ] Welche von denen haben Sie bereits persönlich verwnendet. Kennen Sie weitere Fixtures, die in
  jedem Werkzeugkasten eines Softwareentwicklers gehören sollte? Welches dieser Fixtures hat Ihnen
  Schwierigkeiten verursacht? Woran könnte das gelegen haben?

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
