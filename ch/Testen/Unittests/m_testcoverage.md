title: Code Coverage - Code angemessen abdecken
stage: draft
timevalue: 0
difficulty: 3
assumes: m_unittest
---
TODO_1_ruhe:

- Im Prinzip eine schöne Kombination von technischer und methodischer Aufgabe!
- Bitte stellen Sie das auf pytest-coverage um.
  Das ist ein eigenes Paket, das ein pytest-Plugin liefert, mit dem coverage dann netter
  in pytest integriert ist als bei unittest möglich.
- Die Überlegungen zur "sinnvollen" Testabdeckung finde ich sehr wertvoll.  
  Allerdings ist es schade, dass auf einem Trivialbeispiel zu machen.  
  Sondern diese Aufgabe sollte eine Folgeaufgabe von derjenigen (noch zu erstellenden)
  Aufgabe sein, die den Testfallentwurf und sinnvolle Überlegungen zum black-box-Testen
  und White-Box-Testen an einem nicht ganz simplen (gern auch realen -- wir dürfen uns für diesen
  wichtigen Stoff gern ausgiebig Zeit lassen) Beispiel lehrt.

[SECTION::goal::idea]

- Ich kann die Vor- und Nachteile von einer hohen Testabdeckung erklären.
- Ich kann meine Unittest-Abdeckung abfragen

[ENDSECTION]
[SECTION::background::default]

Während Unittests dazu dienen, die Funktionalität von Code zu überprüfen und sicherzustellen, dass
er wie erwartet funktioniert, ermöglicht die Code-Abdeckung einen Einblick in den Umfang, in dem der
Code von Tests erreicht wird.
Dabei sollte man aufpassen: Wenige Testfälle können viel Abdecken, viele Testfälle bestimmte Bereiche
doppelt testen. Können Sie festlegen, wie viele Tests gut sind?

[ENDSECTION]
[SECTION::instructions::loose]

Hier sollen sie sich mit dem Thema auseinander setzen, wie man sicherstellen kann, dass Tests eine
angemessene Code-Abdeckung bieten? Dazu werden wir im Folgenden ein gewissen Maß an Abdeckung umsetzen,
um zu analysieren, ob diese Abdeckung gut ist. Diese Analyse lassen wir von dem Python Tool
`coverage` durchführen. Sie werten anschließend aus.

