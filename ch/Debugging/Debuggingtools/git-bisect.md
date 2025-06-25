title: git bisect
stage: beta
timevalue: 1.0
difficulty: 3
assumes: m_pytest
---
[SECTION::goal::idea]

- Ich kann mit Unterstützung von `git bisect` herausfinden, in welchem vorherigen Commit sich ein
  Defekt eingeschlichen hat.
- Ich kann sowohl mit dem halbautomatischen als auch mit dem automatischen Modus von `bisect` umgehen.
[ENDSECTION]

[SECTION::background::default]
Stellen Sie sich vor, **Ihre Codebasis hat eine Million Zeilen Code**.
Und nun entdecken Sie ein [TERMREF::Versagen], das offenbar nichts mit dem zu tun hat,
woran Sie zuletzt gearbeitet haben, sondern der [TERMREF::Defekt] muss schon länger
in der Codebasis schlummern.

Wenn man eine gute Versionshistorie hat, kann man die benutzen, um den Defekt einzukreisen, 
indem man einen automatisierten Test schreibt, der das Versagen zeigt,
und dann den ältesten Commit X sucht, bei dem das Versagen auftritt.
Beim letzten Commit vor X ist das jetzt defekte Verhalten also noch intakt.
Dann müsste doch Commit X den Defekt eingefügt haben?

Die Bestimmung von X kann man teilweise oder sogar komplett automatisieren.
Dazu dient `git bisect`.
[ENDSECTION]

[SECTION::instructions::loose]

### Verstehen

Beschäftigen Sie sich mit der [Dokumentation von `git bisect`](https://git-scm.com/docs/git-bisect).
Lesen Sie die ersten zwei Abschnitte (zu "start", "good", "bad" und "reset"), bis Sie 
das Grundprinzip von `git bisect` verstanden haben.
Überfliegen Sie den Rest der Seite (Überschriften) für den Fall, dass Sie noch Wissen
nachtanken müssen.

[EQ] Warum muss man `git bisect reset` von Hand machen, statt das `git bisect` es automatisch tut,
sobald die Suche erfolgreich war?

[EQ] Angenommen, Sie kennen den Defekt schon und könnten ihn direkt reparieren.
Warum kann es trotzdem hilfreich sein, den Commit zu finden, der den Defekt eingefügt hat?
Nennen Sie zwei denkbare Gründe.


### Anwenden

Nun setzen `git bisect` an einem Beispiel-Repo selber praktisch ein.
Klonen Sie 
[HREF::https://github.com/takluyver/bisect-demo]
in Ihren [TERMREF::Hilfsbereich] und wechseln Sie in dessen Arbeitsverzeichnis.

[EC] Führen Sie den im README beschriebenen Prozess aus und liefern Sie das Ergebnis
als Kommandoprotokoll ab.

[NOTICE]

- Wenn `my-first-code` nicht existiert, setzen Sie als Ersatz den Hash des betreffenden
  (allerersten) Commits ein: `1cc68ddf`.
- Verwenden Sie im zweiten Teil `pytest`, nicht `py.test`, denn das ist keine heute mehr übliche
  Schreibweise (des ansonsten gleichwertigen Kommandos).
  Wenn beides nicht funktioniert, machen Sie `pip install pytest`.
[ENDNOTICE]

Im wirklichen Leben geht der bisect-Prozess leider meist nicht ganz so einfach.
Es kommt zum Beispiel vor, dass der Test bei manchen Commits nicht lauffähig ist,
ohne dass das mit dem Defekt zu tun hat.

[EQ] Welches Subkommando von `git bisect` hilft im manuellen Modus, ggf. mit solchen
nicht auswertbaren Commit-Ständen umzugehen?

Aber es kommt noch schlimmer: Auch Ihre Ausführungsumgebung kann schuld sein,
dass sich manche Commit-Stände nicht testen lassen, z.B. wenn eine Aufgabe,
die heute von der Bibliothek `y` übernommen wird, in genügend alten früheren Ständen
von der Bibliothek `x` abgedeckt wurde, die heute bei Ihnen nicht mehr installiert ist.

Das klingt schon für den manuellen `bisect`-Modus recht unangenehm,
wie schwierig muss es erst sein, dass mit einem automatisierten Testskript zu bewältigen?
Glücklicherweise brauchen wir die Vollautomatisierung meistens gar nicht!

Nehmen Sie an, der defekteinfügende Commit liegt 666 Commits weit in der Vergangenheit.
Der letzte bekannte "good" Commit ist 800-900 Commits weit in der Vergangenheit. 
Sie brauchen für jeden manuellen Prüfschritt 2 Minuten (weil Sie manchmal Bibliotheken
uminstallieren müssen).

[EQ] Wie lange dauert es mit bisect schlimmstenfalls, den defekten Commit zu finden?

[NOTICE]
Diese Aufgabe ist nur eine zielstrebige Einführung in *eine* Funktion von git.
Wenn Sie sich mehr mit git auseinandersetzen wollen, werden Sie in 
der Aufgabengruppe [PARTREFMANUAL::Git::Werkzeuge/Git] fündig!
[ENDNOTICE]
[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::F4 zeigt ggf. die Ahnungslosigkeit auf]
[INCLUDE::ALT:]
[PROT::ALT:git-bisect.prot]
[ENDINSTRUCTOR]
