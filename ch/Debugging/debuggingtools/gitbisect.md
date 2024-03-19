title: git bisect
stage: alpha
timevalue: 1.0
difficulty: 3
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

- Legen Sie das Dokument `gitbisect.md` an.
- Fügen Sie in diesem Dokument die Überschrift `Wie funktioniert git bisect?` ein.
- [EQ] Beschreiben Sie den allgemeinen Ablauf von `git bisect`.
- [EQ] Beschreiben Sie, wie man einen `git bisect`-Prozess startet.
- [EQ] Beschreiben Sie, was die Argumente "good" und "bad" in `git bisect` bedeuten.
- [EQ] Beschreiben Sie, wie ein Skript aussehen muss, anhand dessen `git bisect` automatisiert prüft, 
  ob ein Commit fehlerhaft ist oder nicht. Geben Sie auch an, wie die Rückgabewerte aussehen müssen. 
- [EQ] Gibt es einen Befehl in `git bisect`, der ohne ein zusätzliches Test-Skript automatisiert
  Ihre Commits prüfen kann?
  Wenn ja, wie lautet er?
  Welche Voraussetzung muss dafür gegeben sein?
- [EQ] Geben Sie den Befehl an, mit dem Sie den `git bisect`-Prozess beenden.
- [EQ] Überlegen Sie: Sie könnten auch einfach so den Defekt reparieren und die Commit History 
  ignorieren.
  Warum kann es aber nützlich mittels `git bisect` herauszufinden, *wann* der Defekt eingetreten ist?

Als Nächstes versuchen wir `git bisect` an einem Beispiel-Repo einzusetzen.

- Klonen Sie [dieses Repo](https://github.com/takluyver/bisect-demo).
- In dem Repo befinden sich zwei Dateien:
  - ein Python-Skript, `squares.py`, welches als Eingabe eine Zahl bekommt und diese quadriert
  - und ein Bash-Skript, `breakme.sh`, welches eine git-History für uns erstellt.
- Wechseln Sie im Terminal in das Verzeichnis des Repos.
- Fügen Sie in `gitbisect.md` eine weitere Überschrift ein, `Übung`.
  Fügen Sie die folgenden Arbeitsschritte unter dieser Überschrift ein.
- [EC] Vergewissern Sie sich, dass der Aufruf `python squares.py 2` das richtige Ergebnis liefert.
- Führen Sie das Skript `breakme.sh` aus. 
- [EC] Vergewissern Sie sich, dass der Aufruf `python squares.py 2` jetzt nicht mehr funktioniert.
- [EC] Starten Sie den `git bisect`-Prozess.
- [EC] Wählen Sie als "good commit" den Hash `312c137` aus (das ist der Commit bevor sie 
  `breakme.sh` benutzt haben).
- [EC] Wählen Sie als "bad commit" `HEAD` aus.
- [EC] Führen Sie den `git bisect`-Prozess automatisiert aus.
- [EQ] Welche der beiden Möglichkeiten zur Automatisierung haben Sie gewählt? Begründen Sie.
- [EC] Sie haben nun den fehlerhaften Commit gefunden.
  Beenden Sie den `git bisect`-Prozess.
- [EQ] Wie würde jetzt das weitere Vorgehen aussehen?

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::heading]

Wenn `git bisect` nicht automatisiert benutzt worden ist, zurückweisen.

[ENDINSTRUCTOR]
