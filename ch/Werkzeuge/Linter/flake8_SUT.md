title: SUT mit flake8 analysieren
stage: draft
timevalue: 0.5
difficulty: 4
explains: Linter
assumes: flake8
requires: LokalesDeployment
---

[SECTION::goal::product]

- Ich kann ein Bestandscode mit Hilfe von flake8 analysieren

[ENDSECTION]
[SECTION::background::default]

Die Übersicht über einen Codeabschnitt zu behalten, ist relativ einfach. Ein unbekanntes Projekt
hingegen zu verinnerlichen, oftmals zeitintensiv und umständlich. Eine gute Praxis ist es daher zu
identifizieren, welche Teile des Codes nicht normiert sind. Wir wollen das einmal mit unserem
Bestandscode `SUT` durchführen.

[ENDSECTION]
[SECTION::instructions::tricky]

- [ER] Analysieren Sie SUT v1.0.0 mit flake8.
- [ER] Analysieren Sie SUT v1.0.0 mit flake8 ohne den Anteil der Unittests
- [ER] Konfigurieren Sie flake8 so, dass bei einer Analyse keine Fehlermeldungen mehr erscheinen.

[WARNING]
Wenn Sie eine virtuelle Umgebung verwenden (venv) und diese sich im Verzeichnis v1.0.0 untergebracht
ist, achten Sie darauf, dieses Verzeichnis auszuschließen.
[ENDWARNING]

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::heading]
Es sollten um die 30 - 40 Meldungen auftauchen.
[ENDINSTRUCTOR]
