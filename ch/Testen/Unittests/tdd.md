title: "Test Driven Development: FizzBuzz mit pytest"
stage: alpha
timevalue: 2
difficulty: 2
assumes: m_pytest, Git101
explains: TDD
---

[SECTION::goal::experience]

Ich habe eine kleine Funktion mittels Test Driven Development entwickelt
und dabei den Red-Green-Refactor-Zyklus mehrfach durchlaufen.

[ENDSECTION]
[SECTION::background::default]

Bei [TERMREF::TDD] schreibt man den Test _vor_ dem Code, der ihn erfüllen soll.
Das klingt zunächst verdreht, führt aber zu einer ungewohnt ruhigen Arbeitsweise in kleinen,
jederzeit abgesicherten Schritten.
Ob das für Sie funktioniert, finden Sie am besten heraus, indem Sie es ausprobieren.

[ENDSECTION]
[SECTION::instructions::detailed]

### Der TDD-Zyklus
<!-- time estimate: 15 min -->

TDD besteht aus der ständigen Wiederholung von drei Schritten:

1. **Red**: Schreiben Sie einen Test für ein kleines Stück gewünschten Verhaltens.
   Der Test muss fehlschlagen, denn das Verhalten gibt es ja noch nicht.
2. **Green**: Schreiben Sie den _minimalen_ Code, der den Test bestehen lässt.
   Das darf (und soll hier ausdrücklich) eine plumpe Lösung sein, notfalls mit hart kodierten Werten.
   Ziel ist nur: grün.
3. **Refactor**: Verbessern Sie nun die Struktur des Codes, z.B. indem Sie hart kodierte Werte
   durch eine allgemeine Lösung ersetzen.
   Dabei ändern Sie das geprüfte Verhalten nicht; die Tests müssen grün bleiben und sichern Sie so ab.

Lesen Sie Martin Fowlers kurzen Artikel
[Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html).
Achten Sie darauf, welchen Fehler Fowler als den häufigsten beim Anwenden von TDD nennt.
Genau diesen Fehler sollen Sie hier vermeiden.

Als Übungsgegenstand dient die Funktion `fizzbuzz(n)`.
Sie soll für eine positive ganze Zahl `n` zurückgeben:

- `"FizzBuzz"`, wenn `n` durch 3 und durch 5 teilbar ist,
- sonst `"Fizz"`, wenn `n` durch 3 teilbar ist,
- sonst `"Buzz"`, wenn `n` durch 5 teilbar ist,
- sonst die Zahl selbst als String, z.B. `"7"`.
- Für `n <= 0` soll ein `ValueError` ausgelöst werden.

Diese Spezifikation setzen Sie aber nicht auf einmal um, sondern Stück für Stück, Test für Test.


### Arbeitsweise

Arbeiten Sie zu zweit an einem gemeinsamen Rechner nach dem "Ping-Pong"-Muster:
Person A schreibt einen Test (Red).
Person B bringt ihn zum Bestehen (Green), refaktoriert (Refactor) und schreibt dann den nächsten Test.
Dann ist wieder Person A mit Green und Refactor dran, usw.
Besprechen Sie dabei jeden Schritt miteinander.
Erst ganz am Ende überträgt eine Person das fertige Repo auf den Rechner der anderen
(siehe Abschnitt "Abschluss und Reflexion").

Nach jedem einzelnen Schritt machen Sie einen Commit,
damit man den Rhythmus der Arbeitsweise hinterher im Git-Log ablesen kann.


### Vorbereitung
<!-- time estimate: 10 min -->

Sie arbeiten in einem eigenen kleinen Git-Repository in Ihrem
[TERMREF::Hilfsbereich], nicht in Ihrem Kursrepo.

- Legen Sie das Verzeichnis an und wechseln Sie hinein:
  `mkdir -p ~/ws/tmp/Testen/Unittests/tdd && cd ~/ws/tmp/Testen/Unittests/tdd`
