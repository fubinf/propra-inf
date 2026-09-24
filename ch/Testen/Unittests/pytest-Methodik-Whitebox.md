title: "Whitebox-Testing: Testmethodik und Anwendung mit pytest"
stage: alpha
timevalue: 2.0
difficulty: 3
assumes: m_pytest, pytest-Methodik-Blackbox, Fehler-Defekt-Versagen
explains: Überdeckung
---

[SECTION::goal::idea]

- Ich verstehe, wie mir der Blick in den Code hilft, Lücken in meiner Testmenge zu finden.
- Ich kenne die Überdeckungskriterien Anweisungs-, Zweig-, Schleifen-, Bedingungs- und Pfadüberdeckung
  und weiß, welches davon schärfer ist als welches.
- Ich kann Anweisungs- und Zweigüberdeckung mit `pytest-cov` messen.

[ENDSECTION]
[SECTION::background::default]

Beim Blackbox-Testen denkt man sich Testfälle nur anhand der Spezifikation aus.
Dabei übersieht man leicht, dass die Implementierung intern mehr Fälle unterscheidet, als man denkt –
und genau in diesen Fällen stecken gern Defekte.
Whitebox-Testen schaut deshalb in den Code und fragt: Welche Teile davon haben meine Tests noch nie
ausgeführt?
Das funktioniert sogar dann, wenn einem niemand eine schriftliche Spezifikation gegeben hat.

[ENDSECTION]

[SECTION::instructions::detailed]

### Worum es geht
<!-- time estimate: 10 min -->

Whitebox-Tests (auch: strukturelle Tests) nutzen die Struktur des Codes, um Testeingaben auszuwählen.
Ziel ist, dass der Code _robust_ ist: Er soll sich auch in selten durchlaufenen Ecken richtig verhalten.

**Erwartete Ergebnisse** leitet man dabei aber niemals aus dem Code ab, sondern immer aus dem,
was die Funktion leisten _soll_.
Fehlt eine schriftliche Spezifikation, muss man das erschließen, z.B. aus dem Zweck, dem Namen
und dem Docstring der Funktion – aber eben nicht aus ihrem Code.
Wer das erwartete Ergebnis im Code nachliest, bestätigt nur, dass der Code tut, was er tut,
und findet so allenfalls Abstürze, aber keine falschen Ergebnisse.
Der Code sagt uns also, _welche Eingaben_ interessant sind; die Spezifikation sagt uns,
_was herauskommen muss_.

[TERMREF2::Überdeckung::-skriterien] (engl. coverage criteria) legen fest, welche Situationen im Code
die Tests herbeigeführt haben müssen, z.B. dass jede Anweisung ausgeführt oder jeder Zweig genommen wurde.
Gemessen wird dann, welcher Anteil dieser Situationen tatsächlich erreicht wurde.
Ein Überdeckungskriterium ist keine Methode: Es sagt Ihnen nicht, wie Sie Testfälle finden,
sondern nur, wie weit Sie schon gekommen sind.
Die passenden Testfälle auszudenken bleibt Ihre Aufgabe.

Ein Kriterium A ist **schärfer** als ein Kriterium B, wenn jede Testmenge, die A vollständig erfüllt,
automatisch auch B vollständig erfüllt, aber nicht umgekehrt.

### Vorbereitung
<!-- time estimate: 5 min -->

Die beiden folgenden Funktionen stammen aus dem Open-Source-Projekt keon/algorithms von GitHub,
einer Sammlung von Algorithmen in Python.
Eine der beiden Funktionen haben wir gegenüber dem Original leicht verändert:
Sie enthält jetzt einen Defekt.
Ihre Whitebox-Tests sollen ihn finden.

Legen Sie die Datei `whitebox.py` mit folgendem Inhalt an:

```python
def binary_search_recur(array, low, high, val):
    """
    Rekursive Binärsuche im sortierten `array` zwischen den Indizes `low` und `high`.
    Liefert den Index von `val` oder -1, falls `val` dort nicht vorkommt.
    """
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if val < array[mid]:
        return binary_search_recur(array, low, mid - 1, val)
    elif val > array[mid]:
        return binary_search_recur(array, mid + 1, high, val)
    else:
        return mid


def cocktail_shaker_sort(arr):
    """
    Sortiert `arr` aufsteigend (an Ort und Stelle) und liefert es zurück.
    Cocktail Shaker Sort ist eine Variante von Bubble Sort,
    die abwechselnd vorwärts und rückwärts durch die Liste läuft.
    """
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    while swapped:
        swapped = False

        # Vorwärts durchlaufen
        for i in range(1, n - 1):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

        if not swapped:  # Frühzeitiger Exit
            return arr

        swapped = False

        # Rückwärts durchlaufen
        for i in range(n - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

    return arr
```

