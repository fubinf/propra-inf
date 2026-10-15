title: Testen und Debugging voneinander abgrenzen
stage: alpha
timevalue: 1.0
difficulty: 2
explains: Debugging, Test
assumes: m_pytest, venv, print-Debugging, Fehler-Defekt-Versagen
---

[SECTION::goal::idea]

- Ich kann an einem konkreten Defekt zeigen, was Testen leistet und was Debugging leistet.
- Ich kann begründen, warum ein fehlschlagender Test den Defekt meist nur grob eingrenzt
  und ein bestandener Test keine Defektfreiheit belegt.

[ENDSECTION]


[SECTION::background::default]

Ein Test ist rot – und jetzt?
Wer Testen und Debugging nicht auseinanderhält, sucht den Defekt gern dort, wo `pytest` gerade
hinzeigt, oder hält einen grünen Testlauf für den Beweis, dass alles stimmt.
Beides kostet im Alltag viel Zeit.
An einem kleinen Beispiel erleben Sie hier, wo das eine aufhört und das andere anfängt.

[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

Ein Verkehrsbetrieb berechnet mit einem kleinen Python-Modul die Fahrpreise für Reisegruppen.
Welche Altersgruppe welchen Tarif zahlt, steht im Docstring von `tarifgruppe()`.

- Legen Sie in Ihrem [TERMREF::Hilfsbereich] ein Verzeichnis `testabgrenzung` an
  und wechseln Sie hinein.
- Aktivieren Sie ein `venv`, in dem `pytest` installiert ist
  (siehe [PARTREF::venv] und [PARTREF::m_pytest]).
- Legen Sie die Datei `tarif.py` mit folgendem Inhalt an:

```python
PREISE = {"frei": 0.00, "kind": 2.50, "erwachsen": 4.00, "senior": 3.00}


def tarifgruppe(alter):
    """Kinder unter 6 fahren frei, Kinder unter 14 zahlen den Kindertarif,
    ab 65 gilt der Seniorentarif, alle anderen zahlen den Erwachsenentarif."""
    if alter < 6:
        return "frei"
    if alter < 14:
        return "kind"
    if alter > 65:
        return "senior"
    return "erwachsen"


def gesamtpreis(alter_liste):
    """Summe der Fahrpreise für eine Reisegruppe."""
    summe = 0.0
    for alter in alter_liste:
        gruppe = tarifgruppe(alter)
        summe += PREISE[gruppe]
    return summe
```

- Legen Sie daneben die Testdatei `test_tarif.py` an:

```python
from tarif import gesamtpreis


def test_familie():
    assert gesamtpreis([41, 39, 10, 4]) == 10.50


def test_grossfamilie():
    assert gesamtpreis([70, 65, 41, 14, 13, 6, 5]) == 19.00
```

<!-- time estimate: 10 min -->


### Testen: Ein Versagen wird sichtbar

Ein [TERMREF::Test] vergleicht das tatsächliche Verhalten eines Programms mit einer Erwartung.
Hier stecken die Erwartungen in den beiden `assert`-Zeilen.

[EC] `pytest test_tarif.py`

[EQ] Was erfahren Sie aus der Ausgabe über das [TERMREF::Versagen]:
Welcher Test schlägt fehl, mit welcher Eingabe, welcher Wert wurde erwartet und welcher geliefert?
Auf welche Codezeile zeigt `pytest`, und steckt der [TERMREF::Defekt] in dieser Zeile?

[HINT::Wie kann ich das beurteilen, ohne den Defekt zu kennen?]
Rechnen Sie die Erwartung `19.00` anhand des Docstrings von `tarifgruppe()`
und der Preise in `PREISE` nach.
[ENDHINT]

<!-- time estimate: 10 min -->


### Debugging: Vom Versagen zum Defekt

Sie wissen jetzt, _dass_ `gesamtpreis()` falsch rechnet, aber noch nicht, _wo_ der Defekt steckt.
Diese Suche ist [TERMREF::Debugging].
Der fehlschlagende Test ist dafür ein guter Ausgangspunkt:
Er führt das Versagen bei jedem Aufruf zuverlässig wieder herbei.

Grenzen Sie den Defekt mit print-Debugging ein, wie Sie es aus [PARTREF::print-Debugging] kennen.
Auch wenn Sie den Defekt beim Lesen des Codes schon vermuten:
Prüfen Sie Ihre Vermutung an der tatsächlichen Ausführung, statt zu raten.
Ergänzen Sie dazu in der Schleife von `gesamtpreis()` eine `print()`-Anweisung,
die für jede Person das Alter, die ermittelte Tarifgruppe und die Zwischensumme ausgibt.

[HINT::Wie sieht die `print()`-Anweisung aus?]
Direkt nach der Zeile `summe += PREISE[gruppe]` passt
`print(f"{alter=} {gruppe=} {summe=}")`.
Die Schreibweise `{alter=}` gibt Name und Wert der Variable aus.
[ENDHINT]

[EC] `pytest test_tarif.py`

Ihre Ausgaben zeigt `pytest` nur beim fehlschlagenden Test an, im Abschnitt `Captured stdout call`.

[EQ] Bei welcher Person geht die Rechnung schief?
In welcher Zeile von `tarif.py` steckt der Defekt, und wie lautet die Korrektur?
Beschreiben Sie für diesen Fall den Weg vom Defekt über den [TERMREF::Fehlerzustand]
bis zum Versagen.

<!-- time estimate: 15 min -->


### Korrigieren und erneut testen

- Korrigieren Sie den Defekt in `tarif.py`.
- Entfernen Sie die `print()`-Anweisung wieder.

[EC] `pytest -v test_tarif.py`

[EQ] Die `print()`-Anweisung haben Sie wieder gelöscht, die Tests dagegen behalten Sie.
Warum ist das sinnvoll?
Welche Aufgabe übernimmt `test_grossfamilie` von nun an?

<!-- time estimate: 10 min -->


### Was ein grüner Test aussagt

[EQ] `test_familie` war schon vor Ihrer Korrektur grün, obwohl der Defekt im Code steckte.
Warum hat der Defekt bei diesem Test kein Versagen ausgelöst?
Was sagt ein grüner Testlauf demnach über die Defektfreiheit eines Programms aus?

<!-- time estimate: 10 min -->

[ENDSECTION]


[SECTION::submission::reflection,trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Testen zeigt das Versagen, Debugging findet den Defekt]
[INCLUDE::ALT:]
[PROT::ALT:Testabgrenzung.prot]
[ENDINSTRUCTOR]
