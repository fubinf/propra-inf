title: "hypothesis: Eigenschaften statt Einzelbeispiele testen"
stage: alpha
timevalue: 2.0
difficulty: 3
explains: Eigenschaftsbasiertes Testen
assumes: m_pytest, pytest_parametrize, pytest-Methodik-Blackbox, pip, venv
---

[SECTION::goal::idea]

- Ich kann für eine Funktion Eigenschaften formulieren, die für alle gültigen Eingaben gelten,
  und sie mit `hypothesis` prüfen.
- Ich kann erklären, wie `hypothesis` Gegenbeispiele findet und verkleinert.
- Ich kann beurteilen, wann eigenschaftsbasierte Tests beispielbasierte Tests sinnvoll ergänzen.

[ENDSECTION]


[SECTION::background::default]
Ein beispielbasierter Test prüft genau die Eingaben, an die jemand beim Schreiben gedacht hat.
Defekte stecken aber gern in den Fällen, an die niemand gedacht hat.

Eigenschaftsbasiertes Testen geht anders vor:
Sie beschreiben, was für _alle_ gültigen Eingaben gelten muss,
und ein Werkzeug sucht nach Eingaben, für die das nicht stimmt.
Findet es eine, verkleinert es sie so weit, dass der Defekt leicht zu erkennen ist.
In Python leistet das die Bibliothek `hypothesis`, die sich als Plugin in `pytest` einklinkt.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

Sie testen in dieser Aufgabe drei kleine Funktionen einer Anwendung,
mit der eine Gruppe ihre Rechnung im Restaurant aufteilt.

- Legen Sie in Ihrem [TERMREF::Arbeitsbereich] ein Verzeichnis `m_hypothesis/` an
  und arbeiten Sie darin.
- Aktivieren Sie Ihr venv (siehe [PARTREF::venv]).

[EC] `pip install pytest hypothesis`

