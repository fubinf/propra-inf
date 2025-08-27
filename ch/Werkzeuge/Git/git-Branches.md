title: Git Branches
stage: alpha
timevalue: 2.0
difficulty: 2
assumes: git-Grundlagen, git-Zweitrepo
---

[SECTION::goal::idea]

Ich verstehe, wie Branches in git funktionieren, wann es sinnvoll ist, Branches zu verwenden, und 
welche Probleme dabei entstehen können. Ich lerne ausserdem die Unterschiede zwischen `git 
branch`, `git switch` und `git checkout` sowie die grundlegende Funktionsweise von `git stash`.

[ENDSECTION]

[SECTION::background::default]

Ein in der Praxis wichtiger und nützlicher Aspekt von git sind die sogenannten Branches (dt. Zweige).
Mithilfe von Branches kann man in git leicht zwischen verschiedenen Revisionen eines Projektes hin 
und her springen, um Änderungen an bestehendem Code vorzunehmen, ohne sich um gleichzeitige 
Änderungen anderer Projektteilnehmer Gedanken machen zu müssen. Gleichzeitig werden Branches 
auch benutzt, um z.B. zwischen stabilen Release- und instabilen Developer-Versionen eines 
Projekts zu unterscheiden, wodurch einzelne Branches bestimmtes Verhalten zugewiesen bekommen.

[ENDSECTION]

Bisher haben wir git immer als eine fortlaufende Historie auf einem einfachen Zeitstrahl 
betrachtet. Eigentlich handelt es sich bei Git-Repositories jedoch um gerichtete azyklische Graphen,
welche auch beliebig viele und verschachtelte Abzweigungen und Zusammenführungen erlauben.
Git nennt diese Abzweigungen einen "Branch". 
In vielen Anfängerquellen wird zur Erklärung eine Baummetapher verwendet, aber 
spätestens, wenn die "Äste" dann wieder zusammenwachsen, gibt es dahingehend Schwierigkeiten, 
diese Analogien aufrechtzuerhalten. 
Daher sparen wir uns an dieser Stelle irgendwelche Metaphern und lernen einfach direkt, wie es 
richtig geht.

Wie bei [PARTREF::git-Grundlagen] werden wir auch hier wieder mit einem neuen Repository arbeiten.
Wir gehen davon aus, dass Sie [PARTREF::git-Zweitrepo] durchgearbeitet haben und ein zweites, 
auf Gitlab gehostetes Repo erstellt haben. 
Während wir in [PARTREF::git-Grundlagen] noch mit einem reinen "offline" Repo gearbeitet haben, 
erwarten wir für diese Aufgabe die Erstellung eines neuen Repos in Gitlab, da sie die Aufgabe 
auch mit ihrem Übungspartner gemeinsam bearbeiten sollen.

Als Grundlage werden wir auch diesmal wieder mit einem kleinen Projekt arbeiten. 
Dazu erstellen wir wieder unsere initiale Umgebung. 
Erstellen Sie eine neue Datei `calc.py` mit dem folgenden Inhalt:

```python
def add(a, b):
    return a + b
```

Committen Sie jetzt die Datei in ihr Repository.

Und weil es so schön war und wir ein bisschen Inhalt in unserem git log haben wollen, 
fügen wir noch ein paar Kommentare hinzu und commiten noch einmal. 

```python
"""calc.py – collection of CS helper functions"""

def add(a, b):
    """Return a + b."""
    return a + b
```

Führen wir jetzt `git log` aus sollten wir ungefähr so eine Ausgabe sehen:

```terminaloutput
commit 890c3db45f5a60391b624e8fab80f6de24bc38eb (HEAD -> master)
Author: Sven Hüster <sven.svelle@gmail.com>
Date:   Tue May 20 10:29:21 2025 +0200

    add comment

commit 10dace86873901f53a67733c3417395b7c0a02b7
Author: Sven Hüster <sven.svelle@gmail.com>
Date:   Tue May 20 10:28:43 2025 +0200

    add calc.py
```

