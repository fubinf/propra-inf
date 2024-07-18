title: Git Branches
stage: alpha
timevalue: 2.0
difficulty: 2
assumes: git-Funktionsweise
requires: git-Zweitrepo
---

[SECTION::goal::idea]

Ich verstehe wie Branches in git funktionieren, wann es sinnvoll ist, Branches zu verwenden und 
welche Probleme dabei entstehen können.

[ENDSECTION]

[SECTION::background::default]

Ein in der Praxis sehr wichtiger und nützlicher Aspekt von git sind die sogenannten Branches. 
Wer sich gewundert hat, warum es "Worktree" heißt, wird hier vermutlich einen kleinen aha!-Moment 
haben. Diese bieten uns nämlich verschiedene Möglichkeiten, um unser Projekt zu verwalten,  
Code zu pflegen bzw. einzupflegen. Auch die verteilte Arbeit wird mit Branches deutlich einfacher.

[ENDSECTION]

[SECTION::instructions::detailed]
Zu aller erst sollten wir die Frage klären "Was sind eigentlich Branches?". Ganz vereinfacht lässt 
sich Sagen, dass Branches einfach nur parallel laufende Versionshistorie sind. Sprich man kann 
an zwei vollkommen Verschiedenen Branches gleichzeitig Arbeiten, diese Arbeit commiten und dann 
sogar ins Repo pushen, ohne dass man sich in die Quere kommt. Zwischen Branches hin und her zu 
springen ist aufgrund der Snapshot-basierten Architektur von git gar kein Problem und geht auch 
super schnell.

Wenn wir uns jetzt die technischen Details anschauen, wird es eigentlich sogar gar nicht so viel 
komplizierter. Denn wenn ein Branch erzeugt wird, wird einfach nur eine Datei erzeugt, welche 
den Branchnamen enthält und den Hash des Commits mit dem der Branch "beginnt". 
Wird dieser Branch nun aktiviert, zeigt unser git Pointer/Zeiger auf diesen Commit und alle 
neuen Commits werden darauf aufbauen.
Wechseln wir auf einen anderen Branch, wird der Pointer entsprechend umgesetzt und der Zustand 
des Repositories auf dessen Zustand umgesetzt.

Das klingt jetzt natürlich alles doch etwas komplizierter als gedacht aber spätestens, wenn Sie 
gleich den Abschnitt im git Book lesen und die entsprechenden Grafiken sehen, werden Sie 
merken wie simpel diese ganze Vorgehensweise eigentlich ist und vor allem lernen Sie endlich was 
eigentlich dieses ominöse HEAD bedeutet, was man immer mal wieder beim Arbeiten mit git zu 
Gesicht bekommt.

Lesen wir jetzt also [den Abschnitt über Branches im git-Book](https://git-scm.
com/book/en/v2/Git-Branching-Branches-in-a-Nutshell). 
Schauen Sie sich vor allem die Grafiken genau an, die Zeigen nämlich wunderbar wie git Pointer, 
Branch und Commit zueinander stehen.

Das ist ganz schön viel Stoff daher werden Sie sicherlich noch das ein oder andere Mal im Verlauf 
dieser Aufgabe nachschlagen müssen.

Wenn Sie die Seite durchgelesen haben, öffnen Sie ein Terminal und navigieren Sie in ihr 
Test-Repository welches Sie in der zugehörigen Aufgabe [PARTREF::git-Zweitrepo] erstellt haben.

### Einen neuen Branch erstellen

Stellen wir uns jetzt also folgende Situation vor: 
Wir haben unser Arbeitsrepository. Das haben Sie gerade frisch geklont und jetzt wollen Sie ein 
neues Feature hinzufügen. Im ersten Moment denkt man natürlich "Da fang' ich einfach an 
draufloszuschreiben, erstell dann meinen Commit und push den zurück auf den [TERMREF::Main-Branch]". 
Blöd nur, wenn jetzt eine der folgenden Situationen eintritt:

1. Der Main-Branch ist gesperrt! 
2. Einer ihre_r Kolleg_innen hat gleichzeitig an denselben Dateien wie Sie gearbeitet und 
   nun Änderungen gespusht die mit Ihren Änderungen Kollidieren könnten.

