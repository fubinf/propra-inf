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

Ein in der Praxis wichtiger und nützlicher Aspekt von git sind die sogenannten Branches.
Mit Branches kann man in git leicht zwischen verschiedenen Revisionen eines Projektes hin und her 
springen z.B. um neue Features einzupflegen, bestimmte Softwareversionen festzuhalten oder um 
Bugs zu beheben. 

#TODO background fertig schreiben

[ENDSECTION]

Bisher haben wir git immer als eine fortlaufende Historie auf einem einfachen Zeitstrahl 
betrachtet. Eigentlich handelt es sich bei Git-Repositories jedoch um gerichtete azyklische Graphen,
welche auch beliebig viele und verschachtelte Abzweigungen und Zusammenführungen erlauben.
Git nennt diese Abzweigungen einen "Branch". Oft wird dann eine Baummetapher verwendet, aber 
spätestens, wenn die "Äste" dann wieder zusammenwachsen, gibt es dahingehend Schwierigkeiten, 
diese Metapher aufrechtzuerhalten. Daher sparen wir uns an dieser Stelle irgendwelche Metaphern 
und lernen einfach direkt, wie es richtig geht.

Wie bei [PARTREF::git-Grundlagen] werden wir auch hier wieder mit einem neuen Repository arbeiten.
Wir gehen davon aus, dass Sie [PARTREF::git-Zweitrepo] durchgearbeitet haben und ein zweites, 
auf Gitlab gehostetes Repo erstellt haben. Diesmal ist das wichtig, da wir auch stellenweise die 
Zusammenarbeit mit dem Übungspartner erwarten.

Als Grundlage werden wir auch diesmal wieder mit einem kleinen Projekt arbeiten. Dazu erstellen 
wir wieder unsere initiale Umgebung. Erstellen Sie eine neue Datei `calc.py` mit dem folgenden 
Inhalt:

```python
def add(a, b):
    return a + b
```

Committen Sie jetzt die Datei in ihr Repository.

Und weil es so schön war und wir ein bisschen Inhalt in unserem git log haben wollen, fügen wir 
noch ein paar Kommentare hinzu und commiten noch einmal. 

```python
"""calc.py – collection of CS helper functions"""

def add(a, b):
    """Return a + b."""
    return a + b
```

Führen wir jetzt `git log` aus sollten wir ungefähr so eine Ausgabe sehen:

```bash
commit 890c3db45f5a60391b624e8fab80f6de24bc38eb (HEAD -> master)
Author: Sven Hüster <sven.svelle@gmail.com>
Date:   Tue May 20 10:29:21 2025 +0200

    add comment

commit 10dace86873901f53a67733c3417395b7c0a02b7
Author: Sven Hüster <sven.svelle@gmail.com>
Date:   Tue May 20 10:28:43 2025 +0200

    add calc.py
```

Das ist ganz schön viel Ausgabe, das geht auch kürzer.
Für den Rest der Aufgabe nutzen wir folgenden Befehl:

`git log --oneline --graph --decorate`

[NOTICE]
Das können wir uns auch als git-alias anlegen, wie das geht erfahren Sie in [PARTREF::git-Anpassen].
[ENDNOTICE]

Jetzt sieht unsere Ausgabe deutlich kürzer aus. Lediglich ein kürzerer Commit-Hash und unsere 
Commit-Nachricht bleiben noch erhalten. Dazu fällt uns noch `(HEAD -> master)` auf.

```bash
* 890c3db (HEAD -> master) add comment
* 10dace8 add calc.py
```

Git log kennen wir ja bereits aus der [PARTREF::git-Grundlagen] Aufgabe. Was wir darin 
allerdings nicht so richtig beachtet haben, war der sogenannte HEAD. Der ist uns zwar ein paar 
Mal untergekommen, aber was das ist wissen wir eigentlich noch nicht.

