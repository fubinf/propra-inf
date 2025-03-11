title: GCC Werkzeugkette auf Linux mit Apt
stage: draft
timevalue: 0.5
difficulty: 2
---
[SECTION::goal::product]
Ich habe sichergestellt, dass die GCC Werkzeugkette für C/C++ funktioniert.
[ENDSECTION]

[SECTION::instructions::detailed]
### GCC Werkzeugkette prüfen

Rufen Sie `gcc -v` auf, um die C-Compiler-Version zu prüfen. Wir brauchen
[mindestens](https://semver.org/) GCC 12.

Rufen Sie `g++ -v` auf, um die C++-Compiler-Version zu prüfen. Diese sollte
identisch mit der Version des C-Compiler sein.

Ist die GCC Werkzeugkette nicht installiert, so holen Sie dies mittels
`sudo apt install build-essential` nach und wiederholen Sie dann die obigen
beiden Tests.

[INCLUDE::C_CheckCompile.inc]

[SECTION::submission::snippet]
Die Abgabe besteht aus den Ausgaben der `gcc -v` und `g++ -v` Befehle, jeweils
in einer eigenen Datei.
[ENDSECTION]
[ENDSECTION]

[INSTRUCTOR::Warnhinweise]
[INCLUDE::C_InstructorCheck.inc]
[ENDINSTRUCTOR]
