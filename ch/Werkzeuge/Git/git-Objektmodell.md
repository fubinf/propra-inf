title: Staging Area und Git-Objekte
stage: alpha
timevalue: 2
difficulty: 3
explains:
requires: git-Repository
---

[SECTION::goal::experience]
Ich verstehe das Drei-Bereiche-Modell (Working Directory, Staging Area, Repository),
weiß, was Git-Objekte (Blobs, Trees, Commits) sind, und kann sie inspizieren.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::git-Repository] haben wir `git add` und `git commit` benutzt, 
ohne genau zu verstehen, was dabei passiert.
In dieser Aufgabe schauen wir unter die Haube:
Was tut `git add` wirklich? Was speichert Git, wenn wir committen?
Und warum ist die Staging-Area so zentral für die Arbeitsweise von Git?
[ENDSECTION]

[SECTION::instructions::detailed]

Wir arbeiten weiter in dem Repository aus [PARTREF::git-Repository].
Dort haben wir einen Commit mit der Datei `calculator.py` (Additionsfunktion als Skelett).

### Das Drei-Bereiche-Modell

In der letzten Aufgabe haben wir den Zyklus `git add` → `git commit` kennengelernt.
Aber was passiert dabei eigentlich genau?

Bisher konnten wir uns Git als zwei Bereiche vorstellen:
das Arbeitsverzeichnis (wo wir Dateien bearbeiten) und das Repository (wo Git sie archiviert).
Das ist nicht falsch, aber es fehlt ein entscheidendes Puzzleteil: die **Staging-Area**.

Die Staging-Area (auch *Index* genannt – beide Begriffe meinen dasselbe) ist eine Art 
Zwischenablage zwischen Arbeitsverzeichnis und Repository.
Man kann sie sich als Ablagestapel vorstellen:
Bevor wir ein Paket (einen Commit) schnüren und ins Archiv legen,
sammeln wir auf diesem Stapel die Dateien, die ins Paket sollen.

Das Modell sieht also so aus:

```
Working Directory  →  Staging Area (Index)  →  Repository
    (Dateien            (Ablagestapel /          (Archiv /
     bearbeiten)         Vormerkung)              Commits)
```

`git add` kopiert den **aktuellen Zustand** einer Datei in die Staging-Area.
`git commit` nimmt alles, was in der Staging-Area liegt, und erstellt daraus einen Commit.

Dabei werden nicht einzelne Änderungen gesichert, sondern immer ein vollständiges Abbild aller Dateien im Index — 
ein Snapshot. Unveränderte Dateien übernimmt Git einfach per Referenz vom vorherigen Commit, 
sodass kein Speicher verschwendet wird.

Das klingt nach einem unwichtigen Zwischenschritt – aber es hat eine mächtige Konsequenz,
die wir jetzt direkt ausprobieren.

### Das Doppel-Änderungs-Experiment

Implementieren wir die Additionsfunktion. Ändern Sie `calculator.py` zu:

```python
# Ein einfacher Rechner

def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

```

Fügen Sie die Datei mit `git add calculator.py` zur Staging-Area hinzu.

Jetzt, **bevor wir committen**, fügen wir gleich noch eine neue Funktion hinzu:

```python
# Ein einfacher Rechner

def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

def multipliziere(a, b):
    
```

Führen Sie jetzt `git status` aus.

Sie sollten etwas Unerwartetes sehen: `calculator.py` taucht **zweimal** auf –
einmal unter „Changes to be committed" und einmal unter „Changes not staged for commit".

[EQ] Wie ist das möglich? Was sagt uns das darüber, was `git add` wirklich tut?

Die Erklärung: `git add` merkt nicht einfach eine Datei vor.
Es kopiert den **exakten Inhalt** der Datei zum Zeitpunkt des `git add` in die Staging-Area.
Spätere Änderungen an der Datei im Arbeitsverzeichnis landen **nicht** automatisch in der 
Staging-Area – dafür müsste man erneut `git add` ausführen.

Die Staging-Area erlaubt uns auch, Änderungen gezielt zusammenzustellen:
Wir können z. B. nur bestimmte Dateien in einen Commit aufnehmen 
und andere Änderungen für einen späteren Commit aufheben.

[NOTICE]
Die Staging-Area bietet eine gewisse Sicherheit:
Dateien, die wir dort abgelegt haben, können wir wiederherstellen,
selbst wenn wir die Arbeitskopie danach weiter verändern.
Aber Vorsicht: Ein echtes Backup ist das nicht.
Wirklich dauerhaft gesichert sind Änderungen erst nach einem Commit –
und idealerweise auch erst, wenn dieser auf einen Git-Server gepusht wurde.
[ENDNOTICE]

### Git-Objekte: Was speichert Git wirklich?

Bevor wir weiterarbeiten, wollen wir verstehen, *was genau* Git beim `git add` und 
`git commit` eigentlich speichert.

