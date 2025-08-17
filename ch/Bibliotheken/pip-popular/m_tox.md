title: "'tox': automatisierte Tests in virtuellen Umgebungen"
stage: draft
timevalue: 1.5
difficulty: 3
assumes: pip, venv, m_pytest, pytest-Methodik-Blackbox
---

[SECTION::goal::trial]

Ich kann das Python-Paket `tox` verwenden, um Tests automatisiert in verschiedenen virtuellen
Umgebungen auszuführen.

[ENDSECTION]

[SECTION::background::default]

Moderne Python-Projekte müssen oft auf verschiedenen Python-Versionen funktionieren und mit
unterschiedlichen Abhängigkeiten getestet werden.
Außerdem sollen Tests in einer sauberen, isolierten Umgebung laufen, um sicherzustellen,
dass keine lokalen Installationen die Ergebnisse verfälschen.
Das manuelle Erstellen und Verwalten multipler virtueller Umgebungen ist mühsam und fehleranfällig.

[`tox`](https://tox.wiki/) automatisiert genau diesen Prozess: Es erstellt automatisch virtuelle
Umgebungen, installiert Abhängigkeiten und führt Tests aus - und das für beliebig viele
Python-Versionen und Konfigurationen parallel.

[ENDSECTION]

[SECTION::instructions::loose]

Benutzen Sie bei Bedarf die [Dokumentation von `tox`](https://tox.wiki/).

### Installation und Vorbereitung

- [ER] Installieren Sie `tox` mittels [PARTREF::pip].
- [ER] Erstellen Sie einen neuen Ordner `tox_example` und wechseln Sie in diesen.
- [ER] Erstellen Sie eine einfache Python-Datei `calculator.py` mit folgenden Funktionen:

```python
def add(a, b):
    """Addiert zwei Zahlen."""
    return a + b

def multiply(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b

def divide(a, b):
    """Dividiert zwei Zahlen."""
    if b == 0:
        raise ValueError("Division durch Null ist nicht erlaubt")
    return a / b
```

- [ER] Erstellen Sie eine Testdatei `test_calculator.py` mit pytest-Tests für diese Funktionen:

```python
import pytest
from calculator import add, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
```

### Grundlegende tox-Konfiguration

[ER] Erstellen Sie eine `tox.ini` Datei im Projektordner mit folgendem Grundgerüst:

```ini
[tox]
envlist = py39, py310, py311

[testenv]
deps = pytest
commands = pytest test_calculator.py -v
```

- [ER] Führen Sie `tox` aus und beobachten Sie, was passiert.
- [EQ] Welche Umgebungen werden erstellt? Was passiert, wenn eine Python-Version nicht installiert ist?
- [EQ] Wo befinden sich die erstellten virtuellen Umgebungen und wie heißen sie?

### Tox-Umgebungen erkunden

[ER] Führen Sie folgende Kommandos aus und beschreiben Sie die Ausgabe:

- `tox -l` (oder `tox --list`)
- `tox -e py39` (nur eine bestimmte Umgebung)
- `tox -r` (recreate - Umgebungen neu erstellen)

[EQ] Was ist der Unterschied zwischen den ersten beiden Kommandos?

### Abhängigkeiten hinzufügen

[ER] Erstellen Sie eine `requirements.txt` Datei:

```
pytest>=6.0
requests>=2.25.0
```

[ER] Erweitern Sie die `tox.ini` um diese Abhängigkeiten:

```ini
[tox]
envlist = py39, py310, py311

[testenv]
deps = -r{toxinidir}/requirements.txt
commands = pytest test_calculator.py -v
```

[ER] Erstellen Sie einen neuen Test in `test_calculator.py`, der das `requests` Paket verwendet:

```python
import requests

def test_requests_available():
    """Test that requests is available in the environment."""
    response = requests.get('https://httpbin.org/get')
    assert response.status_code == 200
    assert 'headers' in response.json()
```

- [ER] Führen Sie `tox -r` aus, um die Umgebungen mit den neuen Abhängigkeiten neu zu erstellen.
- [EQ] Wie verhält sich tox, wenn Sie jetzt `tox` ohne `-r` ausführen? Warum?

### Mehrere Testkommandos

[ER] Erweitern Sie Ihre `tox.ini` um mehrere Kommandos:

```ini
[testenv]
deps = -r{toxinidir}/requirements.txt
commands = 
    python --version
    pip list
    pytest test_calculator.py -v --tb=short
```

- [ER] Führen Sie tox aus und analysieren Sie die Ausgabe.
- [EQ] Was zeigen die zusätzlichen Kommandos? Warum könnte das nützlich sein?

### Spezielle Umgebungen definieren

[ER] Fügen Sie spezielle Umgebungen zu Ihrer `tox.ini` hinzu:

```ini
[tox]
envlist = py39, py310, py311, lint, docs

[testenv]
deps = -r{toxinidir}/requirements.txt
commands = 
    python --version
    pytest test_calculator.py -v

[testenv:lint]
deps = flake8
commands = flake8 calculator.py test_calculator.py

[testenv:docs]
deps = 
commands = python -c "print('Dokumentation würde hier erstellt werden')"
```

- [ER] Führen Sie `tox -e lint` aus. Was passiert?
- [ER] Installieren Sie `flake8` in Ihrer lokalen Umgebung und führen Sie `tox -e lint` erneut aus.
- [EQ] Müssen Sie flake8 lokal installieren, damit es in der tox-Umgebung funktioniert? Erklären Sie!

### Fehlerbehandlung erkunden

[ER] Fügen Sie absichtlich einen Fehler in `calculator.py` ein (z.B. Syntaxfehler) und führen Sie `tox` aus.

- [EQ] Wie verhält sich tox bei Fehlern? Bricht es alle Umgebungen ab oder nur die betroffene?
- [EQ] Wo finden Sie detaillierte Fehlermeldungen?

[ER] Korrigieren Sie den Fehler wieder.

### Konfiguration verstehen

[ER] Experimentieren Sie mit verschiedenen Konfigurationsoptionen in der `tox.ini`:

```ini
[testenv]
deps = -r{toxinidir}/requirements.txt
changedir = {toxworkdir}
commands = 
    python --version
    pwd
    ls -la
    pytest {toxinidir}/test_calculator.py -v
```

- [EQ] Was bewirkt `changedir = {toxworkdir}`? 
- [EQ] Warum müssen Sie jetzt `{toxinidir}/test_calculator.py` statt nur `test_calculator.py` verwenden?

### Umgebungsvariablen und Vererbung

[ER] Erstellen Sie eine erweiterte Konfiguration:

```ini
[tox]
envlist = py39, py310, coverage

[testenv]
deps = -r{toxinidir}/requirements.txt
setenv = 
    PYTHONPATH = {toxinidir}
passenv = HOME
commands = pytest test_calculator.py -v

[testenv:coverage]
deps = 
    {[testenv]deps}
    pytest-cov
commands = pytest test_calculator.py --cov=calculator --cov-report=term-missing
```

- [ER] Führen Sie `tox -e coverage` aus.
- [EQ] Was bewirkt `{[testenv]deps}` in der coverage-Umgebung?
- [EQ] Welche Coverage-Informationen erhalten Sie?

### Parallele Ausführung

[ER] Installieren Sie `tox-parallel`: `pip install tox[parallel]`
[ER] Führen Sie `tox -p` aus und beobachten Sie das Verhalten.

- [EQ] Was ist der Unterschied zur normalen Ausführung? Welche Vor- und Nachteile sehen Sie?

### Projekt-Integration

[ER] Erstellen Sie eine `setup.py` oder `pyproject.toml` für Ihr Testprojekt:

**setup.py** Variante:
```python
from setuptools import setup

setup(
    name="calculator-example",
    version="0.1.0",
    py_modules=["calculator"],
    install_requires=[],
    extras_require={
        "test": ["pytest", "requests"],
    },
)
```

[ER] Anpassung der `tox.ini` für die Installation des eigenen Pakets:

```ini
[testenv]
deps = -r{toxinidir}/requirements.txt
commands = 
    pip install -e .
    pytest test_calculator.py -v
```

- [EQ] Welchen Vorteil hat die Installation mit `pip install -e .` in der tox-Umgebung?

[ENDSECTION]

[SECTION::submission::information,snippet]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Erste Schritte mit tox]

Die Studenten sollen verstehen:
- Wie tox virtuelle Umgebungen automatisch verwaltet
- Den Unterschied zwischen lokalen und tox-Umgebungen
- Grundlegende tox.ini Konfiguration
- Abhängigkeitsverwaltung mit tox
- Spezielle Umgebungen für verschiedene Zwecke

Typische Fallstricke:
- Python-Versionen nicht installiert → skip ist normal
- Pfad-Probleme bei changedir
- Verwirrung über lokale vs. tox-Abhängigkeiten

Mögliche Beispiel-Ausgaben:

[EREFQ::1] Bei `tox -l` sollten die konfigurierten Umgebungen aufgelistet werden:
py39, py310, py311, lint, docs, coverage

[EREFQ::2] Tox stoppt nur die betroffene Umgebung bei Fehlern, andere laufen weiter

[EREFQ::3] `{[testenv]deps}` erbt die Abhängigkeiten der Basis-Umgebung

[ENDINSTRUCTOR]