Git log kennen wir ja bereits aus der [PARTREF::git-Grundlagen] Aufgabe. 
Was wir darin allerdings nicht so richtig beachtet haben, war der sogenannte `HEAD`. 
Der ist uns zwar ein paar Mal untergekommen, aber was das ist wissen Sie wahrscheinlich noch nicht.

Um `HEAD` zu verstehen, schauen wir mal in unser `.git` Verzeichnis. 
Dann fällt uns direkt auf, dass dort auch eine Datei names HEAD liegt. 
Das ist kein Zufall und diese Datei ist auch lesbar. 
Schauen wir uns also den Inhalt mit `cat .git/HEAD` an.

```terminaloutput
ref: refs/heads/master
```

Was sehen wir hier? 
Einen Verweis auf ein Unterverzeichnis vom [TERMREF::Repository-Verzeichnis].
Auch darauf werfen wir mal einen näheren Blick.

```terminaloutput
.git/refs
├── heads
│   └── master
└── tags
```

[EC] Schauen Sie sich den Inhalt von `.git/refs/heads/master` an. Was beschreibt dieser?

Aber warum ist das so? 
Ganz einfach: Der **HEAD-Pointer** verweist immer auf den aktuell _ausgecheckten_ Branch bzw. 
dessen letzten Commit, im Repository. 
Der Begriff „ausgecheckt“ stammt dabei vom Befehl `git checkout`, der es uns erlaubt, zwischen 
verschiedenen Zuständen im Repository zu wechseln. 
Diese Zustände werden in erster Linie durch Branches, Tags oder spezifische Commits bestimmt und 
können sogar bis auf Dateiebene heruntergebrochen werden. 
Aber dazu später mehr.


### Einen neuen Branch erstellen

Häufig werden Branches in git benutzt, um z.B. neue Funktionalität zu einem Projekt hinzuzufügen.
Also benutzen wir das jetzt direkt als Fallbeispiel in unserem "Projekt" und implementieren eine 
Fakultätsfunktion.

```python
def factorial(n):
    """Return n! (naïve recursion)."""
    return 1 if n <= 1 else n * factorial(n - 1)
```

Wenn Sie den Code um diese Funktion erweitert haben, erstellen Sie diesmal **noch keinen neuen 
Commit**.

Normalerweise würde man den Branch erstellen *bevor* man die Änderungen am Code vornimmt, aber 
solange man noch nicht Commitet ist es auch gar kein Problem, nachher noch den Branch zu erstellen.
Also machen wir das jetzt einfach mal:

`git branch factorial`

Führen wir jetzt wieder unseren `git log`-Befehl aus, sehen wir Folgendes:

```git
* 890c3db (HEAD -> master, factorial) add comment
* 10dace8 add calc.py
```

Dort fällt uns direkt auf, dass unser neuer Branch jetzt direkt neben *master* gelistet wird.
Was uns aber auch auffällt, ist, dass HEAD noch immer auf *master* zeigt. 
Würden wir also jetzt einen neuen Commit erstellen, würde dieser wieder auf dem *master*-Branch landen. 
Da wir aber unsere Änderungen auf den neu erstellten *factorial*-Branch commiten wollen, müssen 
wir erst zu diesem Wechseln. 
Dazu brauchen wir, Sie ahnen es sicher schon, `git checkout`.

[EC] Checken Sie den neu erstellen `factorial` Branch aus, Commiten Sie dort ihre Änderungen und 
führen Sie wieder `git log --oneline --graph --decorate` aus.

[EQ] Nachdem Sie erneut git log ausgeführt haben, sollte `HEAD` diesmal nicht mehr auf *master* 
zeigen. 
Worauf zeigt er stattdessen und warum? Hat sich auch der Inhalt der `.git/HEAD` Datei geändert?

Neben `git checkout` gibt es übrigens seit git 2.23 noch einen anderen Befehl, nämlich `git switch`.

[EQ] Wechseln Sie mit `git switch` zurück auf den master Branch und schauen Sie erneut in den git 
log. Was fällt ihnen auf?

[EQ] Gibt es eine Möglichkeit in `git log` alle Branches anzeigen zu lassen?


