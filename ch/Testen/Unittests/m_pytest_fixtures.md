title: Fixtures mit dem Pytest Framework
stage: alpha
timevalue: 3
difficulty: 3
assumes: m_pytest
---

[SECTION::goal::idea]

Ich kann Fixtures mit dem Pytest Framework anwenden.

[ENDSECTION]
[SECTION::background::default]

Oftmals benötigen Sie zum Testen bestimmte Voraussetzungen, die erfüllt sein müssen.
Fixtures sind ein zentrales Konzept in Pytest, das es ermöglicht, wiederverwendbare Setup- und
Teardown-Code für Tests bereitzustellen. Sie sind auch hervorragend geeignet, um Testdaten für
Unittests bereitzustellen.
Hier lernen Sie, wie Sie Fixtures mit Pytest nutzen können.

[ENDSECTION]
[SECTION::instructions::loose]

Nutzen Sie das [Pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
um die nachfolgenden Aufgaben zu lösen:

### Einfache Fixture Daten bereitstellen

- Legen Sie die Datei `unittests/test_pytest_fixtures.py` an.

Fügen Sie folgenden Test ein:

```python
def example_fixture():
    return "Hello, World!"

def test_example(example_fixture):
    assert example_fixture == "Hello, World!"
```

- [ER] Ergänzen Sie die fehlende Fixture-Markierung.

Mit dieser Methoden haben wir die Möglichkeit einfache Testdaten zur Verfügung zu stellen. Es kann
aber auch gerne minimal komplexer werden.

### Komplexere Fixture Daten bereitstellen

- Legen Sie die Datei `unittests/test_pytest_fixtures2.py` an.

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

@pytest.fixture
def user_data():
    return User(username="testuser", email="testuser@example.com")

def test_user_data():
   # Ergänzen Sie die fehlenden Asserts
   
```

- [ER] Prüfen Sie in `test_user_data()`, ob der Nutzername und die E-Mail Adresse übereinstimmen.

### Komplexe Testdaten mit mehreren Fixtures

- Legen Sie die Datei `unittests/test_pytest_fixtures3.py` an.

```python

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

@pytest.fixture
def user_data():
   pass

@pytest.fixture
def product_data():
   pass

def test_user_data(user_data):
    assert len(user_data) == 3
    assert user_data[0].username == "testuser1"
    assert user_data[0].email == "testuser1@example.com"
    assert user_data[1].username == "testuser2"
    assert user_data[1].email == "testuser2@example.com"
    assert user_data[2].username == "testuser3"
    assert user_data[2].email == "testuser3@example.com"

def test_product_data(product_data):
    assert len(product_data) == 3
    assert product_data[0].name == "Product1"
    assert product_data[0].price == 10.99
    assert product_data[1].name == "Product2"
    assert product_data[1].price == 15.49
    assert product_data[2].name == "Product3"
    assert product_data[2].price == 7.99

def test_combined_data(user_data, product_data):
    assert len(user_data) == 3
    assert len(product_data) == 3
    assert user_data[0].username == "testuser1"
    assert product_data[0].name == "Product1"
```

- [ER] Ergänzen Sie die fehlenden Testdaten in den Fixtures.

Dieses Vorgehen ist ein sogenanntes Tabellengesteuerter Test, bei dem ein Testfall mehrfach mit
unterschiedlichen Testdaten ausgeführt wird. Das hat Scharm, um die Testabdeckung zu erhöhen und um
die eine oder andere Testmethodik anzuwenden (z.B. Äquivalenzklassentests, oder Tests von Randbedingungen)
Jedoch hat es auch Nachteile.

- [EQ] Welcher Nachteil hat dieses Vorgehen?

[HINT::Testdaten anpassen]
Spielen Sie ein wenig mit den Testdaten. Verwenden Sie auch negative / falsche Testdaten.
`@pytest.parametrize` ist für diesen Zweck richtig und wird in [PARTREF::m_pytest_parametrize] behandelt.
[ENDHINT]

- [EC] Führen Sie den Test aus und dokumentieren Sie das Ergebnis.

Mit Fixtures können nicht nur Testdaten bereitgestellt werden, sondern auch benötigte Objekte erzeugt
und gelöscht werden.

### Vor- und Nachbedingung auf Testfallebene schaffen

- Legen Sie die Datei `unittests/test_pytest_fixtures4.py` an.

Verwenden Sie die folgende Klasseninitialisierung, um ...

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
```

- [ER] ... ein `user_setup_teardown()`-Fixture und ein `test_user()` zu erstellen, wobei:
`user_setup_teardown` sowohl die Erstellung, als auch die Löschung des Nutzer umsetzt und
`test_user` Nutzername und Passwort prüft

[HINT::Umsetzungshilfe]
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
def greet(name):
    print(f"Hello, {name}!")
```

- [ER] Erstellen Sie einen Test, der die Ausgabe von `stdout` mit `capsys` abfängt und überprüft, ob die Begrüßung korrekt ist.

[HINT::Referenz_capsys]
Weitere Informationen zur Verwendung von `capsys` finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function).
[ENDHINT]

#### Aufgabe 2: Verwendung von `tmpdir`

Betrachten Sie die folgende Funktion:

```python
def write_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
```

- [ER] Erstellen Sie einen Test, der ein temporäres Verzeichnis mit `tmpdir` verwendet, um eine Datei zu erstellen und deren Inhalt zu überprüfen.

[HINT::Referenz_tmpdir]
Weitere Informationen zur Verwendung von `tmpdir` finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/tmpdir.html).
[ENDHINT]

#### Aufgabe 3: Verwendung von `monkeypatch`

Betrachten Sie die folgende Funktion:

```python
import os

def get_current_directory():
    return os.getcwd()
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
def write_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
```

- [ER] Erstellen Sie einen Test, der ein temporäres Verzeichnis mit `tmp_path` verwendet, um eine Datei zu erstellen und deren Inhalt zu überprüfen.

[HINT::Referenz_tmp_path]
Weitere Informationen zur Verwendung von `tmp_path` finden Sie in der [Pytest-Dokumentation](https://docs.pytest.org/en/stable/how-to/tmpdir.html#the-tmp-path-fixture).
[ENDHINT]

#### Aufgabe 2: Verwendung von `caplog`

Betrachten Sie die folgende Funktion:

```python
import logging

def log_message(message):
    logging.info(message)
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

[ENDSECTION]
[INSTRUCTOR::Kommandoprotokoll prüfen]

- [EREFR::1]: Hier fehlt lediglich der Decorator `@pytest.fixture` über `example_fixture()`
- [EREFR::2]: Ein Test könnte so aussehen:

```python
def test_user_data(user_data):
    assert user_data.username == "testuser"
    assert user_data.email == "testuser@example.com"
```

- [EREFR::3]: Es sollten folgende Daten vorhanden sein, damit der Test erfolgreich abgeschlossen wird:

```python
@pytest.fixture
def user_data():
    users = [
        User(username="testuser1", email="testuser1@example.com"),
        User(username="testuser2", email="testuser2@example.com"),
        User(username="testuser3", email="testuser3@example.com")
    ]
    return users

@pytest.fixture
def product_data():
    products = [
        Product(name="Product1", price=10.99),
        Product(name="Product2", price=15.49),
        Product(name="Product3", price=7.99)
    ]
    return products
```

- [EREFQ::1] `@pytest.fixture` ist für den Zweck tabellengesteuerter Tests nicht der beste Mechanismus,
  weil dann alle Eingabedatensätze in nur einem Test benutzt werden müssen und wenn einer davon
  fehlschlägt, sieht man nicht, was beim Rest passiert.

- [EREFC::1] Konsolenauszug:

```bash
================================================================== test session starts ==================================================================
platform darwin -- Python 3.9.6, pytest-8.2.1, pluggy-1.5.0
rootdir: <removed_by_author>
collected 3 items                                                                                                                                       

test_main.py ...                                                                                                                                  [100%]

=================================================================== 3 passed in 0.01s ===================================================================
```

- [EREFR::4] Eine mögliche Lösung könnte so aussehen - Wichtigster Punkt (yield im Fixture zu verwenden)

```python
@pytest.fixture
def user_setup_teardown():
    print("\nSetup: Benutzer wird erstellt")
    user = User(username="testuser", email="testuser@example.com")
    yield user
    print("\nTeardown: Benutzer wird gelöscht")
    del user

def test_user(user_setup_teardown):
    user = user_setup_teardown
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
```

- [EREFR::5] Ergänzt wurde der Dekorierer-Parameter: `@pytest.fixture(scope="session")`
- [EREFR::6] Das Auslagern muss in dieser speziellen Datei geschehen und die Klasse `User` muss
  ebenfalls mitgenommen werden.

- [EREFR::7] Eine mögliche Umsetzung:

```python
def test_cache(cache):
    value = cache.get("example_key", None)
    if value is None:
        cache.set("example_key", "example_value")
    assert cache.get("example_key", None) == "example_value"
```

- [EREFQ::2] Nein, die Funktion kann korrekt sein, denn die Funktion speichert Daten nur innerhalb
  von Python und nicht im Browser. Um hier diesen Wert zur Verfügung zu stellen, müsste man ein
  Framework wie Flask, Django oder ähnlichem verwendet. (Automatisiert dann über eine Testautomatisierungs-
  lösung wie Selenium oder mittels JS auslesen)

- [EREFR::8] Beispiel-unittests für eingebaute Fixtures:

```python
import pytest

def greet(name):
    print(f"Hello, {name}!")

def test_capsys(capsys):
    greet("World")
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

def write_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def test_tmpdir(tmpdir):
    temp_file = tmpdir.join("temp_file.txt")
    write_to_file(temp_file, "Hello, World!")
    assert temp_file.read() == "Hello, World!"

import os

def get_current_directory():
    return os.getcwd()

def test_monkeypatch(monkeypatch):
    monkeypatch.setattr(os, "getcwd", lambda: "/tmp")
    assert get_current_directory() == "/tmp"
```

- [EREFC::2] Konsolenauszug:

```bash
================================================================== test session starts ==================================================================
platform darwin -- Python 3.9.6, pytest-8.2.1, pluggy-1.5.0
rootdir: <removed_by_author>
collected 3 items                                                                                                                                       

test_pytest_built_in_fixtures.py ...                                                                                                              [100%]

=================================================================== 3 passed in 0.01s ===================================================================
```

- [EREFR::9] Beispiel-unittests für erweiterte und eingebaute Fixtures:

```python
import pytest
import logging

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

@pytest.fixture(autouse=True)
def setup_teardown():
    print("Setup")
    yield
    print("Teardown")

def test_example():
    assert True

def write_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def test_tmp_path(tmp_path):
    temp_file = tmp_path / "temp_file.txt"
    write_to_file(temp_file, "Hello, World!")
    assert temp_file.read_text() == "Hello, World!"

def log_message(message):
    logging.info(message)

def test_caplog(caplog):
    log_message("Test message")
    assert "Test message" in caplog.text
```

- [EREFC::3] Konsolenauszug:

```bash
================================================================== test session starts ==================================================================
platform darwin -- Python 3.9.6, pytest-8.2.1, pluggy-1.5.0
rootdir: <removed_by_author>
collected 5 items                                                                                                                                       

test_pytest_yield_fixture.py .                                                                                                                     [ 20%]
test_pytest_autouse_fixture.py .                                                                                                                   [ 40%]
test_pytest_more_built_in_fixtures.py ...                                                                                                          [100%]

=================================================================== 5 passed in 0.02s ===================================================================
```

[ENDINSTRUCTOR]
