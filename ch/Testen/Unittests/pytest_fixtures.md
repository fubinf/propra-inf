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
Oftmals benötigt ein Test, dass bestimmte Voraussetzungen hergestellt werden.

[TERMREF::Fixture] sind ein zentrales Konzept in pytest, das es ermöglicht,
wiederverwendbaren Code zur Vor- und Nachbereitung (Setup und Teardown) von Tests bereitzustellen.
Gerade bei vielen Tests wird dabei schnell sichtbar, wie nützlich es ist,
Setup- und Testlogik sauber zu trennen.
In dieser Aufgabe lernen Sie deshalb Schritt für Schritt, wie Sie dieselben Voraussetzungen
für mehrere Tests wiederverwenden, wie Sie ihre Lebensdauer steuern und wie Sie
beim Arbeiten mit gemeinsamen Ressourcen die richtige Aufräumlogik einbauen.
[ENDSECTION]


[SECTION::instructions::detailed]
Nutzen Sie die folgende Übersicht parallel zum Bearbeiten der Aufgaben:

[pytest-Doku: How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

Wir betrachten zuerst das Grundlegende.
In diesem Abschnitt geht es um einen sehr einfachen Fall: Ein Test braucht ein Objekt,
das mehrfach verwendet wird. Statt den gleichen Setup-Code in jedem Test zu wiederholen,
werden wir ihn einmal als Fixture definieren und dann als Abhängigkeit deklarieren.

### Das Problem ohne Fixtures
<!-- time estimate: 5 min -->

Betrachten Sie zunächst diesen kleinen Test für einen Benutzer-Dienst. Der Code ist bewusst
noch etwas unordentlich, damit Sie das Problem direkt sehen können.

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


def test_user_registration():
    service = PseudoUserservice()

    # Setup
    service.register("alice", "alice@test.com", "password123")

    # Test
    result = service.login("alice", "password123")
    assert result.success

    # Cleanup
    service.users.clear()


def test_user_login():
    service = PseudoUserservice()

    # Setup
    service.register("alice", "alice@test.com", "password123")

    # Test
    result = service.login("alice", "password123")
    assert result.success

    # Cleanup
    service.users.clear()
```

[EQ] Welche Probleme erkennen Sie in diesem Code? Notieren Sie mindestens drei Probleme.

### Das Fixture-Konzept entdecken
<!-- time estimate: 10 min -->

pytest löst genau diese Schwächen mit sogenannten "Fixtures".

Ein Fixture ist im Grunde ein wiederverwendbares Setup, das ein Test als Abhängigkeit
anfordern kann. Statt in jedem Test denselben Initialisierungscode neu zu schreiben, definieren
Sie ihn einmal und referenzieren ihn dann über die Test-Signatur.

Das hat zwei Vorteile: Der eigentliche Test wird viel lesbarer, weil die Abhängigkeiten sofort
sichtbar sind, und die Einrichtung bleibt an einer Stelle zentralisiert.

Erstellen Sie die Datei `test_userservice.py` und implementieren Sie die folgenden Tests
mit einer einfachen Klasse:

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

def test_user_registration():
    service = PseudoUserservice()
    result = service.register("alice", "alice@test.com", "password123")
    assert result.success

def test_user_login():
    service = PseudoUserservice()
    service.register("alice", "alice@test.com", "password123")  # Pre-condition
    result = service.login("alice", "password123")
    assert result.success
```

### Setup deklarativ machen
<!-- time estimate: 15 min -->

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

[ER] Ergänzen Sie Ihre `test_userservice.py` um diese Fixture, und modifizieren Sie beide Tests,
um die Fixture zu nutzen.

Ein Test kann auch mehrere Fixtures gleichzeitig verwenden: Sie einfach als mehrere Parameter
in der Signatur auflisten.
Suchen Sie in der oben verlinkten pytest-Doku nach dem Abschnitt
„A test/fixture can request more than one fixture at a time“ und lesen Sie ihn.

Zum Beispiel:

```python
@pytest.fixture
def credentials():
    return {"email": "alice@test.com", "password": "secret"}

def test_login(user_service, credentials):
    user_service.register("alice", credentials["email"], credentials["password"])
    result = user_service.login("alice", credentials["password"])
    assert result.success
```

[EQ] Stellen Sie sich eine Testdatei mit Dutzenden Tests vor, die verschiedene Kombinationen
von Fixtures verwenden.
Welchen Vorteil hat es, wenn alle benötigten Fixtures als Parameter in der Signatur stehen?

### Fixture Scopes: wann welcher?
<!-- time estimate: 25 min -->

Manche Fixtures sind aufwendig: Eine Datenbankverbindung aufzubauen, Testdaten zu laden oder
einen Server zu starten kann Sekunden dauern. Das ist genau der Fall, in dem es relevant wird,
wie lange ein Fixture lebt.

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

Die allgemeine Faustregel ist unkompliziert: Behalten Sie in der Regel `function` bei. Nutzen Sie
einen größeren Scope nur dann, wenn das Setup wirklich teuer ist und der gemeinsame Zustand
bewusst kontrolliert werden kann. Wenn ein Test zu viele Zustandsänderungen hinterlässt, ist
`function` die sichere Standardwahl.

Ein sinnvoller Fall für einen größeren Scope ist zum Beispiel das einmalige Laden einer großen
Konfigurationsdatei oder eines Testdaten-Containers: Das ist aufwendig, aber danach nur lesbar.

```python
@pytest.fixture(scope="session")
def app_config():
    return load_big_test_config()
```

Wenn Sie einen größeren Scope wählen, müssen Sie selbst dafür sorgen, dass der Zustand zwischen
den Tests sauber zurückgesetzt wird. Die gemeinsame Nutzung hat nur dann Sinn, wenn die Ressource
unverändert bleibt oder bewusst wieder in einen Ausgangszustand gebracht wird.

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
Im `function`-Scope bekommt jeder Test eine frische Instanz – Zustandsänderungen eines Tests
sind für andere Tests unsichtbar.
Im `module`-Scope teilen sich alle Tests dieselbe Instanz: Wenn ein Test Nutzerdaten speichert
oder andere Zustandsänderungen vornimmt, sehen das alle nachfolgenden Tests ebenfalls.
Tests müssen deshalb so geschrieben sein, dass sie nicht auf Zustand angewiesen sind,
den ein anderer Test hinterlassen hat.
[ENDHINT]

Wenn Sie fertig sind, entfernen Sie `slow_service` und die drei zugehörigen Tests wieder,
damit der Rest der Datei nicht durch das `sleep()` ausgebremst wird.

### Setup und Teardown: Das Cleanup-Problem
<!-- time estimate: 30 min -->

Manche Tests erstellen Dateien, Datenbank-Einträge oder andere Ressourcen.
Was passiert, wenn diese nicht aufgeräumt werden?

Ein guter erster Gedanke ist: Für temporäre Dateien benutzen wir nicht manuell einen festen
Dateinamen im Arbeitsverzeichnis, sondern die Standard-Mechanismen von Python oder pytest.
Siehe auch [PARTREF::m_tempfile].

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

[EC] Führen Sie den folgenden Code aus: `pytest -v test_userservice.py`

[EQ] Was ist hier das Problem?

Wir könnten den Scope ändern, aber nehmen wir mal an, dass wir ihn für unsere Testsammlung an dieser
Stelle benötigen.
Dann ist die sauberere Lösung, die Datei nicht im Projektverzeichnis anzulegen, sondern ein eigenes
Verzeichnis für temporäre Testdaten zu verwenden. pytest bietet dafür `tmp_path` an, und das Modul
`tempfile` stellt ähnliche Mechanismen bereit. Siehe auch [PARTREF::m_tempfile].

```python
import pytest

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
    temp_file.write_text("Test war hier!")
    content = temp_file.read_text()
    print(f"Dateiinhalt: {content}")
    assert content == "Test war hier!"
```

[EQ] Warum ist `tmp_path` oder `tempfile` in diesem Fall besser als eine feste Datei im
Arbeitsverzeichnis? Welche Vorteile hat das für Wiederholbarkeit und sauberes Cleanup?

[EC] Verändern Sie jetzt absichtlich einen Test so, dass er fehlschlägt:

```python
def test_another_temp_file(temp_file):
    assert False
```

Führen Sie danach erneut `pytest -v test_userservice.py` aus.

[EQ] Welche Ausgabe sehen Sie in der pytest-Konsole? Wird der Cleanup im Fixture noch ausgeführt,
wenn der Test selbst fehlschlägt? Warum ist das wichtig?

### Fixtures teilen: conftest.py
<!-- time estimate: 15 min -->

Wenn Sie mehrere Testdateien haben, die dieselben Fixtures brauchen, gibt es dafür eine
praktische Lösung in pytest. Lassen Sie uns genau anschauen, wie das funktioniert.

Erstellen Sie eine Datei `conftest.py` mit geteilten Fixtures und der gemeinsam genutzten
Hilfsklasse:

```python
import pytest


class Result:
    def __init__(self, success):
        self.success = success


class PseudoUserservice:
    def __init__(self):
        self.users = {}
        print(f"Neuer UserService erstellt (ID: {id(self)})")

    def register(self, username, email, password):
        if username in self.users:
            return Result(False)
        self.users[username] = {'email': email, 'password': password}
        return Result(True)


@pytest.fixture
def fresh_user_service():
    """Frischer UserService für jeden Test."""
    return PseudoUserservice()
```

Erstellen Sie eine zweite Testdatei `test_sharing.py` und importieren Sie die gemeinsame Klasse
explizit:

```python
from conftest import PseudoUserservice


def test_in_other_file(fresh_user_service):
    assert isinstance(fresh_user_service, PseudoUserservice)
    result = fresh_user_service.register("bob", "bob@test.com", "pass")
    assert result.success
```

Damit gibt es die Klasse nur noch an einer Stelle. Die Fixture-Definition bleibt über pytest
automatisch sichtbar, aber die gemeinsame Test-Hilfsklasse wird nicht doppelt definiert.
Das macht das Beispiel leicht nachvollziehbar und vermeidet eine unnötige Verdopplung.

[EC] Führen Sie die beiden Dateien `test_userservice.py` und `test_sharing.py` mit pytest aus:
`pytest -v test_userservice.py test_sharing.py`

Wenn Sie den Test ausführen, sehen Sie, dass pytest die Fixture automatisch findet.
Die gemeinsame Klasse `PseudoUserservice` liegt aber nur noch an einer Stelle in `conftest.py`
und wird in `test_sharing.py` explizit importiert.

Folgendes haben Sie gerade beobachtet:

1. **Automatisches Laden:** pytest lädt automatisch alle `conftest.py` Dateien im aktuellen
   Verzeichnis und allen übergeordneten Verzeichnissen
2. **Fixture-Discovery:** pytest scannt diese `conftest.py`-Dateien nach `@pytest.fixture`-
   Dekoratoren und registriert sie global
3. **Namensauflösung:** Wenn ein Test einen Parameter `fresh_user_service` hat, sucht pytest
   automatisch nach einer gleichnamigen Fixture in
   (1) der gleichen Datei, (2) `conftest.py` im gleichen Verzeichnis,
   (3) `conftest.py` in übergeordneten Verzeichnissen, (4) eingebauten pytest-Fixtures.

Die Fixture selbst ist also über die pytest-Discovery sichtbar, ohne dass ein normaler
Python-Import notwendig ist. Die gemeinsame Hilfsklasse wird aber bewusst importiert, damit
es nicht zu einer zweiten, von der echten Klasse abweichenden Definition kommt.

Das ist ein guter Mittelweg für eine Einsteiger-Aufgabe: Die Abhängigkeit des Tests bleibt in
seiner Signatur sichtbar, und die gemeinsame Klasse wird nicht doppelt definiert.
Damit bleibt beides nachvollziehbar:
Das Setup ist klar sichtbar, aber die gemeinsame Hilfsklasse muss nicht
in jeder Datei erneut geschrieben werden.

[EQ] Warum kann die automatische Auflösung über `conftest.py` in einem übergeordneten Verzeichnis
plötzlich unangenehm werden, wenn ein Projekt wächst? Nennen Sie ein konkretes Beispiel für ein
Problem, das dadurch entstehen kann, und vergleichen Sie das mit einer expliziten Import-Variante.

### Eingebaute Fixtures verstehen
<!-- time estimate: 15 min -->

pytest bringt viele eingebaute Fixtures mit. Für diese Aufgabe sind vor allem zwei davon
relevant:

- `tmp_path`: Temporäre Dateien/Verzeichnisse für File-IO-Tests
- `capsys`: Output-Testing, Debug-Ausgaben validieren

Lesen Sie nach, was jede davon tut:
[Built-in fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html)

[EQ] Skizzieren Sie für jede der beiden ein Testszenario, in dem Ihnen der Einsatz sinnvoll erscheint.

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

[EC] Fügen Sie beide Tests zu `test_userservice.py` hinzu und führen Sie sie aus:
`pytest -v test_userservice.py`

### Reflexion: Wann und warum Fixtures?
<!-- time estimate: 5 min -->

Sie haben jetzt verschiedene Möglichkeiten kennengelernt, wie pytest beim Aufbau eines Tests
helfen kann. Denken Sie kurz darüber nach, wie das Ihr Vorgehen verändert:

[EQ] Fixtures verändern die Art, wie Sie über Tests nachdenken:
weg von "Setup-Code schreiben" hin zu "Dependencies deklarieren".
Die eigentliche Testlogik wird dadurch deutlich besser erkennbar.
Welcher Nachteil entsteht dadurch, dass das Setup nicht mehr direkt im Testrumpf steht?
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Prüfhilfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
