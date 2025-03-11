title: GCC Werkzeugkette auf macOS mit Homebrew
stage: draft
timevalue: 0.5
difficulty: 2
---
[SECTION::goal::product]
Ich habe sichergestellt, dass die GCC Werkzeugkette für C/C++ funktioniert.
[ENDSECTION]

[SECTION::instructions::detailed]
### GCC Werkzeugkette installieren

Installieren sie die GCC Werkzeugkette über Homebrew mittels
`brew install gcc@14`.
Sollte diese Version sich bei Ihnen nicht installieren lassen, so können Sie
auch `gcc@13` bzw. `gcc@12` verwenden.
Da wir mindestens Version 12 benötigen, müssen Sie sich für einen anderen
Rechner entscheiden, sollte auch `gcc@12` sich nicht installieren lassen

### GCC Werkzeugkette prüfen

Rufen Sie `gcc-14 -v` auf, um die C-Compiler-Version zu prüfen.

Rufen Sie `g++-14 -v` auf, um die C++-Compiler-Version zu prüfen.

Haben Sie bei der Installation eine andere Version als 14 verwendet, so passen
Sie die Befehle entsprechend an.

[WARNING]
Wenn künftig von die Befehle `gcc` oder `g++` ausgeführt werden
sollen, so müssen Sie diese auf die von Ihnen hier installierte Version
anpassen.
Tun Sie dies nicht, so rufen Sie anstelle dessen den clang-Compiler
von Apple auf (dieser wurde mit den Xcode Command Line Tools installiert welche
von Homebrew benötigt werden).
GCC und clang führen zwar zum selben Ziel, haben aber andere
Kommandozeilenparameter und Warnungen.
[ENDWARNING]

[INCLUDE::C_CheckCompile.inc]

[SECTION::submission::snippet]
Die Abgabe besteht aus den Ausgaben der `gcc -v` und `g++ -v` Befehle, jeweils
in einer eigenen Datei.
[ENDSECTION]
[ENDSECTION]

[INSTRUCTOR::Warnhinweise]
[INCLUDE::C_InstructorCheck.inc]
[ENDINSTRUCTOR]
