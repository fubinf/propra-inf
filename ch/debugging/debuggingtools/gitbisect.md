title: git bisect
stage: draft
timevalue: 1.0
difficulty: 3
profiles:
explains:
assumes:
requires:
---
[SECTION::goal::idea]

- Ich weiß, wie ich mittels `git bisect` prüfe, in welchem vorherigen Commit sich ein Bug eingeschlichen hat.
- Ich verstehe, in welchen Fällen `git bisect` zum Debuggen nützlich ist.
- Ich verstehe, welche Aufgabe `git bisect` beim Debuggen übernimmt.

[ENDSECTION]


[SECTION::instructions::loose]

### Die grundsätzliche Idee

Viele Bugs passieren direkt vor der eigenen Nase.
Allerdings kann es in einigen Fällen sein, dass Commits Funktionalität brechen, die vorher einwandfrei funktioniert hat.
In diesem Fall muss erst einmal herausgefunden werden, _wann_ der Bug in der Commit History passiert ist.
Sollten Sie das Konzept der binären Suche verstanden haben, werden Sie das Vorgehen schnell verstehen:

1. Betrachten Sie die Commit History als einen Zeitstrahl.
2. Wählen Sie den einen Zeitpunkt, an dem der Bug nicht auftritt als Start des Zeitstrahls.
3. Wählen Sie einen Zeitpunkt, an dem der Bug nicht mehr auftritt als Ende des Zeitstrahls. 
4. Wählen Sie den Zeitpunkt, der mittig zwischen Start und Ende liegt:
    - Wenn der Bug in diesem Commit nicht auftritt, ist dies der neue Start.
    - Wenn der Bug in diesem Commit auftritt, ist dies das neue Ende.
5. Wiederholen Sie 4., bis nur noch ein Commit übrig ist.

So einfach das Vorgehen ist, so aufwendig ist es auch händisch durchzuführen.
Wir wären aber nicht Programmierer, wenn wir nicht versuchen würden dieses Vorgehen zu automatisieren.
Eine Möglichkeit hierfür bietet `git bisect`.

### Ihre Aufgabe

Beschäftigen Sie sich mit der Dokumentation von [`git bisect`](https://git-scm.com/docs/git-bisect).


- [EQ] Beschreiben Sie den allgemeinen Ablauf von `git bisect`.
- [EQ] Beschreiben Sie, wie man einen `git bisect`-Prozess startet.
- [EQ] Beschreiben Sie, was die Argumente "good" und "bad" in `git bisect` bedeuten.
- [EQ] Beschreiben Sie, wie ein Skript aussehen muss, anhand dessen `git bisect` automatisiert prüft, 
  ob ein Commit fehlerhaft ist oder nicht. Geben Sie auch an, wie die Rückgabewerte aussehen müssen. 
- [EQ] Geben Sie den Befehl an, mit dem Sie den `git bisect`-Prozess beenden.

TODO_2_pietrak Ein gutes Repo finden, mit dem hier noch eine Praxisaufgabe eingefügt werden kann.

[ENDSECTION]
[SECTION::submission::information]

.

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
