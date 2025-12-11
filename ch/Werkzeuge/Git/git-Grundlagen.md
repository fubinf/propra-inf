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
abzugeben. 
Jetzt geht es darum, das Gelernte zu vertiefen und das Wissen um die Befehle und 
[PARTREF::git-Funktionsweise] zu festigen.
[ENDSECTION]

[SECTION::instructions::detailed]
In dieser Aufgabe werden wir vertieft in die Interna von git einsteigen:
Wie verwaltet git Dateien und Commits? 
Wie können wir diese vergleichen und uns einen Überblick darüber 
verschaffen, was während der Entwicklung eines Projektes geschieht?
 
Um die git-Kommandos zu beherrschen, muss man diverse Konzepte verstehen:
Objekt, Blob, Snapshot, Index, Staging Area und ein paar mehr.
Nur mit diesem Wissen kann man ein mentales Modell von git bilden,
das zu echtem _Verständnis_ der git-Befehle und ihrer Wirkung führt.
Erst damit kann man sich in Situationen außerhalb des kleinen git-Einmaleins
(pull, add, commit, push; und zwar bitte ohne Merge-Konflikte) sicher fühlen
und wissen, was jeweils zu tun ist.

Wir arbeiten die Inhalte anhand eines winzig kleinen Beispielprojekts durch: 
wenige Zeilen Code für ein supersimples Taschenrechner-Programm.

Anders als bei den meisten Aufgaben brauchen wir diesmal ein ganz neues Repo. 
Das dient in erster Linie dazu, dass Sie weiteres Verständnis darüber aufbauen was in diesem 
Schritt passiert und einmal die Repo-Erstellung selber durchturnen als wie üblich von Tools wie 
Gitlab und Co. abgenommen zu bekommen. 
Dafür erstellen Sie ein neues Verzeichnis **außerhalb ihrer bestehenden ProPra-Repositories**, 
wie wir es bereits im [TERMREF::Hilfsbereich] teil der ProPra Grundlagen eingerichtet haben.
Navigieren Sie mit ihrer Kommandozeile dort hinein und führen den Befehl `git init` aus. 

[HINT::Kann ich ein neues Repository in meinem bestehenden erstellen?]
Jein. git bietet die Möglichkeit des Einbindens weiterer Repos mithilfe sogenannter Submodules an. 
Submodules sind auch bei kompetenten Git-Nutzer_innen berüchtigt dafür, wie kompliziert
das Leben dann wird; also gehen wir diesen Weg hier lieber nicht,
sondern trennen unser Übungs-Repo vom ProPra-Repo.
[ENDHINT]

### Git initialisieren; Repository-, Working-Directory und Bäume

Unser neues Repo wirkt auf den ersten Blick leer – sowohl im GUI-Dateimanager des Betriebssystems als auch in der Kommandozeile mit `ls`.
Warum ist das so?

Wenn `git init` ausgeführt wird, legt git den unsichtbaren Ordner `.git` an.
Führen wir `ls -a` aus oder lassen uns im Dateimanager versteckte Verzeichnisse anzeigen, sehen wir diesen Ordner.

Der Ordner `.git` wird auch [TERMREF::Repository-Verzeichnis] (engl. Repository-Directory) genannt.
*Repository* bedeutet *Lager* oder *Speicher*. Man kann es sich wie ein Archiv vorstellen, in dem git alle Informationen über unser Projekt speichert – sowohl Dateiinhalte als auch Metadaten.

Jedes Mal, wenn Sie eine Datei bzw. den Zustand einer Datei dauerhaft sichern möchten, übergeben Sie sie an das Repository.
Dieses Archiv teilen Sie später mit anderen Nutzern bzw. laden es auf einen Git-Server hoch.
Andere können dann jeden gespeicherten Zustand wiederherstellen oder eigene Zustände hinzufügen.

Gespeicherte Dateien lassen sich nicht ohne Weiteres ändern. Das ist wichtig zu wissen!
Haben Sie z. B. versehentlich Passwörter oder andere sensible Daten commitet und auf den Git-Server gepusht, wird es mühsam, diese wieder zu entfernen.
Dazu später mehr.

Neben dem *Repository Directory* gibt es auch das *Working Directory* (dt. Arbeitsverzeichnis), manchmal *Working Tree* genannt.
Das Arbeitsverzeichnis enthält den aktuellen Zustand Ihres Projekts. Mit diesen Dateien arbeiten Sie und können daran grundsätzlich alles ändern, denn alte Zustände lassen sich jederzeit aus dem Archiv wiederherstellen.
Aus dem Working Tree wählen Sie auch die Dateien und Änderungen aus, die Sie erneut im Repository speichern möchten.

