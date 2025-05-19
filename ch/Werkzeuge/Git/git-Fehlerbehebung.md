title: Fehler beheben im git Repository
stage: beta
timevalue: 1.0
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

In dieser Aufgabe beschäftigen wir uns hauptsächlich mit der git-Book-Seite 
[2.4 Git Basics: Undoing Things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things),
die davon handelt, wie wir Dinge rückgängig machen können.
Für jede Unteraufgabe lesen wir nur je ein Häppchen davon.

[WARNING]
Lesen Sie die Abschnitte _gründlich_! Viele der hier gelernten Befehle können Änderungen 
verursachen, welche **nur aufwändig** wieder rückgängig gemacht werden können -- und
manche auch gar nicht.
[ENDWARNING]


### Einen bestehenden lokalen Commit mit weiteren Änderungen ergänzen

Es kann vorkommen, dass wir einem schon angefertigten Commit weitere Änderungen hinzufügen 
wollen. Wie das funktioniert, lernen wir in dieser Aufgabe.

Dazu lesen wir zuerst 
bis _vor_ den Abschnitt "Unstaging a Staged File" 
und bearbeiten dann die nachfolgenden Aufgabenteile.

[EC] Erstellen Sie eine minimale neue Datei namens `amend.md` und fügen sie diese mit `git add` und 
`git commit` einem neuen Commit hinzu.
(Minimal heißt z.B. nur eine Zeile wie "Ich bin amend.md.". 
So ähnlich ist das in dieser Aufgabe oft sinnvoll.)

[HINT::"amend.md" schnell und bequem erstellen]
Haben Sie schon die Aufgabe [PARTREF::redirect] bearbeitet?
Danach kennen Sie ein Konstrukt wie `echo 'Ich bin amend.md' > amend.md`,
mit dem das Erstellen einer solchen Minidatei einfacher geht als mit einem Editor.
Aber Vorsicht vor dem versehentlichen Überschreiben!
[ENDHINT]

Nehmen Sie nun Änderungen (z.B. zweite Zeile zufügen) an der Datei vor.

[EC] Verwenden Sie nun das frisch angelesene Wissen, um diese Änderungen dem vorherigen Commit aus 
Schritt 1 hinzuzufügen, ohne einen zusätzlichen Commit zu erzeugen.
(So geht das auch unten weiter: Der Aufgabenschritt setzt frisch Angelesenes einmal ein.)

[EQ] Wird hier wirklich ein bestehender Commit modifiziert? Wenn nein, was passiert stattdessen? 


### Eine Datei(-änderung) aus der Staging-Area entfernen

Manchmal fügt man nach fertiggestellter Arbeit Veränderungen _voreilig_ mit `git add` 
der Staging-Area (dem "Index") hinzu -- und merkt erst dann, dass man nur manche davon committen möchte. 
Auch das ist natürlich lösbar.
Lesen Sie den Abschnitt "Unstaging a Staged File" und tun Sie dann dies:

- Legen Sie zwei neue Dateien mit den Namen `add.md` und `remove.md` an und fügen Sie diese mit 
  `git add` der Staging-Area hinzu. Auch hier möchten wir wieder einen kurzen Text in beiden 
  Dateien haben, z.B. "Ich bin add.md" und "Ich bin remove.md".
- [EC] `git status` zeigt die zwei Zufügungen.
- [EC] Entfernen Sie die Datei `remove.md` aus der Staging-Area.
- [EC] `git status` zeigt für den Index nur noch `add.md`, wogegen `remove.md` nicht mehr von 
  git "getrackt" wird.
- [EC] Erstellen Sie nun einen Commit für `add.md` mit einer sinnvollen Commit-Nachricht. 
- [EC] Nun einen weiteren Commit für `remove.md`, ebenfalls mit einer sinnvollen Commit-Nachricht.
  (Achtung: dies ist nur _ein_ Schritt im Kommandoprotokoll.)


### Änderungen an einer Datei rückgängig machen