Legen Sie für Ihre Tests die Datei `test_whitebox.py` an.

Zum Messen der Überdeckung benutzen wir das pytest-Plugin `pytest-cov`.
Installieren Sie es mit `pip install pytest-cov`.
Die Option `--cov=whitebox` misst die Überdeckung des Moduls `whitebox`,
`--cov-report=term-missing` listet zusätzlich die Zeilen auf, die nie ausgeführt wurden.
Mehr zu `pytest-cov` (Konfiguration, HTML-Berichte, Aussagekraft von Überdeckungswerten)
finden Sie in [PARTREF::testcoverage].

### Anweisungsüberdeckung
<!-- time estimate: 15 min -->

**Anweisungsüberdeckung** (statement coverage) verlangt, dass jede Anweisung mindestens einmal
ausgeführt wird.
Eine Anweisung ist in Python z.B. eine Zuweisung, ein `return`, ein `if` samt seiner Bedingung –
und auch die `def`-Zeile selbst.
`def` ist nämlich keine bloße Deklaration, sondern wird beim Import ausgeführt:
Sie erzeugt ein Funktionsobjekt und bindet es an den Namen.
Definiert man denselben Namen später ein zweites Mal, gewinnt die zweite Definition;
wer die erste vorher einer anderen Variablen zugewiesen hat, kann sie trotzdem weiter benutzen.
Die `def`-Zeilen sind also schon durch den Import überdeckt.

- [ER] Schreiben Sie eine Testfunktion `test_statement_coverage_binary_search()`,
  die jede Anweisung von `binary_search_recur()` mindestens einmal ausführt.
  Kommen Sie mit möglichst wenigen Aufrufen aus.
- [EC] Messen Sie nur für diese Testfunktion die Überdeckung:
  `pytest --cov=whitebox --cov-report=term-missing -k statement`.
  `-k statement` wählt nur die Testfunktionen aus, deren Name `statement` enthält.
  Die Spalte `Missing` nennt die Zeilen, die nie ausgeführt wurden.
  Die Zeilen von `cocktail_shaker_sort()` dürfen dort noch auftauchen, die von `binary_search_recur()` nicht.

[HINT::Ich bekomme `return -1` nicht ausgeführt]
Rufen Sie die Funktion so auf, wie ein Benutzer es tun würde: mit `low=0` und `high=len(array)-1`.
Wann kommt es dann im Laufe der Rekursion zu `low > high`?
[ENDHINT]

### Zweigüberdeckung
<!-- time estimate: 20 min -->

Eine **Entscheidung** ist eine Stelle, an der das Programm zwischen zwei Fortsetzungen wählt:
`if`, `elif`, `while` sowie `for` (noch ein Element da oder nicht?).
Die beiden möglichen Fortsetzungen heißen **Zweige**.
Auch ein `if` ohne `else` hat zwei Zweige: Der eine führt in den `if`-Block,
der andere springt direkt an ihm vorbei zur nächsten Anweisung.

**Zweigüberdeckung** (branch coverage) verlangt, dass jeder Zweig jeder Entscheidung
mindestens einmal genommen wird.
Weil jede Anweisung in irgendeinem Zweig liegt, ist Zweigüberdeckung schärfer als Anweisungsüberdeckung:
Bei `if x > 0: y = 1` genügt `x=5` für Anweisungsüberdeckung, aber nicht für Zweigüberdeckung.
`pytest-cov` misst Zweigüberdeckung, wenn man zusätzlich `--cov-branch` angibt.
Im Bericht erscheint dann die Spalte `BrPart` (Entscheidungen, von denen nur ein Zweig genommen wurde),
und unter `Missing` stehen fehlende Zweige in der Form `12->14`.

- [EC] Messen Sie Ihre Testfunktion aus [EREFR::1] erneut, diesmal mit `--cov-branch`.
- [EQ] Erreichen Ihre Tests auch Zweigüberdeckung für `binary_search_recur()`?
  Erklären Sie anhand des Codes, warum das bei dieser Funktion so ist.