- Machen Sie es zu einem Git-Repository: `git init`
- Damit die Hilfsdateien von Python und `pytest` nicht mit eingecheckt werden,
  legen Sie eine Datei `.gitignore` mit folgendem Inhalt an:

```
__pycache__/
.pytest_cache/
```

- Legen Sie die leeren Dateien `fizzbuzz.py` (für den Code) und `test_fizzbuzz.py` (für die Tests) an.

Die Tests in `test_fizzbuzz.py` brauchen Zugriff auf die Funktion aus `fizzbuzz.py`.
Schreiben Sie dafür als erste Zeile in `test_fizzbuzz.py`:

```python
from fizzbuzz import fizzbuzz
```


### Zyklus 1: Eine normale Zahl
<!-- time estimate: 15 min -->

**Red:**

- Schreiben Sie in `test_fizzbuzz.py` einen Test `test_normal_number`,
  der prüft, dass `fizzbuzz(1)` den Wert `"1"` liefert.
- Führen Sie den Test aus: `pytest test_fizzbuzz.py`

Der Test schlägt fehl, und zwar nicht an der Assertion, sondern schon vorher mit einem
`ImportError`, weil es die Funktion `fizzbuzz` noch gar nicht gibt.
Auch das zählt als "Red": Der Test verlangt etwas, das noch fehlt.

- Commit: `git add . && git commit -m "Red: 1 ergibt '1'"`

**Green:**

- Schreiben Sie in `fizzbuzz.py` eine Funktion `fizzbuzz(n)`, die einfach immer `"1"` zurückgibt.
  Ja, wirklich: Mehr verlangt der Test noch nicht.
- Prüfen Sie mit `pytest test_fizzbuzz.py`, dass der Test besteht.
- Commit: `git add . && git commit -m "Green: 1 ergibt '1'"`

**Refactor:**

Die hart kodierte `"1"` ist offensichtlich nur ein Platzhalter.
Die allgemeine Form dessen, was der Test verlangt, ist: die Zahl als String.

- Ersetzen Sie `"1"` durch eine allgemeine Lösung.
- Prüfen Sie mit `pytest test_fizzbuzz.py`, dass der Test weiterhin besteht.
- Commit: `git add . && git commit -m "Refactor: Zahl allgemein als String"`


### Zyklus 2: Fizz
<!-- time estimate: 15 min -->

**Red:**

- Ergänzen Sie einen Test `test_fizz`, der prüft, dass `fizzbuzz(3)` den Wert `"Fizz"` liefert.
- Führen Sie die Tests aus: `pytest test_fizzbuzz.py`
- Commit: `git add . && git commit -m "Red: 3 ergibt 'Fizz'"`

**Green:**

- Bringen Sie den Test so einfach wie möglich zum Bestehen, also mit einer Abfrage `n == 3`.
- Prüfen Sie mit `pytest test_fizzbuzz.py`, dass alle Tests bestehen.
- Commit: `git add . && git commit -m "Green: 3 ergibt 'Fizz'"`

[EQ] Ihre Funktion besteht nun alle Tests und ist trotzdem offensichtlich falsch.
Geben Sie einen Test an, der das aufdecken würde.
Was folgt daraus über die Aussagekraft eines grünen Testlaufs?

**Refactor:**

- Verallgemeinern Sie die Abfrage `n == 3` so, dass sie der Spezifikation "durch 3 teilbar" entspricht.
- Prüfen Sie mit `pytest test_fizzbuzz.py`, dass alle Tests bestehen.
- Commit: `git add . && git commit -m "Refactor: Fizz für alle Vielfachen von 3"`


### Zyklus 3: Buzz
<!-- time estimate: 10 min -->

Gehen Sie genauso vor wie in Zyklus 2, diesmal für `fizzbuzz(5)` → `"Buzz"`
mit einem Test `test_buzz`.
Machen Sie wieder nach jedem der drei Schritte einen Commit
mit einer Commit-Botschaft nach dem obigen Muster.


### Zyklus 4: FizzBuzz
<!-- time estimate: 15 min -->

