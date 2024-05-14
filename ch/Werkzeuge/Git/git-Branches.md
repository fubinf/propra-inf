title: Git Branches
stage: alpha
timevalue: 1.0
difficulty: 1
assumes: git-Funktionsweise
requires: git-Zweitrepo
---

[SECTION::goal::idea]

Ich verstehe wie Branches in git funktionieren, wann es sinnvoll ist Branches zu verwenden und 
welche Probleme dabei entstehen können.

[ENDSECTION]

[SECTION::background::default]

Ein in der Praxis sehr wichtiger und nützlicher Aspekt von git sind die sogenannten Branches. 
Wer sich gewundert hat, warum es "Worktree" heißt, wird hier vermutlich einen kleinen aha!-Moment 
haben. Diese bieten uns nämlich verschiedene Möglichkeiten, um unser Projekt zu verwalten,  
Code zu pflegen bzw. einzupflegen. Auch die verteilte Arbeit wird mit Branches etwas einfacher.

Im Allgemeinen unterscheidet man zwischen kurz- und langlebigen Branches. Um zu verstehen, warum 
Branches nützlich sind, ist es auch hilfreich sich verschiedene Anwendungsfälle von Branches 
anzusehen.

1. Feature-Branches. Hier arbeitet der Entwickler auf einer Kopie des Main-Branches 
   und implementiert das geplante Feature. Ist das Feature fertig, wird der Code wieder in den 
   Main-Branch eingepflegt.
2. Fix-Branches. Hierbei handelt sich im Grunde auch um Feature-Branches nur, dass hier eben 
   kein Feature, sondern ein Bugfix implementiert wird. Sowohl bei Feature- als auch bei 
   Fix-Branches handelt es sich um kurzlebige/short-lived bzw. sogenannte "Topic" Branches.
3. Release Branches. Wird eine bestimmte Version erreicht, so ist es oft hilfreich einen Branch 
   für diese Version zu erstellen. Dadurch kann man in Zukunft auf diesen Branch zurückgreifen 
   sollten Änderungen an dem Code dieser Version vornehmen um z.B. Patches oder evtl. auch neue 
   Features zu implementieren. Diese Art von Branch fällt unter die Kategorie der 
   langlebigen/long-lived Branches.

Natürlich haben wir im ProPra nicht vor eigene Features oder Releases zu bauen, jedoch ist es 
sinnvoll einmal auszuprobieren wie Branches in git funktionieren und wie man die Änderungen aus 
einem Branch wieder in den Main-Branch bekommt.

Weitere Informationen zu dem Thema "Branching Workflows" findet man [unter dem gleichnamigen 
Thema im Git-Book](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows).

[ENDSECTION]

[SECTION::instructions::detailed]

Lesen Sie die [Git-Book Seite zu Git Branches](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) 
gründlich durch und bearbeiten Sie dann die folgenden Aufgaben. Nutzen Sie dafür ihr Zweitrepo 
was sie in [PARTREF::git-Zweitrepo] erstellt haben.

### Erstellen des Branches

Zuerst müssen wir den neuen Branch erstellen. Standardmäßig befinden wir uns auf dem Main oder 
Master-Branch, dieser ist jedoch in vielen öffentlichen bzw. größeren Projekten gesperrt bzw. 
geschützt. Geschützt deshalb, weil man oft davon ausgeht, dass dieser Branch problemlos 
funktionieren sollte. Zwar könnten wir lokal Änderungen an diesem Branch vornehmen, allerdings 
würden wir spätestens beim pushen auf den git-Server Probleme bekommen. Ein anderer Grund für 
eigene Branches kann auch schlichtweg sein, dass man über längere Zeit an einem eigenen Feature 
arbeiten und sich nicht mit dem ständigen updaten herumschlagen möchte. Oder aber man möchte 
eine bestimmte Version festhalten.
In jedem Fall bietet uns git jedoch einfache Mittel um unsere eigenen Branches zu erstellen und 
zwischen diesen hin und her zu wechseln.
Fangen wir nun also damit an. In fast allen Teilen dieser Aufgabe werden wir `git branch` bzw. 
`git checkout` verwenden. Es bietet sich also an von beiden Befehlen mal die Dokumentation bzw. 
man-page aufzurufen. 

Erstellen Sie nun einen neuen Branch basierend auf dem Main-Branch ihres Test-Repositories und 
wechseln Sie auf diesen. Nennen Sie ihren Branch "propra-git-branches". Grundsätzlich ist es 
durchaus zu empfehlen Branches bezeichnende Namen zu geben, unter denen man sich auch einfach 
etwas vorstellen kann. Das hilft vor allem Ihnen selbst. 

- [EC] Welche Befehle haben Sie verwendet um den neuen Branch zu erstellen?

