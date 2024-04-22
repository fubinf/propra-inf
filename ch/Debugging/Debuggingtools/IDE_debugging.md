title: Debugging mittels IDE
stage: beta
timevalue: 1.0
difficulty: 3
assumes: pdb
---
[SECTION::goal::idea]

- Ich verstehe, was ein Debugger ist.
- Ich kann den Debugger von PyCharm einsetzen, um meinen Code systematisch zu durchlaufen.

[ENDSECTION]
[SECTION::background::default]

Für viele einfache Debugging-Fälle ist [PARTREF::pdb] die handlichste Lösung,
wenn man einen Debugger braucht.
Aber wenn es komplizierter wird, kann eine IDE wesentlich mehr leisten.
Das probieren wir hier aus.

[ENDSECTION]
[SECTION::instructions::loose]

Verwenden Sie für das Folgende
    - die [Debugger-Dokumentation für PyCharm](https://www.jetbrains.com/help/pycharm/debugging-code.html) oder
    - die [Debugger-Dokumentation für VS Code](https://learn.microsoft.com/en-us/visualstudio/python/debugging-python-in-visual-studio)


### Ausprobieren!

Laden Sie das Programm aus der Aufgabe [PARTREF::pdb] in Ihre IDE
und probieren Sie die folgenden Dinge damit aus, während die die Antworten zu 
den folgenden Fragen recherchieren:
 
- [EQ] Wie startet man das Debugging? (Das ist leider gar nicht mal so einfach.)
- [EQ] Was ist ein [TERMREF::Breakpoint] und welche Eigenschaften können Sie daran verändern?
- [EQ] Wie können Sie einen [TERMREF::Breakpoint] zu einem [TERMREF::Conditional Breakpoint] 
  machen?
- Probieren Sie die Funktionen zum Steuern des schrittweisen Programmablaufs
  und die Funktionen zum Erkunden von Datenstrukturen aus.
- [EQ] Was sind Ihrer Einschätzung nach die 10 wichtigsten Funktionen des Debuggers?
- [EQ] Als wie nützlich empfinden Sie den grafischen Debugger?
  Was gefällt Ihnen gut (insbesondere im Vergleich zu [PARTREF::pdb]), was schlecht?

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::???]

TODO_1_pietrak

[ENDINSTRUCTOR]