Gehen Sie genauso vor für `fizzbuzz(15)` → `"FizzBuzz"` mit einem Test `test_fizzbuzz`.

[HINT::Mein neuer Test schlägt fehl, obwohl ich den Fall 15 behandle]
Welche Abfrage in Ihrer Funktion trifft bei `n = 15` als erste zu?
Die Reihenfolge der Abfragen ist entscheidend.
[ENDHINT]

[HINT::Ich weiß nicht, was ich hier refaktorieren soll]
Mögliche Ansatzpunkte:

- Ist noch irgendwo eine hart kodierte Zahl wie `n == 15` übrig?
- Sind die Zahlen 3 und 5 jetzt mehrfach im Code verstreut?
  Dann können Sie sie z.B. als Konstanten mit sprechenden Namen definieren.
- Ist die Abfrage für `"FizzBuzz"` direkt als Kombination der beiden anderen Bedingungen erkennbar?
[ENDHINT]


### Zyklus 5: Ungültige Eingaben
<!-- time estimate: 15 min -->

Laut Spezifikation soll für `n <= 0` ein `ValueError` ausgelöst werden.
Wie man in `pytest` prüft, dass eine Ausnahme ausgelöst wird, steht in der `pytest`-Dokumentation unter
[Assertions about expected exceptions](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions).

**Red:**

- Ergänzen Sie einen Test `test_invalid_input`, der mit `pytest.raises` prüft,
  dass `fizzbuzz(0)` und `fizzbuzz(-3)` jeweils einen `ValueError` auslösen.
  Dafür brauchen Sie in `test_fizzbuzz.py` zusätzlich `import pytest`.
- Führen Sie die Tests aus: `pytest test_fizzbuzz.py`

[HINT::Ich verstehe die Meldung `Failed: DID NOT RAISE` nicht]
Der Test erwartet einen `ValueError`, aber `fizzbuzz(0)` liefert bisher ohne Fehler `"FizzBuzz"`.
0 ist nämlich durch jede Zahl teilbar, denn `0 % 3` ergibt `0`.
Genau deshalb braucht es eine ausdrückliche Regel für diesen Fall.
[ENDHINT]

Machen Sie dann wie gewohnt Commits für Red, Green und (falls es etwas zu verbessern gibt) Refactor.


### Abschluss und Reflexion
<!-- time estimate: 10 min -->

Damit beide Personen ein eigenes Kommandoprotokoll abgeben können,
packt die Person, auf deren Rechner Sie gearbeitet haben, das Verzeichnis samt Git-Historie ein:
`cd .. && tar czf tdd.tar.gz tdd`.
Schicken Sie die Datei `tdd.tar.gz` der anderen Person (z.B. per Mail oder Chat).
Diese legt das Elternverzeichnis an und wechselt hinein:
`mkdir -p ~/ws/tmp/Testen/Unittests && cd ~/ws/tmp/Testen/Unittests`.
Dann kopiert sie die Datei dorthin und packt sie aus: `tar xzf tdd.tar.gz && cd tdd`.

Führen Sie dann beide jeweils auf Ihrem eigenen Rechner im Verzeichnis `tdd` aus:

- [EC] `pytest -v test_fizzbuzz.py`
- [EC] `git -P log -p --reverse`

Prüfen Sie in der Ausgabe von `git log`, dass jeder Red-Commit (abgesehen vom allerersten) nur Testcode ändert,
jeder Green-Commit nur Programmcode, und dass bei Refactor-Commits die Tests unverändert bleiben.

[EQ] In welchem Refactoring-Schritt haben Sie Ihren Code am stärksten verändert?
Was genau haben Sie dort geändert und was hat Ihnen die Sicherheit gegeben,
dass dabei nichts kaputtgeht?

[EQ] Vergleichen Sie diese Arbeitsweise mit Ihrer bisherigen (erst Code, dann ggf. Tests):
Was war ungewohnt oder lästig?
Welche Vorteile sehen Sie?
Bei welcher Art von Aufgaben würden Sie TDD eher einsetzen, bei welcher eher nicht?

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
