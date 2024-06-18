title: Rebasing in git
stage: alpha
timevalue: 2.0
difficulty: 2
requires: git-Zweitrepo, git-Branches
---

TODO_1_hüster:

- goal: "git rebase benutzen" ist kein sinnvolles Lernziel. 
  Sondern: Was kann ich mit dem hier Gelernten erreichen?
- Die Arbeitsschritte beginnen mit einer rein mechanischen Abfolge von Schritten.
  Wir brauchen aber ein _vom Arbeitszweck_ her verständliches Szenario ("A arbeitet an Auftrag X,
  B zugleich an Y" usw.), damit die Studis verstehen, wozu das alles dient.
- Außerdem brauchen wir semantisch mehr Schärfe.  
  Insbesondere müssen die Studis lernen, die zwei Sichten auf Commits auseinanderzuhalten:
  Commit als Schnappschuss (bezeichnet durch einen Hash) und Commit als Änderungsoperation.
  Die Formulierung "der commit in dem wir rebase-a.md hinzugefügt haben" in der zweiten 
  Bemerkung bezieht sich z.B. auf letztere Sicht und die Angelegenheit wird erst mit ihr
  wirklich verständlich.  
  Dafür dürfen und sollten wir uns viel Zeit nehmen und hilfreiche Verständnisfragen formulieren.  
  Das sollte bei git-Fehlerbehebung los- und hier weitergehen und darf gern dazu führen,
  dass aus diesen zwei Aufgaben drei oder vier oder fünf werden.
- Siehe https://stackoverflow.com/questions/40617288/a-commit-in-git-is-it-a-snapshot-state-image-or-is-it-a-change-diff-patch-delta  
  Dass diese Frage so wenig Views hat und dass so viele Leute bei git nicht durchblicken,
  hat meiner Ansicht nach viel miteinander zu tun.  
  ProPra-Teilnehmer_innen sollen in dieser Hinsicht bitte auf einem hohen Verständnisniveau rauskommen.

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

[SECTION::instructions::detailed]

Wie nach den anderen Aufgaben schon zu erwarten war, fangen wir auch hier wieder mit einem 
Abschnitt aus dem Git Pro Book an. Diesmal geht es natürlich um [git rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing). 
Lesen Sie die verlinkte Seite gründlich durch und arbeiten Sie danach zu zweit die folgende 
Aufgabe durch.

Auch in dieser Aufgabe nutzen wir wieder unser Zweitrepo aus [PARTREF::git-Zweitrepo].

Wichtig ist auch, dass Sie die Aufgabe zu Branches bereits erfolgreich bearbeitet haben, ohne 
diese werden Sie sehr wahrscheinlich schnell aufgeschmissen sein.

- Zuerst klonen beide Übungspartner_innen das Zweitrepo je auf ihren Rechner und arbeiten dann 
  durch die nachfolgenden Schritte. 
- Person A erstellt einen neuen Branch **rebase-a** wechselt hinein und erstellt darin eine 
  neue Datei `rebase-a.md`. 
- Jetzt commiten wir `rebase-a.md` in den Branch **rebase-a** und mergen diesen Branch 
  in den Main-Branch. Zuletzt pushen wir alles auf den git-Server.
- Person B erstellt einen neuen Branch **rebase-b** wechselt hinein und erstellt darin 
  eine neue Datei `rebase-b.md`. Diese wird ebenfalls zu einem neuen Commit hinzugefügt. Kann 
  auch gepusht werden, muss aber nicht.
- Person wechselt jetzt wieder zurück in den main-Branch und führt `git pull` aus um die 
  Änderungen von Person A zu synchronisieren. Öffnet man nun das git-Log, sollte man zuletzt den 
  gemergten Commit von Person A mit der `rebase-a.md` sehen.  

Bis hier hin sollte uns der Prozess einigermaßen bekannt vorkommen, neue Befehle haben wir noch 
nicht genutzt, sondern uns lediglich bei `clone, pull, push, add, commit, branch, checkout` und 
`merge` bedient. Das klingt vielleicht viel, ist aber eigentlich nur die Menge unserer 
alltäglichen Befehle. Zu unserem Werkzeugkasten kommt jetzt aber auch ein neuer Befehl, nämlich 
`git rebase`. Dieser ist äußerst hilfreich, aber auch ein bisschen Angsteinflößend, da man, wenn 
man ohne Bedacht vorgeht, viel kaputt machen kann. 
Wenn man sich aber gut überlegt, was man da eigentlich für Änderungen vornimmt, ist er ganz 
schnell gar nicht mehr so gruselig.

Was wollen wir jetzt eigentlich als nächstes Bewerkstelligen?

Nun, die Änderungen aus **rebase-b** sollten jetzt auch in den Main-Branch eingepflegt 
werden. Allerdings wollen wir jetzt im Gegensatz zu vorher unsere Änderungen mit rebase 
einpflegen und damit die commits direkt in den Main-Branch schreiben anstatt wie bei `git merge` 
einfach einen neuen commit für den merge zu erstellen und somit quasi die "Historie" neu zu 
schreiben. Tun wir dies nicht, wird uns git mit der Aufforderung begrüßen eine nachricht für den 
neuen merge-Commit zu schreiben. 

[NOTICE]
Sollte man etwas übereifrig schon versucht haben **rebase-b** in main zu mergen kann man 
einfach die vorgeschriebene Nachricht löschen und den Editor wieder schließen. Der oder dem 
aufmerksamen Leser_innen sollte das auch schon aufgefallen sein, denn es steht am Ende des 
langen Kommentars im neu geöffneten Editor.
[ENDNOTICE]

Damit das nicht passiert nutzen wir nun also `git rebase`. Wie genau, steht auch in der 
ursprünglich verlinkten Seite.

- [EC] Geben Sie das Kommando an um Branch **rebase-b** auf **main** zu rebasen

[NOTICE]
In der Aufgabe zu Branches haben wir uns schon mal die Graphenansicht für `git log` angeschaut. 
Zur besseren Visualisierung von merging und rebasing kann man auch hier am Ende mal einen Blick auf 
den git log werfen.

Die Ausgabe sollte in etwa so aussehen:

```git
* 1a62513 (HEAD -> master) add rebase-a.md
* 8c841bb (rebase-b) add rebase-b.md
| * 3124383 (rebase-a) add rebase-a.md
|/
* 776de6c better state
* ca4ac0b good state
* 80d0877 added test.md
```

Zum Beispiel stellt sich einem dort auch die Frage, warum taucht eigentlich der commit in dem 
wir "rebase-a.md" hinzugefügt haben zweimal auf, der commit mit "rebase-b.md" aber nur einmal?

Wer diese Frage nicht beantworten kann, liest am besten nochmal den Unterschied zwischen merge 
und rebase und rebase nach!

Dazu kann man sich auch mal die Frage stellen wie unser Graph aussehen würde, wenn man für beide 
Branches `git rebase` verwendet hätte? Oder wie, wenn man die branches jeweils getauscht, also 
`rebase-a` mit rebase und `rebase-b` mit merge eingepflegt hätte?
[ENDNOTICE]

[SECTION::submission::trace]

Geben Sie die eingegebenen git-Befehle von beiden Rechnern ab und beschreiben Sie ihre 
Vorgehensweise und ggf. Probleme, auf welche Sie während dem Bearbeiten der Aufgabe gestoßen sind 
und wie Sie diese gelöst haben.  

[ENDSECTION]

[INSTRUCTOR::Prüfen Sie ob die Studierenden das Prinzip von git rebase verstanden haben, wie man 
rebase nutzt und warum das nützlich ist.]

Prüfen Sie die Vorgehensweise der Studierenden, vor allem beim rebasen von branch b auf den main 
branch.

Im Grunde benötigen die studis zum Lösen der aufgabe einfach nur `git merge rebase-a` und `git 
rebase rebase-b`. Beide Befehle sollten jeweils ohne Probleme durchlaufen.

Wichtig ist, dass verstanden wird, dass beim rebase die commits aus dem branch übertragen werden,
währen bei merge ggf. neue commits erstellt werden. 

Das erklärt auch warum in der Graphenansicht der `rebase-a` Commit zweimal auftaucht, wurde für 
diesen eben beim mergen ein neuer Commit erstellt und `rebase-b` nur einmal, da der commit 
übertragen wurde und somit den gleichen hash hat.
Ändert man die Reihenfolge bzw. die Befehle so ändert sich dann natürlich auch die 
Graphenansicht entsprechend.

[ENDINSTRUCTOR]
