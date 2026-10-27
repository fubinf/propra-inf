title: Unittests
---
Unit-Tests sind automatisierte Tests, die einzelne Komponenten einer Software isoliert prüfen.
Sie bilden das Fundament jeder professionellen Testpyramide: schnell, granular und reproduzierbar.

In dieser Taskgroup lernen Sie zunächst Pythons Standard-Testframework `unittest`,
dann das leistungsfähigere `pytest`-Ökosystem.
Aufbauend darauf werden systematische Testmethodik (Blackbox/Whitebox),
wichtige pytest-Features (Fixtures, Mocking, Parametrisierung)
sowie Test-Driven Development behandelt.

**Empfohlener Einstiegspfad:**
`m_unittest` → `m_pytest` → `pytest_call` → thematische Vertiefung nach Interesse

## Thematische Übersicht

### Grundlagen

- **m_unittest.md**: Einführung in Pythons Standard-Testframework `unittest`.
  Ausgangspunkt für alle weiteren Tasks in dieser Gruppe.
- **m_pytest.md**: Wechsel auf `pytest`, das leistungsfähigere Framework der professionellen Praxis.
  Setzt `m_unittest.md` voraus und ist Grundlage für alle weiteren pytest-Tasks.

### Teststruktur & Methodik

- **pytest_aaa.md**: Das Arrange-Act-Assert-Muster als strukturierende Konvention für lesbare Unit-Tests.
  Setzt `m_pytest.md` und `pytest_call.md` voraus.
- **pytest_parametrize.md**: Tabellengesteuerte Tests mit `@pytest.mark.parametrize`.
  Setzt `m_pytest.md` voraus; Grundlage für Blackbox-Testing.
- **pytest-Methodik-Blackbox.md**: Systematisches Blackbox-Testing mit Äquivalenzklassen und Randwertanalyse.
  Setzt `m_pytest.md` und `pytest_parametrize.md` voraus.
- **pytest-Methodik-Whitebox.md**: Whitebox-Testmethodik und strukturierte Testfallableitung aus dem Quellcode.
  Setzt `pytest-Methodik-Blackbox.md` voraus.

### pytest-Features

- **pytest_call.md**: Steuerung der Testausführung – Selektion, Konfiguration, Kommandozeilenoptionen.
  Setzt `m_pytest.md` voraus.
- **pytest_fixtures.md**: Wiederverwendbare Vor- und Nachbedingungen mit pytest-Fixtures.
  Setzt `m_pytest.md` voraus.
- **pytest_mocking.md**: Abhängigkeiten mit `unittest.mock` isolieren und ersetzen.
  Setzt `m_pytest.md` voraus.
- **pytest_mocking_freezegun.md**: Zeitabhängige Tests mit der `freezegun`-Bibliothek.
  Setzt `pytest_mocking.md` und `pytest_aaa.md` voraus.

### Werkzeuge & Integration

- **pytest_plugin_linter_flake8.md**: Code-Qualitätsprüfung mit dem Flake8-Plugin direkt in pytest.
  Setzt `pytest_call.md` und die externe Task
  [`flake8.md`](../../Werkzeuge/Linter/flake8.md) voraus.

### Test-Driven Development

- **tdd.md**: Einführung in Test-Driven Development am Beispiel FizzBuzz mit pytest.
  Setzt `m_pytest.md` voraus.

### In Entwicklung

Diese Tasks sind noch nicht veröffentlicht (`stage: draft`) und werden künftig verfügbar sein:

- **testcoverage.md**: Code Coverage mit `pytest-cov` messen, interpretieren und kritisch bewerten.
  Setzt `pytest_call.md` und `pytest-Methodik-Blackbox.md` voraus.
- **tdd_pp.md**: TDD im Pair Programming. Setzt `tdd.md` voraus.
- **pytest_benchmark.md**: Performance-Benchmarks mit `pytest-benchmark`. Setzt `pytest_fixtures.md` voraus.
- **pytest_tox.md**: Eine fremde Test-Suite (MechanicalSoup) mit `tox` so ausführen wie deren CI,
  Fehlschläge per Umgebungsmatrix auf Code oder Abhängigkeitsversion zurückführen
  und erkennen, ob die Tests den Quellcode oder das installierte Paket prüfen.
  Setzt `m_pytest.md` sowie die externen Tasks
  [`flake8.md`](../../Werkzeuge/Linter/flake8.md),
  [`m_tox.md`](../../Bibliotheken/pip-popular/m_tox.md) und
  [`pyenv.md`](../../Werkzeuge/Paketmanager/pyenv.md) voraus.
- **pytest_mutation_testing.md**: Mutation Testing mit `mutmut` zur Qualitätsbewertung von Tests.
  Setzt `m_pytest.md` und `pytest-Methodik-Blackbox.md` voraus.
- **pytest-Methodik-REST.md**: Blackbox-Testing einer REST-API über den CRUD-Lebenszyklus.
  Setzt `pytest-Methodik-Blackbox.md`, `m_requests.md`, `m_json.md` und `http-REST.md` voraus.
- **pytest_bugsinpy.md**: Reale Defekte aus der Sammlung BugsInPy (PySnooper, FastAPI) nachstellen,
  defektaufdeckende Tests erkennen und mit `TestClient` selbst einen Regressionstest schreiben.
  Setzt `m_pytest.md` sowie die externen Tasks
  [`Fehler-Defekt-Versagen.md`](../Testgrundlagen/Fehler-Defekt-Versagen.md),
  [`flake8.md`](../../Werkzeuge/Linter/flake8.md) und
  [`FastAPI-GET.md`](../../Bibliotheken/Frameworks/FastAPI-GET.md) voraus.
- **m_doctest.md**: Ausführbare Beispiele in Docstrings mit dem Standardmodul `doctest` schreiben
  und mit `pytest --doctest-modules` zusammen mit gewöhnlichen Tests ausführen.
  Setzt `m_pytest.md` voraus.
- **m_hypothesis.md**: Eigenschaftsbasiertes Testen mit `hypothesis`:
  Eigenschaften formulieren, die für alle gültigen Eingaben gelten,
  und von `hypothesis` gefundene und verkleinerte Gegenbeispiele auswerten.
  Setzt `m_pytest.md`, `pytest_parametrize.md` und `pytest-Methodik-Blackbox.md` voraus.
