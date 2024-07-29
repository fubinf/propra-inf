title: Fixtures mit dem Pytest Framework
stage: draft
timevalue: 0
difficulty: 3
assumes: m_pytest
---

TODO_1_ruhe:

- `@pytest.fixture` ist für den Zweck tabellengesteuerter Tests nicht der beste Mechanismus,
  weil dann alle Eingabedatensätze in nur einem Test benutzt werden müssen und wenn einer davon
  fehlschlägt, sieht man nicht, was beim Rest passiert.
- `@pytest.parametrize` ist für diesen Zweck richtig und wird schon in `m_pytest_parametrize`
  abgehandelt. (Das wandelt jeden Datensatz in einen virtuell separaten Test um.)
- Schauen Sie gern beide dieser Aufgaben durch, ob noch ein Gedanke aus Ihrer in `m_pytest_parametrize`
  ergänzt werden sollte (Achtung: Die Aufgabe ist schon freigegeben), aber vermutlich eher nicht.
- Gegen eine Aufgabe zu `@pytest.fixture` ist nichts zu sagen, aber dafür müsste man sich erst
  noch einen neuen Zweck ausdenken.
- Man könnte eine Aufgabe machen, die ein paar der in pytest eingebauten Fixtures ausprobiert.
  Z.B. capsys ist ganz nützlich: Damit kann man die von pytest aufgefangenen Ausgaben des SUT 
  in die Hand bekommen, um zu prüfen, ob sie den Erwartungen entsprechen.


[SECTION::goal::idea]

Ich kann Fixtures mit dem Pytest Framework anwenden.

[ENDSECTION]
[SECTION::background::default]

Oftmals benötigten Sie zum Testen bestimmte Voraussetzungen, die erfüllt sein müssen.
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

[HINT::Modulimport]
Damit Sie diesen Test ausführen können, müssen Sie Pytest noch importieren.
[ENDHINT]

- [ER] Ergänzen Sie die fehlende Fixture-Markierung.

Mit dieser Methoden haben wir die Möglichkeit einfache Testdaten zur Verfügung zu stellen. Es kann
aber auch gerne minimal komplexer werden.

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

Zum Abschluss der Testdatenverwendung noch etwas komplexer:

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

- [ER] Ergänzen Sie die fehlenden testdaten in den Fixtures.
- [EC] Führen Sie den Test aus und dokumentieren Sie das Ergebnis.

Mit Fixtures können nicht nur Testdaten bereitgestellt werden, sondern auch benötigte Objekte erzeugt
und gelöscht werden.

### ### Vor- und Nachbedingung auf Testfallebene schaffen

- Legen Sie die Datei `unittests/test_pytest_fixtures4.py` an.

Verwenden Sie die folgende Klasseninitialisierung, um ...

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
```

- [ER] ... ein `user_setup_teardown()`-Fixture und ein `test_user()` zu erstellen, wobei:
user_setup_teardown: sowohl die Erstellung, als auch die Löschung des Nutzer umsetzt
test_user: Nutzername und Passwort prüft

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

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Kommandoprotokoll prüfen]

- [EREFR::1]: Hier fehlt lediglich der Decorator `@pytest.fixture` über `example_fuxture()`
- [EREFR::2]: Ein Test könnte so aussehen:

```python
def test_user_data(user_data):
    assert user_data.username == "testuser"
    assert user_data.email == "testuser@example.com"
```

- [EREFR::3]: Es sollten folgende Datenv orhanden sein, damit der Test erfolgreich abgeschlossen wird:

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

- [EREFC::1] Konsolenauszug:

```bash
================================================================== test session starts ==================================================================
platform darwin -- Python 3.9.6, pytest-8.2.1, pluggy-1.5.0
rootdir: <removed_by_author>
collected 3 items                                                                                                                                       

test_main.py ...                                                                                                                                  [100%]

=================================================================== 3 passed in 0.01s ===================================================================
```

- [EREFR::4] Eine Mögliche Lösung könnte so aussehen - Wichtigster Punkt (yield im Fixture zu verwenden)

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

[ENDINSTRUCTOR]