Die Dokumentation von `hypothesis` finden Sie hier:
[HREF::https://hypothesis.readthedocs.io/en/latest/]

Die erste Funktion teilt den Rechnungsbetrag auf die Personen am Tisch auf.
Die Anwendung rechnet in ganzen Cent, damit keine Rundungsfehler von Gleitkommazahlen entstehen.
Legen Sie die Datei `aufteilen.py` mit folgendem Inhalt an:

```python
def aufteilen(betrag_cent, personen):
    """Teilt einen Betrag in Cent möglichst gerecht auf mehrere Personen auf.

    Liefert eine Liste mit einem Anteil (in Cent) pro Person.
    Die Anteile ergeben zusammen genau betrag_cent
    und unterscheiden sich um höchstens 1 Cent.
    Vorbedingung: betrag_cent >= 0 und personen >= 1.
    """
    anteil = round(betrag_cent / personen)
    rest = betrag_cent % personen
    return [anteil + 1] * rest + [anteil] * (personen - rest)
```

Eine Testerin hat dazu bereits einen Test mit drei sorgfältig gewählten Beispielen geschrieben,
darunter ein Betrag, der sich nicht glatt teilen lässt.
Legen Sie `test_aufteilen.py` mit folgendem Inhalt an:

```python
import pytest

from aufteilen import aufteilen


@pytest.mark.parametrize("betrag_cent, personen, erwartet", [
    (1000, 4, [250, 250, 250, 250]),
    (1000, 3, [334, 333, 333]),
    (4250, 1, [4250]),
])
def test_beispiele(betrag_cent, personen, erwartet):
    assert aufteilen(betrag_cent, personen) == erwartet
```

[EC] `pytest test_aufteilen.py`

Alle drei Tests bestehen.
Ob `aufteilen` damit korrekt ist, finden Sie in den nächsten Schritten heraus.

<!-- time estimate: 10 min -->


### Die erste Eigenschaft

Der Docstring von `aufteilen` verspricht unter anderem:
Die Anteile ergeben zusammen genau `betrag_cent`.
Das soll für _jeden_ gültigen Betrag und _jede_ gültige Personenzahl gelten, nicht nur für drei.
Eine solche Aussage über alle gültigen Eingaben heißt "Eigenschaft" (_property_).
Wer Eigenschaften statt Einzelbeispiele prüft,
betreibt [TERMREF2::Eigenschaftsbasiertes Testen::eigenschaftsbasiertes Testen].

In `hypothesis` schreiben Sie dafür eine Testfunktion mit Parametern
und setzen den [TERMREF2::Decorator::Dekorator] `@given` davor.
`@given` erhält für jeden Parameter eine "Strategie",
die beschreibt, welche Werte `hypothesis` erzeugen soll.
Die Strategien stehen im Modul `hypothesis.strategies`, das man üblicherweise als `st` importiert.
`hypothesis` ruft die Testfunktion dann mit vielen erzeugten Werten auf, standardmäßig 100-mal.

Lesen Sie in der Einführung die Abschnitte "Defining a simple test"
und "Tests with multiple arguments":
[HREF::https://hypothesis.readthedocs.io/en/latest/tutorial/introduction.html]

Ganze Zahlen erzeugt die Strategie `st.integers()`.
Mit `min_value` und `max_value` begrenzen Sie den Bereich,
siehe den Eintrag `integers` in der Übersicht der Strategien:
[HREF::https://hypothesis.readthedocs.io/en/latest/reference/strategies.html]

[ER] Schreiben Sie in `test_aufteilen.py` einen Test `test_summe`,
der die Eigenschaft "Die Anteile ergeben zusammen genau `betrag_cent`" prüft.
Lassen Sie `hypothesis` Beträge von 0 bis 100 000 Cent und 1 bis 100 Personen erzeugen.

Die Untergrenzen folgen aus der Vorbedingung im Docstring.
Die Obergrenzen sind eine bewusste Entscheidung für den Test:
Ohne sie erzeugt `hypothesis` auch riesige Personenzahlen,
`aufteilen` baut dann eine entsprechend lange Liste,
und der Test belegt immer mehr Speicher, statt fertig zu werden.

[HINT::Wie sieht ein Test mit `@given` aus?]
Ein Beispiel mit einem Parameter und einer anderen Eigenschaft:

```python
from hypothesis import given, strategies as st


@given(st.integers(min_value=1, max_value=6))
def test_wuerfel(augen):
    assert 1 <= augen <= 6
```

Bei zwei Parametern übergeben Sie `@given` zwei Strategien, in der Reihenfolge der Parameter.
[ENDHINT]

Die Option `--hypothesis-show-statistics` lässt `hypothesis` nach dem Lauf berichten,
was es in seinen einzelnen Phasen getan hat.

[EC] `pytest --hypothesis-show-statistics test_aufteilen.py`

[EQ] Was steht unter `Failing test case`, und was liefert `aufteilen` für diese Eingabe?
(Ältere Versionen von `hypothesis` schreiben dort `Falsifying example`.)
`hypothesis` durfte Beträge bis 100 000 Cent erzeugen.
Warum ist das gemeldete Gegenbeispiel trotzdem so klein?
Begründen Sie Ihre Antwort mit der Statistik.

[HINT::Meine Statistik zeigt keine `shrink phase`]
Dann haben Sie den Test vermutlich schon einmal ausgeführt.
Warum das eine Rolle spielt, klären Sie weiter unten.
Löschen Sie das Verzeichnis `.hypothesis/` und rufen Sie das Kommando noch einmal auf.
[ENDHINT]

[HINT::Was passiert in der `shrink phase`?]
Vergleichen Sie die Zahl der fehlschlagenden Testfälle
in der `generate phase` und in der `shrink phase`.
"to shrink" heißt "schrumpfen".
[ENDHINT]

[HINT::Mein Gegenbeispiel ist gar nicht klein]
Das kommt gelegentlich vor.
Beim Verkleinern probiert `hypothesis` nur bestimmte kleinere Eingaben aus
und hört auf, sobald keine davon mehr fehlschlägt.
Es findet deshalb nicht immer das kleinstmögliche Gegenbeispiel.
Löschen Sie das Verzeichnis `.hypothesis/` und rufen Sie das Kommando noch einmal auf.
[ENDHINT]

[EC] Rufen Sie dasselbe Kommando noch einmal auf.

Vergleichen Sie Gegenbeispiel und Statistik mit dem ersten Lauf.
`hypothesis` hat beim ersten Lauf ein Verzeichnis `.hypothesis/` angelegt.

- Sehen Sie sich mit `ls -aR .hypothesis` an, was darin steht.
  Das Unterverzeichnis `constants/` können Sie ignorieren:
  Dort merkt sich `hypothesis` Konstanten aus Ihrem Code, die es gelegentlich als Eingaben nutzt.
  Auf den Rest kommen Sie weiter unten zurück.

<!-- time estimate: 25 min -->


### Weitere Eigenschaften und der Defekt

Der Docstring macht außer der Summe noch zwei weitere Zusagen.

[ER] Schreiben Sie für jede der beiden Zusagen einen eigenen Test mit `@given`,
mit denselben Strategien wie in `test_summe`.

[HINT::Welche Zusagen sind gemeint?]
Die Liste enthält einen Anteil pro Person,
und die Anteile unterscheiden sich um höchstens 1 Cent.
[ENDHINT]

[HINT::Wie prüfe ich "unterscheiden sich um höchstens 1 Cent"?]
Es genügt, den größten und den kleinsten Anteil zu vergleichen.
[ENDHINT]

- Führen Sie die Tests aus und sehen Sie nach, welche fehlschlagen.

[ER] Finden Sie mithilfe des Gegenbeispiels den Defekt in `aufteilen` und beheben Sie ihn.

[HINT::Wo steckt der Defekt?]
Rechnen Sie das Gegenbeispiel von Hand nach:
Welche Werte haben `anteil` und `rest`, und welche müssten sie haben?

[HINT::Ich sehe es immer noch nicht]
`anteil` soll der Betrag sein, der jeder Person mindestens zusteht.
Welcher Python-Operator liefert den ganzzahligen Anteil einer Division, ohne zu runden?
[ENDHINT]
[ENDHINT]

[EC] `pytest test_aufteilen.py`

<!-- time estimate: 20 min -->


### Strategien und Wiederholbarkeit

`hypothesis` bietet einen weiteren Weg, ungültige Eingaben auszuschließen:
`assume(bedingung)` im Test verwirft den aktuellen Testfall, wenn die Bedingung nicht gilt.
`hypothesis` zählt ihn dann als ungültig (_invalid_) und erzeugt einen neuen.
Legen Sie probehalber die Datei `test_assume.py` an,
die die Summe mit `assume()` statt mit Grenzen in den Strategien prüft:

```python
from hypothesis import assume, given, strategies as st

from aufteilen import aufteilen


@given(st.integers(), st.integers())
def test_summe_mit_assume(betrag_cent, personen):
    assume(0 <= betrag_cent <= 100_000)
    assume(1 <= personen <= 100)
    assert sum(aufteilen(betrag_cent, personen)) == betrag_cent
```

[EC] `pytest test_assume.py`

[EQ] Warum scheitert dieser Test, obwohl `aufteilen` inzwischen korrekt ist?
Warum ist es besser, den Wertebereich wie in `test_summe` mit `min_value` und `max_value`
festzulegen?

Die Fehlermeldung ist lang, enthält aber Hinweise zu beiden Fragen; lesen Sie sie vollständig.

- Löschen Sie `test_assume.py` wieder.

Das Gegenbeispiel aus [EREFC::3] soll künftig bei jedem Lauf geprüft werden,
unabhängig davon, welche Werte `hypothesis` gerade erzeugt.
Dafür gibt es den Dekorator `@example`, siehe den Abschnitt
"Using @example to run a specific input":
[HREF::https://hypothesis.readthedocs.io/en/latest/tutorial/replaying-failures.html]

[ER] Ergänzen Sie `test_summe` um Ihr Gegenbeispiel als `@example`.

Ein solcher Testfall ist ein [TERMREF::Regressionstest]:
Er sorgt dafür, dass der behobene Defekt nicht unbemerkt zurückkehrt.

- Führen Sie die Tests noch einmal aus.

In [EREFC::4] meldete `hypothesis` sofort wieder dasselbe Gegenbeispiel,
obwohl es seine Eingaben zufällig erzeugt.
Die Erklärung liegt im Verzeichnis `.hypothesis/`.

- Sehen Sie sich mit `ls -aR .hypothesis` noch einmal an, was jetzt darin steht,
  und vergleichen Sie mit dem Stand nach [EREFC::4].
- Lesen Sie die Datei `.hypothesis/.gitignore`
  und auf der oben verlinkten Seite den Abschnitt "The Hypothesis database".

[EQ] Wozu dient das Verzeichnis `.hypothesis/`, und gehört es in Ihr Git-Repo?
Warum ergänzt man das Gegenbeispiel trotzdem mit `@example`,
statt sich auf `.hypothesis/` zu verlassen?

<!-- time estimate: 20 min -->


### Hin und zurück

Die beiden anderen Funktionen halten fest, wer sich eine Rechnung geteilt hat:
`kodiere` fasst die Namen zu einem einzigen String zusammen,
etwa für ein Textfeld in einer Datenbank,
und `dekodiere` macht das wieder rückgängig.
Legen Sie `namensliste.py` mit folgendem Inhalt an:

```python
TRENNER = ","


def kodiere(namen):
    """Fasst eine Liste beliebiger Strings zu einem einzigen String zusammen."""
    return TRENNER.join(namen)


def dekodiere(text):
    """Macht kodiere() rückgängig."""
    if text == "":
        return []
    return text.split(TRENNER)
```

Auch dazu hat die Testerin Beispiele geschrieben.
Legen Sie `test_namensliste.py` mit folgendem Inhalt an:

```python
import pytest

from namensliste import dekodiere, kodiere


@pytest.mark.parametrize("namen", [
    ["Ada", "Ben", "Cem"],
    ["Ada"],
    [],
])
def test_beispiele(namen):
    assert dekodiere(kodiere(namen)) == namen
```

In diesem Test steckt bereits eine Eigenschaft, allerdings nur für drei Listen:
Wer eine Liste kodiert und wieder dekodiert, erhält die ursprüngliche Liste zurück.
Eine solche "Hin-und-zurück-Eigenschaft" (_round trip_) passt zu jedem Paar von Funktionen,
von denen die eine die andere umkehren soll, etwa Speichern und Laden oder Packen und Entpacken.

Listen erzeugt die Strategie `st.lists(...)`;
ihr übergeben Sie eine Strategie für die Elemente.
Beliebige Strings erzeugt `st.text()`.

[ER] Schreiben Sie in `test_namensliste.py` einen Test `test_hin_und_zurueck`,
der die Eigenschaft mit `st.lists(st.text())` prüft.

[EC] `pytest test_namensliste.py`

[EQ] Welches Gegenbeispiel hat `hypothesis` gefunden, und was geht dabei schief?
Die Testerin hat die leere Liste ausdrücklich getestet.
Warum übersieht man diesen Fall trotzdem leicht, wenn man Testfälle über Äquivalenzklassen
und Randwerte auswählt (siehe [PARTREF::pytest-Methodik-Blackbox])?

[ER] Beheben Sie den Defekt in `namensliste.py`.
Ändern Sie dabei nicht die Strategie im Test:
Die Funktionen sollen mit beliebigen Strings umgehen können, auch mit leeren.

[HINT::Nach meiner Korrektur findet `hypothesis` ein neues Gegenbeispiel]
Das ist kein Rückschritt, sondern ein weiterer Defekt derselben Art.
Fragen Sie sich allgemein:
Gibt es zwei verschiedene Listen, aus denen `kodiere` denselben String macht?
Dann kann `dekodiere` sie nicht auseinanderhalten, und kein Sonderfall in `dekodiere` hilft.
Das Format selbst muss sich ändern.
[ENDHINT]

[HINT::Muss ich mir ein eigenes Format ausdenken?]
Nein.
Das Standardmodul `json` verwandelt eine Liste von Strings in einen String und zurück:
`json.dumps(...)` und `json.loads(...)`.
Ein eigenes Format geht auch, beispielsweise indem Sie Kommas in Namen maskieren
und hinter _jeden_ Namen ein Komma setzen.
[ENDHINT]

[EC] `pytest`

<!-- time estimate: 25 min -->


### Reflexion

Typische Arten von Eigenschaften sind:

- Hin und zurück: Eine Funktion macht eine andere rückgängig.
- Invariante: Etwas gilt immer oder bleibt erhalten, etwa eine Summe oder eine Länge.
- Vergleich mit einer Referenzimplementierung: Eine einfache, offensichtlich richtige,
  aber vielleicht langsame Fassung muss dieselben Ergebnisse liefern.
- "Stürzt nicht ab": Für keine gültige Eingabe löst die Funktion eine unerwartete Ausnahme aus.

[EQ] Ordnen Sie jeden Ihrer `@given`-Tests einer dieser Arten zu.
Wie könnte ein Test der Art "Vergleich mit einer Referenzimplementierung"
für `aufteilen` aussehen?

[EQ] Ein Test mit `@given` besteht.
Was wissen Sie damit über die Funktion, und was wissen Sie nicht?
Bedenken Sie auch, dass eine Eigenschaft selbst falsch oder zu schwach sein kann:
Welche Ihrer Tests hätte die ursprüngliche Fassung von `aufteilen` bestanden?
Wann lohnen sich eigenschaftsbasierte Tests zusätzlich zu beispielbasierten, wann eher nicht?

<!-- time estimate: 15 min -->
[ENDSECTION]


[SECTION::submission::reflection,trace,snippet]
[INCLUDE::/_include/Submission-Quellcode.md]
Gemeint sind `aufteilen.py`, `test_aufteilen.py`, `namensliste.py` und `test_namensliste.py`
im Endzustand.
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Knackpunkte: allgemeine Eigenschaften, Shrinking, Aussagekraft grüner Tests]
[INCLUDE::ALT:]
[PROT::ALT:m_hypothesis.prot]
[ENDINSTRUCTOR]
