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

Damit wir die Befehle nicht einfach nur herunter rattern, arbeiten wir die Inhalte anhand eines 
kleinen Beispielprogramms durch. 
Hierzu schreiben wir ein paar Zeilen für einen hypothetischen Taschenrechner.

Anders als bei den meisten Aufgaben werden Sie für diese ein ganz neues Repo erstellen. 
Das dient in erster Linie dazu, dass Sie weiteres Verständnis aufbauen was in diesem Schritt 
passiert und einmal die Repo-Erstellung selber durchturnen als wie üblich von Tools wie Gitlab 
und Co. abgenommen zu bekommen. 
Dafür erstellen Sie ein neues Verzeichnis, navigieren mit ihrer Kommandozeile dort hinein und 
führen den Befehl `git init` aus. 

In [PARTREF::git-Funktionsweise] haben Sie schon einmal den Befehl `git help` kennengelernt. 
Diesen wollen wir jetzt wieder nutzen um zu lernen wozu `git init` genutzt wird.

[EQ] Was macht der Befehl `git init`? 
Referenzieren Sie hierbei die Git-Hilfe und vor allem die Teile, die Sie verstehen.

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
Als nächstes wollen wir den aktuellen Zustand unseres Repos betrachten. 
Dafür gibt es den Befehl `git status`. 
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

Hier sehen wir jetzt einige neue Informationen. 
Zum einen bekommen wir noch immer "No commits yet" angezeigt. 
Was ja auch stimmt, denn wir haben lediglich eine neue Datei angelegt. 
Zumindest scheint git aber *irgendwas* über diese Datei zu wissen, denn sie wird als "Untracked file" 
angegeben.

Aber weiß git auch, was sich in dieser Datei befindet? 
Die letzte Zeile des git-Status gibt uns einen kleinen Hinweis. 
Git betrachtet den Inhalt einer Datei erst, wenn wir die Datei mit `git add` zum 
Verfolgen ("Tracken") markieren.

#### Git und die Staging-Area

Die staging area, auch Index genannt, ist ein Kernelement der git-Arbeitsweise und bezeichnet eine
Art Zwischenablage.
Sie kommt ständig zum Einsatz, nämlich immer dann, wenn wir dem Repository neue Dateien 
hinzufügen, bestehende Dateien ändern oder bereits vorhandene Dateien löschen wollen.

Wie weiter oben bereits angemerkt, verwenden wir dafür den Befehl `git add`.

Man kann sich die staging area als Pufferzone zwischen dem Arbeitsverzeichnis und dem Repository
vorstellen:
Erst wenn ein neuer git-Commit erstellt wird, werden alle im Index vorgemerkten Dateien dauerhaft in
einem Commit-Objekt gespeichert.

Wichtig ist dabei, sich noch einmal vor Augen zu führen, dass git keine reinen Änderungen speichert,
sondern immer vollständige Abbilder (Snapshots) der jeweils vorgemerkten Dateien.

Die Staging-Area erlaubt uns auch, wie so oft in git, Änderungen im Arbeitsverzeichnis 
rückgängig zu machen, indem wir den Zustand der Datei auf den der Staging-Area zurücksetzen. 
Daher bietet es sich an, öfter mal Dateien an sinnvollen Zeitpunkten der Staging-Area 
hinzuzufügen damit man ggf. auf den dabei gesicherten Zustand zurückgreifen kann.

Trotzdem sollte man das ganze nicht als "Backup" sehen, denn wirklich sicher sind unsere 
Änderungen erst mit einem neuen Commit.

Wer mehr darüber lernen möchte, findet später im Abschnitt [PARTREF::git-Fehlerbehebung] mehr 
praktisches Wissen.

Fügen Sie also jetzt die Datei der [TERMREF::Staging-Area] hinzu und prüfen Sie wieder den Status.
Welche Veränderung stellen Sie fest?

