title: "Mutation Testing mit mutmut: Taugen meine Tests etwas?"
stage: alpha
timevalue: 2.0
difficulty: 3
explains: Mutationstests
assumes: m_pytest, pytest-Methodik-Blackbox, venv
---

[SECTION::goal::idea]

- Ich verstehe, wie Mutation Testing die Qualität einer Testsuite bewertet
  und warum das mehr aussagt als die Überdeckung.
- Ich kann mit `mutmut` Mutanten erzeugen, die Ergebnisse auswerten
  und überlebende Mutanten mit gezielten Testfällen töten.
- Ich kann äquivalente Mutanten erkennen und einschätzen, wann sich Mutation Testing lohnt.

[ENDSECTION]
[SECTION::background::default]

Eine grüne Testsuite beruhigt.
Sie ist aber nur dann etwas wert, wenn sie rot würde, sobald sich ein Defekt in den Code einschleicht.
Die [TERMREF::Überdeckung] beantwortet diese Frage nicht:
Sie zeigt, welcher Code während der Tests _ausgeführt_ wurde,
aber nicht, ob die Tests seine Ergebnisse auch genau genug _prüfen_.

Mutation Testing geht die Frage direkt an:
Es baut absichtlich kleine Defekte in den Code ein und schaut nach, ob die Tests sie bemerken.
Jeder unbemerkte Defekt zeigt eine konkrete Lücke in der Testsuite
und verrät meist gleich mit, welcher Testfall fehlt.

[ENDSECTION]
[SECTION::instructions::detailed]

### Vorbereitung

Ein Prüfungsbüro wertet Klausuren mit einem kleinen Python-Modul aus:
Es berechnet aus Klausur- und Bonuspunkten die Gesamtpunktzahl, daraus die Note
und entscheidet, ob jemand das Modul bestanden hat.
Jemand aus dem Team hat dafür bereits Tests geschrieben.

Legen Sie in Ihrem Arbeitsbereich ein Verzeichnis `pytest_mutation_testing/` an
und arbeiten Sie dort in einem aktivierten venv (siehe [PARTREF::venv]).

Das Modul `klausur.py`:

```python
[INCLUDE::include/pytest_mutation_testing-klausur.py]
```

Die vorhandenen Tests in `test_klausur.py`:

```python
[INCLUDE::include/pytest_mutation_testing-test_klausur.py]
```

Legen Sie die Dateien `klausur.py` und `test_klausur.py` mit obigem Inhalt an.

Legen Sie außerdem eine Datei `pyproject.toml` an:

```toml
[tool.pytest.ini_options]
addopts = "--ignore=mutants"

[tool.mutmut]
source_paths = ["klausur.py"]
```

Im Abschnitt `[tool.mutmut]` steht, welchen Code das Werkzeug `mutmut` verändern soll;
was es damit tut, sehen Sie gleich.
`mutmut` arbeitet auf Kopien Ihrer Dateien im Verzeichnis `mutants/`.
Diese Kopien soll `pytest` nicht als weitere Tests einsammeln (daher `--ignore=mutants`),
und `git` soll sie nicht einchecken.
Legen Sie deshalb noch eine Datei `.gitignore` an
(`.coverage` ist die Messdatei von `pytest-cov`, das Sie ebenfalls gleich benutzen):

```text
mutants/
.coverage
__pycache__/
.pytest_cache/
```

Installieren Sie `mutmut` und das Coverage-Plugin `pytest-cov`:
`pip install "mutmut>=3.8" pytest-cov`.
`mutmut` hat sich mit Version 3 grundlegend geändert;
viele Anleitungen im Netz beschreiben noch Version 2 mit anderen Kommandos und Einstellungen.
`mutmut` läuft nur auf Linux und macOS; unter Windows benutzen Sie wie üblich WSL.

- [EC] `mutmut --version`

[HINT::`mutmut` meldet `Could not figure out where the code to mutate is`]
`mutmut` liest seine Einstellungen aus der `pyproject.toml` im aktuellen Verzeichnis.
Rufen Sie es im Verzeichnis `pytest_mutation_testing/` auf und prüfen Sie den Abschnitt `[tool.mutmut]`.
[ENDHINT]

<!-- time estimate: 10 min -->

