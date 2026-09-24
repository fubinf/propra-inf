title: Code automatisch formatieren mit black
stage: alpha
timevalue: 1.0
difficulty: 2
explains: Codeformatierer
assumes: venv, git-Branches
requires: flake8
---

[SECTION::goal::experience]

Ich kann meinen Python-Code mit `black` automatisch formatieren und das Ergebnis beurteilen.

Ich verstehe, warum `flake8` nach `black` nicht still ist, und kann die beiden Werkzeuge
aufeinander abstimmen.

Ich habe darüber reflektiert, ob ich lieber selektiv von Hand oder vollständig automatisch korrigiere.

[ENDSECTION]
[SECTION::background::default]

Ein [TERMREF::Linter] wie `flake8` meldet Probleme, lässt den Code aber unverändert.
Ein [TERMREF::Codeformatierer] wie `black` meldet nichts, sondern schreibt das Layout des Codes
(Leerzeichen, Zeilenumbrüche, Anführungszeichen, Klammern) einfach nach festen Regeln um.
`black` bietet dabei absichtlich kaum Einstellmöglichkeiten:
Wer es benutzt, soll nicht mehr über Formatierungsfragen nachdenken oder im Team diskutieren müssen.

[ENDSECTION]
[SECTION::instructions::detailed]

### Die Fassung vor `flake8` wiederherstellen

Wir verwenden denselben Code wie in [PARTREF::flake8],
und zwar in der Fassung _vor_ Ihren dortigen Korrekturen.
Damit Ihre Korrekturen erhalten bleiben, arbeiten wir auf einem eigenen Branch.

- [EC] `git log --oneline -10`
- Suchen Sie darin den Commit mit Ihren `flake8`-Korrekturen.
  Dessen Vorgänger ist die gesuchte Fassung.
- [EC] `git switch -c black-versuch <commit>`, wobei Sie für `<commit>` die Kennung des
  Vorgänger-Commits einsetzen.

[HINT::Ich finde den Commit mit den `flake8`-Korrekturen nicht]
Das ist der Commit, den Sie in [PARTREF::flake8] direkt vor `git show HEAD` gemacht haben.
Falls Sie seitdem nichts mehr eingecheckt haben, können Sie einfach `HEAD~1` als `<commit>` benutzen.
Mit `git show <commit>` können Sie nachsehen, ob Sie den richtigen erwischt haben.
[ENDHINT]

- [EC] Rufen Sie `flake8 --count --statistics` für dieselben Dateien auf wie in [PARTREF::flake8]
  (ohne Ihre dortige Konfiguration mit `--ignore` oder `--select`).
  `--statistics` zeigt am Ende, wie oft jeder Meldungstyp vorkommt.

[HINT::Ich habe in der Aufgabe `flake8` einen Alias oder eine Shellfunktion namens `flake8` angelegt]
Dann ruft `flake8` Ihre gefilterte Konfiguration auf, und Sie sehen hier nicht alle Meldungen.
Umgehen Sie den Alias bzw. die Shellfunktion, indem Sie `command flake8 ...` statt `flake8 ...` schreiben.
Das gilt auch für alle weiteren `flake8`-Aufrufe in dieser Aufgabe.
[ENDHINT]

<!-- time estimate: 10 min -->


### `black` anwenden

- [EC] Installieren Sie `black` in Ihrer virtuellen Umgebung mit `pip install black`.
- [EC] Wenden Sie `black` auf dieselben Dateien an.
  Die Dateien werden dabei direkt überschrieben.
- [EC] `git diff --stat`
- Sehen Sie sich mit `git diff` (nicht im Kommandoprotokoll) an, was `black` verändert hat.
- [EQ] Hat `black` etwas Wichtiges verschlechtert?
  Achten Sie besonders auf Kommentare und auf Stellen, die Sie absichtlich besonders ausgerichtet hatten
  (z.B. tabellenartige Listen oder Dictionaries).
- [EQ] Nennen Sie zwei Stellen, an denen Ihnen das Ergebnis gut gefällt oder zumindest akzeptabel ist,
  und (falls vorhanden) eine, an der es Ihnen nicht gefällt.
  Warum?

[HINT::`black` hat eine Stelle verschlechtert, die ich so behalten will]
Mit Kommentaren wie `# fmt: skip` oder `# fmt: off`/`# fmt: on` lässt sich `black` stellenweise abschalten,
siehe
[Ignoring sections](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#ignoring-sections).
Für diese Aufgabe ist das aber nicht nötig.
[ENDHINT]

- [EC] `git commit -am "black angewendet"`

<!-- time estimate: 15 min -->


### `flake8` erneut anwenden

Jetzt ist der Code sauber formatiert, also müsste `flake8` doch still sein?

- [EC] Rufen Sie `flake8 --count --statistics` wie oben erneut auf.
- [EQ] Welche Meldungstypen sind im Vergleich zum ersten Aufruf verschwunden,
  welche sind geblieben?

Die verbliebenen Meldungen haben zwei verschiedene Ursachen:

**Kategorie a)**: Die Meldung betrifft etwas, das `black` nicht anfasst.
Das sind vor allem Dinge jenseits des Layouts, z.B. ungenutzte Importe, Variablennamen
oder die Programmlogik, aber auch einige Layoutfragen, die `black` bewusst in Ruhe lässt,
etwa den Inhalt von Kommentaren und String-Literalen.