Warum eigentlich *Working **Tree***?
Weil git Verzeichnisse grundsätzlich als Baumstrukturen darstellt.

Was haben wir bis hierhin gelernt?

* `git init` erzeugt das Repository-Verzeichnis und legt es im Ordner `.git` an.
* Im Repository-Verzeichnis befinden sich alle Informationen und Daten zu unserem Projekt.
* Wir können jederzeit zu jedem einmal abgelegten Zustand des Repositorys zurückkehren.
* Das Arbeitsverzeichnis (Working Directory) ist unsere lokale Arbeitskopie des Repos. Hier können wir beliebig Änderungen vornehmen.
* Diese Änderungen sowie neu hinzugefügte Dateien und Verzeichnisse können wir dem Repository zum dauerhaften Speichern übergeben.

### Wo bekomme ich nochmal Hilfe?

In [PARTREF::git-Funktionsweise] haben Sie bereits den Befehl `git help` kennengelernt.
Diesen wollen wir jetzt wieder nutzen, um zu lernen, wozu `git init` dient.

[EQ] Was macht der Befehl `git init`?
Referenzieren Sie hierbei die Git-Hilfe und vor allem die Teile, die Sie verstehen.

### Aufbau des Repository-Verzeichnisses und Git-Objekte

Besonders wichtig für uns sind der `.git`-Ordner (Repository-Verzeichnis) und die Git-Objekte.
Zwar müssen wir im Idealfall nie direkt in diesem Ordner arbeiten, aber es hilft beim Verständnis zu wissen, was sich darin befindet und wie git ihn verwaltet.