### Grüne Tests, volle Überdeckung

Zunächst prüfen wir die Testsuite mit dem Maß, das Sie vermutlich schon kennen.
`--cov=klausur` misst die Überdeckung des Moduls `klausur`,
`--cov-branch` schaltet zusätzlich die Zweigüberdeckung ein
und `--cov-report=term-missing` listet nicht ausgeführte Zeilen auf.
Mehr zu `pytest-cov` finden Sie in [PARTREF::testcoverage].

- [EC] `pytest --cov=klausur --cov-branch --cov-report=term-missing`

Alle Tests sind grün, jede Anweisung und jeder Zweig wurde ausgeführt.
Nach diesem Maß ist die Testsuite perfekt.

<!-- time estimate: 5 min -->

### Ein Defekt, den niemand bemerkt

Bevor ein Werkzeug die Arbeit übernimmt, sabotieren Sie den Code einmal von Hand.

- Ändern Sie in `note()` die Zeile `if punkte >= 90:` in `if punkte > 90:`.
- [EC] `pytest`
- [EQ] Wen träfe dieser Defekt im echten Prüfungsbetrieb, und mit welcher Folge?
  Warum bemerkt ihn die Testsuite nicht, obwohl sie jede Zeile und jeden Zweig von `note()` ausführt?
- Machen Sie die Änderung wieder rückgängig.

Genau diese Sabotage automatisieren [TERMREF::Mutationstests]:
Ein Werkzeug erzeugt viele leicht abgewandelte Fassungen des Codes, sogenannte **Mutanten**,
jede mit genau einer kleinen Änderung, z.B. `>` statt `>=`, `91` statt `90` oder `or` statt `and`.
Solche Änderungen ähneln typischen echten Defekten wie den [PARTREF2::Off-by-1-Defekte::Off-by-1-Defekten].
Für jeden Mutanten lässt das Werkzeug die Tests laufen:

- Schlägt mindestens ein Test fehl, ist der Mutant **getötet** (_killed_).
  So soll es sein.
- Bleiben alle Tests grün, hat der Mutant **überlebt** (_survived_):
  Diesen Defekt hätte die Testsuite nicht bemerkt.

Der Anteil der getöteten Mutanten an allen Mutanten heißt **Mutation Score**.

<!-- time estimate: 10 min -->

### `mutmut` ausführen

`mutmut` ist das gebräuchlichste Werkzeug für Mutation Testing in Python und arbeitet mit `pytest` zusammen.
Es verändert nur Code innerhalb von Funktionen
und führt für jeden Mutanten nur die Tests aus, die die betroffene Funktion aufrufen.

- [EC] `mutmut run`

Die letzte Zeile der Ausgabe fasst das Ergebnis zusammen.
Vorn steht, wie viele Mutanten bereits geprüft sind, dahinter die Anzahl je Ergebnis:

- 🎉 getötet
- 🙁 überlebt
- 🫥 kein Test ruft die mutierte Funktion auf
- ⏰ Zeitüberschreitung, z.B. weil der Mutant eine Endlosschleife erzeugt;
  das wertet man üblicherweise wie getötet

Die übrigen Symbole spielen in dieser Aufgabe keine Rolle.
`mutmut results` listet alle Mutanten auf, die nicht getötet wurden.
Ein Name wie `klausur.x_note__mutmut_1` bedeutet: Mutant Nr. 1 der Funktion `note()` im Modul `klausur`.
`mutmut show` zeigt, was ein Mutant am Code verändert hat.

- [EC] `mutmut results`
- [EC] `mutmut show klausur.x_note__mutmut_1`

Sehen Sie sich auf diese Weise alle überlebenden Mutanten an.
Diese weiteren Aufrufe gehören nicht ins Kommandoprotokoll.

- [EQ] Wie hoch ist der Mutation Score der vorhandenen Testsuite?
  Ordnen Sie die überlebenden Mutanten in Gruppen: Welche Art von Testfall fehlt der Testsuite jeweils?

[HINT::Ich erkenne keine Gemeinsamkeiten zwischen den Mutanten]
Fragen Sie bei jedem Mutanten: Für welche Eingaben liefern Original und Mutant verschiedene Ergebnisse?
Liegen diese Eingaben an einer Grenze?
Kommt eine davon in den vorhandenen Tests vor?
[ENDHINT]

