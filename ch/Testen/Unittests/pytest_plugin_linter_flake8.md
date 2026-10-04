title: "Pytest: Code-Qualität mit Flake8-Plugin prüfen"
stage: alpha
timevalue: 1.25
difficulty: 2
assumes: m_pytest, flake8, pytest_call
---

[SECTION::goal::trial]

- Ich kann `flake8`-Prüfungen mit dem Plugin `pytest-flake8` in einen `pytest`-Lauf einbinden
  und diese Prüfungen gezielt auswählen.
- Ich kenne den Unterschied zwischen `ignore` und `extend-ignore` in der `flake8`-Konfiguration.
- Ich weiß, wann der Cache des Plugins veraltete Ergebnisse liefert.
- Ich weiß, welche Folgen es hat, ob eine Regel in `.flake8` oder in `pytest.ini` konfiguriert ist.

[ENDSECTION]
[SECTION::background::default]

In [PARTREF::flake8] haben Sie `flake8` als eigenständiges Kommandozeilenwerkzeug benutzt.
Das Plugin `pytest-flake8` macht aus der `flake8`-Prüfung jeder Python-Datei einen zusätzlichen Testfall.
Dann genügt ein einziger `pytest`-Aufruf, um Funktionalität und Code-Stil zu prüfen.
Das ist praktisch, hat aber ein paar Eigenheiten, die man kennen sollte.

[ENDSECTION]
[SECTION::instructions::detailed]

### Plugin installieren

Arbeiten Sie in einem eigenen [PARTREF::venv].
Legen Sie es _neben_ (nicht in) dem Verzeichnis `flake8_demo` an, das Sie gleich erzeugen,
sonst prüft `flake8 .` später auch alle Bibliotheken im venv.

Die letzte Version von `pytest-flake8` (1.3.0) funktioniert nicht mit `pytest` 9:
Dort bricht jeder `pytest`-Aufruf mit einem `PluginValidationError` ab.
Wir installieren deshalb eine ältere `pytest`-Version mit.
Solche Versionskonflikte zwischen Werkzeug und Plugin sind im Alltag häufig.

- [EC] `pip install "pytest<9" pytest-flake8`
- [EC] `pytest --help | grep -A3 flake8`

Die Ausgabe des zweiten Kommandos zeigt die Kommandozeilenoption `--flake8` sowie mehrere Konfigurationseinträge
(`flake8-ignore` usw.), die man in die `pytest`-Konfigurationsdatei `pytest.ini` schreiben kann.
Wir brauchen das später.

<!-- time estimate: 5 min -->


### Testprojekt anlegen

Erstellen Sie ein Verzeichnis `flake8_demo` und darin die Datei `demo_code.py`
mit folgendem Inhalt, der absichtlich etliche Stilprobleme enthält:

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

Erstellen Sie außerdem `test_demo.py`:

```python
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

<!-- time estimate: 5 min -->


### `flake8` als Testfall

Führen Sie alle folgenden Kommandos im Verzeichnis `flake8_demo` aus.

- [EC] `pytest --flake8 -v`
- [EQ] Wie viele Testfälle meldet `pytest`, und welche davon gibt es nur wegen `--flake8`?
  Welche Dateien prüft das Plugin?
- Das Plugin versieht seine Testfälle mit der Markierung `flake8`.
  Wie man mit `-m` nur markierte Testfälle ausführt, kennen Sie aus [PARTREF::pytest_call].
- [EC] `pytest --flake8 -m flake8`
  (Dass dabei ein Testfall als `skipped` gemeldet wird, klären wir weiter unten.)
- In vielen Projekten steht `--flake8` nicht auf der Kommandozeile, sondern fest in `pytest.ini`,
  sodass jeder `pytest`-Aufruf auch die `flake8`-Testfälle enthält.
  Das geht mit dem Eintrag
  [`addopts`](https://docs.pytest.org/en/stable/reference/reference.html#confval-addopts).
- [EQ] Wozu ist es in einem solchen Projekt nützlich, mit `-m flake8` nur die `flake8`-Testfälle
  laufen zu lassen, und wozu umgekehrt mit `-m "not flake8"` nur die übrigen?

<!-- time estimate: 10 min -->


### `ignore` oder `extend-ignore`?

Die Meldung `E302` (zwei Leerzeilen vor einer Funktions- oder Klassendefinition) halten wir hier für entbehrlich.

`flake8` liest seine Einstellungen nicht nur von der Kommandozeile, sondern auch aus einer
Konfigurationsdatei im Projektverzeichnis, z.B. `.flake8`, siehe
[Configuring Flake8](https://flake8.pycqa.org/en/stable/user/configuration.html).
Die Einträge darin heißen wie die Kommandozeilenoptionen, nur ohne `--`:
`ignore = E302` in der Datei wirkt wie `--ignore E302` auf der Kommandozeile.

Legen Sie in `flake8_demo` eine Datei `.flake8` mit folgendem Inhalt an:

```ini
[flake8]
ignore = E302
```

- [EC] `pytest --flake8`
- [EQ] Vergleichen Sie die Meldungen mit denen des ersten Laufs.
  Welche sind verschwunden, welche sind neu hinzugekommen?
  Warum gibt es überhaupt neue Meldungen?

[HINT::Ich verstehe nicht, woher die neuen Meldungen kommen]

Lesen Sie in der `flake8`-Dokumentation die Beschreibung von
[`--ignore`](https://flake8.pycqa.org/en/stable/user/options.html#cmdoption-flake8-ignore)
und
[`--extend-ignore`](https://flake8.pycqa.org/en/stable/user/options.html#cmdoption-flake8-extend-ignore).
Achten Sie auf den Standardwert von `--ignore`.

[ENDHINT]

- [ER] Ändern Sie `.flake8` so, dass `E302` ignoriert wird, ohne dass neue Meldungen auftauchen.
- [EC] `pytest --flake8`

<!-- time estimate: 15 min -->


### Code bereinigen

- [ER] Beseitigen Sie alle verbleibenden Meldungen in `demo_code.py`, ohne `.flake8` weiter zu ändern.
  Die Bedeutung der Meldungscodes kennen Sie aus [PARTREF::flake8].
  Lassen Sie `a+b` und `x*y` dabei unverändert; dazu gibt es ja keine Meldung.
- [EC] `pytest --flake8`

<!-- time estimate: 10 min -->


### Der Cache des Plugins

- [EC] `pytest --flake8 -rs`
  (`-rs` zeigt am Ende den Grund für übersprungene Testfälle.)
- Das Plugin legt im Cache-Verzeichnis `.pytest_cache` von `pytest` eine Datei an,
  in der es sich für jede bestandene Datei etwas merkt.
- [EC] `cat .pytest_cache/v/flake8/mtimes`
  (`mtime` steht für _modification time_, den Zeitpunkt der letzten Änderung einer Datei.)
- Ergänzen Sie in `.flake8` vorübergehend die Zeile `max-line-length = 20`.
  Damit müssten viele Zeilen beanstandet werden.
- [EC] `pytest --flake8`
- [EC] `pytest --flake8 --cache-clear`
- [EQ] Was merkt sich das Plugin laut `mtimes` für jede bestandene Datei?
  Warum hat der vorletzte Lauf die neue Zeilenlänge deshalb nicht bemerkt?
  Welches Risiko entsteht daraus in der Praxis, und wie begegnet man ihm?
- Entfernen Sie die Zeile `max-line-length = 20` wieder.

<!-- time estimate: 10 min -->


### Regeln nur für einzelne Dateien abschalten

Ergänzen Sie in `demo_code.py` vor dem `if __name__ ...`-Block diese Funktion mit überlangen Zeilen:

```python
def long_function_with_many_parameters(parameter_one, parameter_two, parameter_three, parameter_four, parameter_five):
    return parameter_one + parameter_two + parameter_three + parameter_four + parameter_five