Ersteres ist vermutlich eher nicht der Fall, wenn Sie alleine Arbeiten, gehört aber inzwischen 
häufig beim Arbeiten mit git zum guten Ton. Das ist ganz einfach so, weil häufig die Faustregel 
gilt: "Der Main-Branch muss funktionieren!" sprich, wenn man den Main branch klont und baut, 
dann sollte das einfach alles gehen. Wenn jetzt jeder einfach so Änderungen dort hineinpushen 
kann, dann kann das unweigerlich dazuführen, dass mal aus Versehen Fehler gepusht werden.
Damit das nicht passiert, gibt es auf git Servern wie Github und GitLab Werkzeuge um den 
Main-Branch zu sperren, sodass nur durch sogenannte [TERMREF2::Pull-Request::Pull-Requests], oft 
auch mit PR abgekürzt. Änderungen von anderen Branches in den Main-Branch gemergt (integriert) 
werden können, nachdem Sie getestet und reviewt (gesichtet) wurden.

Zweiteres wird in ihrem Test-Repo auch (noch!) nicht der Fall sein, da Sie sehr wahrscheinlich 
bis hierher nur alleine an einem Repo gearbeitet haben. Ist aber ganz oft der Fall, wenn man mit 
anderen Menschen zusammenarbeitet. 
Um also die möglichen Kollisionen zu minimieren, arbeitet erstmal jeder für sich auf dem eigenen 
Branch, mergt dann nach Fertigstellung der Arbeit seine Änderungen wieder in den Main-Branch 
und löst zu diesem Zeitpunkt ggf. Auftretende Konflikte im eigenen Branch.
Das erspart allen Beteiligten viel Zeit und Schmerz.

Der erste Schritt für beide Situationen ist aber natürlich jetzt erstmal einen neuen Branch zu 
erstellen!

Gehen wir dazu also zurück zu unserem ausgedachten, aber realistischen, Beispielszenario:

Sie wollen ihrer modernen Applikation jetzt ein neues Feature hinzufügen, sagen wir ... 
einen KI-Assistenten. Erstellen Sie also jetzt einen neuen Branch und benennen diesen 
entsprechend (Wie wär's mit "AI-Assistant"?). Anschließend wechseln Sie auf diesen Branch.

[EC] Welche(n) Befehl(e) nutzen wir um einen neuen Branch zu erstellen und auf diesen zu Wechseln?

[NOTICE]
Wir sprechen hier und auch in weiteren Aufgaben meistens vom [TERMREF::Main-Branch]. Ab und zu wird 
allerdings auch mal der Master-Branch referenziert. Das kann durchaus verwirren, falls Sie den 
Glossareintrag noch nicht gelesen haben. Deshalb hier nochmal eine kurze Zusammenfassung:
`master` und `main` branch sind die Standardnamen für den Namen des ersten Branches, welcher beim 
Initialisieren eines Git-Repos erstellt wird. Die meisten Server (GitHub/GitLab/GitTea) benutzen 
`main`. Git selbst benutzt (noch) `master`, verweist allerdings selbst auch darauf, dass der 
Name in Zukunft geändert werden kann.
Funktional unterscheiden sich die beiden, wie alle anderen Branches auch, absolut nicht. Es ist 
schlicht ein Bezeichner.
Wer noch mehr darüber lernen will, wie diese Abweichung zustande kam, kann sich den Blogpost von 
[GitLab](https://about.gitlab.com/blog/2021/03/10/new-git-default-branch-name/) durchlesen, in 
welchem die Thematik ausführlich behandelt wird.
[ENDNOTICE]

### Arbeiten auf einem Branch 

In unserem neuen Branch können wir jetzt ganz wie gewohnt arbeiten. Neue Dateien erstellen oder 
bestehende modifizieren. Auch Commits können wir erstellen und bearbeiten wie wir lustig sind. 
Denn unser neuer Branch unterscheidet sich von der Funktionsweise ja absolut gar nicht vom 
Main-Branch. Der einzige Unterschied ist, dass der Main-Branch der erste von git erstellte 
Branch ist und deswegen immer da ist. Alle Branches verhalten sich aber grundsätzlich gleich.

Ärger können Sie sich sparen, wenn Sie erst den Branch erstellen und dann ihre Änderungen 
vornehmen und commiten. Zur not kann man Commits auch zwischen Branches hin und her schieben, 
aber das ist eher nervig und lässt sich einfach vermeiden.

Erstellen Sie jetzt eine neue Datei in ihrem aktiven AI-Assistant-Branch. Geben Sie dieser einen 
sinnvollen Namen z.B. `assistant.py` und ein paar Zeilen Inhalt. Dann commiten Sie diese Datei auf
ihren neuen Branch und schauen sich mal den `git log` mit Decorations an.

[EC] Welche Kommandos haben Sie für diesen Teilabschnitt verwendet?  
[EC] Wie sieht der Befehl und die Ausgabe von `git log` mit Decorations aus?

### Einpflegen bzw. kombinieren von Änderungen zwischen Branches

Jetzt geht's ans Eingemachte. Und zwar wollen wir jetzt unsere Änderungen von unserem 
AI-Assistant-Branch in den Main-Branch mergen.

Grundsätzlich gibt es hierfür zwei Vorgehensweisen. Das mergen mit `git merge` und das `git 
rebase`. Letzteres ist aber richtig kompliziert und kann einiges kaputt machen, deswegen 
behandeln wir das in einer anderen Aufgabe, damit wir hier nicht komplett den Rahmen sprengen.

Also wollen wir jetzt die folgenden Schritte erledigen:

1. Wir wechseln auf den Main-Branch und aktualisieren diesen mit `git pull`. (Sehr 
   wahrscheinlich wird es keine neuen Änderungen geben, aber hier geht es ja auch darum 
   sogenannte "best practice" also "optimales Vorgehen" zu erlernen)
2. Wir mergen den AI-Assistant-Branch in den Main-Branch.

[EC] Welche Befehle haben Sie für diese beiden Schritte verwendet? Gab es evtl. Probleme dabei? 
Wenn ja, wie haben Sie diese gelöst.

[WARNING]
Man sollte immer(!) vor dem mergen in den Main-Branch diesen nochmal mit `git pull` aktualisieren.
So spart man sich, mal wieder, viel Zeit und Ärger. Es ist nämlich nicht unwahrscheinlich, dass, 
wenn man mit anderen Menschen zusammenarbeitet, jemand schon wieder neue Änderungen dort 
vorgenommen hat.
[ENDWARNING]

### Merge-Konflikte

Beim Arbeiten mit mehreren Branches und der Merge-Methode kann es immer wieder dazu kommen, dass 
man sogenannte Merge-Konflikte (merge-conflicts) verursacht. Diese zu verstehen ist als 
git-Einsteiger überhaupt nicht trivial. Im Grunde geht es dabei aber nur darum, dass es zwei 
Änderungen an der gleichen Datei gibt welche miteinander Konkurrieren, da sie wahrscheinlich den 
gleichen Bereich, sprich die gleichen Zeilen, innerhalb einer Datei verändern sollen.

In unserem Main-Branch des Testrepos befindet sich nun unsere `assitant.py` Datei.

Diese nutzen wir jetzt, um gezielt einen merge-Konflikt zu erzeugen!

- Öffnen Sie die `assistant.py` Datei, schreiben Sie einen Text in die erste Zeile und 
  speichern die Datei. 
- Fügen Sie diese Änderungen einem neuen Commit hinzu.
- Wechseln Sie jetzt zurück in ihren AI-Assistant-Branch und öffnen Sie dort wieder die 
  `assistant.py` Datei und schreiben sie einen anderen(!) Text in die erste Zeile und speichern 
  Sie diese Änderungen.
- Auch hier brauchen wir wieder einen neuen Commit der unsere Änderungen beinhaltet.
- Wechseln Sie jetzt wieder auf den Main-Branch.

Jetzt haben wir alles für unser perfektes Desaster vorbereitet. Wenn wir uns vergewissern wollen, 
können wir noch einmal `git log` mit den Argumenten `--all --decorate --graph --name-only 
--oneline` aufrufen, dann sehen wir schon, dass in beiden Commits die gleiche Datei bearbeitet 
wurde.

Das könnte dann nämlich z.B. so aussehen:

```
* 19a0399 (ai-assistant) changed assistant.py but in a branch
| assistant.py
| * 14f53dd (HEAD -> master) changed assistant.py
|/
|   assistant.py
* 69fa86b added assistant.py
| assistant.py
```

Jetzt lösen wir den Merge-Konflikt aus!

- Mergen Sie nochmal den AI-Assistant-Branch in den Main-Branch.

Wenn die vorherigen Schritte richtig befolgt wurden sollten wir jetzt mit der folgenden 
Nachricht begrüßt werden:

```
Auto-merging assistant.py
CONFLICT (content): Merge conflict in assistant.py
Automatic merge failed; fix conflicts and then commit the result.
```

Also öffnen wir unsere `assistant.py` um uns den Schaden mal genauer anzuschauen:

```
<<<<<<< HEAD
This is old!
=======
This is new!
>>>>>>> ai-assistant
```

Was wir hier jetzt sehen ist wie git uns ermöglicht Merge konflikte aufzulösen.
Über dem `=======` stehen die Änderungen in unserem Main-Branch, darunter die Änderungen aus dem 
AI-Assistant-Branch.
Der simpelste Weg ist jetzt einfach alles zu löschen, was wir nicht haben wollen, die Datei zu 
speichern und dann wieder mit `git add` hinzuzufügen. 
Der Merge-Konflikt wäre damit behoben. 
Allerdings muss natürlich trotzdem noch einmal `git commit` ausgeführt werden, was einem auch von 
`git status` mitgeteilt wird, wenn man es nach `git add` einmal aufruft.
Wer aufmerksam war, hat natürlich auch vorher schon gelesen was beim ursprünglichen Auftreten 
des merge-Konflikts ausgegeben wurde "`fix conflicts and then commit the result.`".

Und jetzt schauen wir uns noch ein letztes Mal den `git log` Graphen an und können jetzt sehr 
schön sehen an welcher Stelle wir die beiden Branches zusammengeführt haben.

```
*   a76ed22 (HEAD -> master) Merge branch 'ai-assistant'
|\
| * 19a0399 (ai-assistant) changed assistant.py but in a branch
| | assistant.py
* | 14f53dd changed assistant.py
|/
|   assistant.py
* 69fa86b added assistant.py
| assistant.py
```

[NOTICE]
Es gibt zum Mergen von branches bzw. zum Beheben von Konflikten auch das sogenannte `git 
mergetool`, das zu erklären würde hier den Rahmen sprengen und ist eher Fortgeschrittenen (vim) 
Nutzer_innen zu empfehlen.

Wer sich trotzdem mal daran versuchen möchte oder einfach nur interessiert ist, findet hier [die 
nötige Dokumentation.](https://git-scm.com/docs/vimdiff/en)
[ENDNOTICE]


### Branches löschen

Wenn wir nun unseren Merge-Konflikt behoben und unsere Änderungen in den Main-Branch gemergt 
haben, können wir unseren Arbeitsbranch löschen.

Hierzu gibt es ein paar nützliche Werkzeuge. 

Zum einen können wir natürlich wieder mit `git log` unsere Commits sehen und auf welchen Branch 
sie angewandt wurden bzw. wo sich aktuell unser `HEAD` befindet.

Andererseits können wir aber auch einfach mit `git branch` prüfen, ob es andere Branches gibt 
die in den aktuell aktiven Branch gemergt wurden. 

[EC] Welches Argument nimmt `git branch` an um anzuzeigen welche Branches bereits in den aktuell 
aktiven Branch gemergt wurden?

Nun da wir ein Kommando haben, welches uns hilft, anzuzeigen welche Branches wir nicht mehr 
brauchen, können wir diese nach dem erfolgreichen Merge auch löschen.

[EC] Welchen Befehl nutzen wir, um nicht mehr benötigte Branches zu löschen?

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Befehle prüfen und schauen ob das mentale Modell vom Branching und die Behebung von 
Merge-Konflikten verstanden wurde]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
