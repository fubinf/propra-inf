title: "'tox': automatisierte Tests in virtuellen Umgebungen"
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: pip, venv, m_pytest, flake8
requires: pyenv
---

[SECTION::goal::trial]
Ich kann das Python-Paket `tox` verwenden, um Tests und andere Prüfwerkzeuge automatisiert
in verschiedenen virtuellen Umgebungen und unter mehreren Python-Versionen auszuführen.
[ENDSECTION]

[SECTION::background::default]
Python-Projekte müssen oft auf verschiedenen Python-Versionen funktionieren.
Außerdem sollen Tests in einer sauberen, isolierten Umgebung laufen, damit keine lokalen Installationen
die Ergebnisse verfälschen.
Mehrere virtuelle Umgebungen von Hand zu erstellen und aktuell zu halten, ist mühsam und fehleranfällig.

[`tox`](https://tox.wiki/) automatisiert genau das: Es erstellt virtuelle Umgebungen, installiert
Abhängigkeiten und führt Tests oder andere Werkzeuge darin aus – für beliebig viele
Python-Versionen und Konfigurationen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Wozu tox?

Lesen Sie in der tox-Dokumentation die Abschnitte
[Overview und System overview](https://tox.wiki/en/stable/explanation.html#overview).

[EQ] Welche Arten von Werkzeugen kann tox für ein Projekt ausführen?
Welche Schritte führt tox für jede Umgebung nacheinander aus?

<!-- time estimate: 10 min -->

### Projekt vorbereiten

- Erstellen Sie einen neuen Ordner `tox_example` und wechseln Sie in diesen.
- In [PARTREF::pyenv] haben Sie Python 3.10 als globale Version eingestellt.
  Schalten Sie mit `pyenv global system` wieder auf Ihr System-Python zurück
  und ermitteln Sie mit `python3 --version` dessen Version (z. B. 3.13).
- Legen Sie wie in [PARTREF::venv] eine virtuelle Umgebung `.venv` an, aktivieren Sie sie
  und installieren Sie `tox` darin mittels [PARTREF::pip].
- Machen Sie im Ordner die beiden Python-Versionen aus [PARTREF::pyenv] und Ihr System-Python verfügbar:
  `pyenv local 3.10.17 3.11.12 system` _(Patchnummern ggf. anpassen)_.

[HINT::Warum brauche ich `pyenv local` mit mehreren Versionen?]
tox sucht die Interpreter über Namen wie `python3.10` im `PATH`.
Die Platzhalter-Programme (shims) von `pyenv` funktionieren aber nur für Versionen,
die gerade aktiviert sind.
Mit `pyenv local` können Sie mehrere Versionen gleichzeitig aktivieren.
Ihre aktivierte `.venv` bleibt davon unberührt, weil sie im `PATH` vor den shims steht.
[ENDHINT]

[HINT::`pip install tox` meldet "externally-managed-environment"]
Sie versuchen, ins System-Python zu installieren.
Aktivieren Sie zuerst Ihre `.venv` (`source .venv/bin/activate`).
[ENDHINT]

Erstellen Sie die Datei `calculator.py`:
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

Erstellen Sie die Testdatei `test_calculator.py`:
```python
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
```

<!-- time estimate: 10 min -->

### Die erste `tox.ini`

tox liest seine Konfiguration aus der Datei `tox.ini` im Projektordner.
Erstellen Sie sie mit folgendem Inhalt und ersetzen Sie dabei `py3XX` durch Ihre System-Version
(z. B. `py313` für Python 3.13):
```ini
[tox]
envlist = py38, py310, py311, py3XX

[testenv]
deps = pytest
commands = pytest test_calculator.py -v
```

`envlist` nennt die Umgebungen, die ein einfaches `tox` ausführt.
Wie tox aus einem Namen wie `py310` die Python-Version ableitet, steht unter
[Environment names and Python versions](https://tox.wiki/en/stable/tutorial/getting-started.html#environment-names-and-python-versions).
Python 3.8 haben Sie absichtlich _nicht_ installiert.

Führen Sie `tox` aus und betrachten Sie vor allem die Zusammenfassung am Ende der Ausgabe.

[EQ] Welche Umgebungen laufen erfolgreich, welche nicht?
Mit welcher Meldung scheitert `py38`, und wie lautet das Gesamtergebnis?

[HINT::Auch `py310` oder `py311` scheitern mit "could not find python interpreter"]
tox findet die pyenv-Versionen nicht.
Prüfen Sie mit `python3.10 --version` im Projektordner, ob der Aufruf funktioniert.
Falls nicht, haben Sie `pyenv local` nicht im Projektordner ausgeführt
oder die Patchnummern passen nicht zu `pyenv versions`.
[ENDHINT]

Ergänzen Sie im Abschnitt `[tox]` die Zeile `skip_missing_interpreters = true`
(siehe [`skip_missing_interpreters`](https://tox.wiki/en/stable/reference/config.html#skip_missing_interpreters))
und führen Sie `tox` erneut aus.

[EQ] Was ändert sich an der Zusammenfassung und am Gesamtergebnis?
In welcher Situation wäre diese Einstellung gefährlich, weil sie ein Problem verdeckt?

Schauen Sie sich nun den Ordner `.tox` in Ihrem Projektordner an.

[EQ] Welche Unterordner gibt es darin, und was enthält ein solcher Unterordner (z. B. `.tox/py311`)?
Womit aus [PARTREF::venv] ist das vergleichbar?

<!-- time estimate: 20 min -->

### Einzelne Umgebungen

Führen Sie `tox -l` und `tox -e py311` aus
(siehe [Listing available environments](https://tox.wiki/en/stable/tutorial/getting-started.html#listing-available-environments)).

[EQ] Was tun die beiden Kommandos jeweils?
Wann ist `-e` im Alltag nützlich?

<!-- time estimate: 5 min -->

### Abhängigkeiten

Bisher installiert tox nur `pytest`.
Wir wollen zusätzlich die Testabdeckung messen, also welche Codezeilen die Tests ausführen.
Das leistet das pytest-Plugin `pytest-cov`.

Erstellen Sie eine `requirements.txt`:
```text
pytest
pytest-cov
```

Ändern Sie den Abschnitt `[testenv]` Ihrer `tox.ini`:
```ini
[testenv]
deps = -r{toxinidir}/requirements.txt
commands = pytest test_calculator.py -v --cov=calculator --cov-report=term-missing
```

`{toxinidir}` ist eine tox-Variable für das Verzeichnis, in dem die `tox.ini` liegt.
Führen Sie `tox` aus, und zwar _ohne_ `-r` (`--recreate`).
Führen Sie es danach gleich noch einmal aus.
Lesen Sie dann
[Dependency change detection](https://tox.wiki/en/stable/explanation.html#dependency-change-detection).

[EQ] Woran erkennen Sie in der Ausgabe des ersten Laufs, dass tox die neue Abhängigkeit installiert hat,
und was ist beim zweiten Lauf anders?
Wann braucht man `tox -r` überhaupt noch?

Die Spalte `Missing` im Coverage-Bericht nennt die Zeilen von `calculator.py`, die kein Test ausführt.

[ER] Ergänzen Sie in `test_calculator.py` einen Test `test_divide_by_zero`,
der mit `pytest.raises` prüft, dass `divide(5, 0)` einen `ValueError` auslöst,
sodass `calculator.py` zu 100 % abgedeckt ist.

<!-- time estimate: 15 min -->

### Eine Umgebung für den Linter

tox kann nicht nur Tests ausführen, sondern beliebige Prüfwerkzeuge,
also neben [TERMREF::Dynamische analytische Qualitätssicherung]
auch [TERMREF::Statische analytische Qualitätssicherung].

Ergänzen Sie Ihre `tox.ini` um eine Umgebung für [PARTREF::flake8]
und nehmen Sie diese in die `envlist` auf:
```ini
[tox]
envlist = py38, py310, py311, py3XX, lint
skip_missing_interpreters = true

[testenv:lint]
deps = flake8
commands = flake8 calculator.py test_calculator.py
```

Der Abschnitt `[testenv]` bleibt wie bisher.
Führen Sie `tox -e lint` aus.
Prüfen Sie außerdem mit `flake8 --version` direkt in Ihrer Shell (außerhalb von tox),
ob `flake8` dort überhaupt verfügbar ist.

[EQ] Wieso funktioniert `tox -e lint` unabhängig davon, ob `flake8` in Ihrer Shell installiert ist?
Welche Python-Version verwendet die `lint`-Umgebung?

<!-- time estimate: 10 min -->

### Ein Fehlschlag

Bauen Sie absichtlich einen Syntaxfehler in `calculator.py` ein
(z. B. den Doppelpunkt hinter `def add(a, b)` löschen) und führen Sie `tox` aus.

[EQ] Welche Umgebungen schlagen fehl, einschließlich `lint`?
Bricht tox nach der ersten fehlgeschlagenen Umgebung ab?

[EQ] tox protokolliert jeden Schritt zusätzlich in Dateien.
In welchem Verzeichnis liegen diese Protokolle für `py311`, und wie sind die Dateien benannt?

Korrigieren Sie den Fehler wieder.

<!-- time estimate: 10 min -->

### Arbeitsverzeichnis und externe Kommandos

Standardmäßig führt tox die Kommandos im Projektordner aus.
Mit [`changedir`](https://tox.wiki/en/stable/reference/config.html#changedir)
lässt sich das ändern, etwa damit Tests nicht versehentlich von Dateien im Projektordner abhängen.
Ändern Sie den Abschnitt `[testenv]` wie folgt:
```ini
[testenv]
deps = -r{toxinidir}/requirements.txt
changedir = {envtmpdir}
commands =
    pwd
    pytest {toxinidir}/test_calculator.py -v --cov=calculator --cov-report=term-missing
```

Führen Sie `tox -e py311` aus.

[EQ] Mit welcher Meldung scheitert die Umgebung?
Lesen Sie zu [`allowlist_externals`](https://tox.wiki/en/stable/reference/config.html#allowlist_externals)
nach: Welches Problem soll tox verhindern, indem es solche Kommandos standardmäßig ablehnt?

Ergänzen Sie im Abschnitt `[testenv]` die Zeile `allowlist_externals = pwd` und führen Sie `tox -e py311` erneut aus.

[EQ] Welches Verzeichnis gibt `pwd` aus?
Warum steht beim `pytest`-Aufruf jetzt `{toxinidir}/test_calculator.py` statt nur `test_calculator.py`?

Führen Sie nun `tox -e lint` aus.

[EQ] Warum schlägt `lint` jetzt fehl, obwohl Sie `[testenv:lint]` gar nicht geändert haben?
Beheben Sie das Problem mit einer zusätzlichen Zeile in `[testenv:lint]`.

[ER] Ihre finale `tox.ini` führt mit `tox` alle Umgebungen außer der nicht vorhandenen `py38` erfolgreich aus.

<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::information,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
Reichen Sie `tox.ini` und `test_calculator.py` ein.
[ENDSECTION]

[INSTRUCTOR::Erste Schritte mit tox]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
