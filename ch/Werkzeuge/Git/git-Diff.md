title: Änderungen vergleichen und Historie
stage: draft
timevalue: 1.5
difficulty: 2
explains:
assumes: git-Objektmodell
---

[SECTION::goal::experience]
Ich kann mit `git diff` gezielt Änderungen zwischen den drei Bereichen vergleichen
und mit `git log` die Commit-Historie durchsuchen und filtern.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::git-Objektmodell] haben wir gelernt, dass Git drei Bereiche kennt:
Working Directory, Staging Area und Repository.
Jetzt lernen wir zwei Werkzeuge kennen, die dieses Modell im Alltag praktisch nutzbar machen:
`git diff` zeigt uns *was* sich verändert hat, `git log` zeigt uns *wann* und *warum*.
[ENDSECTION]

[SECTION::instructions::detailed]

Wir arbeiten weiter in unserem Taschenrechner-Repository.
Dort sollten sich zwei Commits befinden (Addition und Multiplikation).

### Die drei Vergleiche: `git diff`

Rufen Sie zunächst die Dokumentation zu `git diff` auf (`git help diff`).
Das ist eine Menge Stoff – das meiste brauchen wir noch nicht.
Schauen Sie sich vor allem den Abschnitt *EXAMPLES* an.

Aus dem Drei-Bereiche-Modell ergeben sich drei sinnvolle Vergleiche:

```
Working Directory  ←──git diff──→  Staging Area  ←──git diff --staged──→  letzter Commit
       ↑                                                                        ↑
       └────────────────────git diff HEAD────────────────────────────────────────┘
```

Um alle drei Vergleiche in Aktion zu sehen, brauchen wir einen Zustand, 
in dem sich alle drei Bereiche unterscheiden.

Fügen Sie `calculator.py` eine neue Funktion als Skelett hinzu:

```python
# Ein einfacher Rechner

def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

def multipliziere(a, b):
    # Diese Funktion multipliziert zwei Zahlen
    return a * b

def subtrahiere(a, b):
    
```

Fügen Sie diese Änderung mit `git add` zur Staging-Area hinzu.

Jetzt implementieren wir die Funktion gleich weiter, **ohne erneut** `git add` auszuführen:

```python
# Ein einfacher Rechner

def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

def multipliziere(a, b):
    # Diese Funktion multipliziert zwei Zahlen
    return a * b

def subtrahiere(a, b):
    # Diese Funktion subtrahiert zwei Zahlen
    return a - b

```

Jetzt unterscheiden sich alle drei Bereiche:
- Der **letzte Commit** kennt nur Addition und Multiplikation.
- Die **Staging-Area** enthält zusätzlich das Subtraktions-Skelett.
- Das **Working Directory** enthält die vollständige Subtraktions-Implementierung.

[EC] Vergleichen Sie den aktuellen Zustand der Datei im Working Directory 
mit den bereits vorgemerkten Änderungen in der Staging-Area.

[EC] Vergleichen Sie die vorgemerkten Änderungen in der Staging-Area 
mit dem letzten Commit.

[EC] Vergleichen Sie den aktuellen Zustand im Working Directory 
direkt mit dem letzten Commit.

[EQ] Führen Sie `git diff` ohne Argumente aus. Was zeigt es, und warum?

[EQ] Git speichert vollständige Snapshots, keine Diffs. 
Wie erzeugt es dann die `git diff`-Ausgabe?

### `git status` mit neuen Augen

Führen Sie `git status` aus. 
In der vorherigen Aufgabe haben wir gesehen, dass `git status` uns auch Befehle vorschlägt.

[EQ] Welche Befehle schlägt `git status` vor, und was tun sie?
Schauen Sie bei unbekannten Befehlen in `git help` nach.
(Wir werden diese Befehle in einer späteren Aufgabe üben – 
für jetzt reicht es, ihre Funktion zu kennen.)

Es gibt auch eine Möglichkeit, sich mit `git status` direkt die Änderungen anzeigen zu lassen,
die beim nächsten Commit gespeichert würden, und separat die Änderungen, 
die noch nicht in der Staging-Area sind.

[EQ] Wie geht das? (Tipp: Schauen Sie in `git help status` nach den *verbose*-Optionen.)

