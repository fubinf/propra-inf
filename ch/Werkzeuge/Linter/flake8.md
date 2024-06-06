title: Linting mit flake8
stage: beta
timevalue: 1.5
difficulty: 3
explains: Linter
assumes: venv, Shell-Grundlagen
requires: PEP8
---

[SECTION::goal::trial]

Ich kann mit `flake8` Probleme in meinem Python-Code identifizieren
und kann das Werkzeug so konfigurieren, dass unnötige Meldungen ausbleiben.

Ich habe darüber reflektiert, ob ich in Bezug auf diese Probleme ein eher gründlicher
Mensch bin oder eher nicht.

Ich habe eine wichtige Merkwürdigkeit vieler Bibliotheks-Dokumentationen verstanden.

[ENDSECTION]
[SECTION::background::default]

In der Softwareentwicklung ist es wichtig, [TERMREF::Linter]-Werkzeuge einzusetzen, um eine hohe
**Codequalität** zu gewährleisten. Durch die kontinuierliche Überprüfung auf **Syntaxfehler** und
potenzielle Fehler hilft flake8 Entwicklern, Probleme frühzeitig im Entwicklungsprozess zu erkennen
und zu beheben, was letztendlich zu **stabileren** und zuverlässigeren Anwendungen führt.
zusätzlich trägt die Einhaltung von **Coding-Standards**, die flake8 ermöglicht, zur Schaffung von
konsistent formatiertem Code bei, was die **Lesbarkeit** erhöht und die **Wartbarkeit** erleichtert.

Diese erwähnten Eigenschaften sind für ein Softwareprojekt wichtig, weshalb flake8 in einem Python
Projekt eine gute Möglichkeit bietet, diese Ziele zu erreichen.

[ENDSECTION]
[SECTION::instructions::loose]

### `flake8`-Überblick