- [ER] Schreiben Sie eine Testfunktion `test_branch_coverage_cocktail_sort()`,
  die Zweigüberdeckung für `cocktail_shaker_sort()` erreicht.
  Leiten Sie die erwarteten Ergebnisse aus der Spezifikation ab
  (Tipp: Vergleichen Sie mit `sorted()` und übergeben Sie eine Kopie der Eingabeliste).
- [EC] Weisen Sie die Zweigüberdeckung nach:
  `pytest --cov=whitebox --cov-branch --cov-report=term-missing -k branch`.

[HINT::Ich erreiche den Zweig nicht, in dem die `while`-Schleife regulär endet]
Die `while`-Schleife endet regulär nur, wenn im Rückwärtslauf nichts mehr zu tauschen war,
im Vorwärtslauf davor aber schon.
Welche kurze Liste wird durch einen einzigen Tausch im Vorwärtslauf vollständig sortiert?
[ENDHINT]

### Schleifenüberdeckung
<!-- time estimate: 20 min -->

Schleifen sind besonders fehleranfällig, vor allem an ihren Grenzen.
Zweigüberdeckung verlangt aber nur, dass eine Schleife irgendwann betreten und irgendwann verlassen wird.
**Schleifenüberdeckung** (loop coverage) verlangt deshalb zusätzlich, dass jede Schleife in den Tests
einmal **0-mal**, einmal **genau 1-mal** und einmal **mehrmals** durchlaufen wird.
Manche dieser Fälle sind bei einer bestimmten Schleife unmöglich; die entfallen dann.
`pytest-cov` misst Schleifenüberdeckung nicht, hier müssen Sie selbst nachdenken.

- [ER] Schreiben Sie eine Testfunktion `test_loop_coverage_cocktail_sort()`,
  die für jede der drei Schleifen in `cocktail_shaker_sort()` jeden möglichen der drei Fälle herbeiführt.
  Schreiben Sie an jeden Aufruf einen Kommentar, welche Fälle er abdeckt.
  Wählen Sie, wo immer möglich, Eingaben, die tatsächlich etwas zu sortieren haben:
  Eine bereits sortierte Liste ist ein schwacher Testfall.
- [EQ] Welche der insgesamt neun Fälle (drei Schleifen × drei Fälle) sind unmöglich, und warum?

[HINT::Ich weiß nicht, wie oft die `for`-Schleifen bei einer bestimmten Listenlänge laufen]
Rechnen Sie für `n = 0, 1, 2, 3, 4` aus, wie viele Werte `range(1, n - 1)` bzw. `range(n - 1, 0, -1)` liefern.
Beachten Sie außerdem, unter welcher Bedingung der Rückwärtslauf überhaupt erreicht wird.
[ENDHINT]

### Den Defekt finden
<!-- time estimate: 10 min -->

Spätestens jetzt sollte einer Ihrer Tests fehlschlagen.
Reparieren Sie `whitebox.py` nicht; der fehlschlagende Test bleibt in Ihrer Abgabe stehen
und dokumentiert das Versagen.
Falls noch keiner Ihrer Tests fehlschlägt, prüfen Sie, ob Ihre Tests zur Schleifenüberdeckung
wirklich etwas zu sortieren hatten.

- [EQ] Beschreiben Sie das [TERMREF::Versagen]: Mit welcher Eingabe, welches erwartete, welches tatsächliche Ergebnis?
- [EQ] Beschreiben Sie den [TERMREF::Defekt]: Welche Stelle im Code ist falsch, wie müsste sie lauten,
  und warum führt sie zu dem Versagen?
- [EQ] Welches Überdeckungskriterium hat Sie zu dem entscheidenden Testfall geführt?
  Hätte Zweigüberdeckung allein zuverlässig dorthin geführt?

### Bedingungsüberdeckung
<!-- time estimate: 20 min -->

Der Ausdruck hinter `if` oder `while` kann aus mehreren Teilen zusammengesetzt sein,
z.B. `if (a > 0 and b > 0) or c > 10:`.
Die Teile, die selbst kein `and`, `or` oder `not` enthalten, heißen **atomare Bedingungen**;
hier sind das `a > 0`, `b > 0` und `c > 10`.
Mit „Bedingung“ ist im Folgenden immer eine atomare Bedingung gemeint.

