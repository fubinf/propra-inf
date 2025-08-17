title: Whitebox-Testing - Testmethodik und Anwendung mit pytest
stage: alpha
timevalue: 1.0
difficulty: 3
assumes: m_pytest, pytest-Methodik-Blackbox
---

[SECTION::goal::idea]

Ich verstehe die Idee von Whitebox-Testing.

Ich kann Whitebox-Tests mit pytest schreiben und ausführen.

[ENDSECTION]
[SECTION::background::default]

Blackbox-Testing testet nur die sichtbaren Eingaben und Ausgaben – dabei übersieht man leicht
interne Logik, Sonderfälle oder seltene Zweige.
Whitebox-Testing hilft, diese verborgenen Aspekte gezielt zu prüfen und sorgt für eine höhere
Testabdeckung.
Besonders nützlich ist Whitebox-Testing, wenn keine vollständige Spezifikation vorliegt:
Die Analyse des Codes selbst zeigt, welche zusätzlichen Tests sinnvoll oder notwendig sind.

[ENDSECTION]

[SECTION::instructions::detailed]

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

Whitebox-Tests sind besonders nützlich, um sicherzustellen, dass der Code aus Sicht des Entwicklers
_robust_ ist und keine ungetesteten Bereiche enthält.
Das Ganze basiert auf der Analyse möglicher 'Wege', 'Stationen' und Werte die im Laufe der
Codeausführung durchlaufen werden können.

Typische Whitebox-Testkriterien:

- **Anweisungsüberdeckung** (statement coverage, C₀): Testet, ob jede einzelne Anweisung im Code
  mindestens einmal ausgeführt wird. Dies ist die grundlegendste Form der Testabdeckung.
- **Bedingungsüberdeckung** (condition coverage, C₁): Testet, ob jede Bedingung im Code sowohl den
  Wert True als auch False annimmt. Bei zusammengesetzten Bedingungen sollte jede Teilbedingung
  separat betrachtet werden.
- **Zweigüberdeckung** (branch coverage): Testet, ob jeder mögliche Zweig (also jeder Ausgang einer
  Verzweigung, z.B. if/else) mindestens einmal durchlaufen wird. Sie ergibt sich aus der
  Bedingungsüberdeckung, ist aber nicht identisch – insbesondere bei komplexen Bedingungen.
- **Schleifenüberdeckung** (loop coverage): Testet, ob jede Schleife im Code mindestens einmal gar
  nicht (0-mal), einmal und mehrmals durchlaufen wird. Bei einfachen Funktionen ohne Schleifen
  bringt Schleifenüberdeckung keine zusätzlichen Testfälle.
- **Pfadüberdeckung** (path coverage): Testet alle möglichen Ausführungspfade durch den Code.
  Dies ist oft nur bei sehr kleinen Funktionen praktikabel, da die Anzahl der Pfade schnell explodiert.
- **Datenflusskriterien**: Hierbei werden die möglichen Belegungen und Verwendungen von Variablen
  getestet (z.B. „def-use“-Paare). Das ist ein fortgeschrittenes Thema und für Einsteiger meist komplex
  - dennoch wagen wir einen kleinen Blick in das Thema.

[NOTICE]
Methoden geben vor, wie Sie beim Testen vorgehen sollen.
Kriterien für die Testqualität zeigen Ihnen, wie vollständig Ihre Tests sind.
Die Auswahl und das Ausdenken der konkreten Testfälle bleibt jedoch weiterhin Ihre Aufgabe –
auch wenn es dafür Hilfestellungen gibt.
[ENDNOTICE]

### Vorbereitung

- Legen Sie die Datei `whitebox.py` mit folgendem Inhalt an:

```python
def discount(price, is_member):
    """
    Berechnet Rabatt basierend auf Preis und Mitgliedschaft.
    - price: Grundpreis des Produkts (float, >=0)
    - is_member: True, wenn Mitgliedsrabatt gilt, sonst False
    
    Mitglieder: 10% Rabatt + 20% Extrarabatt bei Preis > 100
    Nicht-Mitglieder: 5% Rabatt nur bei Preis > 200
    """
    if price < 0:
        raise ValueError("Preis darf nicht negativ sein.")
    
    if is_member:
        if price > 100:
            return price * 0.8  # 20% Rabatt für Mitglieder bei teueren Produkten
        else:
            return price * 0.9  # 10% Rabatt für Mitglieder
    else:
        if price > 200:
            return price * 0.95  # 5% Rabatt für Nicht-Mitglieder bei sehr teueren Produkten
        else:
            return price  # Kein Rabatt


def bonus(salary, performance, years):
    """
    Berechnet Bonus basierend auf Gehalt, Performance und Dienstjahren.
    """
    base_bonus = 0
    if performance == "excellent":
        base_bonus = salary * 0.2
    elif performance == "good":
        base_bonus = salary * 0.1

    loyalty_bonus = 0
    if years > 5:
        loyalty_bonus = salary * 0.05

    total_bonus = base_bonus + loyalty_bonus
    return total_bonus
```

Diese Funktionen enthalten verschiedene Verzweigungen und Bedingungen, die für das Erlernen der
Whitebox-Testkriterien ideal sind. Die `discount` Funktion hat klare Pfade, die `bonus` Funktion
zeigt Datenflussmuster.

Legen Sie für die folgenden Aufgaben die Datei `test_whitebox.py` an.

### Anweisungsüberdeckung

Diese Methode prüft, ob jede einzelne Anweisung (z. B. `if`, `return`, `raise`, Zuweisungen) im Code
mindestens einmal während der Testausführung ausgeführt wird.
Ziel ist es, „tote“ oder nie ausgeführte Codezeilen zu identifizieren.

**Anwendung** Man analysiert den Code und erstellt gezielte Testfälle, um sicherzustellen, dass jede
Zeile mindestens einmal erreicht wird – unabhängig davon, ob alle möglichen Bedingungen oder Pfade
getestet wurden.
Dies ist die einfachste Form der strukturellen Testabdeckung.

**Beispiel** Bei einer Funktion mit mehreren `if`-Blöcken sollten die Tests so gestaltet sein, dass
für jeden Block mindestens ein Fall zutrifft und ausgeführt wird.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_statement_coverage()`, die sicherstellt,
  dass jede Anweisung in der Funktion `discount(..)` mindestens einmal ausgeführt wird.

### Bedingungsüberdeckung

Diese Methode stellt sicher, dass alle atomaren Bedingungen im Code sowohl den Wert `True` als auch
`False` annehmen – unabhängig davon, ob dies in Kombination mit anderen Bedingungen passiert oder
nicht.

**Anwendung** Zerlegen Sie zusammengesetzte Bedingungen (z. B. `if` `a > 10 and b < 5`) in ihre Einzelteile
`(a > 10, b < 5)` und erstellen Sie Testfälle, sodass jede davon einmal `True` und einmal `False` ergibt.
Hilfreich zur Erkennung von falsch gesetzten oder überflüssigen Bedingungen.

**Beispiel** Wenn eine Funktion prüft `if price > 100`, brauchen Sie Testfälle für `price > 100` und
`price <= 100`.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_condition_coverage()`, die sicherstellt, dass
  alle Bedingungen in der Funktion `discount(..)` sowohl `True` als auch `False` sind.

### Zweigüberdeckung

Diese Methode verlangt, dass jeder mögliche Zweig einer Entscheidung (`if`, `else`, `elif`, `try/except`)
mindestens einmal ausgeführt wird – also jede Richtung, nicht nur jede Bedingung (!).

**Anwendung** Man analysiert die Entscheidungsstellen im Code und erstellt für jede `if`-
oder `else`-Richtung einen passenden Testfall.
So kann man sicherstellen, dass sowohl der positive als auch der negative Pfad tatsächlich getestet
wurde.

