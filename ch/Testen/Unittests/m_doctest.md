title: "doctest: Ausführbare Beispiele in Docstrings"
stage: alpha
timevalue: 1.5
difficulty: 2
explains: Doctest
assumes: m_pytest
---

[SECTION::goal::idea]
- Ich kann Anwendungsbeispiele in Docstrings so schreiben, dass `doctest` sie automatisch prüft.
- Ich kann einschätzen, wofür Doctests taugen und wofür ich besser `pytest`-Tests schreibe.
[ENDSECTION]


[SECTION::background::default]
Beispiele sind oft der hilfreichste Teil einer Dokumentation:
`to_roman(1994)` mit dem Ergebnis `'MCMXCIV'` sagt mehr als ein Absatz Prosa.
Leider veralten Beispiele leicht:
Der Code ändert sich, das Beispiel in der Dokumentation nicht, und niemand merkt es.

Pythons Standardmodul `doctest` dreht den Spieß um:
Es führt die Beispiele in der Dokumentation aus und meldet, wenn eine Ausgabe nicht mehr stimmt.
So bleibt die Dokumentation korrekt, und nebenbei entstehen ein paar Tests.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

- Arbeiten Sie in Ihrem [TERMREF::Hilfsbereich].
- Aktivieren Sie ein venv, in dem `pytest` installiert ist
  (siehe [PARTREF::venv] und [PARTREF::m_pytest]).
  `doctest` gehört zur Standardbibliothek und muss nicht installiert werden.