Studieren Sie zuvor den Folgenden Blog-Eintrag
[Code Coverage – Kein zuverlässiges Qualitätsmaß](https://blog.ordix.de/code-coverage-kein-zuverlaessiges-qualitaetsmass),
der einen guten udn kurzen Überblick über diese Thematik bietet.

Jetzt erahnen Sie sicherlich, wohin die Reise in dieser Aufgabe gehen soll. Aber warum das so ist,
sollen Sie anhand von praktisher Beispiele selber erarbeiten.

### Coverage Packet kennenlernen

Nutzern Sie die Dokumentation [Coverage](https://coverage.readthedocs.io/en/7.5.3/), um für die
anstehende Analyse vorbereitet zu sein.

- [EC] Installieren Sie das Paket `coverage`
- [EC] Welche Version gibt Ihnen `pip show coverage` zurück?

Erstellen Sie die Dateien `greetings.py` und `test_greetings.py` im gleichen Verzeichnis und befüllen Sie diese
Dateien wie folgt:

***greetings.py***

```python
def greet(name):
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"
```

***test_greetings.py***

```python
import unittest
from greetings import greet

class TestGreetFunction(unittest.TestCase):

    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_greet_without_name(self):
        self.assertEqual(greet(""), "Hello, World!")
        self.assertEqual(greet(None), "Hello, World!")
```

- [EC] Führen Sie eine Codeabdeckungsanalyse mit `coverage` durch. Welche Befehle müssen Sie absetzen?
- [EC] Wie sieht das Ergebnis von `coverage` aus?

Jetzt sehen Sie nicht nur Ihre Code-Dateien, sondern auch die Testdateien. Da diese für uns nicht
relevant sind, wollen wir diese Dateien ignorieren. Coverage bietet dafür eine
[Konfiguration](https://coverage.readthedocs.io/en/7.5.3/config.html) an.
Prüfen Sie, wie Sie diese Datei:en aus der Analyse herausnehmen können.

- [ER] Erstellen Sie eine Konfiguration, die die Datatei `test_greetings.py` (oder alle Testdateien)
  ignoriert.
- [EC] Wie sieht die aktuelle Ausgabe aus?

Standardmäßig misst `coverage` die Zeilenabdeckung.

- [EC] Wollen wir eine Zweigabdeckungs-Analyse erreichen, was müssen wir ergänzen?

Das `cpverage`-Modul bietet viele weitere hilfreiche Einstellungen und Funktionalitäten. Stöbern Sie
gerne tiefer in die Dokumentation, um einen besseren Eindruck davon zu gewinnen, wie tiefgehend
eine Testabdeckung gehen kann.

In unserem ersten Beispiel haben wir eine Zeilenadekcung von 100% erreicht. Wenn Sie sich die
vorgegebenen Testfälle anschauen, sind Sie trotz der Analyse glücklich mit der Testabdeckung, oder ...

- [EQ] ... sollten weitere Testdaten ergänzt oder entfernt werden?
- [EQ] ... fehlen Ihnen noch Testfälle, oder können welche entfernt werden?

### Testfälle erstellen

Erstellen Sie die Datei `calculation.py` mit folgendem Inhalt.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

- [ER] Erstellen Sie Testfälle in `test_calculation.py`, so das eine 100% Zeilenabdeckung von `coverage` gemessen wird.
- [EC] Wie sieht Ihre `coverage` Analyse aus?

Sie werden mit Sicherheit eine gute Testabdeckung erreicht haben, aber ...

- [EQ] ... fehlen Ihnen auch hier noch Tests, die ggf. sogar die Testfälle fehlschlagen lassen?
- [EQ] ... sollten wir auch willkürlich große Zahlen in die Testabdekcung mit aufnehmen? Wenn ja, wieviele?

Erstellen Sie die Datei `complex_branch.py` mit folgendem Inhalt:

```python
def complex_function(x, y):
    if x > 0:
        if y > 0:
            return "Both x and y are positive"
        else:
            return "Only x is positive"
    elif y > 0:
        return "Only y is positive"
    else:
        return "Neither x nor y is positive"
```

Zusätzlich gebe ich Ihnen einen Teil meiner gefundenen Testfälle:

```python
import unittest
from complex_branch import complex_function

class TestComplexFunction(unittest.TestCase):

    def test_both_positive(self):
        result = complex_function(1, 1)
        self.assertEqual(result, "Both x and y are positive")

    def test_only_x_positive(self):
        result = complex_function(1, -1)
        self.assertEqual(result, "Only x is positive")

    def test_only_y_positive(self):
        result = complex_function(-1, 1)
        self.assertEqual(result, "Only y is positive")
```

- [EQ] Wie hoch ist die Zeilenabdeckung?
- [EQ] Wie viele Zweige müssen getestet werden?
- [ER] Erstellen Sie den/die fehlenden Test/s.

- [EQ] Diskutieren Sie: Wie hoch sollte die Code Coverage aus Ihrer Sicht generell in einem Projekt sein?
- [EQ] Diskutieren Sie: Angenommen, Sie sind Lead Entwickler und planen den Umgang mit Unittests in einem Backendlastigen
  Python Projekt. Welche allgemeine Testabdeckung würden Sie für Ihr Team forcieren?

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Lösungshilfe]

- [EREFC::1] `pip/pip3 install coverage`, aber auch `python3 -m pip install coverage` ist möglich.
- [EREFC::2] Die Version sollte > 7.5.3 sein.
- [EREFC::3] `coverage run -m unittest discover` und `coverage report`
- [EREFC::4] Ausgabe sollte wie folgt aussehen:

```bash
Name                Stmts   Miss  Cover
---------------------------------------
greetings.py            4      0   100%
test_greetings.py       9      0   100%
---------------------------------------
TOTAL                  13      0   100%
```

- [EREFR::1] Inhalt: (`omit` kann auch unter [report] stehen)

```bash
[run]
source = .
omit = test_*.py
```

- [EREFC::5]

```bash
Name           Stmts   Miss  Cover
----------------------------------
greetings.py       4      0   100%
----------------------------------
TOTAL              4      0   100%
```

- [EREFC::6] Wir müssen --branch ergänzen: `coverage run --branch -m unittest discover`

- [EREFQ::1] Ja, es sollten weitere Testdaten verwendet werden, die spezielle Eingaben wie z.B.
  Sonderzeichen, sehr lange Eingaben (üblic über 255 Zeichen oder auch gerne 10k), Integer oder ähnliche
  prüfen. Auch sicherheitsrelevante Eingaben wie bei SQL Injection oder Cross Site Scripting wären sinnvoll,
  wenn eine bestimmte Version von Python (z.B. sehr alte) genutzt wird. 
  Bsp.: `user_input = "__import__('os').system('rm -rf /')" greet(user_input)`
- [EREFQ::2] Weder noch.

- [EREFR::2] Mögliche Unittests: (interessant sind hier Randwerte, positive udn negative Werte)
  Ausnahembehandlungen wurden nicht geprüft. Falls ein Student das getan hat - somit Exceptions und Test
  faile erhilt, sollte ein Lob ausgesprochen werden.

```python
import unittest
from calculation import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(-6, -3), 2)
        with self.assertRaises(ValueError):
            divide(1, 0)
```

- [EREFC::7]

```bash
Name             Stmts   Miss  Cover
------------------------------------
calculation.py      10      0   100%
greetings.py         4      0   100%
------------------------------------
TOTAL               14      0   100%
```

- [EREFQ::3] Ja, Exceptions sollten geprüft werden, z.B. durch Werte wie `add(Integer, String)`.
- [EREFQ::4] Nein, Randwerte sind entscheidend (Äquivalentklassenbildung von Testdaten)
- [EREFQ::5] Bei 86%
- [EREFQ::6] 6 Zweige:
Alle haben einen Zweig, bis auf `"Neither x nor y is positive"`, hier gilt:
Der erste Pfad tritt ein, wenn die Bedingung x <= 0 im elif-Block erfüllt ist.
Der zweite Pfad tritt ein, wenn weder die Bedingung x > 0 noch die Bedingung elif y > 0 erfüllt sind
und somit die Bedingung im else-Block erreicht wird.

- [EREFR::3] Der letzte, der zwei Zweige abdeckt:

```python
    def test_neither_positive(self):
        result = complex_function(-1, -1)
        self.assertEqual(result, "Neither x nor y is positive")
```

[ENDINSTRUCTOR]
