title: git-Grundlagen
stage: alpha
timevalue: 2
difficulty: 3
explains:
assumes: git-Funktionsweise
---

[SECTION::goal::experience]
Ich lerne, wie die Grundfunktionen von git funktionieren, und festigte mein mentales Modell von Git.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::Git101] haben wir gerade so das Nötigste gelernt, um unsere Aufgaben im ProPra 
abzugeben. Jetzt geht es darum, das gelernte zu vertiefen und das Wissen um die Befehle und 
[PARTREF::git-Funktionsweise] zu festigen.
[ENDSECTION]

[SECTION::instructions::detailed]
In dieser Aufgabe werden wir so richtig tief in die Interna von git einsteigen. 
Wie verwaltet git Dateien und Commits? 
Wie können wir diese vergleichen und uns einen Überblick darüber 
verschaffen, was während der Entwicklung eines Projektes geschieht?
 
Die Aufgabe wird, wie der Name schon vermuten lässt, die Grundlage für unser Verständnis 
von git festlegen. Denn ohne zu verstehen, was ein Objekt, Blob, Snapshot oder essenzielle Begriffe 
wie der Index, die Staging Area sind, braucht man gar nicht erst weiterzumachen.
Je mehr sie über git lernen, umso mehr werden Sie Rückschlüsse auf die in dieser Aufgabe 
gesehenen Begriffe und Konzepte ziehen können.
Das Erlernen und Verstehen neuer git-Befehle wird ihnen auch deutlich leichter fallen, wenn Sie 
diese Grundlagen verstanden haben.

Damit wir die Befehle nicht einfach nur herunterrattern, arbeiten wir die Inhalte anhand eines 
kleinen Beispielprogramms durch. 
Hierzu schreiben wir ein paar Zeilen für einen hypothetischen Taschenrechner.

Anders als bei den meisten Aufgaben werden Sie für diese ein ganz neues Repo erstellen. 
Das dient in erster Linie dazu, dass Sie weiteres Verständnis darüber aufbauen was in diesem 
Schritt passiert und einmal die Repo-Erstellung selber durchturnen als wie üblich von Tools wie 
Gitlab und Co. abgenommen zu bekommen. 
Dafür erstellen Sie ein neues Verzeichnis **außerhalb ihrer bestehenden ProPra-Repositories**, 
navigieren mit ihrer Kommandozeile dort hinein und führen den Befehl `git init` aus. 

[HINT::Kann ich kein neues Repository in meinen bestehenden erstellen?]
Jein. Git bietet die Möglichkeit des Einbindens weiterer Repos mithilfe sogenannter Submodules an. 
Deren komplexität übersteigt aber massiv unseren aktuellen Kenntnisstand weshalb wir hier nicht 
weiter darauf eingehen werden.
[ENDHINT]

Schauen wir jetzt mit `ls` in unser Verzeichnis fällt uns auf, dass uns gar nichts auffällt...
Wir haben ja immernoch ein leeres Verzeichnis.
Aber warum ist das so?
Wenn `git init` ausgeführt wird, wird ein neuer unsichtbarer Ordner angelegt, `.git`.
Führen wir `ls -a` aus, sehen wir auch diesen.
Dieser `.git` Ordner wird auch *Repository Directory* genannt. 
Darin speichert git alle Informationen über unser Repository. 
Dabei geht es nicht nur um Meta-Informationen, sondern auch um **alle** Daten, die über die 
Lebenszeit unseres Repositories mithilfe von git getrackt werden.
Was bedeutet getrackt? Git interessiert sich nur für Dateien, die wir ihm explizit angeben. 
Alle anderen Dateien kann es zwar sehen, wird deren Inhalt aber nicht ohne Aufforderung 
speichern oder anderweitig verfolgen.
Wie genau das funktioniert und was gespeichert wird, lernen wir im weiteren Verlauf der Aufgabe.

Genauso wie es ein *Repository Directory* gibt, so gibt es auch ein *Working Directory* (dt. 
Arbeitsverzeichnis), manchmal auch *Working Tree* genannt. 
Warum *Working **tree** *? Weil git Verzeichnisse grundsätzlich als Baumstrukturen aufzeichnet.

