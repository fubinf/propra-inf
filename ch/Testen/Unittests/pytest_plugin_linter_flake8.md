title: "Pytest: Code-Qualität mit Flake8-Plugin prüfen"
stage: alpha
timevalue: 1.0
difficulty: 1
assumes: m_pytest, flake8, pytest_call
---

[SECTION::goal::idea]

- Ich kann das Flake8-Plugin für Pytest installieren und verwenden.
- Ich kann Code-Qualitätsprobleme mit Flake8 identifizieren und beheben.
- Ich kann Flake8-Konfigurationen anpassen und verstehen.

[ENDSECTION]
[SECTION::background::default]

Diese Aufgabe baut auf [PARTREF::flake8] auf und zeigt, wie Flake8 nahtlos in pytest-Workflows integriert werden kann.

Während Flake8 normalerweise als separates Kommandozeilen-Tool verwendet wird, ermöglicht das
`pytest-flake8`-Plugin die Integration von Code-Qualitätsprüfungen direkt in den Testprozess.
Das bedeutet, dass neben Ihren funktionalen Tests auch automatisch die Code-Qualität überprüft wird.

[ENDSECTION]
[SECTION::instructions::loose]

### Flake8-Plugin für pytest installieren

- [ER] Suchen Sie in der [offiziellen Pytest Plugin-Liste](https://docs.pytest.org/en/7.1.x/reference/plugin_list.html#plugin-list) nach dem Plugin `pytest-flake8`.
- [EQ] Wie viele weitere Plugins zu Flake finden sie?
- [ER] Installieren Sie das Plugin mit `pip install pytest-flake8`.
- [EC] Führen Sie `pip show pytest-flake8` aus und notieren Sie die installierte Version.

[HINT::Flake8 bereits installiert?]

Falls Sie [PARTREF::flake8] bereits bearbeitet haben, ist Flake8 bereits installiert.
Das Plugin nutzt die gleiche Flake8-Installation.

[ENDHINT]

### Testprojekt mit Code-Qualitätsproblemen erstellen

Erstellen Sie ein neues Verzeichnis `flake8_demo` und die folgenden Dateien:

- [ER] Erstellen Sie `demo_code.py` mit folgendem Inhalt:

```python
import sys
import os

def calculate_sum(a,b):
    unused_var = 42


    result = a+b
    return result

class Calculator:
    def __init__(self):
        pass
    def multiply(self, x, y):
        return x*y

if __name__ == "__main__":
    print(calculate_sum(5, 3))
```

- [ER] Erstellen Sie `test_demo.py` mit folgendem Inhalt:

```python
import pytest
from demo_code import calculate_sum, Calculator

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(0, 0) == 0
    assert calculate_sum(-1, 1) == 0

def test_calculator():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 5) == 0
```

### Flake8-Prüfung durchführen

- [ER] Führen Sie `pytest --flake8` in Ihrem `flake8_demo`-Verzeichnis aus.
- [EC] Dokumentieren Sie alle Flake8-Warnungen, die angezeigt werden.

[HINT::Keine Warnungen?]

Falls keine Warnungen angezeigt werden, führen Sie `pytest --flake8 --cache-clear` aus.

[ENDHINT]

### Pytest-spezifische Flake8-Konfiguration

- [ER] Erstellen Sie eine `.flake8`-Datei im `flake8_demo`-Verzeichnis mit folgendem Inhalt:

```conf
[flake8]
ignore = E302
```

- [ER] Führen Sie erneut `pytest --flake8` aus und beobachten Sie die Änderungen.
- [EQ] Welcher Unterschied besteht zwischen `flake8 .` und `pytest --flake8`?
  Welche Vorteile bietet die pytest-Integration?

### Code-Probleme praktisch beheben

- [ER] Korrigieren Sie alle verbleibenden Flake8-Warnungen in `demo_code.py`, ohne weitere Regeln zu ignorieren:
  - Entfernen Sie unbenutzte Imports
  - Fügen Sie fehlende Leerzeichen hinzu
  - Korrigieren Sie die Leerzeichenformatierung
  - Entfernen Sie unbenutzte Variablen

- [EC] Führen Sie nach jeder Korrektur `pytest --flake8` aus und dokumentieren Sie den Fortschritt.

### Selektive Ignorierung von Regeln

- [ER] Fügen Sie bewusst eine lange Zeile (über 79 Zeichen) zu `demo_code.py` hinzu:

```python
def long_function_with_many_parameters(parameter_one, parameter_two, parameter_three, parameter_four, parameter_five):
    return parameter_one + parameter_two + parameter_three + parameter_four + parameter_five
```

- [ER] Erweitern Sie die `.flake8`-Konfiguration um die Ignorierung der E501-Regel (Zeilenlänge).
- [EC] Führen Sie `pytest --flake8` aus und bestätigen Sie, dass keine Warnung für die lange Zeile erscheint.

### CI/CD-Integration und Best Practices

- [EQ] Wie könnte die pytest-flake8-Integration in einem Continuous Integration-Workflow nützlich sein?
- [EQ] Welche Vorteile bietet es, Code-Qualität und Tests in einem einzigen Befehl zu prüfen?
- [ER] Erstellen Sie eine finale `.flake8`-Konfiguration, die für pytest-Workflows optimiert ist.

[HINT::Weiterführende Aufgaben]

Für tiefere Flake8-Kenntnisse und erweiterte Konfiguration siehe [PARTREF::flake8].

[ENDHINT]

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