[NOTICE]
Auch, wenn Sie code schon vor dem Branchen *lokal* commitet haben ist das kein Weltuntergang, wie 
Sie Commits, vor dem Pushen, wieder rückgängig machen können, lernen Sie ganz einfach in: 
[PARTREF::git-Fehlerbehebung]
[ENDNOTICE]

### Branchen und wechseln in einem Schritt

Bis jetzt haben wir das Erstellen des Branches und das Wechseln auf den Branch in zwei separaten 
Schritten abgehandelt. 
Dabei kann man auch beides in einem Schritt machen.

[NOTICE]
Die nachfolgenden Schritte können auch Wunderbar durch Übungspartner_innen auf einem separaten 
Gerät durchgeführt werden.
[ENDNOTICE]

[EC] Von ihrem master-Branch ausgehend, erstellen Sie einen neuen Branch `faculty-iterative` und 
wechseln auf diesen mit einem Befehl. 
Geben Sie sowohl den Befehl für `git checkout` als auch `git switch` an.

Nachdem Sie in ihren neuen Branch gewechselt sind, nehmen Sie wieder Änderungen an der Datei `calc.py` vor, 
indem Sie die folgende Funktion hinzufügen.

```python
def factorial(n: int) -> int:
    """Return n! for a non-negative integer n (iterative, naïve)."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

[EC] Commiten Sie wieder ihre Änderungen und wechseln Sie zurück auf den master-Branch.

[NOTICE]
Wenn Sie diesen Teil der Aufgabe zu zweit durchführen, vergessen Sie nicht ihre neuen Branches 
und Commits auch auf den Gitlab-Server zu pushen und auf dem jeweils anderen Gerät wieder zu pullen.
[ENDNOTICE]

Wenn wir uns unseren git log anschauen, werden wir jetzt endlich mal etwas mehr sehen:

```terminaloutput
* d28cb86 (fac_iterative) add iterative version of factorial
| * 6ebb2e8 (factorial) add recursive factorial implementation
|/
* 890c3db (HEAD -> master) add comment
* 10dace8 add calc.py
```

[EQ] Aber was genau sehen wir denn hier? 


[NOTICE]
Falls Sie das bis hierher Gelernte noch einmal festigen möchten, empfiehlt es sich den [Git 
Branching in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) 
Teil des Git-Buchs zu lesen. Dort wird noch einmal, mithilfe von anschaulichen Graphen, erklärt 
was genau beim Branchen passiert. 
[ENDNOTICE]

### Branches zusammenführen

Jetzt, wo wir von master ausgehend, zwei Branches erstellt haben, möchten wir meistens auch 
irgendwann unsere Änderungen zurück in unseren Hauptbranch bringen. 
Dafür gibt es mehrere Wege. 
In dieser Aufgabe werden wir uns lediglich den sogenannten Merge (nach dem Befehl `git merge`) 
anschauen.

[EC] Mergen sie ihre Änderungen vom `factorial` branch in ihren Hauptbranch.

Wenn Sie sich die Ausgabe von `git merge` anschauen, wird ihnen sicherlich der Begriff 
"fast-forward" auffallen.
Was bedeutet "fast-forward"?
Git kann mehrere Strategien zum mergen verwenden. 
Standardmäßig wird es jedoch probieren, die einfachste zu nutzen, nämlich "fast-forward".
Mit dieser Methode wird git einfach nur schauen, ob alle *neuen* Commits im zu mergenden Branch, 
*nach* dem letzten Commit des Branches in den hineingermerged wird, erstellt wurden.
Ist das der Fall, werden einfach nur die Zeiger entsprechend angepasst und der Merge ist fertig.
Der Vorteil hier ist, dass kein neuer Merge-Commit nötig ist und man so eine "saubere" git-Historie hat.

Im git-Book Kapitel 
[Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) 
wird das Verfahren noch einmal ausführlicher erklärt und entsprechend Illustriert.

Führen wir jetzt wieder unseren `git log` Befehl aus, sehen wir Folgendes:

```terminaloutput
* d28cb86 (fac_iterative) add iterative version of factorial
| * 6ebb2e8 (HEAD -> master, factorial) add recursive factorial implementation
|/
* 890c3db add comment
* 10dace8 add calc.py
```

Wie wir sehen können, zeigt unser HEAD jetzt sowohl auf *master*, als auch auf *factorial*.
Der Mergeprozess verlief also problemlos und der Commit vom *factorial* branch konnte ohne 
weiteres auf den *master* branch übertragen werden.

Aber nicht immer verläuft das Mergen ohne Hindernisse.


### Merge-Konflikte

Gelegentlich kann es passieren, dass zwei verschiedene Branches, bzw. deren Commits die gleichen 
Teile des Codes bearbeiten. 
Dann kann Git nicht direkt nachvollziehen, welche Änderung Priorität hat. 
Ein sogenannter "Merge-Konflikt" ist entstanden.

Genau diese Situation simulieren wir jetzt!
 
[EC] Mergen sie ihren *fac_iterative* branch in ihren *master* branch. 

Wenn Sie alles "richtig" gemacht haben, dann sollten Sie jetzt folgende Nachricht im Terminal 
bekommen:

```terminaloutput
Auto-merging calc.py
CONFLICT (content): Merge conflict in calc.py
Automatic merge failed; fix conflicts and then commit the result.
```

Aber warum ist das so?

Wenn wir git merge ausführen, wird git probieren, ausgehend vom gemeinsamen Ursprungscommit, 
alle neuen Commits auf den Zielbranch anzuwenden. 
Das geht so lange gut, bis git auf Zwei Commits trifft, welche die gleiche Stelle im Code 
bearbeiten, aber nicht beide in Quellbranch (`fac_iterative`) existieren.

Öffnen wir die *calc.py* Datei, werden wir einen Hinweis von git vorfinden:

```python
# a collection of cs helper functions

