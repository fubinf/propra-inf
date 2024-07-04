title: Fehler beheben im git Repository
stage: alpha
timevalue: 2.0
difficulty: 2
assumes: git-Funktionsweise
requires: git-Zweitrepo
---


[SECTION::goal::experience]

Ich kann einige kleine Pannen beheben, wie sie beim Arbeiten mit git oft vorkommen.

[ENDSECTION]
[SECTION::background::default]

Wer arbeitet, macht Fehler; das Arbeiten mit git ist da keine Ausnahme.
Wenn man sich dann schlecht mit git auskennt, ist das oft sofort sehr stressig,
denn man muss für die Korrektur des Fehlers die gewohnten Abläufe verlassen.

Hier probieren wir diese Dinge "im Sandkasten" aus: in einer Extraumgebung, 
mit nur wenig Angst, wertvolle Arbeit zu verlieren.
Hier können Sie lernen, sich nicht wie die 
[armen Git-Stümper_innen](https://stackoverflow.com/questions/40503417/how-can-i-add-a-file-to-the-last-commit-in-git)
zu verhalten, die versehentlich [ihr ganzes Repo](https://stackoverflow.com/questions/66394191/accidentally-deleted-overwrote-local-files-in-git-repo)
oder [ihre letzten Änderungen löschen](https://stackoverflow.com/questions/5788037/recover-from-losing-uncommitted-changes-by-git-reset-hard) 
oder sich durch [fehlende git-Kenntnis mithilfe von ChatGPT ihr Arbeit zerstören](https://stackoverflow.com/questions/75908629/i-mistakenly-deleted-most-of-my-files-with-git-is-there-a-way-to-recover). 
Nur um dann [nochmal umständlich von vorne zu beginnen](https://www.reddit.com/r/git/comments/17kte2s/newbie_screwed_up_and_i_need_to_start_over/).

[ENDSECTION]
[SECTION::instructions::detailed]

In dieser Aufgabe beschäftigen wir uns Hauptsächlich mit der git-book seite darüber [wie wir 
Dinge rückgängig machen können](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things).
Für jede Unteraufgabe lesen wir nur je einen Abschnitt, damit wir inhaltlich leicht folgen können

[WARNING]
Lesen Sie die Abschnitte _gründlich_! Viele der hier gelernten Befehle können Änderungen 
verursachen, welche **nur aufwändig** wieder rückgängig gemacht werden können -- und
manche auch gar nicht.
[ENDWARNING]


### Änderungen an einen bestehenden lokalen Commit anhängen

Es kann vorkommen, dass wir einem schon angefertigten Commit weitere Änderungen hinzufügen 
wollen. Wie das funktioniert, lernen wir in dieser Aufgabe.

Dazu lesen wir zuerst [bis zum Abschnitt "Unstaging a Staged File"](
https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) 
und bearbeiten dann die nachfolgenden Aufgabenteile.

1. Erstellen sie eine minimale neue Datei namens `amend.md` und fügen sie diese mit `git add` und `git 
   commit` einem neuen Commit hinzu.
   (Minimal heißt z.B. nur eine Zeile wie "Ich bin amend.md.". 
   So ähnlich ist das in dieser Aufgabe oft sinnvoll.)

[HINT::"amend.md" schnell und bequem erstellen]
Haben Sie schon die Aufgabe [PARTREF::redirect] bearbeitet?
Danach kennen Sie ein Konstrukt wie `echo 'Ich bin amend.md' > amend.md`,
mit dem das Erstellen einer solchen Minidatei einfacher geht als mit einem Editor.
Aber Vorsicht vor dem versehentlichen Überschreiben!
[ENDHINT]

2. Nehmen Sie nun Änderungen (z.B. eine Zufügung) an der Datei vor.
3. Verwenden sie nun `git commit` und `git log` um diese Änderungen dem vorherigen Commit aus 
   Schritt 1 hinzuzufügen, ohne einen zusätzlichen Commit zu erzeugen. 

[EC] Mit welchem Befehl haben Sie die Änderungen an den bestehenden Commit angehangen?
[EQ] Wird hier wirklich ein bestehender Commit modifiziert? Wenn nein, was passiert stattdessen? 


### Eine Datei(-änderung) aus der Staging-Area entfernen

Nach fertiggestellter Arbeit wollen wir natürlich neue Dateien oder Dateiänderungen in unser 
Repository commiten. Manchmal kann es aber vorkommen, dass man etwas zu voreilig mehrere 
Veränderungen mit `git add` der Staging-Area hinzugefügt hat un dann aber merkt, dass man evtl. 
nur ein Subset darin haben möchte. Zum Glück kann man mit git ganz einfach ungewünschte Dateien 
oder Dateiänderungen wieder aus der Staging-Area entfernen.

Um zu lernen, wie das funktioniert, lesen Sie nun weiter [bis zum Abschnitt "Unmodifying a Modified 
File"](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) und bearbeiten anschließend 
wieder die folgende Aufgabe.

1. Legen Sie zwei neue Dateien mit den Namen `add.md` und `remove.md` an und fügen Sie diese mit 
   `git add` der Staging-Area hinzu. Auch hier möchten wir wieder einen kurzen Text in beiden 
   Dateien haben, z.B. "Ich bin add.md" und "Ich bin remove.md".
2. Mit `git status` können wir nun den aktuellen Status der Staging-Area begutachten.
3. Nun wollen wir die datei `remove.md` aus der Staging-Area entfernen. Wie genau das 
   funktioniert, haben Sie gerade gelesen.
4. Stellen Sie nun mit `git show` sicher, dass die Staging-Area nur die Datei `add.md` enthält.
5. Erstellen Sie nun einen Commit mit der Datei `add.md` und einer sinnvollen Commit-Nachricht 
   und danach einen weiteren Commit der die Datei `remove.md` hinzufügt, ebenfalls mit einer 
   sinnvollen Commit-Nachricht.

[EC] Mit welchen Befehlen können Sie die Datei `remove.md` aus der Staging Area entfernen?

[WARNING]
Geheime Informationen wie Schlüssel oder Passwörter sollte man nie in ein git Repo speichern.
Hat man das doch mal getan und noch nicht gepusht, ist das ein guter Anwendungsfall für 
obige Operation.
Hat man hingegen schon gepusht, wird es richtig aufwändig; dazu mehr später.
[ENDWARNING]

### Änderungen an einer Datei rückgängig machen

Manchmal merken wir, dass wir Änderungen an einer Datei vorgenommen haben die wir eigentlich gar 
nicht brauchen, z.B. eine ungenutzte Funktion hinzugefügt. Wenn, ausser dieser keine weiteren
Änderungen an einer Datei vorgenommen wurden, können wir einfach git benutzen, um die Datei auf 
ihren letzten Snapshot im vorherigen Commit zurückzusetzen.

Um zu Lernen wie das funktioniert, lesen wir jetzt [bis zum Abschnitt "Undoing things with git 
restore"](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things). Und bearbeiten dann wieder die dazugehörige Aufgabe.

1. Erstellen Sie eine neue Datei, mit Inhalt, und nennen Sie sie `checkout.md`.
2. Fügen Sie die Datei einem neuen Commit hinzu.
3. Nehmen Sie nun Änderungen an der datei vor und führen Sie dann `git status` aus um zu 
   verifizieren, dass die Änderungen von git erfasst wurden.
4. Setzen Sie nun die datei auf den Zustand des vorher erzeugten Commits zurück.
5. Vergewissern Sie sich, dass die Datei korrekt zurückgesetzt wurde.

[EC] Mit welchem Befehl haben Sie die bearbeitete Datei zurückgesetzt?

[NOTICE]
In der verlinkten Quelle steht "It tells you pretty explicitly how to discard the changes 
you’ve made. Let’s do what it says". 
In neueren git-Versionen steht in der `git status` Ausgabe nicht mehr "(use "git checkout -- 
<file>..." to discard changes in working directory)", sondern "(use "git restore <file>..." to 
discard changes in working directory)". Falls das bei ihnen steht ist also nichts kaputt, 
sondern Sie haben einfach nur eine neuere Version von git.
[ENDNOTICE]

### Wie man git restore benutzt

Anstelle von `git checkout` lässt sich z.B. für das Wiederherstellen einer Datei auf einen anderen 
Zustand auch `git restore` benutzen. Das sieht ein bisschen eleganter aus, braucht weniger 
Argumente und ist inzwischen in neueren git-Versionen auch zum De-Facto-Standard geworden.
Wenn Sie jetzt bis zum Ende der Seite die verlinkte Quelle lesen, sollten Sie alles gesehen 
haben, was wir für die noch kommenden Aufgaben brauchen.

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

1. Fügen Sie nun einen neuen Commit mit dem neuen Inhalt der Datei hinzu.
2. Nutzen sie nun `git log` und die manpage für `git restore` (`man git-restore` bzw. `git help 
   restore`) um herauszufinden, wie Sie mit `git restore` auf den Zustand des vorherigen Commits aus 
   Schritt 2 kommen.

[EC] Wie muss der `git restore`-Befehl aussehen, um eine Datei auf den Zustand des vorherigen 
Commits zurückzusetzen?
[EQ] Wir setzen mit usneren Befehlen die Datei auf einen vorherigen Zustand zurück, wird damit 
auch der vorherige Commit entfernt?

[WARNING]
Auch wenn es bereits in unserer Quelle steht. Falls Sie es überlesen haben, hier noch einmal, 
weil es so wichtig ist:

> It’s important to understand that git restore <file> is a dangerous command. Any local changes 
> you made to that file are gone — Git just replaced that file with the last staged or committed 
> version. Don’t ever use this command unless you absolutely know that you don’t want those 
> unsaved local changes.

[ENDWARNING]

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Auf verwendung der korrekten Befehle achten und ]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