<!-- time estimate: 15 min -->

### Überlebende Mutanten töten

- [ER] Ergänzen Sie `test_klausur.py` um Testfälle, die möglichst viele der überlebenden Mutanten töten.
  Ändern Sie `klausur.py` dabei nicht.
  Leiten Sie die erwarteten Ergebnisse aus den Docstrings ab und nicht aus dem Code,
  denn der Code könnte selbst einen Defekt enthalten.

[HINT::Ich weiß nicht, mit welcher Eingabe ich einen Mutanten töte]
Ein Testfall tötet einen Mutanten, wenn Original und Mutant für seine Eingabe verschiedene Ergebnisse liefern
und der Test das richtige Ergebnis erwartet.
Bei `>=` gegenüber `>` gibt es genau eine solche Eingabe: den Grenzwert selbst.
Das kennen Sie als Randwertanalyse aus [PARTREF::pytest-Methodik-Blackbox].
[ENDHINT]

[HINT::Wie töte ich den Mutanten mit `or` statt `and`?]
Stellen Sie die Wahrheitswerte von `klausurpunkte >= BESTEHENSGRENZE` und `uebungsschein` in einer Tabelle auf.
Für welche Kombinationen unterscheiden sich `and` und `or`?
Welche Kombinationen prüft `test_modul_bestanden()`?
[ENDHINT]

