title: git-Grundlagen
stage: alpha
timevalue: 2
difficulty: 3
explains:
assumes: git-Funktionsweise
requires: git-Zweitrepo
---

[SECTION::goal::experience]
Ich lerne, wie die Grundfunktionen von Git funktionieren, und festigte mein mentales Modell von Git.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::Git101] haben wir gerade so das Nötigste gelernt, um unsere Aufgaben im ProPra 
abzugeben. Jetzt geht es darum, das gelernte zu vertiefen und das Wissen um die Befehle und 
[PARTREF::git-Funktionsweise] zu festigen.
[ENDSECTION]

[SECTION::instructions::detailed]
In dieser Aufgabe werden wir so richtig tief in die Interna von Git einsteigen. 
Wie verwaltet git Dateien und Commits? 
Wie können wir diese vergleichen und uns einen Überblick darüber 
verschaffen, was während der Entwicklung eines Projektes geschieht?

Damit wir die Befehle nicht einfach nur herunter rattern, arbeiten wir die Inhalte anhand eines 
kleinen Beispielprogramms durch. 
Hierzu schreiben wir ein paar Zeilen für einen hypothetischen Taschenrechner.

Wir gehen davon aus, dass Sie bereits die Aufgabe [PARTREF::git-Zweitrepo] erledigt und 
entsprechend ein neues und sauberes Repo bereit haben, in welchem Sie sich ungehindert auslassen 
können.

Falls Sie diese Aufgabe übersprungen haben, legen Sie einfach ein neues Verzeichnis außerhalb 
ihres ProPra-Repos und führen Sie den `git init` Befehl aus. Da wir in dieser Aufgabe weder `git 
push` noch `git pull` benötigen, müssen Sie auch kein neues Repository auf GitLab oder ähnlichen 
Git-Servern anlegen.


Was tut git init? Um das zu verstehen, haben wir einen nützlichen Hilfsbefehl: `git help`.
Dieser gibt uns ausführliche Dokumentation zu praktisch jedem git-Befehl, Begriff oder Konzept aus.
Führen wir `git help` aus erhalten wir eine kurze Liste an gängigen git-Befehlen, dann eine 
längere mit noch mehr Befehlen und ganz unten steht noch ein weiterer nützlicher Hinweis.

```
'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
```

Wir wollen jetzt lernen, was `git init` tut. Führen Sie also den `git help` Befehl für `git init` 
aus und beantworten Sie: 

[EQ] Was macht der Befehl `git init`? 
Referenzieren Sie hierbei die Git-Hilfe und vor allem die Teile, die Sie verstehen.

[NOTICE]
Zu Beginn wird vieles in der git-Hilfe ihren Kenntnisstand übersteigen und kann überwältigend wirken. 
Es hilft dann, alles auszublenden, was für die aktuelle Aufgabe irrelevant ist. 
Nach und nach werden Sie Wissen ansammeln und können dann auch kompliziertere Erklärungen verstehen.

