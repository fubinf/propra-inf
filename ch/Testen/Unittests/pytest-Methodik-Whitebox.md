title: Whitebox-Testing - Testmethodik und Anwendung mit pytest
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: m_pytest, pytest-Methodik-Blackbox
---

[SECTION::goal::idea]

- Ich verxtehe die Idee von Whitebox-Testing.
- Ich kann Whitebox-Tests mit pytest schreiben und ausführen.

[ENDSECTION]
[SECTION::background::default]

### Einführung in die Whitebox-Testmethodik

Whitebox-Tests – auch strukturelle Tests genannt – analysieren die interne Logik und den Aufbau des
Codes.
Im Gegensatz dazu konzentrieren sich Blackbox-Tests ausschließlich auf die Eingaben und Ausgaben
eines Systems, ohne Kenntnis der zugrunde liegenden Implementierung.
Während Blackbox-Testmethoden wie Äquivalenzklassen- und Grenzwertanalyse ein Mindestmaß an
sinnvollen Testfällen definieren, bleibt der Raum möglicher weiterer Testfälle groß und potenziell
unbegrenzt.
Whitebox-Testing hingegen erlaubt es uns, anhand der sichtbaren Code-Struktur genau zu bestimmen,
was und wie viel wir testen müssen – z. B. durch Kriterien wie Anweisungs- oder Schleifenüberdeckung.

[ENDSECTION]

[SECTION::instructions::detailed]

Whitebox-Tests sind besonders nützlich, um sicherzustellen, dass der Code _aus Sicht des Entwicklers_
robust ist und keine ungetesteten Bereiche enthält. Das Ganze basiert auf der Analyse möglicher
'Wege', 'Stationen' und Werte die im Laufe der Codeausführung durchlaufen werden können.

Typische Whitebox-Testmethoden:

- **Anweisungsüberdeckung**: (statement coverage, C_0) Testet, ob jede Anweisung im Code mindestens
  einmal ausgeführt wird.
- **Bedingungsüberdeckung**: (condition coverage, C_1) Testet alle möglichen Wahrheitswerte von
  Bedingungen.