- [EQ] Angenommen, Sie wüssten nichts darüber, wozu `flake8` dient.
  Durchsuchen Sie den Text der Homepage (und nur der Homepage) der
  [flake8-Dokumentation](https://flake8.pycqa.org/en/latest/index.html)
  nach Information über den Zweck des Werkzeugs.
  Was wissen Sie nun? Ist das zufriedenstellend?
- [EQ] Ah, da ist auch eine [FAQ-Seite](https://flake8.pycqa.org/en/latest/faq.html)
  (Frequently Asked Questions). Versuchen Sie das Gleiche dort.
  Was wissen Sie nun? Ist das zufriedenstellend?
- Das ist keine gute Dokumentation. Leider ist genau dieses Phänomen ein verbreitetes Problem.
- [EQ] Etwas mehr Information findet man schließlich auf der dritten Seite:
  [Glossary of Terms](https://flake8.pycqa.org/en/latest/glossary.html).
  Dort sind nämlich drei andere Werkzeuge genannt, die `flake8` benutzt, um seine Leistungen zu 
  erbringen. Welche drei sind das? (Bitte auf gleiche Reihenfolge achten.)
- [EQ] Wo steht die Dokumentation von Werkzeug 1? Welchen Zweck hat es?
  (Sie können den Zweck mit einem kurzen wörtlichen Zitat angeben oder selbst paraphrasieren.)
- [EQ] Was haben Sie auf der Dokuseite von Werkzeug 1 über `flake8` gelernt, 
  das Sie von der `flake8`-Doku-Homepage noch nicht wussten? 
- [EQ] Wo steht die Dokumentation von Werkzeug 2? Welchen Zweck hat es?
- [EQ] Wo steht die Dokumentation von Werkzeug 3? Welchen Zweck hat es?
- [EQ] Was haben Sie auf der Dokuseite von Werkzeug 3 über dessen Zweck _nicht_ gelernt, 
  das Sie von der wenigen Information im `flake8`-Glossar schon wussten? 


### `flake8` aufrufen

- [EC] Installieren Sie `flake8`.
- [EC] Rufen Sie es für den größten zusammenhängenden Satz von Python-Quellcode-Dateien auf,
  den Sie im Rahmen des ProPra geschrieben haben (oder, mit nur einem Aufruf, für die zwei größten 
  Einzeldateien).


### Code bereinigen

Sichten Sie die erhaltenen Meldungen.

- [ER] Wählen Sie einen Meldungstyp aus, für den Ihnen Ihr Code verbesserungswürdig erscheint,
  und korrigieren Sie den Code zu allen oder mindestens 10 der entsprechenden Meldungen (nur dieses
  einen Meldungstyps, nicht aller) so, dass die Meldung verschwindet.  
  (Ziehen Sie die [Liste der Meldungscodes von flake8](https://flake8.pycqa.org/en/latest/user/error-codes.html)
  und [von pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes)
  heran, um die Natur und Bedeutung der Meldungen zu verstehen.)
- [EQ] Macht Ihnen dieses Verbessern Freude oder fühlt es sich eher nach Frohnarbeit an? Warum?
- [EQ] Wäre das für andere der erhaltenen Meldungstypen anders? Für welche zwei oder mehr wäre es erfreulicher?
  (Bitte deren Meldungstext angeben.)
  Für welche zwei oder mehr wäre es lästiger? Warum?
- Auch, wenn man einen Meldungstyp grundsätzlich beachtenswert findet:
  Manchmal gibt es gute Gründe, den Programmcode so zu lassen, wie er ist.
  Dann kann man durch einen geeignet formatierten Kommentar auf der betreffenden Zeile
  die Meldung zum Verschwinden bringen, ohne den eigentlichen Programmcode zu verändern.
- [ER] Lernen Sie unter 
  ["In-line Ignoring Errors"](https://flake8.pycqa.org/en/latest/user/violations.html#in-line-ignoring-errors),
  wie das geht und führen Sie es probehalber mindestens zweimal für zwei verschiedene Meldungstypen
  auf Ihrem Code aus.
- Checken Sie Ihren überarbeiteten Code ein.
- Es sollten jetzt trotzdem noch eine ganze Reihe Meldungen übrig sein.
- [EC] `git show HEAD` (das zeigt also die Korrekturen, die Sie an Ihrem Code gemacht haben.)


### `flake8` konfigurieren

Wir konfigurieren nun das Werkzeug so, dass die Liste der Meldungen Ihnen angemessener erscheint.

- Lesen Sie nach, wie man 
  [Meldungstypen ein- oder ausschaltet](https://flake8.pycqa.org/en/latest/user/violations.html)
- Wenn Sie der eher gründliche Typ sind, wählen Sie mit `--ignore` Meldungstypen aus, 
  die Sie für wenig hilfreich halten und abschalten wollen.
- Wenn Sie eher faul oder eher vorwärtsstürmend sind, wählen Sie mit `--select` Meldungstypen aus,
  die Sie als einzige beibehalten wollen.
- [EC] Wiederholen Sie damit den vorherigen Aufruf.
- [EQ] Damit sollte die Meldungsliste jetzt wesentlich verdaulicher aussehen.
  Kommt für Sie infrage, eine gründliche Bereinigung Ihres Codes mit dieser oder einer weiter
  verfeinerten Liste von Meldungstypen regelmäßig vorzunehmen, sei es immer vor dem Einchecken
  oder zumindest periodisch in größeren Abständen? Warum?
- Heben Sie diese `flake8`-Konfiguration auf, z.B. indem Sie für den Aufruf einen
  passenden [TERMREF::Alias] oder eine [TERMREF::Shellfunktion] anlegen.
- Falls Ihnen das wenig verlockend erscheint: in Ihrer IDE geht das Gleiche wesentlich
  komfortabler, siehe die Aufgabe [PARTREF::Linting-PyCharm].

[ENDSECTION]
[SECTION::submission::reflection,trace,snippet]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
(Damit ist der gemäß der `flake8`-Meldungen modifizierte Code gemeint.)

[ENDSECTION]
[INSTRUCTOR::Eine recht ganzheitliche Aufgabe...]

[INCLUDE::/_include/Instructor-veraltete-Dokumentation.md]
[INCLUDE::ALT:]

[ENDINSTRUCTOR]