`mutmut` merkt sich seine Ergebnisse im Verzeichnis `mutants/`
und prüft einen Mutanten nur dann neu, wenn sich der Code der mutierten Funktion geändert hat.
Neue Tests allein lösen keine Neuprüfung aus; ein schlichtes `mutmut run` zeigt also die alten Ergebnisse.
Eine Neuprüfung erzwingen Sie, indem Sie die Mutanten mit einem Namensmuster angeben
(siehe Abschnitt "Wildcards for testing mutants" in der Dokumentation von `mutmut`):
[HREF::https://mutmut.readthedocs.io/en/latest/]
Die Anführungszeichen im folgenden Kommando verhindern, dass die Shell das `*` selbst als Dateinamenmuster auswertet.

- [EC] `mutmut run "klausur*"`
- [EC] `mutmut results`

[HINT::`mutmut` bricht mit `failed to collect stats` oder `Failed to run clean test` ab]
Mindestens ein Test schlägt schon ohne Mutation fehl.
`mutmut` braucht eine grüne Testsuite als Ausgangspunkt.
Rufen Sie `pytest` auf und klären Sie, ob Ihr Test oder Ihre Erwartung falsch ist.
[ENDHINT]

Wenn Ihre Testfälle gut gewählt sind, überlebt jetzt nur noch ein einziger Mutant, und zwar in `gesamtpunkte()`.
Überleben mehr, ergänzen Sie weitere Testfälle.

<!-- time estimate: 25 min -->

### Der letzte überlebende Mutant

- [EQ] Versuchen Sie, auch den letzten Mutanten mit einem Testfall zu töten.
  Warum gelingt das nicht?
  Begründen Sie Ihre Antwort anhand des Codes.

[HINT::Mein Test tötet ihn nicht, aber ich verstehe nicht, warum]
Für welchen Wert von `bonuspunkte` verhalten sich `>` und `>=` unterschiedlich?
Verfolgen Sie für diesen Wert, was im Original und im Mutanten jeweils passiert.
[ENDHINT]

Ein Mutant, der zwar den Code verändert, nicht aber dessen Verhalten,
heißt **äquivalenter Mutant**.
Kein Test kann ihn töten.
Ob ein überlebender Mutant äquivalent ist oder ob nur ein Testfall fehlt,
kann Ihnen kein Werkzeug zuverlässig sagen; das müssen Sie selbst durchdenken.
`mutmut` zählt ihn deshalb einfach als überlebend.
In der Fachliteratur rechnet man äquivalente Mutanten aus dem Mutation Score heraus,
wie Sie im folgenden Lexikonartikel im Abschnitt "Wie funktioniert Mutation Testing?" nachlesen können:
[HREF::https://www.testautomatisierung.org/lexikon/mutation-testing/]

Mit äquivalenten Mutanten geht man in der Praxis auf eine von zwei Arten um:
Man nimmt die betroffene Zeile mit dem Kommentar `# pragma: no mutate` von der Mutation aus
(siehe Abschnitt "Disabling mutation on specific code" der `mutmut`-Dokumentation).
Oder man formuliert den Code so um, dass der äquivalente Mutant gar nicht erst entsteht;
oft wird der Code dabei sogar einfacher.

- [ER] Formulieren Sie `gesamtpunkte()` so um, dass sie sich genauso verhält wie bisher,
  der äquivalente Mutant aber nicht mehr entstehen kann.

[HINT::Mir fällt keine andere Formulierung ein]
Python hat eine eingebaute Funktion, die von zwei Werten den kleineren liefert.
`gesamtpunkte()` benutzt sie in ihrer letzten Zeile bereits.
[ENDHINT]

Diesmal genügt ein schlichtes `mutmut run`:
Sie haben den Code von `gesamtpunkte()` geändert, also prüft `mutmut` deren Mutanten von selbst neu.

- [EC] `mutmut run`

<!-- time estimate: 15 min -->

### Tests für eine neue Funktion

Das Prüfungsbüro möchte die Bonuspunkte künftig ebenfalls automatisch berechnen lassen.
Diesmal schreiben Sie die Tests selbst und lassen sie anschließend von `mutmut` begutachten.

```python
[INCLUDE::include/pytest_mutation_testing-bonuspunkte.py]
```

- [ER] Fügen Sie `bonuspunkte()` am Ende von `klausur.py` ein.
  Schreiben Sie in einer neuen Datei `test_bonuspunkte.py` Tests für `bonuspunkte()`,
  so gründlich, wie Sie es ohne `mutmut` tun würden:
  mit Äquivalenzklassen und Randwerten, abgeleitet aus dem Docstring.
  Fragen Sie `mutmut` erst, wenn Sie mit Ihren Tests zufrieden sind.

[HINT::Wie prüfe ich, dass ein `ValueError` ausgelöst wird?]
Mit dem Kontextmanager `pytest.raises`, den Sie auch in [PARTREF::pytest_aaa] kennenlernen:

```python
with pytest.raises(ValueError):
    bonuspunkte([-1])
```
[ENDHINT]

Für die neue Funktion genügt wieder ein schlichtes `mutmut run`,
denn ihre Mutanten sind neu und noch ungeprüft.

- [EC] `mutmut run`
- [EC] `mutmut results`
- [EQ] Welche Mutanten von `bonuspunkte()` haben Ihre Tests übersehen, und welcher Testfall fehlte jeweils?
  Hätten Sie diese Lücken auch ohne `mutmut` bemerkt?
- [ER] Ergänzen Sie `test_bonuspunkte.py`, bis jeder überlebende Mutant von `bonuspunkte()`
  entweder getötet ist oder Sie begründen können, warum Sie ihn bewusst überleben lassen.

[HINT::Wie prüfe ich die Fehlermeldung?]
`pytest.raises` hat dafür den Parameter `match`, siehe die
[pytest-Dokumentation zu `raises`](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions).
[ENDHINT]

- [EC] `mutmut run "klausur.x_bonuspunkte*"`
- [EQ] Welche Mutanten haben Sie bewusst überleben lassen, und warum?
  Wie sind Sie insbesondere mit dem Mutanten umgegangen, der die Fehlermeldung durch `None` ersetzt?

<!-- time estimate: 25 min -->

### Reflexion

- [EQ] In dieser Aufgabe brauchte `mutmut` nur Sekundenbruchteile.
  Angenommen, ein Projekt hat 3000 Mutanten, und die Tests zu einem Mutanten laufen im Schnitt 2 Sekunden.
  Wie lange dauert ein vollständiger Lauf ohne Parallelisierung ungefähr?
  Wie würden Sie Mutation Testing in einem solchen Projekt einsetzen,
  und welche Rolle spielt dabei die viel billigere Überdeckungsmessung?
- [EQ] Eine Teamleitung möchte festlegen, dass Code nur noch übernommen wird,
  wenn `mutmut` einen Mutation Score von 100 % meldet.
  Was halten Sie davon, und was würden Sie stattdessen vorschlagen?

<!-- time estimate: 15 min -->

[ENDSECTION]
[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