Manchmal merken wir, dass wir Änderungen an einer Datei vorgenommen haben die wir eigentlich gar 
nicht brauchen, z.B. eine ungenutzte Funktion hinzugefügt. Wenn, ausser dieser, keine weiteren
Änderungen an einer Datei vorgenommen wurden, können wir einfach git benutzen, um die Datei auf 
ihren letzten Snapshot im vorherigen Commit zurückzusetzen.

Lesen Sie den Abschnitt "Unmodifying a Modified File" und tun Sie dann dies:

- Erstellen Sie eine neue Datei `checkout.md` mit kurzem Inhalt. 
- Committen sie diese.
- Ändern Sie den Inhalt; führen Sie `git status` aus um zu sehen, dass die Änderungen von git erfasst wurden.
- [EC] Setzen Sie die Datei auf den Stand des vorherigen Commits zurück.
- Vergewissern Sie sich, dass die Datei korrekt zurückgesetzt wurde.

[NOTICE]
In neueren git-Versionen steht in der Ausgabe von `git status` nicht mehr 
_"(use "git checkout -- <file>..." to discard changes in working directory)"_, 
wie im Buch (jedenfalls mit Stand 2024-08) noch angegeben, sondern 
_"(use "git restore <file>..." to discard changes in working directory)"_.  
Selbst eine so gute Quelle wie das git-Buch fällt im Laufe der Zeit meist ein wenig hinter 
den aktuellen Stand zurück!
[ENDNOTICE]


### Wie man git restore benutzt

Anstelle von `git checkout` lässt sich z.B. für das Wiederherstellen einer Datei auf einen anderen 
Zustand auch das jüngere Kommando `git restore` benutzen, was einleuchtender und ein wenig einfacher ist. 
Lesen Sie dazu den Abschnitt "Undoing things with git restore".

Wiederholen Sie die obigen fünf Schritte analog, verwenden Sie zum Zurücksetzen aber diesmal
`git restore` anstatt `git checkout`:

- Erstellen Sie eine neue Datei `restore.md` mit kurzem Inhalt. 
- Committen sie diese.
- Ändern Sie den Inhalt; führen Sie `git status` aus um zu sehen, dass die Änderungen von git erfasst wurden.
- [EC] Setzen Sie die Datei mit `git restore` auf den Stand des vorherigen Commits zurück.
- Vergewissern Sie sich, dass die Datei korrekt zurückgesetzt wurde.


### Wie man Änderungen noch _nach_ einem Commit verwirft

Jetzt wollen wir einen Schritt weiter gehen und die Datei vor dem Zurücksetzen auch noch committen.
Dazu machen wir weiter nach Schritt 3 der vorherigen Aufgabe. Die Änderungen sollten jetzt 
uncommited in die Datei geschrieben worden sein.

- Ändern Sie den Inhalt von `restore.md` nochmals und committen Sie ihn.
  Es gibt nun also zwei Commits mit `restore.md`: einen brauchbaren ersten und einen falschen zweiten.
- Nutzen Sie nun `git log` und die manpage für `git restore` (`man git-restore` bzw. `git help restore`),
  um herauszufinden, wie Sie mit `git restore` auf den Zustand des ersten Commits kommen.
- [EC] Führen Sie ein entsprechendes Kommando aus.

[EQ] Wir setzen mit unseren Befehlen die Datei im Arbeitsverzeichnis auf einen vorherigen Zustand zurück.
Was passiert dabei mit dem zweiten Commit?

[WARNING]
Auch, wenn es bereits in unserer Quelle steht, falls Sie es überlesen haben, hier noch einmal, 
weil es so wichtig ist:

> "It’s important to understand that git restore <file> is a dangerous command. Any local changes 
> you made to that file are gone — Git just replaced that file with the last staged or committed 
> version. Don’t ever use this command unless you absolutely know that you don’t want those 
> unsaved local changes."

[ENDWARNING]

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Pfusch zurückweisen]

Kleine Abweichungen sind kein Problem, aber wer ganz andere Dinge getan hat als vorgesehen,
muss nochmal antreten. Das sollte aber vermutlich selten sein.

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
