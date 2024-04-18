title: Git ignore
stage: beta
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::idea]

- Ich verstehe, warum eine `.gitignore`-Datei wichtig ist und wie sie funktioniert.
- Ich habe mir eine sinnvolle `.gitignore`-Datei angelegt.

[ENDSECTION]
[SECTION::background::default]

Manchmal gibt es bestimmte Dateien oder Verzeichnisse welche man zwar lokal in seinem git 
repository allerdings nicht im Remote oder anderweitig aufgezeichnet haben möchte. Dafür gibt es 
eine sogenannte `.gitignore`-Datei. Wie man diese Verwendet werden wir in dieser Aufgabe lernen.

[ENDSECTION]
[SECTION::instructions::loose]

Lesen Sie den Abschnitt "Ignoring Files" auf dieser Seite: 
[HREF::https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository]

- Erstellen Sie eine erste `.gitignore`-Datei für ihr ProPra-Repository
  auf Basis dessen, was `git status` als "untracked" meldet, dass Sie aber
  (voraussichtlich) nie werden einchecken wollen.
  Verallgemeinern Sie dabei ggf. hin zu sinnvollen Dateinamen-Mustern.
- Machen Sie einen Commit mit dieser Datei.
- [EC] `git show HEAD`
- Bei GitHub gibt es eine umfangreiche Vorlage für eine 
  [.gitignore für Python-Projekte](https://github.com/github/gitignore/blob/main/Python.gitignore),
  mehr als 150 Zeilen!
  Von dort können Sie im Laufe des ProPra nach und nach immer mal wieder Einträge abgucken und
  übernehmen, denn wir benutzen ein paar der dort behandelten technischen Bausteine.
- [EQ] Jetzt klären Sie bitte durch Recherche die Bedeutung der Einträge
  `__pycache__/` und `*.py[cod]` und erklären Sie sie mit je einem Satz.
  (Das zweite Muster betrifft _drei_ Arten von Dateien.)
- Übernehmen Sie davon alles, was für Ihren Fall sinnvoll erscheint, in Ihre `.gitignore`.
- Machen Sie einen Commit mit dieser Datei.
- [EC] `git show HEAD`
- Falls Sie PyCharm verwenden: Ganz unten in der Python-Vorlage ist eine
  JetBrains-IDEA-Vorlage erwähnt, die für PyCharm relevante Einträge enthält:
  [HREF::https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore].
- Oder falls Sie VS Code verwenden: Analysieren Sie analog
  [HREF::https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore]
- [EQ] Recherchieren Sie, was die Einträge bis Zeile 20 darin bedeuten.
  Welche davon sollten Sie übernehmen? 
  Erklären Sie nur deren Bedeutung in je einem Satz. 
- Fügen Sie diese Einträge Ihrem `.gitignore` zu.
- Machen Sie einen Commit mit dieser Datei.
- [EC] `git show HEAD`

[ENDSECTION]
[SECTION::submission::program,trace]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Einträge sinnvoll?]
Prüfen Sie die Sinnhaftigkeit des Inhalts der `.gitignore`-Datei.
Insbesondere:
    - Es sollten nicht Einzeldateinamen aufgeführt sein, wo Wildcards sinnvoll wären.
    - Es sollten nicht voreilig Dinge ausgeschlossen werden, für die (noch) gar kein Anlass besteht.
    - Für PyCharm und VS Code sollte man normalerweise den "user-specific stuff" ignorieren,
      aber da beim ProPra ja nur eine Person mit dem Repo arbeitet, könnte man das auch
      bleiben lassen. (Tutor_innen dürfen an dieser Stelle einwenden, dass sie ebenfalls
      mit dem Repo arbeiten; das mag ein Grund für einen Nachbesserungswunsch sein, 
      mit oder ohne Ablehnung der Einreichung.)
    - Die Studis müssen (ungefähr) erklären können, was die Dateien bedeuten, die sie 
      ausgeschlossen haben. Das ist ziemlich aufwändig, aber Blindflug ist unzulässig.
[ENDINSTRUCTOR]
