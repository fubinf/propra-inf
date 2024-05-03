title: "My Little Helpers: gitac - git add+commit by file date"
stage: beta
timevalue: 1.5
difficulty: 3
assumes: m_subprocess
requires: mlh-lsnew
---
[SECTION::goal::experience,product]

- Ich habe ein externes Programm (git) von Python aus eingesetzt.
- Ich habe mir ein Hilfsprogramm gebaut, um nachträgliche commits sinnvoller zu gestalten.

[ENDSECTION]
[SECTION::background::default]

Wenn man an einer kleinen oder mittelgroßen Software arbeitet, fokussiert man oft
nicht nur auf eine einzige Änderung, sondern macht mehrere "zugleich".
Nach einer Weile hat man dann mehrere Dateien geändert, was in git aber auf mehrere
Commits aufgeteilt werden sollte.
Dabei macht man sich meist nicht die Mühe, diesen Commits realistische Zeitstempel
mitzugeben, sondern die Zeitstempel der Commits liegen nur um Sekunden oder Minuten auseinander
am Ende der Arbeitsperiode.

Wäre es nicht hübsch, wenn ein Hilfsprogramm sinnvollere Zeitpunkte in diese Commits schreibt?
Das bauen wir uns jetzt.

[ENDSECTION]
[SECTION::instructions::loose]

### Anforderungen

- Angenommen, wir haben (in dieser Reihenfolge) die Dateien A, B, C, D und E geändert.
  Dabei gehören inhaltlich A und D in einen Commit, B, C und E in einen zweiten.
- [ER] Unser Programm hat folgendes Aufrufformat:   
  `python mlh gitac [-m|--message commit-msg] file...`
- Es macht zunächst `git add` auf die angegebenen Dateien.
- Dann macht es `git commit`, ggf. mit der angegebenen Option.
- Beim Commit wird der Zeitstempel entsprechend der 
  mtime der jüngsten Datei gesetzt.
- Auch diese Aufgabe lässt sehr gut komplett mit der Standardbibliothek lösen;
  sie brauchen keine zusätzlichen Pakete.


### Aufräumen

- [EQ] `mlh gitac` überlappt sich von der Funktionalität her mit `mlh lsnew`.
  Haben Sie diese Überlappung bereits im Code widergespiegelt oder gibt es noch Duplikationen im Code?
  Lagern Sie alle gemeinsamen Teile in ein Hilfsmodul `mlh.utils` aus.

 
### Ausprobieren

- [EQ] Führen Sie beim Testen des Programms Protokoll über die Defekte, die Sie entdecken.
- Testen Sie Ihr Programm entweder auf einem Hilfsrepo oder 
  schreiben Sie das Programm richtig genug, dass es schon beim Testen nur sinnvolle Commits macht,
  oder machen Sie reine Test-Commits mit `git reset` wieder rückgängig.

Führen Sie nach ausreichendem Testen zur Abgabe folgende Kommandos aus:

- [EC] `f=mlh/subcmds/gitac.py; date; ls -l $f; python mlh gitac -m"$f, committed by itself" $f`
- Sie haben das Kommando doch hoffentlich genau verstanden bevor Sie es ausgeführt haben?
- [EC] `git -P show HEAD`

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Testfall prüfen]
Bei korrekter Funktion entspricht der Zeitstempel im `git show` am Ende dem
vom vorherigen `ls` und nicht dem vom anfänglichen `date`.  
Ob das auch bei mehreren Dateien korrekt funktionieren würde, sehen wir so allerdings nicht.
[ENDINSTRUCTOR]