### Commit erstellen

Fügen Sie die verbleibenden Änderungen dem Index hinzu und erstellen Sie einen Commit 
mit einer passenden Nachricht.

### `git log`: Die Commit-Historie

Nicht selten wollen wir nicht nur vorwärts arbeiten, 
sondern auch in die Vergangenheit schauen –
sei es, um einen alten Zustand zu betrachten oder um zu prüfen, 
welche Commits im Repository existieren.

`git log` ist unser Git-Tagebuch. 
Wenn wir es ohne Argumente aufrufen, sehen wir für jeden Commit:

1. den Commit-Hash
2. den Autor
3. das Datum
4. die Commit-Nachricht

Das ist bei drei Commits noch übersichtlich, 
aber bei hunderten oder tausenden Commits wird es schnell unübersichtlich.
Deswegen hat `git log` viele nützliche Optionen.
Schauen Sie ruhig in die Dokumentation – 
dort werden Sie *sehr viele* Optionen finden, 
von denen Sie die meisten aktuell nicht brauchen werden.

Für den Anfang sind folgende besonders nützlich:

**`--oneline`** reduziert jeden Commit auf eine einzige Zeile.
Hilfreich bei langer Historie.

**`-p`** erzeugt für jeden Commit einen sogenannten Patch-Text –
im Prinzip ein Diff zu allen veränderten Dateien.
Das ist so, als würde man `git diff` zwischen jedem Commit und seinem Vorgänger ausführen.

Beachten Sie: `git log -p` zeigt für jeden Commit die *Änderungen* gegenüber dem Vorgänger.
Das ist eine zweite Sicht auf Commits.
In [PARTREF::git-Objektmodell] haben wir gelernt, dass ein Commit ein vollständiger 
Snapshot ist — ein Abbild aller Dateien zu einem bestimmten Zeitpunkt.
Aber man kann denselben Commit auch als *Änderungsoperation* betrachten:
"Was wurde gegenüber dem vorherigen Zustand verändert?"
Beide Sichten sind korrekt und nützlich.
Wir werden in einer späteren Aufgabe sehen, dass manche Git-Befehle die eine, 
manche die andere Sicht verwenden.

**`-- <Dateipfad>`** zeigt nur Commits, die eine bestimmte Datei verändert haben.

[EQ] Wie würde der `git log`-Befehl aussehen, um alle Commits und deren Änderungen 
an unserer `calculator.py`-Datei anzuzeigen?

### Weitere nützliche Log-Optionen

In größeren Repositories ist es oft nützlich, Commits nach Datum zu filtern:

- `--since <date>` bzw. `--after <date>`: Commits nach einem bestimmten Datum
- `--until <date>` bzw. `--before <date>`: Commits vor einem bestimmten Datum

Außerdem praktisch ist die Suche nach Autor:

```bash
git log --author="Max Mustermann"
git log --author=Max
```

Damit matcht man entweder den vollständigen Autorennamen oder einen Teilstring.
Das ist besonders hilfreich, wenn mehrere Personen am gleichen Repository arbeiten.

Eine weitere Option, die uns in einer späteren Aufgabe über Branches sehr nützlich werden wird:

```bash
git log --oneline --graph --all
```

`--graph` zeichnet die Commit-Historie als ASCII-Graphen, 
und `--all` zeigt auch Commits auf anderen Branches.
Bei unserem linearen Repository mit einem Branch sieht das noch unspektakulär aus –
aber sobald Branches ins Spiel kommen, wird es unverzichtbar.

### Zwischenfazit

Sie haben jetzt drei Werkzeuge, um jederzeit zu verstehen, 
was in Ihrem Repository passiert:

- `git status` zeigt den **aktuellen Zustand** (was ist geändert, was ist vorgemerkt).
- `git diff` zeigt die **konkreten Änderungen** zwischen den drei Bereichen.
- `git log` zeigt die **Geschichte** aller Commits.

Zusammen mit dem Drei-Bereiche-Modell aus der letzten Aufgabe können Sie sich jetzt 
in jeder Situation orientieren.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhinweise]
Prüfen Sie das Protokoll und die Antworten.

[INCLUDE::ALT:]

[ENDINSTRUCTOR]