Lesen Sie dazu den Abschnitt
[Creating a git repository](https://git-scm.com/docs/gitcore-tutorial)
im `gitcore-tutorial` und beantworten Sie dann die folgenden Fragen.

[EQ] Was wird im Verzeichnis `.git/objects` abgelegt?

[EQ] Wie werden Git-Objekte referenziert?

[EQ] Wie heißt der Default-Branch, und können Sie ihn umbenennen bzw. brauchen Sie ihn überhaupt?

Ziehen wir ein kurzes Zwischenfazit:

Sie sollten jetzt verstehen, was `git init` tut, kennen den Unterschied zwischen Repository- und Arbeitsverzeichnis und wissen, was Git-Objekte sind und wo Sie Hilfe zu bestimmten Git-Kommandos finden können.

### `git status`

Wie wir wissen, können wir im Arbeitsverzeichnis nach Belieben Änderungen vornehmen.
Git hat jedoch eine andere Sicht auf das Arbeitsverzeichnis.
Um den Unterschied zu sehen, gibt es ein hilfreiches Kommando: `git status`.
Es zeigt an, welche Dateien git erkennt, welche es trackt und ob es Änderungen seit dem letzten Commit gibt.

Führen wir `git status` in unserem neuen Repository aus, sehen wir folgende Ausgabe:

```terminaloutput
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

### Was bedeutet eigentlich *tracken*?

*To track something* bedeutet *etwas zu verfolgen*.
Genau das macht git hier. Für jede getrackte Datei prüft Git, ob seit der letzten Archivierung Änderungen vorgenommen wurden.

Mit `git add` sagen wir git für jede Datei einmal, dass wir sie tracken wollen.
Nicht getrackte Dateien kann git zwar sehen, aber es speichert ihren Zustand nicht.

Es gibt auch eine Möglichkeit, bestimmte Dateien oder Verzeichnisse komplett zu ignorieren:
die `.gitignore`-Datei.
Git wird dann nie vorschlagen, diese Dateien zu tracken oder ihre Inhalte zu sichern.

### Was ist ein Commit?

Wir erinnern uns an das Archiv.
Git archiviert nur die Zustände des Repos, die wir ihm *übergeben*.
Diese Zustände nennt man „Commits“. 
Der Begriff kommt vom englischen Verb *to commit*, also „etwas übergeben“ oder „überlassen“.

Wir übergeben git also den aktuellen Zustand unseres Arbeitsverzeichnisses bzw. bestimmter 
Dateien und beauftragen es mit der Archivierung.
Git gibt uns dafür einen eindeutigen Identifikator, einen Hash.
Mit diesem Commit-Hash können wir jederzeit auf den Zustand zum Zeitpunkt dieses Commits zurückgreifen.

Auf Hashes und den Vorgang des Commitens gehen wir weiter unten noch genauer ein.
Das Verständnis fällt jedoch leichter, wenn wir erst ein paar Daten haben, 
mit denen wir Beispiel-Commits erstellen können.

Daher beginnen wir jetzt mit unserem fiktiven Grundgerüst, der Funktionsdefinition:

```python
# Ein einfacher Rechner

def addiere(a, b):
    
```

Erstellen Sie die Datei `calculator.py` mit dem obigen Inhalt und schauen Sie sich anschließend 
noch einmal den Status Ihres Git-Repositories an.

Jetzt zeigt `git status` einige neue Informationen.
Es erscheint weiterhin `No commits yet`, aber git hat die neue Datei erkannt.
Sie wird als `Untracked file` aufgeführt.

Weiß git aber schon, was in dieser Datei steht?
Die Ausgabe von `git status` deutet an, dass git zwar alle Dateien im Arbeitsverzeichnis sieht, 
sich jedoch erst dann aktiv um sie kümmert, wenn wir es dazu auffordern.

Wir erinnern uns: Mit `git add` teilen wir git mit, welche Dateien es tracken soll.
Das tun wir jetzt.

#### Git-Index

Der Git-Index, auch Staging-Area genannt, ist ein Kernelement der Git-Arbeitsweise und dient als 
eine Art Zwischenablage.
Er kommt immer dann zum Einsatz, wenn wir dem Repository neue Dateien hinzufügen, 
bestehende Dateien ändern oder bereits vorhandene Dateien löschen möchten.

Wie weiter oben bereits erwähnt, verwenden wir dafür den Befehl `git add`.

Man kann sich die Staging-Area als Pufferzone zwischen dem Arbeitsverzeichnis und dem 
Repository vorstellen:
Erst wenn ein neuer Commit erstellt wird, speichert git alle im Index vorgemerkten Dateien 
dauerhaft in einem neuen Commit-Objekt.
Dabei werden nicht nur Änderungen gesichert, sondern immer vollständige Abbilder.
Ein Commit ist also eine Momentaufnahme – ein [TERMREF::Snapshot (git)] (dt. Schnappschuss).

Unveränderte Dateien übernimmt git einfach vom vorherigen Commit mithilfe einer Referenz.
So spart git Rechenaufwand und Speicherplatz.

In [PARTREF::git-Funktionsweise] haben wir dies bereits gesehen.
Wer eine Auffrischung braucht, kann sich die Grafiken im Abschnitt
[What is Git?](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)
des *Pro Git Books* anschauen.

Die Staging-Area erlaubt uns auch, Änderungen im Arbeitsverzeichnis rückgängig zu machen, 
indem wir den Zustand einer Datei auf den Stand der Staging-Area zurücksetzen.
Es bietet sich daher an, Dateien zu sinnvollen Zeitpunkten zur Staging-Area hinzuzufügen, 
damit man auf diese gesicherten Zustände zurückgreifen kann.

Trotzdem ersetzt dies kein richtiges Backup: Wirklich langfristig gesichert sind Änderungen erst, 
wenn sie Teil eines Commits geworden sind.

[NOTICE]
Übrigens: Ein Git-Repository sollte generell nicht als Backup betrachtet werden.
Allenfalls, wenn wir unseren lokalen Zustand zusätzlich auf einen entfernten Server gepusht haben.
Nach einem Commit können wir jedoch jederzeit zu dessen Zustand zurückkehren.
Mehr dazu finden Sie später im Abschnitt [PARTREF::git-Fehlerbehebung].
[ENDNOTICE]

Fügen Sie jetzt die Datei `calculator.py` der [TERMREF::Staging-Area] hinzu und prüfen Sie 
erneut den Status.

[EQ] Welche Veränderungen stellen Sie fest?

Inzwischen sollten Sie ein gutes Verständnis davon haben, was Staging-Area/Index, 
Working Directory und Repository Directory sind und wie man Dateien zum Index hinzufügt.

Als nächstes, möchten wir wieder ein bisschen in den theoretischeren Teil eintauchen.
Schauen Sie dazu das Video [Git from the inside out](https://www.youtube.com/watch?v=fCtZWGhQBvo).
Zunächst nur bis 16:08 (Einschließlich des Abschnittes "Each Commit has a Parent").

Das Video gibt es auch in Textform, was vielleicht zum späteren Referenzieren hilfreich sein kann: 
[Git from the inside out](https://maryrosecook.com/blog/post/git-from-the-inside-out).
Wir schauen das Video ca. bis zum Textabschnitt "Check out a commit".

In diesem Video werden einige sehr grundlegende Konzepte aufgegriffen. 
Hierzu ein paar Fragen, die Sie beantworten können sollten, bevor Sie mit der Aufgabe fortfahren:

[EQ] Wie speichert git eine Datei, wenn `git add` ausgeführt wird? (blob object, mit hash name, 
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

Nicht selten wollen wir in git aber nicht nur neue Änderungen hinzufügen und uns ausschließlich 
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