**Bedingungsüberdeckung** (condition coverage) verlangt, dass jede atomare Bedingung mindestens einmal
zu `True` und mindestens einmal zu `False` ausgewertet wird.
Die Entscheidung einer `for`-Schleife („noch ein Element da?“) zählt dabei als eine atomare Bedingung.
In `whitebox.py` bringt dieses Kriterium nichts Neues, denn dort enthält keine Entscheidung
ein `and` oder `or`.
Für diesen Abschnitt benutzen wir deshalb folgende Funktion:

```python
def complex_check(a, b, c):
    if (a > 0 and b > 0) or c > 10:
        return "pass"
    return "fail"
```

**Kurzschlussauswertung:** Python wertet `and` und `or` von links nach rechts aus
und hört auf, sobald das Ergebnis feststeht.
Bei `a > 0 and b > 0` wird `b > 0` also gar nicht erst ausgewertet, wenn `a > 0` schon `False` ist.
Für die Bedingungsüberdeckung zählen nur Bedingungen, die tatsächlich ausgewertet wurden.

`pytest-cov` misst Bedingungsüberdeckung nicht; auch hier sind Sie selbst gefragt.

- [ER] Fügen Sie `complex_check()` zu `whitebox.py` hinzu und schreiben Sie eine Testfunktion
  `test_condition_coverage_complex_check()`, die Bedingungsüberdeckung erreicht.
  Schreiben Sie an jeden Aufruf einen Kommentar, welche Bedingungen mit welchem Wert ausgewertet werden.
- [EQ] Geben Sie eine Testmenge für `complex_check()` an, die Zweigüberdeckung erreicht,
  aber keine Bedingungsüberdeckung.
- [EQ] Geht es auch umgekehrt: Gibt es eine Testmenge, die Bedingungsüberdeckung erreicht,
  aber keine Zweigüberdeckung?
  Begründen Sie Ihre Antwort so, dass sie nicht nur für `complex_check()` gilt.

[HINT::Ich finde für die letzte Frage keinen Ansatz]
Betrachten Sie die Bedingung, die in der Entscheidung ganz rechts steht.
Wann wird sie überhaupt ausgewertet, und was bestimmt dann ihr Wert?
[ENDHINT]

### Pfadüberdeckung
<!-- time estimate: 10 min -->

Ein **Pfad** ist die komplette Folge der Zweige, die ein Aufruf von Anfang bis Ende nimmt.
**Pfadüberdeckung** (path coverage) verlangt, dass jeder mögliche Pfad einmal durchlaufen wird.
Stehen zwei `if` ohne `else` hintereinander, gibt es schon vier Pfade (beide, nur das erste,
nur das zweite, keins); bei n solchen `if` sind es 2ⁿ.
Bei Schleifen ist jede Anzahl von Durchläufen ein eigener Pfad:
Eine Schleife, die 0- bis 10-mal laufen kann, ergibt 11 Pfade;
zwei solche Schleifen hintereinander 11 · 11 = 121.
Weil jeder Zweig auf irgendeinem Pfad liegt, ist Pfadüberdeckung schärfer als Zweigüberdeckung;
praktikabel ist sie aber meist nicht.
Die Schleifenüberdeckung ist gewissermaßen ihr bezahlbarer Ersatz.

- [EQ] Wie viele verschiedene Pfade gibt es durch `binary_search_recur()` (samt aller rekursiven Aufrufe),
  wenn man die Funktion auf eine sortierte Liste aus 7 verschiedenen Zahlen mit `low=0`, `high=6` anwendet?
  Wie viele Aufrufe haben Sie dagegen für Zweigüberdeckung gebraucht?

Neben den hier behandelten Kriterien gibt es weitere, z.B. Datenflusskriterien,
die verfolgen, wo eine Variable gesetzt und wo sie später gelesen wird.
Dafür haben wir kein Messwerkzeug, deshalb lassen wir sie beiseite.

### Reflexion
<!-- time estimate: 10 min -->

- [EQ] Ordnen Sie Anweisungs-, Zweig-, Bedingungs- und Pfadüberdeckung nach ihrer Schärfe.
  Stützen Sie sich dabei auf Ihre Ergebnisse aus den vorigen Schritten.
- [EQ] Welches Kriterium würden Sie nach Ihren Erfahrungen mit den beiden Funktionen
  aus `whitebox.py` im Alltag als Standard verwenden, und wann würden Sie zusätzlich ein anderes heranziehen?
  Berücksichtigen Sie dabei Aufwand, Nutzen und ob es ein Messwerkzeug gibt.

[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