Lesen Sie dazu den Artikel 
[Git from the inside out](https://maryrosecook.com/blog/post/git-from-the-inside-out)
bis einschließlich des Abschnitts „Each Commit has a Parent".

[HINT::Lieber ein Video?]
Den gleichen Inhalt gibt es auch als Vortrag:
[Git from the inside out (Video)](https://www.youtube.com/watch?v=fCtZWGhQBvo), 
bis ca. 16:08.
[ENDHINT]

Beantworten Sie folgende Fragen zum Artikel:

[EQ] Wie speichert Git eine Datei, wenn `git add` ausgeführt wird? 
Was ist ein Blob-Objekt, und wie wird es benannt?

[EQ] Wenn wir `git add` erneut für eine veränderte Datei ausführen 
(ohne vorher committed zu haben): Was passiert mit dem vorherigen Blob-Objekt?

[EQ] Was speichert Git, wenn wir einen neuen Commit erstellen?
Welche Objekte entstehen dabei und wie verweisen sie aufeinander?

[EQ] Kann es zwei Commits mit identischem Hash geben? Warum bzw. warum nicht?

[EQ] Working Directory, Staging-Area und der letzte Commit können scheinbar 
auf die gleichen Daten zeigen. Allerdings können nur zwei davon *tatsächlich* auf 
dasselbe Objekt zeigen. Welche zwei, und warum?

### Objekte selbst inspizieren

Git stellt uns einige Befehle zur Verfügung, mit denen wir die gespeicherten Objekte 
direkt betrachten können.

Erstellen wir zunächst einen Commit mit der implementierten Additionsfunktion.
Ihre Staging-Area enthält bereits die korrekte Version (die ohne `multipliziere`).
Committen Sie also:

```bash
git commit -m "Additionsfunktion implementiert"
```

Jetzt haben wir Commit-Objekte, Tree-Objekte und Blob-Objekte im Repository.
Schauen wir sie uns an:

[EC] Benutzen Sie `git cat-file -p HEAD`, um das Commit-Objekt zu betrachten.
Folgen Sie dann der Referenz auf das Tree-Objekt und von dort auf das Blob-Objekt.
Überprüfen Sie, dass der Blob-Inhalt mit Ihrer Datei übereinstimmt.

Damit haben wir die Kette Commit → Tree → Blob einmal komplett nachverfolgt.
Das ist die grundlegende Datenstruktur von Git.

### Dateien im Index anschauen und verlorene Blobs finden

Git gibt uns auch Befehle, um den Index (die Staging-Area) direkt einzusehen.
Die wichtigsten sind `git ls-files` und `git show`.

[EC] Finden Sie mit `git ls-files` den Hash des Blob-Objekts von `calculator.py` 
im Index und schauen Sie sich dessen Inhalt mit `git show` an.

[HINT::Wie finde ich den Hash?]
`git ls-files` gibt standardmäßig nur den Dateinamen aus, nicht den Hash.
Es fehlt noch ein Argument – denken Sie an `git help ls-files`.
[ENDHINT]

Jetzt ein kleines Experiment, um zu sehen, was mit „alten" Blobs passiert.
Ändern Sie die Funktionsdefinition absichtlich falsch ab:

```python
# Ein einfacher Rechner

def addiere(a, c):
    # Diese Funktion addiert zwei Zahlen
    return a + c

```

Fügen Sie die Datei erneut mit `git add` zum Index hinzu.
Git hat jetzt einen neuen Blob für den neuen Dateiinhalt erstellt.
Aber was ist mit dem vorherigen Blob?

Führen Sie `git fsck` aus. 
Unter den Ausgaben finden Sie sogenannte *dangling blobs* –
Blob-Objekte, die von keiner Dateireferenz mehr erreicht werden.
Das passiert fast immer, wenn wir die gleiche Datei mehrfach mit `git add` zum Index hinzufügen,
ohne zwischendurch zu committen.

[EC] Schauen Sie sich den Inhalt des dangling Blob an. 
Ist es der vorherige Zustand unserer Datei?

Das ist in der Praxis selten nötig, aber es zeigt ein wichtiges Prinzip:
Git löscht Objekte nicht sofort. Solange sie existieren, kann man sie wiederfinden –
auch wenn keine Referenz mehr auf sie zeigt.

Setzen Sie jetzt die Datei wieder auf den korrekten Zustand zurück 
(mit `(a, b)` statt `(a, c)`) und fügen Sie sie erneut dem Index hinzu.

### Zweiter Commit: Multiplikation

Ihre Datei im Arbeitsverzeichnis enthält noch die Multiplikationsfunktion, die sich nicht im Index befindet.
Falls Sie sie bei den vorherigen Experimenten verloren haben, 
bringen Sie `calculator.py` auf diesen Stand:

```python
# Ein einfacher Rechner

def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

def multipliziere(a, b):
    # Diese Funktion multipliziert zwei Zahlen
    return a * b

```

Fügen Sie die Datei zum Index hinzu und erstellen Sie einen zweiten Commit.

Prüfen Sie mit `git log`, dass Sie jetzt zwei Commits sehen.

### Zwischenfazit

Sie verstehen jetzt das Drei-Bereiche-Modell: 
Working Directory → Staging Area → Repository.
Sie wissen:

- dass `git add` den exakten Dateiinhalt als Blob-Objekt speichert,
- dass Commits auf Tree-Objekte verweisen, die wiederum auf Blobs zeigen,
- und dass Git Objekte über SHA-1-Hashes referenziert.

In der nächsten Aufgabe lernen wir, diese Informationen praktisch zu nutzen:
mit `git diff` Änderungen vergleichen und mit `git log` die Historie durchsuchen.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhinweise]
Prüfen Sie das Protokoll und die Antworten.

[INCLUDE::ALT:]

[ENDINSTRUCTOR]