Was die Staging-Area ist und wozu Sie benutzt wird haben Sie gelernt, allerdings hilft es, zum 
Festigen des Verständnisses auch die technische Funktionsweise zumindest einmal betrachtet zu haben.
Lesen Sie dafür den Artikel 
[What really happens when I do git add](https://medium.com/@raffs.os/what-really-happens-when-i-do-git-add-8af29c1ec903).

Dazu ein paar Verständnisfragen:

[EQ] Welche Sorten von git-Objekten gibt es und was speichern die?  

[EQ] Wo speichert git die Metadaten über eine Datei und wo die Inhalte?  

[EQ] Zu welchem Zeitpunkt speichert git welche Daten? Als Zeitpunkt versteht sich hierbei die 
Ausführung eines bestimmten Befehls.

[EQ] Wenn man Änderungen an einer Datei vornimmt, obwohl Sie bereits dem git Index hinzugefügt 
wurde, muss man diese Änderungen wieder dem Index hinzufügen, damit Sie im Commit landen?

Wir sollten jetzt Verständnis dafür haben, was der git-Index ist, was Objekte sind, welche 
Objekttypen es gibt und was passiert, wenn wir mit `git add` eine Datei zum Index hinzufügen.
Außerdem haben wir noch einmal `git help` genutzt um zu lernen was ein Befehl tut und wie man 
ihn benutzt.

Um wieder einmal den Kreis zu unseren mentalen Modellen zu schließen sollten wir jetzt 
verstanden haben, dass beim Benutzen von `git add` Schnappschüsse der referenzierten Dateien 
angelegt und diese dann mit `git commit` zu einem Commit-Objekt mit entsprechenden Zeigern 
auf diese Snappschussobjekte (blobs) geschnürt werden.


### Veränderung feststellen

Schauen wir uns einen neuen sehr nützlichen Befehl an, nämlich `git diff`.
Und was tut der? Rufen Sie doch nochmal die Dokumentation zum Befehl auf.

Das ist richtig viel Stoff!
Das meiste davon interessiert uns aber noch gar nicht.

Trotzdem gibt es nützliche Informationen in der Hilfeseite. 
Schauen Sie doch mal in den Abschnitt *EXAMPLES*.

Mit unserem bisherigen Wissen aus der Aufgabe sollten wir auch schon einigermaßen verstehen 
können was im ersten Beispielblock passiert. 

[EQ] Führen Sie `git diff` aus. Was stellen Sie fest?

Erweitern wir nun unsere Additionsfunktion:

```python
# Ein einfacher Rechner
def addiere(a, b):
    # Diese Funktion addiert zwei Zahlen
    return a + b

```

[EQ] Führen Sie noch einmal `git diff aus`. Was stellen Sie jetzt fest?

[EQ] Git speichert nur Snapshots der Dateien, wie erzeugt es denn die `git diff` Ausgabe?

Als wir das letzte bzw. erste Mal `git status` ausgeführt haben, gab es keine wirklich nützlichen 
Informationen zurück.
Führen Sie den Befehl noch einmal aus und lesen Sie gründlich die Ausgabe.

[EQ] Was hat sich seitdem verändert?

`git status` sollte ihnen jetzt außerdem einige Befehle zum Verwalten der Dateien im Index anbieten.

[EQ] Welche Befehle sind das und was tun sie? Geben Sie kurze Erklärungen an.
(Wenn Sie einen Befehl nicht kennen, denken Sie an `git help`)

Fügen Sie die Änderungen an der datei `calculator.py` ebenfalls der Staging-Area hinzu.
Erinnern Sie sich daran, was wir im vorherigen Abschnitt über git-Objekte gelernt haben und 
wie `git add` funktioniert.

[EQ] Könnten Sie jetzt nochmal zum vorherigen Zustand der Datei zurückkehren? 

Als Letztes erstellen Sie wieder einen neuen Commit mit einer sinnvollen Commit-Nachricht.

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

Schauen Sie sich also wieder die Beispiele in der `git diff` Dokumentation und probieren Sie 
folgende Szenarios durch:

[EC] Vergleichen Sie den aktuellen Zustand der Datei mit den bereits vorgemerkten Änderungen.

[EC] Vergleichen Sie die vorgemerkten Änderungen mit dem letzten Commit-Zustand.

[EC] Vergleichen Sie den aktuellen mit dem letzten Commit-Zustand.

Jetzt, wo wir unsere Multiplikation vollständig implementiert haben, wollen wir wieder den 
aktuellen Zustand festhalten. 
Fügen Sie die verbleibenden Änderungen dem Index hinzu und erstellen Sie wieder einen Commit mit 
sinnvoller Nachricht. 

Damit sind wir an dieser Stelle mit dem Großteil der Aufgabe fertig. 

### Git-Historie

Nicht selten wollen wir in Git aber nicht nur neue Änderungen hinzufügen und uns ausschließlich 
Vorwärts bewegen, sondern oft auch in die Vergangenheit schauen.
Vielleicht, um einen alten Zustand zu betrachten und ggf. auch wiederherzustellen oder einfach nur 
um zu prüfen, was wir aktuell für Commits im Repository haben.

Dazu schauen wir uns in diesem Abschnitt noch kurz den Befehl `git log` an.

`git log` ist praktisch unser Git-Tagebuch. Hier werden alle Commits festgehalten. 
Das ist insofern nützlich, als es uns ermöglicht, die Commit-Historie durchzusehen. 
So können wir nachvollziehen, was Commits verändert haben, und ihre Hash-Namen ermitteln. 
Mit diesen Hash-Namen können wir dann entweder den gesamten Working Tree oder einzelne Dateien 
auf den Zustand eines bestimmten Commits zurücksetzen.

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
in der `git log` Doku nachlesen. 
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