Die Dokumentation des Moduls finden Sie hier:
[`doctest`-Dokumentation](https://docs.python.org/3/library/doctest.html)

Ein "Docstring" ist ein String-Literal, das als erste Anweisung in einem Modul,
einer Klasse oder einer Funktion steht.
Python merkt sich ihn als Dokumentation; `help(funktionsname)` zeigt ihn beispielsweise an.
Üblich sind dreifache Anführungszeichen, damit der Docstring mehrere Zeilen umfassen kann:

```python
def quadrat(x):
    """Liefert das Quadrat von x.

    >>> quadrat(3)
    9
    """
    return x * x
```

Die Zeilen ab `>>>` sehen aus wie eine Sitzung im interaktiven Python:
erst die Eingabe, darunter die Ausgabe.
Genau solche Zeilen sucht `doctest`, führt die Eingabe aus und vergleicht das Ergebnis
mit den Zeilen darunter, bis zur nächsten Leerzeile oder zur nächsten Zeile mit `>>>`.
Ein solches ausführbares Beispiel heißt [TERMREF::Doctest].

<!-- time estimate: 5 min -->


### Das Modul `romzahl.py`

Als Übungsgegenstand schreiben Sie ein kleines Modul,
das ganze Zahlen in römische Zahlen umrechnet und zurück.

[ER] Legen Sie die Datei `romzahl.py` mit zwei Funktionen an,
jede mit einem einzeiligen Docstring (die Beispiele kommen im nächsten Abschnitt):

- `to_roman(n)` wandelt eine ganze Zahl von 1 bis 3999 in eine römische Zahl in der heute
  üblichen Schreibweise um, beispielsweise 1994 in `'MCMXCIV'`.
  Für alle anderen ganzen Zahlen löst sie einen `ValueError` aus.
- `from_roman(s)` wandelt eine römische Zahl in eine ganze Zahl um.
  Für Strings, die keine römische Zahl in dieser Schreibweise sind,
  etwa `''`, `'IIII'`, `'IC'` oder `'ABC'`, löst sie einen `ValueError` aus.

[HINT::Wie rechne ich in römische Zahlen um?]
Benutzen Sie eine absteigend sortierte Tabelle aus Paaren (Wert, Zeichen),
die auch die Subtraktionsformen wie `CM` und `IV` enthält:

```python
WERTE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]
```

`to_roman`: Gehen Sie die Tabelle von oben nach unten durch.
Solange `n` mindestens so groß ist wie der Wert, hängen Sie das Zeichen an und ziehen den Wert ab.

`from_roman`: Gehen Sie dieselbe Tabelle durch.
Solange der restliche String mit dem Zeichen beginnt, addieren Sie den Wert
und schneiden das Zeichen ab.
[ENDHINT]

[HINT::Wie erkenne ich ungültige römische Zahlen?]
Am einfachsten mit `to_roman`:
Wandeln Sie Ihr Ergebnis zurück und vergleichen Sie es mit `s`.
Stimmen beide nicht überein oder bleibt beim Abarbeiten ein Rest übrig,
ist `s` keine römische Zahl in der üblichen Schreibweise.
Falls Sie ein Dictionary für die Ziffernwerte benutzen:
Unbekannte Zeichen dürfen keinen `KeyError` auslösen,
sondern müssen zu einem `ValueError` führen.
[ENDHINT]

Ob Ihre Funktionen richtig rechnen und ungültige Eingaben erkennen, prüft eine Testdatei.
Legen Sie `test_romzahl.py` mit folgendem Inhalt an:

```python
import pytest

from romzahl import from_roman, to_roman


def test_hin_und_zurueck():
    for n in range(1, 4000):
        assert from_roman(to_roman(n)) == n


def test_to_roman_ausserhalb():
    for n in [0, -1, 4000]:
        with pytest.raises(ValueError):
            to_roman(n)


def test_from_roman_ungueltig():
    for s in ["", "IIII", "IC", "ABC"]:
        with pytest.raises(ValueError):
            from_roman(s)
```

[EC] `pytest test_romzahl.py`

Schlägt ein Test fehl, korrigieren Sie `romzahl.py` und wiederholen Sie den Aufruf,
bis alle drei Tests bestehen.

<!-- time estimate: 25 min -->


### Der erste Doctest

- Starten Sie im Hilfsbereich das interaktive Python (`python` ohne Argumente).
- Probieren Sie Ihre Funktionen aus:
  zuerst `from romzahl import to_roman, from_roman`,
  dann einige Aufrufe wie `to_roman(4)`, `from_roman('MCMXCIV')`
  und einen Hin-und-zurück-Aufruf wie `from_roman(to_roman(2024))`.

[ER] Übernehmen Sie aus dieser Sitzung je zwei Aufrufe samt Ergebnis in die Docstrings
von `to_roman` und `from_roman`, und zwar genau so, wie sie in der Sitzung stehen:
die Zeile mit `>>>` und darunter die Ausgabe, eingerückt wie der übrige Docstring.
Bei `from_roman` soll einer der beiden Aufrufe ein Hin-und-zurück-Aufruf sein.
Den `import` brauchen Sie in den Docstrings nicht,
denn `doctest` führt die Beispiele im Namensraum des Moduls aus.

[EC] `python -m doctest romzahl.py`

[EC] `python -m doctest -v romzahl.py`

[EQ] Der erste Aufruf gibt nichts aus, der zweite sehr viel.
Was bedeutet die fehlende Ausgabe, und warum ist es sinnvoll, dass `doctest` ohne `-v` schweigt?
Was zählt die Zusammenfassung am Ende von `-v` als _item_ und was als _test_?

<!-- time estimate: 10 min -->


### Ein fehlschlagendes Beispiel

- Ändern Sie in einem Beispiel die erwartete Ausgabe absichtlich,
  etwa `'MCMXCIV'` in `'MCMXCVI'`.

[EC] `python -m doctest romzahl.py`

[EQ] Woran erkennen Sie in der Ausgabe, welches Beispiel in welcher Datei und Zeile
fehlgeschlagen ist, und was bedeuten `Expected` und `Got`?
`doctest` meldet nur, dass Beispiel und Code nicht zusammenpassen.
Woran entscheiden Sie im Ernstfall, ob das Beispiel oder der Code korrigiert werden muss?

- Machen Sie die Änderung wieder rückgängig.

<!-- time estimate: 5 min -->


### `repr` oder `print`?

- Rufen Sie im interaktiven Python `to_roman(4)` und `print(to_roman(4))` auf.
- Ersetzen Sie im Docstring von `to_roman` probehalber `'IV'` durch `IV`,
  rufen Sie `python -m doctest romzahl.py` auf und machen Sie die Änderung wieder rückgängig.

[EQ] Warum erscheint einmal `'IV'` mit und einmal `IV` ohne Anführungszeichen?
Welche der beiden Formen muss im Docstring unter `>>> to_roman(4)` stehen,
und was meldet `doctest`, wenn dort die andere steht?

[HINT::Woher kommen die Anführungszeichen?]
Probieren Sie `repr('IV')` und `str('IV')` aus.

[HINT::Ich sehe den Zusammenhang noch nicht]
Das interaktive Python zeigt den Wert eines Ausdrucks so an, wie ihn `repr()` liefert,
`print()` dagegen benutzt `str()`.
[ENDHINT]
[ENDHINT]

<!-- time estimate: 5 min -->


### Erwartete Ausnahmen

Auch eine Ausnahme kann ein lehrreiches Beispiel sein:
Wer `to_roman` benutzt, möchte wissen, was bei `to_roman(0)` passiert.

- Rufen Sie `to_roman(0)` im interaktiven Python auf.
  Python gibt einen Traceback aus.
- Lesen Sie in der Dokumentation den Abschnitt
  [What About Exceptions?](https://docs.python.org/3/library/doctest.html#what-about-exceptions)
  bis einschließlich des Beispiels nach dem Satz "Best practice is to omit the traceback stack".

[ER] Ergänzen Sie im Docstring von `to_roman` ein Beispiel für `to_roman(0)`.
Schreiben Sie den Traceback in der kurzen Form, die die Dokumentation empfiehlt.

[HINT::Wie sieht die kurze Form aus?]
Sie besteht aus drei Zeilen:
der Kopfzeile `Traceback (most recent call last):`,
einer eingerückten Zeile `...` anstelle des Aufrufstapels
und der letzten Zeile des Tracebacks mit Ausnahmetyp und Meldung,
also `ValueError:` gefolgt von genau Ihrer Meldung.
Den Aufrufstapel ignoriert `doctest`;
er würde sich ohnehin bei jeder Umstrukturierung des Codes ändern.
[ENDHINT]

<!-- time estimate: 10 min -->


### Instabile Ausgaben

- Ergänzen Sie in `romzahl.py` eine Funktion `ziffern(s)`,
  die die Menge (`set`) der in `s` vorkommenden Zeichen liefert.
- Beenden Sie eine laufende Sitzung des interaktiven Pythons und starten Sie es neu,
  denn ein bereits importiertes Modul lädt Python nicht automatisch nach.
- Importieren Sie `ziffern`, rufen Sie `ziffern('MCMXCIV')` auf und übernehmen Sie
  Aufruf und Ausgabe als Beispiel in den Docstring von `ziffern`.

[EC] Führen Sie `python -m doctest romzahl.py` dreimal hintereinander aus.

[EQ] Was beobachten Sie?
Warum kann ein Beispiel fehlschlagen, das Sie doch aus einer echten Sitzung kopiert haben?

[HINT::Ich verstehe die wechselnde Ausgabe nicht]
Eine Menge hat keine festgelegte Reihenfolge.
Python ordnet ihre Elemente intern nach Hashwerten an,
und die Hashwerte von Strings werden bei jedem Start von Python neu ausgewürfelt.
Der Abschnitt
[Warnings](https://docs.python.org/3/library/doctest.html#warnings)
der Dokumentation beschreibt genau diesen Fall.
[ENDHINT]

Ein Doctest vergleicht Text, nicht Werte.
Das wird zum Problem, wenn derselbe Wert nicht immer gleich aussieht.
Die Abhilfe besteht darin, Beispiele so zu formulieren, dass ihre Ausgabe stabil ist:

- Mengen: das Ergebnis sortieren (`sorted(...)`)
  oder mit einer erwarteten Menge vergleichen (`... == {...}` liefert `True`).
- Gleitkommazahlen: `0.1 + 0.2` ergibt `0.30000000000000004`;
  solche Nachkommastellen sind schlecht lesbar.
  Bei manchen Rechnungen, etwa `1000 ** 0.1`, können die letzten Stellen laut Dokumentation
  außerdem je nach Plattform abweichen.
  Runden Sie deshalb, beispielsweise mit `round(..., 2)`.
- Objektadressen: Die Standarddarstellung vieler Objekte enthält eine Speicheradresse,
  etwa `<object object at 0x1049d8b80>`, und die ändert sich bei jedem Lauf.
  Abhilfe schafft die Direktive `+ELLIPSIS`, siehe unten.

Dictionaries sind dagegen unproblematisch, solange die Einfügereihenfolge feststeht,
denn seit Python 3.7 behalten sie diese Reihenfolge bei.

[ER] Formulieren Sie das Beispiel in `ziffern` so um, dass seine Ausgabe stabil ist.
Zeigen Sie beide Varianten für Mengen, also Sortieren und Vergleichen.

Nicht jede Ausgabe lässt sich sinnvoll umformulieren, und manche ist zu lang für eine Zeile.
Dafür kennt `doctest`
[Direktiven](https://docs.python.org/3/library/doctest.html#option-flags):
Kommentare der Form `# doctest: +NAME` am Ende der Zeile mit `>>>`,
die den Vergleich für dieses eine Beispiel lockern.
Zwei davon sind besonders nützlich:

- `+ELLIPSIS`: `...` in der erwarteten Ausgabe passt auf beliebigen Text,
  beispielsweise `<object object at 0x...>`.
- `+NORMALIZE_WHITESPACE`: Alle Folgen von Leerraum, auch Zeilenumbrüche, gelten als gleich;
  eine lange Ausgabe darf man also dort umbrechen, wo ohnehin ein Leerzeichen steht.

[ER] Schreiben Sie ganz oben in `romzahl.py` einen Docstring für das Modul mit zwei Beispielen:

- `[to_roman(n) for n in range(1, 21)]`, dessen Ausgabe Sie mit `+NORMALIZE_WHITESPACE`
  auf zwei Zeilen verteilen;
- `[to_roman(n) for n in range(1, 4000)]`, dessen Ausgabe Sie mit `+ELLIPSIS`
  auf die ersten drei und die letzten zwei Elemente kürzen.

[EC] `python -m doctest -v romzahl.py`

<!-- time estimate: 20 min -->


### Doctests und `pytest` gemeinsam

In einem echten Projekt stehen Doctests nicht allein, sondern neben gewöhnlichen Tests
wie denen in `test_romzahl.py`.
`pytest` kann beide in einem Lauf ausführen, siehe
[How to run doctests](https://docs.pytest.org/en/stable/how-to/doctest.html).

[EC] `pytest --doctest-modules -v`

Beachten Sie, dass `pytest` jeden Docstring mit Beispielen als einen Testfall zählt,
nicht jedes einzelne Beispiel.

Doctests funktionieren auch in gewöhnlichen Textdateien, etwa in einer README.
Dort gibt es kein Modul, in dessen Namensraum die Beispiele laufen;
die Datei muss also selbst importieren, was sie benutzt.

[ER] Legen Sie eine Datei `README.txt` an mit einer Überschrift, einem Satz zum Modul
und einer kleinen Sitzung, die mit `>>> from romzahl import to_roman, from_roman` beginnt
und beide Funktionen je einmal aufruft.

[EC] `python -m doctest -v README.txt`

`pytest` sammelt Textdateien übrigens nur, wenn ihr Name dem Muster `test*.txt` entspricht;
für andere Namen gibt es die Option `--doctest-glob`.

<!-- time estimate: 10 min -->


### Doctest oder `pytest`?

In `test_romzahl.py` prüft eine einzige Schleife alle 3999 Zahlen hin und zurück,
in den Docstrings stehen nur wenige Beispiele.

[EQ] Wofür würden Sie künftig Doctests verwenden, wofür `pytest`-Tests?
Begründen Sie Ihre Einschätzung mit mindestens zwei Beobachtungen aus dieser Aufgabe.

<!-- time estimate: 5 min -->
[ENDSECTION]


[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Quellcode.md]
Gemeint sind `romzahl.py` und `README.txt` im Endzustand; `test_romzahl.py` ist vorgegeben.
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Knackpunkte: repr oder print, stabile Ausgaben, Reflexion]
[INCLUDE::ALT:]
[PROT::ALT:m_doctest.prot]
[ENDINSTRUCTOR]