Um HEAD zu verstehen, schauen wir mal in unser `.git` Verzeichnis. Dann fällt uns direkt auf, 
dass dort auch eine Datei names HEAD liegt. Das ist kein Zufall und diese Datei ist auch lesbar. 
Schauen wir uns also den Inhalt mit `cat .git/HEAD` an.

```bash
ref: refs/heads/master
```

Was sehen wir hier? Ganz einfach, einen Verweis auf ein Unterverzeichnis vom .git-Verzeichnis.
Auch darauf werfen wir mal einen näheren Blick.

```bash
.git/refs
├── heads
│   └── master
└── tags
```

Also sehen wir, dass dort in `.git/refs/heads` eine datei namens `master` liegt.
Und der Inhalt?

```bash
890c3db45f5a60391b624e8fab80f6de24bc38eb
```

Dieser Wert entspricht dem Hash unseres letzten Commits. Aber warum ist das so? Ganz einfach: 
Der **HEAD-Pointer** verweist immer auf den aktuell _ausgecheckten_ Commit im Repository. Der 
Begriff „ausgecheckt“ stammt vom Befehl `git checkout`, der es uns erlaubt, zwischen 
verschiedenen Zuständen im Repository zu wechseln. Diese Zustände werden in erster Linie durch 
Branches, Tags oder spezifische Commits bestimmt und können sogar bis auf Dateiebene 
heruntergebrochen werden. Aber dazu später mehr. Jetzt wollen wir erstmal wieder zurück zum 
eigentlichen Thema, Branches.


### Einen neuen Branch erstellen

Häufig werden Branches in git benutzt, um z.B. neue Funktionalität zu einem Projekt hinzuzufügen.
Also benutzen wir das jetzt direkt als Fallbeispiel in unserem "Projekt" und implementieren eine 
Fakultätsfunktion.

```python
def factorial(n):
    """Return n! (naïve recursion)."""
    return 1 if n <= 1 else n * factorial(n - 1)
```

Nachdem Sie den Code um diese Funktion erweitert haben, erstellen Sie **noch keinen neuen Commit**.

Normalerweise würde man den Branch erstellen *bevor* man die Änderungen am Code vornimmt, aber 
solange man noch nicht Commitet ist es auch gar kein Problem, nachher noch den Branch zu erstellen.
Also machen wir das jetzt einfach mal:

`git branch factorial`

Führen wir jetzt wieder unseren `git log`-Befehl aus, sehen wir Folgendes:

```bash
* 890c3db (HEAD -> master, factorial) add comment
* 10dace8 add calc.py
```

Dort fällt uns direkt auf, dass unser neuer Branch jetzt direkt neben *master* gelistet wird.
Was uns aber auch auffällt, ist, dass HEAD noch immer auf *master* zeigt. Würden wir also jetzt 
einen neuen Commit erstellen, würde dieser wieder auf dem *master*-Branch landen. Da wir aber 
unsere Änderungen auf den neu erstellten *factorial*-Branch commiten wollen, müssen wir erst zu 
diesem Wechseln. Dazu brauchen wir, Sie ahnen es sicher schon, `git checkout`.

[EC] Checken Sie den neu erstellen `factorial` Branch aus, Commiten Sie dort ihre Änderungen und 
führen Sie wieder `git log --oneline --graph --decorate` aus.

[EQ] Nachdem Sie erneut git log ausgeführt haben, sollte `HEAD` diesmal nicht mehr auf *master* 
zeigen. Worauf zeigt er stattdessen und warum? Hat sich auch der Inhalt der `.git/HEAD` Datei 
geändert?

Neben `git checkout` gibt es übrigens seit git 2.23 noch einen anderen Befehl, nämlich `git switch`.

[EQ] Wechseln Sie mit `git switch` zurück auf den master Branch und schauen Sie erneut in den git 
log. Was fällt ihnen auf?




[SECTION::instructions::detailed]

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Befehle prüfen, und ob Branching und die Behebung von Merge-Conflicts verstanden wurde]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
