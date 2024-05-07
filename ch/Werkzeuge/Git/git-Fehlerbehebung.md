title: Fehler beheben im git Repository
stage: alpha
timevalue: 2.0
difficulty: 2
assumes: git-Funktionsweise
requires: git-Zweitrepo
---

[SECTION::goal::experience]

Ich lerne verschiedene Fehlerarten für das Arbeiten mit git kennen und wie ich diese behebe.

[ENDSECTION]
[SECTION::background::default]

Im Laufe des Programmierpraktikums und auch danach werden wir mit ziemlich großer Sicherheit 
Fehler beim Bedienen von git machen, daher ist es natürlich hilfreich diese Fehler einfach mal 
in einer kontrollierten Testumgebung zu machen und dabei auch direkt wieder zu lernen wie man 
Sie rückgängig machen bzw. beheben kann.

[ENDSECTION]
[SECTION::instructions::detailed]

Zuallererst lesen wir wieder einmal eine Seite aus dem Git Buch. Diesmal geht es darum wie wir 
[Dinge rückgängig machen](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) können.

[WARNING]
Lesen Sie die Seite gründlich durch! Viele der hier gelernten Befehle können Änderungen 
verursachen, welche **nicht** ohne weiteres rückgängig gemacht werden können.
[ENDWARNING]

Nun machen wir uns daran, das gelesene selbst auszuprobieren.

### Änderungen an einen bestehenden Commit anhängen

Es kann vorkommen, dass wir auch nachdem wir bereits Änderungen an einer Datei einem commit 
hinzugefügt haben, noch weitere Änderungen vornehmen und diese dem gleichen commit hinzufügen 
wollen. Wie das funktioniert lernen wir in dieser Aufgabe.

1. Erstellen sie eine neue Datei namens `amend.md` und fügen sie diese mit `git add` und `git 
   commit` einem neuen Commit hinzu.
2. Nehmen Sie nun weitere Änderungen an der Datei vor.
3. Verwenden sie nun `git commit` und `git log` um diese Änderungen dem vorherigen Commit aus 
   Schritt 1 hinzuzufügen. 

[EC] Mit welchem Befehl haben Sie die Änderungen an den bestehenden Commit angehangen?

### Eine Datei(-änderung) aus einem ungepushten Commit entfernen/unstagen

In bestimmten Situationen kann es auch hilfreicher sein eine Datei einfach aus einem Commit zu 
entfernen, entweder weil wir Sie aus Versehen hinzugefügt haben oder weil wir merken, dass wir 
diese vielleicht doch lieber in einem anderen Commit haben wollen.

1. Legen Sie zwei neue Dateien mit den Namen `add.md` und `remove.md` an und fügen Sie diese mit 
   `git add` und `git commit` einem neuen Commit hinzu.
2. Mit `git show` können wir nun den Inhalt des Commits sehen.
3. Nun wollen wir die datei `remove.md` aus dem Commit entfernen. Wie Sie das anstellen können 
   Sie wieder der verlinkten Quelle entnehmen. 
4. Stellen sie nun mit `git show` sicher, dass der Commit nur die Datei `add.md` enthält.

[EC] Mit welchem Befehl können Sie die Datei `remove.md` aus dem Commit entfernen?

[WARNING]
Seien Sie besonders sicher, wenn Sie sensible Informationen wie Schlüssel in ihrem git repo 
liegen haben (am besten sollte das nie der Fall sein). Diese aus Versehen zu einem Commit 
hinzuzufügen, oder noch schlimmer, zu pushen, kann weitreichende Fatale folgen haben.
[ENDWARNING]

### Änderungen an einer Datei rückgängig machen

Manchmal merken wir, dass wir Änderungen an einer Datei vorgenommen haben die wir eigentlich gar 
nicht brauchen, z.B. eine ungenutzte Funktion hinzugefügt. Wenn, ausser dieser keine weiteren
Änderungen an einer Datei vorgenommen wurden, können wir einfach git benutzen, um die Datei auf 
ihren letzten Snapshot im vorherigen Commit zurückzusetzen.

Dafür benutzen wir in dieser Aufgabe `git reset`

1. Zunächst erstellen wir eine neue Datei namens `reset.md` und fügen diese einem neuen commit 
   hinzu. Mit `git log`, `git show` und `git status` können wir prüfen, ob alles in Ordnung ist.
2. Als Nächstes nehmen wir nun einige Änderungen an der `reset.md` vor und speichern diese. 
3. Schauen wir nun in `git status` sollten wir "untracked changes" dieser Datei sehen.
4. Jetzt geht es darum, diese Änderungen wieder Rückgängig zu machen. Das ganze machen wir mit 
   `git reset`. Welchen Befehl wir genau verwenden müssen, können wir der oben verlinkten Quelle 
   entnehmen bzw. in der manpage (`man git-reset`) nachschlagen.

[EC] Mit welchem Befehl setzen wir die Datei `reset.md` nach Schritt 3 auf den Zustand von 
Schritt 1 zurück?

### Wie man git restore benutzt

Anstelle von git revert lässt sich z.B. für das Wiederherstellen einer Datei auf einen anderen 
Zustand auch git restore benutzen. 

Zuerst werden wir `git restore` nutzen um Änderungen an einer Datei, welche noch nicht commitet 
wurden, rückgängig zu machen.

Dazu gehen wir die folgenden Schritte durch:

1. Wir legen eine neue Datei namens `restore.md` an.
2. Wir commiten diese mithilfe von `git add` und `git commit` und prüfen mit `git status` ob 
   unsere Änderungen korrekt im Repo aufgezeichnet wurden.
3. Jetzt fügen wir ein paar weitere Zeilen der Datei hinzu und prüfen wieder mit `git status` ob 
   unser repo die Änderungen registriert hat. 
4. Nun können wir `git restore` benutzen, um die Datei wieder auf den Zustand von Schritt 2 
   wiederherzustellen.

[EC] Geben Sie den genutzten `git restore`-Befehl an.

Jetzt wollen wir einen Schritt weiter gehen und die Datei vor dem Zurücksetzen sogar commiten.
Dazu machen wir weiter nach Schritt 3 der vorherigen Aufgabe. Die Änderungen sollten jetzt 
uncommited in die Datei geschrieben worden sein.

1. Fügen Sie nun einen neuen commit mit dem neuen Inhalt der Datei hinzu.
2. Nutzen sie nun `git log` bzw. `git reflog` und die manpage für `git restore` (`man git-restore`)
   um herauszufinden, wie Sie mit `git restore` auf den Zustand des Vorherigen commits aus 
   Schritt 2 kommen.

[EC] Wie muss der `git restore`-Befehl aussehen, um eine Datei auf den Zustand des vorherigen 
Commits zurückzusetzen?

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Auf verwendung der korrekten Befehle achten und ]

- [EREFC::1] `git commit --ammend`
- [EREFC::2] `git reset HEAD filename`
- [EREFC::3] `git checkout -- filename`
- [EREFC::4] `git restore filename`
- [EREFC::5] `git restore --source=HEAD~ filename`

[ENDINSTRUCTOR]
