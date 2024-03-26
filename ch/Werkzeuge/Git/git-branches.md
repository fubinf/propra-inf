title: Git Branches
stage: draft
timevalue: 1.0
difficulty: 1
assumes: git-funktionsweise
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

Um zu verstehen, warum Branches nützlich sind, ist es auch hilfreich sich verschiedene 
Anwendungsfälle von Branches anzusehen: 

1. Feature-Branches. Hier arbeitet der Entwickler auf einer Kopie des Main-Branches 
   und implementiert das gewünschte Feature. Ist das Feature fertig, wird der Code wieder in den 
   Main-Branch eingepflegt.
2. Fix-Branches. Hierbei handelt sich im Grunde auch um Feature-Branches nur, dass hier eben 
   kein Feature, sondern ein Bugfix implementiert wird.
3. Release Branches. Wird eine bestimmte Version erreicht, so ist es oft hilfreich einen Branch 
   für diese Version zu erstellen. Dadurch kann man in Zukunft auf diesen Branch zurückgreifen 
   sollten Änderungen an dem Code dieser Version vornehmen um z.B. Patches oder evtl. auch neue 
   Features zu implementieren.

Natürlich haben wir im ProPra nicht vor eigene Features oder Releases zu bauen, jedoch ist es 
sinnvoll einmal auszuprobieren wie Branches in git funktionieren und wie man die Änderungen aus 
einem Branch wieder in den Main-Branch bekommt.

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

[ENDSECTION]

[SECTION::submission::trace]

Abzugeben ist ein Kommandozeilenlog über das erstellen, bearbeiten und mergen eines git-Branches 
im ProPra repo. Abschließend erstellen Sie eine ansicht des git-logs in der "Tree" Ansicht um zu 
zeigen wie sich die verschiedenen Branches entwickelt haben.

[ENDSECTION]

[INSTRUCTOR::heading]

Prüfen Sie wie die Studierenden vorgegangen sind und welche Befehle verwendet wurden und schauen 
Sie ob der git-log zur Abgabe passt. Er sollte einen neuen Branch zeigen, mindestens einen 
Commit mit der Abgabe und danach wieder in den Main-Branch gemerged werden. 

[ENDINSTRUCTOR]