```

- [EC] `pytest --flake8`
- [ER] Legen Sie in `flake8_demo` eine Datei `pytest.ini` an, die mithilfe des Eintrags `flake8-ignore`
  die Meldung `E501` (Zeile zu lang) _nur_ für `demo_code.py` abschaltet.
  Die Beschreibung des Eintrags kennen Sie aus der Ausgabe von `pytest --help`.

[HINT::Ich weiß nicht, wie der Eintrag in `pytest.ini` aussehen muss]

Der Typ `linelist` bedeutet, dass der Wert eine Liste ist, mit einem Eintrag pro eingerückter Zeile.
Eine Datei mit dem Beispiel aus der Hilfe sähe so aus:

```ini
[pytest]
flake8-ignore =
    *.py W293
```

[ENDHINT]

- [EC] `pytest --flake8`
- [EQ] Die `E501`-Meldungen sind weg, aber der Lauf schlägt trotzdem fehl.
  Woher kommen die neuen Meldungen, obwohl Sie doch nur eine weitere Meldung abgeschaltet haben?

[HINT::Ich verstehe nicht, woher die `E226`-Meldungen kommen]

Dieselben Meldungen haben Sie schon einmal gesehen, nämlich nach dem ersten Anlegen von `.flake8`.
Was war damals die Ursache?
Welchem der beiden `flake8`-Einträge `ignore` und `extend-ignore` entspricht `flake8-ignore` demnach?

[ENDHINT]

- [EC] `flake8 .`
- [EQ] Warum liefern die beiden letzten Kommandos unterschiedliche Ergebnisse?
- [EQ] Angenommen, in einem Team prüft die [TERMREF::CI/CD]-Pipeline mit `pytest --flake8`,
  während die Entwickler_innen lokal `flake8` oder den Linter ihrer IDE benutzen.
  Welches Problem entsteht durch Regeln in `pytest.ini`?
- [ER] Verlegen Sie die Ausnahme für `demo_code.py` nach `.flake8`, und zwar mit dem Eintrag
  [`per-file-ignores`](https://flake8.pycqa.org/en/stable/user/options.html#cmdoption-flake8-per-file-ignores).
  Kommentieren Sie beide Zeilen des Eintrags `flake8-ignore` in `pytest.ini` mit `#` aus.
- [EC] `flake8 .`
- [EC] `pytest --flake8`

Beide Kommandos sollten jetzt keine Meldungen mehr liefern.

<!-- time estimate: 20 min -->


### Plugin oder eigener `flake8`-Aufruf?

- [EQ] Würden Sie in einem neuen Projekt `pytest --flake8` verwenden oder `flake8` als eigenen Schritt
  (lokal und in der CI-Pipeline) aufrufen?
  Begründen Sie Ihre Wahl mit Beobachtungen aus dieser Aufgabe.

<!-- time estimate: 5 min -->

[ENDSECTION]
[SECTION::submission::reflection,trace,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
(Gemeint sind `demo_code.py`, `.flake8` und `pytest.ini` im Endzustand.)

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