Jetzt geht es aber erstmal zurück zu unserer Aufgabe.
In [PARTREF::git-Funktionsweise] haben Sie schon einmal den Befehl `git help` kennengelernt. 
Diesen wollen wir jetzt wieder nutzen um zu lernen wozu `git init` genutzt wird.

[EQ] Was macht der Befehl `git init`? 
Referenzieren Sie hierbei die Git-Hilfe und vor allem die Teile, die Sie verstehen.

In der Dokumentation zu `git init` werden ihnen vielleicht der `.git` Ordner sowie die "Objekte" 
aufgefallen sein. 
Um deren Zweck zu verstehen, lesen wir den Abschnitt 
[Creating a Git repository](https://git-scm.com/docs/gitcore-tutorial) 
im `gitcore-tutorial`.

[EQ] Was wird im Verzeichnis `.git/objects` abgelegt?  

[EQ] Wie werden Git-Objekte referenziert?  

[EQ] Wie heisst der default Branch?
Kann ich diesen umbenennen und brauche ich ihn überhaupt?  

Nun haben wir also ein neues und sauberes git Repo und haben verstanden, 
was sich bis dato darin befindet. 
Als Nächstes wollen wir herausfinden, 
wie wir den aktuellen Zustand unseres Repos betrachten können. 
Dafür gibt es den Befehl `git status`. 
Dieser zeigt uns Informationen darüber an, welche Dateien git sieht, 
beobachtet und ob es Veränderungen zum letzten Commit gibt. 
Führen Sie `git status` jetzt aus, werden Sie feststellen, dass das Repo fast leer ist:
Es gibt einen Zweig ("branch"), aber keine Commits darauf. 
Damit wir ein bisschen mit Daten hantieren können, brauchen wir also erstmal welche in unserem Repository. 
Beginnen wir also mit unserem fiktiven Grundgerüst, der Funktionsdefinition:

```python
# Ein einfacher Rechner

def addiere(a, b):
    
```

Erstellen Sie die Datei `calculator.py` mit dem obigen Inhalt und schauen Sie sich nochmal 
den Status an.

Hier sehen wir jetzt einige neue Informationen. 
Zum einen bekommen wir noch immer "No commits yet" angezeigt. 
Was ja auch stimmt, denn wir haben lediglich eine neue Datei angelegt. 
Zumindest scheint git aber *irgendwas* über diese Datei zu wissen, denn sie wird als "Untracked file" 
angegeben.

Aber weiß git auch, was sich in dieser Datei befindet? 
Die letzte Zeile des git-Status gibt uns einen kleinen Hinweis. 

Wir erinnern uns: Vorhin haben wir gelernt, dass git zwar alle Dateien im Arbeitsverzeichnis 
sehen kann, sich aber grundsätzlich erst nach Aufforderung um Sie kümmert?
Erst wenn wir `git add` benutzen, sagen wir git, welche Dateien es verfolgen/tracken soll.
Genau das machen wir jetzt.

#### Git-Index

Der git-Index, auch Staging-Area genannt, ist ein Kernelement der git-Arbeitsweise und versteht 
sich quasi als eine Art Zwischenablage.
Er kommt ständig zum Einsatz, nämlich immer dann, wenn wir dem Repository neue Dateien 
hinzufügen, bestehende Dateien ändern oder bereits vorhandene Dateien löschen wollen.

Wie weiter oben bereits angemerkt, verwenden wir dafür den Befehl `git add`.

Man kann sich die Staging-Area als Pufferzone zwischen dem Arbeitsverzeichnis und dem Repository
vorstellen:
Erst wenn ein neuer git-Commit erstellt wird, werden alle im Index vorgemerkten Dateien dauerhaft in
einem neuen Commit-Objekt gespeichert. 
Hierbei werden vor allem nicht nur Änderungen an Dateien gesichert, sondern immer vollständige 
Abbilder.
Einen Commit kann man sich also wie eine Momentaufnahme, also einen [TERMREF::Snapshot (git)] 
(dt. Schnappschuss), vorstellen.
Bestehende unveränderte Dateien werden einfach vom vorherigen Commit übernommen (mithilfe einer 
Referenz). 
So spart git Rechenaufwand und Speicherplatz. 

In [PARTREF::git-Funktionsweise] haben wir es bereits gesehen, aber wer sich dazu einen 
Auffrischer abholen möchte, kann sich nochmal die Grafiken im Teil 
[What is Git?](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) 
des Pro Git Books anschauen.

Die Staging-Area erlaubt uns auch, wie so vieles in git, Änderungen im Arbeitsverzeichnis 
rückgängig zu machen, indem wir den Zustand der Datei auf den der Staging-Area zurücksetzen. 
Daher bietet es sich an, öfter mal Dateien zu sinnvollen Zeitpunkten der Staging-Area 
hinzuzufügen, damit man ggf. auf den dabei gesicherten Zustand zurückgreifen kann.

Trotzdem sollte man das Ganze nicht als "Backup" sehen, denn wirklich langfristig gesichert sind 
unsere Änderungen erst nach dem Hinzufügen zu einem Commit.

[NOTICE]
Übrigens: als Backup sollte man ein git-Repository sowieso nie betrachten. 
Höchstens, wenn wir unseren lokalen Zustand auch auf einen entfernten Server gepusht haben. 
Allerdings können wir, nachdem wir einen Commit erstellt haben, jederzeit zu dessen erfassten 
Zustand zurückkehren. 
Wer mehr darüber lernen möchte, findet später im Abschnitt [PARTREF::git-Fehlerbehebung] mehr 
praktisches Wissen.
[ENDNOTICE]

Fügen Sie also jetzt die Datei `calculator.py` der [TERMREF::Staging-Area] hinzu und prüfen Sie 
wieder den Status.

[EQ] Welche Veränderungen stellen Sie fest?

Inzwischen sollten wir ein recht gutes Verständnis haben, was die Staging-Area/Index, Working 
Directory und Repository Directory sind. 
Außerdem sollten wir wissen, wie man Dateien zum Index hinzufügt.

Als nächstes, möchten wir wieder ein bisschen in den theoretischeren Teil eintauchen.
Schauen Sie dazu das Video [Git from the inside out](https://www.youtube.com/watch?v=fCtZWGhQBvo).
Zunächst nur bis 16:08 (Einschließlich des Abschnittes "Each Commit has a Parent").

Das Video gibt es auch in Textform, was vielleicht zum späteren Referenzieren hilfreich sein kann: 
[Git from the inside out](https://maryrosecook.com/blog/post/git-from-the-inside-out).
Wir schauen das Video ca. bis zum Textabschnitt "Check out a commit".

In diesem Video werden einige sehr grundlegende Konzepte aufgegriffen. 
Hierzu ein paar Fragen, die Sie beantworten können sollten, bevor Sie mit der Aufgabe fortfahren:

[EQ] Wie speichert Git eine Datei, wenn `git add` ausgeführt wird? (blob object, mit hash name, 
eindeutig referenzierbar)

[EQ] Wenn wir mit `git add` weitere Änderungen an einer Datei zum Index hinzufügen, bevor wir 
bestehende Änderungen im Index commiten, was passiert mit dem bestehenden blob-Objekt?

[EQ] Was speichert git, wenn wir einen neuen Commit erstellen? (commit object mit referenz auf 
tree und subtrees)

[EQ] Kann es zwei identische Commit-Objekte geben? (nein, meta informationen wie Autor und 
Zeitstempel verhindern das)

[EQ] Commit, Working Directory und Index können vermeintlich auf die gleichen Daten zeigen. 
Allerdings können nur je zwei der genannten wirklich auf die gleichen Daten zeigen, welche sind 
das? (Commit und Index)

### Dateien im Index anschauen

Bevor wir weiter machen, ein kurzer exkurs.
Git gibt uns einige Befehle an die Hand, welche uns erlauben die Tatsächlich gespeicherten 
Dateien im Repository-Verzeichnis anzuschauen. 
Diese sind `git ls-files`, `git ls-tree` und `git show`.
Wer mit dem Terminal etwas vertraut ist, erkennt ls natürlich sofort wieder.
`git show` ist ein recht universell einsetzbares tool welches uns erlaubt alle möglichen git 
Dateien/Objekte mithilfe ihrer Hash-Referenzen zu betrachten.
Da wir noch keinen Commit erstellt haben, bringt uns `ls-tree` noch nicht viel - 
Wir erinnern uns: Trees werden erst zum Commit-Zeitpunkt erstellt.
Allerdings können Sie `git ls-files` und `git show` schon ausprobieren.

[EC] Finden Sie den Hash ihres blob-Objektes der `calculator.py` und schauen Sie sich dessen 
inhalt an.

[NOTICE]
`git ls-files` gibt Standardmäßig nur den Dateinamen des gespeicherten Blob-Objektes aus, nicht 
dessen Hash. Um das zu bewerkstelligen fehlt noch ein Argument. Denken Sie an `git help`.
[ENDNOTICE]

Warum ist das nützlich? Es gibt seltene Fälle wo es hiflreich sein kann noch einmal den Inhalt 
eines Blobs anschauen zu können. Nämlich genau dann wenn man mit `git add` bereits bestehende 
Dateien neu zum Index hinzugefügt hat *ohne* dass man vorher den Zustand in einem Commit 
festgehalten hat.
`git show` erlaubt uns den Inhalt des vorherigen blobs noch einmal anzuschauen.
Damit wir den blob dafür finden können, brauchen wir allerdings noch einen weiteren Befehl, `git fsck`. 

Um besser verstehen zu können, was der Befehl tut verändern wir unsere Funktionsdefinition wie folgt:

```python
# Ein einfacher Rechner

def addiere(a, c):
    
```

Dann fügen wir Sie wieder mit `git add` dem Index hinzu.

In unserem Beispielprogramm sind die Auswirkungen marginal, man könnte einfach `(a, c)` wieder 
zu `(a, b)` ändern und alles wäre beim Alten.
Allerdings kommt es in der echten Welt gelegentlich zu gröberen Schnitzern bei größeren Änderungen,
da kann es Hilfreich sein, wenn man den vorherigen Status nochmal ansehen kann.
Wenn man jetzt `git fsck` ausführt, erhält man einige interessante Informationen.

Zum einen sagt uns `fsck`, dass `HEAD` auf einen `unborn branch (master)` zeigt.
Das ist kurios, aber nicht besonders schlimm. Wir haben schlicht noch keine Commits auf dem Branch.
Im späteren Verlauf der Aufgabe wird sich das ändern. 
Führen Sie dann ruhig nochmal `git fsck` aus und schauen Sie sich die Veränderungen in der 
Ausgabe an.
Für uns interessant sind jetzt aber die sogenannten `dangling blobs`. 
Überlegen Sie doch mal kurz was das bedeuten könnte. 
In git ist *dangling blob* nichts anderes als ein blob-Objekt ohne zugehörige Datei-Referenz.
Sprich, git weiß nicht, zu welcher Datei der blob gehört. 
Das passiert fast immer dann, wenn wir, wie in unserem Fall, mehrere Male die gleiche Datei mit 
`git add` zum Index hinzufügen. 
Es gibt zwar noch andere Fälle in denen *dangling blobs* entstehen können, diese sind für uns 
aber gerade unwichtig.

[EC] Wie schauen Sie sich den inhalt des *dangling blob* Objektes an?

Wenn Sie das geschafft haben, können Sie die Funktionsdefinition wieder auf den vorherigen 
Zustand zurücksetzen. Wie sie das machen, ist ihnen überlassen.

### Veränderung feststellen

Als nächstes, schauen wir uns einen weiteren nützlichen Befehl an, nämlich `git diff`.
Und was tut der? Rufen Sie doch nochmal die Dokumentation zum Befehl auf.

Das ist richtig viel Stoff!
Das meiste davon interessiert uns aber noch gar nicht.

Trotzdem gibt es nützliche Informationen in der Hilfeseite, im Abschnitt *EXAMPLES*.

Mit unserem bisherigen Wissen aus der Aufgabe sollten wir auch schon einigermaßen verstehen 
können was im ersten Beispiel (1) passiert. 

[EQ] Führen Sie `git diff` aus. Was stellen Sie fest? Warum ist das so?

Danach erweitern wir die Funktion um folgenden Inhalt:

```python
# Ein einfacher Rechner
def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

```

[EQ] Führen Sie noch einmal `git diff` aus. Was hat sich verändert?

[EQ] Git speichert nur vollständige Abbilder der Dateien, wie erzeugt es denn die `git diff` 
Ausgabe?

Jetzt wo wir einige Änderungen vorgenommen haben, wollen wir wieder mal einen Blick auf `git 
status` werfen.
Führen Sie den Befehl noch einmal aus und lesen Sie gründlich die Ausgabe.

[EQ] Was hat sich seitdem an der `git status`-Ausgabe verändert?

[EQ] Wie kann man mit `git status` die spezifischen Änderungen anzeigen lassen, 
die mit einem `git commit` festgehalten werden würden? 
Wie kann man außerdem die Veränderungen zwischen Working-Directory und Staging-Area anzeigen?

Außerdem sollte ihnen `git status` jetzt einige Befehle zum Verwalten der Dateien im Index anbieten.

[EQ] Welche Befehle sind das und was tun sie? Geben Sie kurze Erklärungen an.
(Wenn Sie einen Befehl nicht kennen, denken Sie an `git help`)

Fügen Sie die Änderungen an der datei `calculator.py` ebenfalls der Staging-Area hinzu.
Erinnern Sie sich daran, was wir im vorherigen Abschnitt über git-Objekte gelernt haben und 
wie `git add` funktioniert.

Jetzt landen wir in einer interessanten Situation. Wir haben jetzt ein neues Blob-Objekt für 
calculator.py erstellt. Mit `git ls-files -s` können wir jetzt den Hash dieses neuen Objekts sehen.
Wenn wir aber `tree .git/objects` ausführen, sehen wir, dass sich dort drei Ordner befinden, die 
jeweils ein Objekt beinhalten. 
Wir überlegen also: Wie oft haben wir `git add` bisher ausgeführt? Richtig, dreimal.
Wenn wir jetzt nochmal `git fsck` ausführen sehen wir auch zwei *dangling blobs*.
Was können wir daraus schließen? Es existieren für alle Ausführungen von `git add` jeweils die 
Blob-Objekte, aber git interessiert sich nur noch für das aktuellste Objekt, denn nur dessen 
Wert bekommen wir mit `ls-files` zurückgegeben.


Erstellen Sie jetzt ihren ersten Commit mit einer passenden Commit-Nachricht.

[FOLDOUT::Was ist eine sinnvolle Commit-Nachricht?]
Das ist eine sehr gute Frage. 
So gut, dass es sogar 
[Studien darüber gibt.](https://dl.acm.org/doi/10.1145/3510003.3510205)
Grundsätzlich gilt aber, halten Sie sich kurz und beschreiben Sie klar was der Commit beinhaltet.
In Ihrem Fall könnte das z.B. heißen: `addition: calculator.py`.
Später dann vielleicht sowas wie: `fix: division no longer incorrectly divides by zero`
Die Sprache ist dabei recht egal, aber natürlich wird, genau wie im Code, häufig Englisch verwendet.
Mehr tips dazu, gibt es wie immer im Internet. Z.b. hier: 
https://docs.wpvip.com/development-workflow/write-a-good-commit-message/
[ENDFOLDOUT]

Erweitern wir wieder unseren Taschenrechner mit einer Funktionsdefinition für eine 
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

Jetzt können wir wieder einen näheren Blick auf `git diff` werfen um zu verstehen, 
welche verschiedenen Optionen uns im Alltag nützlich werden können. 

Schauen Sie sich jetzt Beispiele (3-4) in der `git diff` Dokumentation und probieren Sie 
folgende Szenarios durch:

[EC] Vergleichen Sie den aktuellen Zustand der Datei mit den bereits vorgemerkten Änderungen.

[EC] Vergleichen Sie die vorgemerkten Änderungen mit dem letzten Commit-Zustand.

[EC] Vergleichen Sie den aktuellen mit dem letzten Commit-Zustand.

Jetzt, wo wir die Multiplikationsfunktion vollständig implementiert haben, wollen wir wieder den 
aktuellen Zustand festhalten. 
Fügen Sie die verbleibenden Änderungen dem Index hinzu und erstellen Sie wieder einen Commit mit 
sinnvoller Nachricht. 

### Git-Historie

Nicht selten wollen wir in Git aber nicht nur neue Änderungen hinzufügen und uns ausschließlich 
Vorwärts bewegen, sondern oft auch in die Vergangenheit schauen.
Vielleicht, um einen alten Zustand zu betrachten und ggf. auch wiederherzustellen oder einfach nur 
um zu prüfen, was wir aktuell für Commits im Repository haben.

Dazu schauen wir uns in diesem Abschnitt noch kurz den Befehl `git log` an.

`git log` ist praktisch unser Git-Tagebuch. Hier werden alle Commits festgehalten. 
Das ist insofern nützlich, als es uns ermöglicht, die Commit-Historie durchzusehen. 
So können wir nachvollziehen, was Commits verändert haben, und ihre Hash-Namen ermitteln. 

Wir erinnern uns an den Beginn der Aufgabe und unsere git-Objekte: 
Dateien und Commits bekommen von git beim Hinzufügen zum Index bzw. erstellen des Commits einen 
eindeutigen Hash-Namen zugewiesen. 

Mit diesen Hash-Namen können wir die Zustände von Dateien und Commits zum gegebenen Zeitpunkt 
erhalten und dann z.B. auf diesen Zeitpunkt zurücksetzen oder andere nützliche Sachen machen.
Schauen Sie sich später vielleicht mal die Aufgabe [PARTREF::git-bisect] an.

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
1. Den Commit-Hash `commit 2a1251cf381308cf113fe3f23aedc4fb792d6365`
2. Den Autor `Author: Max Mustermann <Max.Mustermann@example.com>`
3. Das Datum `Date:   Tue Apr 29 15:31:51 2025 +0200`
4. Die Commit-Nachricht: `implemented addition`

Aber man kann `git log` noch erweitern bzw. anpassen. 
Schauen Sie ruhig mal in die Dokumentation. 
Dort werden Sie sicherlich *eine Menge* an Optionen finden, 
von denen Sie viele aktuell vermutlich nicht brauchen werden.

Zu Beginn gibt es jedoch trotzdem ein paar Optionen, die wir Ihnen mit an die Hand geben möchten.

Zum einen gibt es `--oneline`, damit wird schlichtweg ein Commit auf eine einzelne Zeile reduziert. 
Dies kann vor allem bei ganz viel Historie hilfreich sein.

Zum anderen gibt es `-p`, dadurch wird für jeden Commit ein sogenannter patch text erzeugt. 
Einfach gesagt für jeden Commit ein diff auf alle files. 
Streng genommen gibt es ein paar unterschiede zu `git diff`, welche das genau sind, können sie 
in der `git log` Hilfe nachlesen. 
Für unsere Zwecke sind die beiden Befehle in diesem Fall aber vorerst mehr oder weniger identisch.

Manchmal ist es hilfreich, sich alle Commits anzeigen zu lassen, in denen eine bestimmte Datei 
verändert wird. 
Dazu kann man einfach an seinen `git log`-Befehl den relativen Dateipfad anhängen.

[EQ] Wie würde der `git log`-Befehl aussehen um alle Commits und deren Änderungen an unserer 
`calculator.py`-Datei anzuzeigen?

In größeren Repos ist es öfter nützlich, mithilfe des Datums Commits zu suchen, dazu stellt `git 
log` einige Befehle bereit. 
Am häufigsten genutzt werden sicherlich `--until <date>, --before <date>` oder `--since <date>, 
--after <date>` welche mehr oder weniger selbsterklärend sind. 

Außerdem praktisch ist das Suchen nach einem bestimmten Autor.
Dafür gibt es `git log --author="Jane Doe"` oer `git log --author=Jane` womit man entweder den 
gesamten oder nur einen Teilstring matcht. 
Das ist vor allem Hilfreich, wenn man mit mehreren Personen am gleichen Repository arbeitet.

Mit der Zeit werden Sie noch weitere nützliche `git log` Optionen kennenlernen und diese immer 
weiter ihren eigenen Bedürfnissen anpassen.
[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::wir prüfen das protokoll und die abgaben der teilnehmer auf verständnis]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]