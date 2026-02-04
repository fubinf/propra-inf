title: "Pytest und tox: professionelles Test-Management"
stage: draft
timevalue: 0
difficulty: 4
assumes: m_pytest, pytest_parametrize, testcoverage, m_tox
---

[SECTION::goal::trial]

Ich kann `pytest` und `tox` zusammen verwenden, um professionelle Test-Suites zu erstellen,
die verschiedene Python-Versionen, Coverage-Berichte, Linting und CI/CD-Vorbereitung umfassen.

[ENDSECTION]

[SECTION::background::default]

In professionellen Python-Projekten reicht es nicht, Tests nur lokal auszuführen.
Man muss sicherstellen, dass:

- Tests auf verschiedenen Python-Versionen funktionieren
- Die Code-Coverage hoch ist und überwacht wird
- Code-Quality-Standards eingehalten werden
- Tests isoliert und reproduzierbar sind
- Die Test-Umgebung der späteren Produktionsumgebung ähnelt

[`tox`](https://tox.wiki/) in Kombination mit [`pytest`](https://docs.pytest.org/) bietet
eine mächtige Lösung für all diese Anforderungen. Aufbauend auf den Grundlagen aus
[PARTREF::m_tox] werden wir hier fortgeschrittene pytest-spezifische Tox-Features erkunden.

[ENDSECTION]

[SECTION::instructions::loose]

Benutzen Sie bei Bedarf die [Dokumentation von `tox`](https://tox.wiki/), 
[pytest](https://docs.pytest.org/) und [MechanicalSoup](https://mechanicalsoup.readthedocs.io/).

### Projekt-Setup: MechanicalSoup Repository für pytest+tox-Testing

Wir werden mit dem echten [MechanicalSoup](https://github.com/MechanicalSoup/MechanicalSoup)
Repository arbeiten und dessen Test-Infrastruktur erweitern und analysieren.
MechanicalSoup ist eine professionelle Python-Bibliothek für Web-Scraping und
Formular-Automatisierung mit einer ausgezeichneten Test-Suite.

[ER] Klonen Sie das MechanicalSoup Repository in der folgenden spezifischen Version: `1.3.0`

[ER] Erstellen Sie einen neuen Branch für Ihre Erweiterungen:

Verschaffen Sie sich vorab einen Überblick über diese Bibliothek,
mit dem Sie in dieser Aufgabe arbeiten sollen.
Analysieren Sie die vorhandene Projektstruktur.
Sie sollten folgende Struktur vorfinden.

```sh
MechanicalSoup/
├── .github/                        # GitHub Actions CI/CD Workflows
├── assets/                         # Projekt-Assets
├── mechanicalsoup/                 # Hauptbibliothek
│   ├── __init__.py                 # Package-Initialisierung, Version
│   ├── stateful_browser.py         # StatefulBrowser-Hauptklasse
│   ├── browser.py                  # Browser-Basisklasse
│   ├── form.py                     # Formular-Handling
│   └── utils.py                    # Hilfsfunktionen
├── tests/                          # Vorhandene Test-Suite
│   ├── requirements.txt            # Test-Abhängigkeiten
│   ├── test_browser.py             # Tests für Browser-Klasse
│   ├── test_stateful_browser.py    # Tests für StatefulBrowser
│   ├── test_form.py                # Formular-Tests
│   ├── utils.py                    # Test-Hilfsfunktionen
│   └── setpath.py                  # Pfad-Setup für Tests
├── examples/                       # Anwendungsbeispiele
├── docs/                           # Dokumentationen
├── .coveragerc                     # Coverage-Konfiguration
├── .gitignore                      # Git-Ausschlüsse
├── .mention-bot                    # GitHub Bot-Konfiguration
├── MANIFEST.in                     # Package-Manifest für setup.py
├── LICENSE                         # MIT-Lizenz
├── CONTRIBUTING.rst                # Contribution-Guidelines
├── setup.py                        # Package-Setup und -Metadaten
├── setup.cfg                       # Setup-Konfiguration
├── requirements.txt                # Laufzeit-Abhängigkeiten
└── README.rst                      # Projekt-Dokumentation
```

[EQ] Entdecken Sie auf dem ersten Blick etwas, das ungewohnt / unbekannt für Sie ist oder eventuell
sogar vermissen bzw. erwartet haben?

### Bestehende Test-Infrastruktur analysieren

Sie sollen ja nicht nur schauen, sondern auch etwas mit dem Repository machen.
Daher sollten Sie das Projekt auch lokal zum laufen bringen.
Zunächst müssen Sie die benötigten Abhängigkeiten bereitstellen.

[ER] Installieren Sie die Entwicklungsabhängigkeiten:

[HINT::Parameter]
Ziehen Sie `pip` mit dem Parameter in Betracht, der die Editierbarkeit berücksichtigt.
[ENDHINT]

Wir beschäftigen uns in diesem Kapitel mit der Qualität einer Softwarelösung,
daher sind Sie natürlich ersteinmal an den Entwicklertests interessiert.

[ER] Führen Sie die vorhandene Test-Suite aus.

[ER] Analysieren Sie die CI/CD-Konfiguration.

[NOTICE]
MechanicalSoup v1.3.0 hat **keine** _tox.ini_-Datei. Die Multi-Python-Version-Tests werden über GitHub Actions durchgeführt.
[ENDNOTICE]

[EQ] Welche Python-Versionen werden in den GitHub Actions getestet?

[EQ] Wie unterscheidet sich das von einer tox-basierten Konfiguration?

### Erweiterte Test-Szenarien entwickeln

[ER] Erstellen Sie eine neue Datei `tests/test_learning_scenarios.py` mit **pedagogischen** Tests.

Diese Tests dienen dem **Lernen von pytest-Konzepten**, nicht der Funktionalitätserweiterung:

**1. TestPytestBasics:**

- Test für pytest Fixtures (erstellen Sie eine `sample_browser` Fixture)
- Test für pytest Parametrisierung (testen Sie verschiedene HTML-Parser)
- Test für pytest Markers (markieren Sie Tests als `@pytest.mark.slow`)

**2. TestMockingAndFakes:**

- Test mit `open_fake_page()` vs. echten HTTP-Requests (Vergleich)
- Test mit `unittest.mock` für externe Dependencies
- Test für verschiedene HTML-Strukturen (valid/invalid)

**3. TestAssertionPatterns:**

- Test für verschiedene pytest Assertion-Stile
- Test für Exception-Handling mit `pytest.raises()`
- Test für ungefähre Werte mit `pytest.approx()` (z.B. Performance-Zeiten)

[HINT::pytest Fixtures Beispiel]
Erstellen Sie wiederverwendbare Test-Komponenten:

```python
@pytest.fixture
def sample_browser():
    """Fixture für einen konfigurierten Browser."""
    return mechanicalsoup.StatefulBrowser(user_agent="Learning/1.0")

def test_fixture_usage(sample_browser):
    assert sample_browser.session.headers['User-Agent'] == "Learning/1.0"
```

[ENDHINT]

[HINT::Parametrisierung und Mocking]
Siehe [pytest Parametrize](https://docs.pytest.org/en/stable/how.html#parametrize) für Daten-getriebene Tests und [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) für Test-Doubles.
[ENDHINT]

[EQ] Welche Herausforderungen ergeben sich beim Testen von Web-Scraping-Bibliotheken?

[EQ] Wie können Sie Tests schreiben, die sowohl lokal als auch in CI/CD-Umgebungen funktionieren?

### Performance-Tests mit pytest-benchmark

[ER] Installieren Sie pytest-benchmark und führen Sie Performance-Tests aus.

[EQ] Welche Performance-Charakteristika können Sie für die Browser-Erstellung messen?

### Coverage-Analyse erweitern

[ER] Führen Sie eine detaillierte Coverage-Analyse durch.

[ER] Öffnen Sie den HTML-Coverage-Report und analysieren Sie.

[EQ] Welche Module haben die niedrigste Coverage? Welche Bereiche sind nicht getestet?

### Tox.ini

Da MechanicalSoup v1.3.0 keine tox.ini hat (zufälle gibt`s), erstellen wir eine eigene in dieser Lernübung.

[ER] Erstellen Sie eine eigene `tox.ini` für das MechanicalSoup-Projekt:

Ihre `tox.ini` sollte folgende Umgebungen und Konfigurationen enthalten:

1. Basis-Konfiguration:

   - `envlist` mit Python-Versionen: py39, py310, py311, py312
   - Zusätzliche Umgebungen: lint, coverage, benchmark  
   - `isolated_build = true` für moderne Python-Pakete

2. Standard-Testumgebung `[testenv]`:

   - Dependencies: pytest, pytest-benchmark, requests, beautifulsoup4
   - Kommando: `pytest tests/ -v --tb=short`

3. Coverage-Umgebung `[testenv:coverage]`:

   - Erbt von `[testenv]`, zusätzlich pytest-cov
   - Kommando mit Coverage-Report: HTML und Terminal
   - Coverage-Threshold: mindestens 85%

4. Linting-Umgebung `[testenv:lint]`:

   - Tools: flake8, black, isort
   - Überprüft Code-Style in mechanicalsoup/ und tests/
   - Ausschluss: tests/setpath.py (Legacy-Datei)

5. Benchmark-Umgebung `[testenv:benchmark]`:

   - Für Performance-Tests mit pytest-benchmark
   - Fokus auf Ihre pytorch-Lern-Tests

[HINT::tox.ini Struktur]
Orientieren Sie sich an der [tox-Dokumentation](https://tox.wiki/en/latest/config.html) für Syntax-Details:

```ini
[tox]
envlist = # Komma-separierte Liste
isolated_build = true

[testenv]
deps = 
    # Dependencies hier
commands = 
    # Test-Kommandos

[testenv:spezial]
deps = 
    {[testenv]deps}  # Erbt Standard-Dependencies
    # zusätzliche Dependencies
commands = 
    # spezielle Kommandos
```

[ENDHINT]

[ER] Testen Sie die tox-Konfiguration:

[EQ] Welche Vorteile bietet tox gegenüber dem direkten Ausführen von pytest?

### Pytest-Marker und Konfiguration erweitern

[ER] Erweitern Sie die bestehende Pytest-Konfiguration durch eine `pytest.ini`:

```ini
[tool:pytest]
testpaths = tests
addopts = 
    --strict-markers
    --tb=short
    -v
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    benchmark: marks tests as performance benchmarks
    network: marks tests that require network access
    edge_case: marks tests for edge cases
    unit: marks tests as unit tests
```

[EQ] Warum ist es wichtig, Test-Marker zu definieren und zu verwenden?

[ER] Führen Sie verschiedene Test-Szenarien aus:

[EQ] Führen Sie folgende Kommandos aus und analysieren Sie die Ergebnisse:

1. `pytest --collect-only` - Wie viele Tests werden gesammelt?
2. `pytest -m "slow" --collect-only` - Wie viele langsame Tests gibt es?
3. `pytest --benchmark-only` - Welche Performance-Metriken werden erfasst?

[EQ] Welche Verbesserungen würden Sie an der bestehenden MechanicalSoup-Test-Suite vorschlagen?

[EQ] Reflektieren Sie: Welche Erkenntnisse haben Sie über professionelle Test-Infrastrukturen gewonnen?

[ENDSECTION]

[SECTION::submission::information,snippet]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