- **Schleifenüberdeckung/Zweigüberdeckung**: (loop coverage, C_2) Testet, ob jede Verzweigung
  (z. B. `if`- und `else`-Blöcke mindestens einmal durchlaufen wird.
- **Pfadüberdeckung**: Testet alle möglichen Ausführungspfade im Code.
- **Datenflusskriterium**: Testet mögliche Belegungen und Verwendungen von Variablen.

### Vorbereitung

- Legen Sie die Datei `whitebox.py` mit folgendem Inhalt an:

```python
def discount(price: float, is_member: bool) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    if is_member:
        if price > 100:
            return price * 0.8  # 20% Rabatt
        return price * 0.9  # 10% Rabatt
    if price > 200:
        return price * 0.95  # 5% Rabatt
    return price
```

Diese Funktion berechnet Rabatte basierend auf dem Preis und der Mitgliedschaft. Sie enthält mehrere
Verzweigungen und Bedingungen, die getestet werden müssen.

Legen Sie für die folgenden Aufgaben die Datei `test_whitebox.py` an.

### Anweisungsüberdeckung

Diese Methode prüft, ob jede einzelne Anweisung (z. B. `if`, `return`, `raise`, Zuweisungen) im Code
mindestens einmal während der Testausführung ausgeführt wird.
Ziel ist es, „tote“ oder nie ausgeführte Codezeilen zu identifizieren.

#### Anwendung:

Man analysiert den Code und erstellt gezielte Testfälle, um sicherzustellen, dass jede Zeile
mindestens einmal erreicht wird – unabhängig davon, ob alle möglichen Bedingungen oder Pfade
getestet wurden.
Dies ist die einfachste Form der strukturellen Testabdeckung.

#### Beispiel:

Bei einer Funktion mit mehreren `if`-Blöcken sollten die Tests so gestaltet sein, dass für jeden
Block mindestens ein Fall zutrifft und ausgeführt wird.

#### Aufgabe

- [ER] Schreiben Sie eine pytest-Testfunktion `test_statement_coverage()`, die sicherstellt,
  dass jede  Anweisung in der Funktion `discount(..)` mindestens einmal ausgeführt wird.

### Bedingungsüberdeckung

Diese Methode stellt sicher, dass alle atomaren Bedingungen im Code sowohl den Wert `True` als auch
`False` annehmen – unabhängig davon, ob dies in Kombination mit anderen Bedingungen passiert oder
nicht.

#### Anwendung:

Zerlegen Sie zusammengesetzte Bedingungen (z. B. `if` `a > 10 and b < 5`) in ihre Einzelteile
`(a > 10, b < 5)` und erstellen Sie Testfälle, sodass jede davon einmal `True` und einmal `False` ergibt.
Hilfreich zur Erkennung von falsch gesetzten oder überflüssigen Bedingungen.

#### Beispiel:

Wenn eine Funktion prüft `if price > 100`, brauchen Sie Testfälle für `price > 100` und
`price <= 100`.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_condition_coverage()`, die sicherstellt, dass
  alle Bedingungen in der Funktion `discount(..)` sowohl `True` als auch `False` sind.

### Schleifenüberdeckung

Diese Methode verlangt, dass jeder mögliche Zweig einer Entscheidung (`if`, `else`, `elif`, `try/except`)
mindestens einmal ausgeführt wird – also jede Richtung, nicht nur jede Bedingung (!).

#### Anwendung:

Man analysiert die Entscheidungsstellen im Code und erstellt für jede `if`- oder `else`-Richtung
einen passenden Testfall.
So kann man sicherstellen, dass sowohl der positive als auch der negative Pfad tatsächlich getestet
wurde.

#### Beispiel:

Für `if is_member:` brauchst du Testfälle mit `is_member = True` und `is_member = False`.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_branch_coverage()`, die sicherstellt, dass
  jede Verzweigung in der Funktion `discount(..)` mindestens einmal durchlaufen wird.

### Pfadüberdeckung

Hier wird überprüft, ob alle möglichen Ausführungspfade im Code getestet wurden – also alle
Kombinationen von Entscheidungswegen, von Start bis Ende der Funktion.

#### Anwendung:

Man erstellt für jeden einzigartigen Ablaufweg durch den Code einen eigenen Testfall.
Je komplexer der Code (z. B. mit vielen verschachtelten `if`-Anweisungen), desto schwieriger wird
die vollständige Pfadüberdeckung.
Hilfreich für sicherheitskritische oder sehr fehleranfällige Funktionen.

#### Beispiel:

Die Funktion `discount(..)` hat mindestens 5 logische Pfade, abhängig von price und is_member.
Jeder Pfad sollte durch einen Testfall abgedeckt werden.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_path_coverage()`, die alle möglichen
  Ausführungspfade in der Funktion `discount(..)` testet.

### Datenflusskriterium

Diese Methode untersucht, ob alle Definitionen und Verwendungen von Variablen im Code abgedeckt sind.
Sie achtet darauf, ob eine Variable nach ihrer Zuweisung tatsächlich verwendet oder überschrieben wird.

#### Anwendung:

Man identifiziert alle Stellen, an denen Variablen gesetzt („definiert“) und anschließend verwendet
werden.
Testfälle sollen sicherstellen, dass es keine „toten“ Variablen gibt und dass Werte konsistent über
den Kontrollfluss hinweg verwendet werden.
Dies hilft besonders bei der Fehlersuche in komplexer Logik.

#### Beispiel:

In der Funktion `discount(...)` wird price mehrfach geprüft und verwendet. Ziel ist es sicherzustellen,
dass jede Zuweisung (z. B. über Rückgabewerte) auch getestet und genutzt wurde.

Ergänzen Sie dazu folgende Funktion in die Datei `whitebox.py`:

```python
def bonus(salary, performance, years):
    base_bonus = 0
    if performance == "excellent":
        base_bonus = salary * 0.2
    elif performance == "good":
        base_bonus = salary * 0.1

    loyality_bonus = 0
    if years > 5:
        loyality_bonus = salary * 0.05

    total_bonus = base_bonus + loyality_bonus
    return total_bonus
```

- [ER] Analysieren Sie, welche Variablen in `discount(..)` verwendet werden und erstellen Sie
  passende Testfälle für `test_bonus()`.

### Refklektieren Sie

- [EQ] Welche Herausforderungen haben Sie bei der Testfallerstellung erkannt? Welche Methode
  empfanden Sie als zu komplex in Relation zur Funktionskomplexität?
- [EQ] Ist es stets sinnvoll oder möglich, alle Whitebox-Testmethoden auf jede Funktion anzuwenden?

### Kontrollergebnis

Zum Schluss werden wird Ihr Gesamtergebnis für den Tutor generieren.
Diese Ausführung installiert das Pip-Packet pytest-cov. 
Falls Sie eine Python Environment verwenden, installieren Sie dieses Packet bitte entsprechend.
Hilfe können Sie hier bekommen: [PARTREF::venv] und [PARTREF::pip]

- [EQ] - Führen Sie alle Tests mit folgendem Befehl aus und dokumentieren Sie das Ergebnis:

```bash
pip install pytest-cov
pytest --cov=whitebox --cov-report=term-missing --cache-clear
```

[NOTICE]
Eventuell können Sie mit dem Thema Coverage mit Pytest noch nichts anfagen. Keine Sorgen, das Thema
ist ebenfalls Bestandteil in diesem Kurs und kann im Anschluss gerne hier [PARTREF::pytest_plugin_testcoverage] oder hier [PARTREF::testcoverage] angepackt werden.
[ENDNOTICE]

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