### Bearbeiten 

In unserem neuen Branch können wir ganz wie gewohnt arbeiten. Neue Dateien erstellen oder 
bestehende modifizieren. Auch commits können wir erstellen und bearbeiten wie wir lustig sind. 
Es ist nicht anzuraten die Historie *vor* dem Startpunkt des erstellten Branches zu modifizieren, 
ist es zwar grundsätzlich sowieso nicht, aber hier noch viel weniger da das einpflegen in andere 
Branches dadurch nur noch viel, viel komplizierter wird.

Nun da wir das geklärt haben, können wir eine neue Datei erstellen, nennen wir sie `branches.md` 
und erstellen wir einen neuen Commit der diese beinhaltet.

- [EC] Welche Befehle haben Sie hier verwendet?

### Einpflegen

Einer der häufigsten, und durchaus nicht einfachen, Arbeitswege ist von einem Branch Änderungen 
wieder in den Main-Branch einzupflegen. Das wollen wir hier einmal üben.

Dafür gibt es im Grunde zwei Wege. Der eine verwendet den sogenannten "merge" Ansatz, diesen 
werden wir hier verwenden. In einem extra Kapitel schauen wir uns jedoch noch `git rebase` an. 
Das ist etwas komplizierter, erzielt aber meistens viel schönere Ergebnisse. Warum das so ist 
erfahren wir auch dort, es lohnt sich also auf jeden Fall auch diesen Teil anzuschauen!

Nutzen wir jetzt also `git merge` um unsere Änderungen in den Main-Branch einzupflegen.

- [EC] Nennen Sie alle Befehle, in der richtigen Reihenfolge, um ihre Änderungen bzw. commits 
  vom Branch "propra-git-branches" in den Main bzw. Master-Branch einzupflegen.

- [EQ] Worauf sollte man nach dem erneuten wechsel auf den Main-Branch und *vor* dem 
Einpflegen des anderen Branches besonders achten?

[HINT::Was könnte Probleme beim Mergen in den Main-Branch verursachen?]
Es kann sein, dass ein anderer Projektteilnehmer auf den git-Server in der Zwischenzeit neue 
Commits in den Main-Branch gepusht hat. Wie kann man hier Konflikte bzw. Probleme beim pushen 
vermeiden?
[ENDHINT]

### Git-Log

Ein sehr nützliches Tool zum Prüfen und Visualisieren der verschiedenen Branches ist `git log`. 
Grundsätzlich liefert dieser Befehl beim Ausführen einfach nur eine Liste *aller* Commits des 
aktuell ausgecheckten Branches und deren Hashes und Commit-Nachrichten. Allerdings kann man auch 
entsprechende Optionen anhängen, um sich einen schicken Graphen ausgeben zu lassen.

- [EC] Erstellen Sie eine Ausgabe des git-log Befehls aus der ersichtlich wird, dass der Branch 
  erstellt, bearbeitet und wieder eingepflegt wurde. Sorgen Sie außerdem dafür, dass die Ausgabe 
  auch zeigt *von wem* die Änderungen vorgenommen wurden.  

[HINT::Ausgabe des git-log Befehls]
Falls Sie Probleme haben die Ausgabe des Befehls anzupassen, schauen Sie doch mal in die 
man-page für `git-log`.
[ENDNOTICE]

[ENDSECTION]

[SECTION::submission::trace]

Abzugeben ist ein Kommandozeilenlog über das Erstellen, Bearbeiten und Mergen eines git-Branches 
in ihrem Zweitrepo. Abschließend erstellen Sie eine Ansicht des git-logs aus der die Änderungen und 
wer diese vorgenommen hat ersichtlich werden.

[ENDSECTION]

[INSTRUCTOR::Befehle prüfen und schauen ob das mentale Modell vom Branching verstanden wurde]

Prüfen Sie die abgegeben Kommandologs.

Der neue Branch sollte mit [EREFC::1] `git branch` erstellt und mit `git checkout` 
ausgecheckt werden. Danach wird mit [EREFC::2] `git add` und `git commit` der neue Commit 
erstellt und schlussendlich mit [EREFC::3] `git merge` wieder in Main gemergt.

[EREFQ::1] Natürlich sollte man Main zuerst mit `git pull` auf den aktuellen Stand bringen bevor 
die Änderungen eingepflegt werden weil es sonst zu ganz unangenehmen Problemen kommen kann wenn 
in der Zwischenzeit Änderungen auf dem Server bzw. Main-Branch gegeben hat.

[EREFC::4] Der git-log Befehl sollte ungefähr folgendermaßen aussehen:

`git log --oneline --decorate --graph --all`

[ENDINSTRUCTOR]