Die gleichen Inhalte lassen sich übrigens auch im Browser in der 
[git Referenz](https://git-scm.com/docs) 
nachschlagen.
[ENDNOTICE]

In der Dokumentation zu `git init` werden ihnen vielleicht der `.git` Ordner sowie die "Objekte" 
aufgefallen sein. 
Um deren Zweck zu verstehen, lesen wir den Abschnitt 
[Creating a Git repository](https://git-scm.com/docs/gitcore-tutorial) 
im `gitcore-tutorial`.

[EQ] Was befindet sich im Verzeichnis `objects`?  

[EQ] Wie werden Git-Objekte referenziert?  

[EQ] Wie heisst der default Branch?
Kann ich diesen umbenennen und brauche ich ihn überhaupt?  

Nun haben wir also ein neues und sauberes git Repo und haben verstanden, was sich bis dato darin 
befindet. 
Jetzt wollen wir den aktuellen Zustand unseres Repos betrachten. 
Dafür gibt es den Befehlt `git status`. 
Dieser zeigt uns Informationen darüber an, welche Dateien git sieht, 
beobachtet und ob es Veränderungen zum letzten Commit gibt. 
Führen Sie `git status` jetzt aus, werden Sie feststellen, dass das Repo fast leer ist:
Es gibt einen Zweig ("branch"), aber keine Commits. 
Damit wir ein bisschen mit Daten hantieren können, brauchen wir also erstmal welche in unserem Repository. 
Beginnen wir also mit unserem fiktiven Grundgerüst, der Funktionsdefinition:

```python
# Ein einfacher Rechner

def addiere(a, b):

```

Erstellen Sie die Datei `calculator.py` mit dem obigen Inhalt und schauen Sie sich nochmal den 
Status an.

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	calculator.py

nothing added to commit but untracked files present (use "git add" to track)
```

Hier sehen wir jetzt einige neue Informationen. 
Zum einen bekommen wir noch immer "No commits yet" angezeigt. 
Was ja auch stimmt, denn wir haben lediglich eine neue Datei angelegt. 
Zumindest scheint git aber *irgendwas* über diese Datei zu wissen, denn sie wird als "Untracked file" 
angegeben.

Aber weiß git auch, was sich in dieser Datei befindet? 
Die letzte Zeile gibt uns einen kleinen Hinweis. 
Git betrachtet den Inhalt einer Datei erst, wenn wir die Datei mit `git add` zum 
Verfolgen ("Tracken") markieren.

Fügen Sie also jetzt die Datei der Staging-Area hinzu und prüfen Sie wieder den Status.
Welche Veränderung stellen Sie fest?

Soweit die Praxis, jetzt wieder ein bisschen Theorie.
Lesen Sie den Artikel 
[What really happens when I do git add](https://medium.com/@raffs.os/what-really-happens-when-i-do-git-add-8af29c1ec903).

Dazu ein paar Verständnisfragen:

[EQ] Welche Sorten von git-Objekten gibt es und was speichern die?  

[EQ] Wo speichert git die Metadaten über eine Datei und wo die Inhalte?  

[EQ] Speichert git erst beim Commiten Änderungen an einer Datei, oder schon vorher?  

[EQ] Wenn man Änderungen an einer Datei vornimmt, nachdem sie dem git Index hinzugefügt wurde, muss 
man diese Änderungen wieder dem Index hinzufügen, damit Sie im Commit landen?  

[NOTICE]
Wir erinnern uns an dieser Stelle nochmal an [PARTREF::git-Funktionsweise], wo wir ja bereits 
festgestellt haben, dass git immer Snapshots speichert. 
Die Blob-Objekte sind nämlich genau das.
[ENDNOTICE]

Wir sollten jetzt Verständnis dafür haben, was der git-Index ist, was Objekte sind, welche 
Objekttypen es gibt und was passiert, wenn wir mit `git add` eine Datei zum Index hinzufügen.

Jetzt schauen wir uns einen neuen sehr nützlichen Befehl an, nämlich `git diff`.
Und was tut der? Rufen Sie doch nochmal die Dokumentation zum Befehl auf.

Das ist richtig viel Stoff!
Das meiste davon interessiert uns aber gar nicht.

Es gibt jedoch einen Abschnitt, den wir uns mal ansehen sollten. Nämlich die *EXAMPLES*. Diese 
befinden sich ganz am Ende der Dokumentation. Darin sehen wir, direkt zu Beginn, folgende Beispiele:

```
EXAMPLES
       Various ways to check your working tree

               $ git diff            (1)
               $ git diff --cached   (2)
               $ git diff HEAD       (3)
               $ git diff AUTO_MERGE (4)

           1.   Changes in the working tree not yet staged for
                the next commit.
           2.   Changes between the index and your last commit;
                what you would be committing if you run git
                commit without -a option.
           3.   Changes in the working tree since your last
                commit; what you would be committing if you run
                git commit -a
           4.   Changes in the working tree you’ve made to
                resolve textual conflicts so far.
```

Das sieht doch schon um einiges verständlicher aus. Aktuell interessiert uns nur Beispiel 1.
Führen wir es doch mal aus und gucken, was passiert.

[EQ] Was gibt `git diff` jetzt aus und warum?   

Erweitern wir nun unsere Additionsfunktion:

```python
# Ein einfacher Rechner
def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

```

Und führen Sie nochmal `git diff` aus.
Jetzt haben wir endlich eine Ausgabe!
Wenn wir jetzt auch nochmal `git status` ausführen, schließt sich der Kreis.

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   calculator.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   calculator.py
```

Wir können jetzt also Folgendes feststellen: 

1. Wir haben noch immer keine Commits erzeugt.
2. Wir haben Änderungen/Neue Dateien zum Commiten vorgemerkt.
3. Wir haben weitere Änderungen an dieser neuen Datei vorgenommen, seitdem wir Sie zum Commiten 
   vorgemerkt haben.
4. Git gibt uns hilfreiche Tips für Befehle welche wir evtl. gebrauchen könnten. 

[EQ] Welche Befehle sind das und was tun sie? (Wenn Sie einen Befehl nicht kennen, denken Sie an 
`git help`)

Fügen Sie die Änderungen an der datei `calculator.py` ebenfalls der Staging-Area hinzu.

[EQ] könnten wir jetzt nochmal zum vorherigen Status der Datei zurückkehren? 

Als Letztes schnüren Sie alles zu einem neuen Commit mit einer sinnvollen Commit-Nachricht.

[EQ] Was passiert nun im Hintergrund?

Erweitern wir wieder unseren Taschenrechner, diesmal mit einer Funktionsdefinition für eine 
Multiplikationsfunktion:

```python
# Ein einfacher Rechner
def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

def multipliziere(a, b):

```

Diese neuen Änderungen fügen wir jetzt wieder dem Index hinzu und nehmen dann direkt weitere 
Änderungen vor:

```python
# Ein einfacher Rechner
def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

def multipliziere(a, b):
    # Diese Funktion multipliziert zwei Zahlen
    return a * b

```

Ohne diese Änderungen dem Index hinzuzufügen, können wir jetzt wieder einen näheren Blick auf 
`git diff` werfen um zu verstehen, welche verschiedenen Optionen uns im Alltag nützlich werden 
können. 

Schauen Sie sich also wieder die Beispiele in der `git diff` Dokumentation und probieren Sie 
folgende Szenarios durch:

[EC] Vergleichen Sie den aktuellen Zustand der Datei mit den bereits vorgemerkten Änderungen.

[EC] Vergleichen Sie die vorgemerkten Änderungen mit dem letzten Commit-Zustand.

[EC] Vergleichen Sie den aktuellen mit dem letzten Commit-Zustand.  

Zusatzfrage:

[EQ] Git speichert ja eigentlich nur Snapshots der Dateien, wie erzeugt es dann also die diff 
ausgabe?

[HINT::Ich stehe auf dem Schlauch, wo soll ich das denn finden?]
Die Ausgabe von `git diff` gibt ihnen einen Hinweis:

```diff 
diff --git a/ch/Werkzeuge/Git/git-102.md b/ch/Werkzeuge/Git/git-102.md
new file mode 100644
index 0000000..140f45f
--- /dev/null
+++ b/ch/Werkzeuge/Git/git-102.md
```

[ENDHINT]

Jetzt, wo wir unsere Multiplikation vollständig implementiert haben, wollen wir wieder den 
aktuellen Zustand festhalten. Fügen Sie die verbleibenden Änderungen dem Index hinzu und erstellen 
Sie wieder einen Commit mit sinnvoller Nachricht. 

Damit sind wir an dieser Stelle mit dem Großteil der Aufgabe fertig. 

Schauen wir uns zuletzt noch ein weiteres nützliches Werkzeug etwas genauer an, `git log`.

`git log` ist praktisch unser Git-Tagebuch. Hier werden alle Commits festgehalten. Das ist 
insofern nützlich, als es uns ermöglicht, die Commit-Historie durchzusehen. So können wir 
nachvollziehen, was Commits verändert haben, und ihre Hash-Namen ermitteln. Mit diesen 
Hash-Namen können wir dann entweder den gesamten Working Tree oder einzelne Dateien auf den 
Zustand eines bestimmten Commits zurücksetzen.

Wenn wir jetzt einfach nur `git log` ohne irgendwelchen weiteren Argumente aufrufen, sieht 
unsere Ausgabe ungefähr so aus:

```
commit f8edd7796f5bee38a383ba131a8caebcafaceb6c (HEAD -> master)
Author: Max Mustermann <Max.Mustermann@example.com>
Date:   Tue Apr 29 15:44:36 2025 +0200

    add multiplication

commit 2a1251cf381308cf113fe3f23aedc4fb792d6365
Author: Max Mustermann <Max.Mustermann@example.com>
Date:   Tue Apr 29 15:31:51 2025 +0200

    implemented addition
```

Soweit so gut, was sehen wir hier also?

Wir sehen:
1. Den commit hash `commit 2a1251cf381308cf113fe3f23aedc4fb792d6365`
2. Den Autor `Author: Max Mustermann <Max.Mustermann@example.com>`
3. Das Datum `Date:   Tue Apr 29 15:31:51 2025 +0200`
4. Die Commit-Nachricht: `implemented addition`

Aber man kann `git log` noch erweitern. Wenn Sie möchten, schauen Sie ruhig mal in die 
Dokumentation. Dort werden Sie sicherlich *eine Menge* an Optionen finden.

Zu Beginn gibt es jedoch trotzdem ein paar Optionen, die wir Ihnen mit an die Hand geben möchten.

Zum einen gibt es `--oneline` damit wird schlichtweg ein Commit auf eine einzelne Zeile 
reduziert. Dies kann vor allem bei ganz viel Historie hilfreich sein.

Zum anderen gibt es `-p`, dadurch wird für jeden Commit ein sogenannter patch text erzeugt. Einfach 
gesagt für jeden Commit ein diff auf alle files. Streng genommen gibt es ein paar unterschiede zu 
`git diff`, welche das genau sind, können sie in der `git log` Doku nachlesen. Für unsere Zwecke 
sind die beiden Befehle in diesem Fall aber vorerst mehr oder weniger synonym.

Manchmal ist es hilfreich, sich alle Commits anzeigen zu lassen, in denen eine bestimmte Datei 
verändert wird. Dazu kann man einfach an seinen `git log` Befehl den vollständigen Dateipfad 
anhängen. So kann man sich z.b. mit `git log -p path/to/file` alle Veränderungen der Datei 
`file` im Verzeichnis `path/to` anschauen.

In größeren Repos ist es öfter nützlich, mithilfe des Datums Commits zu suchen, dazu stellt `git 
log` einige Befehle bereit, am häufigsten genutzt werden sicherlich `--until <date>, --before 
<date>` oder `--since <date>, --after <date>` welche mehr oder weniger selbsterklärend sind. 

Außerdem praktisch ist das Suchen nach einem bestimmten Autor. Dafür gibt es `git log 
--author="Jane Doe"` oer `git log --author=Jane` womit man entweder den gesamten oder nur einen 
Teilstring matcht.
[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::wir prüfen das protokoll und die abgaben der teilnehmer auf verständnis]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
