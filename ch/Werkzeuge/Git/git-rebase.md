title: Rebasing in git
stage: alpha
timevalue: 1.0
difficulty: 2
requires: git-Zweitrepo, git-Branches
---

[SECTION::goal::experience]

Wir lernen und verstehen wie wir `git rebase` benutzen und in welchen Situationen man `git 
rebase` z.B. `git merge` gegenüber bevorzugt. 

[ENDSECTION]

[SECTION::background::default]

In der Aufgabe zu git branching haben wir bereits gelernt wie wir Änderungen über verschiedene 
Branches vornehmen und einpflegen. Bisher haben wir jedoch ausschließlich mit `git merge` 
gearbeitet, dabei gibt es noch ein weiteres Werkzeug für das Arbeiten mit verschiedenen Branches.
Aber auch innerhalb eines einzelnen Branches kann `git rebase` nützlich sein, wenn wir z.B. 
mehrere commit zusammenfassen möchten oder die Commit-Nachrichten anpassen wollen. 

[ENDSECTION]

[SECTION::instructions::loose]

Wie nach den anderen Aufgaben schon zu erwarten war, fangen wir auch hier wieder mit einem 
Abschnitt aus dem Git Pro Book an. Diesmal geht es natürlich um [git rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing). 
Lesen Sie die verlinkte Seite gründlich durch und arbeiten Sie danach zu zweit die folgende 
Aufgabe durch.

- Klonen Sie beide das neu erstellte Repository (nicht das ProPra-Repo mit ihren Abgaben!) auf 
ihren Rechner.
- In diesem neuen Repository erstellen Sie nun einen neuen Branch **rebase-task-a** und darin eine 
neue Datei. Name und inhalt sind dabei egal, im Nachfolgenden werden wir Sie der Einfachheit 
halber **REBASE-A.md** nennen.
- Jetzt erstellen Sie auf dem zweiten Rechner ebenfalls einen neuen Branch **rebase-task-b** und 
auch darin eine neue Datei, diesmal **REBASE-B.md**. Auch in diese Datei schreiben Sie etwas hinein.
- Als Nächstes wird der **rebase-task-a** Branch inklusive der Datei commitet und auf den Remote 
  gepusht und in den main branch gemergt.
- Die Änderungen auf **rebase-task-b** werden jetzt ebenfalls commitet. Jetzt kommt allerdings 
  der etwas kniffligere Teil, da wir nun die Änderungen von **rebase-task-b** auf den neuen main 
  branch rebasen wollen.
- Zum Schluss gehen wir sicher, dass sowohl **REBASE-A.mb** als auch **REBASE-B.md** im main 
  branch existieren und *kein* merge-Commit für die Änderungen vom **rebase-task-b** Branch 
  entstanden ist.

[SECTION::submission::trace]

Geben Sie die eingegebenen git-Befehle von beiden Rechnern ab und beschreiben Sie ihre 
Vorgehensweise und ggf. Probleme, auf welche Sie während dem Bearbeiten der Aufgabe gestoßen sind 
und wie Sie diese gelöst haben.  

[ENDSECTION]

[INSTRUCTOR::heading]

Prüfen Sie die Vorgehensweise der Studierenden, vor allem beim rebasen von branch b auf den main 
branch.

[ENDINSTRUCTOR]
