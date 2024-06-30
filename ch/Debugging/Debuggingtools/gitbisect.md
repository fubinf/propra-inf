title: git bisect
stage: beta
timevalue: 1.0
difficulty: 3
---
[SECTION::goal::idea]

- Ich weiß, wie ich mittels `git bisect` prüfe, in welchem vorherigen Commit sich ein Bug eingeschlichen hat.
- Ich verstehe, in welchen Fällen `git bisect` zum Debuggen nützlich ist.
- Ich verstehe, welche Aufgabe `git bisect` beim Debuggen übernimmt.

[ENDSECTION]

[SECTION::background::default]

Stellen Sie sich vor, **Ihre Codebasis hat eine Million Zeilen Code**.
Und nun entdecken Sie ein [TERMREF::Versagen], das offenbar nichts mit dem zu tun hat,
woran Sie zuletzt gearbeitet haben, sondern der [TERMREF::Defekt] muss schon länger
in der Codebasis schlummern.

Wenn man eine gute Versionshistorie hat, kann man die benutzen, um den Defekt einzukreisen, 
indem man einen automatisierten Test schreibt, der das Versagen zeigt,
und dann den jüngsten Commit X sucht, bei dem das Versagen auftritt.
Beim letzten Commit vor X ist das jetzt defekte Verhalten also noch intakt.
Dann müsste doch Commit X den Defekt enthalten?

Und wenn in jedem Commit nur wenig geändert wird, ist ein Defekt innerhalb 
dieser Änderungen viel leichter zu lokalisieren als in der Codebasis insgesamt.

Das ist die Grundidee von `git bisect`, das wir in dieser Aufgabe kennenlernen wollen.

Leider ist "automatisierter Test" in diesem Zusammenhang viel schwieriger als es klingt,
denn die Codebasis ist ja bei jedem Commit anders (und bei sehr alten Commits sehr anders).
Außerdem gibt es Commits, die keinen konsistenten Zustand bieten, den man überhaupt sinnvoll
testen kann.
Deshalb ist der Test in vielen Fällen dann doch manuell.

[ENDSECTION]
[SECTION::instructions::loose]

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

[NOTICE]
Diese Aufgabe ist nur eine sehr zielstrebige Einführung in *eine* Funktion von git.
Wenn Sie sich mehr mit dem Programm auseinandersetzen wollen, werden Sie in 
[PARTREFTITLE::Git] fündig!
[ENDNOTICE]

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::bisect bitte!]

Wenn `git bisect` nicht automatisiert benutzt worden ist, zurückweisen.

[ENDINSTRUCTOR]