**Beispiel** Für `if is_member:` brauchst du Testfälle mit `is_member = True` und `is_member = False`.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_branch_coverage()`, die sicherstellt, dass
  jede Verzweigung in der Funktion `discount(..)` mindestens einmal durchlaufen wird.

### Pfadüberdeckung

Hier wird überprüft, ob alle möglichen Ausführungspfade im Code getestet wurden – also alle
Kombinationen von Entscheidungswegen, von Start bis Ende der Funktion.

**Anwendung** Man erstellt für jeden einzigartigen Ablaufweg durch den Code einen eigenen Testfall.
Je komplexer der Code (z. B. mit vielen verschachtelten `if`-Anweisungen), desto schwieriger wird
die vollständige Pfadüberdeckung.
Hilfreich für sicherheitskritische oder sehr fehleranfällige Funktionen.

**Beispiel** Die Funktion `discount(..)` hat mindestens 5 logische Pfade, abhängig von price und
is_member.
Jeder Pfad sollte durch einen Testfall abgedeckt werden.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_path_coverage()`, die alle möglichen
  Ausführungspfade in der Funktion `discount(..)` testet.

### Datenflusskriterium

Diese Methode untersucht, ob alle Definitionen und Verwendungen von Variablen im Code abgedeckt sind.
Sie achtet darauf, ob eine Variable nach ihrer Zuweisung tatsächlich verwendet oder überschrieben wird.

**Anwendung** Man identifiziert alle Stellen, an denen Variablen gesetzt („definiert“) und
anschließend verwendet werden.
Testfälle sollen sicherstellen, dass es keine „toten“ Variablen gibt und dass Werte konsistent über
den Kontrollfluss hinweg verwendet werden.
Dies hilft besonders bei der Fehlersuche in komplexer Logik.

**Grundbegriffe der Datenflussanalyse:**

- **Definition (def)**: Eine Variable wird mit einem Wert belegt (z.B. `x = 5`, `result = calculate()`)
- **Verwendung (use)**: Eine Variable wird gelesen/verwendet (z.B. `return x`, `if x > 0`)
- **Def-Use-Pfad**: Ein Pfad von der Definition einer Variable zu ihrer Verwendung
- **Kill**: Eine Variable wird überschrieben/neu definiert, wodurch der alte Wert "getötet" wird

**Typische Datenfluss-Testkriterien:**

- **All-Defs**: Jede Definition einer Variable wird mindestens einmal verwendet
- **All-Uses**: Jede Verwendung einer Variable wird mindestens einmal von jeder möglichen Definition erreicht
- **All-Def-Use-Paths**: Alle möglichen Pfade von Definitionen zu Verwendungen werden getestet

**Beispiel** In der Funktion `discount(...)` wird price mehrfach geprüft und verwendet.
Ziel ist es sicherzustellen, dass jede Zuweisung (z. B. über Rückgabewerte) auch getestet und
genutzt wurde.

- [ER] Analysieren Sie die Variablen in beiden Funktionen und erstellen Sie:
  - `test_dataflow_bonus()` für die Analyse des Datenflusses in der `bonus` Funktion
  - `test_dataflow_discount()` für die Analyse des Datenflusses in der `discount` Funktion

### Reflektieren Sie

- [EQ] Welche Herausforderungen haben Sie bei der Testfallerstellung erkannt? Welche Methode
  empfanden Sie als zu komplex in Relation zur Funktionskomplexität?
- [EQ] Ist es stets sinnvoll oder möglich, alle Whitebox-Testkriterien auf jede Funktion anzuwenden?
- [ER] - Führen Sie alle Tests mit folgendem Befehl aus und dokumentieren Sie das Ergebnis:

```bash
pip install pytest-cov
pytest --cov=whitebox --cov-report=term-missing --cache-clear
```

[NOTICE]
Eventuell können Sie mit dem Thema Coverage mit Pytest noch nichts anfagen.
Keine Sorgen, das Thema ist ebenfalls Bestandteil in diesem Kurs und kann im Anschluss gerne hier
[PARTREF::pytest_plugin_testcoverage] oder hier [PARTREF::testcoverage] angepackt werden.
[ENDNOTICE]

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