**Kategorie b)**: Die Meldung betrifft das Layout, aber `flake8` erwartet ein anderes Format
als das, was `black` standardmäßig erzeugt.

- [EQ] Ordnen Sie jeden verbliebenen Meldungstyp (Code und Kurztext) einer der beiden Kategorien zu.
  Nutzen Sie dafür die
  [Meldungscodes von flake8](https://flake8.pycqa.org/en/latest/user/error-codes.html)
  und die
  [Meldungscodes von pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes).

[HINT::Ich weiß nicht, wie ich einen Meldungstyp einordnen soll]
Fragen Sie sich: Würde die Meldung verschwinden, wenn man nur Leerzeichen und Zeilenumbrüche ändert?
Und würde `black` genau diese Änderung von sich aus vornehmen, nur eben anders als `flake8` es will?
Dann gehört sie zu Kategorie b), sonst zu a).
Für Kategorie b) lohnt sich ein Blick in den Abschnitt
[Line length](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#line-length)
der Beschreibung des `black`-Codestils:
Welche maximale Zeilenlänge benutzt `black`, welche `flake8`?
[ENDHINT]

<!-- time estimate: 15 min -->


### `black` und `flake8` aufeinander abstimmen

Wir versuchen nun, die Meldungen aus Kategorie b) loszuwerden, indem wir `black` passend einstellen.
Damit die Einstellung nicht bei jedem Aufruf neu angegeben werden muss, legen wir sie in einer
Konfigurationsdatei ab.

- Lesen Sie in
  [Configuration via a file](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file)
  nach, wie man `black` über eine Datei `pyproject.toml` konfiguriert.
  Die verfügbaren Optionen stehen weiter oben auf derselben Seite unter
  [Command line options](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#command-line-options).
- [ER] Legen Sie im Wurzelverzeichnis Ihres Projekts eine `pyproject.toml` mit einem Abschnitt
  `[tool.black]` an, in dem Sie die Zeilenlänge auf den Wert einstellen, den `flake8` erwartet.
- [EC] Wenden Sie `black` erneut auf dieselben Dateien an (ohne Optionen).
- [EC] Rufen Sie `flake8 --count --statistics` erneut auf.
- [EQ] Welche Meldungen aus Kategorie b) sind verschwunden, welche nicht?
  Warum lässt sich nicht jede `E501`-Meldung durch `black` beseitigen?

[HINT::Es sind immer noch `E501`-Meldungen da]
Schauen Sie sich die betreffenden Zeilen an.
Was steht dort, das `black` nicht umbrechen kann, ohne die Bedeutung des Programms zu ändern?
[ENDHINT]

Manche Meldungen aus Kategorie b), z.B. `E203`, erzeugt `black` absichtlich und lässt sich davon
auch durch keine Einstellung abbringen.
Hier muss man stattdessen `flake8` anpassen.

- Lesen Sie den Abschnitt
  [flake8](https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html#flake8)
  in der `black`-Dokumentation.
- [EQ] Warum hält die `black`-Dokumentation die Meldung `E203` für falsch?
- Die `black`-Dokumentation geht bei der Zeilenlänge den umgekehrten Weg als wir:
  Sie empfiehlt, `flake8` mit `max-line-length = 88` an `black` anzupassen.
  Wir haben stattdessen `black` auf die 79 Zeichen eingestellt, die [TERMREF::PEP8] vorsieht.
- [EQ] Welchen der beiden Wege finden Sie besser? Warum?
- [EC] Rufen Sie `flake8 --count --statistics` nun mit der dort empfohlenen Option `--extend-ignore`
  auf (die Zeilenlänge haben Sie ja schon in `black` angepasst).
  Jetzt sollten nur noch Meldungen aus Kategorie a) übrig sein.

[HINT::Bei mir kam gar keine `E203`-Meldung vor]
`E203` entsteht nur bei bestimmten Slices wie `liste[start + 1 :]`.
Falls Ihr Code so etwas nicht enthält, beantworten Sie die Frage trotzdem anhand der Dokumentation.
[ENDHINT]

<!-- time estimate: 15 min -->


### Reflexion

- [EQ] In [PARTREF::flake8] haben Sie selektiv von Hand korrigiert, hier hat `black` alles auf einmal
  automatisch umformatiert.
  Welches Vorgehen würden Sie für ein eigenes Projekt wählen, welches für ein Teamprojekt?
  Warum?
- Ihr Hauptbranch bleibt von alledem unberührt.
  Mit `git switch -` kommen Sie dorthin zurück.

<!-- time estimate: 5 min -->

[ENDSECTION]
[SECTION::submission::reflection,trace,snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
(Damit ist die `pyproject.toml` gemeint.)

[ENDSECTION]
[INSTRUCTOR::Kategorien a) und b) sauber getrennt?]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