func addition(a, b):
        return a + b

<<<<<<< HEAD
func factorial(n):
        """Return n! (naïve recursion)."""
        return 1 if n <= 1 else n * factorial(n - 1)
=======
def factorial(n: int) -> int:
    """Return n! for a non-negative integer n (iterative, naïve)."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
>>>>>>> fac_iterative
```

Was hat git hier gemacht? 
Da es den Konflikt nicht von selbst lösen kann, stellt es uns vor die Wahl: 
Wollen wir den aktuellen Zustand, alles zwischen `<<<<<<< HEAD` und `=======`, behalten, 
oder wollen wir die Änderungen aus *fac_iterative* übernehmen, 
also alles zwischen `=======` und `>>>>>>> fac_iterative`?

[EC] Lösen Sie den Merge-Konflikt auf und Commiten Sie ihr Ergebnis. 
Welche Implementierung Sie wählen ist Ihnen überlassen.

[NOTICE]
Wenn Sie `git commit` allein ausführen, gibt ihnen git eine Commitnachricht für ihren 
Merge-Commit vor. 
Die können Sie benutzen, müssen Sie aber nicht. 
Konvention wäre es allerdings, diese zu benutzen, damit klar ist, 
dass es sich hierbei um einen Merge-Commit handelt.
[ENDNOTICE]

Schauen wir noch einmal in unseren git log:


```terminaloutput
*   efe6b82 (HEAD -> master) Merge branch 'fac_iterative'
|\
| * d28cb86 (fac_iterative) add iterative version of factorial
* | 6ebb2e8 (factorial) add recursive factorial implementation
|/
* 890c3db add comment
* 10dace8 add calc.py
```

Was können wir hier sehen?

1. Der HEAD/master ist nun wieder alleine an oberster Stelle, mit dem neusten Commit, unserem 
   Merge-Commit.
2. Darunter sehen wir unsere beiden Commit und können sehen, dass diese jeweils auf ihrem 
   eigenen Branch existieren.
3. Wir sehen, dass beide Commits wieder in unseren Master-Branch gemerged wurden.


[SECTION::instructions::detailed]

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Befehle prüfen, und ob Branching und die Behebung von Merge-Conflicts verstanden wurde]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
