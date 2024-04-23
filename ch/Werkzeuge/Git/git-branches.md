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
gründlich durch.

Für diese Aufgabe erstellen Sie die abzugebenden Dateien *in ihrem neu zu erstellenden Branch* und 
pflegen diese zum Schluss wieder in den Main-Branch ein. Sollten Sie nach dem Einpflegen noch 
änderungen an der abzugebenden Datei vornehmen müssen, so können Sie das auch im Main-Branch machen.

### Erstellen des Branches

- [EC] Geben Sie den Befehl bzw. die Befehle an um einen neuen Branch basierend auf dem 
  Main-Branch zu erstellen und auf diesen zu wechseln.

### Bearbeiten 

- [EC] Erstellen Sie nun ihre Abgabe-Datei, fangen Sie an diese Auszufüllen und commiten diese in 
  ihren neuen Branch.

### Einpflegen

- [EC] Nun pflegen Sie den neuen Branch wieder in ihren Main-Branch ein. Geben Sie alle dazu 
  verwendeten Befehle sowie die verwendete Methode an.

### Git-Log

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
im ProPra repo. Abschließend erstellen Sie eine Ansicht des git-logs aus der die Änderungen und 
wer diese vorgenommen hat ersichtlich werden.

[ENDSECTION]

[INSTRUCTOR::heading]

Prüfen Sie wie die Studierenden vorgegangen sind und welche Befehle verwendet wurden und schauen 
Sie ob der git-log zur Abgabe passt. Er sollte einen neuen Branch zeigen, mindestens einen 
Commit mit der Abgabe und danach wieder in den Main-Branch gemergt werden. 

Der git-log Befehl sollte ungefähr folgendermaßen aussehen:

`git log --oneline --decorate --graph --all --format=%aE`

[ENDINSTRUCTOR]
