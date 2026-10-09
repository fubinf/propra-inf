title: Fixtures mit dem pytest-Framework
stage: alpha
timevalue: 2.0
difficulty: 3
assumes: m_pytest
explains: Fixture
---

[SECTION::goal::idea]
Ich kann Fixtures mit dem pytest-Framework anwenden.
[ENDSECTION]


[SECTION::background::default]
Oftmals braucht ein Test bestimmte Voraussetzungen, bevor er überhaupt sinnvoll prüfen kann,
was er prüfen soll.
Ein Test kann zum Beispiel eine Benutzer-Instanz, eine Konfiguration oder eine vorbereitete Datei brauchen.

Eine [TERMREF::Fixture] ist in pytest genau dafür gedacht: Sie kapselt das Setup und das Cleanup.
Dadurch bleibt der eigentliche Test lesbarer,
und dieselben Vorbereitungen können leicht in mehreren Tests wiederverwendet werden.

In dieser Aufgabe lernen Sie Schritt für Schritt, wie Sie solche Voraussetzungen sauber
vorbereiten, wie Sie ihre Lebensdauer steuern und wann es wichtig ist, Ressourcen nach dem
Test wieder aufzuräumen.
[ENDSECTION]


[SECTION::instructions::detailed]
Nutzen Sie die folgende Übersicht parallel zum Bearbeiten der Aufgaben:

[pytest-Doku: How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

### Das Problem ohne Fixtures

Betrachten Sie zunächst diese kleinen Tests für einen Benutzer-Dienst.
Der Code ist bewusst noch etwas unordentlich, damit Sie die Probleme direkt sehen können.

```python
class Result:
    def __init__(self, success):
        self.success = success


class PseudoUserservice:
    def __init__(self):
        self.users = {}

    def register(self, username, email, password):
        if username in self.users:
            return Result(False)
        self.users[username] = {'email': email, 'password': password}
        return Result(True)

    def login(self, username, password):
        user = self.users.get(username)
        if user and user['password'] == password:
            return Result(True)
        return Result(False)


service = PseudoUserservice()  # wird von allen Tests gemeinsam benutzt


def test_user_login():
    # Setup
    service.register("alice", "alice@test.com", "password123")

    # Test
    result = service.login("alice", "password123")
    assert result.success

    # Cleanup
    service.users.clear()


def test_user_registration():
    # Test
    result = service.register("alice", "alice@test.com", "password123")
    assert result.success

    # Cleanup
    service.users.clear()


def test_user_login_wrong_password():
    # Setup
    service.register("alice", "alice@test.com", "password123")

    # Test
    result = service.login("alice", "wrong")
    assert not result.success

    # Cleanup
    service.users.clear()


def test_user_registration_duplicate():
    # Setup
    service.register("alice", "alice@test.com", "password123")

    # Test
    result = service.register("alice", "other@test.com", "secret")
    assert not result.success

    # Cleanup
    service.users.clear()
```

[EQ] Welche Probleme erkennen Sie in diesem Code? Notieren Sie mindestens drei Probleme.
<!-- time estimate: 5 min -->

### Die Fixture-Idee und der Ausgangscode

pytest löst genau diese Schwächen mit Fixtures.

Eine Fixture ist im Grunde ein wiederverwendbares Setup, das ein Test als Abhängigkeit
anfordern kann.
Statt in jedem Test denselben Initialisierungscode neu zu schreiben,
definieren Sie ihn einmal und referenzieren ihn dann über die Test-Signatur.

Das hat zwei Vorteile: Der eigentliche Test wird viel lesbarer,
und die Einrichtung bleibt an einer Stelle zentralisiert.

Bevor wir Fixtures einsetzen, legen wir den Ausgangscode an.
Der zu testende Code gehört nicht in eine Testdatei.
Legen Sie deshalb eine Datei `userservice.py` an und übernehmen Sie dorthin
die Klassen `Result` und `PseudoUserservice` aus dem Beispiel oben.

Den ersten Schritt machen wir noch ohne Fixtures:
Das gemeinsame globale `service` entfällt, jeder Test erzeugt sich eine eigene, frische Instanz.
Dann kann kein Test einem anderen Zustand hinterlassen, und das Cleanup entfällt.
Legen Sie im selben Verzeichnis die Datei `test_userservice.py` mit folgenden Tests an:

```python
from userservice import PseudoUserservice


def test_user_registration():
    service = PseudoUserservice()
    result = service.register("alice", "alice@test.com", "password123")
    assert result.success

def test_user_registration_duplicate():
    service = PseudoUserservice()
    service.register("alice", "alice@test.com", "password123")  # Pre-condition
    result = service.register("alice", "other@test.com", "secret")
    assert not result.success

def test_user_login():
    service = PseudoUserservice()
    service.register("alice", "alice@test.com", "password123")  # Pre-condition
    result = service.login("alice", "password123")
    assert result.success

def test_user_login_wrong_password():
    service = PseudoUserservice()
    service.register("alice", "alice@test.com", "password123")  # Pre-condition
    result = service.login("alice", "wrong")
    assert not result.success
```

Das duplizierte Setup ist dabei geblieben:
Jeder Test erzeugt seine Instanz selbst, und drei der vier Tests registrieren vorab dieselbe `alice`.
<!-- time estimate: 10 min -->

### Setup deklarativ machen

Anstatt in jedem Test den gleichen Setup-Code zu kopieren, definieren Sie ihn einmal als
Fixture und verwenden ihn dann an den Stellen, an denen ein Test ihn braucht.

```python
import pytest


@pytest.fixture
def user_service():
    return PseudoUserservice()

def test_user_registration(user_service):
    ...
```

Damit wäre erst das Erzeugen der Instanz zentralisiert; die Registrierung von `alice` stünde
weiterhin in drei Tests.

Ein Test kann auch mehrere Fixtures gleichzeitig verwenden: Sie listen einfach mehrere
Parameter in der Signatur auf.
Auf dieselbe Weise kann auch eine Fixture ihrerseits andere Fixtures anfordern.
Suchen Sie in der oben verlinkten pytest-Doku nach den Abschnitten
„Fixtures can request other fixtures“ und
„A test/fixture can request more than one fixture at a time“ und lesen Sie sie.

[ER] Ergänzen Sie Ihre `test_userservice.py` um die Fixture `user_service` von oben
und um eine zweite Fixture `registered_service`, die `user_service` anfordert
und darin `alice` registriert.
Stellen Sie alle vier Tests auf diese beiden Fixtures um:
Kein Test soll mehr selbst eine Instanz erzeugen oder `alice` vorab registrieren.

[EQ] Stellen Sie sich eine Testdatei mit Dutzenden Tests vor, die verschiedene Kombinationen
von Fixtures verwenden.
Welchen Vorteil hat es, wenn alle benötigten Fixtures als Parameter in der Signatur stehen?
<!-- time estimate: 20 min -->

### Fixture Scopes: wann welcher?

Manche Fixtures sind aufwendig: Eine Datenbankverbindung aufzubauen, Testdaten zu laden oder
einen Server zu starten kann Sekunden dauern.
Genau in solchen Fällen wird wichtig, wie lange eine Fixture bestehen bleibt.

Mit dem Standard-Scope `"function"` wird das Setup für jeden einzelnen Test erneut ausgeführt.

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

[EC] Fügen Sie diesen Code zu `test_userservice.py` hinzu und messen Sie die Laufzeit:
`pytest -v test_userservice.py`

[EQ] Wie viele Sekunden dauert die Testsuite insgesamt?
Was wäre bei 100 Tests, die diese Fixture verwenden?

pytest bietet verschiedene Scopes für Fixtures:

- `function`: Neue Instanz für jeden Test (Standard, beste Isolation)
- `class`: Eine Instanz für alle Tests einer Test-Klasse
- `module`: Eine Instanz für alle Tests einer Datei
- `session`: Eine Instanz für die gesamte Test-Session

Faustregel: Behalten Sie in der Regel `function` bei.
Nutzen Sie einen größeren Scope nur dann, wenn das Setup wirklich teuer ist
und der gemeinsame Zustand bewusst kontrolliert werden kann.

Ein sinnvoller Fall für einen größeren Scope ist zum Beispiel das einmalige Laden einer großen
Konfigurationsdatei: Das ist aufwendig, aber danach nur lesbar.

```python
@pytest.fixture(scope="session")
def app_config():
    return load_big_test_config()
```

Ändern Sie nun den Scope auf `"module"`:

```python
@pytest.fixture(scope="module")
def slow_service():
    time.sleep(1)
    return PseudoUserservice()
```

[EC] Führen Sie die Tests erneut aus: `pytest -v test_userservice.py`

[EQ] Wie verändert sich die Laufzeit, und warum?
Was müssen Sie beachten, wenn mehrere Tests dieselbe Instanz teilen?

[HINT::Ich verstehe nicht, was dabei schiefgehen kann]
Was passiert, wenn `test_slow_1` einen Nutzer registriert und ein weiterer Test sich darauf
verlässt, dass noch kein Nutzer registriert ist?
[ENDHINT]

Wenn Sie einen größeren Scope wählen, müssen Sie selbst dafür sorgen, dass der Zustand zwischen
den Tests sauber zurückgesetzt wird.
Die gemeinsame Nutzung hat nur dann Sinn, wenn die Ressource unverändert bleibt
oder bewusst wieder in einen Ausgangszustand gebracht wird.

Entfernen Sie danach `slow_service` und die drei zugehörigen Tests wieder,
damit der Rest der Datei nicht durch das `sleep()` ausgebremst wird.
<!-- time estimate: 25 min -->

### Setup und Teardown: Das Cleanup-Problem

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

[EC] Fügen Sie diesen Code zu `test_userservice.py` hinzu und führen Sie die Tests aus:
`pytest -v test_userservice.py`

[EQ] Was ist hier das Problem?

In diesem Beispiel stecken zwei verschiedene Probleme:

- **Zustandsleckage:** Beide Tests teilen sich wegen `scope="module"` dieselbe Datei.
  Was der erste Test hineinschreibt, sieht der zweite.
  Am einfachsten wäre `function`-Scope.
  Nehmen wir aber an, die Datei sei teuer zu erzeugen und wir bräuchten `module`-Scope.
  Dann muss jeder Test, der sich auf den Ausgangszustand verlässt, diesen selbst herstellen.
- **Aufräumen:** `debug_output.txt` liegt fest im Arbeitsverzeichnis und bleibt nach dem Testlauf
  dort liegen.
  Laufen zwei Testläufe gleichzeitig oder aus einem anderen Verzeichnis, kommen sie sich in die Quere.
  Besser ist ein eigenes Verzeichnis für temporäre Testdaten.
  pytest bietet dafür `tmp_path` an; das Modul `tempfile` stellt ähnliche Mechanismen bereit.
  Siehe auch [PARTREF::m_tempfile].

`tmp_path` selbst hat `function`-Scope und lässt sich deshalb in einer `module`-Fixture nicht
verwenden.
Für diesen Fall gibt es
[`tmp_path_factory`](https://docs.pytest.org/en/stable/reference/reference.html#tmp-path-factory):
Sein `mktemp()` legt ein neues temporäres Verzeichnis an.

Außerdem soll die Fixture ihre Datei am Ende selbst wieder entfernen.
Dafür schreibt man eine Fixture mit `yield` statt `return`:
Der Code vor `yield` ist das Setup, der mit `yield` übergebene Wert ist das, was der Test bekommt,
und der Code nach `yield` ist der Teardown.
pytest führt den Teardown aus, sobald das Fixture-Exemplar nicht mehr gebraucht wird,
bei `function`-Scope also nach jedem Test, bei `module`-Scope erst nach dem letzten Test der Datei.
Wie `yield` in Python allgemein funktioniert, müssen Sie hierfür nicht wissen; das Muster genügt.
Lesen Sie dazu in der pytest-Doku den Anfang des Abschnitts
[Teardown/Cleanup (AKA Fixture finalization)](https://docs.pytest.org/en/stable/how-to/fixtures.html#teardown-cleanup-aka-fixture-finalization)
über Yield-Fixtures.

Ersetzen Sie in `test_userservice.py` die Fixture `temp_file` und die beiden Tests
durch folgende Fassung:

```python
@pytest.fixture(scope="module")
def temp_file(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp("shared-temp")
    path = temp_dir / "debug_output.txt"
    path.write_text("Test war hier!")
    yield path
    print(f"Cleanup: {path} wird entfernt.")
    path.unlink(missing_ok=True)


def test_creates_temp_file(temp_file):
    assert temp_file.exists()
    with open(temp_file, "a") as f:
        f.write(" - Test 1 war hier!")
    assert "Test war hier" in temp_file.read_text()


def test_another_temp_file(temp_file):
    temp_file.write_text("Test war hier!")  # Ausgangszustand selbst herstellen
    content = temp_file.read_text()
    print(f"Dateiinhalt: {content}")
    assert content == "Test war hier!"
```

Den Import von `os` braucht `test_userservice.py` danach nicht mehr.
Löschen Sie außerdem die übrig gebliebene `debug_output.txt` aus Ihrem Arbeitsverzeichnis.

Wohin legt pytest diese temporären Verzeichnisse eigentlich, und was bleibt davon übrig?

[EC] Führen Sie die Tests viermal hintereinander aus: `pytest -v -s test_userservice.py`.
Mit `-s` zeigt pytest auch die `print()`-Ausgaben bestandener Tests an,
hier die Cleanup-Meldung mit dem vollständigen Pfad der Datei.
Listen Sie danach mit `ls -l` den Inhalt des Verzeichnisses `pytest-of-<Benutzername>` auf,
das in diesem Pfad vorkommt, und ebenso den Inhalt eines der darin liegenden `pytest-<Nummer>`-Verzeichnisse.

[EQ] Welche Verzeichnisse finden Sie, und wie viele davon?
Was ist aus den Verzeichnissen der älteren Läufe geworden, und wo ist `debug_output.txt` geblieben?
Was bedeutet das im Vergleich zur festen Datei im Arbeitsverzeichnis?

Verändern Sie jetzt absichtlich einen Test so, dass er fehlschlägt:

```python
def test_another_temp_file(temp_file):
    assert False
```

[EC] Führen Sie danach erneut `pytest -v test_userservice.py` aus.

[EQ] Welche Ausgabe sehen Sie in der pytest-Konsole?
Wird der Cleanup in der Fixture noch ausgeführt, wenn der Test selbst fehlschlägt?
Warum ist das wichtig?

Machen Sie die Änderung an `test_another_temp_file` danach wieder rückgängig.
<!-- time estimate: 30 min -->

### Fixtures teilen: `conftest.py`

Wenn Sie mehrere Testdateien haben, die dieselben Fixtures brauchen, gibt es dafür in pytest
eine praktische Lösung.

Verschieben Sie die Fixture `user_service` aus `test_userservice.py` in eine neue Datei
`conftest.py` im selben Verzeichnis:

```python
import pytest

from userservice import PseudoUserservice


@pytest.fixture
def user_service():
    return PseudoUserservice()
```

`registered_service` bleibt in `test_userservice.py` und bekommt `user_service` nun aus `conftest.py`.
Den Import von `PseudoUserservice` braucht `test_userservice.py` danach nicht mehr.

Erstellen Sie eine zweite Testdatei `test_sharing.py`, die dieselbe Fixture benutzt:

```python
from userservice import PseudoUserservice


def test_in_other_file(user_service):
    assert isinstance(user_service, PseudoUserservice)
    result = user_service.register("bob", "bob@test.com", "pass")
    assert result.success
```

Keine der beiden Testdateien definiert oder importiert `user_service`.

[EC] Führen Sie beide Testdateien mit pytest aus:
`pytest -v test_userservice.py test_sharing.py`

pytest findet die Fixture trotzdem, und beide Dateien benutzen dieselbe Definition.
Dahinter steckt Folgendes:

1. **Automatisches Laden:** Beim Sammeln der Tests lädt pytest automatisch die `conftest.py`-Dateien
   im Verzeichnis der Testdateien und in den übergeordneten Verzeichnissen.
2. **Sichtbarkeit:** Fixtures aus einer `conftest.py` stehen allen Tests in deren Verzeichnis
   und dessen Unterverzeichnissen zur Verfügung, aber nicht darüber hinaus.
3. **Namensauflösung:** Wenn ein Test einen Parameter `user_service` hat, sucht pytest
   nach einer gleichnamigen Fixture in
   (1) der gleichen Datei, (2) `conftest.py` im gleichen Verzeichnis,
   (3) `conftest.py` in übergeordneten Verzeichnissen, (4) Plugins, darunter die eingebauten pytest-Fixtures.

Die Fixture ist also ohne normalen Python-Import sichtbar.
Die Klasse `PseudoUserservice` dagegen wird ganz normal aus `userservice.py` importiert;
`conftest.py` selbst sollte man nicht importieren, sie ist allein für pytest da.

Fixtures so zu teilen, ist zugleich die von pytest empfohlene Praxis:
Fixtures, die mehrere Testdateien brauchen, gehören in eine `conftest.py`
(projektübergreifend in ein Plugin); aus anderen Modulen importiert man sie nicht.
Die pytest-Doku rät davon ausdrücklich ab, siehe
[Using fixtures from other projects](https://docs.pytest.org/en/stable/how-to/fixtures.html#using-fixtures-from-other-projects).

[EQ] Warum kann die automatische Auflösung über `conftest.py` in einem übergeordneten Verzeichnis
plötzlich unangenehm werden, wenn ein Projekt wächst?
Nennen Sie ein konkretes Beispiel für ein Problem, das dadurch entstehen kann.

Um nachzusehen, welche Fixtures ein Test tatsächlich bekommt und in welcher Datei sie definiert sind,
gibt es `pytest --fixtures-per-test`.
<!-- time estimate: 15 min -->

### Eingebaute Fixtures: Ausgaben prüfen mit `capsys`

pytest bringt viele eingebaute Fixtures mit; eine Übersicht gibt die
[Built-in fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html).
`tmp_path` und `tmp_path_factory` kennen Sie schon.
Eine weitere häufig gebrauchte ist `capsys`: Sie fängt die Ausgaben auf stdout und stderr ab,
damit ein Test sie prüfen kann.
Lesen Sie dazu in der pytest-Doku den Abschnitt
[Accessing captured output from a test function](https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function).

Damit es etwas zu prüfen gibt, soll `register()` einen bereits vergebenen Benutzernamen
künftig mit einer Fehlermeldung auf stderr quittieren.
Ändern Sie `register()` in `userservice.py` wie folgt und ergänzen Sie dort oben `import sys`:

```python
    def register(self, username, email, password):
        if username in self.users:
            print(f"Benutzername {username} ist bereits vergeben.", file=sys.stderr)
            return Result(False)
        self.users[username] = {'email': email, 'password': password}
        return Result(True)
```

[ER] Schreiben Sie in `test_userservice.py` einen Test `test_duplicate_registration_message`,
der mit `capsys` prüft, dass eine doppelte Registrierung genau diese Meldung auf stderr ausgibt
und auf stdout nichts.
Verwenden Sie dafür Ihre Fixture `registered_service`.

[EC] Führen Sie die Tests aus: `pytest -v test_userservice.py`
<!-- time estimate: 15 min -->
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Prüfhilfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
